# RI terminal-profile signature transportation

This note compresses exact terminal blocker/profile demands before the owner-collateral transportation theorem. It does not prove RI6 or the no-three-in-line conjecture.

## Complete profile demand

Fix the retained owner, coherence, host, context, and arithmetic fields. Every exact terminal profile `p` has:

- an integer symmetric demand `d_p>=0`; and
- a complete compatible owner-collateral neighbourhood `N(p)`.

All physical profiles with the same retained fields and the same neighbourhood are transport-equivalent.

## Signature quotient

Define the signature of `p` to be `N(p)`. Aggregate all demands with one signature:

`D_S = sum_{p:N(p)=S} d_p`.

With `O` retained owner-collateral classes, there are at most `2^|O|` signatures, or `Q 2^|O|` after adjoining a finite retained label set of size `Q`.

## Exact preservation

Replacing all profiles of signature `S` by one demand node of weight `D_S` preserves:

1. the maximum integral owner-collateral flow;
2. the unpaid symmetric demand;
3. the maximum capacitated Hall deficit;
4. the existence of a full payment.

Indeed, profiles in one signature class have identical outgoing arcs, so every feasible flow can be summed within the class and every quotient flow can be distributed among its members up to their demands.

## Canonical deficient signature cut

If full payment fails, the quotient returns a least signature subset `A` with

`sum_{S in A} D_S > capacity(N(A))`.

Its inverse image is an exact deficient terminal-profile/owner-collateral cut. Thus blocker-profile multiplicity does not create a new recurrence state once the complete compatibility signature is retained.

## Outside the contract

A change in owner, coherence, host, context, unit-sensitive arithmetic, or compatibility neighbourhood is a reset. The quotient does not merge profiles whose physical payment arcs differ, even when their unlabelled geometry agrees.
