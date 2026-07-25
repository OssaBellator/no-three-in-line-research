# Determinant comparison of the two radial decoder roles

**Branch:** `research/bounded-denominator-absorbers`

BDA5k--BDA5l localize a failed balanced rank-one floor to one occupancy type and one finite arithmetic profile, with substantial exclusive collateral under both decoder roles \(u\) and \(v\). This note compares those two role states geometrically.

## Homothetic decoder coordinates

Translate the common anchor \(P\) to the origin and retain

\[
d=(a,b),
\qquad H=h+q.
\]

For a role parameter \(w\in\{u,v\}\), the direct decoder uses the cells

\[
A_w=P+wz_A,
\qquad
B_w=P+wz_B,
\qquad
C_w=P+wz_C,
\qquad
D_w=P+wz_D,
\]

where

\[
z_A=(ha,hb),
\qquad
z_B=(Ha,Hb),
\]

\[
z_C=(ha,Hb),
\qquad
z_D=(Ha,hb).
\]

The active layer always inserts \(C_w,D_w\). A full phase flip also inserts \(A_w,B_w\) in the blocker layer. Thus every inserted cell in either role is obtained by scaling one of four fixed vectors about \(P\).

A newly created monochromatic triple meeting only this decoder envelope contains either:

- one inserted local cell and two fixed context cells; or
- two inserted local cells in one layer and one fixed context cell.

There are at most six local channel words:

\[
\boxed{C,\ D,\ CD,\ A,\ B,\ AB.}
\]

The last three occur only for a full phase flip.

## BDA5m -- exact role-address identities -- PROVED

### One-local-cell channels

Fix one channel vector \(z\in\{z_A,z_B,z_C,z_D\}\) and two context cells \(X,Y\). Put

\[
x=X-P,
\qquad y=Y-P.
\]

Then

\[
\boxed{
\det(X-P-wz,Y-P-wz)
=
\det(x,y)-w\det(z,y-x).
}
\]

Consequently, if \(\det(z,y-x)\ne0\), collinearity determines the role parameter uniquely:

\[
\boxed{
 w=
 \frac{\det(x,y)}{\det(z,y-x)}.
}
\]

If the same fixed context pair is collinear with both \(P+uz\) and \(P+vz\), where \(u\ne v\), then

\[
\det(x,y)=0,
\qquad
\det(z,y-x)=0.
\]

For distinct context cells, their line is therefore exactly the anchor ray

\[
\boxed{P+\operatorname{span}(z).}
\]

### Two-local-cell channels

Fix two channel vectors \(z_i,z_j\) and one context cell \(X\), with \(x=X-P\). Then

\[
\boxed{
\det(P+wz_i-X,P+wz_j-X)
=
w^2\det(z_i,z_j)
-w\det(z_i-z_j,x).
}
\]

Since \(w\ne0\), the triple is collinear exactly when

\[
\boxed{
\det(z_i-z_j,X-P)
=
w\det(z_i,z_j).
}
\]

For the active pair \(CD\),

\[
\det(z_C,z_D)
=-abq(2h+q)\ne0,
\]

so the role-\(w\) context points lie on the affine line

\[
\boxed{
\det(z_C-z_D,X-P)
=
-wabq(2h+q).
}
\]

The \(u\)- and \(v\)-lines are parallel and distinct. No fixed context point can complete both the \(CD\) triple in role \(u\) and the \(CD\) triple in role \(v\).

For the blocker pair \(AB\),

\[
\det(z_A,z_B)=0,
\]

and the condition becomes

\[
\boxed{
\det(d,X-P)=0.
}
\]

Thus every \(AB\) context point lies on the original radial anchor line, independently of the role parameter.

### Proof

Expand both determinants bilinearly. For the one-local identity,

\[
\det(x-wz,y-wz)
=
\det(x,y)-w\det(z,y-x).
\]

If it vanishes for the two distinct values \(u,v\), subtraction gives \((u-v)\det(z,y-x)=0\), and then the original identity gives \(\det(x,y)=0\).

For the two-local identity,

\[
\det(wz_i-x,wz_j-x)
=
w^2\det(z_i,z_j)-w\det(z_i-z_j,x).
\]

The displayed values of the channel determinants follow by direct substitution. \(\square\)

## BDA5n -- finite two-role channel router -- PROVED

Assume BDA5l returns one occupancy/profile class with exclusive rank-one collateral at least

\[
Q
\ge
\frac{D-F}{12L}
\]

under each of the roles \(u\) and \(v\).

For each role, one of the at most six local channel words carries collateral weight at least

\[
\boxed{
\frac{Q}{6}
\ge
\frac{D-F}{72L}.
}
\]

Hence one ordered pair of channel words

\[
(\omega_u,\omega_v)
\in
\{C,D,CD,A,B,AB\}^2
\]

supports the two heavy role-side families. Each side is then governed by one of the exact BDA5m alternatives:

1. a one-local non-wall determinant address equal to its role parameter;
2. a one-local anchor-ray wall;
3. an active \(CD\) affine line, with the \(u\)- and \(v\)-lines parallel and distinct;
4. the blocker \(AB\) radial line.

For a one-local channel, splitting its weight into wall and non-wall contexts loses at most another factor two. Thus either an anchor-ray wall has weight at least

\[
\boxed{
\frac{D-F}{144L},
}
\]

or the same amount lies on contexts with the exact nonzero determinant address \(w=u\) or \(w=v\).

### Proof

Every new rank-one collateral triple contains at least one inserted local cell. In one matching layer there are at most two inserted cells, so its local intersection word is one of the six displayed words. Pigeonhole separately on each role side. BDA5m supplies the stated geometry for the selected words, and the wall/non-wall split is a two-class pigeonhole. \(\square\)

## Consequence for BDA6

The balanced floor no longer presents two unstructured collections of collateral. After BDA5k and BDA5n, it is one of only thirty-six ordered channel comparisons, and each side lies on an explicit determinant-address locus.

The remaining arithmetic comparison can now be organized as follows:

- anchor-ray walls feed the existing affine-anchor and primitive-slope concentration routes;
- \(CD\) channels give two separated parallel affine lines whose offsets differ by \((u-v)abq(2h+q)\);
- non-wall one-cell channels give exact rational determinant addresses equal to \(u\) or \(v\);
- \(AB\) channels return the original radial line.

This is the precise input for the valuation, residue/carry, and finite-transition charts. A failed balanced floor may no longer hide in an arbitrary mixture of local decoder geometry.

## Finite check

`scripts/verify_bda_role_geometry.py` exhausts small integer decoder parameters and context points. It checks both determinant identities, uniqueness of every non-wall role address, impossibility of a common \(CD\) context for distinct roles, the radial \(AB\) wall, and the finite channel pigeonhole constants.