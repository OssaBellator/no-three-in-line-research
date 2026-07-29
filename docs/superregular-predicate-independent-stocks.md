# Superregular predicate-independent stocks

## Status

This note proves SRR2fy--SRR2gb under the rooted conditioned Hall-cut and complete witness-failure contracts through SRR2fx. It does not construct the conditioned predicates or physical witnesses, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

In the balanced conditioned-key branch, a support-key root family has size `m`, and one named failed predicate labels a graph `F_p` between those candidates and outside witness tokens with `e>=m^2/q` edges. Every edge has a least physical failure witness: a source candidate, endpoint, blocker occurrence, cycle edge, threshold record, burden certificate, conditioned-source field or repair slot.

## SRR2fy -- retained conditioned-predicate mass -- PROVED

The selected predicate retains all `e>=m^2/q` failed candidate-witness pairs for independent extraction.

## SRR2fz -- conditioned star or endpoint matching -- PROVED

For any `D>=1`, either one candidate or outside witness token has predicate-failure degree at least `D+1`, or every endpoint degree is at most `D` and greedy selection gives a matching `M` with

\[
\boxed{|M|\ge\left\lceil\frac{e}{2D-1}\right\rceil.}
\]

## SRR2ga -- witness overload or independent conditioned stock -- PROVED

For `mu>=1`, either one physical failure witness labels at least `mu+1` edges of `M`, or choosing one edge per witness gives a stock `S` with distinct candidates, witness tokens and physical witnesses and

\[
\boxed{|S|\ge\left\lceil\frac{|M|}{\mu}\right\rceil
\ge\left\lceil\frac{e}{(2D-1)\mu}\right\rceil.}
\]

## SRR2gb -- conditioned-stock payment router -- PROVED UNDER THE PAYMENT CONTRACT

One exact continuation holds: a degree-`D+1` failed-predicate star; a physical witness overload; an endpoint- and witness-disjoint conditioned stock; or an incomplete predicate/witness dictionary. If each distinct witness pays at least `rho` units of endpoint burden or source credit, capacity-one charging gives total payment at least `rho|S|`. Extraction creates no witness mass and pays no burden by itself.

## Corrected SRR frontier

The conditioned obstruction is now a high-degree predicate star, a physical-witness overload, or an independent realized stock. Remaining work is to construct the cycle/threshold/burden witness dictionary and prove concrete `D,mu,rho` bounds.

## Finite check

`scripts/verify_srr_predicate_independent_stocks.py` checks the degree-star/matching dichotomy, witness overload and independent-stock bounds.