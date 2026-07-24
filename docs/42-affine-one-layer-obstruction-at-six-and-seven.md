# Affine one-inner-layer obstruction at base sides six and seven

PX34 proves a factor-independent special closure for `2 x 5` by normalizing any
side-five permutation layer into one successful affine double coset. This note
tests whether the same blockwise-affine one-inner-layer mechanism persists at
the next two base sides.

It does not: the complete affine family is empty at base sides six and seven.

## 1. Complete affine one-layer family

Fix the saturated side-two outer factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0).
\]

For `n in {6,7}`, let

\[
G_n=
\{x\mapsto ax+b\pmod n:\gcd(a,n)=1,\ b\in\mathbb Z/n\mathbb Z\}.
\]

Thus

\[
|G_6|=12,
\qquad
|G_7|=42.
\]

Choose an arbitrary permutation `tau in Sym([n])`, arbitrary affine block maps

\[
\alpha_0,\alpha_1,\beta_0,\beta_1\in G_n,
\]

one of the four orientations `cc,cf,fc,ff`, and form the PX28 state using both
outer layers and the single inner permutation `tau`.

## Lemma PX35 -- PROVED

To exhaust the complete four-block affine family, it is enough to impose

\[
\alpha_0=\beta_0=\operatorname{id}
\]

and range independently over

\[
\tau'\in\operatorname{Sym}([n]),
\qquad
\alpha'_1,\beta'_1\in G_n.
\]

### Proof

Given arbitrary affine block maps, substitute

\[
u'=\alpha_0(u),
\qquad
v'=\beta_0(v).
\]

The selected inner permutation becomes

\[
\tau'=\beta_0\tau\alpha_0^{-1},
\]

while the second-block maps become

\[
\alpha'_1=\alpha_1\alpha_0^{-1},
\qquad
\beta'_1=\beta_1\beta_0^{-1}.
\]

Because `G_n` is a group, the two relative maps remain in `G_n`; because `tau`
ranges over the full symmetric group, so does `tau'`. This substitution merely
renames the decoded fine row and column digits and leaves the resulting scalar
point set unchanged. \(\square\)

## Theorem PX36 -- PROVED FINITE

No blockwise-affine one-inner-layer state is no-three at base side six or base
side seven.

More precisely, the normalized exhaustive searches test

\[
6!\cdot4\cdot|G_6|^2
=
720\cdot4\cdot12^2
=
414{,}720
\]

states at base side six and

\[
7!\cdot4\cdot|G_7|^2
=
5040\cdot4\cdot42^2
=
35{,}562{,}240
\]

states at base side seven. Every state contains a real-collinear triple.

### Proof

For every normalized parameter tuple, construct the explicit PX28 point set in
the ordinary integer grid. It has exactly two points in every row and column by
PX28. Expose the points in deterministic order and reject the state as soon as
one point completes a zero-determinant triple with two earlier points. Complete
enumeration returns zero no-three states in both cases. PX35 transfers the
normalized result to the full four-block affine family. \(\square\)

## Interpretation

The universal `2 x 5` theorem is genuinely special. It relies on the exceptional
double-coset identity

\[
S_5=\operatorname{AGL}(1,5)\sqcup
\operatorname{AGL}(1,5)t\operatorname{AGL}(1,5),
\]

combined with the fact that affine permutation graphs are already invalid at
side five. No affine one-inner-layer witness exists at the next composite or
prime base side, even when the fine permutation is allowed to be completely
arbitrary rather than required to occur in a saturated factor.

This does not rule out:

- non-affine block permutations;
- the full degree-two selector in affinely relabelled hosts;
- products with an outer factor larger than two;
- block maps chosen from a larger structured group;
- multi-layer or composite-batch repairs.

It does show that PX34 cannot be promoted to a general doubling theorem by
reusing only affine digit maps and one inner layer.

## Verification

Run

```bash
python scripts/verify_product_affine_one_layer_obstruction.py --side 6
python scripts/verify_product_affine_one_layer_obstruction.py --side 7 --workers 8
```

The worker count changes only parallel execution; the enumerated state family
and asserted totals are exact.
