# Corrected seventeenth boundary transition

This chapter continues the corrected radius-64 boundary chain from the legal
128-point, sixteen-block state in
`docs/663-corrected-sixteenth-boundary-transition.md`.

## PP3dbr — Exact repair census for the unique minimum-three attempt

The unique minimum-three raw seventeenth attempt is `P2` at offset `-57`, with
block origin `(64,252)`. It has exactly five conflict triples and exactly three
minimum transversals.

All three minimum cores admit a row-and-column-preserving legal correction. Each
first succeeds at deletion budget five, so the exact first-success distribution is

```text
5:3.
```

The exhaustive audit is
`scripts/check_boundary_seventeenth_corrections.cpp`.

## PP3dbs — Canonical five-point correction

The raw `P2` block is

```text
(64,253),(64,255),(65,252),(65,254),
(66,252),(66,254),(67,253),(67,255).
```

For the canonical first core, delete

```text
(0,110),(42,193),(54,378),(64,253),(66,252)
```

and add

```text
(0,252),(42,378),(54,253),(64,110),(66,193).
```

The deletion and addition multisets agree in every row and column. The corrected
state has 136 distinct points, seventeen blocks, and no collinear triple.

## PP3dbt — Exact raw eighteenth spectrum

Using next origin `(68,252)`, all 1,032 raw eighteenth attempts fail. Their exact
minimum-transversal histogram is

```text
4:3, 5:16, 6:70, 7:211, 8:218,
9:2, 10:15, 11:68, 12:152, 13:178, 14:99.
```

The three minimum-four attempts are

```text
P0/-39: three minimum cores,
P2/-40: three minimum cores,
P2/-26: one minimum core.
```

Thus the next correction frontier contains seven minimum cores across three
attempts. The exact spectrum is
`scripts/check_boundary_eighteenth_spectrum.cpp`, and the combined state audit is
`scripts/check_boundary_seventeenth_transition.py`.

## Evidence boundary

The corrected finite chain now reaches seventeen blocks. No corrected eighteenth
transition, recurrence, periodic state invariant, or all-length construction is
proved.
