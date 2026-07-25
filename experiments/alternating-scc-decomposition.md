# Alternating-SCC decomposition regression

This experiment accompanies
[`docs/143-alternating-scc-nonsuperregular-decomposition.md`](../docs/143-alternating-scc-nonsuperregular-decomposition.md),
[`scripts/check_alternating_scc_decomposition.py`](../scripts/check_alternating_scc_decomposition.py),
and
[`alternating-scc-example.json`](alternating-scc-example.json).

Run

```bash
python scripts/check_alternating_scc_decomposition.py \
  experiments/alternating-scc-example.json
```

The six matching indices split into three alternating strong components:

```text
{0,1}
{2,3,4}
{5}
```

The first component has two perfect-matching states: the identity and the
transposition.  The second has two states: the identity and the directed
three-cycle

```text
2 -> 3 -> 4 -> 2.
```

The singleton component has only its reference edge.  Thus the predicted global
matching count is

```text
2 * 2 * 1 = 4.
```

Two allowed edges cross between strong components:

```text
1 -> 2
4 -> 5.
```

Neither belongs to any global perfect matching.  The exact enumeration therefore
verifies:

```text
global perfect matchings                   = 4
product of component state counts          = 4
forced reference indices                   = {5}
trivial strong-component indices           = {5}
cross-component selected-edge count        = 0
```

This finite regression validates the matching-state factorization and exact
forced-edge characterization.  It does not solve the geometric CSP or paid-cost
selection on a large flexible-component bank.
