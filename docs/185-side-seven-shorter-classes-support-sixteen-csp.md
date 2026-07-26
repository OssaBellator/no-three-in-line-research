# Support-sixteen obstruction in the three shorter side-seven classes

PX537 and PX541 close support sixteen for `(3,2,2)` and `(4,3)`.  The remaining
shorter relative class is `(5,2)`, whose radius-two support-sixteen layer contains
`5315` selectors.  This chapter records its exact coordinate census and the
combined three-class boundary.

## 1. The `(5,2)` support-sixteen census

### Theorem PX555 -- PROVED FINITE

Every `(5,2)` radius-two selector satisfying

\[
|F\triangle F_0|=16
\]

fails the 21-variable coordinate CSP in all four radix orientations.

The `5315` selectors are split into ten deterministic lexicographic intervals:

| Selector interval | CSP nodes |
|---:|---:|
| 1--532 | 297,973,260 |
| 533--1,064 | 375,305,493 |
| 1,065--1,596 | 305,353,084 |
| 1,597--2,128 | 389,168,515 |
| 2,129--2,660 | 373,483,392 |
| 2,661--3,192 | 357,261,219 |
| 3,193--3,724 | 534,515,368 |
| 3,725--4,256 | 405,841,387 |
| 4,257--4,788 | 488,709,445 |
| 4,789--5,315 | 553,223,034 |
| **Total** | **4,080,834,197** |

No interval returns a complete coordinate assignment.

## 2. Combined shorter-class boundary

The exact support-sixteen results for the three non-seven-cycle classes are:

| Relative class | Selectors | CSP nodes | Feasible selectors |
|---|---:|---:|---:|
| `(5,2)` | 5,315 | 4,080,834,197 | 0 |
| `(4,3)` | 2,013 | 1,817,808,149 | 0 |
| `(3,2,2)` | 478 | 310,703,324 | 0 |
| **Total** | **7,806** | **6,209,345,670** | **0** |

### Corollary PX556 -- PROVED FINITE

No support-sixteen radius-two certificate exists in any of the three shorter
relative classes.

### Corollary PX557 -- PROVED REDUCTION

Within the full support-sixteen layer of `26,684` selectors, the only unresolved
coordinate stratum is the seven-cycle class, containing

\[
\boxed{18{,}878}
\]

selectors.

Thus the active support-sixteen coordinate problem is now exactly one canonical
relative class.  This does not decide later supports in `(5,2)` and does not
prove universal side-seven doubling false.

## 3. Verification

Use the exact support-range executable

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_two_support.cpp \
  -o /tmp/side7_radius2_range
```

and run the ten displayed `(5,2)` support-sixteen intervals.  PX537 and PX541
supply the embedded exact certificates for the other two rows.  All searches
use integer determinants and print either a concrete embedding or the exact
negative node count.