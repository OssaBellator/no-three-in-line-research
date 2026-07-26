# Controller-entry deletion telescoping diagnostic

Run

```text
python scripts/check_controller_entry_deletion_telescoping.py \
  experiments/controller-entry-deletion-telescoping-example.json
```

The example contains one surviving candidate entry and two entries whose
controllers are punctured later.  The active chronological potentials are

```text
[9, 11, 10, 4].
```

Thus the potential may increase during intermediate trades, but the complete
package decreases it by five.

The surviving entry changes from `3` to `4`, contributing `+1`.  The two deleted
entries have initial blocker masses `4` and `2`; their complete chronological
contributions are exactly `-4` and `-2`, regardless of the second deleted entry's
intermediate trajectory

```text
2 -> 6 -> 8.
```

The expected output is

```text
chronological potentials [9, 11, 10, 4]
surviving-entry change 1
initial deleted-entry mass 6
deleted-entry contributions {'z1': -4, 'z2': -2}
exact chronological change -5
outcome controller_entry_deletion_exact_telescoping
```

This verifies PP3aqu--PP3aqv: every later-deleted candidate entry contributes only
the negative of its initial blocker mass.  All intermediate future-controller
credit dependencies on that entry cancel automatically.
