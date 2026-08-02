# Product theorem-index continuation: PX270--PX293

This continuation follows
[`product-growing-direction-theorem-index-PX249-PX269.md`](product-growing-direction-theorem-index-PX249-PX269.md)
and records the terminal Hall-core, exact optimizer, causal descent, principal
absorber, cycle-escape, and trajectory-saturation results.

| ID | Statement | Status | Location |
|---|---|---|---|
| PX270 | Every terminal matching failure contains a complete forbidden Hall rectangle and has deficiency at most `2Delta-m` | PROVED | `docs/127-terminal-hall-core-classification.md` |
| PX271 | At order `m=2Delta-1`, nonexistence is equivalent to a saturated forbidden `K_(Delta,Delta)` core | PROVED | `docs/127-terminal-hall-core-classification.md` |
| PX272 | At order `m=2Delta-r`, deleting at most `r` rows and columns leaves an allowed balanced perfect matching | PROVED | `docs/127-terminal-hall-core-classification.md` |
| PX273 | An exact one-block terminal rank-at-most-three optimizer runs in `O(m!m^6)` operations | PROVED | `docs/128-terminal-core-subpower-optimizer.md` |
| PX274 | The dependent two-block terminal optimizer runs in `O((m!)^2m^6)` operations | PROVED | `docs/128-terminal-core-subpower-optimizer.md` |
| PX275 | Every fixed-number terminal matching enumeration has `N^o(1)` complexity at `m=O(log log N)` | PROVED | `docs/128-terminal-core-subpower-optimizer.md` |
| PX276 | A nonimproving terminal instance has an auditable `N^o(1)` obstruction certificate | PROVED | `docs/128-terminal-core-subpower-optimizer.md` |
| PX277 | Causal designated-certificate transitions strictly decrease a lexicographic and scalar potential | PROVED | `docs/129-causal-lexicographic-certificate-forest.md` |
| PX278 | Star, line, radial, coordinate-field, mixed-shadow, and packet certificates admit exact ancestor-safety constraints | PROVED | `docs/129-causal-lexicographic-certificate-forest.md` |
| PX279 | Paid designated certificates remain absent through the log-log nested chain with only `N^o(1)` spread loss | PROVED | `docs/129-causal-lexicographic-certificate-forest.md` |
| PX280 | A strict-sign-or-child interface plus terminal handling yields full finite lexicographic termination | PROVED | `docs/129-causal-lexicographic-certificate-forest.md` |
| PX281 | Every sharp Hall core has a principal allowed matching after deleting one common Hall-core label | PROVED | `docs/130-sharp-terminal-hall-core-absorber.md` |
| PX282 | A sharp terminal Hall obstruction leaves at most one designated endpoint unpaid | PROVED | `docs/130-sharp-terminal-hall-core-absorber.md` |
| PX283 | The sharp-core absorber strictly lowers the designated coordinate by at least `m-1` | PROVED | `docs/130-sharp-terminal-hall-core-absorber.md` |
| PX284 | Every maximally deficient near-threshold Hall core admits principal trimming by `r=2Delta-m` common labels | PROVED | `docs/131-maximal-deficiency-terminal-absorber.md` |
| PX285 | The maximal-deficiency absorber moves exactly `m-r=2(m-Delta)` endpoints | PROVED | `docs/131-maximal-deficiency-terminal-absorber.md` |
| PX286 | Every near-threshold core is either maximally deficient and principally absorbable or has strictly smaller unmatched support | PROVED | `docs/131-maximal-deficiency-terminal-absorber.md` |
| PX287 | Every diagonal-forbidden block with `m>Delta` contains an allowed principal directed-cycle trade | PROVED | `docs/132-terminal-principal-cycle-escape.md` |
| PX288 | Such a cycle trade strictly lowers the designated coordinate by its cycle length | PROVED | `docs/132-terminal-principal-cycle-escape.md` |
| PX289 | Principal fixed-point-free rematchings are exactly directed cycle covers in the allowed label digraph | PROVED | `docs/132-terminal-principal-cycle-escape.md` |
| PX290 | Terminal principal cycle optimization has `N^o(1)` complexity | PROVED | `docs/132-terminal-principal-cycle-escape.md` |
| PX291 | A cycle-free terminal allowed digraph forces one fully forbidden row and one fully forbidden column | PROVED | `docs/133-trajectory-saturated-terminal-core.md` |
| PX292 | A fully forbidden row or column forces at least `m-Delta_0` distinct historical endpoint positions | PROVED | `docs/133-trajectory-saturated-terminal-core.md` |
| PX293 | Every terminal core is cycle-executable or trajectory-saturated | PROVED | `docs/133-trajectory-saturated-terminal-core.md` |

The active ledger is
[`tracks/all-n-product-terminal-core-stage.md`](../tracks/all-n-product-terminal-core-stage.md).

The remaining exact frontier is the absorption of trajectory-saturated cores,
the strict-sign-or-child conversion for diffuse unassigned collateral, the
small-block packet range, and final insertion into PX63.
