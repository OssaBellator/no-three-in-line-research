# Alternating-core predicate-independent stocks

## Status

This note proves AC5gl--AC5go under the synchronized rooted-cut contracts through AC5gk and the six side-track predicate-stock contracts. It does not construct the physical witness dictionaries, prove AC6, or prove the no-three-in-line conjecture.

## Setup

A positive synchronized deficit selects one typed support-key triple `(s,x,k)` with `m` unmatched roots. In the balanced-key branch, one named predicate `p` labels a missing-pair graph `F_{s,x,k,p}` with

\[
 e\ge m^2/q_s,
\]

where `q_s` is the retained predicate count on track `s`. Every labeled pair has a least physical failure witness of the same track type.

## AC5gl -- synchronized predicate-edge retention -- PROVED

The selected track, support, key and predicate retain the entire edge mass `e>=m^2/q_s`; no cross-track or cross-key nonedge is used.

If `delta` is the synchronized deficit and `M` typed support-key triples occur among unmatched roots, then

\[
m\ge\left\lceil\frac{\delta}{M}\right\rceil.
\]

## AC5gm -- typed star or endpoint-disjoint matching -- PROVED

Fix `D>=1` for the selected track predicate. Either one incidence root or outside token has failed-predicate degree at least `D+1`, or every endpoint degree is at most `D` and greedy edge selection gives a matching `N` with

\[
\boxed{|N|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

The matching lies entirely inside one track-key component.

## AC5gn -- typed witness overload or independent realized stock -- PROVED

Fix `mu>=1`. Either one physical witness labels at least `mu+1` edges of `N`, or choosing one edge per witness yields a stock `S` with distinct incidence roots, distinct tokens and distinct typed physical witnesses, satisfying

\[
\boxed{|S|\ge\left\lceil\frac{|N|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

Consequently the selected component has a stock on the scale

\[
\frac{1}{q_s(2D-1)\mu}
\left\lceil\frac{\delta}{M}\right\rceil^2,
\]

with the rigorous bound taken through the preceding integer inequalities.

## AC5go -- synchronized independent-stock router -- PROVED UNDER THE PAYMENT CONTRACTS

One exact continuation holds:

1. every repair assignment is complete;
2. one track-key has a direct numerical token shortfall;
3. one selected track predicate has a degree-`D+1` failure star;
4. one typed physical witness is overloaded on at least `mu+1` endpoint-disjoint pairs;
5. one track returns an endpoint- and witness-disjoint stock of the displayed size;
6. one support, key, predicate, witness, epoch, occurrence, source-ledger or cross-track contract fails.

If each selected witness on track `s` pays at least `rho_s`, capacity-one charging gives at least `rho_s|S|` payment. The stock cannot cancel resources across tracks because all vertices and witnesses have one fixed track type.

## Corrected AC6 frontier

The residual synchronized obstruction is now a numerical shortage, a high-degree predicate star, a typed witness overload, or a capacity-one independent stock. Remaining work is to construct each physical witness dictionary, prove useful degree/multiplicity/payment constants, and convert the star and overload branches into descent, reset or replenishment.

## Finite check

`scripts/verify_ac_predicate_independent_stocks.py` generates synchronized typed rectangles and checks support-key concentration, predicate mass, star/matching extraction, typed witness overload and independent-stock bounds.