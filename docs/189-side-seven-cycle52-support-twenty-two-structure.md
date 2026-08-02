# Structure of the `(5,2)` radius-two support-twenty-two layer

PX565 closes support twenty in the `(5,2)` class.  The first open radius-two
stratum has support twenty-two and contains `3544` selectors.  This chapter
classifies their balanced symmetric-difference graphs and radius-one parent
paths before the coordinate census.

## 1. Component and overlap census

### Theorem PX568 -- PROVED FINITE

The `3544` support-twenty-two selectors have exactly the following component
shapes:

| Component edge sizes | Selectors |
|---|---:|
| `4+18` | 1,280 |
| `8+14` | 392 |
| `4+4+14` | 64 |
| `6+16` | 8 |
| `22` | 1,800 |
| **Total** | **3,544** |

Their exact distribution by the number of degree-four row/column vertices is:

| Degree-four vertices | Selectors |
|---:|---:|
| 0 | 1,280 |
| 2 | 512 |
| 3 | 800 |
| 4 | 688 |
| 5 | 248 |
| 6 | 8 |
| 7 | 8 |
| **Total** | **3,544** |

Thus `1280` supports are disjoint unions of ordinary alternating cycles, while
`2264` contain at least one degree-four overlap vertex.

## 2. Radius-one parent paths

### Theorem PX569 -- PROVED FINITE

Every support-twenty-two selector has at least two radius-one parents.  The exact
parent-multiplicity distribution is:

| Radius-one parents | Selectors |
|---:|---:|
| 2 | 1,312 |
| 4 | 672 |
| 6 | 64 |
| 7 | 256 |
| 8 | 576 |
| 10 | 192 |
| 11 | 64 |
| 12 | 128 |
| 13 | 64 |
| 14 | 128 |
| 21 | 64 |
| 24 | 16 |
| 32 | 8 |

In total the layer has

\[
\boxed{20{,}864}
\]

directed radius-one parent incidences.

Exactly

\[
\boxed{1088}
\]

selectors admit at least one two-step path whose first or second flip is an
alternating 4-cycle.

### Corollary PX570 -- PROVED REDUCTION

A cache restricted to paths containing a 4-cycle covers

\[
\frac{1088}{3544}<0.308
\]

of the support-twenty-two layer.  This is substantially larger than the
support-sixteen proportion but still cannot certify the complete layer.

The structural census does not decide coordinate feasibility.

## 3. Verification

Compile and run

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_cycle52_support_twenty_two_structure.cpp \
  -o /tmp/side7_cycle52_s22_structure
/tmp/side7_cycle52_s22_structure
```

The verifier regenerates the exact radius-one and radius-two layers, retains
support twenty-two, traverses every support graph, and verifies all parent
multiplicities using exact selector masks.