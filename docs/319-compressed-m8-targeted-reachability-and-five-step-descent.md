# Compressed `m=8` targeted reachability and five-step descent

`docs/318` scores every signed Hamilton state at `m=8` but leaves the directed
targeted graph open.  Storing all directed edges is unnecessary.  The owner
interaction tables determine both the defect value and every possible targeted
predecessor of a state.

No asymptotic bounded-horizon theorem is claimed.

## 1. Exact implicit reverse neighbours

Index a state by its Hamilton cycle `rho` and orientation word `e`.  Store:

```text
P(x): owner pairs supporting at least one two-owner flaw,
T(x): owner triples supporting at least one three-owner flaw.
```

### Proposition PP3bma -- PROVED / IMPLICIT REVERSE GRAPH

Every incoming targeted edge to a state `y=(rho,e)` is obtained by exactly one of
the following tests.

1. **Orientation predecessor.**  For a source `s`, put
   `x=(rho,e xor 1_s)`.  Then `x->y` is a legal targeted flip precisely when
   some pair in `P(x)` contains `s`.
2. **Rotation predecessor.**  For a source triple `S`, apply the involutive
   successor rotation on `S` to `rho`, obtaining the unique predecessor cycle
   `rho_S`.  Keep the orientation bits outside `S` equal to those of `y` and
   enumerate the eight old bit assignments on `S`.  Such a predecessor `x`
   has a legal targeted rotation to `y` precisely when `S in T(x)`.

#### Proof

A targeted two-owner action flips exactly one owner orientation, and every owner
of the selected two-owner flaw is an allowed flip source.  Reversing the bit
therefore gives the first characterization.

For a fixed source triple, the successor rotation is an involution by PP3bjh.
A forward targeted rotation leaves every sign outside the triple unchanged and
may choose any of the eight fresh sign assignments on the triple.  Reversing the
move therefore fixes the outside bits and enumerates the eight possible old
inside assignments.  The move was targeted exactly when the predecessor
contained a three-owner flaw on that source triple.  These are all supported
move types from PP3bka. ∎

Thus reverse breadth-first search needs only constant-time owner-mask tests and
never materializes the full edge set.

## 2. Exact reachability at `m=8`

### Theorem PP3bmb -- VERIFIED FINITELY

The complete signed Hamilton state space at `m=8` has

```text
1,290,240 states,
28 valid states.
```

Every state reaches a valid state by flaw-targeted orientation flips and
three-source successor rotations.  The exact distance distribution to the valid
set is

| distance | states |
|---:|---:|
| 0 | 28 |
| 1 | 1,560 |
| 2 | 57,408 |
| 3 | 736,212 |
| 4 | 493,728 |
| 5 | 1,304 |

Hence the maximum directed distance to validity is five.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m8.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m8
/tmp/check_hamilton_combined_flaw_reachability_m8
```

The checker rebuilds the exact orbit geometry, precomputes all pair and triple
owner interactions, scores every state, constructs reverse neighbours by
PP3bma, and compares the complete distance distribution against the stored
ledger `experiments/hamilton-combined-flaw-reachability-m8.json`. ∎

## 3. Five-step strict-descent upper bound

Recall the integer potential

```text
Psi = B_3/4
```

from PP3blz.

### Corollary PP3bmc -- VERIFIED FINITELY / DESCENT HORIZON EXTENDED

For every nonvalid signed Hamilton state at `m=8`, there is a flaw-targeted walk
of length at most five ending at a state with strictly smaller `Psi`.

#### Proof

PP3bmb gives a targeted walk of length at most five from every state to a valid
state.  A valid state has `Psi=0`, while every nonvalid state has positive
integer `Psi`. ∎

This proves a uniform five-step strict-descent **upper bound** at `m=8`.  It does
not prove that five is the smallest possible strict-descent horizon; the 1,304
states at distance five from validity may still reach an intermediate lower
potential sooner.

## 4. Revised bounded-horizon frontier

The exact finite picture is now

```text
m<=7: maximum distance to optimum at most 4,
m=8:  maximum distance to validity exactly 5.
```

The next asymptotic target remains a uniform bound independent of `m`, or a
weighted potential for which the owner-interaction structure gives such a bound.
A secondary finite target is the exact strict-descent-distance distribution at
`m=8`, which is finer than distance to validity.
