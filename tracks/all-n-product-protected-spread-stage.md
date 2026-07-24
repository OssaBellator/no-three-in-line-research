# All-n product track: protected simultaneous-rainbow spread

**Branch:** `research/all-n-product-construction`

This stage refines the general rectangle route after PX63--PX80.  Low primitive
directions can be protected, and additive cosets supply local states, but affine
local maps have only rank-two spread.  The protected nonlinear problem is now an
exact simultaneous-rainbow matching problem.

## Current endpoint

Let one prime-order coset be `F_ell`.  For every protected direction `(a,b)`,
colour the edge `(x,y)` of `K_(ell,ell)` by

\[
\chi_{a,b}(x,y)=bx-amy.
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
- PX81--PX82: independent affine row and column parameters enlarge each local
  bank quadratically.
- PX83--PX84: the affine bank has ideal rank-two cylinders but freezes after two
  point images.
- PX85--PX86: nonlinear protected entropy is a sequential simultaneous-rainbow
  matching problem.

## Literature boundary

Known rainbow-perfect-matching and `n`-queens work proves existence, completion,
or asymptotic abundance in closely related proper colourings.  The product proof
needs the stronger uniform statement above: simultaneous rainbow constraints,
rank-three cylinder bounds, and a bound that remains uniform after conditioning
on the first protected matching.

Therefore existing existence or counting theorems cannot simply be quoted as
PX86.  A switching, entropy-completion, or conflict-free matching refinement is
still required.

## Next proof tasks

1. **One-stage spread.** Prove the rank-three cylinder estimate for common-rainbow
   matchings in the linear colourings `chi_(a,b)`.
2. **Conditional stability.** Prove the same estimate for `psi_(a,b)^Phi`
   uniformly over every first-stage matching in a high-probability regular class.
3. **Exceptional first-stage absorption.** Show that irregular `Phi` can be
   repaired or absorbed without losing protected capacities.
4. **Local-load conversion.** Insert the resulting joint cylinder bounds into
   the PX79 certificate loads.
5. **Combine with direction cutoff.** Choose `H` so PX71 has polynomial
   high-direction codegree saving while the rainbow family still has enough
   entropy.

## Verification

```bash
python scripts/verify_product_two_coordinate_coset_bank.py
python scripts/verify_product_protected_affine_cylinders.py
python scripts/verify_product_protected_rainbow_reduction.py
```

No exact all-side doubling theorem is claimed at this stage.