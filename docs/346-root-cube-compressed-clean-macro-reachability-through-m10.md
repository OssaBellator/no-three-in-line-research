# Root-cube compressed clean-macro reachability through `m=10`

`docs/332` proves complete clean-macro reachability through `m=9`, but its
state-level representation does not scale directly to the

```text
115,586,396
```

parity-clean signed states at `m=10`.  This chapter stores each clean
orientation fibre as an affine component-root cube and performs the reverse
reachability search with bit sets.

No uniform macro horizon, asymptotic reachability theorem, or
no-three-in-line seed theorem is claimed.

## 1. Clean fibres are affine root cubes

Let `rho` be a Hamilton cycle with satisfiable parity graph `H_rho`.  Give each
connected parity component one root bit.  Propagating the signed XOR equations
expresses every owner orientation as

```text
e_i = colour_i xor root_(component_i).
```

### Proposition PP3bqf -- PROVED / AFFINE ROOT-CUBE REPRESENTATION

If `H_rho` has `c(rho)` connected components, its clean orientation fibre is
canonically an affine cube of size

```text
2^c(rho).
```

For any fixed owner support `S`, the presence of an atomic flaw on `S` is a
Boolean function of at most the component-root bits met by `S`.

#### Proof

Choose one root value in each connected component.  Every parity edge then
forces the remaining owner values uniquely, and consistency makes the result
independent of propagation path.  Conversely, every root assignment gives one
clean orientation.

An atomic flaw on `S` depends only on the signed assignments of owners in `S`.
Those signs are affine functions of the component roots touched by `S`, so flaw
presence depends only on those roots. ∎

At `m=10`, one fibre therefore needs at most `2^10=1024` bits rather than one
explicit record per signed state.

## 2. Owner-incidence masks encode every legal source rotation

For a clean cycle `rho` and owner `i`, define the root-cube bit set

```text
B_i(rho)
```

to contain exactly the clean orientations for which some present three-owner
flaw support contains `i`.

### Proposition PP3bqg -- PROVED / OWNER-INCIDENCE ELIGIBILITY

For a source triple `T={a,b,c}`, the clean source orientations from which the
macro may rotate `T` are exactly

```text
B_a(rho) union B_b(rho) union B_c(rho).
```

A clean orientation is line-valid exactly when it belongs to none of the
owner-incidence masks.

#### Proof

The macro may rotate `T` precisely when `T` meets at least one present
three-owner flaw support.  This occurs exactly when one of its three owners is
incident with such a support, giving the displayed union.

A parity-clean orientation has no two-owner atomic flaw by construction, and
one orbit contains no collinear triple.  Hence it is line-valid exactly when it
has no three-owner flaw support, equivalently when no owner-incidence mask
contains it. ∎

The checker constructs each `B_i(rho)` with word-level Boolean operations from
the eight sign patterns on one owner triple.

## 3. Reverse search needs only the best target orientation per cycle

Let `d(x)` be clean-macro distance to validity for a clean signed state `x`.
For a clean cycle `rho`, define

```text
d_min(rho)=min d(x)
```

over its clean fibre.

### Theorem PP3bqh -- PROVED / CYCLE-MINIMUM REVERSE RECURRENCE

Suppose a clean target cycle `eta` has `d_min(eta)=d`.  For any source triple
`T`, let `rho` be its inverse successor neighbour.  Every clean orientation in

```text
B_a(rho) union B_b(rho) union B_c(rho)
```

has distance at most `d+1`.

Consequently each target cycle needs to be processed only when its first
reachable orientation is discovered.  Layered reverse search on cycle minima,
together with one reached bit set per root cube, computes every signed-state
distance exactly.

#### Proof

Choose a target orientation over `eta` attaining distance `d`.  The clean macro
allows arbitrary regeneration in the target clean fibre.  Therefore every
eligible source orientation over `rho` may rotate `T`, choose that target
orientation, and then follow its length-`d` path.

Processing a cycle at its first discovery uses its smallest possible target
distance.  Later orientations over the same cycle cannot improve the
predecessor bound.  A reached mask prevents duplicate assignment and records
the first, hence exact, distance layer of every root assignment. ∎

This is the compression that removes the need for a 115-million-entry signed
state graph.

## 4. Complete regression at `m=9`

### Theorem PP3bqi -- VERIFIED FINITELY / ROOT-CUBE REGRESSION

The bitset algorithm exactly reproduces the complete `m=9` ledger:

```text
parity-satisfiable cycles: 31,688
clean signed states:    6,727,728
line-valid states:              8
unreached states:               0
```

with distance distribution

```text
0:         8
1:    59,008
2: 1,317,376
3: 4,873,296
4:   478,040
```

Thus the cycle-minimum recurrence and owner-incidence masks agree with the
state-level verifier of `docs/332`.

## 5. Complete `m=10` clean-macro reachability

### Theorem PP3bqj -- VERIFIED FINITELY / FIVE-MOVE `m=10` HORIZON

At `m=10` there are

```text
297,886 parity-satisfiable Hamilton cycles,
115,586,396 parity-clean signed states,
12 line-valid signed states.
```

Every clean signed state reaches validity.  The exact distance distribution is

| distance | signed states |
|---:|---:|
| 0 | 12 |
| 1 | 205,376 |
| 2 | 5,534,564 |
| 3 | 52,044,980 |
| 4 | 57,266,392 |
| 5 | 535,072 |

Hence

```text
maximum clean-macro distance at m=10 = 5.
```

The entries sum to all `115,586,396` clean signed states, and the unreached
count is zero.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_parity_clean_macro_reachability_m10_bitset.cpp \
  -o /tmp/check_parity_clean_macro_reachability_m10_bitset

OMP_NUM_THREADS=8 \
  /tmp/check_parity_clean_macro_reachability_m10_bitset 9

OMP_NUM_THREADS=8 \
  /tmp/check_parity_clean_macro_reachability_m10_bitset 10
```

The first invocation checks the complete hard-coded `m=9` regression.  The
second reconstructs all `9!` Hamilton cycles, every satisfiable parity fibre,
the owner-incidence root masks, and the complete reverse macro search.  It
compares the exact `m=10` ledger with

```text
experiments/parity-clean-macro-reachability-m10-bitset-audit.json.
```

∎

## 6. Revised clean-macro frontier

The finite clean-macro horizons are now

```text
m=8:  3,
m=9:  4,
m=10: 5.
```

The first nonforest parity fibres do not break reachability, but the maximum
distance increases again by one.

The computational bottleneck has also shifted.

1. Explicit signed-state storage is unnecessary; affine root cubes and owner
   incidence masks suffice.
2. The complete `m=10` reachability problem is closed.
3. The next exact target is terminal-layer classification at `m=10`, especially
   the `535,072` distance-five states.
4. The asymptotic target is a structural bound on the macro horizon or a
   compensated potential that explains the observed `3,4,5` progression.
5. Charge remains separate: reachability does not control predecessor merging
   along the five-step paths.

The next theorem identifier after this chapter is `PP3bqk`.
