# Exact `(5,2)` radius-two support-twenty obstruction

PX562 closes support eighteen in the `(5,2)` class.  Its next radius-two stratum
contains `6762` selectors at symmetric-difference support twenty.  This chapter
exhausts that stratum.

## 1. Complete coordinate census

### Theorem PX565 -- PROVED FINITE

Every `(5,2)` radius-two selector satisfying

\[
|F\triangle F_0|=20
\]

fails the 21-variable coordinate CSP in all four radix orientations.

The exact deterministic shards are:

| Selector interval | CSP nodes |
|---:|---:|
| 1--677 | 316,808,398 |
| 678--1,354 | 401,284,589 |
| 1,355--2,031 | 489,020,677 |
| 2,032--2,708 | 572,742,409 |
| 2,709--3,385 | 510,382,544 |
| 3,386--4,062 | 533,140,022 |
| 4,063--4,739 | 573,035,141 |
| 4,740--5,416 | 582,252,474 |
| 5,417--6,093 | 649,854,512 |
| 6,094--6,762 | 795,289,448 |
| **Total** | **5,423,810,214** |

No shard returns a complete coordinate assignment.

## 2. Revised `(5,2)` boundary

### Corollary PX566 -- PROVED REDUCTION

Any successful `(5,2)` full-selector template must either:

1. lie at radius two with symmetric-difference support at least twenty-two; or
2. have selector-cycle distance at least three from the certified centre.

### Corollary PX567 -- PROVED REDUCTION

The first open `(5,2)` radius-two stratum is support twenty-two and contains
exactly

\[
\boxed{3544}
\]

selectors.

The only open support-eighteen stratum remains the seven-cycle class, containing
`25,096` selectors.  This chapter does not prove the `(5,2)` or universal
side-seven host problem infeasible.

## 3. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_two_support.cpp \
  -o /tmp/side7_radius2_range
```

and run the ten displayed `(5,2)` support-twenty selector intervals.  The search
regenerates the exact support layer and applies the dangerous-point coordinate
CSP with exact integer determinants.