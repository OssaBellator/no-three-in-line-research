# Corrected fifteenth boundary transition

This chapter continues the corrected radius-64 boundary chain from the legal
112-point, fourteen-block state in `docs/651-corrected-fourteenth-boundary-transition.md`.

## PP3dah — Exact fifteenth low-transversal census

The complete raw fifteenth spectrum is already recorded by
`scripts/check_boundary_fifteenth_spectrum.cpp`:

```text
4:10, 5:36, 6:100, 7:193, 8:186,
9:28, 10:81, 11:106, 12:151, 13:110, 14:31.
```

Exactly ten attempts have minimum transversal four.  Their minimum-core counts are

```text
P0/-45:9, P0/-33:3, P0/-30:45, P0/-28:3, P0/-25:9,
P1/-28:15, P2/-29:27, P2/-26:9, P3/-26:27, P3/-23:9.
```

Thus there are exactly 156 minimum cores.

## PP3dai — Every minimum core repairs through budget seven

Every one of the 156 minimum cores has a row-and-column-preserving legal
correction with deletion size at most seven.  The exact first-success budget
histogram is

```text
4:6, 5:70, 6:74, 7:6.
```

The exhaustive correction kernel is
`scripts/check_boundary_fifteenth_corrections.cpp`.

## PP3daj — Canonical correction and raw sixteenth obstruction

Use `P0` at offset `-30`, from origin `(56,376)`.  Delete

```text
(9,59),(19,74),(58,349),(59,346)
```

and add

```text
(9,349),(19,346),(58,74),(59,59).
```

The corrected state has 120 points, fifteen blocks, and no collinear triple.
Using next origin `(60,346)`, all 1,032 raw sixteenth attempts fail.  Their exact
minimum-transversal histogram is

```text
4:9, 5:21, 6:88, 7:166, 8:238,
9:8, 10:38, 11:83, 12:157, 13:151, 14:73.
```

The audit wrapper is `scripts/check_boundary_fifteenth_transition.py`.

## Evidence boundary

The corrected finite chain now reaches fifteen blocks.  No corrected sixteenth
transition, recurrence, periodic state invariant, or all-length construction is
proved.
