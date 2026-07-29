# Superregular higher-order conflict shadow

This note records SRR2bg--SRR2bk.  It extends pairwise conflict thinning to a complete finite hypergraph of higher-order switching conflicts by using a conservative clique shadow.

## Contract

Let `V` be weighted switching candidates and let `H` be a complete family of conflict hyperedges.  A certified executable family may contain at most one vertex from every `e in H`.  Hyperedges have finite rank and every omitted interaction is treated as reset.

Construct the shadow graph `G` by joining two candidates whenever they occur together in some conflict hyperedge.

## Results

### SRR2bg — shadow safety

Every independent set of `G` contains at most one candidate from each conflict hyperedge and is therefore executable under the hypergraph contract.

### SRR2bh — local degree bound

For every candidate `v`,

`deg_G(v) <= sum_{e contains v} (|e|-1)`.

Repeated shadow neighbors only improve this bound.

### SRR2bi — weighted executable family

There is an executable family of weight at least

`sum_v w_v/(deg_G(v)+1)`

and hence at least

`sum_v w_v/[1+sum_{e contains v}(|e|-1)]`.

### SRR2bj — uniform rank/load corollary

If every hyperedge has size at most `q` and every candidate lies in at most `Delta_H` hyperedges, at least a fraction

`1/[1+(q-1)Delta_H]`

of total candidate weight is executable.

### SRR2bk — composition with endpoint thresholds

Apply the shadow construction inside each low-cost threshold family from SRR2bb--SRR2bf.  Failure now identifies either a threshold transport deficit, a heavy exact conflict hyperedge/atom, or an omitted-interaction reset.

## Proof

A shadow-independent set cannot contain two vertices from one hyperedge.  Each incident hyperedge contributes at most `|e|-1` possible shadow neighbors of `v`, proving the degree bound.  The weighted random-priority/local-minimum argument on `G` gives the stated independent-set weight.

## Finite audit

Run:

`python scripts/verify_srr_higher_order_conflict_shadow.py`

The deterministic audit checks:

- 3,500 conflict systems;
- 22,676 candidates;
- 19,408 conflict hyperedges;
- 12,355 genuinely higher-order hyperedges;
- 38,577 shadow edges;
- 113,489 candidate-weight units;
- 3,500 brute-force weighted checks.

## Scope

The clique shadow is deliberately stronger than merely forbidding a complete hyperedge.  The theorem does not construct the concrete geometric conflict hypergraph or prove its rank and incidence bounds.  Interactions not represented by the retained hyperedges return reset.  SRR2, SRR4 and the no-three-in-line conjecture remain open.
