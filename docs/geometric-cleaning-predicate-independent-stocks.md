# Geometric-cleaning predicate-independent stocks

## Status

This note proves GC2mp--GC2ms under the rooted donor-cut and complete geometric witness contracts through GC2mo. It does not construct the geometric predicates or witnesses, prove GC5, or prove the no-three-in-line conjecture.

## Setup

In the balanced geometric-key branch, a support-key root family of size `m` and outside donor set determine a missing rectangle. One named failed geometric predicate labels an edge set `F_p` of size `e>=m^2/q`. Every edge carries a least physical witness: a moved cell, protected event, chart coefficient/root record, donor occurrence, remedy slot, height certificate or boundary record.

## GC2mp -- retained geometric predicate mass -- PROVED

The named predicate retains all `e>=m^2/q` failed remedy-donor pairs for independent extraction.

## GC2mq -- geometric star or endpoint matching -- PROVED

For `D>=1`, either one remedy root or outside donor has failure degree at least `D+1`, or every endpoint degree is at most `D` and greedy selection produces a matching `M` with

\[
\boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

## GC2mr -- witness overload or independent donor stock -- PROVED

For `mu>=1`, either one physical geometric witness labels at least `mu+1` matched pairs, or choosing one pair per witness gives a stock `S` with distinct remedies, donors and witnesses and

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

## GC2ms -- geometric-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One continuation holds: a degree-`D+1` failed-predicate star; a witness overload; an endpoint- and witness-disjoint stock; or an incomplete predicate/witness dictionary. If each distinct witness pays at least `rho` units of donor/remedy or protected-height credit, capacity-one charging gives at least `rho|S|` total payment. Extraction creates no donor mass and changes no height ledger.

## Corrected GC5 frontier

The cleaning obstruction is now a high-degree geometric star, a physical witness overload, or an independent realized stock. Remaining work is to construct chart/protected-event witnesses and prove concrete `D,mu,rho` bounds.

## Finite check

`scripts/verify_gc_predicate_independent_stocks.py` checks the degree, matching, witness-overload and independent-stock bounds.