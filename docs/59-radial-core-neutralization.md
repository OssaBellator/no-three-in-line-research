# Spread neutralization of radial defect cores

PX71 leaves a radial-core outcome: many current bad triples have supporting
lines through one outside point `z`.  PX76 already handles the case in which one
of those lines is heavily occupied.  This chapter handles the complementary
case by choosing one movable endpoint on many distinct radial lines.

Let

\[
\mu(z)=\sum_{\ell\ni z}\binom{|Q\cap\ell|}{3}
\]

be the radial triple mass from PX70.

## 1. Many moderate radial lines

Call a radial line **loaded** when it contains at least three selected points.
Assume first that every radial line through `z` contains at most twelve selected
points.  One such line contributes at most

\[
\binom{12}{3}=220
\]

radial triples.

### Lemma PX78 -- PROVED

There are at least

\[
q\ge\frac{\mu(z)}{220}
\]

distinct loaded lines through `z`.  One can choose one selected point from each
of at least

\[
\boxed{
t\ge\frac q2\ge\frac{\mu(z)}{440}
}
\]

of those lines so that all chosen points lie in one permutation layer.

The chosen points occupy distinct scalar rows and distinct scalar columns.

### Proof

The first inequality follows by dividing the total radial triple mass by the
maximum contribution of one line.

Every loaded line contains a selected point from at least one of the two
permutation layers.  Assign each line to one layer represented on it.  One layer
receives at least half the lines.  Choose one point of that layer from every
assigned line.

Distinct lines through the outside point `z` have disjoint selected point sets.
The chosen points are therefore distinct, and one permutation layer uses
distinct rows and columns. \(\square\)

If some radial line has at least thirteen points, PX76 applies instead.  Thus
PX78 covers the complementary radial geometry.

## 2. Moving one endpoint off every radial line

Let the chosen points be

\[
A=\{(x_j,y_j):1\le j\le t\},
\]

with one point on each of `t` distinct radial lines.  Rematch their row set to
their column set.

Forbid:

1. the original cells `(x_j,y_j)`;
2. the cells occupied by the other permutation layer in the chosen rows and
   columns.

The union has row and column degree at most two.

### Theorem PX79 -- PROVED

If `t>=7`, there is a nonempty replacement family `Omega_z` such that every
replacement:

1. preserves exact row and column degree two;
2. stays disjoint from the other permutation layer;
3. moves every chosen point off its original radial line;
4. destroys every old radial triple containing a chosen point.

The uniform replacement satisfies the fixed-rank spread bound

\[
\boxed{
\Pr(F\subseteq M_\pi)\le\frac{128}{(t)_{|F|}}
}
\]

for every compatible prescribed partial matching `F`.

### Proof

AN1 applies to the two forbidden partial matchings.  The original diagonal is
forbidden, so a chosen point changes its scalar column while retaining its
scalar row.  Its old radial line is not a scalar-row line: it contains at least
three selected points, while a scalar row contains exactly two.  Hence that
line meets the fixed source row only in the original cell.  Every replacement
therefore moves the point off its old line.

All old triples on that line containing the chosen point disappear.  Layer
disjointness, saturation, and the spread bound follow from AN1. \(\square\)

The sufficient numerical condition from PX78 is

\[
\mu(z)\ge3080,
\]

which guarantees `t>=7`.  Smaller radial cores are a bounded-mass exception,
not an asymptotically growing obstruction.

## 3. Exact collateral inequality

Put

\[
X=Q\setminus A,
\qquad
Q_\pi=X\cup M_\pi.
\]

If the chosen point on line `ell_j` lies among `k_j` selected points of that
line, it belongs to exactly

\[
\binom{k_j-1}{2}
\]

old triples there.  Different radial lines have disjoint selected point sets,
so these triples are distinct.  Consequently

\[
D_*:=\Phi(Q)-\Phi(X)
\ge
\sum_{j=1}^t\binom{k_j-1}{2}
\ge t.
\]

For `r=1,2,3`, let `T_r` count collinear certificates containing exactly `r`
mutually compatible nonforbidden replacement cells and `3-r` points of `X`.

### Theorem PX80 -- PROVED

For a uniform radial-core replacement,

\[
\boxed{
\mathbb E[\Phi(Q_\pi)-\Phi(X)]
\le
128\left(
\frac{T_1}{t}
+
\frac{T_2}{t(t-1)}
+
\frac{T_3}{t(t-1)(t-2)}
\right).
}
\]

If the right-hand side is smaller than `D_*`, some replacement strictly lowers
the triple potential.

### Proof

Apply the PX79 cylinder bound to every rank-`r` certificate and sum by linearity
of expectation.  The potential identity is

\[
\Phi(Q_\pi)-\Phi(Q)
=
\Phi(Q_\pi)-\Phi(X)-D_*.
\]

\(\square\)

## 4. Completion of the first-generation decoder

Every geometric outcome of PX71 now has an explicit first-generation absorber.

1. Clean secant star: PX73--PX74.
2. Loaded selected line: PX76--PX77.
3. Radial defect core:
   - PX76 if one radial line has at least thirteen points;
   - PX79--PX80 otherwise, once the radial mass reaches the fixed threshold.

All three banks preserve saturation and have the same `128/(t)_r` fixed-rank
spread.  Their failure is therefore expressed by the same normalized
second-generation certificate masses

\[
T_1/t,
\qquad
T_2/(t)_2,
\qquad
T_3/(t)_3.
\]

The remaining growing obstruction is no longer a first-generation star, radial
core, or loaded line.  It is concentration of these replacement-cell
certificates.  Bounded radial masses below the fixed threshold can be isolated
as finite-support exceptions in a future batch theorem.

## Verification

Run

```bash
python scripts/verify_product_radial_core_bank.py
```

The verifier checks the radial-line counting and common-layer extraction in
random tagged rectangle states in all four orientations through base ten, and
checks that the selected endpoints occupy distinct rows and columns.
