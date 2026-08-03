# First-host two-restoration closure signature

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact on the chart-safe background class. It does not prove that a physical two-restoration operation is installed or legal.

## Why the five-response quotient is not closed

The first-host complete-score audit used five responses:

```text
3012,3210,2031,2310,3201.
```

The full off-diagonal response host with target `01` kept response-ineligible also admits

```text
2301 = {02,13,20,31}.
```

This response uses both first-host deletion edges `02` and `20`, so it first appears after a two-edge restoration from the `{02,20}` host. It is intrinsically triple-free.

Therefore any proposed transition quotient that may restore both deletion edges must also control the complete score of `2301`.

## Expanded lossless signature

The original five-response signature used

```text
20 response-secant line loads
11 pair-through-response-point counts
31 coordinates total.
```

Adding `2301` introduces exactly three new secant lines:

```text
x+y=4       coefficient (1,1,-4)
x+y=2       coefficient (1,1,-2)
3x+y=6      coefficient (3,1,-6).
```

The point-coordinate union remains eleven cells. The closure signature therefore has

```text
23 line-load coordinates
11 pair-through coordinates
34 coordinates total.
```

The exact six-response coefficient matrix has rank six, and its selector-difference matrix has rank five.

## Exact Boolean formula on the safe class

For a safe background `B subset {00,01,11,22,33}`, define

```text
a = 1[{00,01} subset B]
b = 1[{01,11} subset B]
u = 1[11 in B]
v = 1[22 in B].
```

Put `c=a+b`. The first five scores remain

```text
(3012,3210,2031,2310,3201)
  = (1+c,4+c,c,c,c).
```

The new response has the exact score

```text
score(2301;B)=a+b+u+v.
```

Thus `11` and `22`, which were invisible or partly invisible to the five-response quotient, become line-load data for `2301` through `x+y=2` and `x+y=4`.

Cell `33` remains invisible to all six scores and all 34 signature coordinates.

## Exact census

Across all 32 safe backgrounds:

```text
realized four-bit states             10
exact 34-coordinate signatures       10
complete six-response score vectors   8
maximum signatures per score vector   2
```

The ten exact signature classes have background-count census

```text
6,6,4,4,2,2,2,2,2,2.
```

Two independent score collisions remain:

- background `11` and background `22` both give six-response scores `(1,4,0,0,0,1)` but activate different line coordinates;
- other equal-score pairs similarly retain different ordered geometric data.

Therefore even complete six-response score equality is not a lossless recurrence quotient.

## Transition consequence

```text
five-response four-signature quotient transition-closed   no
adding 2301 changes the exact safe signature alphabet      yes
exact closure candidate states                             10
```

A transition-aware first-host quotient must retain at least the exact four Boolean coordinates `(a,b,u,v)` on the safe class, subject to their ten realized combinations, or prove a stronger operation congruence that honestly identifies some of them.

This result does not establish that restoring both deletion edges is a physical legal operation. It proves only that any operation family which can expose `2301` cannot use the earlier four-state quotient without additional data.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_two_restoration_closure_signature.py \
  --check data/exact_recurrent_first_host_two_restoration_closure_signature.json
```

The checker recomputes all 32 backgrounds, the 23-line/11-point coordinate system, matrix ranks and ten-class census, and rejects eleven deliberate corruptions.

Physical chart confinement, physical two-restoration legality, occurrence coverage, child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
