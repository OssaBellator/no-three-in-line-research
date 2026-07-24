# Universal affine blockwise closure for `2 x 5`

The previous chapters found a side-ten witness by reversing fine digits in both
coordinate families, then classified the simplest reversal and one-inner-layer
families. This chapter upgrades those finite examples to a factor-independent
special closure theorem:

> every saturated no-three side-five factor composes with the saturated
> side-two factor to an exact saturated no-three configuration at side ten,
> after suitable blockwise affine digit maps.

This is a genuine PC4 result for the specific factor pair of side lengths
`2` and `5`. It is not an infinite multiplicative closure theorem.

## 1. The affine group on five digits

Let

\[
H=\operatorname{AGL}(1,5)
=
\{x\mapsto ax+b\pmod 5:a\in\{1,2,3,4\},\ b\in\mathbb F_5\}.
\]

Thus `|H|=20`. Write permutations as functions composed from right to left.
Let

\[
t=(2,4,0,3,1),
\]

the unique `ff` one-inner-layer reversal permutation from PX30.

## Theorem PX33 -- PROVED

The symmetric group on five symbols is the disjoint union

\[
\boxed{S_5=H\sqcup HtH.}
\]

The double coset `HtH` has 100 elements and is exactly the set of non-affine
permutations. Every element of `HtH` has exactly four representations

\[
\tau=\beta^{-1}t\alpha,
\qquad \alpha,\beta\in H.
\]

### Proof

A direct conjugation calculation gives

\[
H\cap tHt^{-1}
=
\{
(0,1,2,3,4),
(1,0,4,3,2),
(2,4,1,3,0),
(4,2,0,3,1)
\},
\]

so the intersection has order four. The double-coset formula gives

\[
|HtH|
=
\frac{|H|^2}{|H\cap tHt^{-1}|}
=
\frac{20^2}{4}
=100.
\]

The permutation `t` is not affine, so `HtH` is disjoint from `H`. Since

\[
|H|+|HtH|=20+100=120=|S_5|,
\]

the two sets partition `S_5`. The same intersection calculation shows that
each element of the double coset has four pairs `(alpha,beta)` representing it.
\(\square\)

## 2. Affine permutations cannot occur as factor layers

### Lemma PX33a -- PROVED

The real graph in `[5]^2` of every permutation in `H` contains three collinear
points.

### Proof

For `h(x)=ax+b mod 5`, the following table gives three row indices whose graph
points are collinear. The entries in each cell are the three `x` coordinates.

| `a` | `b=0` | `b=1` | `b=2` | `b=3` | `b=4` |
|---:|---|---|---|---|---|
| 1 | `0,1,2` | `0,1,2` | `0,1,2` | `2,3,4` | `1,2,3` |
| 2 | `0,1,2` | `2,3,4` | `0,2,4` | `0,2,4` | `0,2,4` |
| 3 | `0,2,4` | `0,2,4` | `0,2,4` | `2,3,4` | `0,1,2` |
| 4 | `1,2,3` | `2,3,4` | `0,1,2` | `0,1,2` | `0,1,2` |

Substitution in each of the twenty cases gives zero integer determinant.
\(\square\)

Consequently, every permutation layer of a saturated no-three side-five factor
lies in the non-affine double coset `HtH`: each individual layer is a subset of
the factor configuration and therefore cannot already contain a collinear
triple.

## 3. Universal `2 x 5` closure

Take the saturated side-two outer factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0).
\]

Let `(tau_0,tau_1)` be an arbitrary saturated no-three side-five factor. Choose
either layer `tau=tau_s`. By PX33 and PX33a, there exist

\[
\alpha_0,\beta_0\in H
\]

such that

\[
\beta_0\tau\alpha_0^{-1}=t.
\]

Let

\[
\rho(u)=4-u,
\]

and define the second block maps by

\[
\alpha_1=\rho\alpha_0,
\qquad
\beta_1=\rho\beta_0.
\]

Use the `ff` orientation and the PX28 one-inner-layer state based on `tau`.

## Theorem PX34 -- PROVED

For every saturated no-three side-five factor and either one of its two
permutation layers, the displayed affine block maps produce a saturated
no-three configuration of 20 points in `[10]^2`.

Equivalently,

\[
\boxed{
2\times5\longrightarrow10
}
\]

is a factor-independent product closure statement inside the blockwise affine
one-inner-layer family.

### Proof

Reparameterize the fine row digit by

\[
u'=\alpha_0(u)
\]

and the fine column digit by

\[
v'=\beta_0(v).
\]

In the first coarse row and column blocks, the local maps become the identity.
In the second blocks,

\[
\alpha_1\alpha_0^{-1}=\rho,
\qquad
\beta_1\beta_0^{-1}=\rho.
\]

The chosen fine permutation becomes

\[
\beta_0\tau\alpha_0^{-1}=t.
\]

Therefore the resulting scalar point set is exactly the normalized `ff`
parity-reflection state `L_5^{ff}(t)` from PX25 and PX30. Its two permutation
layers are

\[
(4,2,1,3,0,9,6,8,7,5)
\]

and

\[
(5,7,8,6,9,0,3,1,2,4),
\]

which form a saturated no-three configuration. Host membership and saturation
also follow abstractly from PX24 and PX28. \(\square\)

## 4. Algorithmic form

Given the side-five factor:

1. choose either permutation layer `tau`;
2. enumerate the 400 pairs `(alpha_0,beta_0) in H^2` until
   `beta_0 tau alpha_0^{-1}=t`;
3. set `alpha_1=rho alpha_0` and `beta_1=rho beta_0`;
4. output the PX28 `ff` state.

PX33 guarantees exactly four valid affine pairs. The search is constant-size;
the coordinate output is linear in the 20 resulting cells.

## 5. Boundary

PX34 is the first factor-independent closure statement in this branch, but it
covers only the single multiplication `2 x 5`. It does not iterate by itself:
no corresponding affine double-coset theorem is known for arbitrary `n`, and
the one-inner-layer reversal census is empty at base sides 3, 4, 6, 7, and 8.

The next promising target is to identify moduli `n` for which a manageable
digit-map group has a large double coset containing every permutation layer
that can occur in a saturated no-three factor.

## Verification

Run

```bash
python scripts/verify_product_affine_side_five_closure.py
```

The verifier checks the double-coset decomposition, all twenty affine graph
obstructions, all 64 ordered saturated side-five factor pairs, both layers of
each factor, and the resulting 128 side-ten constructions.
