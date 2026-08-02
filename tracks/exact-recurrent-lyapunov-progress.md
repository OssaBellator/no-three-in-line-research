# Exact recurrent Lyapunov progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

The classical no-three-in-line conjecture remains open. Every result below is a
finite local theorem, an exact projection, or an explicit obstruction to the
current certificate architecture. All physical-coverage, legal-operation,
recurrent-row, Lyapunov, termination and all-`n` flags remain zero.

## ERL1 — exact side-four residual kernel

```text
feasible hosts                 86
response incidences           206
hosts with a zero response     75
residual hosts                 11
minimal blockers                3
maximum reopening depth         2
```

The minimal blockers are `{02,20}`, `{02,31}`, `{13,31}`. The unique local
depth-two state is `{02,13,20,31}`.

## ERL1a–c — lineage, selected provenance and line geometry

All eleven residual states join bijectively to stable upstream raw-fibre host
IDs and blocker IDs. The selected-response manifest supplies normalized owner
scope, fate, collision key, line class, interface and CRT scope, but not physical
background or owner ancestry.

```text
3012: 9 hosts, intrinsic energy 1, next gap 3, line x-y-1=0
3210: 2 hosts, intrinsic energy 4, no higher face, line x+y-3=0
```

Every residual selected response is supported on one affine line. The total
selected intrinsic triple incidence count is 17.

## ERL1d — complete line-kernel non-identifiability

For the installed complete line kernel

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3),
```

the populated host records determine response occupancy `k` but omit background
load `h`:

```text
3012 class: K(0,3)=1, K(1,3)=4
3210 class: K(0,4)=4, K(1,4)=10.
```

Therefore no current residual record determines even its selected-line
contribution to the complete coupled row.

## ERL1e–f — first-host selector witness and coarse moment certificate

The first active host is

```text
upstream ID       s4-75b04c45c1c8eac2
deletions         {02,20}
selected response 3012
restore 02        exposes 2031 and 2310
restore 20        exposes 3201.
```

Adding affine schema-completion point `(4,3)` changes original-response scores
from `(3012,3210)=(1,4)` to `(4,4)`, consuming the intrinsic selector gap.

For response family `{3012,3210}`, exact occupancy moments are

```text
M1=42, M2=11, M3=5, E2=M1+2*M2+M3=69.
```

The value 69 is an exact upper certificate for triple-free backgrounds, not a
strict row without a parent budget.

## ERL1g — reopening singleton fragility

The three intrinsically zero reopening responses have five common affine secant
points:

```text
(-1,4), (2/3,7/3), (3/2,3/2), (7/3,2/3), (4,-1).
```

Only `(-1,4)` and `(4,-1)` are integral. Either singleton raises all three
reopening scores from zero to one. Global physical realization is not claimed.

## ERL1h — lossless 31-coordinate background signature

For response menu

```text
3012, 3210, 2031, 2310, 3201,
```

the complete score vector is determined by

```text
20 response-secant line loads
11 background-pair-through-response-point counts.
```

For every finite background `B` disjoint from response `Q`,

```text
score(Q;B)
 = intrinsic(Q)
 + sum_l C(k_Q(l),2) h_B(l)
 + sum_{q in Q} pair_B(q).
```

The exact `5 x 31` coefficient matrix has rational row rank five; its four
selector-difference rows have rank four. Direct enumeration agrees on 2,626
backgrounds and 13,130 response/background comparisons.

## ERL1i — canonical forbidden-background safe class

For every subset `B` of

```text
F={00,01,11,22,33},
```

all five scores receive the common offset

```text
c(B)=1[{00,01} subset B]+1[{01,11} subset B].
```

Hence

```text
2031=2310=3201=c(B)
3012=c(B)+1
3210=c(B)+4.
```

All 32 subsets preserve minimizer face `{2031,2310,3201}`. This is a complete
safe local class, not a theorem that every physical occurrence lies in it.

## ERL1j — complete integer singleton atlas

The full integer lattice has exactly 15 one-point score signatures:

```text
20 response secants
103 rational secant intersections
27 integer intersections including response points
16 admissible integer intersections
15 distinct integer singleton score signatures.
```

```text
minimum score 0                 14 signatures
minimum score 1                  1 signature
original response is minimizer   0 signatures.
```

The unique no-zero class is realized exactly by `(-1,4)` and `(4,-1)` and has

```text
3012=2, 3210=10, 2031=2310=3201=1.
```

Even there, all three reopening responses remain the minimizer face.

## ERL1k — pair-through-response-point component atlas

For a two-point background `{b1,b2}`, the first non-additive term is the number
of response points on the line through `b1,b2`.

```text
response-union points                         11
lines through response-union pairs            36
pair-through contribution classes             39
stored integer witness pairs                  48.
```

Componentwise maxima are

```text
3012:3, 3210:4, 2031:2, 2310:2, 3201:2.
```

## ERL1l–m — minimal reversals and infinite tie families

The smallest strict original-response reversals occur at radius five. The two
critical pair lines are

```text
x+y=2, through 02 and 20
x+y=4, through 13 and 31.
```

Generic integer pairs on either line produce

```text
3012=1, 3210=4, 2031=1, 2310=1, 3201=1,
```

so `3012` re-enters the minimizer face on infinite affine families.

## ERL1n — global integer two-point strict-reversal classification

The full integer-lattice strict-reversal problem reduces to

```text
15 singleton vectors
39 pair vectors
43 abstract triples making 3012 uniquely minimal
 0 abstract triples making 3210 uniquely minimal.
```

Exact incidence compatibility audits

```text
14 fixed response-union lines
26 exceptional pairs on those lines
24 candidate pairs through exactly one response-union point
0 generic strict families.
```

Exactly four strict backgrounds survive globally:

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}
{(-2,6),(4,0)}
{(-2,6),(6,-2)}.
```

Every one gives

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2.
```

There are no other strict original-response reversals anywhere in the integer
lattice at background size two. The full two-point score atlas remains open
because non-strict tie classes are still infinite.

## ERL1o — side-four projection non-identifiability

The current deterministic first-host projection stores

```text
host ID, deletion edges, intrinsic response energies, dispatch and blocker IDs.
```

It stores no coordinate-labelled background, deletion causes or physical owner
labels. Consequently the same projected row admits at least two different
complete lineage candidates:

```text
empty background
  score vector (1,4,0,0,0)
  minimizer face {2031,2310,3201}

background {(-3,5),(5,-3)}
  score vector (1,4,2,2,2)
  minimizer face {3012}.
```

The complete background-sensitive lineage identifiers differ, but the stored
side-four projection is identical. Therefore no proof using only the current
host/response manifest can physically exclude the strict signatures.

## Current exact interface

```text
first host             s4-75b04c45c1c8eac2
score signature        20 line loads + 11 pair counts
safe local class       32 forbidden-cell backgrounds
singleton atlas        15 exact integer signatures
pair component         39 exact contribution classes
strict two-point set   exactly 4 backgrounds globally
strict 3210 set        empty
projection status      non-injective for complete scores
coarse H=2 bound       69.
```

## Active work queue

- **#18:** populate complete coordinate-labelled physical first-host fibres,
  then exclude, reroute, pay or retain the four strict signatures and infinite
  tie classes.
- **#19:** publish a realizable non-strict SCC or failed row whenever found.
- **#20:** classify the unique depth-two overlap under installed operations.
- **#21:** compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Acceptance test for the next row

A valid first-host compiler must provide:

1. every realizable physical occurrence over deletion trace `{02,20}`;
2. exact coordinate-labelled backgrounds and the 31 signature coordinates;
3. physical causes and owners of cells `02` and `20`;
4. proof excluding the four strict backgrounds and tie classes, or explicit
   labelled states for them;
5. every installed legal operation and intermediate state;
6. exact labelled child multiplicities and positive weights;
7. either a strict exact row, a strict parent-budget comparison, or a realizable
   residual witness.

No artifact may set `all_n_proved_by_checker` to one.
