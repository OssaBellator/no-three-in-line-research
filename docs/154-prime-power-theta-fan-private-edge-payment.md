# Boundary theta fans have private entering edges and a rooted-conflict payment

CMR477--CMR481 turn mixed-cycle concentration into a colour-boundary arc with
many edge-disjoint return routes, or a narrow two-edge bottleneck. This chapter
pays the theta-fan branch in the existing conflict and full-token ledgers.
Flipping one return route gives one minimum marked-cost state. Because the
return paths are edge-disjoint, the entering-edge sets of those states intersect
only in the common colour-boundary edge.

Consequently, a clean conflict family has an exact alternative: either one
conflict is already rooted on the common boundary edge and the base matching,
or dirty theta states consume pairwise distinct private route edges.

Use the same-level host and matching-contraction notation of CMR467--CMR481.
Fix a cyclic colour-boundary arc

\[
a=u\to w
\]

and pairwise edge-disjoint simple return paths

\[
Q_1,\ldots,Q_q:w\leadsto u
\]

in `D-a`. Let

\[
\Gamma_i=\{a\}\cup Q_i
\]

be the corresponding mixed directed cycles, and let `P_i` be the perfect
matching obtained from the base matching `P` by flipping the alternating cycle
corresponding to `\Gamma_i`.

We use the same symbols for contraction arcs and their nonmatching bipartite
host edges.

## 1. Private entering-edge code

Put

\[
E_i^+=P_i\setminus P,
\qquad
E_i^{\mathrm{priv}}=E_i^+\setminus\{a\}.
\]

### Theorem CMR482 — PROVED

For every `i`,

\[
\boxed{E_i^+=\{a\}\cup E(Q_i),}
\]

and for distinct `i,j`,

\[
\boxed{E_i^+\cap E_j^+=\{a\}.}
\]

Equivalently, the private sets

\[
E_1^{\mathrm{priv}},\ldots,E_q^{\mathrm{priv}}
\]

are nonempty and pairwise disjoint. Each has size between `1` and `m-1`.

### Proof

Flipping an alternating cycle inserts exactly its nonmatching edges and removes
exactly its base matching edges. The nonmatching edges of `\Gamma_i` are the
common arc `a` and the return-path arcs of `Q_i`. Pairwise edge-disjointness of
the return paths gives the intersection identity.

A return path contains at least one and at most `m-1` arcs because its endpoints
are distinct and it is simple. ∎

Thus the theta fan is a sunflower of entering-edge sets with core `\{a\}`.

## 2. New-edge blocker resilience

### Corollary CMR483 — PROVED

Let `F` be any host-edge set with

\[
a\notin F.
\]

If `F` meets every entering set `E_i^+`, then

\[
\boxed{|F|\ge q.}
\]

Equivalently, every set `F` of fewer than `q` noncore edges misses the complete
entering set of at least one theta state:

\[
\boxed{
\exists i,\qquad F\cap(P_i\setminus P)=\varnothing.
}
\]

### Proof

Since `a\notin F`, meeting `E_i^+` requires meeting
`E_i^{\mathrm{priv}}`. Those private sets are nonempty and pairwise disjoint by
CMR482, so one edge cannot meet two of them. ∎

This is an exact reserve statement whenever only newly introduced edges need to
avoid the current blocker set.

## 3. Rooted conflict or private support

Let `\mathcal C` be any candidate conflict family which is clean in `P`:

\[
C\nsubseteq P
\qquad
\text{for every }C\in\mathcal C.
\]

Call a conflict **`a`-rooted** when

\[
\boxed{a\in C\subseteq P\cup\{a\}.}
\]

### Theorem CMR484 — PROVED

If

\[
C\in\mathcal C,
\qquad
C\subseteq P_i,
\]

then exactly one of the following conclusions is available.

1. `C` is `a`-rooted.
2. `C` contains a private entering edge from `E_i^{\mathrm{priv}}`.

Consequently, if all `q` theta states are dirty for `\mathcal C` and
`\mathcal C` contains no `a`-rooted conflict, then there exist pairwise distinct
host edges

\[
\boxed{e_i\in E_i^{\mathrm{priv}},\qquad 1\le i\le q,}
\]

such that each `e_i` supports a conflict recreated in `P_i`.

### Proof

Because `P` is clean and `C\subseteq P_i`, the conflict contains an entering
edge from `P_i\setminus P=E_i^+`. If it contains no private entering edge, its
only edge outside `P` is `a`; hence `a\in C\subseteq P\cup\{a\}`.

If no rooted conflict exists, choose one dirty conflict in each state and then
choose one of its private entering edges. CMR482 makes those chosen edges
pairwise distinct. ∎

The common-edge obstruction is therefore explicit: it is a conflict completed
by adding only the single source-switch edge `a` to the base state.

## 4. Aggregate nonrooted conflict incidence

Define the maximum edge degree of the conflict system by

\[
d(\mathcal C)
=
\max_e|\{C\in\mathcal C:e\in C\}|.
\]

For each state, let `R_i^{\mathrm{nr}}` be the number of recreated conflicts in
`P_i` which are not `a`-rooted.

### Theorem CMR485 — PROVED

One has

\[
\boxed{
\sum_{i=1}^q R_i^{\mathrm{nr}}
\le
 d(\mathcal C)
 \sum_{i=1}^q|E_i^{\mathrm{priv}}|
\le
 d(\mathcal C)q(m-1).
}
\]

### Proof

By CMR484, every nonrooted recreated conflict contains a private entering edge.
Assign it to one such edge. The private sets are disjoint across states, and
one host edge belongs to at most `d(\mathcal C)` candidate conflicts. Sum over
the private edges and use `|E_i^{\mathrm{priv}}|\le m-1`. ∎

Unlike a state-by-state union bound, this estimate records that all noncore
support edges are globally private across the theta family.

## 5. Harmonic-packet and token endpoint

### Corollary CMR486 — PROVED

Let `\mathcal K` be a harmonic packet of total weight

\[
W(\mathcal K)
=
\sum_{K\in\mathcal K}\frac1K,
\]

and suppose the base matching `P` is clean for its represented candidate-only
triple system. Across a boundary theta fan of size `q`, the number of non-`a`-
rooted recreated packet-triple occurrences is at most

\[
\boxed{
2(t-1)^2W(\mathcal K)
\sum_{i=1}^q|E_i^{\mathrm{priv}}|
}
\]

and therefore at most

\[
\boxed{
2(t-1)^2W(\mathcal K)q(m-1).
}
\]

If every theta state is packet-dirty, then at least one of the following holds.

1. **Boundary-rooted packet obstruction.** A represented packet triple satisfies
   \[
   \boxed{a\in C\subseteq P\cup\{a\}.}
   \]
2. **Private-edge payment.** There are at least `q` distinct private route edges
   supporting recreated packet triples. Their exact labelled full-token
   incidence is
   \[
   \boxed{q(p+1)(h-1)}
   \]
   when the parent side is `t=p^h`.

### Proof

CMR386 gives

\[
d(\mathcal C_{\mathcal K})
\le
2(t-1)^2W(\mathcal K).
\]

Apply CMR485. The dirty-state dichotomy is CMR484. In its private branch, the
`q` support edges are distinct, and CMR413 assigns exactly
`(p+1)(h-1)` labelled full-token incidences to every edge. ∎

Thus a theta fan cannot sustain unpriced packet dirtiness. It either exposes one
single-edge completion of a base conflict or consumes fresh private edge
incidence linearly.

## 6. Revised frontier

The mixed-cycle frontier now has payments on both low-overlap branches.

- Vertex-disjoint mixed cycles flip simultaneously by CMR475.
- Edge-disjoint return routes through one boundary edge form a theta state code
  with private entering edges.
- Dirty theta states either pay those private edges or expose an `a`-rooted
  conflict contained in `P\cup\{a\}`.

The next theorem should analyze the rooted obstruction. Geometrically it says
that one fixed source-switch edge completes a conflict using only base-matching
edges. This should reduce to target load at `a`, a matching-vertex wall or
secant star, a primitive-height/quotient/carry signature, protected-reserve
failure, or envelope expansion. The two-edge bottleneck branch of CMR481 remains
a parallel concentration target.

No all-`n` theorem is claimed. The private-edge sunflower, blocker resilience,
rooted-conflict dichotomy, and conflict-degree accounting are checked in
[`scripts/verify_prime_power_theta_fan_private_edges.py`](../scripts/verify_prime_power_theta_fan_private_edges.py).
