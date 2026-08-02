# Spread neutralization of loaded selected lines

The third outcome of PX71 is a nontrivial bank pair whose supporting line
contains many selected points.  This chapter installs a direct permutation-layer
absorber for that outcome.

Unlike a one-cell move, the absorber moves every point of one permutation layer
that lies on the loaded line.  All of those points are forced off the line, so a
constant fraction of the line's current triples disappears exactly.  The
replacement is again a `128/t`-spread matching.

Let `Q` be any saturated configuration decomposed into two disjoint permutation
layers, and let `ell` be a real line containing `k>=3` selected points.

## 1. One layer carries half the line

### Lemma PX75 -- PROVED

One permutation layer contains

\[
\boxed{m\ge\left\lceil\frac k2\right\rceil}
\]

points of `ell`.  Those points occupy distinct scalar rows and distinct scalar
columns.

The line is neither a scalar-row line nor a scalar-column line.

### Proof

The two layers partition the `k` points, so one contains at least half.  A
permutation layer has one point in every row and column.  A scalar row or column
contains exactly two points of the saturated configuration and therefore cannot
contain `k>=3` points. \(\square\)

Choose a layer attaining `m`, and let `R` and `C` be the row and column sets of
its points on `ell`.

## 2. Forcing every replacement off the line

A replacement state is a perfect matching between `R` and `C`.  Forbid:

1. every cell of `R x C` lying on `ell`;
2. every cell occupied by the other permutation layer whose row lies in `R` and
   whose column lies in `C`.

The first forbidden set has row and column degree at most one because `ell` is
neither vertical nor horizontal.  The second is a partial permutation and also
has row and column degree at most one.  Their union has maximum row and column
degree at most two.

### Theorem PX76 -- PROVED

If `m>=7`, there is a nonempty family `Omega_ell` of replacement matchings such
that every replacement:

1. preserves exact row and column degree two;
2. remains disjoint from the other permutation layer;
3. places no replacement point on `ell`;
4. removes every old line triple containing one of the chosen `m` points.

The uniform replacement is `128/m`-spread: every compatible prescribed partial
matching of rank `r` has probability at most

\[
\boxed{\frac{128}{(m)_r}.}
\]

### Proof

Apply AN1 to the union of the two forbidden partial matchings.  The second
forbidden set preserves layer disjointness.  The first forbids every possible
replacement position on `ell`, including all original selected cells there, so
all chosen points move off the line.  The row and column sets are unchanged.
The spread bound is exactly AN1. \(\square\)

Since `m>=ceil(k/2)`, the theorem applies whenever `k>=13`.

## 3. Exact destruction and average collateral

Let `A` be the chosen `m` points and put

\[
X=Q\setminus A.
\]

For a replacement matching `M_pi`, write

\[
Q_\pi=X\cup M_\pi.
\]

The old line retains only the `k-m` points from the other layer.  Hence the
number of old triples on `ell` destroyed by every replacement is exactly

\[
\boxed{
D_\ell
=
\binom k3-\binom{k-m}{3}.
}
\]

Define

\[
D_*=\Phi(Q)-\Phi(X).
\]

Then `D_*>=D_ell`.  For `r=1,2,3`, let `T_r` count real-collinear certificates
formed from exactly `r` mutually compatible nonforbidden replacement cells and
`3-r` points of `X`.

### Theorem PX77 -- PROVED

For a uniform replacement,

\[
\boxed{
\mathbb E[\Phi(Q_\pi)-\Phi(X)]
\le
128\left(
\frac{T_1}{m}
+
\frac{T_2}{m(m-1)}
+
\frac{T_3}{m(m-1)(m-2)}
\right).
}
\]

Therefore, if

\[
D_*
>
128\left(
\frac{T_1}{m}
+
\frac{T_2}{m(m-1)}
+
\frac{T_3}{m(m-1)(m-2)}
\right),
\]

some loaded-line replacement strictly lowers the triple potential.

### Proof

The spread estimate from PX76 bounds the probability of every rank-`r`
certificate.  Sum by linearity of expectation.  Since

\[
\Phi(Q_\pi)-\Phi(Q)
=
\Phi(Q_\pi)-\Phi(X)-D_*,
\]

a negative expected change gives an improving state. \(\square\)

## 4. Consequence for the decoder program

Two of the three PX71 outcomes now have exact first-generation absorbers.

- PX73 neutralizes a clean radial secant star.
- PX76 neutralizes a loaded selected line.

Both replacement measures have the same fixed-rank cylinder bound
`128/(t)_r`.  Their failure therefore produces the same type of
second-generation obstruction: a large normalized one-, two-, or three-cell
matching-certificate mass.

The only first-generation PX71 outcome not yet absorbed is a radial defect core
spread across many lines through one outside point.  The next useful theorem is
either:

1. a bounded-degree matching extraction from those radial lines; or
2. a direct batch that moves one selected endpoint on each radial line while
   controlling the column-degree of the resulting forbidden positions.

## Verification

The matching and layer-disjointness assertions are checked by

```bash
python scripts/verify_product_rectangle_star_bank.py
```

using the extremal representative in which the line cells and opposite-layer
cells form two disjoint forbidden permutations.
