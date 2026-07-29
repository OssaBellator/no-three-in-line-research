# Geometric-cleaning support-rooted Hall cuts

## Status

This note proves GC2ml--GC2mo under the support-local donor and exact geometric-key contracts through GC2mk. It does not construct the physical geometric predicate dictionary, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the exact remedy-incidence to donor-token graph. Each unmatched remedy incidence retains its least touched cleaning primitive and complete geometric key. For one support-key pair `(x,k)`, let `U_{x,k}` be its roots, `m=|U_{x,k}|`, and let `A,B` be their alternating incidence and donor closures inside key `k`.

## GC2ml -- geometric support-key concentration -- PROVED

If the residual donor deficit is `delta>0` and `M` support-key pairs occur among its unmatched roots, one pair has

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Thus one moved cell, protected event, polynomial/rational chart, donor occurrence, remedy slot, height record or boundary primitive and one geometric key carry a quantified root family.

## GC2mm -- exact rooted donor Hall cut -- PROVED

The alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

A reachable free donor would produce an augmenting path. Every reached donor is matched bijectively to `A\setminus U_{x,k}`, and closure gives `N(A)=B`. Hence the geometric Hall deficit is exactly `m`.

## GC2mn -- donor shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be all remedies and donors in key `k`.

1. If `|T_k|<|R_k|`, return the exact donor-key numerical shortfall.
2. Otherwise `|T_k\setminus B|>=m`, and
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a missing-compatibility rectangle of at least `m^2` pairs.

## GC2mo -- geometric-predicate concentration -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assign each within-key nonedge to its least failed retained predicate among `q` donor, remedy, height, chart, protected-event, certificate, occurrence and boundary predicates. One predicate labels at least

\[
\boxed{m^2/q}
\]

root-donor pairs, and one selected root has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside donors failing that predicate. A nonedge with no named failed predicate is an incomplete geometric dictionary witness.

Thus the remaining cleaning obstruction is localized to one touched primitive, one chart/height key, one exact rooted Hall cut and one named failed geometric predicate.

## Corrected GC5 frontier

Construct and bound the physical support, key and predicate dictionaries, then pay, descend from, or reset the returned support-key-predicate donor obstruction.

## Finite check

`scripts/verify_gc_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems and every displayed identity and concentration bound.