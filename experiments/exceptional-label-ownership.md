# Exceptional-label balanced-ownership regressions

These experiments accompany
[`docs/108-exceptional-label-balanced-ownership.md`](../docs/108-exceptional-label-balanced-ownership.md),
[`docs/109-ownership-hall-core-localization.md`](../docs/109-ownership-hall-core-localization.md),
and
[`scripts/check_exceptional_label_ownership.py`](../scripts/check_exceptional_label_ownership.py).

## 1. Successful exceptional-label routing

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
Thus each label rejects one macro, and each macro rejects two labels. The expanded
ownership-host degrees are

```text
degree of every movement label = W*2 = 4,
degree of every macro copy     = 4.
```

Every ownership nonedge has degree sum

```text
4+4=8 >= T=6.
```

The exact checker finds

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
macro.

## 2. Exact ownership Hall core

Run

```bash
python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-hall-example.json
```

Movement labels `0,1,2` accept only macro zero. That macro has capacity `W=2`,
so the exact matching size is five rather than six. The checker returns

```text
movement Hall set       = {0,1,2},
acceptable macro set    = {0},
label count             = 3,
macro capacity          = 2,
deficiency              = 1.
```

All pairs between these three labels and macros one and two are unacceptable,
which is the PP3mn high-score rectangle.

These are finite regressions for the matching and Hall calculations. They do not
assert that every geometric controller-defect instance satisfies the successful
score bounds.
