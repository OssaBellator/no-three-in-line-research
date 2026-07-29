# Rational-inverse support-rooted Hall cuts

## Status

This note proves RI5he--RI5hh under the support-local collateral and exact typed-key contracts through RI5hd. It does not construct the arithmetic dependency or predicate dictionaries, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum collateral matching in the exact next-epoch RI compatibility graph. Every unmatched repair incidence retains its least touched primitive support cause and its complete collateral key. For a support-key pair `(x,k)`, let `U_{x,k}` be the unmatched roots with that pair and put `m=|U_{x,k}|`.

Inside key `k`, orient every nonmatching compatibility edge from incidences to collateral tokens and every matching edge from tokens to incidences. Let `A` and `B` be the incidence and token sets reachable from `U_{x,k}`.

## RI5he -- support-key root concentration -- PROVED

If the total RI matching deficit is `delta>0` and `M` support-key pairs occur among the unmatched roots, one pair satisfies

\[
\boxed{m\ge \left\lceil\frac{\delta}{M}\right\rceil.}
\]

This refines the support-only concentration from RI5hd to one touched arithmetic primitive and one complete collateral key.

## RI5hf -- exact rooted alternating Hall cut -- PROVED

The rooted alternating closure satisfies

\[
\boxed{N(A)=B,\qquad |A|-|B|=m.}
\]

No token in `B` is free, because that would give an augmenting path from one of the unmatched roots. Every token in `B` is matched to a distinct incidence in `A\setminus U_{x,k}`, and every incidence in that difference is reached through its matched token. Hence matching gives a bijection between `B` and `A\setminus U_{x,k}`. Closure under all nonmatching incidence-to-token edges and the matched predecessor edge gives `N(A)=B`.

Thus `(A,B)` is an explicit RI Hall cut whose deficit is exactly the number of selected support-key roots, not merely a positive lower bound.

## RI5hg -- numerical shortfall or quadratic missing rectangle -- PROVED

Let `R_k,T_k` be the complete incidence and collateral sets in key `k`.

1. If `|T_k|<|R_k|`, return the exact numerical collateral-key shortfall `|R_k|-|T_k|`.
2. If `|T_k|>=|R_k|`, then
   \[
   |T_k\setminus B|\ge m.
   \]
   Moreover every pair in
   \[
   \boxed{U_{x,k}\times(T_k\setminus B)}
   \]
   is a compatibility nonedge. Hence this rooted missing rectangle has at least `m^2` pairs.

Indeed `|T_k\setminus B|>=|R_k|-|B|=|R_k\setminus A|+m`, while `N(A)=B` excludes every displayed pair.

## RI5hh -- failed-predicate concentration router -- PROVED UNDER THE COMPLETE PREDICATE CONTRACT

Assume every within-key nonedge is assigned to its least failed retained RI predicate among `q` ordered arithmetic, owner/charge, blocker, occurrence, certificate and boundary predicates.

In the balanced-key branch of RI5hg, one failed predicate labels at least

\[
\boxed{\frac{m^2}{q}}
\]

root-token pairs. One selected support-key root therefore has at least

\[
\boxed{\left\lceil\frac{m}{q}\right\rceil}
\]

outside collateral tokens failing that same named predicate.

If a nonedge has no failed retained predicate, the compatibility dictionary is incomplete and the least such pair is returned instead. Thus a residual RI obstruction is now localized to one touched primitive, one collateral key, one exact Hall cut and one named failed predicate.

## Corrected RI6 frontier

The remaining RI work is to construct the physical support, key and predicate dictionaries; prove numerical support, fibre and predicate-count bounds; and pay or descend from the returned support-key-predicate obstruction.

## Finite check

`scripts/verify_ri_support_rooted_hall_cuts.py` checks 2,500 exact keyed systems, maximum matchings, support-key concentration, rooted alternating closures, numerical shortfalls, missing rectangles and failed-predicate concentration.