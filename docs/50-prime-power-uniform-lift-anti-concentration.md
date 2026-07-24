# Uniform-lift determinant anti-concentration

The restricted conic-fibre bank CMR43--CMR46 is the preferred recursive lift.
This short chapter records the complementary exact statement for the larger
uniform `S_p` fibre bank.

Let \(N=pa\) and fix a saturated quotient state modulo `a`. Write a lifted
selected point as

\[
P_i=(x_i,y_i)
=(\bar x_i+a\xi_i,\bar y_i+a\eta_i).
\]

A **fibre key** is the pair `(layer, quotient column)`.

## 1. Affine dependence on one top row digit

### Lemma CMR53 — PROVED

Fix three distinct actual columns and their layer choices. Conditional on all
top row digits except `eta_j`, the determinant is

\[
\Delta=C+a\kappa_j\eta_j,
\]

where

\[
\kappa_1=x_3-x_2,
\qquad
\kappa_2=x_1-x_3,
\qquad
\kappa_3=x_2-x_1.
\]

Every coefficient is nonzero. Thus at most one value of any remaining top row
digit can make the triple collinear.

### Proof

The determinant is linear in each row coordinate. Replacing `y_j` by
`y_j+a eta_j` changes it by `a eta_j` times the signed difference of the other
two columns. Distinct columns make that coefficient nonzero. ∎

## 2. Uniform fibre permutations

### Theorem CMR54 — PROVED

Under the CMR26 lift with independent uniform permutations in every
layer-fibre, a fixed compatible triple of distinct columns has conditional
collinearity probability at most

\[
1/p
\]

unless all three points have the same fibre key. In that exceptional case the
probability is at most

\[
1/(p-2)
\]

for \(p\ge3\).

### Proof

If the fibre-key multiplicity profile is `1+1+1` or `2+1`, expose all choices
except a point whose key occurs once. Its top row digit is uniform on all `p`
values, and CMR53 leaves at most one successful value.

If all three keys are equal, the three distinct columns use three distinct top
column digits in one uniform permutation. After two images are exposed, the
third image is uniform among the remaining `p-2` rows. Again CMR53 leaves at
most one successful value. ∎

The weak case is exactly the fibre-internal case removed deterministically by
the restricted conic bank CMR45. The checker remains
[`scripts/verify_prime_power_lift_anti_concentration.py`](../scripts/verify_prime_power_lift_anti_concentration.py).
