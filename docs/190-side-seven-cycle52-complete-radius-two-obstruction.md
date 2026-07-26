# Complete radius-two obstruction for the side-seven `(5,2)` class

PX562--PX570 close supports eighteen, twenty, and twenty-two in the `(5,2)`
relative class.  This chapter exhausts every remaining radius-two support
stratum and closes the full 26,550-selector layer.

## 1. Support twenty-four

### Theorem PX571 -- PROVED FINITE

All `1930` support-twenty-four selectors fail the exact coordinate CSP.
The five deterministic shard totals are

\[
221{,}467{,}808,
320{,}176{,}946,
283{,}375{,}514,
329{,}941{,}224,
380{,}966{,}043,
\]

for total

\[
\boxed{1{,}535{,}927{,}535}.
\]

## 2. Supports twenty-six and twenty-eight

### Theorem PX572 -- PROVED FINITE

All `776` support-twenty-six selectors fail.  The two equal 388-selector
intervals require

\[
301{,}158{,}609
\quad\text{and}\quad
330{,}241{,}135
\]

nodes, for total

\[
\boxed{631{,}399{,}744}.
\]

All `288` support-twenty-eight selectors fail after exactly

\[
\boxed{229{,}218{,}191}
\]

nodes.

## 3. Final support strata

### Theorem PX573 -- PROVED FINITE

The final five nonempty support strata are all infeasible:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 30 | 56 | 34,757,139 |
| 32 | 45 | 30,055,392 |
| 34 | 8 | 4,827,528 |
| 36 | 4 | 2,750,582 |
| 40 | 1 | 508,527 |
| **Total** | **114** | **72,899,168** |

No support-thirty-eight selector occurs in the exact radius-two histogram.

## 4. Complete class ledger

The full `(5,2)` radius-two certificate is:

| Support | Selectors | CSP nodes |
|---:|---:|---:|
| 8 | 533 | 346,044,962 |
| 10 | 232 | 172,039,249 |
| 12 | 1,584 | 1,103,440,538 |
| 14 | 1,768 | 1,225,466,432 |
| 16 | 5,315 | 4,080,834,197 |
| 18 | 3,704 | 2,766,686,696 |
| 20 | 6,762 | 5,423,810,214 |
| 22 | 3,544 | 2,767,130,810 |
| 24 | 1,930 | 1,535,927,535 |
| 26 | 776 | 631,399,744 |
| 28 | 288 | 229,218,191 |
| 30 | 56 | 34,757,139 |
| 32 | 45 | 30,055,392 |
| 34 | 8 | 4,827,528 |
| 36 | 4 | 2,750,582 |
| 40 | 1 | 508,527 |
| **Total** | **26,550** | **20,354,897,736** |

### Corollary PX574 -- PROVED FINITE

No selector at alternating-cycle distance two from the certified `(5,2)` centre
has a no-three coordinate embedding in any of the four radix orientations.

### Corollary PX575 -- PROVED REDUCTION

Any successful `(5,2)` full-selector template has selector-cycle distance at
least three from the certified centre.

Together with PX540 and PX545, three of the four canonical side-seven relative
classes are now completely obstructed through radius two.  The seven-cycle
class remains open at radius two beginning with support eighteen.

This does not prove global infeasibility of the `(5,2)` class or universal
side-seven doubling.

## 5. Verification

Use

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_two_support.cpp \
  -o /tmp/side7_radius2_range
```

with class `cycle52` and the displayed support intervals.  Every run regenerates
the exact breadth-first radius-two layer, applies the PX515 dangerous-point CSP,
and prints either a concrete embedding or the exact negative node total.
All recorded runs returned `NO` and used integer determinants on `[14]^2`.