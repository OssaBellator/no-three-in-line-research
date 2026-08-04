# Alternative boundary continuation through twenty-one blocks

This chapter continues the corrected boundary history in `docs/693`. That chapter
certifies the sharp budget-seven nineteenth threshold and one valid first repair.
The present chapter compares both budget-seven repairs, selects the stronger raw
twentieth continuation, and advances the finite chain twice more.

## PP3deo — The second nineteenth repair has the smaller low twentieth frontier

For `P2/-64`, the first two minimum cores both admit a preserving correction for
the first time at budget seven. The first repair used in `docs/693` gives raw
twentieth histogram

```text
4:3,5:21,6:73,7:195,8:224,9:4,
10:35,11:98,12:140,13:153,14:86.
```

The second repair deletes

```text
(1,113),(33,101),(57,347),(62,106),
(73,151),(75,150),(75,152)
```

and adds

```text
(1,150),(33,347),(57,151),(62,152),
(73,101),(75,106),(75,113).
```

It has no preserving repair at budgets four, five, or six and first repairs at
budget seven. Its raw twentieth histogram is

```text
4:2,5:14,6:74,7:199,8:227,9:2,
10:23,11:91,12:160,13:149,14:91.
```

Thus its number of attempts at transversal at most six is `90`, compared with
`97` for the first repair. We use this second repaired state as the continuation
branch. This does not invalidate the first repair or the sharp lower bound in
`docs/693`; it changes only the selected finite continuation.

## PP3dep — Exact twentieth and twenty-first corrections

The selected 152-point state has two minimum-four twentieth attempts:

```text
P1/-28: 3 minimum cores,
P3/-27: 9 minimum cores.
```

Across these twelve cores, five have no repair through budget seven, six first
repair at budget seven, and exactly one first repairs at budget six. It is
`P3/-27` core 6, containing

```text
(62,309),(70,214),(76,188),(78,187).
```

Delete

```text
(4,33),(7,32),(62,309),(70,214),(76,188),(78,187)
```

and add

```text
(4,188),(7,187),(62,33),(70,309),(76,214),(78,32).
```

The resulting 160-point, twenty-block state has raw twenty-first histogram

```text
4:3,5:11,6:63,7:184,8:255,9:3,
10:13,11:51,12:117,13:180,14:152.
```

Its minimum-four frontier consists of 33 cores across `P0/59`, `P2/60`, and
`P3/60`. None repairs at budget four or five; exactly eleven repair at budget six.

## PP3deq — Selected twenty-first repair raises the next minimum to six

For each of the eleven budget-six repairs, compute the complete raw twenty-second
spectrum. Two repaired states attain minimum transversal six. Under the selection
rule

```text
maximize the minimum transversal,
then minimize the number of minimum attempts,
```

`P3/60` core 8 is selected over core 23 because it has 26 minimum attempts rather
than 37.

Core 8 is

```text
(10,58),(29,111),(81,276),(83,276).
```

Delete

```text
(10,58),(18,76),(29,111),(53,376),(81,276),(83,276)
```

and add

```text
(10,276),(18,276),(29,376),(53,58),(81,111),(83,76).
```

The resulting state has 168 distinct points, twenty-one blocks, and no collinear
triple. From next origin `(84,213)`, its exact raw twenty-second histogram is

```text
6:26,7:205,8:285,9:1,10:3,
11:38,12:100,13:199,14:175.
```

The minimum-six frontier contains 26 attempts and 178 minimum cores.

## Reproducibility and evidence boundary

The canonical path audit is
`scripts/check_boundary_continuation_694.py`. The independent eleven-state
selection census is `scripts/check_boundary_twentyfirst_selection_694.py`, and
the exact data are recorded in
`certificates/prime-patching-boundary-continuation-694.json`.

This is a finite exact chain through twenty-one blocks. It does not provide a
recurrence, a periodic state invariant, or an all-length construction. The
all-`n` theorem remains open.
