# All-n product track: effective repair and side-seven structural stage

**Branch:** `research/all-n-product-construction`

PX397--PX492 give an effective rectangle-label doubling reduction above
`10^2900`. PX493--PX507 isolate the first unresolved finite base, reduce it to
four canonical relative classes, and successively rule out direct insertion,
local host transpositions, and complete coordinate reordering of the four best
abstract selectors.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Effective closure root | **AUDITED** | PX492 closes the asymptotic numerical ledger at `N_3=10^2900`. |
| Side-seven factor census | **COMPLETE** | PX493--PX495 give 132 saturated configurations, 488 ordered factors, and four relative classes. |
| Direct side-six insertion recursion | **REFUTED** | PX497 rejects all 21,952 inherited one-label host extensions. |
| Auxiliary `(2,2,2)` affine route | **REFUTED** | PX498 rejects all 6,912 affine hosts for the missing predecessor class. |
| Two-column selector normal form | **AVAILABLE** | PX499 writes every host as `g_ijs=A_j H^s P^i`; PX500 gives exact alternating-cycle selector moves. |
| Certified centre minima | **EXACT** | PX501 gives minimum triple counts `4,3,4,3` in the four best centre hosts. |
| Local transposition repair | **REFUTED** | PX502 rejects all 170,368 hosts in the four one-transposition product boxes. |
| Coordinate repair of centre selectors | **REFUTED** | PX505 rejects every bottom-row and two-column ordering of all four centre selectors. |
| Universal side-seven doubling | **OPEN** | A successful construction must change the abstract selector itself. |
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

The retained-order exponent is

\[
\frac65-1-\frac{16}{109}=\frac{29}{545}>0.
\]

## Exact side-seven classes

| Relative type | Configurations | Ordered factors |
|---|---:|---:|
| `(7)` | 60 | 120 |
| `(5,2)` | 32 | 128 |
| `(4,3)` | 20 | 80 |
| `(3,2,2)` | 20 | 160 |
| **Total** | **132** | **488** |

PX50 reduces universal `2 x 7 -> 14` closure to four canonical full-selector
host problems.

## Selector and coordinate decomposition

Put

\[
A_0=T,
\qquad
A_1=QT.
\]

Then

\[
\boxed{g_{ijs}=A_jH^sP^i}.
\]

After gauge-fixing the top row order, a fixed abstract selector has exactly 21
coordinate variables:

- seven values of `A_0`;
- seven values of `A_1`;
- seven values of the bottom-row order `R`;

with one all-different condition on each group. Every bad triple uses three
distinct abstract column vertices, so coordinate feasibility is an exact finite
CSP.

## Exact finite barriers

### Local host boxes

The four centre minima are

\[
(7):4,
\qquad
(5,2):3,
\qquad
(4,3):4,
\qquad
(3,2,2):3.
\]

All 170,368 hosts in their one-transposition product boxes fail, after
126,633,677 exact selector nodes.

### Complete coordinate orbits

Fix the abstract selector underlying each centre. Vary `A_0,A_1,R` over all of
`S_7^3` and use all four orientations. The exact CSP node counts are:

| Relative type | `cc` | `cf` | `fc` | `ff` | Total |
|---|---:|---:|---:|---:|---:|
| `(7)` | 95,187 | 128,576 | 84,090 | 118,771 | 426,624 |
| `(5,2)` | 123,744 | 126,196 | 124,181 | 127,384 | 501,505 |
| `(4,3)` | 136,854 | 311,894 | 124,166 | 264,514 | 837,428 |
| `(3,2,2)` | 93,186 | 91,698 | 124,604 | 152,878 | 462,366 |
| **Total** |  |  |  |  | **2,227,923** |

This rejects over two trillion raw coordinate assignments. It does not rule out
other abstract selectors.

## Immediate frontier

1. **Abstract selector search.** Traverse the degree-two selector space by
   alternating-cycle flips and send each new selector to the coordinate CSP.
2. **Cross-half obstruction.** Determine why many coordinate orderings make the
   top and bottom halves separately no-three but still force a mixed triple.
3. **Selector invariant.** Find a computable selector signature that predicts
   coordinate infeasibility before running the full 21-variable CSP.
4. **Single-cycle theorem.** Explain the persistent low-defect floor in the
   `(7)` class, or construct a selector outside the current basin.
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
```

Every recorded census and minimum uses exact integer determinants. Exact
all-side product closure and the classical no-three-in-line conjecture remain
open.
