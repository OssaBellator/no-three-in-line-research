# Superregular resampling and exact conflict-free matching

**Branch:** `research/superregular-resampling`

This is an independent endpoint track. It seeks to upgrade the spread perfect-matching results SR1–SR5 to a local-load theorem in a dense superregular host. It does not depend on the carry-cycle analysis.

## Proved inputs

- SR1: a uniform perfect matching of a dense superregular pair is fixed-rank `O(1/N)`-spread;
- SR2: the two-clone blow-up preserves superregularity;
- SR3: an all-rank spread measure exists in the dense superregular regime;
- SR4: two edge-disjoint spread perfect matchings give exact degree two;
- SR5: a global conflict-mass union bound works when total weighted conflict mass is below one;
- D1–D4: the complete-clone permutation space has a local-load LLL endpoint.

The gap is that spread in an arbitrary host does not imply the Lu–Szekely negative-dependency graph.

## SRR1 — Stationary local resampling oracle — COMPLETE-HOST CASE PROVED

### Target statement

Let `G=(X,Y)` be an `(epsilon,d)`-superregular balanced bipartite graph with `d>=delta N`. Construct a probability measure `mu` on perfect matchings and, for every forbidden partial matching `F` of size at most three, a randomized map

\[
\mathcal R_F:M\mapsto M'
\]

such that:

1. if `F subseteq M`, then `F` is not contained in `M'`;
2. `M'` is a perfect matching of `G`;
3. `mu` is stationary under the resampling operation;
4. the symmetric difference `M triangle M'` is supported on `O_delta(1)` alternating cycles and has `O_delta(1)` edges in expectation;
5. for every event `B` whose matching vertices are disjoint from a controlled neighbourhood of `F`, resampling `F` does not increase the probability of `B` by more than `1+o(1)`.

A version using an exact heat-bath update on a bounded alternating-cycle gadget is preferred.

[`complete-host-resampling-oracle.md`](complete-host-resampling-oracle.md)
proves all five properties for `K_{N,N}`. The oracle swaps the matched
columns of the distinguished forbidden row and one uniformly random other
row; it is a symmetric stationary kernel supported on one four-cycle and
has an exact `1+O(1/N)` remote-event bound. The note also fixes the
stationarity convention: stationarity must refer to the all-state kernel,
since conditional regeneration to `mu` would contradict guaranteed flaw
removal. The superregular missing-edge extension remains open.

## SRR2 — Resampling dependency theorem

### Target statement

Using SRR1, prove an algorithmic or lopsided local lemma for canonical forbidden submatchings of sizes two and three. A sufficient form is:

If

\[
\max_v
\sum_{A\ni v}\Pr_\mu(A)
\le c_0
\]

for a sufficiently small absolute constant `c_0`, then a perfect matching avoiding every forbidden event exists.

The dependency graph should be indexed by overlapping matching vertices, possibly enlarged by the bounded resampling neighbourhood from SRR1.

## SRR3 — Two-layer exact-cover extension

### Target statement

Apply SRR2 sequentially or jointly to two edge-disjoint perfect matchings. The resulting theorem should select a simple 2-factor of the row-column graph while avoiding:

- duplicate cells across layers;
- all collinear candidate triples;
- optional unavailable-cell constraints already encoded by the host.

The local-load hypothesis should scale as the natural spread probabilities `O(N^{-2})` and `O(N^{-3})` for pair and triple events.

## SRR4 — Superregular local-load endpoint

### Target statement

There are constants `epsilon_0,delta,c>0` such that every `(epsilon,delta)`-superregular candidate host with `epsilon<=epsilon_0` and maximum normalized conflict load at most `c` contains two edge-disjoint perfect matchings whose union is no-three-in-line.

An explicit geometric corollary should bound the permitted number of residual collinear triples incident with each row or column.

## Alternative route: conflict-free exact-cover theorem

Instead of SRR1, one may prove a specialization of conflict-free hypergraph matching/covering theory:

- host edges are row-column cells;
- desired object is an exact perfect matching or two disjoint perfect matchings;
- forbidden configurations are matchings of size two or three;
- superregularity supplies the exact-cover reservoir.

The theorem must achieve exact coverage, not merely an almost-perfect conflict-free matching.

## Regression tests and obstructions

- four-cycle host, where opposite compatible edges are positively correlated;
- near-disconnected superregular-looking examples with hidden forced edge pairs;
- duplicate-cell conflicts across two layers;
- preservation of stationary measure after repeated resampling;
- comparison against the exact complete-permutation constant `1/24`.

The four-cycle positive-correlation example and the complete-host oracle
are exhaustively checked by `scripts/verify_complete_resampling.py`.

## Completion criterion

This branch is complete when the superregular extension of SRR1 and
SRR2–SRR4, or an equivalent conflict-free exact-cover theorem, is proved
with constants and supplies a directly usable replacement for D1 in a
dense superregular host.
