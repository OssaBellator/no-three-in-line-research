# Two-rectangle trade-bank experiments

These computations use
[`scripts/search_width_two_two_rectangle_repairs.py`](../scripts/search_width_two_two_rectangle_repairs.py)
and the exact multi-rectangle theorem in
[`docs/44-multi-rectangle-trade-banks.md`](../docs/44-multi-rectangle-trade-banks.md).

## Exhaustive two-switch search

The command

```bash
python scripts/search_width_two_two_rectangle_repairs.py \
  certificates/prime-patching-small.json
```

starts from every distinct internally clean cross-only width-two matching-patch
state.  For a proposed first switch, the original triples it leaves untouched
must have a transversal of size at most two, because the second switch removes
only two points.  Proposition PP3bc proves that this filter is necessary, so the
search remains exhaustive.

| Source | Target | Initial states | Promising first switches | Repair sequences | Distinct two-switch finals | Additional finals beyond one switch |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 20 | 804 | 63 | 10 | 9 |
| 5 | 7 | 149 | 7,365 | 39 | 8 | 7 |
| 6 | 8 | 969 | 41,599 | 83 | 15 | 14 |
| 7 | 9 | 3,686 | 51,906 | 0 | 0 | 0 |
| 8 | 10 | 9,813 | 49,324 | 0 | 0 | 0 |
| 9 | 11 | 22,555 | 13,308 | 0 | 0 | 0 |
| 10 | 12 | 43,539 | 21,928 | 0 | 0 | 0 |

The first three rows show that depth two is genuinely stronger than one
rectangle: the previous one-switch search produced only one final configuration
at each of sources four, five, and six.  The last four rows are complete negative
results for two sequential alternating rectangle switches on the stored seeds.

## Exact Boolean trade-bank fixture

The file
[`two-rectangle-bank-n4.json`](two-rectangle-bank-n4.json)
contains one side-six near miss and two corner-disjoint protected rectangles.
Running

```bash
python scripts/solve_rectangle_trade_bank.py \
  experiments/two-rectangle-bank-n4.json
```

constructs the exact triple clauses and returns:

- two Boolean rectangle variables;
- eight potentially selected collinear triples;
- four distinct clauses, two unary and two binary;
- maximum clause rank two;
- the satisfying assignment that switches both rectangles.

The resulting side-six configuration is

```text
(1,1), (1,3), (2,4), (2,5),
(3,2), (3,6), (4,1), (4,2),
(5,5), (5,6), (6,3), (6,4).
```

It is independently checked to have exactly two points in every row and column
and no collinear triple.

## Interpretation

Rectangle repair is not merely a bounded-depth search primitive.  A prepared
corner-disjoint rectangle family is an exact rank-three SAT bank, and becomes
2-SAT whenever no potential triple involves three rectangle variables.  The
finite positive examples demonstrate satisfiable rank-two banks; the negative
results from source side seven onward show that protected rectangles must be
installed with geometric intent rather than chosen post hoc from arbitrary
matching-patch near misses.
