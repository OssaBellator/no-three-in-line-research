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
| PP3bp | Universal matching-admissible density bound | PROVED | `docs/48-matching-density-and-matching-first.md` |
| PP3bq | Independent sheared boxes have density at most `4mt/(H_A H_B)` | PROVED | `docs/48-matching-density-and-matching-first.md` |
| PP3br | Matching admissibility forces source-edge endpoint correlation `t/m` | PROVED | `docs/48-matching-density-and-matching-first.md` |
| PP3bs | Every saturated source has an exact hypergeometric matching-first bank | PROVED | `docs/48-matching-density-and-matching-first.md` |
| PP3bt--PP3bu | Every four-edge matching reservoir has a canonical clean internal width-two rung | PROVED | `docs/49-universal-adjacent-width-two-rungs.md` |
| PP3bv--PP3bw | Canonical matching-first spread and constant anchored-defect bound | PROVED | `docs/50-width-two-matching-first-spread.md` |
| PP3bx--PP3bz | `binom(r,4)` equal-margin matching-block states and unary pruning | PROVED | `docs/51-matching-block-multistate-rungs.md` |
| PP3ca--PP3cb | Local signature-load clean-density endpoint and failure trichotomy | PROVED | `docs/52-matching-block-local-loads.md` |
| PP3cc--PP3ce | Clean-rung hypergraph packing, spread, and transversal core | PROVED | `docs/53-clean-rung-hypergraph-packing.md` |
| PP3cf--PP3ch | Full 36-state width-two block bank and improved spread | PROVED | `docs/54-full-width-two-block-banks.md` |

## Current exact target

The independent-template matching-density assumption is now refuted.  Two
correlated routes remain:

1. matching-first constant-width blocks: about `m^0.525` width-two rungs grouped
   into blocks of size `r asymp m^0.475`, with a polynomial clean-state density,
   diffuse clean-deletion hypergraph, and controlled external/cross-block bad
   boxes;
2. larger endpoint-adapted or parabolic rungs whose row and column templates are
   correlated through actual source edges rather than sampled independently.

Either route may use protected rectangle or tomographic trades to neutralize the
small transversal cores exposed by PP3ce.