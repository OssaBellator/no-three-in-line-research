# Sparse algebraic spread: irreducible pair/completion cores

This note follows the neutral-move cut-localization theorem. It replaces an arbitrary unpaid mixed terminal set by a canonical irreducible core whose every retained address has the same exact marginal shortfall.

## Complete finite network

Fix one finite integral physical-source/neutral-move/pair-completion network. Let `T` be the exact sign-pair and completion-task terminal set with integral demands `b_t`. For `X subseteq T`, let `nu(X)` be maximum payable flow when only terminals in `X` are active, and set `delta(X)=sum_(t in X)b_t-nu(X)`.

The sign-pair/completion type and every boundary-neutral move label remain part of the address.

## Theorem block SAS5ku--SAS5ky

1. `delta(X)` is a nonnegative integer, and deficiency is exactly `delta(X)>0`.
2. Choose a deficient subset of minimum cardinality, breaking ties by the complete terminal-address order. Call it `X_*`.
3. Every proper subset of `X_*` is fully payable.
4. For `x in X_*`, define `m_x=nu(X_*)-nu(X_* minus {x})`. Then

   `b_x-m_x=delta(X_*)`.

   Every retained sign-pair or completion address therefore carries the full mixed-core deficit against its exact marginal neutral-move capacity.
5. Omitting a legal pair, completion task, neutral move or physical source, merging demand types, or comparing different boundary states is a reset.

## Frontier consequence

The previous theorem returned physical-source and move barriers plus outside pair/completion demand. This theorem prunes that demand to a canonical minimum-cardinality core and reduces the remaining sparse-algebraic work to one exact local pair-or-completion inequality.

## Finite audit

Run `python scripts/verify_sas_irreducible_pair_completion_core.py`. The verifier enumerates all terminal subsets and checks the common-deficit marginal identity at every retained typed address.

## Scope

This does not prove SAS6 or the no-three-in-line conjecture.
