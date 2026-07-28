# Geometric cleaning: irreducible cause cores

This note follows the physical remedy-height cut theorem. It replaces an arbitrary unpaid outside cause set by a canonical irreducible core in which every retained cause has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical/remedy/height/cause network. Let `T` be the exact cause-address set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only causes in `X` are active, and define `delta(X)=sum_(t in X)b_t-nu(X)`.

## Theorem block GC2jv--GC2jz

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Choose a deficient set of minimum cardinality, breaking ties by the complete cause-address order. Call it `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For each `x in X_*`, put `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Thus every retained cause carries the full core deficit against its exact marginal physical/remedy/height capacity.
5. Omitting a remedy or height edge, merging causes, changing height costs or comparing different cleaning states is a reset.

## Frontier consequence

The previous theorem returned an outside cause set and separate physical, remedy and height barriers. This theorem prunes that set to a canonical minimum-cardinality core and reduces the remaining geometric work to one exact local cause-capacity inequality.

## Finite audit

Run `python scripts/verify_gc_irreducible_cause_core.py`. The verifier enumerates all terminal subsets, checks every proper subset of the selected core, and verifies the exact marginal identity.

## Scope

This does not prove GC5 or the no-three-in-line conjecture.
