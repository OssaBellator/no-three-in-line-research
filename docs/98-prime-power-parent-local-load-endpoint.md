# A matching-space local-load endpoint for inherited parent banks

The Hall-wall argument treats the support of a frozen parent cover. The
matching-space local lemma from `docs/15-degree-constrained-hypergraph-selection.md`
gives a stronger weighted contrapositive. Applied to one inherited parent
layer, it isolates the remaining obstruction as a cubic candidate-only load at
one parent row or column.

Fix one nonroot one-layer envelope parent of size `t>=5`. Its columns and
inherited rows form a complete `t` by `t` matching board. The opposite-layer
row fibre is disjoint. Let `X` be the fixed selected points outside the moved
layer block.

For `r=1,2,3`, let `\mathcal F_r` be the set of distinct compatible rank-`r`
partial matchings of board cells which support at least one real collinear
triple after adding `3-r` points of `X`. Repeated geometric triples with the
same board prescription define one canonical bad event and are counted once.

For a board vertex `v` on either side, put

\[
T_r(v)=
|\{F\in\mathcal F_r:v\in V(F)\}|.
\]

## 1. Exact parent local-load theorem

### Theorem CMR219 — PROVED

If every board vertex satisfies

\[
\boxed{
\frac1t
+
\frac{T_1(v)}t
+
\frac{T_2(v)}{(t)_2}
+
\frac{T_3(v)}{(t)_3}
\le
\frac1{24},
}
\]

then there is a parent permutation which

1. avoids every old diagonal cell;
2. creates no real triple touching the replacement block;
3. preserves saturation and layer disjointness.

Consequently it destroys every old triple touching the block and strictly
lowers the triple potential whenever that population is nonzero.

### Proof

Choose a uniformly random perfect matching of the complete `t` by `t` board.
Use two kinds of canonical bad events.

1. For each old diagonal cell, forbid its singleton matching event. Its
   probability is `1/t`.
2. For each `F in mathcal F_r`, forbid the event `F subseteq M`, of probability
   `1/(t)_r`.

For a board vertex `v`, the displayed expression is exactly its total event
probability load. Every event has at most three matching edges and hence at
most six board vertices. The Lu--Szekely matching-space negative-dependency
graph and the proof of Theorem D1 apply verbatim: assign

\[
x_A=2\Pr(A).
\]

If every vertex load is at most `1/24`, then every event sees total adjacent
`x`-mass at most `1/2`, so the lopsided local lemma gives positive probability
that no bad event occurs.

Avoiding the diagonal moves every old block point. Avoiding every canonical
candidate event excludes every possible new real triple touching the block.
The inherited opposite-layer row set is disjoint, so every board permutation
remains layer-disjoint. ∎

## 2. Frozen-state concentration

### Corollary CMR220 — PROVED

If no parent permutation improves the current state, then some board vertex
`v` satisfies

\[
\boxed{
\frac{T_1(v)}t
+
\frac{T_2(v)}{(t)_2}
+
\frac{T_3(v)}{(t)_3}
>
\frac1{24}-\frac1t.
}
\]

For `t>=48`, one rank `r in {1,2,3}` satisfies

\[
\boxed{
\frac{T_r(v)}{(t)_r}>\frac1{144}.
}
\]

### Proof

The first assertion is the contrapositive of CMR219. If `t>=48`, then

\[
\frac1{24}-\frac1t\ge\frac1{48}.
\]

One of three nonnegative rank contributions exceeds one third of this value.
∎

Thus a frozen large parent has one of the explicit populations

\[
T_1(v)>\frac t{144},
\qquad
T_2(v)>\frac{t(t-1)}{144},
\qquad
T_3(v)>\frac{t(t-1)(t-2)}{144}.
\]

## 3. Rank-one and rank-two loads are executable

### Theorem CMR221 — PROVED

Let `v` be the concentrated board vertex from CMR220.

1. If the rank-one alternative holds, there is an alternating endpoint bank
   neutralizing at least
   \[
   \left\lceil
   \frac12
   \max\left\{1,
   \left\lfloor
   \sqrt{\frac{T_1(v)}2}
   \right\rfloor
   \right\}
   \right\rceil
   \]
   distinct rank-one target triples.
2. If the rank-two alternative holds, there is an alternating endpoint bank
   neutralizing at least
   \[
   \left\lceil\frac{T_2(v)}2\right\rceil
   \]
   distinct rank-two target triples.
3. Otherwise one board source row or target column is incident with more than
   \[
   \boxed{
   \frac{t(t-1)(t-2)}{144}
   }
   \]
   distinct candidate-only collinear triples.

### Proof

For rank one, every distinct canonical prescription is one distinct candidate
cell incident with `v`. Choose one fixed secant pair witnessing each event.
The same fixed pair cannot witness two cells in one board row or column unless
its line is horizontal or vertical, which CMR196 excludes. Hence the secant
pairs are distinct, and the matching-or-star argument of CMR188 gives the
stated same-layer movable endpoint bank.

For rank two, choose one fixed selected point witnessing each distinct board
pair prescription. At least half of the chosen fixed-point incidences lie in
one permutation layer. Move all distinct points of that layer which occur in
the chosen incidences, padding to four endpoints if necessary. Every selected
rank-two target loses its fixed point; repetition of one fixed point only
increases the number neutralized by the same move.

The final alternative is the rank-three inequality from CMR220. A rank-three
prescription is exactly one candidate-only board triple. ∎

## 4. Primitive-height concentration

After dividing the common prefix spacing, the inherited parent board is an
affine copy of the integer `t` by `t` grid. Give every nonaxis candidate-only
triple the primitive direction height

\[
H=\max\{|u|,|v|\},
\qquad 1\le H\le t-1.
\]

### Corollary CMR222 — PROVED

In the rank-three alternative of CMR221, some dyadic primitive-height band
contains more than

\[
\boxed{
\frac{t(t-1)(t-2)}
{144\,\lceil\log_2 t\rceil}
}
\]

candidate-only triples incident with the same parent row or column.

### Proof

The height range has at most `ceil(log_2 t)` dyadic bands. Partition the
CMR221 population by its primitive line height and average. ∎

This is the exact fixed-envelope obstruction left by the matching-space local
lemma: a logarithmically localized cubic candidate-only wall. It is compatible
with the reverse-scale programme and no longer contains unavailable-cell,
rank-one, or anchored rank-two ambiguity.

## 5. Revised remaining theorem

A complete internal no-return result may now focus only on the CMR222 band.
One must prove that such a band

- is paid by a first-separation or primitive carry cell;
- exposes several simultaneously resamplable Hall walls;
- violates the inherited line-signature multiplicity bounds;
- or forces strict closure-envelope expansion.

No all-`n` theorem is claimed here. The local-load arithmetic and dyadic
thresholds are checked in
[`scripts/verify_prime_power_parent_local_load.py`](../scripts/verify_prime_power_parent_local_load.py).
