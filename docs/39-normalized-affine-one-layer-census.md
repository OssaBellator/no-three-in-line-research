# Normalized affine one-inner-layer census at `2 x 5`

PX28 gives an explicit saturated product family using both outer permutation
layers and one fixed inner permutation.  This note tests the first controlled
enlargement beyond identity/reversal maps: affine fine-digit permutations in
the second coarse row and second coarse column blocks.

The result is rigid.  In the normalized family, every no-three state is the
same side-ten witness already found by blockwise reversal.

## 1. Normalized affine family

Take the canonical side-two outer factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0).
\]

Fix the first coarse row and first coarse column digit maps to the identity.
In the second coarse row and column blocks choose independently

\[
\alpha_1(u)=au+b\pmod5,
\qquad
\beta_1(u)=cu+d\pmod5,
\]

where

\[
a,c\in\{1,2,3,4\},
\qquad
b,d\in\mathbb Z/5\mathbb Z.
\]

Thus each second-block map has twenty possibilities.  Let `tau` range over
every permutation that occurs as one layer of a saturated no-three side-five
factor.  There are exactly 44 such permutations.  For each `tau`, test the
one-inner-layer state PX28 in all four orientations.

The census therefore contains

\[
44\cdot20\cdot20\cdot4=70,400
\]

explicit saturated states.

## Theorem PX30 -- PROVED FINITE

Exactly three of the 70,400 normalized affine one-inner-layer states are
no-three.  They are:

\[
\begin{array}{c|c|c|c}
\tau & \alpha_1 & \beta_1 & \theta\\
\hline
(2,1,4,3,0) & q & q & cf\\
(2,4,0,3,1) & q & q & ff\\
(4,1,0,3,2) & q & q & fc
\end{array}
\]

where

\[
q(u)=4-u.
\]

All three states are the same subset of `[10]^2`, namely the union of the
permutation graphs

\[
(4,2,1,3,0,9,6,8,7,5)
\]

and

\[
(5,7,8,6,9,0,3,1,2,4).
\]

There is no successful normalized affine state in orientation `cc`, and no
affine translation or non-reversal multiplier produces a new witness.

### Proof

Enumerate the 64 ordered saturated no-three side-five factor pairs and extract
their 44 distinct permutation layers.  For every layer, every pair of affine
second-block maps, and every orientation, construct the explicit state PX28 and
check all `binom(20,3)` integer determinants.  Exactly the three displayed
parameter quadruples survive.  Their cell sets are checked to equal the same
side-ten certificate. \(\square\)

## 2. Interpretation

The affine family confirms both the strength and the limitation of the side-ten
escape.

- The successful geometry is not caused by an arbitrary affine perturbation:
  the reversal is isolated inside the normalized affine search.
- The three successful factor layers are coordinate presentations of one
  resulting scalar configuration.
- Enlarging identity/reversal maps to all affine maps in the second blocks does
  not increase the number of scalar witnesses in the explicit one-layer family.

This makes the next target more specific.  A universal construction will need
at least one of:

1. independent non-affine block permutations;
2. nontrivial maps in all coarse blocks rather than the normalized pair;
3. the full degree-two selector instead of PX28;
4. a structural rule that chooses maps from the factor secant geometry rather
   than from a fixed affine family.

## 3. Verification

Run

```bash
python scripts/verify_product_affine_one_layer.py
```

The script checks the exact 70,400-state census using only the standard library.
PX30 is finite evidence, not an infinite doubling or multiplicative closure
theorem.
