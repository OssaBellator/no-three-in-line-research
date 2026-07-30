# Mixed-period supercycles for shell controls

`docs/529` optimizes the order of one shell-service multiset. A complete shell
controller may superpose several periodic subsystems with different periods.
This chapter synchronizes them through a finite phase torus and computes the
minimum startup reserve of the resulting supercycle.

Subsystem `i` has period `p_i`, service vector `s_i(t)`, and mean `bar s_i`.
Choose a phase `phi_i`, put `L=lcm_i p_i`, and define the aggregate centered
increment

```text
d_phi(t)=sum_i (s_i(t+phi_i)-bar s_i).
```

It has period `L` and zero total over one superperiod.

## 1. Exact phase buffer

### Theorem PP3cmf -- PROVED / MIXED-PERIOD STARTUP BUFFER

For a fixed phase vector `phi`, the componentwise least startup reserve is

```text
b_j(phi)=max_(0<=t<=L) -sum_(u<t) d_phi(u)_j.
```

Starting with `b(phi)` makes every prefix feasible, and decreasing any coordinate
violates the prefix attaining its maximum deficit.

#### Proof

The reserve after `t` slots is the initial reserve plus the displayed cumulative
centered service. Nonnegativity for every prefix is equivalent to the stated
coordinatewise lower bounds, and each bound is attained by definition. ∎

## 2. Finite phase-torus optimization

### Theorem PP3cmg -- PROVED / SUPERCYCLE PHASE ORACLE

All phase choices form the finite torus

```text
product_i Z/p_i Z.
```

Exact enumeration computes every buffer vector, its Pareto frontier, and an
optimizer for any rational monotone objective such as `l_1` or `l_infinity`.
A predecessor table reconstructs the corresponding mixed-period supercycle.

#### Proof

There are only `product_i p_i` phase vectors, and `PP3cmf` evaluates each from
`L` rational prefix sums. Pareto pruning and objective comparison are exact
finite operations. ∎

## 3. Arbitrary truncations

### Theorem PP3cmh -- PROVED / MIXED-PERIOD ALL-LENGTH CERTIFICATE

Repeating an optimized supercycle preserves feasibility for every finite
truncation. Complete superperiods have zero centered sum; the remaining residue
uses the stored prefix table. The startup reserve contributes average overhead
`b(phi)/N`, hence `O(1/N)`.

#### Proof

Decompose the truncation into complete superperiods and one prefix. The complete
periods do not change reserve relative to the mean, and `PP3cmf` protects the
prefix. ∎

## 4. Stored exact fixture

The audit `scripts/check_mixed_period_shell_supercycles.py` combines

```text
W1=AB  of period 2,
W2=AAB of period 3.
```

The aggregate target is `(7/6,5/6,0)` and the superperiod is six. Among the six
phase pairs, the exact `l_infinity` buffer values are

```text
2/3,2/3,5/6,5/6,7/6,7/6.
```

The two optimal phases are `(0,2)` and `(1,0)`. The lexicographic phase has
buffer `(2/3,1/2,0)` and supercycle

```text
AB,BA,AA,BB,AA,BA.
```

The audit verifies every prefix through length 120.

## 5. Prime-patching consequence

Shell components with unrelated local periods can now be synchronized without
rounding them to independent startup reserves. One finite phase-torus search
gives the exact shared supercycle and its vanishing finite-length overhead.
