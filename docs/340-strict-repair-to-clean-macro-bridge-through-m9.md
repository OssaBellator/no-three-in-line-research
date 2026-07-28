# Strict-repair to clean-macro bridge through `m=9`

`docs/336` shows that most target-optimal fixed-sign states whose total atomic
count does not decrease reach parity-clean termination before strict parity
repair can cancel their three-owner collateral.  `docs/328` and `docs/332`
prove that every parity-clean state through `m=9` nevertheless reaches validity
by clean macro moves.

This chapter joins those two finite graphs and measures the exact hybrid path.
No asymptotic hybrid-repair theorem is claimed.

## 1. Terminal macro profiles

Fix an optimal signed state `x=(rho,e)`.  Follow only target-optimal fixed-sign
strict-repair edges until the frustration index reaches zero.  Let `C(x)` be the
set of parity-clean terminal states reachable in this way.

For a clean state `y`, let `d_M(y)` be its exact clean-macro distance to
validity.  Define

```text
d_min(x) = min_(y in C(x)) d_M(y),
d_max(x) = max_(y in C(x)) d_M(y),
H(x)     = min_[strict path x -> y] [strict path length + d_M(y)].
```

### Proposition PP3bpg -- PROVED / EXACT HYBRID DAG RECURSION

On a parity-clean state `x`,

```text
d_min(x)=d_max(x)=H(x)=d_M(x).
```

On a positive-frustration state,

```text
d_min(x)=min_(x->y) d_min(y),
d_max(x)=max_(x->y) d_max(y),
H(x)=1+min_(x->y) H(y),
```

where the edges are target-optimal fixed-sign strict repairs.

The same DAG recursion for the least reachable total atomic count identifies
exactly the failed strict-cancellation sources of `docs/336`.

#### Proof

Every strict edge lowers the nonnegative integer frustration index, so the graph
is acyclic.  Every terminal path begins with one outgoing strict edge and then a
terminal path from its target.  Taking the appropriate minimum or maximum gives
the displayed recurrences.  At frustration zero no strict edge remains, so only
the clean-macro distance contributes. ∎

## 2. Exact `m=8` bridge

### Theorem PP3bph -- VERIFIED FINITELY / THREE-MOVE HYBRID HORIZON

There are `4,186` optimal signed `m=8` sources for which no target-optimal
fixed-sign strict-repair path reaches a lower total atomic count before parity
cleaning.  Their best terminal clean-macro distances are

```text
d_min=1: 3,020 sources,
d_min=2: 1,166 sources.
```

Their worst reachable terminal distances are

```text
d_max=2: 1,068 sources,
d_max=3: 3,118 sources.
```

The minimum total hybrid-length distribution is

```text
H=2: 3,014 sources,
H=3: 1,172 sources.
```

Thus every failed strict-cancellation source reaches validity in at most three
total moves: first use zero or more target-optimal strict repairs, then switch
to the clean-macro action.

The source-frustration distribution is

```text
lambda=1: 4,170,
lambda=2:    16.
```

## 3. Exact `m=9` bridge

### Theorem PP3bpi -- VERIFIED FINITELY / FOUR-MOVE HYBRID HORIZON

There are `25,894` failed strict-cancellation sources at `m=9`.  Their best
terminal clean-macro distances are

```text
d_min=1:  3,816 sources,
d_min=2: 19,226 sources,
d_min=3:  2,852 sources.
```

Their worst reachable terminal distances are

```text
d_max=2:    146 sources,
d_max=3: 10,680 sources,
d_max=4: 15,068 sources.
```

The minimum total hybrid-length distribution is

```text
H=2:  3,792 sources,
H=3: 19,250 sources,
H=4:  2,852 sources.
```

Hence every failed strict-cancellation source reaches validity in at most four
total moves.  The source-frustration distribution is

```text
lambda=1: 25,862,
lambda=2:     32.
```

The hybrid horizon equals, rather than exceeds, the known maximum clean-macro
horizon at `m=9`.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_strict_repair_clean_macro_bridge.cpp \
  -o /tmp/check_strict_repair_clean_macro_bridge
/tmp/check_strict_repair_clean_macro_bridge
```

The checker reconstructs the exact pair and atomic geometry, every optimal
orientation, the target-optimal strict-repair DAG, all parity-clean fibres, and
the complete reverse clean-macro distances at `m=8` and `m=9`.  It compares all
profiles with `experiments/strict-repair-clean-macro-bridge-audit.json`. ∎

## 4. Revised repair interface

The finite obstruction is now an action-switching problem, not a reachability
problem.

1. Strict parity repair is useful until the state becomes parity clean, even
   when it does not lower the complete atomic count.
2. At parity-clean termination, switching to the clean macro reaches validity
   without increasing the existing finite horizon.
3. The remaining asymptotic task is to price that switch: control predecessor
   merging and compensated three-owner collateral across the boundary between
   the locally coupled strict action and the fibre-regenerating clean action.
4. `docs/338` confines all collateral created before the switch to the union of
   rotated owners, while `docs/339` supplies sharp bounded-collateral words for
   the smallest isolated terminal core.

The next theorem identifier after this chapter is `PP3bpj`.
