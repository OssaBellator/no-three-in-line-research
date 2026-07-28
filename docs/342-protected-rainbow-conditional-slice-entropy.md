# Protected rainbow conditional slice entropy

The protected simultaneous-rainbow route needs rank-three cylinder bounds not only before conditioning, but uniformly after fixing up to three matching edges. This chapter isolates the corresponding entropy requirement and computes the exact small-order failure profile.

## PX1101 — general slice-size necessity

Let `F` be a nonempty family of perfect matchings, and let `F_E` be the subfamily containing a fixed rank-`r` partial matching `E`. If the uniform law on `F_E` satisfies a residual rank-three cylinder bound

`Pr(G subset M | E) <= K / (ell-r)_3`,

then necessarily

`|F_E| >= (ell-r)_3 / K`.

Indeed, any matching in `F_E` contains a residual rank-three cylinder `G`, and that cylinder has conditional probability at least `1/|F_E|`.

Thus conditional stability requires cubic entropy in every nonempty slice of rank at most three, not merely cubic size of the unconditioned family.

## PX1102 — exact order-five slices

For the complete order-five first-stage family, and uniformly for every conditional second-stage family:

- all 25 one-edge slices have size 2;
- all 100 occurring two-edge slices have size 1;
- all 100 occurring three-edge slices have size 1.

## PX1103 — exact order-seven slices

For the complete order-seven first-stage family, and uniformly for every conditional second-stage family:

- all 49 one-edge slices have size 4;
- all 588 occurring two-edge slices have size 1;
- all 980 occurring three-edge slices have size 1.

## PX1104 — strengthened protected-spread target

The small families collapse to a unique matching after two compatible edge conditions. Therefore the missing protected-spread theorem must establish, uniformly over all admissible rank-`r` conditions with `r<=3`, both:

1. residual family size `Omega((ell-r)^3)`;
2. bounded multiplicity for every further rank-three cylinder.

Unconditioned cubic abundance alone is insufficient.

## Verification

```bash
python scripts/verify_product_protected_rainbow_slice_entropy.py
```
