# Exact `(5,2)` radius-two support-eighteen obstruction

PX559 closes support sixteen in every side-seven relative class.  The `(5,2)`
radius-two layer next contains `3704` selectors at support eighteen.  This
chapter exhausts that stratum.

## 1. Complete coordinate census

### Theorem PX562 -- PROVED FINITE

Every `(5,2)` radius-two selector satisfying

\[
|F\triangle F_0|=18
\]

fails the 21-variable coordinate CSP in all four radix orientations.

The exact deterministic shards are:

| Selector interval | CSP nodes |
|---:|---:|
| 1--463 | 236,394,516 |
| 464--926 | 289,732,318 |
| 927--1,389 | 344,574,068 |
| 1,390--1,852 | 313,208,950 |
| 1,853--2,315 | 347,276,457 |
| 2,316--2,778 | 358,745,336 |
| 2,779--3,241 | 383,689,604 |
| 3,242--3,704 | 493,065,447 |
| **Total** | **2,766,686,696** |

No shard returns a complete coordinate assignment.

## 2. Revised class boundary

### Corollary PX563 -- PROVED REDUCTION

Any successful `(5,2)` full-selector template must either:

1. lie at radius two with symmetric-difference support at least twenty; or
2. have selector-cycle distance at least three from the certified centre.

The radius-two support-twenty stratum contains exactly

\[
\boxed{6{,}762}
\]

selectors.

### Corollary PX564 -- PROVED REDUCTION

Among all four canonical side-seven classes, the only remaining support-eighteen
coordinate stratum is the seven-cycle class, containing

\[
\boxed{25{,}096}
\]

selectors.  The `(5,2)` class advances to support twenty, while `(4,3)` and
`(3,2,2)` require selector distance at least three.

This does not prove the `(5,2)` or universal side-seven host problem infeasible.

## 3. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_two_support.cpp \
  -o /tmp/side7_radius2_range
```

and run the eight displayed `(5,2)` support-eighteen selector intervals.  The
search regenerates the exact support layer and uses integer determinants for
every CSP rejection.