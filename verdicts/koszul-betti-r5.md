# Adversarial critic verdict: `scouting/koszul-betti.md`, round 5

## Commands run

| Command | Exit |
|---|---:|
| `bd prime` | 0 |
| `sed -n '1,240p' verdicts/koszul-betti-r4.md` | 0 |
| Normalised-whitespace verbatim FIX-DEMAND audit | 0 (`status=1`, `criterion-3a=1`, `K-KB11=1`) |
| `git diff --unified=0 HEAD~1 HEAD -- scouting/koszul-betti.md` | 0 |
| Exact reconstruction of the current memo from `HEAD~1` by deleting only ` (O23)` | 0 |
| Byte comparison of §§5–6 against `HEAD~1` | 0 |
| `git diff --check HEAD~1 HEAD -- scouting/koszul-betti.md` | 0 |

## O23 disposition

**VERIFIED.** After normalising whitespace, the mandated FIX DEMAND sentence appears verbatim exactly once in each required passage: the status summary, §3 criterion 3(a), and K-KB11. The scouting-memo diff since r4 deletes only ` (O23)` from the status-summary sentence; nothing else changes. Sections 5–6 are byte-identical to `HEAD~1`.

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

**LOCKSTEP:** YES — the mandated sentence is verbatim in all three passages, the r4 residue alone was deleted, and §§5–6, rows, and definitions remain unchanged.

VERDICT: PASS