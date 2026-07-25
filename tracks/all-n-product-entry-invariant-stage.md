# All-n product track: effective repair and side-seven selector-cycle stage

**Branch:** `research/all-n-product-construction`

PX397--PX492 give an effective rectangle-label doubling reduction above
`10^2900`. PX493--PX514 isolate the first unresolved finite base, reduce it to
four canonical relative classes, locate the fixed-selector obstruction in
mixed-half triples, and turn alternating cycles into a complete selector move
language.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Effective closure root | **AUDITED** | PX492 closes the asymptotic numerical ledger at `N_3=10^2900`. |
| Side-seven factor census | **COMPLETE** | 132 saturated configurations, 488 ordered factors, four relative classes. |
| Direct side-six insertion recursion | **REFUTED** | All 21,952 inherited one-label extensions fail. |
| Local host transpositions | **REFUTED** | All 170,368 one-transposition-box hosts fail. |
| Fixed-selector coordinate repair | **REFUTED** | The four centre selector coordinate orbits fail in 2,227,923 CSP nodes. |
| Cross-half profile | **EXACT** | 926,852 top-clean pairs; 806,548 admit a separately clean bottom half; every union has a mixed-half triple. |
| Selector move graph | **CONNECTED** | Alternating cycles connect all selectors with diameter at most fourteen. |
| Radius-one selector layer | **ENUMERATED** | The four centres have 1,748 distinct simple alternating-cycle neighbours. |
| Universal side-seven doubling | **OPEN** | Coordinate feasibility of the selector-changing layers remains unresolved. |
| Exact all-side closure | **OPEN** | No structural bridge covers every base below the cutoff. |

## Effective asymptotic constants

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
A_3=320,
\]

\[
\mathfrak d(N)\le10^{59}N^{16/109},
\qquad
N_3=10^{2900}.
\]

## Exact side-seven classes

| Relative type | Configurations | Ordered factors | Abstract selectors |
|---|---:|---:|---:|
| `(7)` | 60 | 120 | 1,323,522 |
| `(5,2)` | 32 | 128 | 2,269,620 |
| `(4,3)` | 20 | 80 | 1,975,428 |
| `(3,2,2)` | 20 | 160 | 4,422,600 |
| **Total** | **132** | **488** | **9,991,170** |

## Fixed-selector coordinate obstruction

After gauge-fixing the top row order, a selector embedding has 21 variables:
`A_0`, `A_1`, and the bottom-row order `R`, each an element of `S_7`. The four
centre selectors have no embedding in any orientation.

The finer half-profile is:

| Relative type | Top-clean pairs | Also bottom-clean |
|---|---:|---:|
| `(7)` | 172,568 | 134,382 |
| `(5,2)` | 67,628 | 59,450 |
| `(4,3)` | 221,952 | 202,836 |
| `(3,2,2)` | 464,704 | 409,880 |
| **Total** | **926,852** | **806,548** |

For every bottom-clean completion, PX505 forces a triple meeting both halves.
Thus the coordinate failure is genuinely cross-half rather than an intrinsic
failure of either half.

## Selector-cycle graph

For selectors `F,F'`, colour `F\setminus F'` red and `F'\setminus F` blue. Equal
red and blue degree at every abstract row and column decomposes the symmetric
difference into alternating cycles. Flipping at most fourteen such cycles
transforms `F` into `F'`.

The exact first layers around the four centres are:

| Relative type | Radius-one neighbours |
|---|---:|
| `(7)` | 1,092 |
| `(5,2)` | 364 |
| `(4,3)` | 180 |
| `(3,2,2)` | 112 |
| **Total** | **1,748** |

The cycle lengths range from four to twenty-two. Every resulting selector has
abstract degree two exactly.

## Immediate frontier

1. **Cached radius-one CSP.** Apply the 21-variable coordinate solver to all
   1,748 neighbours while sharing triple constraints between nearby selectors.
2. **Cross-half cycle ledger.** For a selector flip, count destroyed and created
   mixed-half triples rather than recomputing the full geometry independently.
3. **Breadth-first selector search.** If radius one fails, continue by selector
   distance; PX512 guarantees completeness by distance fourteen.
4. **Selector invariant.** Find a signature that predicts coordinate
   infeasibility before the full CSP.
5. **Finite-range bridge.** Convert a successful side-seven or general cycle
   theorem into arithmetic coverage below PX492.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_side_seven_relative_classes.py
python scripts/verify_product_side_seven_two_column_normal_form.py
g++ -O3 -std=c++17 scripts/verify_product_side_seven_insertion_barrier.cpp -o /tmp/side7_barrier
g++ -O3 -std=c++17 scripts/verify_product_side_seven_local_minimum_boxes.cpp -o /tmp/side7_boxes
g++ -O3 -std=c++17 scripts/verify_product_side_seven_selector_coordinate_csp.cpp -o /tmp/side7_coordinate_csp
g++ -O3 -std=c++17 scripts/verify_product_side_seven_cross_half_profile.cpp -o /tmp/side7_cross_half
g++ -O3 -std=c++17 scripts/verify_product_side_seven_selector_cycle_graph.cpp -o /tmp/side7_selector_cycles
/tmp/side7_selector_cycles
```

Every recorded census and minimum uses exact integer determinants. Exact
all-side product closure and the classical no-three-in-line conjecture remain
open.
