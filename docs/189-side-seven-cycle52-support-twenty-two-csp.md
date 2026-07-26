# Exact `(5,2)` radius-two support-twenty-two obstruction

PX565--PX567 close support twenty in the side-seven `(5,2)` relative class.
The next radius-two stratum has symmetric-difference support twenty-two and
contains exactly `3544` abstract selectors.

## 1. Complete coordinate census

### Theorem PX568 -- PROVED FINITE

Every `(5,2)` radius-two selector satisfying

\[
|F\triangle F_0|=22
\]

fails the exact 21-variable coordinate CSP in all four radix orientations.

The lexicographically ordered selector layer is split into six deterministic
contiguous intervals:

| Selector interval | Selectors | CSP nodes | Feasible selectors |
|---:|---:|---:|---:|
| `1--591` | 591 | 299,064,507 | 0 |
| `592--1182` | 591 | 423,592,289 | 0 |
| `1183--1773` | 591 | 489,300,346 | 0 |
| `1774--2364` | 591 | 432,845,495 | 0 |
| `2365--2955` | 591 | 490,193,167 | 0 |
| `2956--3544` | 589 | 632,135,006 | 0 |
| **Total** | **3,544** | **2,767,130,810** | **0** |

### Proof

Regenerate the exact radius-two selector layer using the PX519 alternating-cycle
breadth-first construction and retain the support-twenty-two stratum from the
complete PX521 histogram.  For every selector and every orientation, run the
PX515 dangerous-point coordinate recursion on `A_0,A_1,R`.  Each shard exhausts
its interval without a complete assignment and records the exact node total
above.  The intervals partition all `3544` selectors, so their sum proves the
claim. \(\square\)

### Corollary PX569 -- PROVED REDUCTION

Any coordinate-embeddable `(5,2)` selector at alternating-cycle distance two
has

\[
|F\triangle F_0|\ge24.
\]

### Corollary PX570 -- PROVED REDUCTION

The remaining `(5,2)` radius-two support strata are

\[
24,26,28,30,32,34,36,40
\]

with counts

\[
1930,776,288,56,45,8,4,1.
\]

They contain in total

\[
\boxed{3108}
\]

selectors.  This remains a finite obstruction around the certified centre, not
a proof that the canonical `(5,2)` host problem is globally infeasible.

## 2. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_two_support.cpp \
  -o /tmp/side7_radius2_range
```

and run class `cycle52`, support `22`, on the six displayed intervals.  The
search regenerates the exact selector layer and uses integer determinant tests
throughout.