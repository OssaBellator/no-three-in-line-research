# Hall walls in frozen parent covers

CMR198 forces linearly many real-line signatures, but the union of candidate
cells has an even sharper structure. Because every parent derangement must use
at least one candidate cell from some certificate, those cells form a blocker
of the derangement matching problem. Hall's theorem turns every such blocker
into a dense source-row by target-column wall.

Fix one nonroot one-layer parent board of size `t>=5`. Let `U` be the set of all
nonfixed parent-board cells which occur in at least one rank-one, rank-two, or
rank-three candidate certificate.

## 1. Exact Hall rectangle

### Theorem CMR199 — PROVED

If the candidate cylinders cover every parent derangement, then there are a
source set `A` and a target set `T` such that

\[
|A|+|T|>t
\]

and every off-diagonal cell of

\[
A\times T
\]

belongs to `U`.

### Proof

Delete from the complete parent board both the old diagonal and every cell of
`U`. If the remaining graph had a perfect matching, that matching would be a
derangement using no candidate cell from any certificate and would therefore
be uncovered. Hence the remaining graph has no perfect matching.

By Hall's theorem there is a source set `A` whose allowed neighbourhood `N(A)`
satisfies

\[
|N(A)|<|A|.
\]

Put

\[
T=[t]\setminus N(A).
\]

Then

\[
|T|=t-|N(A)|>t-|A|,
\]

so `|A|+|T|>t`. By the definition of `T`, every cell of `A times T` is deleted.
The only deleted cells not in `U` are old diagonal cells. Hence every
off-diagonal cell of the rectangle lies in `U`. ∎

This is the exact matching-theoretic form of a frozen parent obstruction.

## 2. A half-full board row or column

### Corollary CMR200 — PROVED

Some source row or target column contains at least

\[
\boxed{
\left\lfloor\frac t2\right\rfloor
}
\]

distinct cells of `U`.

After assigning each such cell one certificate containing it, one rank
`r in {1,2,3}` occurs on at least

\[
\boxed{
W(t)=
\left\lceil
\frac{\lfloor t/2\rfloor}{3}
\right\rceil
}
\]

distinct wall cells.

### Proof

Let `a=|A|` and `b=|T|` in CMR199. If `a<=b`, each source row in `A` contains at
least `b-1` off-diagonal rectangle cells, and

\[
b-1
\ge
\left\lceil\frac{t+1}{2}\right\rceil-1
=
\left\lfloor\frac t2\right\rfloor.
\]

If `b<a`, use a target column in `T` instead. Assign one containing certificate
to each supported wall cell and apply the three-rank pigeonhole principle. ∎

A certificate of rank two or three contains at most one cell of one fixed
source row or target column, because its candidate cells are matching
compatible. Thus the assigned certificates in those ranks are distinct.

## 3. Neutralizing rank-one and rank-two walls

### Theorem CMR201 — PROVED

Let `M>=1` distinct cells in one fixed parent source row or target column be
assigned certificates of one common rank.

1. If the rank is one, the certificates expose an alternating endpoint bank
   neutralizing at least
   \[
   \left\lceil
   \frac12
   \max\left\{1,
   \left\lfloor\sqrt{\frac M2}\right\rfloor
   \right\}
   \right\rceil
   \]
   of them.
2. If the rank is two, an alternating endpoint bank neutralizes at least
   \[
   \left\lceil\frac M2\right\rceil
   \]
   of them.

The banks preserve saturation and layer disjointness and may be padded to four
endpoints when necessary.

### Proof

For rank one, choose the two fixed selected secant endpoints of each
certificate. As in CMR188, distinct wall cells give distinct secant pairs. The
matching-or-star argument applied to the `M`-edge secant graph gives either a
matching or a star of size

\[
r=
\max\left\{1,
\left\lfloor\sqrt{M/2}\right\rfloor
\right\}.
\]

One permutation layer supplies movable endpoints for at least `ceil(r/2)` of
those certificates. Move them with CMR128.

For rank two, every assigned certificate has exactly one fixed selected point.
At least `ceil(M/2)` of the certificates have that fixed point in one common
permutation layer. Let `B` be the set of distinct such fixed points. Rematching
all points of `B`, padded to four endpoints if necessary, removes every old
cell in `B`. Each of the selected certificates contains its assigned fixed
point in `B`, so all selected certificates are destroyed. Repeated use of one
fixed point only increases the number neutralized by the same move. ∎

## 4. The sole wall obstruction is candidate-only

### Corollary CMR202 — PROVED

Every globally frozen nonroot parent cover has at least one of the following
three structures, where `W(t)` is defined in CMR200.

1. **Rank-one secant wall.** An explicit alternating bank neutralizes at least
   the CMR201 square-root number of wall certificates.
2. **Rank-two anchored wall.** An explicit alternating bank neutralizes at least
   `ceil(W(t)/2)` wall certificates.
3. **Rank-three candidate-only wall.** One source row or target column contains
   `W(t)` distinct cells, each lying in a distinct rank-three candidate triple.

### Proof

Apply CMR200 and split according to the majority rank. CMR201 handles ranks one
and two. In rank three, compatibility implies that one candidate triple uses at
most one cell of the fixed wall, so the assigned triples are distinct. ∎

Thus the internal no-return problem has been reduced again: every wall with a
fixed selected anchor is executable. The only non-executable Hall wall is a
candidate-only population of rank-three line triples.

## 5. Revised remaining theorem

The next proof should combine the rank-three wall with one of the existing
candidate-only endpoints:

- a product-state conflict regularization theorem;
- a line-matching avoidance bank on the parent derangement board;
- a primitive-direction/carry dispersion bound for the `W(t)` wall cells; or
- simultaneous resampling of several Hall walls.

No all-`n` theorem is claimed here. Hall rectangles, half-wall arithmetic, and
small blocker examples are checked in
[`scripts/verify_prime_power_parent_hall_walls.py`](../scripts/verify_prime_power_parent_hall_walls.py).
