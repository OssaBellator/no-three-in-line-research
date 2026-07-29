# Rational inverse: irreducible owner/charge cores

This note follows the exact owner-charge cut-address theorem. It replaces an arbitrary unpaid mixed terminal set by a canonical irreducible core whose every retained address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical-source/collateral/owner-charge network. Let `T` be the exact owner and perturbation-charge terminal set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only terminals in `X` are active, and set `delta(X)=sum_(t in X)b_t-nu(X)`.

The owner/charge type is retained on every address and may not be aggregated away.

## Theorem block RI5eo--RI5es

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Choose a deficient subset of minimum cardinality, breaking ties by the complete terminal-address order. This canonical set is `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For every `x in X_*`, define `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Each retained owner or charge address therefore carries the full mixed-core deficit against its exact marginal collateral capacity.
5. Omitting compatibility, suppressing the owner/charge type, merging physical sources, changing retained fields or comparing different arithmetic states is a reset.

## Frontier consequence

The previous cut theorem returned physical and collateral barriers plus outside owner/charge mass. The present theorem prunes that set to a canonical minimum-cardinality core and turns the global unpaid mass into one exact local owner-or-charge inequality.

## Finite audit

Run `python scripts/verify_ri_irreducible_owner_charge_core.py`. The verifier enumerates all terminal subsets and checks the common-deficit marginal identity at every retained typed address.

## Scope

This does not prove RI6 or the no-three-in-line conjecture.
