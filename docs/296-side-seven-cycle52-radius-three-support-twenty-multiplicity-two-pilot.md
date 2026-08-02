# Exact `(5,2)` radius-three support-twenty multiplicity-two pilot

PX940--PX943 identify the residual side-seven cache exactly: `3,840` multiplicity-two signatures containing `7,680` selectors, plus `26,579` multiplicity-one selectors. This chapter classifies the first ten multiplicity-two signatures and calibrates the next finite stage.

This is a finite obstruction result, not an infinite product theorem and not a proof of the no-three-in-line conjecture.

## 1. Exact pilot census

### Theorem PX944 -- PROVED FINITE

Global multiplicity-two cases `0` through `9` contain ten signatures and therefore

\[
10\cdot2=\boxed{20}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Case | Signature | Clean top orders | Top-search nodes | Bottom-CSP nodes |
|---:|---|---:|---:|---:|
| 0 | `[3,6,12,2056,144,96,4160]` | 59,976 | 167,377 | 186,628 |
| 1 | `[3,6,12,2056,144,96,12288]` | 97,608 | 282,999 | 303,001 |
| 2 | `[3,6,12,2056,144,4128,4160]` | 73,272 | 204,105 | 220,664 |
| 3 | `[3,6,12,2056,144,4128,8256]` | 51,276 | 149,375 | 144,226 |
| 4 | `[3,6,12,2056,144,8224,96]` | 28,344 | 80,842 | 91,434 |
| 5 | `[3,6,12,2056,144,8224,4128]` | 72,108 | 207,396 | 202,982 |
| 6 | `[3,6,12,2056,144,8224,8256]` | 73,272 | 204,105 | 220,664 |
| 7 | `[3,6,12,2056,144,8224,12288]` | 179,430 | 508,910 | 539,768 |
| 8 | `[3,6,12,2056,144,8256,4128]` | 51,276 | 149,370 | 144,388 |
| 9 | `[3,6,12,2056,144,8256,4160]` | 72,108 | 207,397 | 202,982 |
| **Total** | 10 signatures | **758,670** | **2,161,876** | **2,256,737** |

The complete ordered transcript has deterministic digest

`10095218108694584973` (`0x8c1c834e8f71c90d`).

## 2. Exact clean-top census

### Theorem PX945 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 217,122 | 640,749 |
| Interleaved | 541,548 | 1,521,127 |
| **Total** | **758,670** | **2,161,876** |

The pilot already shows substantial heterogeneity: the number of clean top orders per signature ranges from `28,344` to `179,430`. Fixed 100-signature shards would therefore have poorly controlled work even before the multiplicity-one tier is reached.

## 3. Exact shared bottom CSP

### Theorem PX946 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 282,364 |
| 1 | 926,841 |
| 2 | 404,053 |
| 3 | 643,479 |
| **Total** | **2,256,737** |

Every search terminates with the two-bit active-selector mask empty. No feasible selector occurs in the pilot.

## 4. Revised finite cache boundary

### Corollary PX947 -- PROVED REDUCTION

Adding these twenty selectors gives

\[
37{,}600+20=\boxed{37{,}620}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+2{,}256{,}737
=\boxed{2{,}768{,}711{,}981}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, the unclassified cache is now

\[
71{,}860-37{,}620-1=\boxed{34{,}239}.
\]

It consists exactly of:

- `3,830` remaining multiplicity-two signatures, containing `7,660` selectors;
- all `26,579` multiplicity-one signatures and selectors.

## 5. Sharding consequence

The pilot supports ten-signature canonical shards as the initial multiplicity-two unit. A later scheduler may combine adjacent shards by predicted top-order load, but the proof objects should retain fixed lexicographic ten-signature boundaries so that each transcript remains independently replayable.

A full multiplicity-two completion would require `383` further ten-signature shards. Before launching that census, the branch should test whether the two-candidate mask admits a direct certificate or symmetry reduction that avoids repeating the complete bottom search for both selectors.

## 6. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  -o /tmp/m2-pilot10

/tmp/m2-pilot10
/tmp/m2-pilot10 0 0
/tmp/m2-pilot10 9 3
```

The full run asserts the tier size `3,840`, the exact shard interval, aggregate clean-top counts, top-search nodes, all four bottom-CSP totals, and the ordered transcript digest. A single-case invocation replays one signature and may restrict to one orientation.
