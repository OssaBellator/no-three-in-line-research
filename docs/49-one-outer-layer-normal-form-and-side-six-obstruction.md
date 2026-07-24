# One-outer-layer normal form and side-six obstruction

PX51 obtains the universal `2 x 3 -> 6` closure from the complete selector.  Its
canonical certificate has an additional feature: it selects one outer
permutation layer and both inner layers.  This chapter isolates that intermediate
family and tests it exactly at base side six.

## 1. One-outer-layer states

Fix one outer layer of the canonical side-two factor and retain both inner
layers.  The selected cells occupy exactly two coarse blocks.  If the outer
identity layer is chosen, they are `(0,0)` and `(1,1)`; if the swap layer is
chosen, they are `(0,1)` and `(1,0)`.

Inside one occupied block `(i,j)`, the two selected fine permutations are

\[
a_s=\beta_j\tau_s\alpha_i^{-1},
\qquad s\in\{0,1\}.
\]

Let

\[
h=\tau_0^{-1}\tau_1.
\]

Then

\[
a_0^{-1}a_1
=
\alpha_i h\alpha_i^{-1}.
\]

## Theorem PX52 -- PROVED

Under arbitrary blockwise digit permutations, a one-outer-layer state is
completely described by two ordered permutation pairs

\[
(a_0,a_1),
\qquad
(b_0,b_1),
\]

whose relative permutations are each conjugate to the inner factor relative
permutation `h`.  The two target pairs may be chosen independently.

Conversely, every such ordered pair of target pairs is realized by suitable
block maps.

### Proof

The forward statement is the displayed conjugation identity.  The two occupied
blocks use disjoint row-map and column-map variables, so no additional relation
couples their target pairs.

For the converse, suppose

\[
a_0^{-1}a_1=\gamma h\gamma^{-1}.
\]

Choose

\[
\alpha_i=\gamma,
\qquad
\beta_j=a_0\gamma\tau_0^{-1}.
\]

Then

\[
\beta_j\tau_0\alpha_i^{-1}=a_0
\]

and

\[
\beta_j\tau_1\alpha_i^{-1}
=
a_0\gamma h\gamma^{-1}
=
a_1.
\]

Apply the same construction independently in the other occupied block. \(\square\)

## Corollary PX52a -- PROVED

A no-three one-outer-layer template for a given relative cycle type exists if
and only if two saturated no-three factor pairs of that cycle type can be placed
in the two occupied scalar blocks, in some global orientation and outer-layer
choice, without creating a cross-block collinearity.

Thus this family can be tested using only finite lists of saturated factor pairs,
not arbitrary block maps.

The PX51 side-three certificate is exactly such a state: both occupied blocks
contain the canonical side-three factor and the swap outer layer is selected.

## 2. Relative types at side six

There are exactly `116` ordered saturated no-three side-six factor pairs.  Their
relative cycle types are:

| Relative cycle type | Ordered factors |
|---|---:|
| `(6)` | 84 |
| `(4,2)` | 16 |
| `(3,3)` | 16 |

No other derangement type occurs among saturated side-six factors.

For each type, exhaust every ordered choice of the target factor in the first
occupied block and the target factor in the second occupied block, all four
radix orientations, and both outer-layer choices.  The total number of scalar
states is

\[
2\cdot4\left(84^2+16^2+16^2\right)
=
60,544.
\]

## Theorem PX53 -- PROVED FINITE

None of the `60,544` one-outer-layer side-six states is no-three.

Consequently, no saturated side-six factor can be doubled by selecting one outer
layer and both inner layers, even with arbitrary blockwise digit permutations.

### Proof

Enumerate all `6!^2` ordered permutation pairs and retain exactly those whose
union graphs are saturated and no-three.  Group the resulting `116` factors by
the cycle type of `tau_0^{-1} tau_1`.  For every pair of targets in the same
group, construct the corresponding two occupied coarse blocks in every
orientation and outer-layer choice.  Every resulting state is saturated, and an
exact integer-determinant check finds at least one collinear triple in each of
the `60,544` cases. \(\square\)

## 3. Verification

Run

```bash
python scripts/verify_product_one_outer_layer_six.py
```

The verifier checks:

- the exact count `116` of ordered saturated side-six factors;
- the cycle-type distribution `84,16,16`;
- saturation of every tested scalar state;
- failure of all `60,544` states by exact integer determinants.

## 4. Updated side-six boundary

At base side six, two large explicit subfamilies are now completely excluded:

1. PX48 rules out every one-inner-layer state, even with arbitrary block maps;
2. PX53 rules out every one-outer-layer state, again with arbitrary block maps.

A successful `2 x 6 -> 12` product must therefore use a genuinely mixed
degree-two selector: it must use both outer and both inner layers without fixing
either layer globally.  The full four-permutation host normal form PX50 reduces
that remaining search to the three relative cycle types above, but no complete
full-selector classification is yet proved.
