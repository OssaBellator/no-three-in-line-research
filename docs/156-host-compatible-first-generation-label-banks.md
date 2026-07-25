# Host-compatible label lifts of first-generation decoder banks

PX411--PX419 replace channel-based terminal moves by exact permutations of one
rectangle column labeling `t` or `r`.  This chapter lifts the three
first-generation geometric outcomes--clean stars, radial cores, and loaded
lines--to the same invariant-preserving label banks.

The lift has two key properties.  First, one of the four rectangle point types
`T_0,T_1,R_0,R_1` carries a constant fraction of every endpoint family, so the
chosen endpoints have distinct rectangle source labels.  Second, one label
assignment inserts a pair of points in one scalar column.  Saturation implies
that no created triple can use both points of that pair.  Every prospective
triple therefore depends on one, two, or three distinct label assignments and
obeys the ordinary permutation-cylinder denominator `(s)_r`.

The result verifies row/column saturation, layer disjointness, rectangle normal
form, and factor-host membership for the first-generation neutralizations.  The
remaining invariant problem is the paired-copy version of the support-four
packet and mixed two-block decoders.

## 1. Four exact point types

Use the address notation of PX411:

\[
T_0(u),\ T_1(u),\ R_0(u),\ R_1(u).
\]

Call these the four **rectangle point types**.  A point of type `T_epsilon`
uses the label variable `t(u)` and a point of type `R_epsilon` uses `r(u)`.

### Theorem PX420 -- PROVED

Let `E` be any finite set of selected point incidences in a rectangle state.
One rectangle point type occurs at least `|E|/4` times.

Within one fixed type, distinct selected points have distinct source labels,
scalar rows, and scalar columns.

### Proof

Pigeonhole over four types.  For fixed type, the source-to-point map is
injective by PX411. \(\square\)

## 2. Clean-star source extraction

Let

\[
\{P_j,Q_j\},\qquad 1\le j\le M,
\]

be an endpoint-disjoint clean secant star.  If a fixed parent move removes a
set `R` of at most `b` selected points, first discard star pairs meeting `R`.

### Theorem PX421 -- PROVED

There is a rectangle point type and a set of source labels `U` of order

\[
\boxed{
|U|
\ge
\left\lceil\frac{M-b}{4}\right\rceil
}
\]

such that one endpoint from each of `|U|` surviving star pairs has that type.
Permuting the corresponding label variable on `U` by a derangement moves every
chosen endpoint and destroys every assigned star triple.

### Proof

At least `M-b` endpoint-disjoint pairs survive.  Choose one arbitrary endpoint
incidence from each pair and pigeonhole those incidences over the four point
types.  Fixed type gives distinct source labels by PX420.  A label derangement
moves the chosen endpoint in its scalar row.  Its clean secant line is not the
scalar row and meets that row only at the original cell, so the assigned triple
is destroyed. \(\square\)

Using both endpoint incidences before pigeonholing gives the same constant up
to harmless rounding; the stated form avoids duplicate-pair bookkeeping.

## 3. Loaded-line source extraction

Let a nonaxis real line `ell` contain `k>=3` selected points.

### Theorem PX422 -- PROVED

One rectangle point type contributes a source set `U` of order

\[
\boxed{|U|\ge\left\lceil\frac k4\right\rceil.}
\]

For a fixed source `u`, at most two target labels `v` place either paired
replacement point of `u -> v` on `ell`.  For a fixed target label `v`, at most
one source label places a paired point on `ell`.

Thus the label assignments meeting `ell` form a forbidden bipartite graph of
source degree at most two and target degree at most one.  Adding the current
label diagonal and inherited historical restrictions gives a bounded-forbidden
label-permutation bank in which every state moves all chosen points off `ell`.

### Proof

Pigeonhole the `k` line points over four types.  The line is neither a scalar
row nor scalar column because saturation gives only two selected points on an
axis line.

For source `u`, the paired assignment uses two fixed scalar rows.  The line
meets each row at at most one scalar column, hence at most two target labels.
For target `v`, the paired assignment occupies one scalar column.  A nonvertical
line meets that column in at most one of the `2n` scalar rows, determining at
most one source/copy and hence one source label. \(\square\)

Every old line triple containing a chosen point is deleted.  If `m=|U|`, the
old line retains at most `k-m` selected points and the exact line destruction is
at least

\[
\boxed{
\binom k3-\binom{k-m}{3}.
}
\]

## 4. Radial-core source extraction

Let `z` be an outside point and let `L_1,...,L_q` be distinct radial lines,
each carrying a designated old triple.  Choose one selected endpoint on each
line, with all chosen endpoints distinct.

### Theorem PX423 -- PROVED

One rectangle point type supplies distinct source labels on at least

\[
\boxed{\left\lceil\frac q4\right\rceil}
\]

radial lines.  A derangement of the corresponding `t`- or `r`-labels moves the
chosen point off its original radial line and destroys every assigned radial
certificate.

### Proof

Pigeonhole the chosen endpoints over four types.  Distinct radial lines through
an outside centre have disjoint selected point sets.  The chosen line is not a
scalar row because it contains at least three selected points, while saturation
places two points in a scalar row.  A changed label value moves the endpoint to
a different cell of its row, off the unique radial-line intersection. \(\square\)

## 5. Spread and inherited constraints

Let `U` be any source set extracted above and let `Delta_lab` be its inherited
label forbidden degree, including line avoidance when relevant.

### Theorem PX424 -- PROVED

If `|U|>=2 Delta_lab`, an allowed label permutation exists.  If the residual
order is at least `8 Delta_lab+2`, the uniform optimized bank satisfies

\[
\boxed{
\Pr(E\subseteq\pi)
\le
\frac{\mathcal C(|U|,\Delta_{\rm lab})}{(|U|)_r}
\le
\frac{e^{2\Delta_{\rm lab}}}{(|U|)_r}
}
\]

for every compatible rank-`r` partial label assignment.

Every bank state remains an exact factor-compatible rectangle state.

### Proof

PX415 bounds inherited geometric partial matchings at label level, and PX422
adds source degree two/target degree one in the loaded-line case.  Apply
PX200 and PX232--PX233.  Factor compatibility is PX412. \(\square\)

## 6. Paired assignments do not collapse certificate rank

A selected label assignment `u -> v` inserts two points in one scalar column.

### Theorem PX425 -- PROVED

No collinear triple in a saturated state obtained from a label-permutation bank
contains both inserted points belonging to one label assignment.

Consequently every prospective created triple uses points from exactly
`r in {1,2,3}` distinct label assignments, and its occurrence is a rank-`r`
label-permutation cylinder.

### Proof

The two paired points are the complete selected population of their scalar
column.  Their line is that column.  A third selected point in the same state
cannot lie in that column because saturation gives column degree exactly two.
Thus a triple uses at most one point from each paired assignment.  The distinct
assignments have distinct source and target labels, so they form a compatible
partial permutation. \(\square\)

This removes the principal concern created by moving the paired copy: it adds
more candidate cell choices but never lowers the cylinder rank.

## 7. Constant-copy collateral transfer

For a rank-`r` label partial permutation, every assignment contributes one of
two row-copy points to a prospective triple.  There are at most `2^r` copy
patterns.

### Theorem PX426 -- PROVED REDUCTION

Every weighted rank-at-most-three collateral family for an individual-endpoint
bank lifts to the paired label bank as at most

\[
\boxed{2^r\le8}
\]

copy-pattern families in rank `r`, with the same label support and the same
falling-factorial cylinder denominator.

In particular:

1. rank-one and rank-two external blocker ledgers change only by absolute
   constant factors;
2. internal rank three remains rank three and gains at most a factor eight in
   candidate weight;
3. all support-excess thinning exponents are unchanged;
4. the hybrid-thinning conclusion `o(s)` for support-five/six internal rank
   three remains `o(s)`;
5. constant-scale support-three/four internal rank three remains constant-scale.

### Proof

Partition every geometric certificate by the copy choice of each participating
label assignment.  PX425 gives distinct label assignments, so each part is a
rank-`r` label cylinder.  There are `2^r` parts.  Multiplying a constant or an
`o(s)` bound by at most eight preserves its scale, while endpoint-index support
is unchanged. \(\square\)

The theorem is purely a spread and scale transfer.  Exact product-packet
identities involving two paired copies still require a separate audit.

## 8. Host-compatible first-generation interface

### Theorem PX427 -- PROVED REDUCTION

Every clean-star, radial-core, or loaded-line outcome in a rectangle-compatible
repair state admits a factor-compatible `t/r` label-permutation neutralization
with:

1. a source block of at least one quarter the original endpoint order, up to the
   fixed parent-support deletion;
2. exact assigned old destruction as in PX240--PX243;
3. bounded-forbidden optimized spread;
4. no certificate-rank collapse from the paired copy;
5. internal rank-three and support-excess estimates differing only by absolute
   constants.

Therefore these three large-block outcomes can remain inside the rectangle
product state space.  The remaining product-invariant frontier is the paired
label treatment of:

- support-four product packets;
- mixed two-block shadows;
- packet-complement recurrence constraints.

Until those sectors are lifted, PX427 is not a complete invariant-preservation
theorem for the full decoder.

## 9. Verification

Run

```bash
python scripts/verify_product_first_generation_label_lift.py
```

The verifier checks four-type extraction, line-forbidden label degrees, radial
and star source distinctness, saturation under label permutations, the exact
loaded-line destruction formula, and the impossibility of a triple using both
paired points from one assignment.
