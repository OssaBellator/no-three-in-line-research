# Exact `(5,2)` radius-three support-twelve obstruction

PX576--PX579 enumerate the exact `(5,2)` selector layer at alternating-cycle
distance three.  Its minimum symmetric-difference support is twelve, with
exactly `3600` selectors.

## 1. Complete coordinate census

### Theorem PX580 -- PROVED FINITE

Every `(5,2)` radius-three selector satisfying

\[
|F\triangle F_0|=12
\]

fails the exact coordinate CSP in all four radix orientations.

The lexicographically ordered layer is split into six deterministic intervals:

| Selector interval | Selectors | CSP nodes | Feasible selectors |
|---:|---:|---:|---:|
| `1--600` | 600 | 337,047,424 | 0 |
| `601--1200` | 600 | 383,506,926 | 0 |
| `1201--1800` | 600 | 330,225,789 | 0 |
| `1801--2400` | 600 | 315,110,342 | 0 |
| `2401--3000` | 600 | 715,849,537 | 0 |
| `3001--3600` | 600 | 545,331,459 | 0 |
| **Total** | **3,600** | **2,627,071,477** | **0** |

### Proof

Regenerate the exact first three selector layers.  Retain the support-twelve
stratum from the PX577 histogram, order its fourteen-row masks
lexicographically, and run the PX515 dangerous-point coordinate CSP for every
selector and orientation.  Every shard exhausts its interval without a
complete assignment and records the exact node total above.  The six intervals
partition all `3600` selectors. \(\square\)

### Corollary PX581 -- PROVED REDUCTION

Any coordinate-embeddable `(5,2)` selector at alternating-cycle distance three
has

\[
|F\triangle F_0|\ge14.
\]

### Corollary PX582 -- PROVED REDUCTION

The first open `(5,2)` radius-three stratum is support fourteen and contains
exactly

\[
\boxed{2048}
\]

selectors.  The support-twelve strata of `(4,3)` and `(3,2,2)`, containing
`3950` and `6604` selectors, remain separate open coordinate targets.

This is a finite obstruction around one certified centre, not a proof that the
`(5,2)` class is globally infeasible.

## 2. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_three_support.cpp \
  -o /tmp/side7_radius3_range
```

and run class `cycle52`, support `12`, on the six displayed intervals.  Every
run regenerates the exact radius-three selector layer and applies integer
collinearity tests on `[14]^2`.