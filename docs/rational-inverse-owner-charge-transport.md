# Rational-inverse owner charge transport

This note records RI5da--RI5de. It composes owner-local compatibility-deletion charges with a finite exact collateral payment graph.

## Contract

Let `O` be the finite exact owner dictionary and `S` a finite dictionary of deletion-collateral sources. Each owner `o` has nonnegative integer perturbation charge `q_o`; each source `s` has finite capacity `c_s`; and a complete compatibility graph records which sources may pay which owner charges. Charges retain owner, secant, root, host and coherence identity.

## Theorem block

### RI5da — charge transportation

Owner charges and source capacities form an integral bipartite transportation problem. The maximum paid charge is attained by an integral flow.

### RI5db — Hall criterion

All perturbation charge is paid exactly when every owner subset `X` satisfies

`sum_{o in X} q_o <= sum_{s in N(X)} c_s`.

### RI5dc — perturbation composition

If the charge transport is complete, the actual owner-collateral deficit is bounded by the reference deficit with no unpaid compatibility-deletion term.

### RI5dd — deficient charge cut

If full charge payment fails, the least owner subset maximizing

`sum_{o in X} q_o - sum_{s in N(X)} c_s`

is a canonical unpaid owner-charge cut. Its positive value is exactly the minimum unpaid charge.

### RI5de — reset boundary

Omitted compatibility arcs, duplicated collateral capacity, changed owner/coherence labels, negative charge cancellation, or unrecorded source replenishment return reset.

## Proof

This is the integral max-flow/min-cut theorem on the owner/source network. The cut formula is the capacitated Hall deficit. RI5dc follows by substituting full payment into the owner-local deletion-charge bound.

## Remaining physical work

The result leaves the arithmetic construction of the owner/source compatibility graph, the source capacities and the local deletion charges open.