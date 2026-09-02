# Adversarial critic verdict: `scouting/koszul-betti.md`, round 4

## Commands run

| Command | Exit |
|---|---:|
| `bd prime` | 0 |
| `sed -n '1,240p' verdicts/koszul-betti-r3.md` | 0 |
| `git diff f4a8ace HEAD -- scouting/koszul-betti.md` | 0 |
| `rg -n -i -o 'exponentially small' scouting/koszul-betti.md` | 0 |
| Normalized-whitespace verbatim FIX-DEMAND audit | 1 (`status=0`, `criterion-3a=1`, `K-KB11=1`) |
| Byte comparison of §§5–6 against `f4a8ace` | 0 |
| `git diff --check f4a8ace HEAD -- scouting/koszul-betti.md` | 0 |

## O23 disposition

**NOT VERIFIED.** The exponential direction is now correct everywhere, and no sentence calls either cost exponentially small. However, the mandated sentence is verbatim in §3 criterion 3(a) and K-KB11 only. In the status summary it ends “are exponentially large **(O23).**” rather than the required “are exponentially large.” Thus the explicit verbatim FIX DEMAND remains unmet. Sections 5 and 6 are byte-identical to `f4a8ace`. No separate O24 is raised.

## “Exponentially small” occurrence audit

All 24 case-insensitive occurrences are accounted for:

| Lines | Count | Judgment |
|---|---:|---|
| 37, 38, 40 | 3 | Acceptance weight, including the qualified and negated forms; correct. |
| 205, 210 | 2 | `h_N/M_N` acceptance weight; correct. |
| 386 | 1 | Normalized Betti fraction; correct, not a cost. |
| 454, 455, 457 | 3 | Acceptance weight and its qualification; correct. |
| 512 | 1 | Exponentially small overlap `h_N/M_N`; correct. |
| 615, 616, 622, 624 | 4 | Acceptance weight and its qualification; correct. |
| 972 | 3 | Historical quoted wording in the r2 audit; not a current cost claim. |
| 1001 | 5 | Repair metacommentary, the correct ratio, FIX-DEMAND wording, and surviving statement; no current cost claim. |
| 1003 | 1 | Metalinguistic occurrence-audit heading; harmless. |
| 1008 | 1 | Negated metalinguistic claim that no cost is called exponentially small; correct. |

## Final proposed-row decisions

| Proposed row | Decision |
|---|---|
| C-NEW-KB-HODGE | ACCEPT AS CONJECTURE |
| C-NEW-KB-FREE | ACCEPT AS CONJECTURE |
| C-NEW-KB-SUPPORT | ACCEPT AS CONJECTURE |
| C-NEW-KB-HOCHSTER | ACCEPT AS CONJECTURE |
| C-NEW-KB-QMA1 | HOLD — missing a polynomial reduction preserving the total-block normalized gap across all non-squarefree summands. |
| C-NEW-KB-DEQUANT | ACCEPT AS REFUTED |
| C-NEW-KB-GAP-INDEPENDENT | HOLD — missing a total-block counterfamily, a specified positive class of forbidden lower bounds, and any reverse-direction result. |
| C-NEW-KB-FRACTION | ACCEPT AS CONJECTURE |
| C-NEW-KB-SEED-IS-A-BLOCK | ACCEPT AS CONJECTURE |
| C-NEW-KB-NO-FREE-LUNCH | ACCEPT AS REFUTED |

## Final definition decisions

| Definition | Decision |
|---|---|
| D-fermionic-modes | ACCEPT |
| D-koszul-supercharge | ACCEPT |
| D-betti-laplacian | ACCEPT |
| D-graded-betti-number | ACCEPT |
| D-betti-gap | ACCEPT |
| D-normalised-betti-fraction | ACCEPT |
| D-generator-koszul-supercharge | ACCEPT |
| D-betti-estimation-problem | ACCEPT |

**LOCKSTEP:** NO — the mathematics is synchronized, but the status summary does not reproduce the mandated sentence verbatim; §§5–6, rows, and definitions remain unchanged.

VERDICT: FAIL(O23)