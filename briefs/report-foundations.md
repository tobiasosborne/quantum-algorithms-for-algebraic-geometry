# Report content inventory: foundations and the original research arms

The user requests an elegant self-contained HTML report of ALL documented
work so far, with animation and interaction, accessible after Nielsen--Chuang.
Root is building the artifact and owns shared files/tracking qaag-dx0.
No new subagents. Write only `reports/content/foundations.json`.

Read CLAUDE.md/PRD/HANDOFF and the original scientific scouting memos:
classical-landscape, applications-wide-net, quantum-primitives, quantum-native,
koszul-betti, intersection-observables, real-variety, robotics-deep-dive,
robotics-space, two-copy-real-filter, plus their pertinent arguments/verdicts.
Inspect the seed/claims context needed to explain the initial Fock/Macaulay
proposal and its normalization corrections. The report will separately embed
the full scientific source archive and searchable claim register.

Deliver a JSON array of accessible narrative route records. Use fields:
`id`, `title`, `family`, `question`, `idea`, `test`, `outcome`, `survives`,
`remaining`, `claimIds` (array), `sources` (repository-path array),
`terms` (array of short {term,meaning} objects if useful).
All prose fields are ordinary plain text, not nested Markdown.

Cover the documented ideas, not just the successful ones. Group closely
related subprobes when that improves understanding, but preserve meaningful
differences: absolute vs normalized gap; state vs scalar output; explicit
input vs copies; geometric reality vs a real vector; an observed interaction
vs a measured degeneracy; a dense-memory comparison vs a true time/space
tradeoff. Explain each geometric term before relying on it. Readers know
qubits, measurement, matrices and basic complexity, but not algebraic geometry.

Do not assign independent PROVED/SKETCH labels: `claims/CLAIMS.md` is the only
status source. `outcome` should state the scientific conclusion in plain
language. Include exact limitations and useful surviving statements. Give
numbers/formulas only when they explain the conclusion. Distinguish open
lemmas from rejected versions and from directions needing an entirely new
mechanism. Aim for a comprehensive, concise inventory (roughly 15--25 routes),
not a chronological transcript. No tool logs or model-internal deliberations.
