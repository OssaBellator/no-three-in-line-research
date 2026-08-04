# Twenty-second boundary budget-six obstruction

This chapter continues from the selected 168-point, twenty-one-block state in
`docs/694-alternative-boundary-continuation-through-twenty-one-blocks.md`.

## PP3der — Exact minimum-six twenty-second frontier

From next origin `(84,213)`, the exact raw twenty-second spectrum is

```text
6:26,7:205,8:285,9:1,10:3,
11:38,12:100,13:199,14:175.
```

Thus the raw minimum transversal is six. The 26 minimum-six attempts contain
exactly 178 minimum cores.

## PP3des — No preserving correction at budget six

For every minimum core, delete its six points and enumerate every distinct
permutation of the deleted column multiset among the deleted rows. Reject the
identity replacement and test the complete no-three condition against the
remaining 170 points and among the six replacement points.

The number of distinct row/column matchings per core has histogram

```text
180: 49 cores,
360: 92 cores,
720: 37 cores.
```

Therefore the exact budget-six layer contains

```text
49*180 + 92*360 + 37*720 = 68,580
```

replacement permutations. Every one is rejected. No minimum-six twenty-second
core has a preserving correction at its minimum deletion budget.

## PP3det — Remaining boundary frontier

The corrected finite chain remains at twenty-one blocks. Any correction based on
the raw minimum frontier now requires deletion budget at least seven, a raw
attempt of larger transversal, or a changed repertoire/state representation.

The exact audit is
`scripts/check_boundary_twentysecond_budget_six_obstruction_695.py`. It rebuilds
the selected 21-block state through the canonical continuation audit and uses the
independent legacy permutation kernel for the complete budget-six layer.

This is a finite exact obstruction. It is not a recurrence, periodic invariant,
or all-length construction. The all-`n` theorem remains open.
