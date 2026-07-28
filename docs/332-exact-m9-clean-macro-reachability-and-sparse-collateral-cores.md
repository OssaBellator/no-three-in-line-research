# Exact `m=9` clean-macro reachability and sparse collateral cores

`docs/328` proves that every one of the `404,080` parity-clean signed states at
`m=8` reaches a line-valid state within three owner-intersecting clean macro
steps. This chapter scales the same compressed reverse search to `m=9`,
classifies the terminal distance layers, and tests the two most natural defect
potentials.

No uniform macro horizon, asymptotic descent theorem, or prime seed is claimed.

## 1. Exact clean-macro graph at `m=9`

A macro step starts from a parity-clean signed state, selects a present
three-owner flaw with owner set `S`, rotates any source triple meeting `S`,
requires a parity-satisfiable target cycle, and then chooses any clean orientation
in the target fibre.

### Theorem PP3boe -- VERIFIED FINITELY / COMPLETE `m=9` REACHABILITY

At `m=9` there are

```text
31,688 parity-satisfiable Hamilton cycles,
6,727,728 parity-clean signed states,
8 line-valid signed states.
```

Every clean signed state reaches validity. The exact macro-distance distribution
is

| distance | states |
|---:|---:|
| 0 | 8 |
| 1 | 59,008 |
| 2 | 1,317,376 |
| 3 | 4,873,296 |
| 4 | 478,040 |

Thus the maximum clean-macro distance increases from three at `m=8` to four at
`m=9`.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_parity_clean_macro_reachability_m9.cpp \
  -o /tmp/check_parity_clean_macro_reachability_m9
/tmp/check_parity_clean_macro_reachability_m9
```

The checker reconstructs every clean fibre and every three-owner flaw-support
mask. Reverse search is compressed through target cycles: once any clean state
over a target cycle has distance `d`, every legal predecessor state has distance
at most `d+1`. All totals are checked against
`experiments/parity-clean-macro-reachability-m9-audit.json`. ∎

## 2. Terminal-layer owner geometry

Let `H(x)` be the three-uniform hypergraph of owner triples supporting at least
one bad geometric triple in a clean signed state `x`, and let `tau(H)` be its
minimum owner cover number.

### Theorem PP3bof -- VERIFIED FINITELY / TERMINAL CORE CENSUS

For the `33,632` distance-three states at `m=8`, the owner-cover distribution is

```text
tau=1:    528,
tau=2: 11,908,
tau=3: 19,508,
tau=4:  1,688.
```

Their support count ranges from one to 38. In particular the terminal layer is
not one intersecting-star family.

For the `478,040` distance-four states at `m=9`, the owner-cover distribution is

```text
tau=1:    588,
tau=2: 58,772,
tau=3:318,892,
tau=4: 97,848,
tau=5:  1,940,
```

and the support count ranges from one to 43.

The `m=8` classification is checked by
`scripts/check_parity_clean_macro_terminal_core_m8.cpp`; the `m=9` values are
checked by the reachability checker above. ∎

## 3. Raw support and atomic counts are not descent potentials

Write

```text
h(x)=number of flaw-support owner triples,
a(x)=number of atomic bad geometric triples.
```

A macro target may choose the minimum-count orientation in its clean target
fibre.

### Theorem PP3bog -- VERIFIED FINITELY / NATURAL POTENTIAL BARRIER

At `m=9`, among nonvalid clean signed states:

```text
2,160 states have no one-step decrease of h,
2,148 states have no one-step decrease of a,
2,104 states are local minima for both.
```

By macro distance, the joint obstruction includes 68 distance-four states.
Every legal target of one of those 68 states has both

```text
h(target)>=h(source),
a(target)>=a(source).
```

Consequently no nonnegative linear combination

```text
alpha h + beta a,   alpha,beta>=0,
```

can be a universal one-step strict-descent potential, unless both coefficients
vanish.

## 4. Exact sparse normal form of the 68 hard states

### Theorem PP3boh -- VERIFIED FINITELY / SPARSE COLLATERAL CORE

The 68 distance-four joint local minima have:

```text
support count 1:  8 states,
support count 2: 56 states,
support count 3:  4 states;
```

exactly four atomic triples per support, owner-cover number at most two, and only
five owner-degree signatures:

```text
1-1-1-0-0-0-0-0-0 :  8,
1-1-1-1-1-1-0-0-0 : 24,
2-1-1-1-1-0-0-0-0 : 24,
2-2-1-1-0-0-0-0-0 :  8,
2-2-2-1-1-1-0-0-0 :  4.
```

They lie on 22 Hamilton cycles and form 34 global-sign-complement pairs.

For 60 of the 68 states, a lower support and atomic count is reachable in exactly
two macro steps. The remaining eight states have one support and one atomic
quarter-turn orbit; their first lower count is validity itself, at distance four.
They form four complement pairs.

Thus the terminal obstruction is sparse collateral repair, not dense flaw mass.

## 5. Revised clean-macro frontier

The finite clean-macro horizons are now

```text
m=8: 3,
m=9: 4.
```

The next targets are:

1. classify the eight one-support four-step states by an invariant normal form;
2. construct a bounded collateral-repair word for a single atomic orbit;
3. find a structural potential that distinguishes the 68 sparse local minima;
4. extend compressed clean-macro reachability to `m=10` without storing all
   `115,586,396` clean orientations explicitly;
5. combine bounded macro repair with the heat-kernel charge and causal-light-cone
   interfaces.

The finite distance bound does not imply an asymptotically bounded horizon.
