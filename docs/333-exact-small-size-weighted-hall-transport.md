# Exact small-size weighted Hall transport and label-merging penalties

`docs/324` proves that the optimal one-step merged charge for an atomic
three-owner flaw `A` is

```text
gamma_A^* = max_(empty != U subseteq X_A) w_A(U)/v(N(U)).
```

`docs/330` gives the dynamic heat-kernel version. This chapter exhausts every
atomic signed-assignment flaw and every Hall subset through `m=7`.

No asymptotic expansion or mixing theorem is claimed.

## 1. Finite exhaustive transport model

For each atomic signed three-owner flaw:

1. enumerate every clean source cycle carrying its three directed assignments;
2. count the compatible clean source orientations, giving `w_A(rho)`;
3. enumerate every parity-clean target cycle reachable by an owner-intersecting
   successor rotation;
4. weight each target by its complete clean fibre size `v(eta)`;
5. enumerate every nonempty subset of the source-cycle set.

A flaw has at most six source cycles in the audited range, so the complete Hall
maximum is exact.

### Theorem PP3boi -- VERIFIED FINITELY / COMPLETE SMALL HALL AUDIT

The exact worst optimal charges are:

| `m` | clean signed states | atomic signed-assignment flaws | worst charge | `m^3 gamma` |
|---:|---:|---:|---:|---:|
| 4 | 80 | 52 | `2/48` | `2.66667` |
| 5 | 376 | 368 | `4/148` | `3.37838` |
| 6 | 3,576 | 1,692 | `16/860` | `4.01860` |
| 7 | 36,736 | 5,100 | `96/7,448` | `4.42105` |

For the flaw attaining the worst absolute charge at each size, the maximizing
Hall subset is the complete source-cycle set. Hence the worst audited charge is
already the global source mass divided by its full reachable fibre mass.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_weighted_hall_transport_small.cpp \
  -o /tmp/check_weighted_hall_transport_small
/tmp/check_weighted_hall_transport_small
```

The checker compares exact integer numerators and denominators with
`experiments/weighted-hall-transport-small-audit.json`. ∎

## 2. Proper Hall bottlenecks do occur

### Theorem PP3boj -- VERIFIED FINITELY / LABEL-MERGING PENALTY CENSUS

No atomic flaw has a proper-subset Hall bottleneck at `m=4` or `m=5`. At the
next sizes:

```text
m=6: 884 of 1,692 flaws have a proper bottleneck,
m=7: 4,864 of 5,100 flaws have a proper bottleneck.
```

The largest ratio

```text
[optimal Hall charge]/[global-source-set ratio]
```

is

```text
m=6: 1.44962,
m=7: 1.69555.
```

Thus label merging is a real local phenomenon even though it does not determine
the worst absolute charge through `m=7`.

## 3. Finite stationary-scale evidence

### Corollary PP3bok -- VERIFIED FINITELY / CUBIC-SCALE CONSISTENCY

Across `4<=m<=7`, the exact maximum satisfies

```text
gamma_A^* <= 4.422/m^3.
```

This is finite evidence for the `Theta(m^-3)` expansion target in `docs/324` and
the stationary clean-flaw scale in `docs/330`. It is not an asymptotic bound:
the source sets grow factorially after the audited range, and proper Hall cuts
already become common.

## 4. Revised charge frontier

The finite transport data separate two tasks:

1. control the global clean-measure mass of an atomic flaw at scale `O(m^-3)`;
2. prove that every proper weighted Hall cut loses at most a constant or
   subpolynomial factor relative to that global mass.

The next exact target is `m=8`, where one flaw may have 24 source cycles and
subset enumeration should be replaced by exact max-flow or parametric min-cut.
The asymptotic target remains a weighted expansion or heat-kernel mixing theorem
on the clean-cycle coordinate.
