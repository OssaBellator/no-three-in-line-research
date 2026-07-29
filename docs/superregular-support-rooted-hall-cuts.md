# Superregular support-rooted Hall cuts

## Status

This note proves SRR2fu--SRR2fx under the support-local witness and exact conditioned-key contracts through SRR2ft. It does not construct the physical conditioned predicate dictionary, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the exact candidate-incidence to witness-token graph. Each unmatched candidate retains its least touched resampling primitive and complete conditioned key. For a support-key pair `(x,k)`, let `U_{x,k}` be its roots, put `m=|U_{x,k}|`, and let `A,B` be their alternating candidate and witness closures inside key `k`.

## SRR2fu -- conditioned support-key concentration -- PROVED

If the total witness deficit is `delta>0` and `M` support-key pairs occur among its roots, one pair satisfies

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Thus one source candidate, endpoint, blocker occurrence, cycle edge, threshold record, burden certificate, conditioned-source field or repair slot and one conditioned key carry a quantified root family.

## SRR2fv -- exact rooted witness Hall cut -- PROVED

The alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

A reachable free witness would give an augmenting path. Matching bijects `B` with `A\setminus U_{x,k}`, while alternating closure gives `N(A)=B`. Hence the rooted Hall deficit is exactly `m`.

## SRR2fw -- witness shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be all candidates and witnesses in conditioned key `k`.

1. If `|T_k|<|R_k|`, return the exact conditioned-key witness shortfall.
2. Otherwise `|T_k\setminus B|>=m`, and
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a missing candidate-witness rectangle containing at least `m^2` pairs.

## SRR2fx -- conditioned-predicate concentration -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assign each within-key nonedge to its least failed retained predicate among `q` threshold, burden, conditioning, source, endpoint, blocker, cycle, occurrence and repair predicates. One predicate labels at least

\[
\boxed{m^2/q}
\]

root-witness pairs, and one selected candidate has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside witnesses failing that same predicate. A nonedge with no named failure is an incomplete conditioned dictionary witness.

The residual resampling obstruction is now localized to one touched primitive, one conditioned key, one exact rooted Hall cut and one named failed predicate.

## Corrected SRR frontier

Construct and bound the physical support, key and conditioned-predicate dictionaries, then pay or descend from the returned support-key-predicate burden obstruction.

## Finite check

`scripts/verify_srr_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems and every displayed cut and concentration bound.