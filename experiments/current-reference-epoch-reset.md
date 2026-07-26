# Current-reference epoch-reset diagnostic

Run

```text
python scripts/check_current_reference_epoch_reset.py \
  experiments/current-reference-epoch-reset-example.json
```

The stored active layer starts equal to its epoch reference.  A four-row seed and two
fresh-helper growth moves produce the exact defect sequence

```text
4, 7, 10.
```

The union of all selected indices has size ten, exactly the final defect size.  Even
when all selected indices are treated as controllers, the epoch puncture cost is ten;
with `R=10,000` its ratio is `0.001`.

After the paid epoch is conceptually completed, the current active layer is declared
the new reference.  Its relative defect becomes zero immediately.  A new four-row
seed then creates a fresh defect of size four while the complementary permutation
layer remains unchanged.

The exact output is

```text
m 30
q 4
first epoch defect sizes [4, 7, 10]
first epoch selected indices 10
selected punctures 10
puncture to R ratio 0.001
defect after reference reset 0
next epoch seed defect 4
complementary layer preserved True
outcome current_reference_epoch_reset
```

This verifies PP3ato--PP3ats in a finite two-epoch model.  Monotone defect growth uses
one fixed current reference only inside an epoch; historical preservation of the
initial layer is unnecessary.
