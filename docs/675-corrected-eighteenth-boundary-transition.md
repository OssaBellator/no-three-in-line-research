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

## PP3dcl — Exact raw nineteenth spectrum

Using next origin `(72,213)`, all 1,032 raw nineteenth attempts fail. Their exact
minimum-transversal histogram is

```text
4:2, 5:9, 6:47, 7:175, 8:283,
9:3, 10:16, 11:63, 12:121, 13:176, 14:137.
```

The two minimum-four attempts are

```text
P1/-33: one minimum core,
P2/-64: five minimum cores.
```

Thus the next correction frontier contains six minimum cores across two attempts.
The exact spectrum is `scripts/check_boundary_nineteenth_spectrum.cpp`, and the
combined state audit is `scripts/check_boundary_eighteenth_transition.py`.

## Evidence boundary

The corrected finite chain now reaches eighteen blocks. No corrected nineteenth
transition, recurrence, periodic state invariant, or all-length construction is
proved.
