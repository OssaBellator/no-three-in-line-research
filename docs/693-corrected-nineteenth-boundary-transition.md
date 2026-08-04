# Corrected nineteenth boundary transition

This chapter repairs the stale nineteenth-state coordinate inherited by the old
spectrum source, proves the sharp deletion budget, and advances the finite
boundary chain to nineteen blocks.

## PP3del — Canonical nineteenth state and sharp budget lower bound

Reconstruct the 144-point eighteenth state directly from the certified transition
in `docs/675`. The canonical point is

```text
(42,378),
```

not the stale source coordinate `(42,193)`. The reconstructed state has no
collinear triple and gives the exact raw nineteenth histogram

```text
4:2, 5:9, 6:47, 7:175, 8:283,
9:3, 10:16, 11:63, 12:121, 13:176, 14:137.
```

The two minimum-four attempts are

```text
P1/-33: ten conflict triples and one minimum core,
P2/-64: nine conflict triples and five minimum cores.
```

All six minimum-four cores have no row-and-column-preserving correction at
budgets four, five, or six. Therefore every corrected nineteenth transition has
deletion budget at least seven.

## PP3dem — Canonical seven-point nineteenth correction

Use node `P2` at offset `-64`, with block origin `(72,213)`, and the first
minimum core. Delete

```text
(8,34),
(13,77),
(16,76),
(46,1),
(73,151),
(75,150),
(75,152).
```

Add

```text
(8,77),
(13,152),
(16,151),
(46,150),
(73,34),
(75,1),
(75,76).
```

The deletion and addition multisets agree in every row and every column. The
result has 152 distinct points, nineteen blocks, and no collinear triple. Since
budget six is impossible on the complete minimum-four frontier, this budget-seven
transition is globally minimal among corrections based on a minimum-four raw
attempt.

The exact reconstruction, correction audits, and certificate verification are in
`scripts/check_boundary_nineteenth_transition.py`.

## PP3den — Exact raw twentieth spectrum

Using the corrected 152-point state and next origin `(76,213)`, all 1,032 raw
twentieth attempts fail. Their exact minimum-transversal histogram is

```text
4:3, 5:21, 6:73, 7:195, 8:224,
9:4, 10:35, 11:98, 12:140, 13:153, 14:86.
```

There are three minimum-four attempts:

```text
P1/-28: eleven conflict triples and one minimum core,
P2/52:  ten conflict triples and five minimum cores,
P3/-27: ten conflict triples and three minimum cores.
```

Thus the next correction frontier contains nine minimum-four cores across three
raw attempts.

## Evidence boundary

This is an exact finite transition and an exact raw twentieth census. It does not
supply a recurrence, a periodic boundary signature, or an all-length coordinate
construction. The all-`n` theorem remains open, and the next theorem identifier is
`PP3deo`.
