# Target-optimal atomic cancellation depth through `m=9`

`docs/335` proves that target-optimal fixed-sign parity repair always decreases
the exact two-owner atomic defect through `m=9`, but it need not decrease the
complete atomic defect

```text
Z=Z_2+Z_3.
```

This chapter asks whether temporary three-owner collateral is cancelled by a
second or third target-optimal fixed-sign parity-repair step before the parity
potential reaches zero.

No asymptotic cancellation or no-three-in-line theorem is claimed.

## 1. The strict repair DAG

Fix an orientation vector `e`.  Its target-optimal strict-repair graph has one
vertex for every pair-safe Hamilton cycle `rho` on which `e` attains the
frustration index.  There is an edge

```text
rho -> eta
```

when `eta` is a successor rotation, `e` is still optimal on `eta`, and

```text
lambda(eta)<lambda(rho).
```

The graph is acyclic because `lambda` strictly decreases.

For a source state `x=(rho,e)`, let

```text
P_d(x)=minimum Z(y)
```

over target-optimal fixed-sign repair paths of exactly `d` edges from `x`.
Empty levels have value `+infinity`.

### Proposition PP3bor -- PROVED / EXACT DEPTH RECURSION

The profiles satisfy

```text
P_0(x)=Z(x),
P_(d+1)(x)=min_(x->y) P_d(y).
```

Every nonempty level has

```text
d<=lambda(rho).
```

Hence the first lower-total-atomic descendant, its distance, and the least
necessary temporary excess are computable exactly by dynamic search on the
strict repair DAG.

#### Proof

Every length-`d+1` path is uniquely an initial repair edge followed by a
length-`d` path.  Taking the minimum gives the recursion.  Since every edge
lowers the nonnegative integer `lambda`, no path has more than
`lambda(rho)` edges. ∎

## 2. Exact cancellation-depth census

### Theorem PP3bos -- VERIFIED FINITELY / BOUNDED CANCELLATION CENSUS

Every optimal positive-frustration signed state was audited for `5<=m<=9`.
Among states with no one-step decrease of `Z`, the exact outcomes are:

| `m` | optimal positive states | one-step obstructions | first lower `Z` at distance 2 | first lower `Z` at distance 3 | no lower `Z` before parity-clean termination |
|---:|---:|---:|---:|---:|---:|
| 5 | 48 | 14 | 0 | 0 | 14 |
| 6 | 272 | 0 | 0 | 0 | 0 |
| 7 | 2,752 | 170 | 0 | 0 | 170 |
| 8 | 93,980 | 4,308 | 122 | 0 | 4,186 |
| 9 | 977,312 | 26,164 | 270 | 0 | 25,894 |

Thus a second strict parity-repair step cancels only a small part of the
one-step collateral obstruction, and no audited state first succeeds only at
distance three.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_target_optimal_atomic_cancellation.cpp \
  -o /tmp/check_target_optimal_atomic_cancellation
/tmp/check_target_optimal_atomic_cancellation
```

The checker reconstructs all pair predicates, optimal orientations, exact
`Z_2` and `Z_3` tables, and every target-optimal fixed-sign strict-repair path.
It compares the complete output with
`experiments/target-optimal-atomic-cancellation-audit.json`. ∎

## 3. Parity termination is the dominant obstruction

### Corollary PP3bot -- VERIFIED FINITELY / TERMINAL FRUSTRATION LOCALIZATION

The unresolved states have the following source-frustration distribution:

```text
m=5: lambda=1:    14,
m=7: lambda=1:   170,
m=8: lambda=1: 4,170; lambda=2: 16,
m=9: lambda=1:25,862; lambda=2: 32.
```

In particular, almost every unresolved state already has `lambda=1`.  Its next
strict parity-repair step is parity-clean, so there is no further edge in the
strict repair DAG on which to cancel the created three-owner collateral.

This explains why merely allowing a bounded number of additional strict parity
steps does not resolve the atomic frontier.

## 4. Temporary-collateral barriers in the resolvable cases

For a path from `x` to a lower-`Z` state, define its temporary excess by

```text
max Z(along the path)-Z(x).
```

### Theorem PP3bou -- VERIFIED FINITELY / MINIMUM BARRIER DISTRIBUTION

For the 122 resolvable `m=8` obstructions, the least temporary-excess
distribution is

```text
0:60, 4:30, 8:24, 12:4, 16:4.
```

For the 270 resolvable `m=9` obstructions, it is

```text
0:124, 4:76, 8:40, 12:14,
16:6, 20:4, 24:4, 28:2.
```

Thus even among states repaired in two steps, some require a temporary increase
of 16 atomic triples at `m=8` and 28 atomic triples at `m=9`.

For the terminal unresolved states, the best reachable total atomic excess over
the source is:

```text
m=8: 0:3102, 4:888, 8:178, 12:16, 16:2,
m=9: 0:19240, 4:5554, 8:944, 12:140, 16:14, 20:2.
```

The zero class consists of paths that can hold `Z` level but cannot make it
strictly smaller before parity termination.

## 5. Revised collateral frontier

The finite evidence separates three mechanisms.

1. Exact two-owner atomic descent is automatic inside the target-optimal
   fixed-sign repair family.
2. A small family of three-owner collateral obstructions cancels after one
   additional strict repair step, sometimes with positive temporary excess.
3. The dominant family reaches parity-clean termination before total atomic
   descent occurs.

Therefore a universal repair must leave the strict parity-descent DAG, or add a
second move class after parity cleaning.  The most relevant options are:

- a clean-macro cancellation word for the terminal state;
- a potential that credits parity-core removal against later three-owner repair;
- a weighted transport action whose capacities include the terminal collateral;
- or a joint parity/three-owner move that does not require strict `lambda`
  descent at every intermediate step.

The next theorem identifier after this chapter is `PP3bov`.