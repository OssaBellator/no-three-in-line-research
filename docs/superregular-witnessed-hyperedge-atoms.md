# Superregular witnessed hyperedge atoms

This note records SRR2bl--SRR2bp. It converts a complete higher-order conflict dictionary into a local atom-incidence target.

## Contract

Let `H` be the complete conflict hypergraph of feasible switching candidates. Every hyperedge `e` has a retained witness atom `a(e)` that belongs to every candidate in `e`. Candidate `v` has an exact atom support `S_v`.

Define the witnessed load

`M(v,a) = sum { |e|-1 : v in e and a(e)=a }`.

No conflict hyperedge may be omitted or assigned to an atom absent from one of its vertices.

## Theorem block SRR2bl--SRR2bp

1. The clique-shadow degree of candidate `v` is at most
   `sum_{a in S_v} M(v,a)`.
2. If `|S_v|<=r` and `M(v,a)<=M`, then the shadow degree is at most `rM`.
3. A shadow-independent family uses at most one candidate from every conflict hyperedge.
4. Hence a weighted executable family has weight at least
   `W/(1+rM)`.
5. Excess witnessed load returns one exact candidate/atom pair; an unwitnessed conflict returns a dictionary reset.

The degree bound may overcount neighbours appearing in several witnessed hyperedges, which is favourable.

## Consequence

The remaining geometric task is not to bound an abstract higher-order conflict degree directly. It is enough to construct the complete witness-atom map and bound `M(v,a)` locally.

## Finite audit

Run:

`python scripts/verify_srr_witnessed_hyperedge_atoms.py`

The audit generates witnessed conflict hypergraphs, verifies the shadow-degree bound and brute-forces the executable weighted optimum.

## Scope

This theorem assumes a complete hypergraph and valid witness atoms. It does not construct the geometric dictionary or prove SRR2, SRR4 or the global conjecture.
