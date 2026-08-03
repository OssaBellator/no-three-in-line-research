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

## New response score

The exact complete score of `2301` on the safe class is

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

On the safe class, `22` lies on `x+y=4` and `11` lies on `x+y=2`. Neither point was visible through a response-secant load in the previous five-response interface.

## Exact expanded score census

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

The earlier current-menu classification had four exact 31-coordinate signatures. Those four states are therefore not closed under the expanded response menu.

## Consequence for alternating-core import

A recurrence quotient must be closed under every installed operation menu. The four-class current geometric signature fails this test if simultaneous restoration is admitted: backgrounds identified by the old signature can have different `2301` scores.

The minimum operation-aware refinement must retain at least the new line loads detecting `11` and `22`, in addition to the two existing target-pair indicators. Even that refinement is only score-complete; owner identity, legal operations, intermediate states, child multiplicities, positive weights, parent budget, continuation edges and capacities still require physical data.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_restoration_menu_closure.py \
  --check data/exact_recurrent_first_host_restoration_menu_closure.json
```

The checker enumerates all four response menus and all 32 safe backgrounds, verifies the exact `2301` formula and eight-class census, and rejects eleven deliberate corruptions.

Physical chart confinement, legal restoration, occurrence coverage, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
