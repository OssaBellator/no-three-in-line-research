# One-step anti-concentration for recursive prime-power lifts

The recursive determinant identity CMR28 can be sharpened into a direct
conditional probability bound at one lift. A modified lift using the CMR35
terminal family in every fibre removes the only weak local case.

Let

\[
N=pa,
\]

and fix a saturated quotient state at modulus `a`. A lifted selected point has
coordinates

\[
P_i=(x_i,y_i)
=(\bar x_i+a\xi_i,\bar y_i+a\eta_i).
\]

For each layer and each quotient column, the `p` top row digits are assigned to
the `p` top column digits by one fibre permutation. Call the pair

\[
(\text{layer},\bar x)
\]

the **fibre key** of a point.

A real collinear triple must use three distinct actual columns. Indeed, two
points in one column and a third point in another column have a nonzero
vertical determinant.

## 1. Affine dependence on one top row digit

### Lemma CMR41 — PROVED

Fix three distinct actual columns and their layer choices. Conditional on all
top row digits except `eta_j`, the exact determinant is an affine function

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

Every coefficient is nonzero. Consequently, after all other random choices
are exposed, at most one value of any remaining top row digit can make the
triple collinear.

### Proof

The determinant is linear in each row coordinate. Replacing `y_j` by
`y_j+a eta_j` changes the determinant by `a eta_j` times the signed difference
of the other two columns. The displayed coefficients follow from the standard
determinant expansion. Distinct columns make them nonzero. ∎

## 2. Uniform fibre permutations

### Theorem CMR42 — PROVED

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

for `p>=3`.

### Proof

If the three fibre keys are not all equal, their multiplicity profile is
`1+1+1` or `2+1`. Choose a point whose key occurs once. Its fibre permutation
has no other exposed output from this triple, so its top row digit is uniform
on all `p` values. CMR41 leaves at most one successful value.

If all three keys are equal, the three distinct columns use three distinct top
column digits in one uniform permutation. After two images are exposed, the
third image is uniform among the remaining `p-2` rows. Again CMR41 leaves at
most one successful value. ∎

The weak case is exactly a monochromatic triple entirely inside one lifted
fibre.

## 3. Conic-family fibre lifts

Assume now that `p` is odd. Instead of choosing a uniform permutation in each
layer-fibre, choose independently one map `F_{b,c}` from CMR35. Put

\[
h=(p-1)/2.
\]

### Theorem CMR43 — PROVED

Every saturated quotient state has

\[
(h^2)^{2a}=h^{4a}
\]

conic-family lifts. Every lift remains saturated. Under the product measure on
these lifts:

1. a compatible prescription using `r` cells in one layer-fibre has probability
   at most
   \[
   \psi(r),
   \]
   where
   \[
   \psi(0)=1,
   \qquad
   \psi(1)=1/h,
   \qquad
   \psi(r)=1/h^2\quad(r\ge2);
   \]
2. a triple whose three points have one fibre key is never collinear;
3. every other fixed compatible triple has conditional collinearity probability
   at most
   \[
   1/h=2/(p-1).
   \]

### Proof

Each `F_{b,c}` is a permutation of the `p` digit rows, so replacing every
uniform fibre permutation by one such map preserves both layer permutations
and pointwise disjointness of the quotient row fibres. The state count and
cylinder law follow independently from CMR36.

If all three points have one fibre key, their quotient column and quotient row
are common. Subtracting that quotient point and dividing both coordinates by
`a` identifies the three lifted points with three points of one `F_{b,c}`
graph. CMR35 excludes collinearity.

Otherwise some fibre key occurs exactly once. Expose every other fibre. By
CMR41, at most one top row digit in the unique fibre can solve the determinant
equation. CMR36 bounds the probability of that one cell by `1/h`. ∎

## 4. Decoder consequence

CMR43 replaces the unrestricted recursive lift by a smaller but still explicit
product bank with three useful properties:

- exact saturation at every quotient state;
- no monochromatic triple internal to one fibre;
- uniform `O(1/p)` anti-concentration for every remaining triple at the current
  lift level.

A complete recursive decoder still needs to sum these bounds over
first-separation signatures without losing a factor comparable to the number
of candidate triples. The local obstruction itself, however, is removed.

The checker is
[`scripts/verify_prime_power_lift_anti_concentration.py`](../scripts/verify_prime_power_lift_anti_concentration.py).
