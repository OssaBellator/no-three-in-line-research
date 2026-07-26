# Exact `(5,2)` radius-three support-fourteen obstruction

PX580--PX582 close the support-twelve stratum in the exact `(5,2)` radius-three
selector layer.  The next stratum has symmetric-difference support fourteen and
contains exactly `2048` selectors.

## 1. Complete coordinate census

### Theorem PX583 -- PROVED FINITE

Every `(5,2)` radius-three selector satisfying

\[
|F\triangle F_0|=14
\]

fails the exact coordinate CSP in all four radix orientations.

The lexicographically ordered layer is split into four deterministic intervals:

| Selector interval | Selectors | CSP nodes | Feasible selectors |
|---:|---:|---:|---:|
| `1--512` | 512 | 306,145,347 | 0 |
| `513--1024` | 512 | 319,189,842 | 0 |
| `1025--1536` | 512 | 428,908,418 | 0 |
| `1537--2048` | 512 | 574,419,715 | 0 |
| **Total** | **2,048** | **1,628,663,322** | **0** |

### Proof

Regenerate the exact first three selector layers, retain the support-fourteen
stratum from PX577, and run the PX515 dangerous-point coordinate CSP for every
selector and every orientation.  Every shard exhausts its interval without a
complete coordinate assignment and records the displayed exact node total.
The four intervals partition all `2048` selectors. \(\square\)

### Corollary PX584 -- PROVED REDUCTION

Any coordinate-embeddable `(5,2)` selector at alternating-cycle distance three
has

\[
|F\triangle F_0|\ge16.
\]

### Corollary PX585 -- PROVED REDUCTION

The first open `(5,2)` radius-three stratum is support sixteen and contains
exactly

\[
\boxed{19{,}352}
\]

selectors.  This remains a finite obstruction around the certified centre, not
a proof that the `(5,2)` canonical host problem is globally infeasible.

## 2. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_three_support.cpp \
  -o /tmp/side7_radius3_range
```

and run class `cycle52`, support `14`, on the four displayed intervals.