# Constant terminal cores as finite obstruction cones

PX315--PX318 reduce every no-composite-reset trajectory antichain to order
`s<=Delta_0+1`.  This chapter converts that constant core into a finite algebraic
obstruction problem.

On `s` labels, every possible created triple is represented by a compatible
partial matching of rank one, two, or three, carrying a nonnegative completion
weight.  Every principal rematching and every subset of releasable historical
layers has an exact integer effect on this finite feature vector.  Therefore the
set of terminal weight tables for which no candidate move improves is a rational
polyhedral cone with finitely many extreme rays depending only on `Delta_0`.

This is not an absorber theorem.  It turns the remaining terminal frontier into
a finite list of extremal weighted templates whose geometric realizability can
be attacked directly.

## 1. Constant rank-at-most-three feature space

Fix a terminal label set `Q` of order `s`.  For `1<=r<=3`, let `P_r(Q)` be the
set of compatible rank-`r` partial matchings between the rows and columns of
`Q`.  Give every `E in P_r(Q)` a nonnegative weight `w_E` equal to its number of
fixed-point completions to a collinear triple; for rank three this is the
indicator/multiplicity of the internal triple itself.  Include analogous weights
for old current certificates destroyed by candidate moves.

### Theorem PX336 -- PROVED

The number of rank-at-most-three candidate features is at most

\[
\boxed{
P(s)=\sum_{r=1}^{\min(3,s)}\binom sr^2r!.
}
\]

Hence for `s<=Delta_0+1` the full terminal certificate table has dimension
`O_(Delta_0)(1)`.

### Proof

A rank-`r` partial matching is obtained by choosing `r` rows, choosing `r`
columns, and choosing a bijection between them.  This gives
`binom(s,r)^2 r!` possibilities.  Sum over `r<=3`; adding the old-destruction
coordinates changes only the constant factor. \(\square\)

## 2. Constant move family

Let `h<=s(s-1)` be the number of nonempty releasable historical restrictions on
`Q`, as in PX318.  A **composite terminal move** chooses a subset of these
restrictions to release and then chooses a principal permutation of `Q` using
only cells allowed after that release.  Partial principal moves are included by
first choosing their support subset.

### Theorem PX337 -- PROVED

The number of labelled composite terminal moves is at most

\[
\boxed{
M(s)
\le
2^{s(s-1)}
\sum_{k=0}^s\binom sk k!.
}
\]

For fixed `Delta_0` this is `O_(Delta_0)(1)`.

### Proof

There are at most `2^h<=2^(s(s-1))` release subsets.  A principal move on a
support of order `k` chooses the support and a permutation of it, giving at most
`binom(s,k)k!` possibilities.  The allowedness and nontriviality conditions only
remove candidates. \(\square\)

## 3. Every move is an integer linear form

Let `w in R^P_+` be the complete terminal feature vector, including old and
prospective certificate weights.  For a composite move `sigma`, let
`Delta_sigma(w)` be its exact change in the triple potential after the selected
historical releases.

### Theorem PX338 -- PROVED

For every composite terminal move there is an integer vector

\[
a_\sigma\in\mathbb Z^P
\]

such that

\[
\boxed{
\Delta_\sigma(w)=a_\sigma\cdot w.
}
\]

The vector `a_sigma` is computable exactly from the move and the rank-at-most-
three certificate table.

### Proof

Each certificate coordinate contributes its weight once for every occurrence
created by the move and negatively once for every occurrence destroyed.  These
multiplicities are integers determined entirely by `sigma`.  Summing the signed
multiplicities gives the dot product. \(\square\)

This includes recurrence created by released historical positions: those
certificates are ordinary positive coordinates in the exact terminal delta.

## 4. The no-improvement cone

Let `Sigma` be the finite composite move family and form the integer matrix `A`
whose row indexed by `sigma` is `a_sigma`.

### Theorem PX339 -- PROVED

The terminal weight tables for which no composite move strictly improves are
exactly

\[
\boxed{
\mathcal K
=
\{w\in\mathbb R_{\ge0}^P:Aw\ge0\}.
}
\]

This is a rational polyhedral cone.  For fixed `Delta_0`, it has a finite set of
rational extreme rays and these rays can be enumerated in `O_(Delta_0)(1)`
symbolic time.

### Proof

By PX338, move `sigma` is nonimproving exactly when
`a_sigma dot w>=0`.  Intersect these finitely many rational halfspaces with the
nonnegative orthant.  Standard finite-dimensional polyhedral theory gives a
finite rational generating set of extreme rays.  The matrix dimensions and
coefficient sizes are bounded in terms of `Delta_0`, so exact enumeration has
constant complexity with respect to `N`. \(\square\)

### Corollary PX340 -- PROVED REDUCTION

To close the trajectory terminal branch for a fixed base degree, it suffices to
rule out or absorb the geometrically realizable extreme rays of finitely many
cones `K`, one for each labelled base/historical template of order at most
`Delta_0+1`.

Equivalently, any failure of terminal improvement has a constant-size rational
obstruction certificate consisting of:

1. the base and historical template;
2. one extreme-ray feature vector;
3. the finite matrix of move inequalities it satisfies.

The remaining terminal question is now finite but still substantive: determine
which extreme rays can arise from actual grid collinearities and whether each
such ray admits a nonprincipal or coupled absorber.

## 5. Verification

Run

```bash
python scripts/verify_product_terminal_obstruction_cone.py
```

The verifier checks the feature and move counts, constructs exact random
rank-at-most-three tables on small cores, and confirms that direct potential
differences agree with the integer linear forms for every principal move.
