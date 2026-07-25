# Exceptional-label balanced-ownership regressions

These experiments accompany
[`docs/108-exceptional-label-balanced-ownership.md`](../docs/108-exceptional-label-balanced-ownership.md),
[`docs/109-ownership-hall-core-localization.md`](../docs/109-ownership-hall-core-localization.md),
[`docs/111-ownership-bottleneck-refill-slack.md`](../docs/111-ownership-bottleneck-refill-slack.md),
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
3, 1, 2, 0, 2, 2,
```

and the corresponding refill slacks are

```text
3, 5, 4, 6, 4, 4.
```

Hence

```text
ownership bottleneck = 1,
minimum refill slack = 3,
```

so both PP3mk and the threshold-free PP3mx comparison are certified.

## 2. Exact ownership Hall and bottleneck-slack gap

Run

```bash
python scripts/check_exceptional_label_ownership.py \
  experiments/exceptional-label-ownership-hall-example.json
```

At the displayed threshold `r=1`, movement labels `0,1,2` accept only macro zero.
That macro has capacity `W=2`, so the exact matching size is five. The checker
returns

```text
movement Hall set       = {0,1,2},
acceptable macro set    = {0},
label count             = 3,
macro capacity          = 2,
deficiency              = 1.
```

All pairs between these three labels and macros one and two are unacceptable,
which is the PP3mn high-score rectangle.

The least threshold at which a balanced movement ownership exists is

```text
ownership bottleneck = 4.
```

Every column score equals `W=2`, so every refill slack is zero. Thus

```text
minimum refill slack = 0,
4 > 0,
```

and the threshold-free PP3mz gap is also present.

These are finite regressions for the matching, Hall, bottleneck, and slack
calculations. They do not assert that every geometric controller-defect instance
satisfies the successful score bounds.
