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
selector `3012` and gap `3`. Adding the affine schema-completion point `(4,3)` on
`x-y-1=0` and off `x+y-3=0` changes the scores to `(4,4)`. The minimizer face
changes from `{3012}` to `{3012,3210}`.

This proves that the populated first-host record does not determine a unique
complete-score selector. Global realizability of the completion is not claimed.

## ERL1f first-host occupancy moments — PROVED

For the response family `{3012,3210}`, exact enumeration of all nonaxis lines in
the standard `4x4` grid gives

```text
nonaxis lines   54
active lines    35
capacity census {1:31, 2:2, 3:1, 4:1}
M1              42
M2              11
M3               5
```

For a triple-free background, every relevant line has load at most `H=2`, so the
installed moment inequality gives

```text
E2=M1+2*M2+M3=69.
```

This is an exact deterministic upper certificate for the stated background
class. It is not an exact row and cannot prove strictness until a destroyed-load
or parent-budget value greater than the applicable row is supplied.

## First host: exact known interface

```text
upstream ID       s4-75b04c45c1c8eac2
deletions         {02,20}
selected response 3012
selected line     x-y-1=0
selected triple   {(1,0),(2,1),(3,2)}
restore 02        exposes zero responses 2031 and 2310
restore 20        exposes zero response 3201
coarse H=2 bound  69
```

## Active work queue

- **#18:** populate physical backgrounds, causes, owners and legal transitions
  for `s4-75b04c45c1c8eac2`.
- **#19:** publish a realizable non-strict SCC or failed row whenever found.
- **#20:** classify the unique depth-two overlap under installed operations.
- **#21:** compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Acceptance test for the next row

A valid first-host compiler must provide:

1. every realizable background over deletion trace `{02,20}`;
2. physical causes and owners of cells `02` and `20`;
3. background loads and retained incidences on every response-relevant line;
4. the complete coupled response scores and selector face;
5. every installed legal operation and intermediate state;
6. exact labelled child multiplicities and weights;
7. either a strict exact row, a parent budget making the `69` bound strict, or an
   explicit realizable residual witness.

No artifact may set `all_n_proved_by_checker` to one.
