# Rational-inverse predicate-independent stocks

## Status

This note proves RI5hi--RI5hl under the rooted Hall-cut and complete physical failure-witness contracts through RI5hh. It does not construct the arithmetic predicates or witnesses, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Use the balanced-key branch of RI5hg--RI5hh. A support-key root family `U` has size `m`; outside collateral tokens form `Y`; every pair in `U x Y` is a nonedge. One named predicate `p` labels a set `F_p` with

\[
 e:=|F_p|\ge m^2/q.
\]

Each edge of `F_p` carries a least physical failure witness: an owner occurrence, blocker slot, arithmetic certificate, boundary record, charge resource or other retained predicate witness.

## RI5hi -- predicate edge concentration -- PROVED

The named failure graph `F_p` has at least `m^2/q` edges. Hence one root has predicate-failure degree at least `ceil(m/q)`, recovering RI5hh, and the full edge mass remains available for independent extraction.

## RI5hj -- high-degree star or endpoint-disjoint matching -- PROVED

Fix an integer `D>=1`. Exactly one continuation holds:

1. one root or outside token has `F_p`-degree at least `D+1`, yielding an explicit failed-predicate star; or
2. every endpoint degree is at most `D`, and greedy edge selection gives a matching `M` with
   \[
   \boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
   \]

Each selected edge deletes at most `2D-1` remaining edges: at most `D` at each endpoint, with the selected edge counted twice.

## RI5hk -- witness overload or independent realized stock -- PROVED

Fix `mu>=1`. On the matching `M`, either one physical failure witness labels at least `mu+1` matched pairs, giving a witness overload, or every witness has multiplicity at most `mu`. In the latter case, choose one matched pair for each witness. The resulting stock `S` has distinct roots, distinct outside tokens and distinct physical witnesses, and

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

Thus in the dense rooted rectangle,

\[
|S|\ge\left\lceil\frac{m^2}{q(2D-1)\mu}\right\rceil
\]

with the outer ceiling interpreted through the integer edge bound.

## RI5hl -- predicate-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One exact continuation holds:

1. a failed-predicate star of degree at least `D+1` is returned;
2. one physical failure witness is overloaded on at least `mu+1` endpoint-disjoint pairs;
3. an endpoint-disjoint, witness-disjoint stock of the displayed size is returned;
4. one nonedge lacks a named predicate or physical witness, so the dictionary is incomplete.

If every realized stock edge pays at least `rho` units through its distinct witness, capacity-one charging gives total payment at least `rho|S|`. No collateral mass is created by the extraction.

## Corrected RI6 frontier

The residual RI obstruction is now either a high-degree predicate star, a physical-witness overload, or a capacity-one independent stock. Remaining work is to build the actual witness dictionary, prove useful `D,mu,rho` bounds, and discharge the star and overload branches.

## Finite check

`scripts/verify_ri_predicate_independent_stocks.py` checks predicate concentration, the degree-star/matching dichotomy, the greedy bound, witness overload, and endpoint- and witness-distinct extraction.