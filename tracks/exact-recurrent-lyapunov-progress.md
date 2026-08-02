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

Zero-score reopening census:

```text
3 zero reopenings   3 signatures
2 zero reopenings   6 signatures
1 zero reopening    5 signatures
0 zero reopenings   1 signature.
```

The unique no-zero class is

```text
3012=2, 3210=10, 2031=2310=3201=1,
```

realized exactly by `(-1,4)` and `(4,-1)`. Even there, all three reopening
responses remain the minimizer face. The checker audits 10,190 integer points in
`[-50,50]^2` and rejects thirteen corruptions.

## ERL1k — pair-through-response-point component atlas

For a two-point background `{b1,b2}`, the first non-additive term is the number
of response points on the line through `b1,b2`.

```text
response-union points                         11
lines through response-union pairs            36
  lines containing 2 union points             28
  lines containing 3 union points              7
  line containing 4 union points               1
pair-through contribution classes             39
stored integer witness pairs                  48.
```

Componentwise maxima are

```text
3012:3, 3210:4, 2031:2, 2310:2, 3201:2.
```

This classifies the non-additive component exactly. It does not by itself
classify compatible complete two-point score signatures.

## ERL1l — minimal two-point original-response reversal

Singleton robustness fails sharply at background size two. Under the
`L_infinity` coordinate-radius measure, the smallest affine integer backgrounds
for which an original residual response is strictly better than every reopening
response occur at radius five.

```text
radius 4: 70 available points, 2,415 pairs, 0 strict original reversals
radius 5: 110 available points, 5,995 pairs, 2 strict original reversals.
```

The complete minimal witness set is

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}.
```

Both produce

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2,
```

so `3012` is the unique complete-score minimizer. The background-pair line is
`x+y-2=0`, containing response-union points `02` and `20`; its pair-through
contribution adds one to each reopening response. The singleton components add
one further hit to `3201`, and one further hit to each of `2031` and `2310`.

This disproves any background-independent rule that a local reopening response
always minimizes the complete score. It does not prove either witness is a
physically realizable construction state.

## ERL1m — infinite two-point original-face family

The pair-through vector

```text
(3012,3210,2031,2310,3201)=(0,0,1,1,1)
```

occurs on exactly two lines determined by response-union points:

```text
x+y=2, through 02 and 20
x+y=4, through 13 and 31.
```

Neither line is a secant of any one candidate response. After removing the
finite response-union and response-secant intersection set, each line still
contains infinitely many integer points with zero singleton increment. Any two
distinct remaining points on either line therefore produce

```text
3012=1, 3210=4, 2031=1, 2310=1, 3201=1.
```

The minimizer face is `{3012,2031,2310,3201}`. Thus the original intrinsically
bad response re-enters the complete-score minimizer face on an infinite affine
schema-completion family. This is not a physical realization theorem.

Artifacts:

```text
scripts/check_exact_recurrent_first_host_two_point_original_face_family.py
data/exact_recurrent_first_host_two_point_original_face_family.json
docs/exact-recurrent-first-host-two-point-original-face-family.md
.github/workflows/exact-recurrent-first-host-two-point-original-face-family.yml
```

The checker proves the two-line classification, validates direct triple counts
and rejects eight mutation corruptions.

## Current exact interface

```text
first host          s4-75b04c45c1c8eac2
score signature     20 line loads + 11 pair counts
safe local class    32 forbidden-cell backgrounds
singleton atlas     15 exact integer signatures
pair component      39 exact contribution classes
singleton critical  (-1,4), (4,-1)
two-point reversal  2 minimal radius-five backgrounds
critical pair lines x+y=2 and x+y=4
coarse H=2 bound    69.
```

## Active work queue

- **#18:** determine whether the two critical pair-line classes and the strict
  reversal signatures are excluded by physical provenance; otherwise retain
  them as labelled states and enumerate installed legal operations, children
  and multiplicities.
- **#19:** publish a realizable non-strict SCC or failed row whenever found.
- **#20:** classify the unique depth-two overlap under installed operations.
- **#21:** compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Acceptance test for the next row

A valid first-host compiler must provide:

1. every realizable physical occurrence over deletion trace `{02,20}`;
2. the exact 20 secant-line loads and 11 pair-through-point counts;
3. proof excluding both critical pair-line classes and strict reversal
   signatures, or explicit labelled states for them;
4. physical causes and owners of cells `02` and `20`;
5. every installed legal operation and intermediate state;
6. exact labelled child multiplicities and positive weights;
7. either a strict exact row, a strict parent-budget comparison, or a realizable
   residual witness.

No artifact may set `all_n_proved_by_checker` to one.
