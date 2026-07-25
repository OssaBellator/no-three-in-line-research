# Product-packet decoding for paired rectangle label assignments

PX427 leaves one major invariant gap: the support-four packet decoder was
written for a matching bank in which one assignment inserts one geometric cell.
A rectangle label assignment inserts two row-copy cells in one scalar column.
This chapter lifts the packet geometry and selected-defect correction graph to
that paired setting.

Split every candidate label assignment by its row copy.  For a fixed copy, the
usual anchor-product level is a partial matching.  A defect using two different
copies is an equal-product collision between one packet in each typed copy.
Swapping the two target labels corrects the defect and simultaneously moves all
four paired cells.  Disjoint correction transpositions commute, remain exact
rectangle label permutations, and have no three-new-cell internal collateral.

The only exceptional product level is zero.  It consists of cells sharing an
anchor row or column and is already a coordinate-line/rank-one child.  All
nonzero levels retain the ambient divisor and packet-overlap bounds up to an
absolute factor four.

## 1. Typed candidate arcs

Fix one rectangle label family `xi in {t,r}` and a source block `U` of order
`h`.  A label assignment

\[
e=u\to v
\]

inserts the paired cells

\[
e^0=(X_0(u),Y_\xi(v)),
\qquad
e^1=(X_1(p(u)),Y_\xi(v)).
\]

For an outside anchor `z=(a,b)`, define the typed product

\[
P_z^\epsilon(u\to v)
=
(X_\epsilon(u)-a)(Y_\xi(v)-b).
\]

### Theorem PX428 -- PROVED

For fixed `z`, copy `epsilon`, and nonzero product `gamma`, the typed level

\[
\mathcal P_z^\epsilon(\gamma)
=
\{u\to v:P_z^\epsilon(u\to v)=\gamma\}
\]

is a partial matching on the label source and target sets.

### Proof

Fixing `u` determines the nonzero column difference and hence at most one
`Y_xi(v)`, because `Y_xi xi` is injective.  Fixing `v` symmetrically determines
at most one row coordinate `X_epsilon(u)`, because both row-copy maps are
injective. \(\square\)

The zero level is contained in the union of the anchor row and anchor column.
It is sent directly to the coordinate-field or loaded-line decoder and is
excluded from packet notation below.

## 2. Paired-copy cross identity

Let the current label permutation contain assignments

\[
u\to v,
\qquad
s\to w,
\qquad u\ne s,\ v\ne w.
\]

Choose copies `epsilon,delta`.  The selected points

\[
(u\to v)^\epsilon,
\qquad
(s\to w)^\delta
\]

are collinear with `z` exactly when

\[
\boxed{
P_z^\epsilon(u\to w)
=
P_z^\delta(s\to v).
}
\]

### Theorem PX429 -- PROVED

Every old paired-label support-four defect has one unique correcting label
transposition: swap the targets `v,w` of sources `u,s`.

The two crossed assignments selected after the correction contain the typed
packet arcs appearing in the displayed equality.

### Proof

The determinant equation for the two old points and `z` is

\[
(X_\epsilon(u)-a)(Y_\xi(w)-b)
=
(X_\delta(s)-a)(Y_\xi(v)-b).
\]

These are exactly the typed products of the crossed assignments.  The source
pair determines the target swap uniquely. \(\square\)

## 3. Ambient nonzero packet count

Let `mathfrak d(N)` be the divisor cap from PX207 and suppose all scalar
coordinates lie in `[0,N-1]`.

### Theorem PX430 -- PROVED

For one anchor `z`, one ordered copy pair `(epsilon,delta)`, and one typed
candidate arc, the number of opposite typed arcs with the same nonzero product
is at most

\[
\boxed{2\mathfrak d(N).}
\]

Consequently the total nonzero paired-copy support-four weight over all four
copy pairs is at most an absolute factor four times the one-copy ambient bound:

\[
\boxed{
W_{2,4}^{\rm pair}
\le
8|Z|\mathfrak d(N)h^2.
}
\]

### Proof

A fixed nonzero product `m` has at most `2 tau(|m|)` signed factorisations into
an integer row difference and integer column difference.  The typed row and
column coordinate maps are injective, so each factorisation gives at most one
opposite arc.  There are four ordered copy pairs.  Sum over at most `h^2`
first arcs and the anchors. \(\square\)

The constant is deliberately slack.  The adaptive square-root ambient
threshold is unchanged because only an absolute factor is introduced.

## 4. Exact paired correction graph

For an unordered source pair `e={u,s}`, let `w_e` be the total number of old
anchor-weighted packet defects using any of the four copy pairs on sources
`u,s`.  Let `G_corr^pair` be the weighted graph on source labels.

### Theorem PX431 -- PROVED

The full old paired packet mass is exactly

\[
\boxed{
D_{\rm pkt}^{\rm pair}
=
\sum_{e\in E(G_{\rm corr}^{\rm pair})}w_e.
}
\]

A matching `Q` in the correction graph gives commuting disjoint label
transpositions.  Before new collateral is counted, executing all of them
destroys exactly

\[
\boxed{W(Q)=\sum_{e\in Q}w_e}
\]

assigned old packet defects and preserves the exact rectangle product state.

### Proof

PX429 assigns every defect to its unique source-pair transposition.  Disjoint
source pairs define commuting transpositions of the label permutation `xi`.
PX412 preserves rectangle compatibility.  Distinct correction edges move
disjoint source-label pairs, so their assigned old defect sets are disjoint.
\(\square\)

The weighted matching bound PX302 applies without change.

## 5. High correction degree is still clean-star geometry

A source label `u` carries two selected points `u^0,u^1` in the chosen label
family.  Split every defect incident with `u` by the copy of the selected point
used at `u`.

### Theorem PX432 -- PROVED

If the weighted correction degree at source `u` is `mu(u)`, one of its two
selected copy points has incident defect weight at least `mu(u)/2`.

Under selected-line occupancy bound `K`, that point centres an
endpoint-disjoint clean star of order at least

\[
\boxed{
\frac{\mu(u)}{2K}.
}
\]

### Proof

Pigeonhole incident defect weight over the two copy points.  Apply the
anchor--partner star extraction PX303 to the heavier copy. \(\square\)

Thus paired-copy concentration loses only a factor two.

## 6. One paired correction has bounded first-order geometry

One source-pair transposition inserts four new points: two in each of two
scalar columns.  No prospective triple uses three of them, by PX416.

For each of the four new cells `f`, let `mu(f)` be its rank-one secant weight
against fixed points.  Among the six pairs of new cells, the two within-column
pairs cannot form an external triple because their column contains no fixed
selected point.  Let `lambda(g)` be the fixed-point occupancy of the line
through each of the remaining four cross-column pairs.

### Theorem PX433 -- PROVED

The complete first-order creation load of one paired correction is

\[
\boxed{
c_e
=
\sum_{f\in W_e}\mu(f)
+
\sum_{g\in\mathcal X_e}\lambda(g),
}
\]

where `|W_e|=4` and `|mathcal X_e|=4`.

If no prospective new cell centres a clean star of order `T` and no cross-pair
line contains more than `L` fixed points, then

\[
\boxed{
c_e<4KT+4L.}
\]

### Proof

A triple created when only this correction is active contains one or two of its
new cells.  The one-cell cases give the four secant weights.  A two-cell case
using the same new column has no fixed third point by saturation.  The four
cross-column pairs give the remaining terms.  Apply PX228 to each new cell and
the line cap to each cross pair. \(\square\)

## 7. Bernoulli strict sign survives pairing

Let `Q` be a matching of paired corrections and activate its edges
independently with probability `p`.

### Theorem PX434 -- PROVED

The expected potential change satisfies

\[
\boxed{
\mathbb E[\Phi(M_p)-\Phi(M)]
\le
-pW(Q)+pC_1(Q)+p^2C_2(Q)+p^3C_3(Q).
}
\]

If `W(Q)>C_1(Q)`, some deterministic subset of paired corrections strictly
improves the full potential.

### Proof

Disjoint label transpositions commute.  Every created triple uses new points
from at most three activated correction edges.  Internal support one is counted
by PX433, and higher support contributes `p^2` or `p^3`.  The PX305--PX306
argument applies verbatim. \(\square\)

## 8. Paired packet strict-sign-or-child theorem

### Theorem PX435 -- PROVED REDUCTION

For every correction-degree threshold `R` and prospective-star threshold `T`,
a paired packet defect family has at least one of the following outcomes.

1. A selected copy point centres a clean star of order at least `R/(2K)`.
2. A prospective paired-correction cell centres a clean star of order at least
   `T`.
3. A cross-pair line contains more than `L` fixed selected points.
4. A subset of commuting host-compatible label corrections strictly lowers the
   full potential.
5. The total paired packet mass satisfies
   
   \[
   \boxed{
   D_{\rm pkt}^{\rm pair}
   \le
   (2R-1)\frac h2(4KT+4L).
   }
   \]

### Proof

If correction degree is at least `R`, apply PX432.  Otherwise PX302 gives a
correction matching of weight at least
`D_pkt^pair/(2R-1)` and order at most `h/2`.  If items 2 and 3 fail, PX433 bounds
its total first-order load by `|Q|(4KT+4L)`.  Failure of item 5 gives a positive
first-order gap, and PX434 gives item 4. \(\square\)

### Corollary PX436 -- PROVED REDUCTION

The selected-defect packet branch, including the bounded linear residue, admits
factor-compatible rectangle-label corrections.  Pairing changes only absolute
constants and preserves:

- the square-root ambient threshold;
- the correction-graph matching dichotomy;
- Bernoulli strict sign;
- clean-star/loaded-line child outcomes;
- causal ancestor safety through forbidden label assignments.

The remaining paired invariant frontier is the mixed `t/r` two-block shadow and
the exact packet-complement constraint when several typed packet families are
released simultaneously.

## 9. Verification

Run

```bash
python scripts/verify_product_paired_label_packet.py
```

The verifier checks the typed product identity on random integer coordinate
maps, partial-matching levels, exact correction aggregation, four-point
first-order classification, absence of internal triples in one correction, and
the paired strict-sign constants.
