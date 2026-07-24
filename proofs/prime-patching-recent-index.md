# Recent prime-patching theorem index

This focused index covers the constructive parabolic, matching-reservoir, and
patch-plus-trade phase of `research/all-n-prime-patching`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP2l | Exact variable-reservoir deletion-aware expectation theorem | PROVED | `docs/37-variable-reservoir-patch-banks.md` |
| PP2m | Uniform joint-incidence form for variable reservoirs | PROVED | `docs/37-variable-reservoir-patch-banks.md` |
| PP2n | Deletion-blind variable-reservoir fallback | PROVED | `docs/37-variable-reservoir-patch-banks.md` |
| PP2o | Failed variable bank forces a concentrated joint certificate | PROVED | `docs/37-variable-reservoir-patch-banks.md` |
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
| PP3bt--PP3bu | Every four-edge matching reservoir has a canonical clean internal width-two rung | PROVED | `docs/49-universal-adjacent-width-two-rungs.md` |
| PP3bv--PP3bw | Canonical matching-first spread and constant anchored-defect bound | PROVED | `docs/50-width-two-matching-first-spread.md` |
| PP3bx--PP3bz | `binom(r,4)` equal-margin matching-block states and unary pruning | PROVED | `docs/51-matching-block-multistate-rungs.md` |
| PP3ca--PP3cb | Local signature-load clean-density endpoint and failure trichotomy | PROVED | `docs/52-matching-block-local-loads.md` |
| PP3cc--PP3ce | Clean-rung hypergraph packing, spread, and transversal core | PROVED | `docs/53-clean-rung-hypergraph-packing.md` |
| PP3cf--PP3ch | Full 36-state width-two block bank and improved spread | PROVED | `docs/54-full-width-two-block-banks.md` |
| PP3ci--PP3cj | Seven-profile global matching-block completion endpoint | PROVED | `docs/55-matching-block-global-endpoint.md` |
| PP3ck--PP3cl | Universal global signature caps and random-block load `O(r^2/m+r/m)` | PROVED | `docs/56-random-matching-block-sparsification.md` |
| PP3cm--PP3cn | Equipartition gives almost-all clean disjoint pools and full-bank density | PROVED | `docs/56-random-matching-block-sparsification.md` |
| PP3co--PP3cq | Exact directional boundary-shadow feasibility and density | PROVED | `docs/57-directional-boundary-shadow-cleaning.md` |
| PP3cw | Exact factored multiplicity of blocker-free width-two geometries | PROVED | `docs/57-directional-boundary-shadow-cleaning.md` |
| PP3cr--PP3cs | Fixed-core cell/pair pattern compression endpoint | PROVED | `docs/58-fixed-core-pattern-compression.md` |
| PP3ct--PP3cv | Random-pool fixed-core pattern sparsification | PROVED | `docs/59-random-pool-fixed-core-sparsification.md` |
| PP3cx--PP3cz | Random cross-pool patch potential and `K=o(m^(1/3))` endpoint | PROVED | `docs/60-random-cross-pool-patch-sparsification.md` |
| PP3da--PP3dc | Multi-rung macro-bank margins, spread, and support-compression warning | PROVED | `docs/61-multi-rung-matching-macro-banks.md` |
| PP3dd--PP3df | Repeated monotone-subsequence extraction at the prime-gap pool exponents | PROVED | `docs/62-monotone-matching-pool-extraction.md` |

## Current exact target

Random equipartition now supplies, for every saturated source, disjoint
`r=o(sqrt(m))` matching pools with same-pool clean density `1/36-o(1)`.  Every
perfect matching layer also contains `m^0.05` disjoint monotone pools of size
`m^0.475`, after at most one global row reflection.

The remaining preparation problem has two explicit parts:

1. make the normalized opposite-layer pattern density `Sigma` from PP3ct vanish,
   or satisfy the weaker directional counts PP3cp and clear the residual anchored
   pairs with protected trades;
2. build an endpoint-adapted support-compressed macro state on one increasing
   `m^0.475`-edge pool, installing width `Theta(m^0.475)` with polynomial clean
   state density.  Merely grouping a full product of micro-rungs does not reduce
   the interval-level cross potential.

Once about `m^0.05` such macro states exist, PP3cz makes their mutual patch-only
compatibility automatic.  The missing theorem is now local compressed geometry
on an ordered matching pool, not matching availability, pool packing, or
cross-variable first moment.