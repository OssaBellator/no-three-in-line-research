# Spread neutralization of rectangle secant stars

PX71 shows that one possible endpoint of rectangle transposition descent is a
clean endpoint-disjoint secant star through an outside point.  This chapter
installs an exact absorber for that outcome by adapting the matching bank AN1
from the alternating-star pathway.

The result does not yet bound all second-generation collateral.  It removes the
dominant concentrated star exactly and replaces it with a spread matching whose
one-, two-, and three-cell certificate probabilities are explicit.

## 1. Canonical permutation layers of a rectangle state

Every rectangle state has a canonical alternating decomposition.  In rectangle
`u`, put the two corners with equal coarse-row and coarse-column bits in layer
zero and the other two corners in layer one.  Each scalar row and column meets
one point of each layer, so both layers are permutations.

A `t`- or `r`-transposition preserves corner types.  Comparing the canonical
layers before and after the move, each layer undergoes its own balanced
two-point switch.

## 2. Extracting a movable substar

Let

\[
\{P_j,Q_j\},\qquad 1\le j\le M,
\]

be a clean endpoint-disjoint secant star through an outside point `z`.  By PX68,
`z` is inserted by one unique move in the complete `t,r` transposition bank.
Call that move `omega`, and let `R_omega` and `W_omega` be its four removed and
four inserted cells.

Discard every star pair meeting `R_omega`.  Endpoint disjointness discards at
most four pairs.

### Lemma PX72 -- PROVED

Among the surviving star pairs one can choose one endpoint from each of at least

\[
\boxed{
t\ge\frac{M-4}{2}
}
\]

pairs so that all chosen endpoints lie in one canonical permutation layer.
They occupy distinct scalar rows and distinct scalar columns, and they all
survive the fixed move `omega`.

### Proof

At least `M-4` pairs survive, giving at least `2(M-4)` endpoint incidences.
One of the two canonical layers contains at least `M-4` incidences.  A star pair
contributes at most two incidences to that layer, so the layer occurs in at
least `(M-4)/2` distinct pairs.  Choose one endpoint from each represented pair.
A permutation layer uses every row and column once, so the selected endpoints
have distinct rows and columns. \(\square\)

## 3. The replacement matching bank

Write the selected endpoints as

\[
Q_j=(x_j,y_j),\qquad 1\le j\le t,
\]

and let

\[
X_*=\{x_1,\ldots,x_t\},
\qquad
Y_*=\{y_1,\ldots,y_t\}.
\]

After applying `omega`, remove these `t` endpoints from their canonical layer.
A replacement state is a perfect matching between `X_*` and `Y_*`.

Forbid two kinds of positions.

1. The original cell `(x_j,y_j)`, so every chosen endpoint moves.
2. The cell occupied in row `x_j` by the other canonical layer after `omega`,
   whenever that column belongs to `Y_*`, so the two layers remain disjoint.

The forbidden-position set has degree at most two in every source row and every
target column.

### Theorem PX73 -- PROVED

If `t>=7`, there is a nonempty family `Omega` of replacement matchings such that
every replacement:

1. preserves exact row and column degree two;
2. remains disjoint from the other permutation layer;
3. moves every chosen star endpoint;
4. destroys every prospective star triple
   \[
   \{z,P_j,Q_j\},\qquad 1\le j\le t.
   \]

Moreover, if a replacement is uniform in `Omega`, then every compatible
prescribed partial matching of size `r` occurs with probability at most

\[
\boxed{\frac{128}{(t)_r}.}
\]

### Proof

Apply AN1 to the forbidden set.  It gives at least `t!/128` allowed matchings and
the displayed cylinder bound.  The row and column sets are unchanged, and the
second forbidden position prevents collision with the other layer.  The
forbidden diagonal moves each `Q_j`, so the old pair `{P_j,Q_j}` is absent and
its triple with `z` is destroyed. \(\square\)

A clean star of size `M>=18` always supplies `t>=7`, so the theorem applies.

## 4. Exact average collateral

Let `A` be the chosen endpoint set.  Since it was selected after discarding
pairs meeting `R_omega`, the sets `A` and `R_omega` are disjoint.  Put

\[
X=Q\setminus(A\cup R_\omega),
\]

\[
Z=X\cup W_\omega.
\]

The current state is

\[
Q=X\cup A\cup R_\omega,
\]

while one joint fixed-move-and-rematching state is

\[
Q_\pi=Z\cup M_\pi,
\qquad \pi\in\Omega.
\]

Let `Phi` denote the bad-triple potential and define

\[
D_*=\Phi(Q)-\Phi(X),
\qquad
F_*=\Phi(Z)-\Phi(X).
\]

For `r=1,2,3`, let `T_r` be the number of real-collinear certificates consisting
of exactly `r` mutually compatible nonforbidden matching cells and `3-r` points
of `Z`.

### Theorem PX74 -- PROVED

For a uniform replacement matching,

\[
\boxed{
\mathbb E[\Phi(Q_\pi)-\Phi(Z)]
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

Consequently, if

\[
D_*
>
F_*
+
128\left(
\frac{T_1}{t}
+
\frac{T_2}{t(t-1)}
+
\frac{T_3}{t(t-1)(t-2)}
\right),
\]

then some joint state strictly lowers the triple potential.

### Proof

A new triple containing exactly `r` replacement cells appears only if its
prescribed compatible partial matching is contained in `M_pi`.  PX73 bounds
that probability by `128/(t)_r`.  Sum all certificates and use linearity of
expectation.

Finally,

\[
\Phi(Q_\pi)-\Phi(Q)
=
F_*-D_*
+
\Phi(Q_\pi)-\Phi(Z).
\]

A negative expectation yields an improving state. \(\square\)

## 5. Remaining second-generation target

The clean-star outcome of PX71 is now neutralized at first order.  Failure of
every joint state forces one of the normalized certificate masses

\[
\frac{T_1}{t},
\qquad
\frac{T_2}{(t)_2},
\qquad
\frac{T_3}{(t)_3}
\]

to be large relative to the destroyed star incidence.

The next theorem must convert this second-generation concentration, or combine
it with the radial-core and loaded-line outcomes of PX71.  Unlike unrestricted
rectangle repair, the remaining obstruction is now expressed in fixed-rank
matching certificates under a `128/t`-spread measure.

## Verification

Run

```bash
python scripts/verify_product_rectangle_star_bank.py
```

The verifier exhausts representative degree-two forbidden-position systems at
`t=7,8`, checks the AN1 counting and cylinder bounds, and verifies that every
allowed rematching preserves two disjoint permutation layers and moves all
selected endpoints.
