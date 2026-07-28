# Exact two-owner atomic descent and the three-owner collateral barrier

`docs/328` keeps the complete orientation vector fixed while decreasing the
minimum parity-edge violation count. A parity edge is only a compressed owner-
pair predicate: one violated edge may represent several atomic collinear
triples. This chapter audits the exact atomic potentials.

For a signed Hamilton state `(rho,e)`, let

```text
Z_2(rho,e) = number of collinear triples using exactly two owners,
Z_3(rho,e) = number of collinear triples using three owners,
Z(rho,e)   = Z_2(rho,e)+Z_3(rho,e).
```

The orbit construction has no one-owner collinear triple, so `Z` is the complete
atomic flaw count. All results below are finite through `m=9`.

## 1. Exact atomic lookup

For two signed assignments, enumerate the eight orbit cells and count every
collinear triple meeting both owners. For three signed assignments, enumerate
the `4^3=64` triples choosing one cell from each orbit. These counts depend only
on the displayed signed assignments and are precomputed exactly.

### Proposition PP3bno -- PROVED / EXACT ATOMIC DECOMPOSITION

For every signed Hamilton state,

```text
Z = sum over owner pairs of their two-owner lookup
  + sum over owner triples of their three-owner lookup.
```

#### Proof

Every selected point belongs to a unique owner orbit. A collinear triple uses
one, two, or three owners. A single orbit is a square and contains no three
collinear points. The pair lookup counts precisely the two-owner triples and
the triple lookup counts precisely the three-owner triples, with each atomic
triple assigned to its unique owner support. ∎

## 2. Two-owner atomic descent with fixed signs

### Theorem PP3bnp -- VERIFIED FINITELY / EXACT `Z_2` DESCENT

For every `5<=m<=9`, every optimal oriented pair-safe state with positive
frustration has a sign-preserving pair-safe strict-frustration descent that also
strictly decreases `Z_2`.

Moreover, for every violated parity edge, there is such a move that meets an
endpoint, clears that edge, and decreases `Z_2`.

| `m` | optimal oriented states | `Z_2`-descent transitions | minimum choices per state | violated-edge checks | targeted clearing `Z_2` descents | minimum choices per edge |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 | 2,752 | 37,020 | 6 |
| 8 | 93,980 | 1,639,152 | 5 | 97,224 | 1,675,180 | 5 |
| 9 | 977,312 | 24,714,106 | 4 | 1,001,344 | 25,035,496 | 4 |

Thus the fixed-sign parity descent is not merely a constraint-edge surrogate in
the audited range: it can be chosen to reduce the exact two-owner atomic defect.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_hamilton_atomic_pair_descent_and_three_owner_collateral.cpp \
  -o /tmp/check_hamilton_atomic_pair_descent_and_three_owner_collateral
/tmp/check_hamilton_atomic_pair_descent_and_three_owner_collateral
```

The checker compares all output counts with a hard-coded regression ledger and
stores the JSON output in
`experiments/hamilton-atomic-pair-descent-and-three-owner-collateral-audit.json`. ∎

## 3. Total atomic descent is not automatic

The same audit tests every sign-preserving strict-frustration descent against
`Z_3` and the total atomic potential `Z`.

### Theorem PP3bnq -- VERIFIED FINITELY / THREE-OWNER COLLATERAL BARRIER

Universal one-step total atomic descent is false in the audited range. The
numbers of optimal oriented states having no sign-preserving strict-frustration
move that decreases `Z` are:

| `m` | states without total-`Z` descent | states without even `Z_3` nonincrease |
|---:|---:|---:|
| 5 | 14 | 20 |
| 6 | 0 | 0 |
| 7 | 170 | 174 |
| 8 | 4,308 | 6,182 |
| 9 | 26,164 | 34,388 |

The targeted form also fails. The numbers of optimal violated-edge instances
for which no clearing sign-preserving strict-frustration move decreases `Z` are:

```text
m=5:       14,
m=6:        0,
m=7:      170,
m=8:    4,482,
m=9:   26,760.
```

#### Verification

For every optimal oriented state, the checker exhausts all pair-safe
strict-frustration targets preserving the same orientation and compares exact
`Z_2`, `Z_3`, and `Z`. The displayed positive failure counts are explicit
counterexamples to a universal implication from parity descent to total atomic
descent. ∎

The obstruction is genuinely three-owner collateral: PP3bnp still supplies
exact `Z_2` descent in every one of these states.

## 4. Revised atomic frontier

The two-owner preprocessing interface is now sharply separated from the generic
three-owner process.

1. Pair-safe fixed-sign rotations can clear every minimum-core edge and descend
   exact two-owner atomic defect through `m=9`.
2. The same move family does not universally control three-owner collateral.
3. Any combined potential must price newly created three-owner flaws or use a
   bounded multi-step path rather than demand immediate total descent.
4. The exact obstruction states should be classified by the source triple,
   created three-owner support, and available second-step cancellation.
5. Weighted Hall transport should be applied to rotations after including their
   `Z_3` collateral, not only their parity-edge charge.

This chapter closes the finite two-owner atomic conversion but refutes the
naive one-step total-atomic extension.
