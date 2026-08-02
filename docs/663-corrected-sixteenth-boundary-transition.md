# Corrected sixteenth boundary transition

This chapter continues the radius-64 corrected boundary chain from the legal
120-point, fifteen-block state in
`docs/657-corrected-fifteenth-boundary-transition.md`.

## PP3daz — Exact sixteenth low-transversal census

For the eight node variants and all 129 offsets in `[-64,64]`, the 1,032 raw
sixteenth attempts have exact minimum-transversal histogram

```text
4:9, 5:21, 6:88, 7:166, 8:238,
9:8, 10:38, 11:83, 12:157, 13:151, 14:73.
```

Exactly nine attempts have minimum transversal four. Their minimum-core counts
are

```text
P0/-38:7,
P1/-37:15, P1/-27:3, P1/-26:1,
P2/-37:5, P2/-27:5, P2/-25:1, P2/-4:1,
P3/-25:1.
```

Thus the low frontier contains exactly thirty-nine minimum cores. The exhaustive
census is `scripts/check_boundary_sixteenth_spectrum.cpp`.

## PP3dba — Certified four-point sixteenth correction

Use node `P1` at offset `-37`, with block origin `(60,309)`. Delete

```text
(22,106),(39,165),(48,315),(62,312)
```

and add

```text
(22,315),(39,312),(48,165),(62,106).
```

The deletion and addition multisets agree in every row and column. The corrected
state has 128 points, sixteen blocks, and no collinear triple.

This theorem certifies one exact repair. It does not claim that all thirty-nine
minimum cores, or all nine minimum-four attempts, repair within a fixed budget.

## PP3dbb — Exact raw seventeenth spectrum

From next origin `(64,309)`, all 1,032 raw seventeenth attempts fail. Their exact
minimum-transversal histogram is

```text
3:1, 4:2, 5:17, 6:56, 7:192, 8:248,
9:1, 10:18, 11:65, 12:182, 13:162, 14:88.
```

The unique minimum-three attempt is `P2` at offset `-57`; it has five conflict
triples and three minimum cores. The reappearance of transversal number three
makes that attempt the first target for the next correction search.

Exact verification is provided by
`scripts/check_boundary_sixteenth_transition.py` and
`scripts/check_boundary_seventeenth_spectrum.cpp`.

## Evidence boundary

The corrected finite chain now reaches sixteen blocks. No corrected seventeenth
transition, recurrence, periodic state invariant, or all-length construction is
proved.
