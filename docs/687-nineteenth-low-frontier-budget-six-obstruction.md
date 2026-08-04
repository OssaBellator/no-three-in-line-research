# Nineteenth low-frontier budget-six obstruction

`docs/681` excludes every correction through deletion budget six for the unique
minimum-four nineteenth attempt. This chapter extends the exact obstruction to
all raw attempts whose minimum transversal is five or six.

## PP3ddt — Exact minimum-five and minimum-six frontier census

For the committed 144-point state and the same 1,032 raw nineteenth attempts,
there are

```text
minimum five: 13 attempts, 68 minimum cores,
minimum six:  46 attempts, 442 minimum cores.
```

The number of minimum cores per minimum-five attempt has histogram

```text
3:6, 5:3, 6:1, 9:2, 11:1.
```

The corresponding minimum-six histogram is

```text
1:6, 3:17, 5:1, 9:13, 11:1, 15:2,
21:2, 27:1, 33:1, 39:1, 81:1.
```

Together with the five minimum-four cores in `docs/681`, this accounts for all
515 minimum cores belonging to the 60 raw attempts with transversal at most six.

## PP3ddu — No low-frontier correction through budget six

For every minimum-five core, enumerate all row-and-column-preserving replacements
at budgets five and six. For every minimum-six core, enumerate the complete
budget-six replacement layer.

No legal correction exists. The exact rejected replacement counts are

```text
minimum-five cores, budget five:       4,890,
minimum-five cores, budget six:    4,258,350,
minimum-six cores, budget six:       142,200.
```

Thus the complete minimum-five and minimum-six frontier contributes

```text
4,405,440
```

additional rejected replacements beyond the minimum-four audit in `docs/681`.

The exact checker is
`scripts/check_boundary_nineteenth_low_frontier_obstruction.py`.

## PP3ddv — Exact remaining boundary alternatives

Every raw nineteenth attempt with minimum transversal at most six is now
obstructed through deletion budget six. A corrected nineteenth transition must
therefore use at least one of the following mechanisms:

1. deletion budget at least seven on a minimum-four, minimum-five, or minimum-six
   core;
2. a raw attempt whose minimum transversal is at least seven, with a correction
   budget at least that minimum;
3. a larger node repertoire, wider offset range, or different state
   representation.

The finite corrected chain remains at eighteen blocks. No twentieth spectrum,
recurrence, or periodic invariant is claimed.

## Evidence boundary

This is an exhaustive finite obstruction for the complete raw low-transversal
frontier of the current state. It does not exclude a budget-seven repair or an
alternative nineteenth construction.
