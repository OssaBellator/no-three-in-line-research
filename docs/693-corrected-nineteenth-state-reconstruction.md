# Corrected nineteenth state reconstruction

This chapter repairs a hard-coded state discrepancy discovered while opening the
budget-seven frontier. It supersedes the nineteenth-spectrum and low-frontier
counts in `docs/675`, `docs/681`, and `docs/687`. Their Hall, threshold, prefix,
shell, and integration results are unaffected.

## PP3del — Exact eighteenth-state reconstruction

Reconstruct the corrected eighteen-block state from the validated 136-point
seventeenth state, the `P0/-39` eighteenth block, and the documented six-point
correction in `docs/675`.

The resulting 144-point state contains

```text
(42,378)
```

and does not contain

```text
(42,193).
```

The latter point was present in the old hard-coded nineteenth spectrum source.
It creates the exact collinear triple

```text
(36,163), (42,193), (54,253).
```

The reconstructed state has 144 distinct points and no collinear triple. The
state discrepancy is exactly the one-point exchange

```text
legacy only:    (42,193),
canonical only: (42,378).
```

## PP3dem — Corrected raw nineteenth spectrum

For the reconstructed state, next origin `(72,213)`, the four `P` nodes, the four
`Q` nodes, and offsets `-64` through `64`, the exact 1,032-attempt histogram is

```text
4:2, 5:9, 6:47, 7:175, 8:283, 9:3,
10:16, 11:63, 12:121, 13:176, 14:137.
```

The two minimum-four attempts are

```text
P1/-33: ten conflict triples and one minimum core,
P2/-64: nine conflict triples and five minimum cores.
```

The new `P1/-33` core is

```text
(70,214), (74,180), (74,183), (75,181).
```

The five `P2/-64` cores remain the five cores listed in `docs/681`.

The corrected minimum-five layer has 9 attempts and 54 cores, with per-attempt
core-count histogram

```text
3:3, 5:2, 6:1, 9:2, 11:1.
```

The corrected minimum-six layer has 47 attempts and 435 cores, with histogram

```text
1:6, 3:15, 5:1, 9:15, 11:1, 15:3,
21:2, 27:1, 33:1, 39:1, 47:1.
```

Thus the complete transversal-at-most-six frontier contains

```text
2 + 9 + 47 = 58 attempts,
6 + 54 + 435 = 495 minimum cores.
```

## PP3den — Corrected budget-six obstruction

Every corrected minimum-four core was checked at deletion budgets four, five,
and six. Each of the six cores rejects exactly

```text
budget four:          24,
budget five:      17,520,
budget six:    7,595,640
```

row-and-column-preserving replacements. The aggregate minimum-four counts are

```text
budget four:          144,
budget five:      105,120,
budget six:    45,573,840.
```

For the 54 minimum-five cores, the exact rejected counts are

```text
budget five:        3,810,
budget six:     3,318,750.
```

For the 435 minimum-six cores, the complete budget-six layer contains

```text
143,640
```

rejected replacements. No repair exists. Across all relevant budgets and all 495
cores, the corrected audit rejects

```text
49,145,304
```

preserving replacements.

The finite chain therefore remains at eighteen blocks. A corrected nineteenth
transition still requires budget at least seven, a raw attempt of minimum at
least seven, or a changed repertoire/state representation. No twentieth spectrum
or all-length recurrence is claimed.

The authoritative checker is
`scripts/check_boundary_corrected_nineteenth_frontier.py`.

## Evidence boundary

This is an exact finite reconstruction, spectrum census, and budget-six
obstruction. It corrects the boundary data used by the preceding tranches but
does not change their candidate ledger: boundary remains `4/5`, no evidence row
is promoted, geometric closure is false, and the all-`n` theorem remains open.
