# Bounded-denominator support-rooted Hall cuts

## Status

This note proves BDA5hn--BDA5hq under the support-local restoration and exact keyed potential contracts through BDA5hm. It does not construct the physical rational-gain predicate dictionary, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in one exact BDA repair-incidence to potential-token graph. Each unmatched incidence retains its least touched restoration primitive and complete restoration key. For a support-key pair `(x,k)`, let `U_{x,k}` be its unmatched roots and let `m=|U_{x,k}|`. Inside key `k`, let `A,B` be the alternating incidence and token closures reached from these roots using nonmatching incidence-to-token edges and matching token-to-incidence edges.

## BDA5hn -- restoration support-key concentration -- PROVED

If the total residual deficit is `delta>0` and `M` support-key pairs occur among its roots, one pair has

\[
\boxed{m\ge\left\lceil\frac{\delta}{M}\right\rceil.}
\]

Thus one touched context cell, gate, line record, owner occurrence, gain/damping field or arithmetic certificate and one restoration key carry a quantified root family.

## BDA5ho -- exact rooted restoration Hall cut -- PROVED

The alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

Maximum matching excludes a reachable free potential token. Matching gives a bijection from `B` to `A\setminus U_{x,k}`, while alternating closure gives `N(A)=B`. Hence the cut deficit is exactly the number of selected support-key roots.

## BDA5hp -- potential shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be all repair incidences and potential tokens in key `k`.

1. If `|T_k|<|R_k|`, return the exact numerical restoration-key shortfall.
2. Otherwise `|T_k\setminus B|>=m`, and every pair in
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a nonedge. The rooted missing rectangle therefore contains at least `m^2` pairs.

## BDA5hq -- rational-gain predicate concentration -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assign each within-key nonedge to its least failed retained predicate among `q` restoration-gate, source, gain, damping, line, owner, arithmetic, occurrence and boundary predicates. One predicate labels at least

\[
\boxed{m^2/q}
\]

pairs in the rooted rectangle, and one selected root has at least

\[
\boxed{\lceil m/q\rceil}
\]

outside potential tokens failing that predicate. A nonedge with no named failed predicate is returned as an incomplete compatibility dictionary witness.

The residual BDA obstruction is therefore localized to one touched restoration primitive, one key, one exact Hall cut and one named rational-gain predicate.

## Corrected BDA6 frontier

Construct and bound the physical support, key and predicate dictionaries, then pay or descend from the support-key-predicate restoration obstruction.

## Finite check

`scripts/verify_bda_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems and every displayed concentration and cut identity.