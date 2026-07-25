# Two-sided balanced-label ownership regression

This experiment accompanies
[`docs/110-two-sided-balanced-label-ownership.md`](../docs/110-two-sided-balanced-label-ownership.md),
[`scripts/check_two_sided_label_ownership.py`](../scripts/check_two_sided_label_ownership.py),
and
[`two-sided-label-ownership-example.json`](two-sided-label-ownership-example.json).

Run

```bash
python scripts/check_two_sided_label_ownership.py \
  experiments/two-sided-label-ownership-example.json
```

The fixture has three compatibility graphs on six movement and six refill labels,
with `W=2`. Macro zero omits the `2 by 2` block on labels `{0,1}`, macro one omits
the block on `{2,3}`, and macro two omits the block on `{4,5}`.

Every label therefore has nondegree two in one macro and nondegree zero in the
other two. With

```text
r = s = 1,
r+s = 2 = W,
```

both ownership hosts route every label away from its bad macro. The checker finds

```text
movement labels 4,5 and refill labels 4,5 -> macro 0,
movement labels 0,1 and refill labels 0,1 -> macro 1,
movement labels 2,3 and refill labels 2,3 -> macro 2.
```

Every induced macro graph is the complete `2 by 2` graph. The local matching
sizes are all two, so PP3mq is certified.

This finite regression verifies the two independent balanced ownerships and the
induced local matching calculation. It does not assert that asymptotic geometric
controller-defect scores are always below the local scale `W`.
