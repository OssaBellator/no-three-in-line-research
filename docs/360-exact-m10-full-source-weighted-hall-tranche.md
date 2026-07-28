# Exact weighted-Hall audit of the full-source `m=10` flaw tranche

`docs/357` reduces the complete `m=10` flaw-transport problem to 47,512 bounded
weighted maximum-closure instances.  Exactly 412 signed flaws attain the full
factorial support of `6!=720` compatible source cycles.  This chapter completes
the exact Hall audit of that entire extremal-support tranche.

No claim is made about the remaining 47,100 supported flaws or about asymptotic
weighted expansion.

## 1. Full factorial-support tranche

For each complement-reduced flaw candidate, the checker reconstructs its
compatible parity-clean source cycles and exact source weights.  It retains the
candidate precisely when all 720 Hamilton cycles containing the three
prescribed arcs remain compatible.  Global sign complementation supplies the
second signed flaw with the same transport instance.

### Theorem PP3brz -- VERIFIED FINITELY / COMPLETE 720-SOURCE HALL CENSUS

There are exactly

```text
412 signed m=10 flaws with 720 compatible source cycles.
```

Every one of the 412 instances has a proper weighted Hall bottleneck: the
optimizing source set is strictly smaller than the complete 720-cycle source
family.

The worst exact optimal charge in this tranche is

```text
gamma_720 = 3897/719620
          = 0.00541535810566...,
10^3 gamma_720 = 5.41535810566... .
```

One maximizing flaw has

```text
source owners:       (3,7,8),
target assignments:  (7,5,3),
orientations:        (1,1,0).
```

Its maximizing Hall set contains 686 of the 720 source cycles and has

```text
W = 62,352,
V = 11,513,920,
W/V = 3897/719620.
```

#### Verification

For every full-source complement representative, the checker generates all
owner-intersecting clean successor rotations, merges duplicate target cycles,
uses the exact target-fibre capacities, and runs rational Dinkelbach iteration
with a weighted maximum-closure min-cut.  The source census, tranche size,
proper-bottleneck count, maximizing ratio, witness cut, and maximum number of
conceptual cuts are all compared with hard-coded values. ∎

## 2. Global ratio and merging penalty

### Corollary PP3bsa -- VERIFIED FINITELY / INTERMEDIATE-CUT PENALTY

Within the 720-source tranche, the worst complete-source-set ratio is

```text
3977/736987 = 0.00539629599979...,
```

strictly below the optimal charge `3897/719620`.  The maximum ratio between an
optimal Hall charge and its own complete-source ratio is

```text
12273992/8520585 = 1.44051048138... .
```

The exact Dinkelbach computation uses at most eight conceptual cuts, including
the analytically known zero-ratio initial closure.

Consequently, even the flaws with maximum factorial source support are not
controlled exactly by global mass.  Their obstruction is an intermediate cut,
but the merging penalty in this tranche is substantially below the worst
`m=9` penalty `226808/108915 = 2.08240...`.

The scaled tranche maximum `5.41536...` is also below the complete `m=9` maximum
`5.55386...`.  This is evidence, not a proof, that the `m^{-3}` scale remains
plausible at `m=10`.

Compile and run the exact tranche audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_full_source_weighted_hall_tranche.cpp \
  -o /tmp/check_m10_full_source_weighted_hall_tranche

OMP_NUM_THREADS=5 /tmp/check_m10_full_source_weighted_hall_tranche
```

The remaining finite task is unchanged in scope but now has a certified first
block: solve the other 47,100 supported signed instances, preferably in
source-count bands with reusable flow workspaces and resumable exact ledgers.

The next theorem identifier after this chapter is `PP3bsb`.
