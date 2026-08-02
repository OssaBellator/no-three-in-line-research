# Corrected fourteenth boundary transition

This chapter continues the exact corrected radius-64 boundary chain from the legal
104-point, thirteen-block state in `docs/645-corrected-thirteenth-boundary-transition.md`.
It records the complete fourteenth attempt census, the bounded correction search,
and the resulting raw fifteenth obstruction.

## PP3czp — Exact fourteenth minimum-transversal spectrum

For the eight node variants and all 129 offsets in `[-64,64]`, the 1,032 raw
fourteenth attempts have exact minimum-transversal histogram

```text
3:3, 4:13, 5:62, 6:123, 7:173, 8:151,
9:36, 10:61, 11:130, 12:131, 13:98, 14:51.
```

Exactly sixteen attempts have minimum transversal at most four.  Their minimum
cores total 130:

```text
P0/-29:9   P0/60:3   P0/62:54
P1/-11:3   P1/27:1   P1/55:7   P1/62:3
P2/-30:3   P2/-13:9  P2/26:9   P2/28:3  P2/63:9
P3/-13:3   P3/57:3   P3/61:3   P3/63:3.
```

The exhaustive kernel is `scripts/check_boundary_fourteenth_spectrum.cpp`.

## PP3czq — Attemptwise correction through budget seven

Every one of the sixteen low-transversal attempts has at least one row-and-column
preserving legal correction with total deletion size at most seven.

Of the 130 minimum cores, 125 admit such a correction.  The exact successful-core
minimum-budget distribution is

```text
3:2, 4:23, 5:54, 6:38, 7:8.
```

Five minimum cores do not admit a correction within the searched budget.  The
claim is therefore attemptwise, not a statement that every minimum core repairs.
The exhaustive kernel is `scripts/check_boundary_fourteenth_corrections.cpp`.

## PP3czr — Canonical three-point correction and fifteenth obstruction

The canonical transition uses `P2` at offset `63`, placed from origin `(52,313)`.
Its raw block is

```text
(52,377),(52,379),(53,376),(53,378),
(54,376),(54,378),(55,377),(55,379).
```

Delete

```text
(32,79),(44,258),(52,377)
```

and add

```text
(32,258),(44,377),(52,79).
```

The deletion and addition multisets agree in every row and column.  The corrected
state has 112 points, fourteen blocks, and no collinear triple.

Using next origin `(56,376)`, all eight node variants at all 129 offsets fail as
raw fifteenth extensions.  Their exact minimum-transversal histogram is

```text
4:10, 5:36, 6:100, 7:193, 8:186,
9:28, 10:81, 11:106, 12:151, 13:110, 14:31.
```

Thus the corrected radius-64 path reaches fourteen blocks, but no raw fifteenth
transition or periodic corrected-state invariant is yet known.

## Evidence boundary

This is an exact finite corrected transition.  It does not establish recurrence,
an unbounded corrected component, or the all-`n` theorem.
