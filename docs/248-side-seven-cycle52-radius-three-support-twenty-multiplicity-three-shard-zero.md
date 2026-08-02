# Exact `(5,2)` radius-three support-twenty multiplicity-three shard zero

PX796--PX799 complete multiplicity four, with one constructive witness and every other selector rejected. This chapter begins the next nonempty tier and closes global multiplicity-three cases `0` through `99`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX800 -- PROVED FINITE

The exact support-twenty layer contains `3,544` top signatures of multiplicity three. Shard zero contains one hundred signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts the complete multiplicity-three histogram, and selects the lexicographic interval `0` through `99`.

## 2. Exact clean-top census

### Theorem PX801 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,545,839 | 22,273,454 |
| Interleaved | 3,856,995 | 16,803,083 |
| **Total** | **8,402,834** | **39,076,537** |

The complete ordered transcript has deterministic digest

`3064849620408509937` (`0x2a88887dd270a5f1`).

## 3. Exact shared bottom CSP

### Theorem PX802 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,437,610 |
| 1 | 6,498,551 |
| 2 | 8,049,399 |
| 3 | 6,030,205 |
| **Total** | **28,015,765** |

Every exact tree terminates with the active-selector mask empty. Five duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX803 -- PROVED REDUCTION

Adding shard zero gives

\[
26{,}968+300=\boxed{27{,}268}
\]

certified-infeasible selectors and

\[
1{,}486{,}167{,}944+28{,}015{,}765
=\boxed{1{,}514{,}183{,}709}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-27{,}268-1=\boxed{44{,}591}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `100` and contains `3,444` signatures and `10,332` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard0.cpp \
  -o /tmp/m3s0

/tmp/m3s0
/tmp/m3s0 0 0
/tmp/m3s0 99 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
