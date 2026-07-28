# Exact `m=10` direct-clean charge optimum and layer-packing obstruction

`docs/353` constructs two globally target-disjoint locally coupled direct-clean
repair layers on all `12,786,720` optimal positive signed Hamilton states at
`m=10`. Averaging those layers gives reverse-column charge at most `1/2`.
This chapter proves that the factor `1/2` is sharp by auditing the number of
distinct clean targets available to each source.

No asymptotic charge or layer-packing theorem is claimed.

## 1. Degree versus disjoint repair layers

Let `G=(S,T,E)` be any finite source-target action graph. A row-stochastic
policy `P` is supported on `E` when

```text
P(x,y)>0 only if xy is an edge,
sum_y P(x,y)=1 for every source x.
```

Write

```text
q=min_(x in S) |N(x)|.
```

An `r`-layer packing is a family of maps

```text
f_1,...,f_r:S -> T
```

such that every `f_i(x)` is adjacent to `x` and all `r|S|` selected targets are
distinct.

### Proposition PP3brn -- PROVED / DEGREE-LAYER CHARGE SANDWICH

For every supported row-stochastic policy,

```text
max_y sum_x P(x,y) >= 1/q.
```

Every `r`-layer packing gives a supported policy with maximum column load at
most `1/r`, by choosing the layers uniformly. Moreover, no layer packing can
have more than `q` layers.

#### Proof

Choose a source `x_0` with exactly `q` neighbours. Its row mass one is
supported on those `q` targets, so one receives mass at least `1/q` from
`x_0` alone. This proves the lower bound.

For an `r`-layer packing, assign probability `1/r` to each edge
`x -> f_i(x)`. Every target occurs in at most one selected edge over all
sources and layers, so every column receives at most `1/r`.

Finally, one source with only `q` available targets cannot be assigned more
than `q` distinct targets. ∎

Thus a layer packing whose size equals the minimum source degree is
simultaneously optimal among all fractional policies.

## 2. Exact locally coupled target-degree census

For an optimal positive signed source `(rho,e)`, retain every distinct clean
signed target `(eta,e')` obtainable by one successor rotation on a three-owner
set `T`, with

```text
e' xor e subseteq T.
```

Duplicate labels leading to the same signed target are removed before the
degree is counted.

### Theorem PP3bro -- VERIFIED FINITELY / COMPLETE `m=10` LOCAL TARGET DEGREE

Across all `12,786,720` optimal positive sources,

```text
minimum distinct locally coupled clean targets = 2,
maximum distinct locally coupled clean targets = 420.
```

The complete small-degree tail is

| distinct targets | source states |
|---:|---:|
| 2 | 8 |
| 4 | 24 |
| 6 | 28 |
| 8 | 36 |

There are no degree-three, degree-five, degree-seven, or degree-nine sources.
The eight degree-two states lie over two Hamilton cycles, with four orientation
masks on each cycle. Their exact cycles and masks are recorded in the machine
ledger.

#### Verification

The checker reconstructs the complete pair geometry, all Hamilton cycles,
every optimal orientation mask, and every clean rotated target cycle. For each
source it enumerates all allowed sign updates on the rotated triple, encodes
the resulting clean signed targets, removes duplicates, and records the exact
degree. The source total reproduces the earlier `m=10` optimal-state census
before the degree ledger is accepted. ∎

## 3. Exact charge optimum and layer capacity

### Corollary PP3brp -- PROVED / VERIFIED FINITELY / SHARP HALF-CHARGE

For the complete locally coupled direct-clean action at `m=10`:

```text
maximum number of globally target-disjoint deterministic layers = 2,
minimum possible maximum reverse-column load                 = 1/2.
```

#### Proof

`docs/353` supplies two target-disjoint layers, so the layer capacity is at
least two and the optimal column load is at most `1/2`.

PP3bro supplies a source with exactly two distinct targets. PP3brn therefore
forbids a third disjoint layer and gives column load at least `1/2` for every
fractional policy. The upper and lower bounds coincide. ∎

Consequently the finite direct-clean switch at the first nonforest size is
optimally contractive by exactly one half. Clean fibre regeneration and every
subsequent stochastic clean-cycle heat step can only decrease the inherited
`L^infinity` density further.

The remaining problem is asymptotic: prove a uniform lower bound on local
target degree together with a comparably large multi-layer packing, or replace
integral layers by a geometric Hall-balanced policy.

Compile and run the exact census with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_local_direct_clean_target_degree.cpp \
  -o /tmp/check_m10_local_direct_clean_target_degree

OMP_NUM_THREADS=12 \
  /tmp/check_m10_local_direct_clean_target_degree
```

The next theorem identifier after this chapter is `PP3brq`.
