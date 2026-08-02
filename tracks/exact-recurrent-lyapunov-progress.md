# Exact recurrent Lyapunov progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

The no-three-in-line conjecture remains open. Every result below is a finite
local theorem, an exact projection, or an explicit obstruction to the current
certificate data. All global proof flags remain zero.

## ERL1 finite side-four kernel — PROVED

```text
feasible hosts                 86
response incidences           206
hosts with a zero response     75
residual hosts                 11
minimal blockers                3
maximum reopening depth         2
```

The minimal blockers are `{02,20}`, `{02,31}`, `{13,31}`. The unique depth-two
state is `{02,13,20,31}`.

## ERL1a raw lineage projection — PROVED

All eleven residual states join bijectively to stable upstream raw-fibre host
IDs and all three blocker IDs. The raw lineage layer leaves 32 physical
deletion-cause assignments, 11 backgrounds, 11 legal-operation families and 11
child rows unpopulated.

## ERL1b selected-response provenance — PROVED

The upstream selector manifest supplies normalized owner scope, fate, collision
key, line class, interface and CRT scope. Every residual minimizer face is a
singleton:

```text
3012: 9 hosts, minimum energy 1, next gap 3
3210: 2 hosts, minimum energy 4, no higher response
```

These are normalized classes, not physical provenance.

## ERL1c selected-line geometry — PROVED

```text
3012 -> x-y-1=0, primitive key (1,-1,-1), k=3, 9 hosts
3210 -> x+y-3=0, primitive key (1,1,-3),  k=4, 2 hosts
```

Every selected residual response is single-line supported. The total selected
triple incidence count is 17.

## ERL1d complete line-kernel non-identifiability — PROVED

For the installed kernel

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3),
```

the populated records determine `k` but omit background load `h`:

```text
3012 class: K(0,3)=1, K(1,3)=4
3210 class: K(0,4)=4, K(1,4)=10
```

Thus no current residual record determines even its selected-line contribution
to the exact coupled kernel. This is a certificate-data obstruction, not a
counterexample to the conjecture.

## ERL1e first-host selector background witness — PROVED

For `s4-75b04c45c1c8eac2`, empty-background scores are `(1,4)`, giving unique
selector `3012` and gap `3`. Adding affine schema-completion point `(4,3)` on
`x-y-1=0` and off `x+y-3=0` changes the scores to `(4,4)`. The minimizer face
changes from `{3012}` to `{3012,3210}`.

This proves that the populated first-host record does not determine a unique
complete-score selector. Global realizability of the completion is not claimed.

## ERL1f first-host occupancy moments — PROVED

For response family `{3012,3210}`, exact enumeration gives

```text
nonaxis lines   54
active lines    35
capacity census {1:31, 2:2, 3:1, 4:1}
M1              42
M2              11
M3               5
E2              69
```

The value `69` is an exact deterministic upper certificate for triple-free
backgrounds. It is not an exact row and is not strict without a parent budget.

## ERL1g reopening singleton fragility — PROVED

The local reopenings expose intrinsically zero responses

```text
restore 02 -> 2031 or 2310
restore 20 -> 3201.
```

The affine common-secant points of all three reopening responses are

```text
(-1,4), (2/3,7/3), (3/2,3/2), (7/3,2/3), (4,-1).
```

The only integer points are `(-1,4)` and `(4,-1)`. Either witness raises all
three reopening scores from zero to one. There is no common integer witness
inside the original `4x4` square. Global realization is not claimed.

## ERL1h lossless first-host background signature — PROVED

For the five-response menu

```text
3012, 3210, 2031, 2310, 3201,
```

the exact complete new-triple score vector is determined by

```text
20 response-secant line loads
11 background-pair-through-response-point counts
31 integer coordinates total.
```

For every finite background `B` disjoint from response `Q`,

```text
score(Q;B)
 = intrinsic(Q)
 + sum_l C(k_Q(l),2) h_B(l)
 + sum_{q in Q} pair_B(q).
```

The exact `5 x 31` coefficient matrix has rational row rank five; the four
selector-difference rows have rank four. Direct enumeration agrees on 2,626
backgrounds and 13,130 response/background comparisons.

## ERL1i canonical forbidden-background invariance — PROVED CONDITIONALLY

Let

```text
F={00,01,11,22,33}.
```

For every one of the 32 subsets `B` of `F`, all five candidate scores receive
the common offset

```text
c(B)=1[{00,01} subset B]+1[{01,11} subset B].
```

Hence

```text
2031=2310=3201=c(B)
3012=c(B)+1
3210=c(B)+4.
```

The selector order is preserved, with minimizer face
`{2031,2310,3201}`. This is a complete safe local class, not a physical coverage
theorem.

## ERL1j full integer singleton signature atlas — PROVED

For one integer background point disjoint from the union of all five candidate
responses, the pair-through-point part of the 31-coordinate signature vanishes.
The point is either off all 20 secants, on exactly one secant, or at an
intersection of at least two secants.

Exact arrangement census:

```text
distinct response secants                         20
distinct rational secant intersections           103
integer intersections including response points   27
excluded response-union points                    11
admissible integer intersections                  16
distinct integer singleton score signatures       15
```

The complete score classification is:

```text
minimum score 0                 14 signatures
minimum score 1                  1 signature
original response is minimizer   0 signatures
```

The zero-score reopening census is:

```text
3 zero reopenings   3 signatures
2 zero reopenings   6 signatures
1 zero reopening    5 signatures
0 zero reopenings   1 signature
```

The unique class with no zero reopening is

```text
3012=2, 3210=10, 2031=2310=3201=1,
```

realized exactly by the two integer points `(-1,4)` and `(4,-1)`. Even there,
the three reopening responses remain the minimizer face. Thus no integer
singleton background makes either original residual response optimal.

The implementation reconstructs all line and intersection classes, supplies a
generic integer witness for every secant, checks direct scores on 10,190 lattice
points in `[-50,50]^2`, and rejects thirteen corruptions. Physical singleton
coverage and every multi-point background claim remain zero.

## ERL1k pair-through-response-point atlas — PROVED

For a two-point background `{b1,b2}`, the full score has one non-additive term:
the number of response points lying on the line through `b1,b2`.

The five-response union has 11 points. Lines through pairs of union points have
the exact census

```text
36 distinct lines
28 lines containing 2 union points
 7 lines containing 3 union points
 1 line containing 4 union points.
```

A background-pair line either avoids the union, meets exactly one union point,
or is one of those 36 lines. After equal vectors are identified, there are
exactly 39 pair-through-response-point contribution classes. The compiler stores
48 integer witness pairs and rejects twelve corruptions.

The maximum component contributions are

```text
3012: 3
3210: 4
2031: 2
2310: 2
3201: 2.
```

This completes the non-additive pair component only. The full two-point score
still requires compatibility between two singleton secant signatures and one
pair-through-point class.

## First host: exact known interface

```text
upstream ID       s4-75b04c45c1c8eac2
deletions         {02,20}
selected response 3012
selected line     x-y-1=0
selected triple   {(1,0),(2,1),(3,2)}
restore 02        exposes 2031 and 2310
restore 20        exposes 3201
coarse H=2 bound  69
score signature   20 line loads + 11 pair counts
safe local class  all 32 subsets of {00,01,11,22,33}
singleton atlas   15 exact integer score classes
pair-line atlas   39 exact contribution classes
critical points   (-1,4), (4,-1)
```

## Active work queue

- **#18:** classify compatibility of the two singleton secant signatures with
  the 39 pair-through-point classes; then prove physical coverage or populate
  exterior signatures, deletion causes, owners and legal transitions.
- **#19:** publish a realizable non-strict SCC or failed row whenever found.
- **#20:** classify the unique depth-two overlap under installed operations.
- **#21:** compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Acceptance test for the next row

A valid first-host compiler must provide:

1. every realizable physical occurrence over deletion trace `{02,20}`;
2. the exact 20 secant-line loads and 11 pair-through-point counts;
3. a proof of safe-class membership or an explicit exterior signature;
4. physical causes and owners of cells `02` and `20`;
5. the complete score vector obtained from the committed integer matrix;
6. every installed legal operation and intermediate state;
7. exact labelled child multiplicities and positive weights;
8. either a strict exact row, a parent budget making an applicable upper bound
   strict, or an explicit realizable residual witness.

No artifact may set `all_n_proved_by_checker` to one.
