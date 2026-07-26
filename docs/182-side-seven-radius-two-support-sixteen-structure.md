# Structure of the side-seven radius-two support-sixteen layer

PX535--PX536 leave `26,684` distance-two selectors at symmetric-difference
support sixteen, while PX537--PX540 subsequently close the complete `(3,2,2)`
radius-two layer.  This chapter classifies the support-sixteen graphs across all
four relative classes and identifies which two-step paths can use a 4-cycle.

Let `F_0` be the certified centre and `F` a radius-two selector with

\[
|F\triangle F_0|=16.
\]

## 1. Balanced support graph

The symmetric difference is a bipartite graph on the fourteen abstract rows and
fourteen abstract columns.  At every vertex its degree is `0`, `2`, or `4`,
because `F` and `F_0` both have degree two.

### Theorem PX541 -- PROVED

Every connected component of `F triangle F_0` has even size, and the complete
support-sixteen layer has exactly the following component-size shapes:

| Component edge sizes | Selectors |
|---|---:|
| `4+4+4+4` | 3,780 |
| `4+4+8` | 9,427 |
| `4+6+6` | 828 |
| `4+12` | 6,636 |
| `6+10` | 1,232 |
| `8+8` | 2,544 |
| `16` | 2,237 |
| **Total** | **26,684** |

The table is obtained by exact generation of the deduplicated radius-two layer
and graph traversal of every support.

## 2. Degree-four overlap profile

A degree-four support vertex records overlap between the two alternating-cycle
moves rather than a disjoint union of simple cycles.

### Theorem PX542 -- PROVED FINITE

The exact distribution by the number of degree-four row/column vertices is:

| Degree-four vertices | Selectors |
|---:|---:|
| 0 | 9,824 |
| 1 | 10,068 |
| 2 | 4,751 |
| 3 | 1,428 |
| 4 | 482 |
| 5 | 108 |
| 6 | 20 |
| 8 | 3 |
| **Total** | **26,684** |

Thus `9,824` supports are ordinary disjoint unions of alternating cycles, while
`16,860` contain at least one degree-four overlap vertex.

## 3. Short-cycle path coverage

For every support-sixteen selector, enumerate all radius-one parents and record
the two flip supports

\[
\bigl(|F_0\triangle P|,|P\triangle F|\bigr).
\]

### Theorem PX543 -- PROVED FINITE

The number of support-sixteen selectors admitting at least one radius-two path
with a 4-cycle as either flip is:

| Relative class | Support-sixteen selectors | With a 4-cycle path |
|---|---:|---:|
| `(7)` | 18,878 | 176 |
| `(5,2)` | 5,315 | 2,176 |
| `(4,3)` | 2,013 | 664 |
| `(3,2,2)` | 478 | 0 |
| **Total** | **26,684** | **3,016** |

Every support-sixteen selector has at least two radius-one parents; the
seven-cycle class has at least four.

### Corollary PX544 -- PROVED REDUCTION

Caching only children of radius-one 4-cycle moves can cover at most

\[
\frac{3016}{26684}<0.114
\]

of the active layer.  A complete support-sixteen census must handle general
larger-cycle overlaps or cache directly by selector support/coordinate state.

This structural result does not decide coordinate feasibility.

## 4. Verification

Compile and run

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_support_sixteen_structure.cpp \
  -o /tmp/side7_s16_structure
for c in cycle7 cycle52 cycle43 cycle322; do
  /tmp/side7_s16_structure "$c"
done
```

The verifier regenerates each radius-one and radius-two layer, deduplicates
selectors, checks support sixteen, traverses every symmetric-difference graph,
and verifies all parent-path counts.