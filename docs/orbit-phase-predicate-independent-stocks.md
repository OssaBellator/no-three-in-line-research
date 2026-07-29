# Orbit-phase predicate-independent stocks

## Status

This note proves OP4go--OP4gr under the rooted phase-cut and complete unit-sensitive failure-witness contracts through OP4gn. It does not construct the phase predicates or witnesses, prove OP5, or prove the no-three-in-line conjecture.

## Setup

In the balanced quotient-key branch, a selected support-key root family has size `m`, and one named failed unit-sensitive predicate labels an edge set `F_p` between those roots and outside source tokens with `e>=m^2/q`. Every edge has a least physical witness: a quotient coordinate, residual/edit slot, action record, owner occurrence, unit/valuation field, holonomy record, carry field or boundary context.

## OP4go -- retained phase-predicate mass -- PROVED

The selected named predicate retains all `e>=m^2/q` failed root-source pairs for independent extraction.

## OP4gp -- phase star or endpoint-disjoint matching -- PROVED

For any `D>=1`, either one residual/edit root or outside source token has predicate-failure degree at least `D+1`, or every endpoint degree is at most `D` and greedy selection yields a matching `M` with

\[
\boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

## OP4gq -- phase-witness overload or independent stock -- PROVED

For `mu>=1`, either one physical phase witness labels at least `mu+1` edges of `M`, or choosing one edge for each witness gives a stock `S` with distinct residual/edit roots, source tokens and physical witnesses and

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

## OP4gr -- phase-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One exact continuation holds: a degree-`D+1` unit-sensitive failure star; a physical-witness overload; an endpoint- and witness-disjoint stock; or an incomplete predicate/witness dictionary. If each distinct witness pays at least `rho` units of source, residual, edit or holonomy credit, capacity-one charging gives total payment at least `rho|S|`. Matching extraction creates no source mass or edit credit.

## Corrected OP5 frontier

The phase obstruction is now a high-degree predicate star, a phase-witness overload, or an independent realized stock. Remaining work is to construct the physical phase witness dictionary and prove concrete `D,mu,rho` bounds.

## Finite check

`scripts/verify_op_predicate_independent_stocks.py` checks predicate concentration, degree-star/matching extraction, witness overload and independent-stock bounds.