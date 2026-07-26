# Exact `(5,2)` radius-three support-twenty multiplicity-four shard zero

PX687--PX690 close multiplicity five. The next nonempty tier has 2,392 top signatures of multiplicity four, hence 9,568 selectors. This chapter closes the lexicographically first one hundred signatures.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX691 -- PROVED FINITE

The exact radius-three support-twenty layer contains exactly 2,392 top signatures of multiplicity four. Shard zero consists of global case indices `0` through `99`, hence contains

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the radius layers of sizes `364`, `26,550`, and `71,860`, groups the support-twenty layer by the first seven row masks, asserts the complete multiplicity-four histogram, and selects the displayed lexicographic interval.

## 2. Exact clean-top census

### Theorem PX692 -- PROVED FINITE

Across the one hundred signatures, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,228,626 | 20,016,951 |
| Interleaved | 4,892,556 | 21,246,205 |
| **Total** | **9,121,182** | **41,263,156** |

The complete ordered per-signature transcript has deterministic 64-bit digest

`17144806294662027537` (`0xedee967ce8361911`).

The digest mixes each global case index, the seven row masks, both top-order counts, both top-node counts, and all four bottom-node counts.

## 3. Exact shared bottom CSP

### Theorem PX693 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact shared bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,664,385 |
| 1 | 7,946,426 |
| 2 | 6,896,384 |
| 3 | 7,431,473 |
| **Total** | **28,938,668** |

Every search tree terminates with the four-bit active-selector mask empty. No no-three coordinate embedding survives.

## 4. Revised cache boundary

### Corollary PX694 -- PROVED REDUCTION

Before this shard the cache had rejected 17,401 selectors in 737,975,588 shared bottom-CSP nodes. Adding shard zero gives

\[
17{,}401+400=\boxed{17{,}801}
\]

certified-infeasible selectors and

\[
737{,}975{,}588+28{,}938{,}668
=\boxed{766{,}914{,}256}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-17{,}801=\boxed{54{,}059}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier contains 2,292 signatures and 9,168 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard0.cpp \
  -o /tmp/m4s0

# Full shard transcript and digest.
/tmp/m4s0

# Optional independent global case and orientation.
/tmp/m4s0 99 3
```

The full run asserts the complete tier histogram, exact shard interval, every coordinate search, aggregate counts, absence of every candidate embedding, and the ordered transcript digest.
