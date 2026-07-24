# Recent prime-patching theorem index

This focused index covers the constructive parabolic, matching-reservoir, and
patch-plus-trade phase of `research/all-n-prime-patching`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP2l--PP2o | Exact variable-reservoir deletion-aware endpoints | PROVED | `docs/37-variable-reservoir-patch-banks.md` |
| PP3ac--PP3ag | Monotone parabolic matching-reservoir patch and square-root width | PROVED | `docs/36-monotone-parabolic-reservoirs.md` |
| PP3ah--PP3ai | Multi-rung coordinate budget and exponent conversion | PROVED | `docs/38-parabolic-rung-budget.md` |
| PP3aj--PP3al | Matching-reservoir path/cycle factorization and deletion marginals | PROVED | `docs/39-matching-reservoir-cycle-factorization.md` |
| PP3am--PP3ap | Exact cycle-reservoir 2-SAT selection | PROVED | `docs/40-cycle-reservoir-2sat.md` |
| PP3aq--PP3at | Sheared parabolic bank and explicit cell/pair spread | PROVED | `docs/41-sheared-parabolic-banks.md` |
| PP3au--PP3aw | Complete width-two matching-patch classification | PROVED / FINITE CHECK | `docs/42-width-two-matching-patches.md` |
| PP3ax--PP3az | Exact one-rectangle repair and repaired finite extensions | PROVED / FINITE CHECK | `docs/43-one-rectangle-patch-repair.md` |
| PP3ba--PP3bd | Multi-rectangle rank-three SAT and exact two-switch classification | PROVED / FINITE CHECK | `docs/44-multi-rectangle-trade-banks.md` |
| PP3be--PP3bg | Unified binary rung/trade CNF and 2-SAT endpoint | PROVED | `docs/45-joint-binary-trade-cnf.md` |
| PP3bh--PP3bl | Multistate equal-margin bad-box CSP, first moment, and LLL | PROVED | `docs/46-multistate-trade-banks.md` |
| PP3bm--PP3bo | Reverse-order cross-rung separation and quadratic component cap | PROVED | `docs/47-reverse-ordered-parabolic-rungs.md` |
| PP3bp--PP3bs | Matching-density barrier and universal matching-first bank | PROVED | `docs/48-matching-density-and-matching-first.md` |
| PP3bt--PP3bu | Universal clean internal width-two rung | PROVED | `docs/49-universal-adjacent-width-two-rungs.md` |
| PP3bv--PP3bw | Canonical matching-first spread and anchored-defect bounds | PROVED | `docs/50-width-two-matching-first-spread.md` |
| PP3bx--PP3bz | Equal-margin matching-block states and unary pruning | PROVED | `docs/51-matching-block-multistate-rungs.md` |
| PP3ca--PP3cb | Local signature-load clean-density endpoint | PROVED | `docs/52-matching-block-local-loads.md` |
| PP3cc--PP3ce | Clean-rung hypergraph packing and transversal core | PROVED | `docs/53-clean-rung-hypergraph-packing.md` |
| PP3cf--PP3ch | Full 36-state width-two block bank and improved spread | PROVED | `docs/54-full-width-two-block-banks.md` |
| PP3ci--PP3cj | Seven-profile global matching-block completion endpoint | PROVED | `docs/55-matching-block-global-endpoint.md` |
| PP3ck--PP3cn | Random-block load `O(r^2/m+r/m)` and almost-all clean equipartition | PROVED | `docs/56-random-matching-block-sparsification.md` |
| PP3co--PP3cq, PP3cw | Directional boundary-shadow feasibility, density, and exact state multiplicity | PROVED | `docs/57-directional-boundary-shadow-cleaning.md` |
| PP3cr--PP3cs | Fixed-core cell/pair pattern compression | PROVED | `docs/58-fixed-core-pattern-compression.md` |
| PP3ct--PP3cv | Random-pool fixed-core pattern sparsification | PROVED | `docs/59-random-pool-fixed-core-sparsification.md` |
| PP3cx--PP3cz | Random cross-pool potential and `K=o(m^(1/3))` endpoint | PROVED | `docs/60-random-cross-pool-patch-sparsification.md` |
| PP3da--PP3dc | Multi-rung macro-bank margins, spread, and support-compression warning | PROVED | `docs/61-multi-rung-matching-macro-banks.md` |
| PP3dd--PP3df | Repeated monotone matching-pool extraction | PROVED | `docs/62-monotone-matching-pool-extraction.md` |
| PP3dg--PP3dh | Balanced exponent reduction to square-root macro states | PROVED UNDER HYPOTHESES | `docs/63-square-root-ordered-pool-macro-reduction.md` |
| PP3di--PP3dk | Greedy square-root component-clean macro bank and cylinder spread | PROVED | `docs/64-greedy-square-root-component-macro-bank.md` |
| PP3dl--PP3do | Universal fully internal square-root macro patch by product LLL | PROVED | `docs/65-product-lll-square-root-macro-patch.md` |
| PP3dp--PP3dr | Conditional LLL-distribution gives `O(R^-q)` fixed-rank macro spread | PROVED FROM PUBLISHED THEOREM | `docs/66-lll-distribution-square-root-macro-spread.md` |
| PP3ds--PP3du | Random balanced coupling disperses the same-edge pair spike | PROVED | `docs/67-random-balanced-coupling-spread.md` |
| PP3dv--PP3dy | Exact product factorization and divisor-energy endpoint for same-edge anchors | PROVED | `docs/68-same-edge-anchor-product-factorization.md` |
| PP3dz--PP3ed | Dense safe-domain square-root macro patch and conditional spread | PROVED | `docs/69-dense-domain-source-clean-macro-patch.md` |
| PP3ee--PP3eh | Boundary-shadow density or Hall-obstruction dichotomy | PROVED | `docs/70-boundary-shadow-density-dichotomy.md` |

## Current exact target

At the balanced exponents

```text
macro variables M = m^0.2875
source-pool size R = m^0.475
macro width W = Theta(sqrt(R)) = m^0.2375,
total width MW = m^0.525.
```

Matching pools, equal-margin restoration, complete internal no-three geometry,
and fixed-rank internal spread are now universal.  Fixed-pair source blockers are
also removed whenever the movement/refill label compatibility graph has a
dense perfect matching.

The remaining bottleneck has two explicit pieces:

1. prove dense safe label domains in almost every macro pool, or exploit the
   boundary-shadow/Hall concentration alternative with protected trades; then
   control fixed-anchor pairs, whose exceptional same-edge class is the divisor
   energy in PP3dv--PP3dy;
2. prove genuine cross-macro support compression, or incorporate all cross-macro
   certificates into one enlarged product-space local lemma.  Formal grouping of
   a full micro-rung product does not reduce the interval-level potential.

The branch no longer lacks square-root macro geometry.  It lacks the global
source-clean and cross-macro distribution theorem for those explicit macros.