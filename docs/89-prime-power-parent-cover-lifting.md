# Lifting inherited four-core covers to the full parent bank

CMR181--CMR185 classify the nine-state derangement board carried by an
inherited nonroot four-core. The containing prefix envelope has a much larger
one-layer parent bank: all derangements of its `t` columns and inherited rows.
This chapter proves that a terminal cover cannot remain a four-cell phenomenon
inside that parent bank.

Throughout, `t>=5`, and `Omega_t` is the set of derangements of `t` objects.
A rank-`r` cylinder is the set of derangements containing one compatible
partial matching of `r` nonfixed cells, where `1<=r<=3`.

## 1. Minimum covers of a full derangement bank

### Theorem CMR186 — PROVED

Every cylinder cover of `Omega_t` by rank-one, rank-two, and rank-three
cylinders contains at least

\[
\boxed{t-1}
\]

distinct cylinders.

If a cover has exactly `t-1` cylinders, then all of them have rank one and they
are precisely either

- all `t-1` nonfixed cells in one source row; or
- all `t-1` nonfixed cells in one target column.

Thus the unique minimum-cover geometries are a complete row shadow and a
complete column shadow.

### Proof

By CMR176, a rank-one cylinder has exact measure `1/(t-1)` under the uniform
derangement law. Rank-two and rank-three cylinders have measure at most

\[
\frac{30}{11(t)_r}<\frac1{t-1}
\]

for `t>=5`. Hence every cylinder has at most `|Omega_t|/(t-1)` states. Covering
all of `Omega_t` requires at least `t-1` cylinders.

Suppose equality holds. Every cylinder must then have maximum size, so every
one has rank one. Equality in the union bound also forces their state sets to
be pairwise disjoint.

Two nonfixed cells in distinct source rows and distinct target columns extend
to one common derangement. Indeed, prescribe those two cells and remove their
rows and columns. On the remaining `t-2` by `t-2` board, the forbidden fixed
positions form a partial matching. Its complement has a perfect matching, so
the prescription extends to a derangement. Therefore two disjoint rank-one
cylinders must share a source row or share a target column.

A pairwise-intersecting family of edges in a bipartite graph has one common
endpoint: after two edges share a source row, any edge meeting both must also
use that row unless the two target endpoints coincide. Hence all `t-1` chosen
cells share one source row or one target column. Those are exactly all the
nonfixed cells at that endpoint. ∎

## 2. A uniform lifting deficit for every terminal Pareto profile

Choose any Pareto-minimal terminal subcover from CMR185, and let
`(u_1,u_2,u_3)` be its profile. Regard the same prescribed cells as cylinders
inside the full parent bank `Omega_t`.

### Theorem CMR187 — PROVED

The parent-law measure covered by the chosen terminal subcover is at most

\[
U_t(u_1,u_2,u_3)
=
\frac{u_1}{t-1}
+
\frac{30u_2}{11(t)_2}
+
\frac{30u_3}{11(t)_3}.
\]

For every one of the sixteen profiles in CMR185 and every `t>=5`,

\[
\boxed{U_t\le\frac9{11}.}
\]

Consequently, if all parent derangements are covered by candidate
certificates, then certificates outside the chosen terminal subcover have
union measure at least

\[
\boxed{\frac2{11}.}
\]

Their expected incidence under the parent law is also at least `2/11`.
Moreover, if the terminal subcover has `q=u_1+u_2+u_3` cylinders, then the full
parent cover contains at least

\[
\boxed{t-1-q}
\]

additional distinct cylinders.

### Proof

The displayed upper bound is the union bound together with the exact rank-one
law and the rank-two/rank-three bounds from CMR176.

At `t=5`, direct substitution in the sixteen profiles gives maximum `9/11`,
attained by `(0,6,0)`. For `t>=6`, multiply by `t-1`:

\[
(t-1)U_t
=
u_1+\frac{30u_2}{11t}
+\frac{30u_3}{11t(t-2)}.
\]

For each of the sixteen fixed profiles this expression decreases with `t`.
Direct substitution at `t=6` gives value at most `3`; hence

\[
U_t\le\frac3{t-1}\le\frac35<\frac9{11}
\]

for every `t>=6`.

If the full candidate family covers every parent state, the complement of the
chosen terminal subcover must be covered by the remaining certificates. Its
measure is at least `1-9/11=2/11`. Expected incidence dominates union measure.
Finally CMR186 gives at least `t-1` distinct cylinders in total, of which the
chosen subcover uses `q`. ∎

This is a genuine finite-to-parent expansion: even the most expensive terminal
profile cannot explain more than `9/11` of the inherited parent bank.

## 3. The extremal parent cover exposes a secant fan

Suppose equality holds in CMR186. For each cell in the complete row or column
shadow, choose one geometric rank-one certificate: the candidate cell together
with its two fixed selected secant endpoints.

### Theorem CMR188 — PROVED

The `t-1` chosen secant pairs are distinct. Put

\[
r(t)=\left\lfloor\sqrt{\frac{t-1}{2}}\right\rfloor,
\qquad
m(t)=\left\lceil\frac{r(t)}2\right\rceil.
\]

The secant-pair graph contains either

1. a matching of `r(t)` pairs; or
2. a star of `r(t)` pairs.

In either case one can choose `m(t)` distinct certificate endpoints in one
permutation layer, one from each of `m(t)` different shadow certificates. After
padding to at least four endpoints, CMR128 gives an alternating endpoint bank
which moves all chosen endpoints and destroys all `m(t)` chosen shadow
certificates.

### Proof

In a complete source-row shadow, the candidate cells lie at distinct heights
in one grid column. The same fixed secant pair cannot certify two of them unless
its line is that vertical grid column. But the moved layer contributes the only
selected point removed from that column, and the fixed outside set contains at
most the one opposite-layer point there. Hence no fixed pair lies on that
vertical line. The target-column case is identical with rows and horizontal
lines. Thus the chosen secant pairs are distinct edges of a simple graph.

Let `q` be the size of a maximal matching in this graph. If `q>=r(t)`, take
`r(t)` disjoint edges. Otherwise the endpoints of the maximal matching cover
all `t-1` edges, so some endpoint has degree at least

\[
\frac{t-1}{2q}
>
\frac{t-1}{2r(t)}
\ge r(t).
\]

This gives the required star.

In the matching case, one permutation layer supplies at least `r(t)` of the
`2r(t)` endpoint incidences. Since one edge supplies at most two such
incidences, at least `m(t)` edges have an endpoint in that layer. Choose one
from each. In the star case, among the `r(t)` distinct leaves one layer contains
at least `m(t)` leaves. Again choose them.

The chosen points are distinct points of one permutation layer, hence occupy
distinct rows and columns. Pad within that layer if fewer than four were chosen
and apply CMR128. Every chosen old endpoint cell is forbidden, so the
corresponding fixed secant certificate is absent in every bank state. ∎

The bank may enlarge the closure envelope if some chosen secant endpoint lies
outside it. CMR174 then pays that event by a strict decrease in envelope depth.
If all chosen endpoints lie inside the envelope, the theorem produces a new
alternating continuation inside the same epoch.

## 4. Parent-cover dichotomy for a frozen inherited core

### Corollary CMR189 — PROVED

Let a nonroot inherited four-core lie in a saturated global-minimum state, and
let its one-layer envelope parent have size `t>=5`. Every parent derangement
moves the designated target endpoint, so global minimality forces the candidate
certificates to cover all parent states.

At least one of the following holds.

1. **Extremal secant fan.** The full parent cover has exactly `t-1` distinct
   cylinders. It is a complete rank-one row or column shadow and exposes the
   CMR188 alternating bank neutralizing `m(t)` shadow certificates.
2. **Strict parent expansion.** The full parent cover has at least `t` distinct
   candidate cylinders.

In both cases, relative to any chosen terminal Pareto subcover, additional
certificates carry parent-law union measure and expected incidence at least
`2/11`.

### Proof

The designated target is destroyed by every envelope derangement because its
old cell belongs to the moved layer block, and the inherited opposite-layer row
fibre is disjoint. If the current state is a global minimum, every parent state
must create at least one new real triple. Hence its candidate cylinders cover
`Omega_t`.

Apply CMR186. Equality gives the first alternative and CMR188. Otherwise the
integer number of distinct cylinders is at least `t`. The final assertion is
CMR187. ∎

## 5. Revised remaining endpoint

A terminal inherited core cannot remain supported only on its four-point
board. Lifting to the canonical envelope parent forces either

- a complete parent secant fan with an explicit alternating neutralization
  bank; or
- linear growth to at least `t` distinct parent candidate cylinders.

The remaining theorem is to iterate this expansion inside one envelope epoch:
show that repeated strict parent-cover growth exceeds the quotient/carry
collateral budget, or that a secant-fan continuation forces a strict envelope
expansion before a balanced cycle can close.

No all-`n` theorem is claimed here. The finite profile arithmetic, minimum-cover
checks, and extraction thresholds are verified in
[`scripts/verify_prime_power_parent_cover_lifting.py`](../scripts/verify_prime_power_parent_cover_lifting.py).
