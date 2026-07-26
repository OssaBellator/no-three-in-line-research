# Exact `(5,2)` radius-three support-twenty multiplicity-seven tier

PX675--PX678 close multiplicity eight. The next nonempty tier has 100 top
signatures of multiplicity seven, hence 700 selectors. This chapter closes the
complete tier.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier census

### Theorem PX679 -- PROVED FINITE

The exact radius-three support-twenty layer contains exactly 100
lexicographically ordered top signatures of multiplicity seven, hence

\[
100\cdot 7=\boxed{700}
\]

selectors.

## 2. Exact clean-top census

### Theorem PX680 -- PROVED FINITE

Across the complete tier, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,293,412 | 41,777,767 |
| Interleaved | 3,628,790 | 30,496,066 |
| **Total** | **8,922,202** | **72,273,833** |

The verifier prints every ordered per-signature result and asserts the 64-bit
transcript digest `10544814853067668521` (`0x9256b53d735c7c29`). The digest mixes
the case index, seven row masks, both top-order counts, both top-node counts,
and all four bottom-node counts.

## 3. Exact shared bottom CSP

### Theorem PX681 -- PROVED FINITE

Every one of the 700 selectors fails in every radix orientation. The exact
bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 11,888,048 |
| 1 | 8,024,253 |
| 2 | 11,224,214 |
| 3 | 8,193,358 |
| **Total** | **39,329,873** |

Every search tree terminates with the seven-bit active-selector mask empty.
No no-three coordinate embedding survives.

## 4. Revised cache boundary

### Corollary PX682 -- PROVED REDUCTION

Adding this tier gives

\[
9{,}932+700=\boxed{10{,}632}
\]

certified-infeasible selectors and

\[
290{,}506{,}260+39{,}329{,}873
=\boxed{329{,}836{,}133}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-10{,}632=\boxed{61{,}228}
\]

support-twenty selectors remain active.

The next nonempty tier has multiplicity six: 524 signatures containing 3,144
selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity7.cpp \
  -o /tmp/m7

/tmp/m7
```

The run regenerates all radius layers, asserts the multiplicity histogram,
checks every clean top and bottom permutation exactly, prints the complete
ordered transcript, and asserts its aggregate counts and digest.
