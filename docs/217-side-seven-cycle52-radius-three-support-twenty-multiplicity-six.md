# Exact `(5,2)` radius-three support-twenty multiplicity-six tier

PX679--PX682 close multiplicity seven. The next nonempty tier has 524 top
signatures of multiplicity six, hence 3,144 selectors. This chapter closes the
complete tier.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier census

### Theorem PX683 -- PROVED FINITE

The exact radius-three support-twenty layer contains exactly 524
lexicographically ordered top signatures of multiplicity six, hence

\[
524\cdot 6=\boxed{3{,}144}
\]

selectors.

## 2. Exact clean-top census

### Theorem PX684 -- PROVED FINITE

Across the complete tier, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 24,004,326 | 182,105,002 |
| Interleaved | 17,430,207 | 135,396,810 |
| **Total** | **41,434,533** | **317,501,812** |

The verifier prints every ordered per-signature result and asserts the 64-bit
transcript digest `17309853148831689366` (`0xf038f3ba324a2a96`).

## 3. Exact shared bottom CSP

### Theorem PX685 -- PROVED FINITE

Every one of the 3,144 selectors fails in every radix orientation. The exact
bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 48,133,628 |
| 1 | 34,573,453 |
| 2 | 46,688,221 |
| 3 | 32,838,128 |
| **Total** | **162,233,430** |

Every search tree terminates with the six-bit active-selector mask empty. The
independent shard runs produced a complete 524-case transcript; duplicated
recovery cases agreed exactly and no no-three embedding survived.

## 4. Revised cache boundary

### Corollary PX686 -- PROVED REDUCTION

Adding this tier gives

\[
10{,}632+3{,}144=\boxed{13{,}776}
\]

certified-infeasible selectors and

\[
329{,}836{,}133+162{,}233{,}430
=\boxed{492{,}069{,}563}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-13{,}776=\boxed{58{,}084}
\]

support-twenty selectors remain active.

The next nonempty tier has multiplicity five: 725 signatures containing 3,625
selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity6.cpp \
  -o /tmp/m6

/tmp/m6
```

The verifier uses `product_side_seven_tier_digest.hpp` to regenerate the layer,
check all coordinate searches, print the complete transcript, and assert its
aggregate counts and deterministic digest.
