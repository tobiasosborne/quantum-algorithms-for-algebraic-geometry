# Dedicated HTML artifact builder

The user explicitly asks you to produce an elegant, human-readable,
self-contained HTML artifact explaining ALL documented work in this project,
with animation and interaction, accessible to a reader of Nielsen--Chuang.
Root handles the scientific data, source archive, canonical claims and
tracking (`qaag-dx0`). A second agent is producing route inventories.
No further subagents. Your writable files are `reports/report.template.html`
and `reports/research-report.html`. Build the actual report interface, not a
design proposal. Root will supply a build script and final embedded dataset.

Read PRD success criteria and HANDOFF. The truthful lead is: quantum copy
advantages have been proved, but NO candidate yet meets the original-mechanism
north star. Make this clear without making the report a wall of failure labels.
Explain what was learned and the surviving mathematical tools. A proof, a
speedup, and historical/mechanism originality are different claims.

DESIGN: warm paper, deep ink, restrained teal/ochre/red accents, editorial
serif headings plus clean system sans body, generous readable line lengths,
excellent typography and equations. Use native SVG/CSS/JS, no network runtime
dependencies, no raster/image-generation assets, no heavy framework. Sticky
chapter navigation on desktop and a compact mobile equivalent. Meaningful
animations with pause controls and prefers-reduced-motion support. Keyboard
accessible buttons, labels, focus, dialogs and expandable content. Print CSS.
Avoid an AI-dashboard look, excessive badges, giant blank hero regions or jargon.

DATA CONTRACT (root will embed JSON in script#report-data):
`meta`: snapshot, generated, counts, researchGoal, notes;
`routes`: array of {id,title,family,question,idea,test,outcome,survives,remaining,
 claimIds:[...],sources:[...],terms:[{term,meaning}],disposition?};
`claims`: array of {id,title,status,statement,dependencies,proof,test,referee,
 relevance,raw,html};
`sources`: array of {id,path,title,kind,text,html};
`glossary`: array of {term,meaning}; `openQuestions`: array of plain-language
records; `references`: array {title,url,note}.
Use a valid small fallback dataset for preview. Enclose the data script between
`<!--REPORT_DATA_START-->` and `<!--REPORT_DATA_END-->` so root can replace it.
Include inline comment slots `/*__KATEX_CSS__*/`, `/*__KATEX_JS__*/` and
`/*__KATEX_AUTORENDER_JS__*/`; root embeds KaTeX and font data. Guard rendering
when it is unavailable in the preview. All other JS/CSS must be inline.

CONTENT STRUCTURE, written as a readable article with progressive depth:
1. Clear current verdict and what counts as a successful new algorithm.
2. A gentle geometry-to-quantum dictionary: varieties, ideals, homogeneous
   polynomials, fixed-degree coefficient spaces, multiplication maps and dark
   states. Readers know linear algebra and quantum mechanics, not geometry.
3. Explain the core Hamiltonian and the normalization/overlap traps.
4. Explain input/output fairness, copies vs coefficient lists, and honest
   postselection accounting. 'Classical' in the copies model allows arbitrary
   within-copy POVMs but only classical memory between original copies.
5. Two substantial positive results: support-to-Pluecker/DPP sampling (r9),
   and the Waring hidden-component test. Both have matched copy advantages;
   their displayed mechanisms are already described and do not meet D22.
6. Searchable/filterable research atlas driven by every route record. Detail
   views must explain question, operation, adversarial test, outcome, surviving
   statement and remaining question, with claim/source buttons.
7. How independent proofs, finite tests, deliberate wrong variants and prior-
   algorithm reductions were used. Include a searchable claim registry and
   an offline source reader for embedded HTML/Markdown documents.
8. Grounded remaining questions, then glossary and primary references.

REQUIRED INTERACTIVES (accurate, substantive, clearly labelled illustrations):
- Geometry picture: circle x^2+y^2=1 and parabola y=x^2-t. Slider t in
  [-1.2,1.4], optional play/pause. Find intersections using u=x^2:
  u=[2t-1 +/- sqrt(5-4t)]/2, retaining nonnegative u. Label this a real slice,
  not a general complex intersection theorem.
- Normalization: f=(x-y)/sqrt2 at degree2, in orthonormal Fock bases,
  M=[[1,0],[-1/sqrt2,1/sqrt2],[0,-1]], H=MM† has eigenvalues0,1,2.
  Scaling f by s multiplies raw gap and block normalization by s²;
  normalized gap stays1/2. Slider/animation must show that invariant.
- Fresh-copy cost explorer: C_t=(2/p)^t for the displayed binary recursion,
  contrasted with ordinary repetitions. Preset Schur step p=1/2 gives4^t.
  Do not imply this is a universal lower bound for all algorithms.
- DPP/coordinate-volume explorer: q=4,r=2, two known coordinate blocks A,B.
  Case0 columns (u_A,0),(0,v_B); case1 columns (u1_A,v1_B)/sqrt2,
  (u2_A,v2_B)/sqrt2, with 2D rotation frames controlled by angles. Compute
  all6 pair probabilities as squared2x2 minors. Their total is1; cross-block
  masses are1 and1/2. Show projected row vectors/parallelogram and probability
  bars. Say this small example illustrates the statistic; the lower bound
  hides the frames in growing dimension.
- Explain a three-copy rank-two conversion stepper: first-pair swap test;
  on failure swap systems2,3 and test first pair again. Flat rank2 success
  is7/16; any accepted pair is the support Slater state. This uses6 data
  qubits plus1 ancilla at q=4. A trial simulation may use first-click1/4,
  conditional second-click1/4. Label simulations as illustrations.
- Dimension/copy chart for DPP: at epsilon=1/16, every separate-copy sampler
  obeys T(T-1)>=3q/16. The flat-rank-two 3-copy/one-recycle protocol repeated
  B=ceil(ln(1/epsilon)/ln(16/9)) times gives a sufficient3B-copy cap with
  fallback on failure (15copies at epsilon1/16). Label lower vs upper bounds;
  neither is an exact practical runtime. Allow q=2^n via n slider.
- Disk-count sensitivity: f_R=z^D-R^D, R=.5 or.75, query radius.625.
  Counts normalized by D are1 and0, despite both having unit-disk count D.
  Infidelity=((.75^D-.5^D)^2)/[(1+.5^(2D))(1+.75^(2D))]; quantum lower
  1/(9 infidelity), simple classical-copy upper ceil(2ln3/(.75^(2D))).
  Root spacing isTheta1/D and boundary distance1/8. Slider D3..60 and an
  access-model toggle should explain why classical coefficient bits evade
  this copies-only obstruction.

Waring result text must be careful: T=sum_(a=1)^4 c_a u_a^tensor4,
u_a in C^d tensor C^d, q=d²,d>=20, Gram>=1/2, seed>=1/512. The bit is
Gamma=average e5 of component Schmidt-probability spectra, zero vs1e-6.
Five ORIGINAL source copies per trial; the proved sufficient total budget is
2,137,652,311,842,450 including an implementation margin. This is not a minimum
and is impractical. Classical single-original-copy lower is
q^(1/4)/(4sqrt24). Explain original copies versus internal component registers.
Don't claim whole-source rank testing solves the full promise.

The source/claim reader must work entirely offline. Render prebuilt source
HTML in a dialog or reading pane; rewrite repository-document links to open
embedded sources. External citation links may open a new tab on explicit
click, but no fetches are needed to render anything. Avoid innerHTML injection
of unsanitized text; root provides sanitized source HTML and safe JSON.

Deliver a complete responsive HTML template and preview artifact. Tell root
when the first version is ready. Continue polishing until the provided data
fits without clipping, broken navigation, misleading counts or blank sections.
Root will test with a real browser and send actionable fixes.
