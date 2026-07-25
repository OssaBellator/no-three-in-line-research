# Binary-shadow congestion-cover regression

This experiment accompanies
[`docs/102-binary-shadow-congestion-covers.md`](../docs/102-binary-shadow-congestion-covers.md),
[`scripts/check_binary_shadow_cover.py`](../scripts/check_binary_shadow_cover.py),
and
[`binary-shadow-cover-example.json`](binary-shadow-cover-example.json).

Run

```bash
python scripts/check_binary_shadow_cover.py \
  experiments/binary-shadow-cover-example.json
```

The endpoint host is the off-diagonal `4 by 4` bipartite graph.  Its three binary
shadow conflicts form a fan centred at the cell `(0,1)`:

```text
{(0,1),(1,2)},
{(0,1),(2,3)},
{(0,1),(3,0)}.
```

The exact minimum-congestion cover is

```text
C = {(0,1)}.
```

It has:

```text
cover size                 = 1,
maximum resource congestion = 1.
```

Deleting this one cell removes all three binary conflicts.  The residual host has
11 edges and still has a perfect matching, for example

```text
(0,3), (1,2), (2,1), (3,0).
```

Thus the fan is converted exactly into one unary deletion.  This is a finite
regression for PP3la--PP3lc, not an asymptotic proof that every controller-shadow
instance has low fractional congestion.
