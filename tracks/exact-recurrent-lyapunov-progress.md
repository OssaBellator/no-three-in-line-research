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
child rows unpopulated. Its six normalized provenance coordinates are absent at
this layer only.

## ERL1b selected-response provenance — PROVED

The separate upstream selector manifest fills normalized owner scope, fate,
collision key, line class, interface and CRT scope. Every residual minimizer
face is a singleton:

```text
3012: 9 hosts, minimum energy 1, next gap 3
3210: 2 hosts, minimum energy 4, no higher response
```

These are normalized classes, not physical owner/background provenance.

## ERL1c selected-line geometry — PROVED

Every residual selected response is supported on one affine line:

```text
3012 -> x-y-1=0, primitive key (1,-1,-1), k=3, 9 hosts
3210 -> x+y-3=0, primitive key (1,1,-3),  k=4, 2 hosts
```

The eleven hosts contain 17 selected triple incidences in total.

## ERL1d complete line-kernel non-identifiability — PROVED

The installed complete line kernel is

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3).
```

The current populated records determine response occupancy `k` but omit
background line load `h`. Exact schema completions give

```text
3012 class: K(0,3)=1, K(1,3)=4
3210 class: K(0,4)=4, K(1,4)=10
```

Therefore none of the eleven current host/selector/selected-line records
determines even its selected-line contribution to the complete coupled kernel.
This is a data/certificate obstruction, not a globally realized geometric
counterexample.

## ERL1e first-host selector background witness — PROVED

For the first residual host

```text
upstream ID  s4-75b04c45c1c8eac2
deletions    {02,20}
responses    3012, 3210
```

the empty-background scores are `(1,4)`, so `3012` is the unique minimizer with
gap `3`. Add the exact affine background point `(4,3)`:

- it lies on the selected line `x-y-1=0`;
- it lies off the competitor line `x+y-3=0`;
- the complete scores become `(4,4)`.

Thus one completion of the omitted background field consumes the intrinsic gap
exactly and changes the minimizer face from `{3012}` to `{3012,3210}`. The
canonical intrinsic selector is not determined as a unique complete-score
selector by the populated record alone. Global realizability of this completion
is not claimed.

## First host: exact known interface

```text
selected response  3012
selected line      x-y-1=0
selected triple    {(1,0),(2,1),(3,2)}
restore 02         exposes zero responses 2031 and 2310
restore 20         exposes zero response 3201
```

The unresolved question is now exact: determine every physically realizable
background and deletion-cause fibre, then decide whether the selected line can
be legally destroyed or either blocked cell can be legally reopened while
accounting for all compulsory children.

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
7. either a strict exact row or an explicit realizable residual witness.

No artifact may set `all_n_proved_by_checker` to one.
