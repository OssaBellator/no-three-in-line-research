# PX63 entry via one-hit rectangle thinning and derangement banks

PX393--PX396 splice the large-block and terminal-return mechanisms under an
entry axiom: every unresolved obstruction produced by the original product
induction must enter a large matching block, an actual order-one/two terminal
block, or a finite base case.  The exact source theorem is PX63.  It produces a
factor-compatible rectangle state with `O(n log n)` bad triples, but it does not
itself identify a repair block.

This chapter verifies the missing entry axiom directly.  Randomly retain
rectangle indices with probability one third.  Every bad triple, whether it
uses two or three rectangle indices, is hit in exactly one rectangle with
probability exactly `4/9`.  The uniquely hit triples can then be assigned to one
of the two column-label permutations `t,r`.  Permuting the selected values of
that one labeling by a derangement preserves the rectangle normal form and
moves exactly one rectangle of every assigned triple.

A constant-density subbank destroys a fixed fraction of all current bad
triples and has constant fixed-rank cylinder spread.  Its order is the exact
entry block: large orders enter PX334--PX335, intermediate orders enter the
nested recurrence PX263--PX266, and orders one or two enter the actual terminal
buffer interface PX341--PX392.

## 1. Exact one-hit thinning of rectangle conflicts

Let `Q=Q(p,t,r)` be any rectangle state on rectangle index set `[n]`.  Let
`D=D(Q)` be its number of bad triples, counted geometrically.  By PX44, the
rectangle-index support of a bad triple has order two or three.

Choose every rectangle index independently with probability `1/3` and call the
selected set `A`.

### Theorem PX397 -- PROVED

There is a deterministic set `A subseteq [n]` for which at least

\[
\boxed{\frac{4D}{9}}
\]

bad triples meet `A` in exactly one rectangle index.

### Proof

If a bad triple has support order `s in {2,3}`, then

\[
\Pr(|\operatorname{supp}(T)\cap A|=1)
=
s\frac13\left(\frac23\right)^{s-1}
=
\frac49.
\]

Linearity of expectation gives expected one-hit count `4D/9`, so one
realization attains at least that value. \(\square\)

Call this one-hit family `C_A`.  For every `T in C_A`, let `v(T)` be its unique
rectangle index in `A`.

## 2. One column family carries constant destruction

Every selected point of a rectangle uses exactly one of the two column
labelings `t` or `r`.  Choose one point of `T` lying in rectangle `v(T)`, and
assign `T` to the corresponding column family.

### Theorem PX398 -- PROVED

One family

\[
\xi\in\{t,r\}
\]

receives a subfamily `C_xi subseteq C_A` of total weight

\[
\boxed{
W:=|C_\xi|\ge\frac{2D}{9}.
}
\]

Let

\[
C=\{v(T):T\in C_\xi\},
\qquad c=|C|.
\]

For every assigned triple `T`, its chosen `xi`-point is the only point of `T`
whose rectangle index lies in `C`.

### Proof

Pigeonhole the at least `4D/9` one-hit triples over the two column families.
The other rectangle indices of an assigned triple lie outside `A`, while
`C subseteq A`.  Hence no other point of the triple has rectangle index in
`C`. \(\square\)

The same source rectangle may carry many assigned triples; this multiplicity is
retained in `W`.

## 3. Host-compatible derangement bank

Assume `c>=3`.  Let `Omega(C)` be the derangements of `C`.  For
`pi in Omega(C)`, replace the chosen column labeling by

\[
\xi_\pi(v)=
\begin{cases}
\xi(\pi(v)),&v\in C,\\
\xi(v),&v\notin C,
\end{cases}
\]

and leave `p` and the other column labeling unchanged.

### Theorem PX399 -- PROVED

Every `pi in Omega(C)` gives a factor-compatible saturated rectangle state in
the same orientation and full product host as `Q`.

Moreover,

\[
\boxed{|\Omega(C)|={!c}\ge\frac{c!}{3}}
\]

and, under the uniform measure on `Omega(C)`, every compatible prescribed
partial permutation of rank `r` has probability at most

\[
\boxed{\frac{3}{(c)_r}}.
\]

### Proof

The map `xi_pi` is a permutation because `pi` permutes `C` and is the identity
outside it.  PX43 and PX61 therefore show that `(p,t_pi,r)` or `(p,t,r_pi)` is
again a normalized factor-compatible rectangle state.  Saturation follows from
the rectangle normal form.

For `c>=3`, the derangement recurrence or inclusion--exclusion gives
`!c>=c!/3`.  At most `(c-r)!` permutations contain a prescribed compatible
rank-`r` partial permutation.  Dividing by the derangement count proves the
cylinder bound. \(\square\)

## 4. Assigned old destruction

Fix `T in C_xi` with unique selected source rectangle `v=v(T)`.  The other two
points of `T` remain fixed under every `pi in Omega(C)`.  The chosen point of
`T` stays in its scalar row and receives column value `xi(pi(v))`.

### Theorem PX400 -- PROVED

For every assigned triple `T`, at most one target

\[
w\in C\setminus\{v(T)\}
\]

preserves its collinearity.  Hence a uniform derangement satisfies

\[
\Pr(T\text{ survives})\le\frac1{c-1}.
\]

Consequently the expected assigned destruction is at least

\[
\boxed{
\mathbb E X
\ge
\frac{c-2}{c-1}W
\ge
\frac W2
\ge
\frac D9.
}
\]

### Proof

The line through the other two points is not a scalar-row line, since a scalar
row contains exactly two selected points.  It therefore meets the fixed row of
the moved point in at most one column.  Because `xi` is a permutation, at most
one target index `w` realizes that column.

In a uniform derangement, `pi(v)` is uniform on `C\setminus{v}` by symmetry.
The survival bound follows, and linearity of expectation gives the displayed
destruction estimate. \(\square\)

## 5. Constant-density good subbank

Let `X(pi)` be the number of assigned triples destroyed by `pi`.

### Theorem PX401 -- PROVED

At least one third of the derangements satisfy

\[
\boxed{X(\pi)\ge\frac W4\ge\frac D{18}.}
\]

Let `Omega_good(C)` be this good subbank.  Then

\[
\boxed{|\Omega_{\rm good}(C)|\ge\frac{c!}{9}}
\]

and every compatible rank-`r` cylinder satisfies

\[
\boxed{
\Pr(E\subseteq\pi\mid\pi\in\Omega_{\rm good}(C))
\le
\frac9{(c)_r}.
}
\]

Every state in the good bank destroys at least `D/18` old triples.

### Proof

We have `0<=X<=W` and `E X>=W/2`.  If

\[
p=\Pr(X\ge W/4),
\]

then

\[
\mathbb E X
\le
pW+(1-p)\frac W4
=
\frac W4+\frac{3pW}{4}.
\]

Thus `p>=1/3`.  Combine this density with `|Omega(C)|>=c!/3` to get the count.
A prescribed rank-`r` cylinder occurs in at most `(c-r)!` permutations, so
conditioning on the good bank gives the factor nine. \(\square\)

## 6. Exact entry classification

### Theorem PX402 -- PROVED REDUCTION

Every non-no-three rectangle state `Q` has one of the following entry objects.

1. **Large or nested column-permutation block:** `c>=3`, with a
   factor-compatible good bank of order `c`, cylinder factor nine, and guaranteed
   old destruction at least `D/18` in every bank state.
2. **Actual terminal block:** `c in {1,2}`, carrying assigned old weight at least
   `2D/9` and having the same diagonal-plus-opposite-layer base structure as the
   order-one/two endpoint terminals of PX341--PX392.

For any prescribed large-block threshold `B(n)`, case 1 enters PX334--PX335 when
`c>=B(n)`; when `3<=c<B(n)`, it is a legitimate root block for the nested
recurrence PX263--PX266; case 2 enters the actual terminal-return interface.

### Proof

PX397--PX398 construct `C` and its assigned weight.  PX399--PX401 handle
`c>=3`.  If `c<=2`, freeze the other column labeling and the canonical opposite
permutation layer.  The selected source labels form an order-one/two matching
block with current diagonal and one opposite-layer partial matching, exactly the
base-degree-one terminal structure used by PX341. \(\square\)

## 7. PX63 entry and invariant audit

### Theorem PX403 -- PROVED REDUCTION

The PX63 low-syndrome seed satisfies the entry dichotomy required by axiom 1 of
PX395.

More precisely:

1. PX63 supplies a factor-compatible saturated rectangle state `Q(p,t,r)`.
2. If `D(Q)=0`, exact doubling is complete.
3. If `D(Q)>0`, PX402 supplies a large, nested, or actual terminal matching
   block.
4. Every entry-bank state remains in the same factor-product host, preserves
   exact row and column degree two, preserves the canonical two-layer
   decomposition, and changes only one of the independent label permutations
   `t,r`.
5. The bank carries explicit old destruction `D/18` and fixed-rank spread
   `9/(c)_r`, so no destruction credit is hidden in the splice bookkeeping.

Thus the previously inaccessible PX63 entry statement is now audited directly.
The remaining PX396 checks are:

- the subpower channel and line-occupancy hypotheses along all descendants;
- finite ambient orders below the buffer/divisor thresholds;
- invariant preservation for later non-rectangle endpoint and packet moves.

PX403 is an entry theorem, not exact infinite product closure.

## 8. Verification

Run

```bash
python scripts/verify_product_px63_entry_derangement.py
```

The verifier exhausts and randomly samples rank-two/rank-three rectangle-support
systems, checks the exact `4/9` one-hit bound, enumerates derangements through
order seven, verifies the cylinder constants and marginal uniformity, and tests
the `1/3` good-subbank density for arbitrary assigned exceptional targets.
