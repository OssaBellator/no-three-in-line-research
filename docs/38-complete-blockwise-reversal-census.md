# Complete blockwise reversal census for `2 x 5`

This note refines
[`docs/36-blockwise-digit-permutations.md`](36-blockwise-digit-permutations.md).
PX24 already proves that arbitrary blockwise fine-digit permutations preserve
the four-regular factor-product host, and PX25 records the exact side-ten
parity-reflection witness.  Here the new results are:

1. a general saturated subfamily using both outer layers and only one inner
   permutation layer;
2. the complete identity/reversal census over every saturated side-five factor
   and every global radix orientation.

The results are finite or structural only.  They do not prove multiplicative
closure.

## 1. One-inner-layer twisted products

Use the blockwise coordinates of Chapter 36.  Fix one inner permutation layer
`s in {0,1}` and define

\[
Q_s^{\theta,\alpha,\beta}
=
\left\{
F_{\theta,\alpha,\beta}
\bigl(i,\sigma_r(i),u,\tau_s(u)\bigr):
 r\in\{0,1\},\ i\in[m],\ u\in[n]
\right\}.
\]

## Theorem PX28 -- PROVED

For every pair of saturated factors, every blockwise digit-map family
`alpha_i,beta_j`, every orientation `theta`, and either fixed inner layer `s`,
the set

\[
Q_s^{\theta,\alpha,\beta}
\]

has exactly `2mn` cells and is the union of two disjoint permutation graphs.
It therefore has exactly two points in every scalar row and column and is
constructible in `O(mn)` time.

### Proof

For fixed outer layer `r`, the decoded map

\[
(i,u)\longmapsto\bigl(\sigma_r(i),\tau_s(u)\bigr)
\]

is a bijection of `[m] x [n]`.  Composing it with the blockwise row and column
bijections from PX24 gives one permutation graph on `[mn]`.  The two graphs are
cell-disjoint because

\[
\sigma_0(i)\ne\sigma_1(i)
\]

for every coarse row `i`. \(\square\)

The parity-reflection state used in PX25 is a member of this family: it fixes
the second inner permutation and uses both outer layers.

## 2. Identity/reversal block maps

Take `m=2`, the canonical saturated side-two outer factor, and a saturated
side-five inner factor.  Let

\[
q(u)=4-u.
\]

Each of the two coarse row blocks and two coarse column blocks independently
uses either `id` or `q`.  Thus there are sixteen block-map assignments.  For
each assignment, examine:

- all 32 layer-unordered saturated no-three side-five factors;
- all four orientations `cc,cf,fc,ff`;
- every spanning degree-two state in the resulting four-regular host;
- both one-inner-layer states from PX28.

## Theorem PX29 -- PROVED FINITE

Exactly four of the sixteen identity/reversal assignments admit any no-three
degree-two product-host state.  They are precisely the assignments satisfying

\[
\alpha_0\ne\alpha_1
\qquad\text{and}\qquad
\beta_0\ne\beta_1.
\]

For each of these four equivalent assignments:

- exactly `13` factor/orientation hosts contain a no-three spanning degree-two
  state;
- those successes involve exactly `9` of the `32` layer-unordered side-five
  factors;
- exactly `7` factor/orientation hosts are already solved by a one-inner-layer
  state from PX28;
- those simple successes involve exactly `7` distinct side-five factors.

For each of the other twelve assignments, all four counts are zero.

### Proof

Enumerate the 32 layer-unordered side-five factor pairs, all four orientations,
and all sixteen assignments.  Every resulting host is checked to be
four-regular.  An exact row-by-row search chooses two cells per scalar row,
tracks column degrees, and prunes whenever a newly inserted cell completes a
collinear triple with two previously exposed cells.  Independently test the two
explicit states from PX28.  The displayed counts result. \(\square\)

This gives a sharp finite statement inside the smallest non-global map family:
variation in both coordinate families is necessary.  Reversing digits only in
one coarse row family or only in one coarse column family never removes the
unmodified `2 x 5` obstruction.

## 3. Recovery of the side-ten witness

For

\[
\tau_0=(0,2,1,4,3),
\qquad
\tau_1=(2,4,0,3,1),
\]

choose

\[
\alpha_0=\beta_0=\operatorname{id},
\qquad
\alpha_1=\beta_1=q,
\]

use orientation `ff`, and select the one-inner-layer state `Q_1`.  Its cell set
is the union of the two permutation graphs

\[
(4,2,1,3,0,9,6,8,7,5)
\]

and

\[
(5,7,8,6,9,0,3,1,2,4),
\]

recovering PX25 without the full degree-two selector.  Thus the geometric
escape from PX23 is already present in the explicit `O(mn)` family PX28.

## 4. Verification and boundary

Run

```bash
python scripts/verify_product_blockwise_reversal.py
```

The verifier checks the displayed side-ten state and the full sixteen-pattern
census using only the standard library.

PX29 remains a finite result.  Twenty-three of the 32 layer-unordered side-five
factors are not rescued by this reversal-only family.  The next natural search
space is a controlled blockwise affine family

\[
u\longmapsto a_i u+b_i\pmod n,
\]

combined with either PX28 or the exact full-selector CNF.  A useful theorem must
explain which local maps destroy the coupled line core from PX27, rather than
merely enumerate isolated finite witnesses.
