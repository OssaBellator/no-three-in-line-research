# Nineteenth boundary budget-six obstruction

This chapter continues from the corrected 144-point, eighteen-block state in
`docs/675-corrected-eighteenth-boundary-transition.md` after correcting the stale
nineteenth spectrum assertion.

## PP3ddb — Unique minimum-four nineteenth attempt

For the current 144-point state and next origin `(72,213)`, the exact raw
nineteenth spectrum has a unique minimum-four attempt:

```text
P2/-64: nine conflict triples and five minimum cores.
```

The five cores are

```text
(13,77),(73,151),(75,150),(75,152),
(33,101),(73,151),(75,150),(75,152),
(36,163),(73,149),(73,151),(75,152),
(39,162),(73,149),(73,151),(75,152),
(73,149),(73,151),(75,150),(75,152).
```

The formerly listed `P1/-33` case is not a minimum-four attempt for the committed
state: it has eleven conflict triples, minimum transversal five, and three
minimum-five cores.

## PP3ddc — No preserving correction through budget six

For each of the five `P2/-64` cores, enumerate every row-and-column-preserving
replacement at deletion budgets four, five, and six. No legal replacement exists.

For every core the exact permutation counts are

```text
budget 4:       24,
budget 5:   17,520,
budget 6: 7,595,280.
```

Thus the exhaustive budget-six audit checks

```text
5 * 7,595,280 = 37,976,400
```

six-point replacements, in addition to all budget-four and budget-five
replacements, without finding a legal corrected state.

The checker is `scripts/check_boundary_nineteenth_corrections.cpp`.

## PP3ddd — Exact remaining boundary frontier

The corrected finite chain remains at eighteen blocks. Any correction based on a
minimum nineteenth core now requires deletion budget at least seven, or a change
of raw attempt, node repertoire, search radius, or state representation.

No corrected nineteenth transition is available, so no raw twentieth spectrum is
claimed. Budget seven is not excluded by this chapter.

## Evidence boundary

This is a finite exact obstruction for one state and the complete minimum-four
frontier through budget six. It is not a recurrence, periodic invariant, or
all-length construction.
