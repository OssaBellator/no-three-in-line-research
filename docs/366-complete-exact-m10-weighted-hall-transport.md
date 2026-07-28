# Complete exact `m=10` weighted-Hall transport

`docs/357` reduces the `m=10` atomic flaw-transport problem to `47,512` exact
weighted maximum-closure instances.  `docs/360`, `docs/362`, and `docs/364`
complete source counts `106--575` and the full `720`-source tranche.  This
chapter completes every remaining source count `576--719` and closes the entire
finite `m=10` audit.

The result is finite.  It does not prove asymptotic weighted expansion or a
uniform `O(m^-3)` constant.

## 1. The remaining high-source ranges

### Theorem PP3bsp -- VERIFIED FINITELY / ALL SOURCE COUNTS `576--719`

Exactly

```text
16,552 flaws have 576--649 compatible source cycles,
14,076 flaws have 650--719 compatible source cycles,
----------------------------------------------------
30,628 signed flaws in total.
```

Every one of these `30,628` weighted-Hall instances has a proper bottleneck.

For source counts `576--649`, the worst exact charge is

```text
5254/791819 = 0.00663535479699...,
```

attained at source count `600`.  A canonical maximizing flaw has

```text
source owners:       (6,7,8),
target assignments:  (5,8,2),
orientations:        (1,0,0).
```

Its maximizing Hall set contains `508` of the `600` source cycles and has

```text
W = 42,032,
V = 6,334,552.
```

For source counts `650--719`, the worst exact charge is

```text
5344/970989 = 0.00550366687985...,
```

attained at source count `672`.  Its maximizing Hall set contains `477` source
cycles and has

```text
W = 42,752,
V = 7,767,912.
```

#### Verification

Each source count was run as an independent resumable worker.  The exact Dinic
and gap-heuristic push--relabel implementations were used on complementary hard
counts.  Every output reconstructs the full Hamilton-cycle geometry, affine
clean fibres, compressed source family, merged target set, exact target-fibre
capacities, and rational Dinkelbach maximum-closure optimum.  The committed
range ledgers form disjoint contiguous partitions of `576--649` and `650--719`.
∎

## 2. Complete `m=10` census

### Theorem PP3bsq -- VERIFIED FINITELY / ALL `47,512` CLOSURES COMPLETE

All `47,512` supported signed atomic flaws at `m=10` have now been solved by
exact weighted maximum-closure min-cuts.  Every instance has a proper Hall
bottleneck.

The complete partition is

```text
106--199 source cycles:     132 flaws,
200--399 source cycles:   2,628 flaws,
400--575 source cycles:  13,712 flaws,
576--649 source cycles:  16,552 flaws,
650--719 source cycles:  14,076 flaws,
exactly 720 cycles:         412 flaws,
--------------------------------------
total:                   47,512 flaws.
```

The global exact maximum is

```text
gamma_10 = 2397/349898
         = 0.00685056787978...,
10^3 gamma_10 = 6.85056787978... .
```

It is attained by the `550`-source flaw already isolated in `docs/364`, with
source owners `(5,7,8)`, target assignments `(6,8,2)`, orientations `(0,0,0)`,
and a maximizing subset of `489` sources having

```text
W = 38,352,
V = 5,598,368.
```

#### Verification

The aggregate verifier checks the six source-range ledgers, contiguous coverage
of every source count from `106` through `720`, the exact total and proper-
bottleneck count, all range maxima, and the global witness. ∎

## 3. Exact finite consequences

### Corollary PP3bsr -- VERIFIED FINITELY / GLOBAL MERGING DATA

Across the complete `m=10` audit:

```text
worst optimal Hall charge:       2397/349898,
worst complete-source ratio:     2558/376281,
maximum local/global penalty:    1500597/656230,
maximum Dinkelbach cut count:    9.
```

The maximum merging penalty occurs in the `200--399` source range, while the
maximum charge occurs at source count `550`.  Therefore neither source-universe
size nor complete-source mass alone predicts the extremal cut.

The exact scaled maximum `6.85057...` is larger than the complete `m=9` value.
The finite evidence is consistent with an `m^-3` scale only with a constant at
least this large; it does not establish such a scale.  The computational
`m=10` transport frontier is closed, while the remaining frontier is now purely
structural: prove all-scale weighted expansion or a heat-kernel substitute
uniformly in the logarithmic frustration window.

Reproduce any source-count interval with the committed worker, for example

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_weighted_hall_mid_source_dinic_worker.cpp \
  -o /tmp/check_m10_hall_dinic
OMP_NUM_THREADS=8 /tmp/check_m10_hall_dinic 600 600
```

Verify the complete partition with

```bash
python scripts/verify_m10_weighted_hall_complete_audit.py .
```

The next theorem identifier after this chapter is `PP3bss`.
