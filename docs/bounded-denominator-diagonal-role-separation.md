# Diagonal two-role separation in the balanced-floor router

**Branch:** `research/bounded-denominator-absorbers`

BDA5k--BDA5n reduce a large balanced decoder floor to one ordered pair of
local channel words. This note closes all six diagonal comparisons
`(omega,omega)`: the two role families are either supported on an already
identified radial wall or are physically disjoint at their fixed context
address.

Translate the common anchor `P` to the origin and retain the vectors
`z_A,z_B,z_C,z_D` from BDA5m. Let `u!=v` be the two role parameters.

## BDA5bl -- exact diagonal role separation -- PROVED

### One-local channels `A,B,C,D`

Fix `z` among `z_A,z_B,z_C,z_D`. Let `{X,Y}` be a pair of distinct fixed
context cells. If both triples

\[
\{P+uz,X,Y\},\qquad \{P+vz,X,Y\}
\]

are collinear, then the context line is exactly

\[
\boxed{P+\operatorname{span}(z).}
\]

Consequently the non-wall context-pair families for roles `u` and `v` are
disjoint.

### Active two-local channel `CD`

The role-`w` context cells lie on

\[
\det(z_C-z_D,X-P)=-wabq(2h+q).
\]

The `u`- and `v`-lines are parallel and distinct. Hence their context-cell
families are disjoint.

### Blocker two-local channel `AB`

For both roles the context condition is

\[
\det(d,X-P)=0.
\]

Thus both role families lie on the same original radial anchor line.

### Proof

The one-local assertion is the subtraction argument in BDA5m: vanishing at
two distinct role parameters forces both the constant and linear determinant
coefficients to vanish, which says that the context line is the anchor ray.
For `CD`, the coefficient `abq(2h+q)` is nonzero and `u!=v`, so the two affine
right-hand sides differ. The `AB` determinant is identically independent of
the role parameter. QED.

## BDA5bm -- weighted diagonal balanced-floor router -- PROVED

Suppose BDA5n selects a diagonal ordered channel pair `(omega,omega)` and each
role side has collateral weight at least `Q`.

1. If `omega` is one of `A,B,C,D`, then either one role has anchor-ray wall
   weight at least `Q/2`, or the two non-wall role families are disjoint and
   each has weight greater than `Q/2`.
2. If `omega=CD`, the two full families are disjoint, lie on two explicit
   parallel affine lines, and each has weight at least `Q`.
3. If `omega=AB`, both full families lie on the original radial line and each
   has weight at least `Q`.

### Proof

For a one-local channel, split each role-side weight into wall and non-wall
parts. If neither wall part reaches `Q/2`, both non-wall parts exceed `Q/2`;
BDA5bl makes their context-pair supports disjoint. The other two cases follow
directly from the `CD` and `AB` parts of BDA5bl. QED.

## BDA5bn -- completed diagonal subfrontier -- PROVED

Every diagonal channel comparison in the BDA5n balanced-floor output now has
one of three exact continuations:

1. an anchor-ray/radial profile already accepted by the fixed-anchor and
   affine-chain routes;
2. two disjoint non-wall one-cell context-pair families retaining more than
   half the role-side mass;
3. two disjoint parallel `CD` context lines retaining the full role-side mass.

No diagonal comparison can hide repeated non-wall context across the two role
states. The remaining balanced-floor work is therefore confined to the
thirty off-diagonal ordered channel pairs and to payment/realization of the
returned radial or disjoint-context families.

## Finite check

`scripts/verify_bda_diagonal_role_separation.py` exhausts small integer decoder
parameters and context cells. It checks common one-local context pairs,
disjoint `CD` affine lines, the role-independent `AB` radial line, and the
weighted half-mass dichotomy.
