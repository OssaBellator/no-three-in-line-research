# Bounded-denominator predicate-independent stocks

## Status

This note proves BDA5hr--BDA5hu under the rooted restoration-cut and complete physical witness contracts through BDA5hq. It does not construct the rational-gain predicates or witnesses, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

In the balanced restoration-key branch, a selected support-key root family has size `m`, and one named failed predicate labels a graph `F_p` between those roots and outside potential tokens with `e>=m^2/q` edges. Every such edge has a least physical witness: a restoration gate, source occurrence, gain/damping field, line record, owner occurrence, arithmetic certificate or boundary resource.

## BDA5hr -- retained predicate edge mass -- PROVED

The selected named predicate carries at least `m^2/q` failed root-token pairs. This full edge mass, not only one high-degree root, is retained for independent extraction.

## BDA5hs -- restoration star or endpoint matching -- PROVED

For any integer `D>=1`, either one endpoint has predicate-failure degree at least `D+1`, or every endpoint degree is at most `D` and greedy selection gives an endpoint-disjoint matching `M` with

\[
\boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

Each selected edge removes at most `2D-1` edges incident with its two endpoints.

## BDA5ht -- witness overload or realized independent stock -- PROVED

Fix `mu>=1`. Either one physical restoration witness labels at least `mu+1` edges of `M`, or choosing one edge per witness gives a stock `S` with distinct repair incidences, distinct potential tokens and distinct physical witnesses, satisfying

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

## BDA5hu -- restoration-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One exact continuation holds: a degree-`D+1` failed-predicate star; a witness overload of multiplicity `mu+1`; an endpoint- and witness-disjoint stock of the displayed size; or an incomplete predicate/witness dictionary. If each distinct witness realizes at least `rho` potential payment, capacity-one charging gives total payment at least `rho|S|`. Matching extraction creates no gain or potential mass.

## Corrected BDA6 frontier

The restoration obstruction is now a high-degree predicate star, a physical-witness overload, or an independent realized stock. Remaining work is to build the physical witness dictionary and prove useful `D,mu,rho` bounds.

## Finite check

`scripts/verify_bda_predicate_independent_stocks.py` checks the degree-star/matching dichotomy, matching bound, witness overload and distinct-stock extraction.