# Live composite-modulus theorem ledger continuation 2

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869; and
- this file from CMR870 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR870--877 | Nine-atom triple support, multiplicity/support alternatives, disjoint support packing versus small cover, atom concentration, wall/cell-star refinement, global compatibility, branch-path payment, and the support endpoint | PROVED | `docs/213-prime-power-new-triple-support-packing.md` |
| CMR878--885 | Deletion/contraction path resources, disjoint-support path bound, polynomial support matching and cover, atom concentration, explicit episode bound, geometric interpretation, and the constant-arity path endpoint | PROVED | `docs/214-prime-power-constant-arity-path-budget.md` |
| CMR886--893 | Physical-cell and matching-vertex edge stabilisation, uniform labelled-edge concentration, exact binary edge split, conditioned edge contraction, rank-two transfer, residual-pair multiplicity, and the support-atom batching endpoint | PROVED | `docs/215-prime-power-support-atom-edge-batching.md` |

The branch still does not prove the all-`n` conjecture. Along one stable-owner
completeness path, canonical new triples have support matching number at most

\[
B_n=2n^2-2n+\left\lfloor\frac{2n}{3}\right\rfloor
\]

unless there is structural exit or strict potential improvement. Therefore the
historical support family has a cover of size at most `9B_n`, and long paths
concentrate on one physical cell or one labelled matching vertex.

A support atom in `d` distinct canonical triples contains one exact labelled edge
in at least `ceil(d/(2n))` of them. One binary split batches those candidates:
delete the edge, or condition on and contract it, transferring all associated
triples to rank-two residual pairs.

The active prime-power frontier is global branch merging: repeated side branches
which concentrate on the same labelled edge, residual pair, or forced certificate
must be memoized or charged to a common target-load and potential budget. The
fixed-owner restoration loop, prime-field transfer, and arbitrary side-length
assembly remain afterward.
