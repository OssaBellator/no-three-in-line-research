# Bounded denominators: irreducible restoration-potential cores

This note follows the exact restoration-cut decomposition. It replaces an arbitrary unpaid terminal set by a canonical irreducible core in which every retained restoration address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical-potential/source/restoration network. Let `T` be the exact restoration-address set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only `X` is active, and define `delta(X)=sum_(t in X)b_t-nu(X)`.

## Theorem block BDA5ex--BDA5fb

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Among all deficient subsets choose one of minimum cardinality, breaking ties by the fixed restoration-address order. Call it `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For `x in X_*`, put `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Every retained restoration address therefore carries the full core deficit against its exact marginal primitive-potential capacity.
5. Omitting an arithmetic compatibility edge, changing a primitive weight, merging source addresses or comparing different gain states is a reset.

## Frontier consequence

The earlier theorem returned outside restoration demand and physical/source barriers. This theorem prunes it to a canonical minimum-cardinality arithmetic core and reduces payment to one exact local marginal-potential inequality.

## Finite audit

Run `python scripts/verify_bda_irreducible_restoration_core.py`. The verifier enumerates all terminal subsets, checks every proper subset of the selected core, and verifies the exact marginal identity.

## Scope

This does not prove BDA6 or the no-three-in-line conjecture.
