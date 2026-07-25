# Fixed secant stars yield a matching-vertex wall, bulk protected absorption, or a large core

CMR560--CMR570 and CMR604 reduce rank-one and repeated-cell rank-zero
collateral to fixed secant stars owned by one canonical protected selector.
Every star arm consists of two outside candidate cells.  The outside pairs are
cell-disjoint, but different arms can still share source or target matching
vertices.

A matching-vertex degree split resolves that overlap.  Either one source or
target vertex lies on many arms, giving the established candidate-wall
endpoint, or a greedy extraction produces many arms whose outside cells use
pairwise distinct source and target vertices.  Relative to a protected matching
of size `k`, at most `2k` such arms can touch protected vertices.  All remaining
arms form one large compatible partial matching, with two cells per arm, and
are absorbed simultaneously into the canonical forbidden matching.

Thus a fixed secant star has a monotone execution: wall concentration, growth
of the protected matching, or certification that the protected core is already
large relative to the extracted star.

Let

\[
\mathcal A
=
\{A_1,\ldots,A_M\}
\]

be a fixed secant star centred at a candidate cell `z`.  Write

\[
A_i=\{z,a_i,b_i\},
\qquad
Z_i=\{a_i,b_i\}.
\]

Assume, as supplied by CMR560, CMR564, or CMR565, that:

1. every `Z_i` is a compatible two-cell partial matching;
2. the outside pairs `Z_i` are pairwise cell-disjoint.

Let `P` be the current protected partial matching on a residual board of side
`n`, and put

\[
k=|P|.
\]

## 1. Matching-vertex wall or disjoint-arm extraction

For a source or target matching vertex `v`, let

\[
d_{\mathcal A}(v)
\]

be the number of outside pairs `Z_i` incident with `v`.  Put

\[
\Delta
=
\max_v d_{\mathcal A}(v).
\]

### Theorem CMR611 — PROVED

Fix an integer threshold `D>=2`.  At least one of the following holds.

1. **Matching-vertex wall.**  One source or target vertex is incident with at
   least
   \[
   \boxed{D}
   \]
   distinct star arms.
2. **Matching-compatible arm family.**  There is a subfamily of at least
   \[
   \boxed{
   R
   \ge
   \left\lceil
   \frac{M}{4(D-1)}
   \right\rceil
   }
   \]
   arms whose complete outside-cell union uses pairwise distinct source and
   target vertices.

### Proof

If `\Delta>=D`, use the first branch.  Otherwise every matching vertex belongs
to at most `D-1` arms.

Greedily choose one arm and delete every remaining arm sharing one of its four
outside matching vertices.  Each of those four vertices belongs to at most
`D-1` arms, so one step removes at most `4(D-1)` arms.  The chosen family has
size at least the displayed ceiling. ∎

The first branch is exactly a source-row or target-column candidate wall.  The
second branch is stronger than cell-disjointness: all outside cells together
form one partial matching of size `2R`.

## 2. Most disjoint arms avoid the protected core

Fix a matching-compatible family of `R` arms supplied by CMR611.  Call an arm
**protected-touching** when one of its four outside matching vertices belongs
to `V(P)`.

### Theorem CMR612 — PROVED

At most

\[
\boxed{2k}
\]

of the `R` arms are protected-touching.  Consequently at least

\[
\boxed{
G
\ge
\max\{0,R-2k\}
}
\]

arms have all outside vertices disjoint from `V(P)`.

The union `S` of the outside pairs of those `G` free arms is a partial matching
of size

\[
\boxed{|S|=2G}
\]

which is vertex-disjoint from `P`.

### Proof

The extracted arms use pairwise distinct matching vertices.  Assign every
protected-touching arm to one protected vertex that it uses.  The assignment is
injective because no two extracted arms share a vertex.  There are `2k`
protected vertices.

All outside cells of the remaining arms use distinct source and target
vertices and avoid `V(P)`, so their union is the claimed partial matching. ∎

## 3. Simultaneous star-arm absorption

### Theorem CMR613 — PROVED

Let `S` be the free outside-cell matching from CMR612.  Then

\[
P\cup S
\]

has a canonical perfect-matching extension, and the corresponding exact
`D_n` derangement cylinder avoids every cell of `S`.

Hence every one of the `G` selected free star arms is absent from every state
of the new cylinder.  Protected matching size grows by

\[
\boxed{2G.}
\]

### Proof

CMR612 says `P\cup S` is a partial matching.  Apply CMR571.  Every selected arm
contains its two outside cells from `S`, both of which lie in the forbidden
matching, so the arm cannot occur in a cylinder state. ∎

The common star centre need not be a residual cell and need not be protected;
only the outside arms are absorbed.

## 4. Finite total star absorption

Consider a monotone sequence of secant-star executions.  At step `i`, let `G_i`
be the number of free arms absorbed, so protected size grows by `2G_i`.  Let
`k_0` be the initial protected size.

### Theorem CMR614 — PROVED

One has

\[
\boxed{
2\sum_iG_i
\le
n-k_0.
}
\]

For every integer `G_0>=1`, the number of executions with

\[
G_i\ge G_0
\]

is at most

\[
\boxed{
\left\lfloor
\frac{n-k_0}{2G_0}
\right\rfloor.
}
\]

### Proof

Every absorbed arm contributes two new edges to the same protected partial
matching.  Its size cannot exceed `n`. ∎

Thus large compatible star-arm banks can be consumed only finitely often.

## 5. Square-root star execution

### Theorem CMR615 — PROVED

Put

\[
D
=
\max\{2,\lceil\sqrt M\rceil\}.
\]

Every `M`-arm secant star reaches at least one of the following endpoints.

1. **Square-root matching-vertex wall.**  One source or target vertex is
   incident with at least `D` star arms.
2. **Bulk star absorption.**  Put
   \[
   R
   =
   \left\lceil
   \frac{M}{4(D-1)}
   \right\rceil.
   \]
   The protected matching grows by at least
   \[
   \boxed{
   2\max\{0,R-2k\}
   }
   \]
   outside star cells.
3. **Large protected core.**  If the bulk-growth lower bound is zero, then
   \[
   \boxed{k\ge R/2.}
   \]

### Proof

Apply CMR611 with the displayed threshold.  In its compatible-family branch,
apply CMR612--CMR613.  If `R-2k<=0`, then `k>=R/2`. ∎

Ignoring integer rounding, the nonwall family has order `\sqrt M`, so either a
comparable compatible subbank is absorbed or the core already has comparable
size.

## 6. Canonical secant-star endpoint

### Corollary CMR616 — PROVED

Every fixed owned secant-star certificate produced by CMR560, CMR564, CMR565,
or CMR569 reaches one of:

1. a fixed matching-vertex wall;
2. simultaneous protected absorption of a matching-compatible arm subbank;
3. a protected core large relative to the extracted arm family.

The absorption branch has the finite total budget of CMR614.  The wall branch
enters the protected-contact and heavy/dispersed token ledgers CMR584--CMR592.

### Proof

Apply CMR611--CMR615 and retain the canonical selector owner throughout. ∎

## 7. Revised frontier

Both fixed single-line and fixed secant-star collateral now have direct
protected executions.

- Heavy lines absorb every cell outside the protected core.
- Secant stars yield a matching-vertex wall or absorb a matching-compatible arm
  bank with two protected edges per arm.
- Total fresh absorption in both branches is bounded by residual matching
  capacity.
- Failure of substantial absorption certifies a large protected core.

The remaining owned-certificate branches are fixed matching walls, heavy or
dispersed prefix/carry cells, and persistent unavailable cores after protected
capacity becomes large.  The next progress theorem should convert large
protected-core size or repeated fixed wall/token use into Hall factorization,
reserve depletion, deletion ancestry, full-token return, or envelope expansion.

No all-`n` theorem is claimed.  Vertex-degree extraction, compatible-arm
packing, protected-touch counting, bulk growth, and square-root thresholds are
checked in
[`scripts/verify_prime_power_secant_star_absorption.py`](../scripts/verify_prime_power_secant_star_absorption.py).
