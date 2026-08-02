# Complete side-seven radius-two support-sixteen obstruction

PX555--PX557 close support sixteen in the three shorter relative classes.  The
remaining seven-cycle stratum contains `18,878` selectors.  This chapter
exhausts that stratum and therefore closes support sixteen globally.

## 1. Seven-cycle coordinate census

### Theorem PX558 -- PROVED FINITE

Every seven-cycle radius-two selector satisfying

\[
|F\triangle F_0|=16
\]

fails the 21-variable coordinate CSP in all four radix orientations.

The selectors are split into twenty deterministic lexicographic intervals:

| Selector interval | CSP nodes |
|---:|---:|
| 1--944 | 289,087,794 |
| 945--1,888 | 318,210,703 |
| 1,889--2,832 | 322,879,082 |
| 2,833--3,776 | 861,741,503 |
| 3,777--4,720 | 758,898,983 |
| 4,721--5,664 | 642,106,496 |
| 5,665--6,608 | 999,493,244 |
| 6,609--7,552 | 509,481,370 |
| 7,553--8,496 | 1,010,276,919 |
| 8,497--9,440 | 1,295,920,468 |
| 9,441--10,384 | 657,018,104 |
| 10,385--11,328 | 474,687,224 |
| 11,329--12,272 | 852,230,809 |
| 12,273--13,216 | 927,236,794 |
| 13,217--14,160 | 769,406,692 |
| 14,161--15,104 | 654,438,254 |
| 15,105--16,048 | 999,771,967 |
| 16,049--16,992 | 1,046,422,487 |
| 16,993--17,936 | 982,987,269 |
| 17,937--18,878 | 1,063,264,358 |
| **Total** | **15,435,560,520** |

No interval returns a complete coordinate assignment.

## 2. Global support-sixteen obstruction

The four exact class ledgers are:

| Relative class | Selectors | CSP nodes | Feasible selectors |
|---|---:|---:|---:|
| `(7)` | 18,878 | 15,435,560,520 | 0 |
| `(5,2)` | 5,315 | 4,080,834,197 | 0 |
| `(4,3)` | 2,013 | 1,817,808,149 | 0 |
| `(3,2,2)` | 478 | 310,703,324 | 0 |
| **Total** | **26,684** | **21,644,906,190** | **0** |

### Corollary PX559 -- PROVED FINITE

No side-seven radius-two selector with symmetric-difference support sixteen has
a no-three coordinate embedding in any radix orientation.

## 3. Revised exact frontier

### Corollary PX560 -- PROVED REDUCTION

A side-seven full-selector certificate must satisfy one of the following:

1. in relative class `(7)` or `(5,2)`, it has radius two and support at least
   eighteen, or selector distance at least three;
2. in relative class `(4,3)` or `(3,2,2)`, it has selector distance at least
   three by PX540 and PX545.

The first remaining radius-two coordinate stratum consists of

\[
25{,}096+3{,}704
=
\boxed{28{,}800}
\]

support-eighteen selectors in the `(7)` and `(5,2)` classes.

### Corollary PX561 -- PROVED REDUCTION

The global radius-two support lower bound is now eighteen.  Two canonical
classes are already completely closed at radius two; the other two have exactly
`28,800` selectors at the first open support.

This remains a finite obstruction around the certified centres. It does not
prove universal side-seven doubling false.

## 4. Verification

The shared verifier

```bash
scripts/verify_product_side_seven_radius_two_support_csp.cpp
```

accepts support `16`. Compile it and run every embedded class shard. Each shard
regenerates the exact radius-two support layer, asserts its selector interval,
and verifies the displayed node total with exact integer determinants.