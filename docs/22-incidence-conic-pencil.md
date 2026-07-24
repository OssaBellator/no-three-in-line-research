# Incidence geometry of the modular conic pencil

This chapter isolates the projective geometry underlying the modular-hyperbola seed. It does not prove the no-three-in-line conjecture. It supplies an exact modular baseline for the remaining geometric bottleneck: controlling secant-star and aligned-anchor concentrations through alternating red/blue closure.

Throughout, `p` is an odd prime and incidence is over `F_p` unless the real lift is stated explicitly.

## 1. Conic-pencil construction

For `c in F_p^*`, define the projective conic

\[
\mathcal C_c:\quad XY=cZ^2.
\]

Its affine part is

\[
H_c=\{(x,c/x):x\in\mathbb F_p^*\}.
\]

Every member contains the two points at infinity

\[
P_\infty=[1:0:0],\qquad Q_\infty=[0:1:0].
\]

### Theorem G1 — PROVED

For every `c != 0`:

1. `C_c` is a nonsingular conic with `p+1` projective points;
2. `H_c` is a permutation graph on `F_p^*` with `p-1` affine points;
3. every projective line meets `C_c` in at most two points.

Consequently, for distinct `a,b`, the standard lift of `H_a union H_b` to `[1,p-1]^2` has exactly two points in every row and column, at most four points on every real line, and no monochromatic real collinear triple.

### Proof

The gradient of `XY-cZ^2` is `(Y,X,-2cZ)`, which cannot vanish at a projective point because `p` is odd and `c != 0`. Thus the conic is nonsingular and has no line component. Its affine points are exactly `(x,c/x)` for `x != 0`, and the equation at infinity is `XY=0`, giving `P_infinity` and `Q_infinity`.

A line restricts the conic equation to a nonzero polynomial of degree at most two, so there are at most two intersections. Three real-collinear lifted points would remain collinear modulo `p`, contradicting this bound within one channel. Applying the bound to both channels gives the real four-point cap. `square`

## 2. Opposite-channel projection

Fix distinct `a,b`, put `r=b/a`, and choose

\[
B_z=[z:b/z:1]\in\mathcal C_b.
\]

Parameterise `C_a` by `P^1(F_p)` using

\[
R_x=[x:a/x:1]\quad(x\in\mathbb F_p^*),
\qquad R_0=Q_\infty,
\qquad R_\infty=P_\infty.
\]

Define

\[
T_z(x)=\frac{z(x-z)}{rx-z}
\]

as a fractional-linear map on `P^1(F_p)`.

### Theorem G2 — PROVED

The line through `B_z` and `R_x` meets `C_a` again at `R_{T_z(x)}`, counting tangency with multiplicity. The map `T_z` is a projective involution and exchanges

\[
0\longleftrightarrow z,
\qquad
\infty\longleftrightarrow z/r.
\]

Hence the vertical and horizontal lines through `B_z` pair one affine conic point with one common point at infinity. Every other nonfixed affine orbit is an affine secant pair; every affine fixed point is a tangency point.

### Proof

The collinearity determinant for `B_z`, `R_x`, and `R_u` gives

\[
u=\frac{z(x-z)}{rx-z}.
\]

The representing matrix

\[
M_z=
\begin{pmatrix}
z&-z^2\\
r&-z
\end{pmatrix}
\]

has determinant `z^2(r-1) != 0` and satisfies

\[
M_z^2=z^2(1-r)I.
\]

Thus its class in `PGL_2(F_p)` has order two. The displayed exceptional transpositions follow by substitution. `square`

## 3. Exact tangent and secant counts

Let `chi` be the quadratic character, extended by `chi(0)=0`.

### Theorem G3 — PROVED

For every anchor `B_z in C_b`, the number of affine tangent contacts with `C_a` is

\[
f(r)=1+\chi(1-r),
\]

and the number of lines through `B_z` containing two distinct affine points of `H_a` is

\[
\boxed{s(r)=\frac{p-4-\chi(1-r)}2.}
\]

The `p+1` lines through `B_z` consist of:

- two axis secants, each joining one affine point to a common point at infinity;
- `1+chi(1-r)` tangents;
- `(p-4-chi(1-r))/2` fully affine secants;
- `(p-chi(1-r))/2` external lines.

Thus every point of `C_b` has the same type relative to `C_a`: two tangents when `chi(1-r)=1`, and no tangent when `chi(1-r)=-1`. Among the `p-2` ratios `r != 0,1`, exactly `(p-3)/2` have the first type and `(p-1)/2` the second.

### Proof

The fixed-point equation `T_z(x)=x` is

\[
rx^2-2zx+z^2=0,
\]

with discriminant `4z^2(1-r)`. Since `r != 1`, the number of roots is `1+chi(1-r)`. Neither `z` nor `z/r` is fixed.

Remove those two exceptional affine parameters and the fixed points from the `p-1` affine parameters. The remainder is partitioned into two-cycles, one for each fully affine secant, giving the formula for `s(r)`. Subtracting all listed line types from `p+1` gives the external-line count. Finally, `r -> 1-r` bijects the admissible ratios with `F_p minus {0,1}`; among these values there are `(p-3)/2` squares and `(p-1)/2` nonsquares. `square`

## 4. Ratio normal form and real-lift warning

Put

\[
\phi_r(t)=\frac{t-1}{rt-1},
\qquad D_z(t)=zt.
\]

### Theorem G4 — PROVED

The modular incidence structure of `(C_a,C_b)` depends only on `r=b/a`:

1. `[X:Y:Z] -> [X:a^{-1}Y:Z]` sends `(C_a,C_b)` to `(C_1,C_r)`;
2. `T_z=D_z phi_r D_z^{-1}`;
3. alternating through a common row from the `a`-channel to the `b`-channel sends a column parameter `x` to `rx`, so row-column components have length `2 ord(r)`.

This preserves modular incidence, tangent type, secant involutions, and row-column cycle lengths. It does **not** preserve the real triple syndrome after the standard lift: residue multiplication has wrap-around and generally is not one affine transformation of the real box.

### Proof

Writing `Y=aY'` changes `XY=aZ^2` to `XY'=Z^2` and `XY=bZ^2` to `XY'=rZ^2`. Also

\[
T_z(zt)=z\frac{t-1}{rt-1}.
\]

The row of the `a`-channel point in column `x` is `a/x`; the `b`-channel point in that row has column `b/(a/x)=rx`. The final warning follows from modular wrap-around. `square`

## 5. Research consequence

The exact projective profile separates the solved modular geometry from the open real-grid geometry:

- every opposite-channel anchor has a known modular secant budget;
- all anchor involutions with fixed ratio are conjugate;
- real bad triples form carry-filtered submatchings of those involutions;
- any alternating-closure proof must exploit that filter to control the secant-star load `Theta` and aligned-anchor multiplicity `Lambda` appearing in the current conversion theorems.

The next incidence-geometric target is therefore not another modular line-cap argument. It is an inequality showing that the real carry filter cannot maintain large `Theta` or `Lambda` through repeated opposite-colour projection, except in an explicitly classified exceptional orbit.

The checker

```bash
python scripts/verify_conic_incidence.py --prime 17
```

verifies the involution and exact profile for every ratio and anchor at a chosen odd prime. It is a finite sanity check, not a proof for arbitrary `p`.
