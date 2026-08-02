# All-n product track: protected simultaneous-rainbow spread

**Branch:** `research/all-n-product-construction`

This stage refines the general rectangle route after PX63--PX80. Low primitive
directions can be protected, and additive cosets supply local states, but affine
local maps have only rank-two spread. The protected nonlinear problem is an exact
simultaneous-rainbow matching problem.

## Current endpoint

Let one prime-order coset be `F_ell`. For every protected direction `(a,b)`,
colour the edge `(x,y)` of `K_(ell,ell)` by

\[
\chi_{a,b}(x,y)=bx-am y.
\]

PX85 proves:

1. the protected column permutation `Phi` is exactly a perfect matching rainbow
   simultaneously in all `chi_(a,b)`;
2. conditioned on `Phi`, the protected row permutation `P` is exactly a second
   perfect matching simultaneously rainbow in the proper colourings

   \[
   \psi_{a,b}^\Phi(x,w)=bw-am\Phi(x).
   \]

PX86 proves conditionally that rank-three cylinder bounds

\[
\Pr(M\supseteq F)\le\frac K{(\ell)_{|F|}}
\qquad(|F|\le3)
\]

for both stages yield joint protected spread

\[
\Pr(\Phi(x_i)=y_i,\ P(x_i)=w_i\text{ for }i\le k)
\le
\frac{K^2}{(\ell)_k^2}.
\]

This is the exact missing probabilistic input.

## Exact small-order cylinder census

PX1033--PX1035 compute the complete two-direction families for slope `m=2` at
orders five and seven.

- First-stage family sizes are `10` and `28`.
- Every admissible first-stage matching has exactly the same number of
  conditional second-stage matchings.
- The exact rank-three cylinder constants are `6` and `15/2` at both stages.
- Every occurring rank-two and rank-three cylinder is unique.

For any nonempty permutation family `F`,

\[
K_3(F)\ge\frac{(\ell)_3}{|F|}.
\]

Therefore an absolute rank-three constant requires `|F|=Omega(ell^3)`.
Existence, completion, or merely quadratic abundance cannot establish PX86.
The missing theorem must produce genuinely cubic entropy while controlling
cylinder multiplicities uniformly after conditioning.

## What is proved around it

- PX63: unrestricted rectangle permutations give `O(n log n)` defects for every
  input factor.
- PX67--PX69: column-transposition descent gives improvement or logarithmic
  one-/two-point shadow concentration.
- PX70--PX73: only low primitive height causes full-order transversal codegree.
- PX75--PX77: rough moduli admit factor-compatible states protecting every
  direction through a chosen height.
- PX78: translation cosets provide protected local variables.
- PX79--PX80: a constant-load LLL criterion is exact, but the first translation
  bank misses it by more than four orders of magnitude.
- PX81--PX84: affine local banks have ideal rank-two cylinders but freeze after
  two point images.
- PX85--PX86: nonlinear protected entropy is a sequential simultaneous-rainbow
  matching problem.
- PX1033--PX1035: rank-three spread requires at least cubic family size.

## Next proof tasks

1. **Cubic abundance.** Prove at least `c ell^3` common-rainbow matchings, with a
   bound robust under conditioning on up to three edges.
2. **Cylinder multiplicity control.** Bound the number of common-rainbow
   completions containing each fixed rank-three cylinder.
3. **Conditional stability.** Prove the same estimates for
   `psi_(a,b)^Phi` uniformly over every first-stage matching in a regular class.
4. **Exceptional first-stage absorption.** Repair or absorb irregular `Phi`
   without losing protected capacities.
5. **Local-load conversion.** Insert the resulting joint cylinder bounds into
   the PX79 certificate loads.
6. **Direction cutoff.** Choose `H` so PX71 retains polynomial high-direction
   codegree saving while the rainbow family still has cubic entropy.

## Verification

```bash
python scripts/verify_product_two_coordinate_coset_bank.py
python scripts/verify_product_protected_affine_cylinders.py
python scripts/verify_product_protected_rainbow_reduction.py
python scripts/verify_product_protected_rainbow_cylinder_census.py
```

No exact all-side doubling theorem is claimed at this stage.
