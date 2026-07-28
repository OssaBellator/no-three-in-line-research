# Optimality-preserving fixed-sign frustration descent through `m=9`

`docs/331` proves that an optimal signed state through `m=9` has a successor
rotation whose violation count decreases while the complete orientation vector
is held fixed.  This chapter proves the stronger target-optimality statement:
the unchanged orientation remains a minimum orientation of the target cycle.

The result is finite.  It does not prove asymptotic descent, weighted action
charge, or a no-three-in-line seed theorem.

## 1. Optimality-preserving descent

Let `rho` be a pair-safe Hamilton cycle and let `e` attain its frustration
index:

```text
V_e(rho)=lambda(rho).
```

A successor rotation `rho -> rho^T` is **optimality preserving** when

```text
V_e(rho^T)=lambda(rho^T)<lambda(rho).
```

Thus the complete sign coordinate has Hamming change zero and remains globally
minimum after the cycle move.

### Theorem PP3bol -- VERIFIED FINITELY / TARGET-OPTIMAL FIXED-SIGN DESCENT

For every `5<=m<=9`, every pair-safe Hamilton cycle `rho` with
`lambda(rho)>0`, and every orientation vector `e` attaining `lambda(rho)`,
there is an optimality-preserving pair-safe successor rotation.

| `m` | optimal oriented states | target-optimal descent transitions | minimum choices from one state |
|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 |
| 8 | 93,980 | 1,642,058 | 5 |
| 9 | 977,312 | 24,730,616 | 4 |

The smaller transition totals than PP3bnz are intentional: PP3bnz only requires
`V_e(rho^T)<lambda(rho)`, whereas PP3bol additionally requires
`V_e(rho^T)=lambda(rho^T)`.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_hamilton_parity_frustration_sign_preserving_descent.cpp \
  -o /tmp/check_hamilton_parity_frustration_sign_preserving_descent
/tmp/check_hamilton_parity_frustration_sign_preserving_descent
```

The checker reconstructs every Hamilton cycle, every geometric pair predicate,
every minimum orientation, and every successor rotation.  It verifies target
optimality of the unchanged vector and compares every total with
`experiments/hamilton-parity-frustration-sign-preserving-descent-audit.json`. ∎

## 2. Every selected core edge can be cleared

Fix an optimal orientation `e` and one of its violated signed parity edges
`uv`.  A rotation **clears** this edge when its source triple meets `u` or `v`
and, on the target cycle with the same orientation, the new owner pair either
carries no XOR constraint or carries the satisfied XOR value.

### Theorem PP3bom -- VERIFIED FINITELY / TARGET-OPTIMAL MARKED CLEARING

For every audited optimal oriented state and every violated parity edge, there
is an optimality-preserving strict-descent rotation that clears the selected
edge.

| `m` | optimal violated-edge checks | clearing target-optimal descents | minimum choices for one edge |
|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 |
| 8 | 97,224 | 1,680,944 | 5 |
| 9 | 1,001,344 | 25,068,372 | 4 |

The move may alter other pair constraints, but the unchanged orientation is
still globally optimal on the target and the minimum violation count decreases.

## 3. Fixed-optimum finite termination

### Corollary PP3bon -- VERIFIED FINITELY / OPTIMUM PRESERVED THROUGHOUT

For `m<=9`, begin with a pair-safe cycle `rho_0` and any orientation `e`
attaining `lambda(rho_0)`.  Repeatedly apply PP3bol while keeping `e` fixed.
At every intermediate cycle the same vector remains optimal, and the process
reaches a pair-safe cycle on which `e` satisfies every parity edge in at most

```text
lambda(rho_0)
```

rotations, hence at most three rotations through `m=9`.

#### Proof

PP3bol keeps `e` optimal and strictly decreases its nonnegative violation
count.  PP3bng gives `lambda<=3` in the audited range. ∎

This strengthens the fixed-sign interface of `docs/331`: no recleaning is
needed, and the initial optimum remains an optimum throughout the complete
finite descent path.

## 4. Revised coupling frontier

The remaining tasks are:

1. prove an asymptotic target-optimal fixed-sign descent theorem;
2. determine whether a bounded local-sign analogue survives beyond `m=10`;
3. control merged predecessor charge for a distribution over target-optimal
   rotations;
4. include exact two-owner and three-owner atomic collateral in the move cost;
5. combine the target-optimal path with the logarithmic sparse parity seed.

The theorem is exhaustive finite evidence, not an asymptotic action theorem.
