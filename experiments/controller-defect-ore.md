# Controller-defect Ore-score regression

This experiment accompanies
[`docs/106-controller-defect-ore-scores.md`](../docs/106-controller-defect-ore-scores.md),
[`scripts/check_controller_defect_ore.py`](../scripts/check_controller_defect_ore.py),
and
[`controller-defect-ore-example.json`](controller-defect-ore-example.json).

Run

```bash
python scripts/check_controller_defect_ore.py \
  experiments/controller-defect-ore-example.json
```

The fixture has two macros, four movement labels, four refill labels, pool size
`R=12`, and `gamma=1/2`.  The first movement label in macro zero has five unsafe
controller values, and the first refill label has two.  All other cell and anchor
defects are zero.

The certified union-bound graph therefore has exactly one nonedge:

```text
macro 0, movement label 0, refill label 0.
```

Its degree data are

```text
movement-row degree              = 3,
average refill-column degree     = 7/2,
complementary degree sum         = 13/2.
```

The PP3ly defect scores are

```text
movement row score               = 2,
average refill column score      = 5/8,
score sum                         = 21/8.
```

For `h=1`, the PP3lz geometric condition is

```text
21/8 <= T-h = 3,
```

so the local complementary-defect inequality succeeds.  The actual degree sum is
also well above

```text
T+h = 5.
```

The finite value of

```text
T*exp(-h^2/(32T))
```

is not below one, so this small fixture does not certify the random balanced
ownership step.  Its purpose is to verify the exact defect-to-nondegree formulas;
the concentration hypothesis is asymptotic and is met by taking
`h=8*sqrt(T log T)` in the theorem.
