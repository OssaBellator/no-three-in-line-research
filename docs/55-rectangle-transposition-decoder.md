# Rectangle transposition decoder and shadow concentration

PX63 supplies a factor-compatible rectangle state with `O(n log n)` bad
triples for every base side.  This chapter develops the first all-side repair
inequality for that seed.

The repair bank uses transpositions in the two column-label permutations `t`
and `r`.  It preserves the rectangle normal form and therefore preserves exact
row and column degree two.  Averaging over the complete bank gives a sharp
alternative: either one transposition lowers the triple potential, or the
external one-point or two-point line shadow is quantitatively concentrated.

Throughout, let

\[
Q=Q(p,t,r)
\]

be a rectangle state of `4n` points in `[2n]^2`, in any of the four radix
orientations, and let `D(Q)` be its number of bad point triples.

## 1. The complete column-transposition bank

For a family

\[
\xi\in\{t,r\}
\]

and an unordered pair `{a,b}`, swap the two values `xi(a),xi(b)` and leave the
other two permutations unchanged.  Write the resulting state as

\[
Q^\xi_{ab}.
\]

Each move removes four cells and inserts four cells.  It is an executable
balanced trade because it merely exchanges two labels in one permutation.

For one move define:

- `d^xi_ab`: bad triples of `Q` absent from `Q^xi_ab`;
- `c^xi_ab(k)`: bad triples of `Q^xi_ab` absent from `Q` and containing exactly
  `k` inserted cells, for `k=1,2,3`.

Then exactly

\[
D(Q^\xi_{ab})-D(Q)
=
\sum_{k=1}^3c^\xi_{ab}(k)-d^\xi_{ab}.
\]

## 2. Every current defect is paid many times

### Theorem PX67 -- PROVED

For `n>=5`, the total number of destroyed-defect incidences over the complete
`t,r` transposition bank satisfies

\[
\boxed{
\sum_{\xi\in\{t,r\}}
\sum_{\{a,b\}}
d^\xi_{ab}
\ge
3(n-4)D(Q).
}
\]

### Proof

Every selected point belongs to exactly one of the two column families: its
coarse column block is zero and it uses `t`, or its coarse column block is one
and it uses `r`.

A bad triple cannot contain both same-family corners from one rectangle.  Those
two corners lie in one scalar column, which contains exactly two selected
points.  Hence the three points of a bad triple determine exactly three
distinct incidences

\[
(\xi,a),
\]

where `a` is the rectangle index of the point and `xi` is its column family.

Fix one such incidence and let the bad triple use `c<=3` rectangle indices.
Swap `xi(a)` with `xi(b)` for a rectangle `b` outside the triple.  Only the
chosen triple point moves: it retains its scalar row and changes its scalar
column.

The line through the other two triple points is not a scalar-row line, because
one scalar row contains only two selected points.  It therefore meets the fixed
scalar row of the moving point in at most one scalar column.  Since `xi` is a
permutation, at most one outside value of `b` preserves collinearity.  At least

\[
n-c-1\ge n-4
\]

outside swaps destroy the triple through this incidence.

The swaps counted for distinct incidences are distinct: within one family the
other endpoint was required to lie outside the triple, and the two families are
separate banks.  Multiplying by the three incidences proves the claim.
\(\square\)

## 3. Exact coverage of candidate cells and pairs

For a grid point `z` outside `Q`, define its selected pair shadow

\[
\lambda_1(z)
=
\#\{\{x,y\}\subset Q:x,y,z\text{ are collinear}\}.
\]

For two outside points `z,z'`, define

\[
\lambda_2(z,z')
=
\#\{x\in Q:x,z,z'\text{ are collinear}\}.
\]

### Lemma PX68 -- PROVED

Across the complete `t,r` transposition bank:

1. every point of `[2n]^2\setminus Q` occurs exactly once as an inserted-point
   occurrence;
2. each move has two inserted pairs in one scalar column, and those pairs have
   no selected background point on their line;
3. the remaining four inserted pairs from every move are all distinct across
   the bank.

Consequently, if `E(Q)` denotes the set of all nontrivial inserted pairs, then

\[
|[2n]^2\setminus Q|=|E(Q)|=4n(n-1),
\]

and

\[
\sum_{\xi,\{a,b\}}c^\xi_{ab}(1)
\le
\mathcal S_1(Q)
:=
\sum_{z\notin Q}\lambda_1(z),
\]

\[
\sum_{\xi,\{a,b\}}c^\xi_{ab}(2)
\le
\mathcal S_2(Q)
:=
\sum_{\{z,z'\}\in E(Q)}\lambda_2(z,z').
\]

### Proof

Consider a `t`-swap.  In each coarse row block, the inserted cells have the
form

\[
(X_i(a),Y_0(t(b))),
\qquad a\ne b.
\]

As the ordered pair `(a,b)` ranges over distinct indices, these are exactly the
off-graph cells in that coarse block, each once.  The same statement holds in
the other coarse row block, and the `r` bank gives the two coarse column-one
blocks.  The four blocks partition the scalar grid, proving the first claim.

For one source rectangle the two moved corners share a scalar column.  The two
old selected points in that column were removed, and saturation leaves no
background point there.  These two inserted pairs therefore create no
one-background-point triple.

For any other inserted pair, its two scalar row coordinates together with their
coarse-row blocks recover the source indices and the pair type.  Its coarse
column block recovers whether it came from the `t` or `r` bank.  Thus no such
pair is repeated.  There are four per move and

\[
2\binom n2
\]

moves, giving `4n(n-1)` pairs.

A new triple with one inserted point uses a selected background pair; replacing
the move-dependent background by all of `Q` only enlarges its count.  Since
each inserted point occurs once, summation gives `S_1`.  The same argument for
the unique nontrivial inserted pairs gives `S_2`. \(\square\)

## 4. Aggregate conversion inequality

### Theorem PX69 -- PROVED

For every rectangle state with `n>=5`,

\[
\boxed{
\sum_{\xi,\{a,b\}}
\bigl(D(Q^\xi_{ab})-D(Q)\bigr)
\le
\mathcal S_1(Q)+\mathcal S_2(Q)
+4n(n-1)-3(n-4)D(Q).
}
\]

Therefore, if

\[
3(n-4)D(Q)
>
\mathcal S_1(Q)+\mathcal S_2(Q)+4n(n-1),
\]

some `t`- or `r`-transposition strictly lowers the triple potential.

### Proof

Sum the exact potential identity over the bank.  PX67 supplies the destruction
term.  PX68 supplies the one- and two-inserted-point creation terms.  A move
inserts four points, so it creates at most

\[
\binom43=4
\]

triples using three inserted points.  There are

\[
2\binom n2=n(n-1)
\]

moves.  This gives the remaining `4n(n-1)` term.  If the displayed upper bound
on the sum is negative, at least one summand is negative. \(\square\)

## 5. Local-load decoder

Put

\[
\Lambda_1(Q)=\max_{z\notin Q}\lambda_1(z),
\]

and

\[
\Lambda_2(Q)=
\max_{\{z,z'\}\in E(Q)}\lambda_2(z,z').
\]

### Corollary PX69a -- PROVED

If

\[
D(Q)
>
\frac{4n(n-1)}{3(n-4)}
\bigl(\Lambda_1(Q)+\Lambda_2(Q)+1\bigr),
\]

then one column-label transposition improves `Q`.

Equivalently, a transposition-local minimum with `D(Q)>0` satisfies

\[
\boxed{
\max(\Lambda_1(Q),\Lambda_2(Q))
\ge
\frac{3(n-4)D(Q)}{8n(n-1)}-\frac12.
}
\]

### Proof

PX68 gives

\[
\mathcal S_1(Q)
\le4n(n-1)\Lambda_1(Q),
\qquad
\mathcal S_2(Q)
\le4n(n-1)\Lambda_2(Q).
\]

Substitute into PX69.  If no move improves, the aggregate upper bound cannot be
negative.  Rearrangement proves both forms. \(\square\)

## 6. Consequence for the general proof

Start from the universal `O(n log n)` state PX63 and repeatedly apply an
improving `t`- or `r`-transposition whenever one exists.  The integer potential
strictly decreases, so the process terminates at either:

1. an exact no-three product state; or
2. a state with an explicit high one-point or bank-pair line shadow certificate
   given by PX69a.

In particular, if a local minimum still has `D(Q)` of order `n log n`, then it
contains a point-pair or pair-point line load of order `log n`.  The next proof
stage is no longer unrestricted repair: it is the conversion or absorption of
this specific logarithmic shadow concentration.

This is the rectangle analogue of the earlier decoder-or-structure theorems,
but it applies at every side and begins from the all-side low-syndrome seed.

## Verification

Run

```bash
python scripts/verify_product_transposition_decoder.py
```

The verifier checks random exact states in every orientation through base eight,
the `3(n-4)` destruction multiplicity, exact complement coverage by inserted
points, uniqueness of all nontrivial inserted pairs, and the aggregate
potential accounting.
