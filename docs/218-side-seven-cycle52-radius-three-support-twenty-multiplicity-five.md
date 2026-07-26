# Exact `(5,2)` radius-three support-twenty multiplicity-five tier

PX683--PX686 close multiplicity six. The next nonempty tier has 725 top
signatures of multiplicity five, hence 3,625 selectors. This chapter closes the
complete tier.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier census

### Theorem PX687 -- PROVED FINITE

The exact radius-three support-twenty layer contains exactly 725
lexicographically ordered top signatures of multiplicity five, hence

\[
725\cdot 5=\boxed{3{,}625}
\]

selectors.

## 2. Exact clean-top census

### Theorem PX688 -- PROVED FINITE

Across the complete tier, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 39,457,291 | 271,756,171 |
| Interleaved | 30,013,327 | 215,692,788 |
| **Total** | **69,470,618** | **487,448,959** |

The verifier prints every ordered per-signature result and asserts the 64-bit
transcript digest `97485168211241114` (`0x015a563e7619a89a`). The digest mixes
the case index, seven row masks, both top-order counts, both top-node counts,
and all four bottom-node counts.

The independent recovery runs produced duplicate rows for selected cases; all
duplicates agreed exactly.

## 3. Exact shared bottom CSP

### Theorem PX689 -- PROVED FINITE

Every one of the 3,625 selectors fails in every radix orientation. The exact
bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 71,190,922 |
| 1 | 53,985,045 |
| 2 | 68,865,985 |
| 3 | 51,864,073 |
| **Total** | **245,906,025** |

Every search tree terminates with the five-bit active-selector mask empty. One
signature has no clean interleaved top order, giving an immediate obstruction
in the corresponding two orientations; all remaining cases are exhausted by
the shared bottom CSP.

## 4. Revised cache boundary

### Corollary PX690 -- PROVED REDUCTION

Adding this tier gives

\[
13{,}776+3{,}625=\boxed{17{,}401}
\]

certified-infeasible selectors and

\[
492{,}069{,}563+245{,}906{,}025
=\boxed{737{,}975{,}588}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-17{,}401=\boxed{54{,}459}
\]

support-twenty selectors remain active.

The next nonempty tier has multiplicity four: 2,392 signatures containing
9,568 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity5.cpp \
  -o /tmp/m5

/tmp/m5
```

The verifier uses `product_side_seven_tier_digest.hpp` to regenerate the layer,
check all coordinate searches, print the complete transcript, and assert its
aggregate counts and deterministic digest.
