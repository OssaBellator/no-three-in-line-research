# Correlated terminal normalizer-bin envelopes through `m=10`

`docs/369` bounds the fibre-capacity-weighted terminal load by maximizing the
population of every normalizer bin independently. That loses the fact that the
same target cycle must support all bin populations simultaneously. At `m=9`
this loss is large enough to destroy contraction even though the exact policy is
contractive.

This chapter retains the target-wise correlation. No asymptotic correlated-bin
estimate is claimed.

## 1. Target-correlated scale separation

Let the disjoint integer normalizer bins be

```text
I_j = [L_j,U_j],
```

and for a target cycle `eta` define

```text
b_j(eta) = #{incoming labelled moves i to eta with Z_i in I_j}.
```

### Proposition PP3btb -- PROVED / TARGET-CORRELATED BIN ENVELOPE

For every target cycle,

```text
kappa_F(eta) <= E(eta) := sum_j b_j(eta)/L_j.
```

Consequently

```text
sup_eta kappa_F(eta) <= max_eta E(eta).
```

#### Proof

Every incoming label in `I_j` has normalizer at least `L_j`, hence contributes
at most `1/L_j`. Summing over the actual target-specific bin populations gives
the first inequality. Maximizing only after the sum preserves all correlations
between the normalizer scales. ∎

The independent-bin envelope of `docs/369` replaces `b_j(eta)` by its separate
maximum `B_j`. Therefore

```text
max_eta E(eta) <= sum_j B_j/L_j,
```

with strict inequality whenever the separate bin maxima cannot coexist on one
target.

## 2. Exact correlated envelopes

### Theorem PP3btc -- VERIFIED FINITELY / COMPLETE CORRELATED-BIN CENSUS

Using the same dyadic bins as `docs/369`, the exact maxima of `E(eta)` are:

| `m` | maximizing target bin populations | exact correlated envelope | decimal | target components | ties |
|---:|---:|---:|---:|---:|---:|
| 8 | `(16,384,1344)` | `203200918/383360387` | `0.530051943004...` | 8 | 2 |
| 9 | `(0,256,5376,1536)` | `148937290752/183330241195` | `0.812398924374...` | 8 | 2 |
| 10 | `(0,896,4096,3072)` | `7972033929088/35188130299905` | `0.226554632518...` | 9 | 2 |

The clean rational bounds are

```text
m=8:  203200918/383360387 < 8/15,
m=9:  148937290752/183330241195 < 13/16,
m=10: 7972033929088/35188130299905 < 1/4.
```

Their exact margins are

```text
m=8:  18869326/5750405805,
m=9:  296483503/2933283859120,
m=10: 3299994583553/140752521199620.
```

#### Verification

The warning-clean checker reconstructs the complete terminal clean-macro shells,
every closing labelled move, and its capacity normalizer. It records the full
bin-population vector for each predecessor-shell target. For each target it
computes `E(eta)` exactly as a rational and then takes the exact maximum. The
normalizer ranges, independent-bin maxima, correlated maxima, maximizing bin
vectors, target component counts, tie counts, and exact capacity-weighted loads
are hard-coded regressions. ∎

## 3. The `m=9` correlation obstruction is resolved

### Corollary PP3btd -- PROVED / VERIFIED FINITELY / FOUR-BIN CONTRACTION THROUGH `m=10`

The same coarse dyadic bins certify terminal contraction at all three audited
sizes once their populations are kept correlated.

At `m=9`, the independent-bin envelope was

```text
1.114133388102... > 1,
```

while the target-correlated envelope is

```text
0.812398924374... < 13/16.
```

Thus the previous failure was entirely caused by combining bin maxima attained
on different target cycles. No refinement of the normalizer partition is needed
for finite contraction through `m=10`.

The asymptotic terminal problem is correspondingly sharper: prove a summable
bound on the *joint* target profile

```text
(b_1(eta),...,b_r(eta)),
```

or an equivalent correlated cumulative estimate. Separate per-scale maxima may
be too weak even when the underlying policy contracts.

Compile and run with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_normalizer_correlated_bin_envelope.cpp \
  -o /tmp/check_terminal_normalizer_correlated_bin_envelope

for m in 8 9 10; do
  OMP_NUM_THREADS=8 /tmp/check_terminal_normalizer_correlated_bin_envelope "$m"
done
```

The next theorem identifier after this chapter is `PP3bte`.
