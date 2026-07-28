# Exact weighted-Hall min-cut transport through `m=8`

`docs/324` identifies the optimal merged one-step charge of an atomic signed
three-owner flaw `A` as

```text
gamma_A^*=max_(empty != U subseteq X_A) w_A(U)/v(N(U)).
```

`docs/333` evaluated this ratio by enumerating every source subset through
`m=7`.  At `m=8` one flaw may have 24 source cycles, so this chapter replaces
subset enumeration by exact weighted maximum closure and completes the full
`m=8` audit.

No asymptotic expansion or no-three-in-line theorem is claimed.

## 1. Exact ratio testing by one min-cut

Fix a flaw and write

```text
W(U)=sum_(x in U) w_A(x),
V(N(U))=sum_(y in N(U)) v(y).
```

For a nonnegative rational trial value `r=p/q`, construct a network with:

- a source arc of capacity `q w_A(x)` into every source-cycle vertex `x`;
- an arc of capacity `p v(y)` from every target-cycle vertex `y` to the sink;
- an infinite-capacity arc `x -> y` for every allowed repair transition.

### Proposition PP3bov -- PROVED / WEIGHTED CLOSURE MIN-CUT TEST

The maximum closure gain in this network is

```text
max_(U subseteq X_A) [q W(U)-p V(N(U))].
```

Consequently

```text
p/q >= gamma_A^*
```

if and only if the maximum gain is zero.

#### Proof

A finite cut cannot retain a source vertex while excluding one of its target
neighbours because of the infinite arc.  Thus its source-side nonterminal
vertices are exactly a closed set consisting of `U` and `N(U)`.  Relative to
the cut that discards every positive source weight, retaining this closure
saves `qW(U)` and pays `pV(N(U))`.  Maximizing the saving gives the displayed
formula.  A positive gain exists exactly when some ratio exceeds `p/q`. ∎

## 2. Exact Dinkelbach iteration

Start with `p/q=0`.  If the min-cut test has positive gain, let `U` be a
maximizing closure and replace

```text
p/q <- W(U)/V(N(U)),
```

reduced to lowest terms.

### Theorem PP3bow -- PROVED / FINITE EXACT RATIO ALGORITHM

The iteration terminates after finitely many min-cuts and returns exactly
`gamma_A^*`.

#### Proof

Whenever the current gain is positive,

```text
W(U)/V(N(U)) > p/q,
```

so the ratio strictly increases.  Every iterate is one of the finitely many
subset ratios.  Therefore the process terminates.  At termination every closure
has nonpositive gain, so the current ratio is an upper bound for all subset
ratios.  Since the current ratio itself arose from a subset, it is the maximum.
∎

This is an exact rational algorithm; it uses neither floating-point search nor
source-subset enumeration.

## 3. Regression against the exhaustive ledgers

### Theorem PP3box -- VERIFIED FINITELY / MIN-CUT REGRESSION

For every atomic signed-assignment flaw through `m=7`, the min-cut algorithm
reproduces the complete exhaustive results of `docs/333`:

| `m` | clean signed states | flaws | worst charge | proper bottlenecks | maximum merging penalty |
|---:|---:|---:|---:|---:|---:|
| 4 | 80 | 52 | `1/24` | 0 | `1` |
| 5 | 376 | 368 | `1/37` | 0 | `1` |
| 6 | 3,576 | 1,692 | `4/215` | 884 | `964/665` |
| 7 | 36,736 | 5,100 | `12/931` | 4,864 | `724/427` |

The maximum numbers of Dinkelbach min-cuts used by one flaw are respectively
`2,2,3,5`.

## 4. Complete `m=8` transport audit

### Theorem PP3boy -- VERIFIED FINITELY / FIRST PROPER WORST CUT

At `m=8`:

```text
clean signed states:             404,080,
atomic signed-assignment flaws:   12,048,
maximum source cycles per flaw:       24,
flaws with a proper bottleneck:    11,952.
```

The exact worst optimal charge is

```text
gamma_max=1/93,
8^3 gamma_max=512/93=5.505376...
```

The maximizing flaw has

```text
source owners:       (3,5,6),
target assignments:  (4,6,7),
orientations:        (0,0,0).
```

It has 15 source cycles, but its maximizing Hall set contains only two source
cycles.  Both have weight 32, so the cut has

```text
W=64,
V=5,952,
W/V=1/93.
```

The complete-source-set ratio for the same flaw is

```text
8/901,
```

strictly smaller than `1/93`.  Thus `m=8` is the first audited size where the
worst absolute charge is caused by a proper Hall cut rather than the global
source set.

The largest label-merging penalty over all `m=8` flaws is

```text
10338/4891=2.11368...
```

and the exact Dinkelbach process uses at most six min-cuts for any flaw.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_weighted_hall_transport_mincut.cpp \
  -o /tmp/check_weighted_hall_transport_mincut
/tmp/check_weighted_hall_transport_mincut
```

The checker precomputes the pair and three-owner geometry, reconstructs every
clean fibre, enumerates atomic signed-assignment flaws, and solves each weighted
Hall ratio by exact Dinkelbach maximum-closure min-cuts.  It reproduces every
`m<=7` exhaustive ledger and compares the `m=8` output with
`experiments/weighted-hall-transport-mincut-audit.json`. ∎

## 5. Revised weighted-expansion frontier

The finite data change the emphasis of the transport problem.

1. The exact optimization itself is now polynomial in the source-target graph;
   exponential subset enumeration is removed.
2. Proper Hall bottlenecks occur for `11,952/12,048` flaws at `m=8`.
3. The worst absolute charge is already a two-source local cut.
4. The finite cubic-scale constant rises from `4.42105` at `m=7` to `5.50538`
   at `m=8`.
5. The maximum local/global penalty rises above two.

Therefore controlling only the global clean-measure mass of a flaw is
insufficient.  The asymptotic theorem must control small and intermediate
weighted neighbourhood cuts, or show that a short heat-kernel trajectory
expands them before charge is measured.

The min-cut checker makes `m=9` conceptually accessible, but the dominant cost
there is construction of the `6,727,728` clean signed states and all atomic
flaw-transition graphs, not Hall optimization itself.

The next theorem identifier after this chapter is `PP3boz`.