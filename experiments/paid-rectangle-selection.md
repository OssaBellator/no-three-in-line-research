# Paid binary rectangle-selection regression

This experiment accompanies
[`docs/122-paid-binary-rectangle-selection.md`](../docs/122-paid-binary-rectangle-selection.md),
[`scripts/check_paid_rectangle_selection.py`](../scripts/check_paid_rectangle_selection.py),
and
[`paid-rectangle-selection-example.json`](paid-rectangle-selection-example.json).

Run

```bash
python scripts/check_paid_rectangle_selection.py \
  experiments/paid-rectangle-selection-example.json
```

The fixture has six binary rectangle variables, each taking state one with
probability `1/10`. There are six cyclic rank-three bad boxes, each requiring
three specified state-one choices. Thus every bad box has probability

```text
1/1000,
```

and

```text
total clause probability = 6/1000 = 3/500.
```

Every variable occurs in three bad boxes, so the local clause mass is

```text
lambda = 3/1000 < 1/24.
```

Each state-one choice has unary insertion cost two. Six adjacent variable pairs
have binary cost three only when both states are one. Therefore

```text
expected unary cost  = 6/5,
expected binary cost = 9/50,
expected total cost  = 69/50.
```

With removal credit four, the paid first-moment value is

```text
3/500 + (69/50)/4
= 351/1000
< 1.
```

The PP3oz conditioned local-lemma cost is also below four. Exact enumeration of
all 64 assignments finds satisfying assignments with insertion cost below the
credit; the all-zero assignment has cost zero.

This is a regression for the probability, local-mass, cost, and exact-enumeration
calculations. It does not assert that every geometric common-line rectangle bank
has diffuse clauses or collateral.
