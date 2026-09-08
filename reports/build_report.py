#!/usr/bin/env python3
"""Build the standalone report from canonical repository records.

Requires Python-Markdown and Beautiful Soup. KaTeX 0.16.22 is bundled in the
output under its MIT license; the complete upstream notice is embedded.
No source documents are modified and no network requests are made.
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter
import hashlib
import html
import json
import os
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

import markdown
from markdown.extensions.toc import slugify as markdown_slugify
from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
STATUSES = {"PROVED", "SKETCH", "CONJECTURE", "REFUTED"}
SOURCE_ALIASES = {"briefs/problem-first-r8.md": "HANDOFF.md"}
CODE = re.compile(
    r"(?m)^[ \t]{0,3}(?P<fence>`{3,}|~{3,})[^\n]*\n"
    r".*?^[ \t]{0,3}(?P=fence)[`~]*[ \t]*(?=\n|$)"
    r"|(?P<ticks>`+)(?!`)[\s\S]*?(?<!`)(?P=ticks)(?!`)", re.DOTALL
)
MATH = re.compile(
    r"(?<!\\)\\\[[\s\S]*?\\\]"
    r"|(?<!\\)\\\([\s\S]*?\\\)"
    r"|(?<![\\$])\$\$[\s\S]*?\$\$(?!\$)"
    r"|(?<![\w\\$])\$(?![\s$])(?:\\.|[^$\n]|\n(?!\n))*?"
    r"(?<![\s\\])\$(?![\w$])"
)
ALLOWED_TAGS = {
    "a", "abbr", "b", "blockquote", "br", "caption", "code", "col", "colgroup",
    "dd", "del", "details", "div", "dl", "dt", "em", "figcaption", "figure",
    "h1", "h2", "h3", "h4", "h5", "h6", "hr", "i", "img", "kbd", "li",
    "ol", "p", "pre", "s", "samp", "small", "span", "strong", "sub", "summary",
    "sup", "table", "tbody", "td", "th", "thead", "tfoot", "tr", "ul", "var",
}
REMOVE_TAGS = {
    "script", "style", "iframe", "object", "embed", "link", "meta", "base",
    "form", "input", "button", "textarea", "select", "video", "audio", "source",
    "track", "svg", "math", "canvas",
}
ALLOWED_ATTRS = {"id", "class", "title", "alt", "colspan", "rowspan", "scope", "start", "open"}
RASTER_MIMES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp"}


def fail(message: str) -> None:
    raise ValueError(message)


def local_path(path: str, base: str = "") -> Path | None:
    raw = unquote(urlsplit(path).path)
    if urlsplit(path).scheme or raw.startswith("//"):
        return None
    for candidate in [(ROOT / base).parent / raw, ROOT / raw.lstrip("/")]:
        candidate = candidate.resolve()
        if candidate.is_relative_to(ROOT) and candidate.is_file():
            return candidate
    return None


def data_image(path: Path) -> str:
    mime = RASTER_MIMES.get(path.suffix.lower())
    if not mime:
        fail(f"Unsupported automatic image type: {path}")
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def sanitize(fragment: str, source_path: str) -> str:
    soup = BeautifulSoup(fragment, "html.parser")
    for comment in soup.find_all(string=lambda x: isinstance(x, Comment)):
        comment.extract()
    for tag in list(soup.find_all(True)):
        if tag.name is None:
            continue
        if tag.name in REMOVE_TAGS:
            tag.decompose()
            continue
        if tag.name not in ALLOWED_TAGS:
            tag.unwrap()
            continue
        if tag.name == "img":
            src = str(tag.get("src", ""))
            target = local_path(src, source_path)
            if target and target.suffix.lower() in RASTER_MIMES:
                tag["src"] = data_image(target)
            elif re.match(r"^data:image/(?:png|jpeg|gif|webp);base64,[A-Za-z0-9+/=]+$", src):
                pass
            else:
                replacement = soup.new_tag("span")
                replacement.string = "[Image: " + str(tag.get("alt") or src or "omitted image") + "]"
                if urlsplit(src).scheme in {"https", "http"}:
                    link = soup.new_tag("a", href=src)
                    link.string = "Open the external image"
                    replacement.append(" ")
                    replacement.append(link)
                tag.replace_with(replacement)
                continue
        for attr in list(tag.attrs):
            if attr not in ALLOWED_ATTRS and not (tag.name == "a" and attr == "href") and not (tag.name == "img" and attr == "src"):
                del tag[attr]
        if tag.name == "a":
            href = str(tag.get("href", ""))
            if source_path == "seed/analysis-2026-09-01/referee/round2.md" and href.startswith("/tmp/") and href.endswith("/scratchpad/report.md"):
                # The seed preserves its original scratchpad backlink; point the
                # rendered copy at the same report as imported into this repo.
                href = "seed/analysis-2026-09-01/report.md"
                tag["href"] = href
            scheme = urlsplit(href).scheme.lower()
            if scheme and scheme not in {"https", "http", "mailto"} or href.startswith("//"):
                tag.attrs.pop("href", None)
            elif scheme in {"https", "http"}:
                tag["target"] = "_blank"
                tag["rel"] = "noopener noreferrer"
    return str(soup)


def render_markdown(text: str, source_path: str) -> str:
    """Protect TeX before Markdown can consume backslashes or underscores.

    Code fences and inline code remain untouched and are ignored by KaTeX.
    Stashed TeX is HTML-escaped, so formula contents cannot introduce markup.
    """
    stashed: list[str] = []
    stashed_tex: list[str] = []

    def protect(part: str) -> str:
        def replace(match: re.Match) -> str:
            token = f"QAAGMATHSTASH{len(stashed):08d}END"
            stashed.append('<span class="math-source">' + html.escape(match[0]) + "</span>")
            stashed_tex.append(match[0])
            return token
        return MATH.sub(replace, part)

    pieces, cursor = [], 0
    for match in CODE.finditer(text):
        pieces.extend([protect(text[cursor:match.start()]), match[0]])
        cursor = match.end()
    pieces.append(protect(text[cursor:]))
    def heading_slug(value: str, separator: str) -> str:
        value = re.sub(r"QAAGMATHSTASH(\d{8})END", lambda m: stashed_tex[int(m[1])], value)
        return markdown_slugify(value, separator)

    rendered = markdown.markdown(
        "".join(pieces), extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": heading_slug}}, output_format="html5",
    )
    for index, value in enumerate(stashed):
        rendered = rendered.replace(f"QAAGMATHSTASH{index:08d}END", value)
    return sanitize(rendered, source_path)


def plain(text: str) -> str:
    # Titles/previews are text only; the complete claim body remains preserved.
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text.replace("`", "").replace("**", "").strip())


def parse_claims(text: str) -> list[dict]:
    headings = list(re.finditer(r"^### (C-\d+)\b([^\n]*)", text, re.M))
    result = []
    labels = re.compile(r"^\s*-\s+([A-Za-z][A-Za-z0-9 _/-]*)(?:\s*\([^\n:]*\))?\s*:\s*", re.M)
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        raw = text[heading.start():end].strip()
        # Section headings between entries are registry organization, not claims.
        boundary = re.search(r"\n#{1,2} ", raw)
        if boundary:
            raw = raw[:boundary.start()].rstrip("\n- ")
        fields, matches = {}, list(labels.finditer(raw))
        for i, match in enumerate(matches):
            next_start = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            fields[match[1].lower().strip()] = raw[match.end():next_start].strip()
        status_match = re.search(r"^\s*- status:\s*(PROVED|SKETCH|CONJECTURE|REFUTED)\b", raw, re.M)
        if not status_match:
            fail(f"No canonical status found for {heading[1]}")
        statement = fields.get("statement") or fields.get("refuted statement")
        if not statement:
            quoted = re.search(r'^"([\s\S]*?)"\.?\s*$', raw, re.M)
            statement = quoted[1] if quoted else fields.get("memo header") or raw.split("\n", 1)[1]
        alias = heading[2].strip(" ()")
        title = re.sub(r"^C-(?:NEW-)?", "", alias).replace("-", " ").title() if alias else plain(statement)[:160]
        result.append({
            "id": heading[1], "title": title, "status": status_match[1],
            "statement": statement, "dependencies": fields.get("depends-on", ""),
            "proof": fields.get("where-proved", ""), "test": fields.get("where-tested", ""),
            "referee": fields.get("referee", ""), "relevance": fields.get("north-star relevance", ""),
            "raw": raw, "html": render_markdown(raw, "claims/CLAIMS.md"),
        })
    return result


def source_files(routes: list[dict], template: str, preview: bool = False) -> list[Path]:
    files = set()
    for directory in ["scouting", "argument", "verdicts", "definitions", "claims", "refs"]:
        files.update((ROOT / directory).rglob("*.md"))
    files.update((ROOT / "seed").rglob("*.md"))
    # Computational evidence is useful source code; runtime/tool logs are omitted.
    files.update((ROOT / "checkers").rglob("*.py"))
    files.update((ROOT / "seed/analysis-2026-09-01/numerics").glob("*.py"))
    required = {"PRD.md", "HANDOFF.md", "checkers/README.md", "checkers/MUTATIONS.md", "seed/page81.tex", "seed/page81.png"}
    required.update(re.findall(r'data-source="([^"]+)"', template))
    required.update(s for route in routes for s in route["sources"])
    for path in required:
        target = ROOT / path
        if not target.is_file():
            if preview:
                continue
            fail(f"Required source is missing: {path}")
        files.add(target)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def make_source(path: Path) -> dict:
    relative = path.relative_to(ROOT).as_posix()
    if path.suffix.lower() in RASTER_MIMES:
        text = "Original notebook page supplied as the starting point of the research."
        rendered = '<figure><img src="' + data_image(path) + '" alt="Original handwritten notebook page 81"><figcaption>' + text + "</figcaption></figure>"
        title = "Original notebook scan — page 81"
    else:
        text = path.read_text(encoding="utf-8")
        if path.suffix == ".md":
            rendered = render_markdown(text, relative)
            first_heading = re.search(r"^#{1,4}\s+(.+)$", text, re.M)
            title = plain(first_heading[1]) if first_heading else path.stem.replace("-", " ").capitalize()
        else:
            rendered = "<pre><code>" + html.escape(text) + "</code></pre>"
            title = "Original notebook transcription — page 81" if path.suffix == ".tex" else path.name
            if path.suffix == ".tex":
                rendered = '<p><a href="page81.png">Open the original notebook scan</a></p>' + rendered
    kind = {
        "scouting": "Research memo", "argument": "Structured argument", "verdicts": "Independent audit",
        "definitions": "Canonical definitions", "claims": "Claim register", "refs": "References",
        "checkers": "Computational evidence", "seed": "Historical seed",
    }.get(relative.split("/")[0], "Scope and handoff")
    if relative == "LICENSE":
        title, kind = "GNU Affero General Public License v3.0", "License"
    elif relative == "reports/THIRD_PARTY_NOTICES.md":
        kind = "License"
    return {"id": relative, "path": relative, "title": title, "kind": kind, "text": text, "html": rendered}


def references(source_text: str) -> list[dict]:
    # Selected primary records explicitly fetched and used by the local audits.
    rows = [
        ("Vershik–Okounkov: symmetric-group representations", "math/0503040", "Young tableaux and Jucys–Murphy operators; verified in the support-conversion audit."),
        ("Bacon–Chuang–Harrow: generalized phase estimation", "quant-ph/0407082", "Prior representation-processing construction underlying the support-conversion originality verdict."),
        ("Optimal purification of single qubits", "quant-ph/9812075", "A rank-two measure/reset/factor-extraction ancestor, compared in the r9 audit."),
        ("High-dimensional quantum Schur transforms", "2509.22640", "Representation-processing access and ambient-dimension costs, checked by the r9 critic."),
        ("Determinantal Processes and Independence", "math/0503110", "The classical projection-DPP sampler assumes a supplied kernel or support basis."),
        ("On the sample complexity of purity and inner product estimation", "2410.12712", "The separate-copy purity-estimation baseline used for the r9 decision bit."),
        ("Chefles–Andersson–Jex: universal state comparison", "quant-ph/0402125", "The all-distinct comparison mechanism identified in the coded-Waring audit."),
        ("Zhang–Ying: programmable discrimination", "quant-ph/0606189", "The known comparison/programming mechanism used in the direct Waring tester."),
        ("Lovitz–Lowe: testing tensor-network states", "2410.21417", "The perfect-completeness span principle used for the scoped minimum-batch results."),
        ("Browne–Rudolph: efficient linear-optical computation", "quant-ph/0405157", "Redundant-encoding Bell fusion, compared directly with rank-two Waring fusion."),
        ("Landsberg–Manivel: equations of secant varieties", "math/0311388", "Representation-theoretic background for the three-copy second-secant span."),
        ("Raicu: secant varieties of Segre–Veronese varieties", "1011.5867", "The equation-completeness input used by the second-secant construction."),
        ("Crampé–Poulain d’Andecy: fused Hecke Baxterization", "2004.05035", "The exact prior formula identified in the flag-gallery operation."),
        ("Clifford–Clifford: the classical complexity of boson sampling", "1706.01260", "An exact sampling baseline for the normalized optical-residue construction."),
        ("Ma–Li–Zhao: quantum Radon transform", "2107.05524", "Prior Fourier-slice mechanism compared with the finite-plane incidence transform."),
        ("Albuquerque–Majid: quasialgebra structure of the octonions", "math/9802116", "The retained-label octonion phase and its coboundary interpretation."),
        ("Bremner–Montanaro–Shepherd: commuting quantum computations", "1504.07999", "The known IQP framework identified in the octonionic phase sampler."),
        ("DiVincenzo–Terhal: Fermionic Linear Optics Revisited", "quant-ph/0403031", "The fermionic operations used by the streamed Grassmann-state proposal."),
    ]
    result = []
    for title, identifier, note in rows:
        if identifier not in source_text:
            fail(f"Selected primary reference is absent from source records: {identifier}")
        result.append({"title": title, "url": "https://arxiv.org/abs/" + identifier, "note": note})
    return result


def open_questions() -> list[dict]:
    return [
        {"title": "An original operation remains the central missing result", "question": "The Waring and DPP copy advantages answer real computational questions, but their operations reduce to described algorithms. A qualifying next result needs a precise geometric input, the same output for both comparators, and a demonstrably different processing mechanism.", "sources": ["PRD.md", "HANDOFF.md", "verdicts/support-plucker-r9.md"]},
        {"title": "Which structured equations have useful normalized gaps?", "question": "The fixed-tuple multigenerator Bombieri bound, proposed non-cone gap criteria and condition-number links remain at their registered scopes. A useful theorem must control the block-encoding scale as well as the raw spectrum and survive sparse classical iterative methods.", "sources": ["claims/CLAIMS.md", "scouting/classical-landscape.md"]},
        {"title": "The general intersection asymptotic still has a named analytic gap", "question": "Linear projector overlaps are exact, but the general clean-intersection derivation needs the ambient Bergman-frame operator estimate. Proving that estimate would strengthen the geometric interpretation; it would not by itself prove computational advantage.", "sources": ["scouting/intersection-observables.md", "verdicts/intersection-observables-r3.md"]},
        {"title": "Betti information requires its own access and spectral theorem", "question": "The squarefree component identities do not automatically control the whole graded block. Non-squarefree gap comparisons, adjacent-degree quotient access and the cost of conditioning on the quotient remain necessary for a complete algorithm.", "sources": ["scouting/koszul-betti.md", "verdicts/koszul-betti-r5.md"]},
        {"title": "Recovery needs an actual channel on a specified family", "question": "Successful growth and a stationary reservoir law are insufficient. A new proposal must specify the failed-state recovery, preserve the intended pure or mixed target, and bound its implementation or mixing cost on a family that remains classically difficult.", "sources": ["scouting/original-growth-round2.md", "scouting/original-recovery-round3.md", "scouting/chow-foulkes-audit.md"]},
        {"title": "A practical application needs an exhibited unmet bottleneck", "question": "For robotics and other classical applications, supply a concrete family with a useful real output, honest data loading and a simultaneous time/space comparison. The surveyed dense-memory estimate and the proposed perception-relaxation bottleneck do not establish that family.", "sources": ["scouting/robotics-space.md", "scouting/robotics-deep-dive.md", "scouting/applications-wide-net.md"]},
    ]


def katex_assets(directory: Path | None) -> tuple[str, str, str, str]:
    candidates = [directory] if directory else []
    if os.environ.get("QAAG_KATEX_DIR"):
        candidates.append(Path(os.environ["QAAG_KATEX_DIR"]))
    candidates.extend([REPORTS / "node_modules/katex", Path("/tmp/qaag-report-tools/node_modules/katex")])
    package = next((p for p in candidates if p and (p / "dist/katex.min.css").is_file()), None)
    if package is None:
        fail("KaTeX not found. Run npm ci --prefix reports, or pass --katex-dir /path/to/node_modules/katex.")
    version = json.loads((package / "package.json").read_text())["version"]
    if version != "0.16.22":
        fail(f"Expected KaTeX 0.16.22, found {version}")
    css = (package / "dist/katex.min.css").read_text()
    # Keep one modern font format per font face, rather than three duplicates.
    css = re.sub(r"src:([^;}]+)", lambda m: "src:" + next((part for part in m[1].split(",") if ".woff2" in part), m[1]), css)
    def font(match: re.Match) -> str:
        name = match[1].strip("\"'")
        font_path = package / "dist" / name
        if font_path.suffix != ".woff2" or not font_path.is_file():
            fail(f"Unexpected external CSS asset: {name}")
        return "url(data:font/woff2;base64," + base64.b64encode(font_path.read_bytes()).decode("ascii") + ")"
    css = re.sub(r"url\(([^)]+)\)", font, css)
    js = (package / "dist/katex.min.js").read_text()
    auto = (package / "dist/contrib/auto-render.min.js").read_text()
    js = re.sub(r"\n?//# sourceMappingURL=.*", "", js)
    auto = re.sub(r"\n?//# sourceMappingURL=.*", "", auto)
    return css, js, auto, (package / "LICENSE").read_text()


def validate(data: dict, template: str, preview: bool) -> list[str]:
    claims = {c["id"] for c in data["claims"]}
    sources = {s["path"] for s in data["sources"]}
    issues = []
    covered_memos = {p for route in data["routes"] for p in route["sources"]}
    for memo in sorted((ROOT / "scouting").glob("*.md")):
        path = memo.relative_to(ROOT).as_posix()
        if path not in covered_memos:
            issues.append("Research atlas needs a route citing " + path)
    for collection in ["routes", "claims", "sources"]:
        ids = [x["id"] for x in data[collection]]
        if len(ids) != len(set(ids)):
            fail(f"Duplicate {collection} IDs")
    for claim in data["claims"]:
        if claim["status"] not in STATUSES or not claim["raw"] or not claim["statement"]:
            fail(f"Incomplete canonical claim: {claim['id']}")
        issues.extend(f"{claim['id']}: unknown numbered dependency {dependency}"
                      for dependency in re.findall(r"C-\d{3}\b", claim["dependencies"])
                      if dependency not in claims)
    for route in data["routes"]:
        for field in ["id", "title", "family", "question", "idea", "test", "outcome", "survives", "remaining"]:
            if not isinstance(route.get(field), str) or not route[field].strip():
                fail(f"Invalid route field: {route['id']}.{field}")
        issues.extend(f"{route['id']}: unknown claim {c}" for c in route["claimIds"] if c not in claims)
        issues.extend(f"{route['id']}: missing source {s}" for s in route["sources"] if s not in sources)
    required_claims = {f"C-{n:03d}" for n in range(1, 365)}
    issues.extend("Missing canonical claim " + c for c in sorted(required_claims - claims))
    for source in re.findall(r'data-source="([^"]+)"', template):
        if source not in sources:
            issues.append("Unresolved article source: " + source)
    for question in data["openQuestions"]:
        issues.extend(f"Open question {question['title']}: missing source {source}"
                      for source in question.get("sources", []) if source not in sources)
    parsed_sources = {source["path"]: BeautifulSoup(source["html"], "html.parser") for source in data["sources"]}
    for source_path, document in parsed_sources.items():
        for link in document.select("a[href]"):
            href = urlsplit(link["href"])
            if href.scheme or href.netloc:
                continue
            raw = unquote(href.path)
            candidates = [source_path] if not raw else [raw, posixpath.normpath(posixpath.join(posixpath.dirname(source_path), raw))]
            target = next((path for path in candidates if path in parsed_sources), None)
            if target is None:
                issues.append(f"{source_path}: unresolved local hyperlink {link['href']}")
            elif href.fragment and not parsed_sources[target].find(id=unquote(href.fragment)):
                issues.append(f"{source_path}: unresolved heading anchor {link['href']}")
    if issues and not preview:
        fail("Reference validation failed:\n" + "\n".join(issues))
    return issues


def build(args: argparse.Namespace) -> dict:
    template = (REPORTS / "report.template.html").read_text()
    routes = []
    for name in ["foundations", "later-routes"]:
        routes.extend(json.loads((REPORTS / f"content/{name}.json").read_text()))
    for route in routes:
        route["sources"] = list(dict.fromkeys(SOURCE_ALIASES.get(s, s) for s in route["sources"]))
    files = source_files(routes, template, args.preview)
    sources = [make_source(path) for path in files]
    claims_text = (ROOT / "claims/CLAIMS.md").read_text()
    claims = parse_claims(claims_text)
    terms = {}
    for route in routes:
        for term in route.get("terms", []):
            terms.setdefault(term["term"].casefold(), term)
    for term, meaning in [
        ("Total-variation distance", "The largest difference in probability assigned to the same event by two distributions."),
        ("Perfect completeness", "A test accepts every promised YES input with probability exactly one under its stated ideal assumptions."),
        ("Normalized gap", "The smallest relevant spectral separation divided by the normalization used to implement the operator."),
        ("Postselection", "Keeping only a specified measurement outcome; its probability must be included in the cost."),
        ("Schur–Weyl decomposition", "A decomposition separating collective basis-change symmetry from permutations of repeated registers."),
        ("Copies-only access", "Independent supplied quantum states, without a free coefficient list, preparation inverse or purification register."),
        ("Independent audit", "A separate examination of the precise statement, assumptions, proof, implementation and classical comparator."),
    ]:
        terms.setdefault(term.casefold(), {"term": term, "meaning": meaning})
    source_text = "\n".join(s["text"] for s in sources)
    fingerprint = hashlib.sha256((template + json.dumps(routes, sort_keys=True, ensure_ascii=False) + source_text).encode()).hexdigest()
    data = {
        "meta": {"snapshot": args.snapshot, "generated": "Reproducible local build", "fingerprint": fingerprint,
                 "counts": {"routes": len(routes), "claims": len(claims), "sources": len(sources), "statuses": dict(Counter(c["status"] for c in claims))},
                 "researchGoal": "Proved D25 results: useful original-generator selection with an unconditional fixed-source copy advantage. Explicit-coefficient and practical hardware advantages remain open.",
                 "notes": ["Scientific source snapshot; historical documents retain their original claims and wording. Only claims/CLAIMS.md assigns current formal statuses.", "Runtime/tool logs and operational briefs are excluded; the r8 side-probe link is represented by HANDOFF.md.", "External references open only on explicit clicks. All source text, formula rendering, fonts and notebook imagery are embedded."]},
        "routes": routes, "claims": claims, "sources": sources,
        "glossary": sorted(terms.values(), key=lambda x: x["term"].casefold()),
        "openQuestions": open_questions(), "references": references(source_text),
    }
    issues = validate(data, template, args.preview)
    if issues:
        data["meta"]["previewWarnings"] = issues
    css, js, auto, license_text = katex_assets(args.katex_dir)
    encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    data_block = '<!--REPORT_DATA_START-->\n<script type="application/json" id="report-data">' + encoded + "</script>\n<!--REPORT_DATA_END-->"
    output, replacements = re.subn(r"<!--REPORT_DATA_START-->[\s\S]*?<!--REPORT_DATA_END-->", lambda _: data_block, template)
    if replacements != 1:
        fail("Expected exactly one REPORT_DATA marker pair")
    for marker, content in [("/*__KATEX_CSS__*/", css), ("/*__KATEX_JS__*/", js), ("/*__KATEX_AUTORENDER_JS__*/", auto)]:
        if output.count(marker) != 1:
            fail("Missing or duplicate template slot: " + marker)
        output = output.replace(marker, content)
    output = output.replace("</body>", "<!-- KaTeX 0.16.22 — MIT license\n" + license_text.replace("--", "—") + "\n-->\n</body>")
    # No runtime-loaded scripts, stylesheets, frames or remote images may remain.
    dom = BeautifulSoup(output, "html.parser")
    forbidden = dom.select("script[src], link[href], iframe, object, embed, img[src^='http'], img[src^='//']")
    if forbidden:
        fail("Runtime external or embedded resource elements remain: " + str(forbidden[:3]))
    if re.search(r"(?:@import|url\(\s*['\"]?(?:https?:|//))", "\n".join(t.get_text() for t in dom.find_all("style"))):
        fail("External CSS request remains")
    if json.loads(dom.find("script", id="report-data").string) != data:
        fail("Embedded JSON round-trip failed")
    if not args.check:
        args.output.write_text(output, encoding="utf-8")
    elif not args.output.is_file() or args.output.read_text() != output:
        fail("Generated artifact is stale; rebuild before checking")
    print(json.dumps({"output": str(args.output), "bytes": len(output.encode()), **data["meta"]["counts"], "glossary": len(data["glossary"]), "references": len(data["references"]), "previewWarnings": issues}, indent=2))
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--katex-dir", type=Path, help="Path to the installed katex package")
    parser.add_argument("--output", type=Path, default=REPORTS / "research-report.html")
    parser.add_argument("--snapshot", default="8 September 2026")
    parser.add_argument("--preview", action="store_true", help="Allow pending canonical claim/source links while integration is in progress")
    parser.add_argument("--check", action="store_true", help="Validate all inputs and require the checked-in artifact to match a fresh build")
    args = parser.parse_args()
    try:
        build(args)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print("Report build failed: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
