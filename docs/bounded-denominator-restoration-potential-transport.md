# Bounded-denominator restoration-potential transport

This note records BDA5ed--BDA5eh. It converts the primitive integer gain account into a simultaneous payment problem for exact restoration classes.

## Contract

Let `S` be exact physical source-potential classes with current nonnegative integer capacities `k_s`. Let `R` be exact restoration classes with integer potential demands `d_r`. A complete compatibility graph records precisely which source-potential units may pay which restoration classes. The primitive integer vertex potential, occurrence lineage, arithmetic role, denominator, wall address and every legality field are retained.

## Theorem block

### BDA5ed — integral restoration graph

Create the capacitated bipartite network `source -> R -> S -> sink`, with restoration demand `d_r`, source capacity `k_s`, and infinite capacity on declared compatibility arcs.

### BDA5ee — exact Hall alternative

All restoration potential is paid if and only if every restoration subset `X` satisfies

`sum_{r in X} d_r <= sum_{s in N(X)} k_s`.

Equivalently, the maximum integral flow has value `sum_r d_r`.

### BDA5ef — threshold and dyadic bounds

If every restoration in a selected family costs at least `J`, the number paid is at most `floor(K/J)`, where `K=sum_s k_s`. More generally, each dyadic scale is bounded by the same transported integer-potential account.

### BDA5eg — canonical unpaid restoration cut

Failure returns the residual minimum restoration/source cut. Its deficit equals the unpaid primitive-potential mass, preserving exact restoration and source addresses.

### BDA5eh — reset boundary

Changed primitive weights, omitted compatibility, fractional or split occurrence lineage, source-less potential creation, arithmetic relabelling or unrecorded deposits return amplification/reset instead of payment.

## Proof

This is integral bipartite max-flow. Max-flow/min-cut is equivalent to the capacitated Hall inequalities. The threshold and dyadic statements follow by dividing total paid integer potential by the minimum cost of each selected restoration.

## Finite audit

Run `python scripts/verify_bda_restoration_potential_transport.py`.

The audit verifies max-flow against every restoration-subset Hall deficit on random finite systems.

## Scope

The theorem does not construct the physical compatibility graph or prove its capacities. It does not prove BDA6 or the no-three-in-line conjecture.