# Exact `m=10` weighted-Hall transport for source counts `400--575`

`docs/357` reduces the complete `m=10` atomic flaw-transport audit to `47,512`
weighted maximum-closure instances.  `docs/360` and `docs/362` certify all
instances with `106--399` compatible source cycles and all instances with the
full `720`-cycle support.  This chapter completes every source count from `400`
through `575`.

The computation is partitioned into 44 resumable bands. Two independent exact
max-flow implementations were used: Dinic and gap-heuristic push--relabel. They
reproduce the same optimal ratios on overlapping regression bands. The committed
reproducibility worker uses Dinic, while the frozen ledger records the solver used
in the original computation of each completed band.

No claim is made about source counts `576--719` or asymptotic weighted
expansion.

## 1. Complete mid-source census

### Theorem PP3bsk -- VERIFIED FINITELY / ALL SOURCE COUNTS `400--575`

Exactly

```text
13,712 signed m=10 flaws
```

have between `400` and `575` compatible source cycles.  Every one of the 13,712
instances has a proper weighted Hall bottleneck.

The exact worst optimal charge over this complete range is

```text
gamma_[400,575] = 2397/349898
                = 0.00685056787978...,
10^3 gamma_[400,575] = 6.85056787978... .
```

A canonical maximizing instance has

```text
source owners:       (5,7,8),
target assignments:  (6,8,2),
orientations:        (0,0,0).
```

It has exactly `550` compatible source cycles.  Its maximizing Hall set contains
`489` source cycles and has

```text
W = 38,352,
V = 5,598,368,
W/V = 2,397/349,898.
```

#### Verification

Each worker reconstructs the complete `m=10` pair geometry, Hamilton-cycle
universe, affine clean fibres, compressed three-arc source family, and
owner-intersecting clean transport graph.  Duplicate targets are merged, target
capacities are exact clean-fibre sizes, and rational Dinkelbach iteration calls
an exact integer maximum-closure min-cut.  The 44 ledger bands form a disjoint,
contiguous partition of `400--575`. ∎

## 2. The scaled finite maximum rises

### Theorem PP3bsl -- VERIFIED FINITELY / NONMONOTONE SCALED CHARGE

The `400--575` maximum satisfies

```text
10^3 gamma_[400,575] = 6.85056787978...,
```

which is larger than both

```text
the complete m=9 maximum:       5.553858...,
the earlier audited m=10 blocks: 5.534407... .
```

Thus the finite evidence does not support monotone decrease of the scaled worst
charge from `m=9` to `m=10`.

The worst complete-source ratio in this range is

```text
2558/376281 = 0.00679811098620...,
```

strictly below the optimal charge.  The maximum local/global merging penalty is

```text
2575814/1223845 = 2.10468972786...,
```

and the exact Dinkelbach computation uses at most nine conceptual cuts.

#### Consequence

The `m^-3` scale remains possible, but any prospective uniform constant must now
exceed `6.85057` on the audited data.  Controlling only complete-source mass is
again insufficient.

## 3. Revised exact workload

### Corollary PP3bsm -- VERIFIED FINITELY / 16,884 CLOSURES CERTIFIED

Combining this chapter with the earlier exact blocks gives

```text
106--399 source cycles:  2,760 flaws,
400--575 source cycles: 13,712 flaws,
exactly 720 cycles:        412 flaws,
------------------------------------
total completed:        16,884 flaws,
remaining:              30,628 flaws.
```

Every completed instance has a proper Hall bottleneck.  The remaining source
counts are exactly `576--719`.

The completed maximizing cuts now include local, intermediate, and near-global
obstructions, and the new range contains a `489/550` maximizing cut.  The
all-scale expansion requirement is therefore strengthened rather than removed.

The exact workers are intended to be run on resumable source-count intervals:

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_weighted_hall_mid_source_dinic_worker.cpp \
  -o /tmp/check_m10_hall_dinic

OMP_NUM_THREADS=8 /tmp/check_m10_hall_dinic 400 424
OMP_NUM_THREADS=1 /tmp/check_m10_hall_dinic 550 550
```

The frozen partition ledger is checked arithmetically with

```bash
python scripts/verify_m10_weighted_hall_mid_source_ledger.py \
  experiments/m10-weighted-hall-mid-source-400-575-audit.json
```

The next implementation frontier is the exact `576--719` range.  Independent one-count workers are preferable to one monolithic OpenMP run. The
original audit used the two max-flow algorithms on complementary hard instances;
the committed Dinic worker reproduces any requested band exactly.

The next theorem identifier after this chapter is `PP3bsn`.
