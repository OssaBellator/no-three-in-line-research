# Corrected eighteenth boundary transition

This chapter continues the corrected radius-64 boundary chain from the legal
136-point, seventeen-block state in
`docs/669-corrected-seventeenth-boundary-transition.md`.

## PP3dcj — Exhaustive correction census through budget six

The raw eighteenth frontier has seven minimum-four cores across three attempts:

```text
P0/-39: three cores,
P2/-40: three cores,
P2/-26: one core.
```

For every core, enumerate every row-and-column-preserving replacement at deletion
budgets four, five, and six. No core repairs at budget four or five. At budget six,
exactly one core repairs: the second minimum core of `P0/-39`.

The other six cores have no preserving correction through budget six. This is a
finite exact obstruction only; budget seven and larger are not excluded.

The audit is `scripts/check_boundary_eighteenth_corrections.cpp`.

## PP3dck — Canonical six-point eighteenth correction

Use node `P0` at offset `-39`, with block origin `(68,213)`. For its second
minimum core, delete

```text
(2,257),(31,111),(58,347),(69,216),(71,213),(71,215)
```

and add

```text
(2,213),(31,257),(58,216),(69,215),(71,111),(71,347).
```

The deletion and addition multisets agree in every row and every column. The
corrected state has 144 distinct points, eighteen blocks, and no collinear triple.
In particular, the canonical state contains `(42,378)`, not the stale coordinate
`(42,193)` that appeared in an earlier nineteenth-spectrum source snapshot.

## PP3dcl — Corrected raw nineteenth spectrum

Using next origin `(72,213)`, all 1,032 raw nineteenth attempts fail. Rebuilding
from the certified eighteenth transition gives the exact minimum-transversal
histogram

```text
4:2, 5:9, 6:47, 7:175, 8:283,
9:3, 10:16, 11:63, 12:121, 13:176, 14:137.
```

There are two minimum-four attempts:

```text
P1/-33: ten conflict triples and one minimum core,
P2/-64: nine conflict triples and five minimum cores.
```

The exact reconstruction and transition audit is
`scripts/check_boundary_nineteenth_transition.py`.

## Evidence boundary

The corrected finite chain reaches eighteen blocks in this chapter. The later
budget-seven correction in `docs/693` reaches nineteen blocks, but no recurrence,
periodic state invariant, or all-length construction follows from either finite
transition.
