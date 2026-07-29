# Orbit phase: irreducible residual/edit cores

This note follows the residual-edit cut decomposition. It replaces an arbitrary unpaid mixed terminal set by a canonical irreducible core whose every retained address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral shared-source residual/edit network. Let `T` be the exact unit-sensitive residual and edit terminal set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only terminals in `X` are active, and set `delta(X)=sum_(t in X)b_t-nu(X)`.

The residual/edit type and all unit-sensitive labels remain part of every address.

## Theorem block OP4du--OP4dy

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Choose a deficient subset of minimum cardinality, breaking ties by the complete terminal-address order. Call it `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For `x in X_*`, define `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Every retained residual or edit address therefore carries the full mixed-core deficit against its exact marginal source capacity.
5. Omitting a unit field, merging residual and edit types, changing compatibility or comparing different quotient states is a reset.

## Frontier consequence

The previous theorem returned a source barrier and outside residual/edit demand. This theorem prunes that demand to a canonical minimum-cardinality core and reduces the remaining physical work to one exact local residual-or-edit source inequality.

## Finite audit

Run `python scripts/verify_op_irreducible_residual_edit_core.py`. The verifier enumerates all terminal subsets and checks the common-deficit marginal identity at every retained typed address.

## Scope

This does not prove OP5 or the no-three-in-line conjecture.
