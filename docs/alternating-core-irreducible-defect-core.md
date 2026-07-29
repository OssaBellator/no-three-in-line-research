# Alternating core: irreducible physical defect cores

This note follows the exact mixed-cut decomposition already proved on this branch. It replaces an arbitrary unpaid terminal set by a canonical irreducible core in which every retained address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical/source/certificate/defect network. Let `T` be its exact defect-address set and let `b_t` be the integral demand at `t`. For `X subseteq T`, let `nu(X)` be the maximum flow when only terminals in `X` are active, and put

`delta(X) = sum_(t in X) b_t - nu(X)`.

All internal capacities, compatibility edges, node splits and physical addresses are retained exactly.

## Theorem block AC5dm--AC5dq

1. `delta(X)` is a nonnegative integer. A set is deficient exactly when `delta(X)>0`.
2. If a deficient set exists, choose one of minimum cardinality, breaking ties by the fixed defect-address order. This gives a canonical irreducible core `X_*`.
3. Every proper subset of `X_*` is fully payable. In particular, `delta(X_* minus {x})=0` for every `x in X_*`.
4. Define the marginal payable capacity of `x` inside the core by `m_x=nu(X_*)-nu(X_* minus {x})`. Then every retained defect satisfies the exact identity

   `b_x - m_x = delta(X_*)`.

   Thus every retained address has demand at least the full core deficit, and the least address is already a local physical shortage witness.
5. Omitting compatibility, merging addresses, changing capacities or comparing different physical states is a reset, not a proved shortage.

## Why this advances AC5

The previous theorem returned an outside defect set and a finite physical/source/certificate barrier vector. This theorem prunes that outside set to a minimum-cardinality exact core and converts its global unpaid mass into a per-address marginal identity. The remaining physical task is to exclude or pay that exact local shortage.

## Finite audit

Run `python scripts/verify_ac_irreducible_defect_core.py`.

The verifier enumerates every terminal subset in each sampled layered network, selects the canonical minimum-cardinality deficient core, checks all proper subsets, and verifies the marginal identity at every retained address.

## Scope

This is a finite network theorem under the complete-address contract. It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.
