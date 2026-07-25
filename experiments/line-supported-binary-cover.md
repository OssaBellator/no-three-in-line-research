# Line-supported binary-cover regression

This experiment accompanies
[`docs/104-line-supported-binary-covers.md`](../docs/104-line-supported-binary-covers.md),
[`scripts/check_binary_shadow_cover.py`](../scripts/check_binary_shadow_cover.py),
and
[`line-supported-binary-cover-example.json`](line-supported-binary-cover-example.json).

Run

```bash
python scripts/check_binary_shadow_cover.py \
  experiments/line-supported-binary-cover-example.json
```

The four endpoint cells

```text
(0,1), (1,2), (2,3), (3,4)
```

form one nonaxis line trace and use pairwise distinct left and right resources.
All six pairs of these cells are declared binary conflicts.  Deleting any three
of the four cells covers the complete conflict clique.

The exact checker returns

```text
binary conflicts             = 6,
minimum cover size           = 3,
minimum resource congestion  = 1.
```

For the displayed cover

```text
{(0,1), (1,2), (2,3)},
```

every left and right resource is used at most once.  The residual `5 by 5` host
still has a perfect matching.  This is the finite form of PP3lm--PP3ln: line
richness increases cover cardinality but not endpoint-resource congestion.
