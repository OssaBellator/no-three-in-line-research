# Orbit-phase support-rooted Hall cuts

## Status

This note proves OP4gk--OP4gn under the support-local typed-source and exact quotient-key contracts through OP4gj. It does not construct the physical unit-sensitive predicate dictionary, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the exact residual/edit incidence to source-token graph. Each unmatched incidence retains its least touched phase primitive and complete quotient key. For a support-key pair `(x,k)`, let `U_{x,k}` be the unmatched roots, put `m=|U_{x,k}|`, and let `A,B` be their alternating incidence and source-token closures inside key `k`.

## OP4gk -- phase support-key concentration -- PROVED

If the total residual/edit deficit is `delta>0` and `M` support-key pairs occur among the unmatched roots, one pair satisfies

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Hence one quotient coordinate, residual/edit slot, action, owner occurrence, unit/valuation/holonomy field, carry record or boundary context and one complete quotient key carry a quantified root family.

## OP4gl -- exact rooted phase Hall cut -- PROVED

The alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

A reachable free source token would yield an augmenting path. Every reached token is matched bijectively to `A\setminus U_{x,k}`, while alternating closure gives `N(A)=B`. Thus the exact rooted deficit is `m`.

## OP4gm -- source shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be all residual/edit incidences and typed source tokens in key `k`.

1. If `|T_k|<|R_k|`, return the exact quotient-key source shortfall.
2. Otherwise `|T_k\setminus B|>=m`, and
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a missing source-compatibility rectangle containing at least `m^2` pairs.

## OP4gn -- unit-sensitive predicate concentration -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assign each within-key nonedge to its least failed retained predicate among `q` quotient, residual/edit, unit, valuation, holonomy, owner, occurrence, carry and boundary predicates. One predicate labels at least

\[
\boxed{m^2/q}
\]

root-source pairs, and one selected root has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside source tokens failing that predicate. A nonedge with no failed named predicate is returned as an incomplete typed-source dictionary witness.

Thus a residual OP obstruction is localized to one touched phase primitive, one quotient key, one exact rooted Hall cut and one named unit-sensitive predicate.

## Corrected OP5 frontier

Construct and bound the physical phase support, key and predicate dictionaries, then pay or descend from the returned support-key-predicate residual/edit obstruction.

## Finite check

`scripts/verify_op_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems and every displayed identity and concentration bound.