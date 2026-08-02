# Radial shadow decomposition and the rectangle decoder trichotomy

PX69 shows that a column-transposition local minimum must have a large
one-point pair shadow or a large bank-pair line load.  This chapter resolves
those two numerical certificates into explicit geometric structures.

Let `Q` be a rectangle state and let `z` be a scalar grid point outside `Q`.
For every real line `ell` through `z`, put

\[
k_\ell=|Q\cap\ell|.
\]

Define

\[
\lambda_1(z)=\sum_{\ell\ni z}\binom{k_\ell}{2}
\]

as in PX68, and let

\[
\mu(z)=\sum_{\ell\ni z}\binom{k_\ell}{3}.
\]

Thus `mu(z)` is the number of current bad triples whose supporting line passes
through `z`.  Let `s_2(z)` be the number of lines through `z` containing exactly
two selected points.

## 1. Clean radial secants

### Theorem PX70 -- PROVED

For every outside point `z`,

\[
\boxed{
s_2(z)\ge\lambda_1(z)-3\mu(z).
}
\]

The `s_2(z)` selected pairs are endpoint-disjoint.  In particular, at least one
of the following holds:

\[
\boxed{s_2(z)\ge\frac12\lambda_1(z)}
\]

or

\[
\boxed{\mu(z)\ge\frac16\lambda_1(z).}
\]

### Proof

Distinct lines through `z` meet only at `z`, which is outside `Q`.  Their
selected point sets are therefore disjoint, so the pairs on the lines with
`k_ell=2` form an endpoint-disjoint matching.

Split the pair shadow into the lines with two selected points and the loaded
lines:

\[
\lambda_1(z)
=
s_2(z)
+
\sum_{k_\ell\ge3}\binom{k_\ell}{2}.
\]

For every integer `k>=3`,

\[
\binom k2
=
\frac{3}{k-2}\binom k3
\le
3\binom k3.
\]

Hence the loaded-line contribution is at most `3mu(z)`, proving the first
inequality.  If `s_2(z)<lambda_1(z)/2`, then the loaded-line contribution is
larger than `lambda_1(z)/2`, so `3mu(z)>lambda_1(z)/2`. \(\square\)

The first outcome is a genuine secant star: every edge lies on a different line
through the same outside centre and no selected endpoint is reused.  The second
outcome says that current defects themselves are radially concentrated around
that centre.

## 2. Pair shadows are loaded selected lines

For one nontrivial bank pair `e={z,z'}` from PX68, recall

\[
\lambda_2(e)
=
|Q\cap\overline{zz'}|.
\]

### Lemma PX70a -- PROVED

If `lambda_2(e)=k`, then the supporting line of `e` contains `k` selected
points and therefore supports exactly

\[
\binom k3
\]

current bad triples.  In particular,

\[
\lambda_2(e)\le2+(6D(Q))^{1/3}.
\]

### Proof

The definition gives the first statement.  Every three of the `k` selected
points are collinear.  Since their number is at most `D(Q)`, the last inequality
follows from

\[
\binom k3\ge\frac{(k-2)^3}{6}.
\]

\(\square\)

## 3. Local-minimum trichotomy

For `n>=5` put

\[
L(Q)
=
\max\left\{
0,
\frac{3(n-4)D(Q)}{8n(n-1)}-\frac12
\right\}.
\]

### Theorem PX71 -- PROVED

If `Q` is a local minimum under all `t`- and `r`-transpositions and `D(Q)>0`,
then at least one of the following structures exists.

1. **Clean secant star.** An outside point is incident with at least
   \[
   \frac12L(Q)
   \]
   endpoint-disjoint selected secants, each on a line containing exactly those
   two selected points.
2. **Radial defect core.** At least
   \[
   \frac16L(Q)
   \]
   current bad triples have supporting lines through one outside point.
3. **Loaded bank line.** One nontrivial inserted pair from the transposition
   bank lies on a line containing at least
   \[
   L(Q)
   \]
   selected points.

### Proof

PX69a gives

\[
\max(\Lambda_1(Q),\Lambda_2(Q))\ge L(Q).
\]

If the maximum is achieved by `Lambda_2`, apply PX70a and obtain the third
outcome.  Otherwise choose `z` with `lambda_1(z)>=L(Q)` and apply PX70.  Its two
alternatives give the first or second outcome. \(\square\)

## 4. Revised absorption target

Starting from PX63, transposition descent now has a fully explicit endpoint:

- exact no-three completion;
- a clean endpoint-disjoint radial secant star;
- a radial concentration of current defects; or
- one heavily occupied line certified by a bank pair.

These are substantially narrower than an arbitrary high-shadow state.  They
suggest three corresponding absorption mechanisms.

1. Randomly reassign the movable endpoints of a clean secant star while
   preserving the two permutation constraints.
2. Use a multi-transposition batch centred on the rectangle indices supporting
   a radial defect core.
3. Move several selected points off one loaded line in one balanced composite
   trade, charging collateral through PX15.

The remaining general proof problem is to show that each outcome admits an
improving bounded-support or spread-distributed batch, or else propagates to a
more rigid algebraic obstruction.

## Verification

Run

```bash
python scripts/verify_product_radial_shadow.py
```

The verifier groups selected points by primitive direction from every outside
point in random rectangle states, checks the exact formulas for `lambda_1`,
`mu`, and `s_2`, and verifies the two alternatives in PX70 in every orientation
through base eight.
