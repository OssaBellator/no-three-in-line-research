# Protected simultaneous-rainbow cylinder census at orders eleven and thirteen

This chapter extends the exact first-stage simultaneous-rainbow census for slope two and protected directions `(1,1)` and `(1,-1)`. These are finite measurements, not an asymptotic spread theorem.

## PX1139 — exact family sizes

The common-rainbow permutation families have sizes:

- order `11`: `88`;
- order `13`: `4,524`.

Thus order eleven remains far below cubic abundance, while order thirteen satisfies

`4,524 > 13^3 = 2,197`.

This is the first tested order in the current family with genuinely cubic total entropy.

## PX1140 — order-eleven cylinder profile

For the order-eleven family:

- every rank-one cylinder has exactly `8` completions;
- every occurring rank-two cylinder has exactly one completion;
- every occurring rank-three cylinder has exactly one completion.

The exact normalized cylinder constants are

`K_1 = 1`, `K_2 = 5/4`, and `K_3 = 45/4`.

Cubic total family size is therefore still absent, and rank-three slices are singletons.

## PX1141 — order-thirteen cylinder profile

For the order-thirteen family:

- every rank-one cylinder has exactly `348` completions;
- rank-two cylinders have either `29` or `58` completions;
- rank-three cylinders have completion counts in
  `{2,4,5,6,8,16,18,20}`.

The exact normalized cylinder constants are

`K_1 = 1`, `K_2 = 2`, and `K_3 = 220/29`.

Thus the first-stage family simultaneously has cubic total entropy and a bounded finite rank-three constant at order thirteen.

## PX1142 — refined protected-spread target

The order-thirteen transition shows that cubic abundance is not by itself incompatible with controlled rank-three multiplicity. The remaining theorem must establish this behavior uniformly as the order grows and must preserve it for the conditional second-stage families.

The exact asymptotic target is therefore:

1. prove `Omega(ell^3)` first-stage family size;
2. prove `O(1)` normalized rank-three cylinder constants;
3. prove the same two statements uniformly after conditioning on a regular first-stage matching.

No such uniform theorem is claimed here.

## Verification

```bash
python scripts/verify_product_protected_rainbow_cylinder_census_orders_11_13.py
```
