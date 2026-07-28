# Sign-preserving parity-frustration descent through `m=9`

`docs/327` proves that the pair-safe Hamilton-cycle coordinate has immediate
strict descent for the frustration index through `m=9`, but it reoptimizes the
orientation vector after every rotation. This chapter removes that
reoptimization in the complete audited range.

The result is finite. It does not prove asymptotic descent, weighted action
charge, or a no-three-in-line seed theorem.

## 1. Oriented frustration states

Let `rho` be a pair-safe Hamilton cycle and let `e` be an orientation vector
attaining its frustration index:

```text
V_e(rho)=lambda(rho).
```

A successor rotation `rho -> rho^T` is **sign preserving** when the identical
vector `e` is retained on the target cycle. It is an optimal sign-preserving
descent when

```text
V_e(rho^T)=lambda(rho^T)<lambda(rho).
```

Thus the cycle coordinate changes while the complete sign coordinate has
Hamming change zero.

## 2. Exact zero-Hamming coupling

### Theorem PP3bnl -- VERIFIED FINITELY / SIGN-PRESERVING STRICT DESCENT

For every `5<=m<=9`, every pair-safe Hamilton cycle `rho` with
`lambda(rho)>0`, and every orientation vector `e` attaining `lambda(rho)`,
there is a pair-safe successor rotation `rho -> rho^T` such that

```text
V_e(rho^T)=lambda(rho^T)<lambda(rho).
```

No orientation bit changes. The exact audited counts are:

| `m` | optimal oriented states | sign-preserving descent transitions | minimum choices from one optimal state |
|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 |
| 8 | 93,980 | 1,642,058 | 5 |
| 9 | 977,312 | 24,730,616 | 4 |

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_hamilton_parity_frustration_sign_preserving_descent.cpp \
  -o /tmp/check_hamilton_parity_frustration_sign_preserving_descent
/tmp/check_hamilton_parity_frustration_sign_preserving_descent
```

The checker reconstructs every Hamilton cycle, every geometric pair predicate,
every minimum orientation, and every successor rotation. It verifies that the
same orientation remains minimum on at least one lower-frustration pair-safe
target. All counts are compared with hard-coded regression values and the JSON
output is stored in
`experiments/hamilton-parity-frustration-sign-preserving-descent-audit.json`. ∎

## 3. Every selected core edge can be cleared

Fix an optimal orientation `e` and one of its violated signed parity edges
`uv`. Say that a rotation **clears** this edge when its source triple meets
`u` or `v` and, on the target cycle with the same orientation, the new owner
pair either carries no XOR constraint or carries the satisfied XOR value.

### Theorem PP3bnm -- VERIFIED FINITELY / TARGETED CLEARING DESCENT

For every audited optimal oriented state and every violated parity edge, there
is a pair-safe sign-preserving strict-descent rotation that clears the selected
edge.

| `m` | optimal violated-edge checks | clearing descent transitions | minimum clearing choices for one edge |
|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 |
| 8 | 97,224 | 1,680,944 | 5 |
| 9 | 1,001,344 | 25,068,372 | 4 |

The clearing transition may create or alter other constraints, but the same
orientation is still globally optimal on the target and the total minimum
violation count decreases.

#### Verification

For each minimum orientation, the checker lists every violated edge, filters to
rotations meeting one endpoint, tests the target pair predicate explicitly,
and verifies both clearing and target optimality with the unchanged bit vector. ∎

## 4. Fixed-orientation finite termination

### Corollary PP3bnn -- VERIFIED FINITELY / NO RECLEANING REQUIRED

For `m<=9`, begin with a pair-safe cycle `rho_0` and any orientation `e`
attaining `lambda(rho_0)`. Repeatedly apply PP3bnl while keeping `e` fixed.
The process reaches a pair-safe cycle on which `e` satisfies every parity edge
in at most

```text
lambda(rho_0)
```

rotations, hence in at most three rotations through `m=9`.

#### Proof

At every step the unchanged vector remains optimal and its violation count
strictly decreases. PP3bng gives `lambda<=3` in the audited range. ∎

This is stronger than the reoptimized termination policy PP3bnk: neither
nearest recleaning nor complete fibre regeneration is needed for the finite
parity descent itself.

## 5. Revised coupling frontier

The orientation-coordinate coupling problem is closed through `m=9`. The
remaining work is now:

1. prove an asymptotic sign-preserving pair-safe descent theorem;
2. control the distribution and merged predecessor charge of the many useful
   rotations;
3. compare parity-edge descent with exact atomic two-owner and three-owner flaw
   potentials;
4. determine whether the minimum number of sign-preserving choices remains
   polynomially large;
5. combine fixed-sign descent with the logarithmic sparse parity seed from
   PP3bnf.

The theorem is exhaustive finite evidence, not an asymptotic action theorem.
