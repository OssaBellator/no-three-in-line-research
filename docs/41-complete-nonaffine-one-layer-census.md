# Complete normalized non-affine one-layer census at `2 x 5`

This chapter continues the blockwise map programme of Chapters 36--40.  PX31
showed that normalized affine second-block maps produce only the known reversal
witness in the explicit PX28 family, while PX32 showed that the canonical
factor remains unsatisfiable even under the full normalized affine selector.

Here the second coarse row and second coarse column maps range over **all**
permutations of `[5]`, not only affine maps.  The result is a genuine enlargement:
the canonical factor itself acquires an explicit no-three PX28 state.

## 1. Search family

Take the canonical side-two outer factor

\[
\sigma_0=(0,1),\qquad \sigma_1=(1,0).
\]

Fix the first coarse row and first coarse column digit maps to the identity.  Let

\[
\alpha_1,\beta_1\in\operatorname{Sym}([5])
\]

be arbitrary.  Let `tau` range over every permutation that occurs as one layer
of a saturated no-three side-five factor.  There are 44 such permutations.
For each `tau`, use the explicit PX28 state consisting of both outer layers and
the single fine permutation `tau`, in each of the four orientations.

The census therefore contains

\[
44\cdot120\cdot120\cdot4=2,534,400
\]

explicit saturated side-ten states.

## Theorem PX33 -- PROVED FINITE

Exactly seven parameter quadruples

\[
(\tau,\alpha_1,\beta_1,\theta)
\]

are no-three.  They are:

| `tau` | `alpha_1` | `beta_1` | orientation |
|---|---|---|---|
| `(1,3,0,4,2)` | `(3,4,1,2,0)` | identity | `cf` |
| `(2,0,4,1,3)` | identity | `(3,4,1,2,0)` | `fc` |
| `(2,1,4,3,0)` | reversal | reversal | `cf` |
| `(2,4,0,3,1)` | reversal | reversal | `ff` |
| `(3,1,4,0,2)` | identity | `(3,4,1,2,0)` | `fc` |
| `(3,1,4,0,2)` | `(3,4,1,2,0)` | identity | `cf` |
| `(4,1,0,3,2)` | reversal | reversal | `fc` |

These seven parameter states use exactly six successful fine permutations and
produce exactly five distinct subsets of `[10]^2`.

Among the 32 layer-unordered saturated no-three side-five factors, exactly 22
contain one of the six successful fine permutations.  Each of those 22 factors
contains exactly one successful fine layer.  Hence the explicit `O(n)` PX28
family rescues 22 of the 32 side-five factors after arbitrary normalized
second-block relabelling.

### Proof

Enumerate the 64 ordered saturated no-three permutation pairs at side five and
remove layer-order duplicates, leaving 32 factors and 44 distinct fine
permutation layers.  For every layer, every ordered pair of second-block
permutations, and every orientation, construct the PX28 state and test all

\[
\binom{20}{3}=1140
\]

integer determinants.  The seven displayed parameter quadruples are the only
survivors.  Canonical sorting of their point sets gives five distinct scalar
configurations.  Direct factor incidence gives the 22-factor count and the
one-successful-layer statement. \(\square\)

## 2. Canonical non-affine escape

Use the canonical side-five factor from PX27 and PX32,

\[
\tau_0=(0,1,3,4,2),
\qquad
\tau_1=(2,0,4,1,3).
\]

Choose

\[
\alpha_1=\operatorname{id},
\qquad
\beta_1=(3,4,1,2,0),
\qquad
\theta=fc,
\]

and fix the inner layer `tau_1`.  The resulting PX28 state decomposes into the
two permutation layers

\[
\pi_0=(2,6,0,8,4,5,1,9,3,7),
\]

\[
\pi_1=(6,2,8,0,5,4,9,1,7,3).
\]

### Corollary PX33a -- PROVED

The union of the graphs of `pi_0` and `pi_1` is a saturated no-three
configuration of 20 points in `[10]^2`, contained in the blockwise-permuted
product host of the canonical factor pair.

The map

\[
(3,4,1,2,0)
\]

is not affine modulo five: its cyclic first differences are not constant.
Therefore PX33a genuinely escapes the complete normalized affine obstruction
PX32 rather than re-presenting an affine host.

## 3. Interpretation

PX33 sharply changes the finite boundary.

- The canonical 35-line obstruction is not stable under arbitrary non-affine
  block relabelling.
- Variation in both coordinate families is not universally necessary: the
  canonical escape changes only the second coarse column map.
- The reversal witness is not the only scalar solution once arbitrary
  permutations are allowed; five distinct side-ten configurations occur.
- Ten of the 32 side-five factors still have no explicit PX28 solution in this
  normalized all-permutation family.

Thus the next exact target is no longer merely "try non-affine maps."  It is to
classify the six successful fine permutations and the two map shapes

\[
(\operatorname{id},(3,4,1,2,0))
\quad\text{or}\quad
((3,4,1,2,0),\operatorname{id}),
\]

together with simultaneous reversal, by a secant- or difference-pattern
criterion.  The remaining ten factors require either the full selector,
nontrivial maps in all four coarse blocks, or a larger factor-compatible host.

## Verification

Run

```bash
python scripts/verify_product_nonaffine_one_layer.py
```

The script uses only the standard library and checks the complete 2,534,400
state census, the five scalar configurations, the 22-factor incidence count,
and the displayed canonical side-ten certificate.
