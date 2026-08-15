# First-host restoration-menu closure

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact on the chart-safe background class. The result classifies response menus and scores; it does not prove that any restoration is a legal physical operation.

## Response menus

For the first residual host with deletions `{02,20}`, exact perfect-matching enumeration gives

```text
blocked:
  3012,3210

restore 02:
  2031,2310,3012,3210

restore 20:
  3012,3201,3210

restore both:
  2031,2301,2310,3012,3201,3210
```

Thus restoring both deletions exposes one response not present in the previous five-response score interface:

```text
2301 = {02,13,20,31}.
```

## Single-edge restoration congruence

For every one of the 32 chart-safe backgrounds `B subseteq {00,01,11,22,33}`:

```text
restore 02 minimizer face = {2031,2310}
restore 20 minimizer face = {3201}
```

Hence selector choice is congruent across the safe class for either individual restoration. This is a score statement only; physical legality and transition provenance remain unpopulated.

## Exact operation-aware signature

Define four Boolean coordinates

```text
a = 1[{00,01} subset B]
b = 1[{01,11} subset B]
u = 1[11 in B]
v = 1[22 in B].
```

The previous five-response signature retained only the ordered pair `(a,b)`. Restoring both deletions exposes line loads detecting `u` and `v`.

Across the 32 safe backgrounds, exactly ten quadruples `(a,b,u,v)` occur, with class sizes

```text
(0,0,0,0): 6
(0,0,0,1): 6
(0,0,1,0): 4
(0,0,1,1): 4
(0,1,1,0): 2
(0,1,1,1): 2
(1,0,0,0): 2
(1,0,0,1): 2
(1,1,1,0): 2
(1,1,1,1): 2.
```

Point `33` remains invisible and doubles every realizable class in which the other four cells are fixed.

## New response score

The exact complete score of `2301` is

```text
score(2301;B)=a+b+u+v.
```

Equivalently,

```text
score(2301;B)
 = 1[11 in B]
 + 1[22 in B]
 + 1[{00,01} subset B]
 + 1[{01,11} subset B].
```

The first two terms come from response secants not present in the earlier five-response signature. The latter two are the existing target-pair-through-response terms.

## Three new secant coordinates

The six secants of `2301` contain exactly three lines absent from the twenty-line five-response union:

```text
x+y-4=0
x+y-2=0
3x+y-6=0.
```

On the safe class, `22` lies on `x+y=4` and `11` lies on `x+y=2`. No safe point lies on `3x+y=6`, but that coordinate remains part of the full expanded response geometry.

## Eight score classes, ten exact signatures

Using response order

```text
3012,3210,2031,2310,3201,2301,
```

the 32 safe backgrounds split into eight score classes:

```text
(1,4,0,0,0,0):  6
(1,4,0,0,0,1): 10
(1,4,0,0,0,2):  4
(2,5,1,1,1,1):  2
(2,5,1,1,1,2):  4
(2,5,1,1,1,3):  2
(3,6,2,2,2,3):  2
(3,6,2,2,2,4):  2.
```

The eight-score quotient is still non-injective on the ten exact operation signatures. There are exactly two collisions:

```text
score (1,4,0,0,0,1):
  (a,b,u,v)=(0,0,0,1)
  (a,b,u,v)=(0,0,1,0)

score (2,5,1,1,1,2):
  (a,b,u,v)=(0,1,1,0)
  (a,b,u,v)=(1,0,0,1).
```

Thus even equality of all six current response scores does not identify the operation-aware geometric state.

## Consequence for alternating-core import

A recurrence quotient must be closed under every installed operation menu. The four-class five-response signature fails this test if simultaneous restoration is admitted, and the resulting eight-score quotient still loses the distinction between the two new line-load coordinates.

The minimum known operation-aware alphabet on the safe class therefore has ten states, represented by `(a,b,u,v)`. This alphabet is exact for the enumerated response geometry only. Owner identity, legal operations, intermediate states, child multiplicities, positive weights, parent budget, continuation edges and capacities still require physical data and may force further refinement.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_restoration_menu_closure.py \
  --check data/exact_recurrent_first_host_restoration_menu_closure.json
```

The checker enumerates all four response menus and all 32 safe backgrounds, verifies the exact `2301` formula, the ten-signature and eight-score censuses, both score collisions, and rejects thirteen deliberate corruptions.

Physical chart confinement, legal restoration, occurrence coverage, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
