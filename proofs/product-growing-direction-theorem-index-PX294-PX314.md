# Product theorem-index continuation: PX294--PX314

This continuation follows
[`product-growing-direction-theorem-index-PX270-PX293.md`](product-growing-direction-theorem-index-PX270-PX293.md)
and records the trajectory reset/antichain reduction, diffuse packet correction
decoder, Bernoulli strict-sign theorem, and path-forest depth obstruction.

| ID | Statement | Status | Location |
|---|---|---|---|
| PX294 | A historical edge reversing an allowed reachability path gives a one-history principal cycle reset | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX295 | Without a historical back-edge reset, every reverse comparability is base-forbidden and the reachability closure has size at most `m Delta_0` | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX296 | Sparse reachability gives an antichain child of order at least `m/H_0`, with `binom(H_0,2)<=m Delta_0` | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX297 | The antichain child contains at least `s(s-1-Delta_0)` releasable historical cells | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX298 | One ancestor level contributes at least the average historical matching load inside the antichain child | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX299 | A full ancestor matching on the antichain child is a fixed-point-free cycle-cover reset | PROVED | `docs/134-historical-backedge-antichain-child.md` |
| PX300 | Old selected packet defects aggregate exactly into a weighted correction graph on row pairs | PROVED | `docs/135-diffuse-packet-correction-dichotomy.md` |
| PX301 | A matching of correction edges gives commuting disjoint transpositions with exact additive old packet destruction | PROVED | `docs/135-diffuse-packet-correction-dichotomy.md` |
| PX302 | Maximum correction degree `rho` yields a correction matching carrying at least `D_pkt/(2rho-1)` weight | PROVED | `docs/135-diffuse-packet-correction-dichotomy.md` |
| PX303 | Weighted correction degree `mu(r)` gives a clean star of order at least `mu(r)/K` | PROVED | `docs/135-diffuse-packet-correction-dichotomy.md` |
| PX304 | Diffuse packet mass gives either a clean-star child or a heavy disjoint correction bank | PROVED | `docs/135-diffuse-packet-correction-dichotomy.md` |
| PX305 | Bernoulli thinning of disjoint packet corrections has a degree-three destruction/creation expectation polynomial | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX306 | Any positive first-order correction gap yields a deterministic strict improvement | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX307 | The support-one creation load of one correction is exactly two rank-one secant weights plus one pair-line term | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX308 | Absence of a candidate-cell star of order `T` bounds first-order creation by `K(2T+1)` per correction | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX309 | Packet mass satisfies an explicit strict-sign-or-two-star-or-linear-residual theorem | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX310 | Packet mass at least `12hK^2` gives strict improvement or a clean star of order `floor(sqrt(D_pkt/(12hK^2)))` | PROVED | `docs/136-bernoulli-packet-correction-strict-sign.md` |
| PX311 | A directed cycle in one releasable historical layer gives a one-level principal reset | PROVED | `docs/137-trajectory-antichain-depth-or-reset.md` |
| PX312 | A cycle-free historical partial matching is a directed path forest with at most `s-1` edges | PROVED | `docs/137-trajectory-antichain-depth-or-reset.md` |
| PX313 | Without a one-level reset, the ancestor depth is at least `ceil(s(s-1-Delta_0)/(s-1))` | PROVED | `docs/137-trajectory-antichain-depth-or-reset.md` |
| PX314 | In the base-free case an antichain child either resets or requires at least `s` ancestor levels | PROVED | `docs/137-trajectory-antichain-depth-or-reset.md` |

The active ledger is
[`tracks/all-n-product-packet-trajectory-sign-stage.md`](../tracks/all-n-product-packet-trajectory-sign-stage.md).

The remaining exact frontier is the bounded linear packet residue, the
path-forest trajectory templates meeting the PX313 depth bound, diffuse
unassigned clean-star/radial first-order creation, and final insertion into
PX63. Exact infinite product closure remains open.
