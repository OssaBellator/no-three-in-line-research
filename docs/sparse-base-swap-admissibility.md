# Exact base-state admissibility for matching swaps

**Branch:** `research/sparse-algebraic-spread`

SAS5hd--SAS5hh reduce mixed-orientation operation-square legality to two
base-state single-swap checks whenever the remaining guards transport across
the disjoint companion swap. This note closes the structural part of those
base checks: host membership and two-layer duplicate-cell avoidance have an
exact two-edge criterion and an atomic failure witness.

## One-layer swap

Let `pi` be a perfect matching from rows to columns in a bipartite host `G`.
For distinct rows `i,j`, let `sigma_ij pi` exchange the two matched columns:

\[
(\sigma_{ij}\pi)(i)=\pi(j),\qquad
(\sigma_{ij}\pi)(j)=\pi(i).
\]

All other rows are unchanged.

## SAS5hi -- exact one-layer host criterion -- PROVED

The swapped state is a perfect matching of `G` if and only if the two cross
edges

\[
\boxed{(i,\pi(j)),\qquad (j,\pi(i))}
\]

belong to `G`.

When legal, the symmetric difference of the two matchings is exactly the
alternating four-cycle on rows `i,j` and columns `pi(i),pi(j)`, and applying the
same swap again returns `pi`.

### Proof

Exchanging two distinct column images preserves bijectivity. The only new
edges are the two displayed cross edges, so host validity is equivalent to
their presence. The swap is a transposition and hence an involution. QED.

## Two-layer simple states

Let `(pi,rho)` be two edge-disjoint perfect matchings of the same host. Only
`pi` is switched.

## SAS5hj -- exact two-layer structural criterion -- PROVED

The state `(sigma_ij pi,rho)` is a pair of edge-disjoint host matchings if and
only if

\[
\boxed{
(i,\pi(j)),(j,\pi(i))\in E(G),
\qquad
\pi(j)\ne\rho(i),
\qquad
\pi(i)\ne\rho(j).
}
\]

No other host or duplicate-cell check can change.

### Proof

SAS5hi gives the host criterion. Rows outside `i,j` are unchanged and were
already disjoint from `rho`. At row `i` the new first-layer edge collides with
the second layer exactly when `pi(j)=rho(i)`; the row `j` condition is
analogous. QED.

## SAS5hk -- atomic base-swap obstruction -- PROVED

A failed structural base check has one of exactly four least witnesses:

1. missing host edge `(i,pi(j))`;
2. missing host edge `(j,pi(i))`;
3. opposite-layer collision `(i,pi(j))=(i,rho(i))`;
4. opposite-layer collision `(j,pi(i))=(j,rho(j))`.

Fixing the ordered row pair, the current images and the witness type gives a
complete finite obstruction address. Reversal of a legal swap needs no new
structural hypothesis: the reverse edges are the original valid matching
edges, and the original state was already layer-disjoint.

### Proof

The four conditions in SAS5hj are necessary and sufficient. Order them and
return the first failed condition. The reversal assertion follows from the
involution and validity of the starting state. QED.

## SAS5hl -- structural import into mixed-orientation squares -- PROVED

For two disjoint matching swaps, the host-membership and duplicate-cell parts
of the two base predicates in SAS5hf are decided by four cross host edges and,
in the two-layer setting, four row-local collision inequalities. If they all
hold, every side of the commuting operation square is structurally legal. If
one fails, SAS5hk returns an exact host/collision atom before any arithmetic
word, line, boundary or payment-sensitive guard is considered.

### Proof

Apply SAS5hi or SAS5hj to each base swap and then SAS5hf to transport the legal
base edges around the disjoint commuting square. Failure is localized by
SAS5hk. QED.

## Remaining legality frontier

Base-state single-swap admissibility is therefore closed for the underlying
one- and two-layer matching structure. The remaining SAS6 legality work is
specific to arithmetic word realization, collinearity and boundary guards,
overlapping swap supports, and payment/context fields that are not invariant
under disjoint transport.

## Finite check

`scripts/verify_sparse_base_swap_admissibility.py` exhausts small host masks,
perfect matchings, row swaps and edge-disjoint second layers. It compares the
direct post-swap validity test with the displayed criteria and verifies
involution and four-cycle support.
