# Frontier pass: exact switch-symmetry quotient

## Active branch

`agent/ac-switch-symmetry-quotient`

Parent: `agent/ac-p31-three-triple-frontier` at `825b5b5be23fd448425f8117d3ebaa9cf56c97c7`.

Only AC is active. Historical side branches remain immutable source libraries.

## New theorem block

- **AC5ob:** the order-16 square-symmetry/layer-swap group acts by automorphisms of the physical two-permutation switch graph.
- **AC5oc:** lexicographic canonicalization gives a complete idempotent orbit key.
- **AC5od:** physical reachability to any invariant target is equivalent to quotient reachability, and quotient paths lift.
- **AC5oe:** canonical breadth-first exhaustion is an exact lower-obstruction certificate.

## Deterministic audit

The committed verifier exhausts the `n=5` ordered disjoint state space:

- ordered disjoint states: `5,280`;
- canonical checks: `5,280`;
- orbit images: `79,936`;
- transformed edge checks: `36,000`;
- raw/quotient reachability checks: `16`;
- raw component-state sum: `76,224`;
- quotient component-state sum: `5,234`.

All assertions pass.

## Logical gain

The exact `p=31` low-potential search no longer needs to enumerate every board-symmetric copy of a state. Exhausting the quotient component proves raw exhaustion for potential-defined targets. A found quotient route can be lifted by transporting each physical edge through the group element relating the current lift to the stored representative.

Intermediate quotient queue sizes remain audit progress only; no barrier theorem is claimed before the component either exhausts or returns a lower orbit.

## Files

- `docs/alternating-core-switch-symmetry-quotient.md`
- `scripts/verify_ac_switch_symmetry_quotient.py`
- `proofs/frontier-ac-switch-symmetry-quotient.md`

## Remaining AC frontier

1. Finish the `p=31` three-triple quotient search inside barrier nine.
2. Continue at the least larger barrier only if the lower component exhausts.
3. Add transform-labelled predecessor edges for compact lifted-path certificates.
4. Reuse the quotient at the two-, one- and zero-triple checkpoints.
5. Keep physical owner, source, ticket and reset records outside the quotient unless the symmetry acts on their complete addresses.

AC6 and the general no-three-in-line conjecture remain open.
