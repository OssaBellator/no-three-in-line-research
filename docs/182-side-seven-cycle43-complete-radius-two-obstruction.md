# Complete radius-two obstruction for the side-seven `(4,3)` class

PX533--PX536 exhaust radius-two support through fourteen in all four canonical
classes.  The `(4,3)` class has five remaining support strata:

\[
16,\qquad18,\qquad20,\qquad22,\qquad24.
\]

This chapter exhausts all five and closes the complete radius-two layer of the
`(4,3)` relative class.

## 1. Support sixteen

### Theorem PX541 -- PROVED FINITE

All `2013` support-sixteen selectors fail after exactly

\[
\boxed{1{,}817{,}808{,}149}
\]

coordinate-CSP nodes.

The five deterministic shard totals are

\[
277{,}360{,}234,
289{,}151{,}213,
318{,}489{,}994,
399{,}523{,}616,
533{,}283{,}092.
\]

## 2. Supports eighteen and twenty

### Theorem PX542 -- PROVED FINITE

All `1168` support-eighteen selectors fail after exactly

\[
\boxed{1{,}001{,}353{,}577}
\]

coordinate-CSP nodes.

### Theorem PX543 -- PROVED FINITE

All `2072` support-twenty selectors fail after exactly

\[
\boxed{1{,}853{,}906{,}225}
\]

coordinate-CSP nodes.

## 3. Final supports twenty-two and twenty-four

### Theorem PX544 -- PROVED FINITE

All `1232` support-twenty-two selectors fail after exactly

\[
\boxed{1{,}113{,}511{,}554}
\]

coordinate-CSP nodes.  The final `39` support-twenty-four selectors fail after
exactly

\[
\boxed{24{,}983{,}319}
\]

nodes.

## 4. Complete class obstruction

The exact `(4,3)` radius-two ledger is:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 8 | 543 | 518,486,782 |
| 10 | 328 | 311,155,140 |
| 12 | 1,004 | 915,236,711 |
| 14 | 2,132 | 1,886,418,924 |
| 16 | 2,013 | 1,817,808,149 |
| 18 | 1,168 | 1,001,353,577 |
| 20 | 2,072 | 1,853,906,225 |
| 22 | 1,232 | 1,113,511,554 |
| 24 | 39 | 24,983,319 |
| **Total** | **10,531** | **9,442,860,381** |

### Corollary PX545 -- PROVED FINITE

No selector at alternating-cycle distance two from the certified `(4,3)` centre
has a no-three coordinate embedding in any radix orientation.

Consequently any successful `(4,3)` full-selector template has selector-cycle
distance at least three from the current centre.

Together with PX540, two of the four canonical side-seven relative classes are
now completely obstructed through radius two.  This does not prove global
infeasibility of either class.

## 5. Verification

Use

```bash
scripts/search_product_side_seven_radius_two_support.cpp
```

with class `cycle43`, supports `16,18,20,22,24`, and the deterministic intervals
recorded by the theorem runs.  The generic executable regenerates each support
stratum exactly and prints either a concrete embedding or the exact negative
node total.
