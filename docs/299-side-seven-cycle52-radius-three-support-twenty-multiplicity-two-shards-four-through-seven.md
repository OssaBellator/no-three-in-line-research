# Exact `(5,2)` radius-three support-twenty multiplicity-two shards four through seven

PX948--PX951 close multiplicity-two cases `10` through `39`. This chapter closes
the next forty signatures, cases `40` through `79`, and extends the fixed
lexicographic ten-signature schedule.

This is a finite obstruction result, not an infinite product theorem and not a
proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX956 -- PROVED FINITE

Cases `40` through `79` contain forty multiplicity-two signatures and therefore

\[
40\cdot2=\boxed{80}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 4 | `40`--`49` | 10 | 20 | `4618887835585757129` |
| 5 | `50`--`59` | 10 | 20 | `15780595376752460129` |
| 6 | `60`--`69` | 10 | 20 | `3249460517323103648` |
| 7 | `70`--`79` | 10 | 20 | `9107125746619132178` |
| **New total** | `40`--`79` | **40** | **80** | four independent digests |

## 2. Exact clean-top census

### Theorem PX957 -- PROVED FINITE

Across cases `40` through `79`, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,527,488 | 11,515,093 |
| Interleaved | 3,120,578 | 10,036,958 |
| **Total** | **6,648,066** | **21,552,051** |

The load remains highly nonuniform. Shard five is interleaved-heavy, while
shards four and seven are concatenated-heavy. Fixed proof boundaries remain
appropriate, but execution should continue to schedule shards by observed or
predicted top-order weight.

## 3. Exact shared bottom CSP

### Theorem PX958 -- PROVED FINITE

For cases `40` through `79`, the exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 5,512,413 |
| 1 | 4,896,136 |
| 2 | 6,058,414 |
| 3 | 4,810,212 |
| **Total** | **21,277,175** |

Combining cases `0` through `79`, the first eighty multiplicity-two signatures
use exactly

\[
9{,}746{,}494+21{,}277{,}175
=\boxed{31{,}023{,}669}
\]

bottom-CSP nodes. All `160` selectors terminate with the active mask empty.

## 4. Revised finite cache boundary

### Corollary PX959 -- PROVED REDUCTION

The first eighty multiplicity-two signatures add `160` certified-infeasible
selectors. The cache boundary is therefore

\[
37{,}600+160=\boxed{37{,}760}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+31{,}023{,}669
=\boxed{2{,}797{,}478{,}913}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-37{,}760-1=\boxed{34{,}099}
\]

selectors remain unclassified:

- `3,760` multiplicity-two signatures containing `7,520` selectors;
- all `26,579` multiplicity-one signatures and selectors.

## 5. Verification

```bash
for shard in 4 5 6 7; do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard${shard}.cpp"
  binary="/tmp/m2s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

Each verifier regenerates the complete layer, asserts the multiplicity-two tier
size `3,840`, checks its exact ten-signature interval, and verifies aggregate
clean-top counts, top-search nodes, all four bottom-CSP totals, and its ordered
transcript digest.
