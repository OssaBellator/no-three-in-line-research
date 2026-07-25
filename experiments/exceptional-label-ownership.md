# Exceptional-label balanced-ownership regression

This experiment accompanies
[`docs/108-exceptional-label-balanced-ownership.md`](../docs/108-exceptional-label-balanced-ownership.md),
[`scripts/check_exceptional_label_ownership.py`](../scripts/check_exceptional_label_ownership.py),
and
[`exceptional-label-ownership-example.json`](exceptional-label-ownership-example.json).

Run

```bash
python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-example.json
```

The fixture has

```text
T = 6 movement labels,
M = 3 macros,
W = 2 labels per macro,
r = 1.
```

Every movement label has score `4` in one macro and score `1` in the other two.
Thus each label rejects one macro, and each macro rejects two labels.  The expanded
ownership-host degrees are

```text
degree of every movement label = W*2 = 4,
degree of every macro copy     = 4.
```

Every ownership nonedge therefore has degree sum

```text
4+4=8 >= T=6.
```

The exact checker finds the balanced ownership

```text
labels 0,1 -> macro 1,
labels 2,3 -> macro 2,
labels 4,5 -> macro 0.
```

The capped refill scores are

```text
3, 1, 2, 0, 2, 2.
```

Since `r=1`, every refill label satisfies

```text
r + capped score <= 4 <= T.
```

Hence PP3mk is certified even though no movement label is acceptable in every
macro.  This finite regression verifies the ownership matching, heterogeneous
Ore inequalities, and capped refill calculation.  It does not assert that the
geometric controller-defect scores of every asymptotic source satisfy these
bounds.
