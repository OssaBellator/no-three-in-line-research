# Sparse algebraic support-rooted Hall cuts

## Status

This note proves SAS5nk--SAS5nn under the support-local neutral and exact sparse-key contracts through SAS5nj. It does not construct the physical boundary-neutral predicate dictionary, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the exact pair/completion incidence to neutral-token graph. Each unmatched incidence retains its least touched sparse primitive and complete neutral key. For one support-key pair `(x,k)`, let `U_{x,k}` be its roots, put `m=|U_{x,k}|`, and let `A,B` be their alternating incidence and neutral-token closures inside key `k`.

## SAS5nk -- sparse support-key concentration -- PROVED

If the total neutral deficit is `delta>0` and `M` support-key pairs occur among its roots, one pair satisfies

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Thus one moved row or cell, swap position, arithmetic-profile field, orientation record, legality guard, boundary record, pair/completion slot or owner occurrence and one complete neutral key carry a quantified root family.

## SAS5nl -- exact rooted neutral Hall cut -- PROVED

The alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

A reachable free neutral token would produce an augmenting path. Matching bijects `B` with `A\setminus U_{x,k}`, and closure gives `N(A)=B`. Hence the rooted sparse Hall deficit is exactly `m`.

## SAS5nm -- neutral shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be all pair/completion incidences and neutral tokens in key `k`.

1. If `|T_k|<|R_k|`, return the exact neutral-key numerical shortfall.
2. Otherwise `|T_k\setminus B|>=m`, and
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a missing compatibility rectangle containing at least `m^2` pairs.

## SAS5nn -- boundary-neutral predicate concentration -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assign each within-key nonedge to its least failed retained predicate among `q` sign, profile, move, legality, boundary, orientation, source, occurrence and repair predicates. One predicate labels at least

\[
\boxed{m^2/q}
\]

root-token pairs, and one selected root has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside neutral tokens failing that predicate. A nonedge with no named failure is an incomplete boundary-neutral dictionary or lineage witness.

Thus a residual sparse obstruction is localized to one touched primitive, one neutral key, one exact rooted Hall cut and one named failed predicate.

## Corrected SAS6 frontier

Construct and bound the physical sparse support, key and predicate dictionaries, then pay, descend from, or reset the support-key-predicate neutral obstruction or lineage failure.

## Finite check

`scripts/verify_sas_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems and every displayed cut and concentration bound.