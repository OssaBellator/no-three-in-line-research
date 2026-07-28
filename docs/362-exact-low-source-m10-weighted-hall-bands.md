# Exact low-source `m=10` weighted-Hall bands

`docs/357` reduces the complete `m=10` atomic flaw-transport problem to `47,512`
weighted maximum-closure instances.  `docs/360` completes the `412` instances
with the full factorial support of `720` source cycles.  This chapter makes the
complementary first step from the low-support end by completing every supported
flaw with at most `399` compatible source cycles.

No claim is made about the remaining source-count bands or asymptotic weighted
expansion.

## 1. The `106--199` source band

### Theorem PP3bse -- VERIFIED FINITELY / COMPLETE LOWEST-SOURCE BAND

Exactly `132` signed `m=10` flaws have between `106` and `199` compatible source
cycles.  Every one has a proper weighted Hall bottleneck.

The worst exact optimal charge is

```text
gamma_[106,199] = 256/57011
                = 0.00449036150918...,
10^3 gamma_[106,199] = 4.49036150918... .
```

A canonical maximizing flaw has

```text
source owners:       (0,2,3),
target assignments:  (1,7,9),
orientations:        (1,1,0).
```

It has `137` compatible source cycles.  Its maximizing Hall set contains only
`16` source cycles, with

```text
W = 2,048,
V = 456,088,
W/V = 256/57,011.
```

The worst complete-source ratio anywhere in the band is `623/199779`.  The
maximum ratio between a flaw's optimal Hall charge and its own complete-source
ratio is

```text
309616/155357 = 1.99293240729... .
```

The exact Dinkelbach computation uses at most seven conceptual cuts.

## 2. The `200--399` source band

### Theorem PP3bsf -- VERIFIED FINITELY / COMPLETE SECOND SOURCE BAND

Exactly `2,628` signed `m=10` flaws have between `200` and `399` compatible source
cycles.  Every one has a proper weighted Hall bottleneck.

The worst exact optimal charge is

```text
gamma_[200,399] = 1560/281873
                = 0.00553440733948...,
10^3 gamma_[200,399] = 5.53440733948... .
```

A canonical maximizing flaw has

```text
source owners:       (2,5,7),
target assignments:  (5,6,8),
orientations:        (1,1,0).
```

It has `386` compatible source cycles.  Its maximizing Hall set contains `235`
source cycles, with

```text
W = 24,960,
V = 4,509,968,
W/V = 1,560/281,873.
```

The worst complete-source ratio anywhere in the band is `2015/372577`.  The
maximum local/global merging penalty is

```text
1500597/656230 = 2.28669368971... .
```

The exact Dinkelbach computation uses at most eight conceptual cuts.

## 3. Certified cut-scale spectrum

### Corollary PP3bsg -- VERIFIED FINITELY / THREE SOURCE-SCALE BLOCKS

The exact `m=10` Hall audit now covers

```text
132   flaws in the 106--199 band,
2,628 flaws in the 200--399 band,
412   flaws with exactly 720 source cycles,
------------------------------------------
3,172 signed flaws in total.
```

All `3,172` audited flaws have proper bottlenecks.  The remaining exact workload
is `44,340` signed instances.

The three certified worst cuts occupy sharply different source scales:

| source block | source universe of maximizing flaw | maximizing Hall subset |
|---|---:|---:|
| `106--199` | 137 | 16 |
| `200--399` | 386 | 235 |
| exactly `720` | 720 | 686 |

Thus the finite obstruction already ranges from a local cut to a genuinely
intermediate cut and finally to an almost-global cut.  This reinforces the
all-scale expansion requirement from `docs/342`: neither constant-size control
nor complete-source mass alone can certify the transport bound.

The largest scaled charge among the three completed blocks is

```text
10^3 * 1560/281873 = 5.53440733948...,
```

which remains below the complete `m=9` maximum `5.553858...`.  This continues to
support, but does not prove, an `O(m^-3)` scale.

#### Verification

The checker reconstructs the complete `m=10` geometry and compressed flaw-source
census before processing either band.  For every retained flaw it constructs the
owner-intersecting clean transport graph, merges duplicate target cycles, uses
exact fibre capacities, and runs rational Dinkelbach iteration with exact
integer maximum-closure min-cuts.  Both complete band ledgers are hard-coded,
and ties between maximizing flaws are resolved lexicographically. ∎

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_weighted_hall_low_source_bands.cpp \
  -o /tmp/check_m10_weighted_hall_low_source_bands

OMP_NUM_THREADS=8 \
  /tmp/check_m10_weighted_hall_low_source_bands 106 199
OMP_NUM_THREADS=8 \
  /tmp/check_m10_weighted_hall_low_source_bands 200 399
```

A direct `400--499` run with the current fresh-allocation Dinic implementation
exceeded the execution window.  The next implementation step is therefore still
workspace reuse and resumable narrower bands, not acceptance of partial output.

The next theorem identifier after this chapter is `PP3bsh`.
