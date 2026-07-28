# Local-sign-coupled parity repair through `m=10`

`docs/327` proves cycle-level frustration descent through `m=9`, and `docs/329`
proves that every pair-safe `m=10` cycle is one successor rotation from a clean
cycle. Those results allow global parity reoptimization after the cycle move.
This chapter audits the stronger signed-state interface: keep all unrotated owner
signs fixed, and change signs only on the three owners whose outgoing targets are
rotated.

No asymptotic repair, charge, or seed theorem is claimed.

## 1. Fixed-orientation descent through `m=9`

Fix a pair-safe Hamilton cycle `rho` and an orientation vector `e` attaining its
frustration index `lambda(rho)`. For a source triple `T`, let `rho^T` be the
successor rotation. Evaluate the target parity constraints using the *same*
orientation vector `e`.

### Theorem PP3bnz -- VERIFIED FINITELY / ZERO-SIGN-CHANGE DESCENT

For every `5<=m<=9`, every pair-safe cycle with positive frustration, and every
orientation attaining `lambda(rho)`, there is a pair-safe successor rotation
`rho^T` such that

```text
violations(rho^T,e) < lambda(rho).
```

Thus no orientation bit needs to change. The exact counts are:

| `m` | optimal positive signed states | fixed-orientation descending rotations | minimum choices per state |
|---:|---:|---:|---:|
| 5 | 48 | 244 | 3 |
| 6 | 272 | 2,596 | 5 |
| 7 | 2,752 | 37,020 | 6 |
| 8 | 93,980 | 1,674,032 | 5 |
| 9 | 977,312 | 25,073,346 | 4 |

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_frustration_fixed_orientation.cpp \
  -o /tmp/check_hamilton_parity_frustration_fixed_orientation
/tmp/check_hamilton_parity_frustration_fixed_orientation
```

The checker reconstructs every pair-safe cycle, all minimum orientations, every
successor rotation, and the target violation count with the source orientation
held fixed. It compares the complete totals with
`experiments/hamilton-parity-frustration-fixed-orientation-audit.json`. ∎

## 2. Every marked violated edge remains targetable

### Theorem PP3boa -- VERIFIED FINITELY / FIXED-SIGN MARKED DESCENT

In the range `5<=m<=9`, fix any minimum orientation and any parity edge violated
by it. There is a fixed-orientation strict-descent rotation whose source triple
meets an endpoint of that edge.

The audit contains `1,101,640` marked violated-edge instances. The minimum
number of fixed-orientation targeted descents is respectively

```text
m=5:3,  m=6:5,  m=7:6,  m=8:5,  m=9:4.
```

Hence the cycle move can replace an assignment supporting any selected member of
the minimum frustration core without changing signs. ∎

## 3. The first fixed-sign exceptions occur at `m=10`

### Theorem PP3bob -- VERIFIED FINITELY / FIXED-SIGN TRANSITION

At `m=10`, among `12,786,720` optimal positive-frustration signed states,
exactly `74` have no direct clean successor rotation preserving the complete
orientation vector. Among `13,185,264` marked optimal violated-edge instances,
exactly `218` have no fixed-sign direct clean rotation meeting the marked edge.

Thus the zero-sign-change statement is genuine through `m=9` but not universal.
The first failure coincides with the first audited size containing satisfiable
nonforest parity graphs.

#### Verification

The `m=10` checker stores the complete clean-orientation mask of every target
cycle and tests each minimum source orientation against every direct clean
rotation. ∎

## 4. Two local sign changes suffice at `m=10`

For a rotation on source triple `T`, call a target orientation **locally coupled**
when it agrees with the source orientation outside `T`.

### Theorem PP3boc -- VERIFIED FINITELY / LOCAL THREE-OWNER REPAIR

Every optimal positive-frustration signed state at `m=10` has a direct clean
successor rotation with a locally coupled target orientation. The minimum
Hamming-change distribution is

```text
0 changed signs: 12,786,646 states,
1 changed sign:          70 states,
2 changed signs:          4 states,
3 changed signs:          0 states.
```

Every state has at least one such rotation, and the maximum necessary Hamming
change is two.

### Theorem PP3bod -- VERIFIED FINITELY / LOCALLY COUPLED MARKED REPAIR

For every minimum source orientation and every selected violated parity edge,
there is a direct clean rotation meeting an endpoint of the selected edge and a
clean target orientation that changes at most two signs, all inside the rotated
source triple.

The minimum number of locally coupled targeted choices is one. No one of the
`13,185,264` marked edge instances fails.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_m10_local_sign_coupling.cpp \
  -o /tmp/check_hamilton_m10_local_sign_coupling
/tmp/check_hamilton_m10_local_sign_coupling
```

For each direct clean target, the checker exhausts the eight sign patterns on the
rotated triple while freezing all other signs. The exact ledger is
`experiments/hamilton-m10-local-sign-coupling-audit.json`. ∎

## 5. Revised parity-preprocessing frontier

Through the first nonforest size, parity preprocessing has a bounded local signed
implementation:

```text
m<=9:  one descending rotation, zero sign changes;
m=10:  one clean rotation, at most two sign changes on its source triple.
```

The remaining asymptotic work is now sharper:

1. prove a bounded local-sign repair theorem for the `O(log m)` frustration core;
2. lower-bound the number of locally coupled choices meeting each marked edge;
3. control predecessor charge for a distribution over those choices;
4. couple the local sign update to atomic three-owner collateral and the
   trajectory-local light cone;
5. determine whether the required local Hamming width remains bounded when clean
   parity graphs have higher cyclomatic rank.

The finite result does not prove that local coupling has stationary-scale charge
or negative atomic-flaw drift.
