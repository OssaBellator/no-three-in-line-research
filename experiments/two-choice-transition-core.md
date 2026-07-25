# Two-choice transition core regression

This experiment accompanies:

- [`docs/169-two-valued-transition-pseudoforest-factorization.md`](../docs/169-two-valued-transition-pseudoforest-factorization.md);
- [`scripts/check_two_choice_transition_core.py`](../scripts/check_two_choice_transition_core.py);
- [`two-choice-transition-core-example.json`](two-choice-transition-core-example.json).

Run

```bash
python scripts/check_two_choice_transition_core.py \
  experiments/two-choice-transition-core-example.json
```

## Feasible case

The choice family is

```text
p0 -> {0,1}
p1 -> {0,1}
p2 -> {2}
p3 -> {3,4}
p4 -> {4}.
```

Its choice multigraph has three unicyclic components:

```text
vertices {0,1}: two parallel labelled edges;
vertex  {2}:   one loop;
vertices {3,4}: one ordinary edge and one loop at 4.
```

There are exactly two injective representatives:

```text
(0,1,2,3,4)
(1,0,2,3,4).
```

Relative to the first representative, the only nontrivial alternating SCC is

```text
{0,1},
```

with arcs `0->1` and `1->0`. The allowed edge `4->3` lies between trivial SCCs and
occurs in no perfect matching. Thus the exact factor count is

```text
2^1=2.
```

## Infeasible case

The balanced choice family is

```text
p0 -> {0,1}
p1 -> {1,2}
p2 -> {2,0}
p3 -> {0,1}.
```

All four middle choices have neighbourhood

```text
{0,1,2},
```

so Hall deficiency is one:

```text
4 choices - 3 resources = 1.
```

The witness multigraph has four edges, three vertices, degree sequence

```text
3,3,2,
```

and cyclomatic number two. Suppressing the degree-two vertex gives three parallel
paths between the two degree-three branch vertices: a theta core.

The checker logic was independently reproduced on 25 July 2026. It returns two
representatives in the feasible case and the four-choice theta Hall witness in the
infeasible case. This finite regression verifies the exact set-system and
alternating-factorization identities; it does not establish the asymptotic paid
conversion of the resulting Boolean bank.
