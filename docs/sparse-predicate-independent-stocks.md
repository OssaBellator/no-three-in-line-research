# Sparse algebraic predicate-independent stocks

## Status

This note proves SAS5no--SAS5nr under the rooted neutral Hall-cut and complete boundary-neutral witness contracts through SAS5nn. It does not construct the sparse predicates or witnesses, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

In the balanced neutral-key branch, a support-key root family has size `m`, and one named failed sparse predicate labels a graph `F_p` between those roots and outside neutral tokens with `e>=m^2/q` edges. Every edge has a least physical witness: a moved row or cell, swap position, arithmetic-profile field, orientation record, legality guard, boundary record, pair/completion slot, owner occurrence or lineage record.

## SAS5no -- retained sparse-predicate mass -- PROVED

The named predicate retains all `e>=m^2/q` failed pair/completion-token pairs for independent extraction.

## SAS5np -- sparse star or endpoint-disjoint matching -- PROVED

For any `D>=1`, either one pair/completion root or outside neutral token has predicate-failure degree at least `D+1`, or every endpoint degree is at most `D` and greedy selection gives a matching `M` with

\[
\boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

## SAS5nq -- neutral-witness overload or independent stock -- PROVED

For `mu>=1`, either one physical sparse witness labels at least `mu+1` edges of `M`, or choosing one edge per witness gives a stock `S` with distinct pair/completion roots, neutral tokens and physical witnesses and

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

## SAS5nr -- sparse-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One exact continuation holds: a degree-`D+1` failed-predicate star; a physical-witness overload; an endpoint- and witness-disjoint neutral stock; or an incomplete predicate/witness or lineage dictionary. If each distinct witness pays at least `rho` units of neutral, orientation or lineage credit, capacity-one charging gives total payment at least `rho|S|`. Extraction creates no neutral mass and changes no orientation payment.

## Corrected SAS6 frontier

The sparse obstruction is now a high-degree predicate star, a physical-witness overload, or an independent realized stock. Remaining work is to construct the move/legality/orientation witness dictionary and prove concrete `D,mu,rho` bounds.

## Finite check

`scripts/verify_sas_predicate_independent_stocks.py` checks predicate concentration, degree-star/matching extraction, witness overload and independent-stock bounds.