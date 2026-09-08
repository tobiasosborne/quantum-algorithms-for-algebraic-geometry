# R14 sharpen the classical generator-selection baseline

Sol xhigh, issue qaag-gff. Own ONLY `scouting/generator-selection-classical-r14.md`.
No agents, bd, shared edits or commits. User deadline: 2026-09-08 01:00 UTC;
wind-down 00:45 UTC. Initial bounded investigation about 20 minutes.

R12's useful source-only ANY original generating pair is proved: quantum cap8,
classical T(T-1)>=d(d-2)/(3(d-1)), q=2d. Root also proved a concrete
O(q log q) separate-copy upper via Clifford two-design tomography. See
definitions/syzygy-plucker-r12.md, argument/syzygy-generator-selection.md,
scouting/syzygy-plucker-r12.md sections5A/5B/6A, and its independent verdict.

Try to close or materially narrow the classical gap for the ANY-pair task.
Do not impose the DPP distribution, assume tomography necessary, or change
the fixed source to a controllable emitter (section6A gives a 2-query classical
controller in that stronger model). Arbitrary POVMs within each copy and
adaptive classical memory are allowed; no quantum memory connects copies.

Investigate a genuinely task-specific sublinear classical sampler or a stronger
lower. Candidate route: random coordinate pairings or hashing, repeated visits
to a low-dimensional block, and adaptive local purity evidence select a
non-collinear pair. Charge collisions/conditioning and require uniform success
for every row coisometry, not only the random balanced Haar hard family.
Root sanity check: with a Haar pure qubit versus maximally mixed qubit,
two-copy separable opposite-outcome evidence gives likelihood ratio at most
3/2, so a single double collision under equal priors only reaches posterior3/5.
Four well-chosen measurements can give a larger ratio, but fourfold collisions
cost roughly q^(3/4), and heavy-column/worst-case normalization is unresolved.
This is an exploratory hint, not a proved universal algorithm.

Alternatively refine the common-minorization/information argument for an
adaptive OUTPUT PAIR. A stronger bound than the generic rank/purity transcript
bound might exist, but the output contains only one relational bit and is
chosen adaptively, so do not import full tomography lower bounds.

Produce an explicit algorithm/proof or a sharply scoped obstruction and a
best current bracket. Derive first, verify targeted primary sources, and
document every assumption. Send early nontrivial findings. No canonical status
promotion. The existing quantum advantage remains valid even if this gap stays open.
