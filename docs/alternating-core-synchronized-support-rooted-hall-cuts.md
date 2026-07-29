# Alternating-core synchronized support-rooted Hall cuts

## Status

This note proves AC5gh--AC5gk under the synchronized support-local contracts through AC5gg and the six side-track rooted-cut contracts. It does not construct the physical predicate dictionaries, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the synchronized disjoint union of the AC, RI, BDA, GC, OP, SRR and SAS exact compatibility graphs. Every unmatched incidence retains its track, complete compatibility key and least touched primitive support cause.

For a typed support-key triple `(s,x,k)`, let `U_{s,x,k}` be its unmatched roots and put `m=|U_{s,x,k}|`. Inside the one track-key component `(s,k)`, let `A,B` be the alternating incidence and token closures reached from those roots.

## AC5gh -- typed support-key concentration -- PROVED

If the synchronized deficit is `delta>0` and `M` typed support-key triples occur among its unmatched roots, one triple satisfies

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Thus synchronized failure is concentrated simultaneously on one frontier, one touched physical primitive and one compatibility key.

## AC5gi -- exact rooted synchronized Hall cut -- PROVED

The selected component closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

A reachable free token would give a within-track augmenting path. Matching bijects `B` with `A\setminus U_{s,x,k}`, and alternating closure gives `N(A)=B`. Hence this one typed rooted cut has exact deficit `m`.

## AC5gj -- numerical key shortfall or quadratic missing rectangle -- PROVED

Let `R_{s,k},T_{s,k}` be the complete incidence and token sets in the selected track-key component.

1. If `|T_{s,k}|<|R_{s,k}|`, return the exact numerical track-key shortfall.
2. Otherwise `|T_{s,k}\setminus B|>=m`, and
   \[
   \boxed{U_{s,x,k}\times(T_{s,k}\setminus B)}
   \]
   is a missing compatibility rectangle containing at least `m^2` pairs.

The rectangle stays inside one track and one key, so no cross-ledger or cross-key nonedge is used to manufacture the bound.

## AC5gk -- typed failed-predicate concentration router -- PROVED UNDER THE COMPLETE PREDICATE CONTRACTS

Let the selected track-key component have `q` ordered retained compatibility predicates. Assign each nonedge in the rooted rectangle to its least failed predicate. One predicate labels at least

\[
\boxed{m^2/q}
\]

root-token pairs, and one selected root has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside tokens failing that predicate.

If a nonedge has no failed retained predicate, the selected track dictionary is incomplete and the least such pair is returned. Therefore one exact synchronized continuation holds:

1. all assignments are complete;
2. one track-key has an explicit numerical token shortfall;
3. one typed support-key Hall cut returns a quadratic missing rectangle and a named failed predicate;
4. one support, key, predicate, epoch, occurrence, source-ledger or cross-track contract fails.

## Corrected AC6 frontier

The residual synchronized obstruction is now one frontier, one touched primitive, one key, one exact rooted Hall cut and one named failed predicate. Remaining work is to construct the physical predicate dictionaries and turn that concentrated object into payment, descent, reset or replenishment sufficient for an AC6 macro cycle.

## Finite check

`scripts/verify_ac_synchronized_support_rooted_hall_cuts.py` generates 1,500 seven-track macro systems and checks typed support-key concentration, exact rooted cuts, key shortfalls, quadratic rectangles and predicate concentration.