# Superregular resampling: irreducible burden cores

This note follows the geometric atom-cut extraction theorem. It replaces an arbitrary unpaid outside burden set by a canonical irreducible core in which every retained burden address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical-source/atom/burden network. Let `T` be the exact witnessed burden-address set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only burdens in `X` are active, and define `delta(X)=sum_(t in X)b_t-nu(X)`.

## Theorem block SRR2de--SRR2di

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Choose a deficient set of minimum cardinality, breaking ties by the complete burden-address order. Call it `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For each `x in X_*`, put `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Every retained witnessed burden therefore carries the full core deficit against its exact marginal physical-source/atom capacity.
5. Omitting a conflict, witness atom or source edge, merging burden addresses, or comparing different conditioned thresholds is a reset.

## Frontier consequence

The previous theorem returned outside burden and physical-source/atom barriers. This theorem prunes that burden to a canonical minimum-cardinality core and reduces the geometric task to one exact local witnessed-burden inequality.

## Finite audit

Run `python scripts/verify_srr_irreducible_burden_core.py`. The verifier enumerates all terminal subsets, checks every proper subset of the selected core, and verifies the exact marginal identity.

## Scope

This does not prove SRR2, SRR4 or the no-three-in-line conjecture.
