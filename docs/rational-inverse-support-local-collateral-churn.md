# Rational-inverse support-local collateral churn

## Status

This note proves RI5ha--RI5hd under the typed-key and incremental collateral contracts through RI5gz. It does not construct the arithmetic dependency dictionary, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the finite set of primitive RI resources: changed grid cells, owner occurrences, blocker slots, arithmetic certificate fields, or exterior records. One physical RI edit has declared support `S subseteq X`, with `1<=|S|<=H`.

Every changed or newly created repair incidence `r in Delta R` carries a nonempty dependency set `D_R(r)` meeting `S`. Every changed or newly created next collateral token `t in Delta T` carries `D_+(t)` meeting `S`. Every old collateral token leaving the unchanged set carries `D_-(t)` meeting `S`. A changed record whose declared dependency misses `S` is a nonlocal-change witness and resets the local argument.

## RI5ha -- exact support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed incidence, changed/new next token, and changed/deleted old token has a least support cause in the fixed order on `S`. Thus all edit churn is partitioned by touched primitive resource. Missing dependencies, an empty support intersection, or an unrecorded global relabelling are returned as the first exact failure.

## RI5hb -- support-incidence churn bounds -- PROVED

Put

\[
\alpha_R=\max_{x\in S}|\{r\in\Delta R:x\in D_R(r)\}|,
\]

and define `alpha_+` and `alpha_-` analogously for changed/new next tokens and old tokens leaving the unchanged set. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\qquad
|\Delta T|\le H\alpha_+,\qquad
|T\setminus T^\circ|\le H\alpha_-.}
\]

### Proof

Every changed record is counted by at least one touched primitive. Summing its incidences over `S` is at most `H` times the maximum primitive incidence. QED.

## RI5hc -- support-local audit and reaugmentation -- PROVED

Let `L_T,L_R` be the collateral key-fibre bounds from RI5gy. Then one physical RI edit needs at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}
\]

fresh compatibility evaluations. The carried matching leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

incidences unmatched. Hence at most that many augmenting paths restore a complete collateral assignment, or the typed Hall deficit is at most the same quantity.

### Proof

Apply RI5gy with `a<=H alpha_R`, `c<=H alpha_+`, and RI5gz with `e<=H alpha_-`. QED.

## RI5hd -- support-cause concentration of residual deficit -- PROVED

Extend the carried matching by augmenting paths until it is maximum. Every remaining unmatched incidence belongs to the initially disturbed set: either it is changed/new, or its old collateral token changed or disappeared. Assign each such root its least support cause from RI5ha.

If the final deficit is `delta>0`, some touched primitive supports at least

\[
\boxed{\left\lceil\delta/H\right\rceil}
\]

unmatched incidence roots. Each root has no augmenting path to a free token in the exact next dictionary and therefore supplies an explicit alternating-search obstruction anchored at that primitive.

### Proof

Augmentation starts only from initially unmatched incidences, so the final unmatched set is a subset of the initially disturbed set. Pigeonhole its `delta` least causes over at most `H` support primitives. Maximality excludes an augmenting path from every residual root. QED.

## Corrected RI6 frontier

RI churn is now bounded by the size of the physical edit support and primitive dependency incidences. Remaining work is to construct the actual RI dependency sets, bound `H,alpha_R,alpha_+,alpha_-` and the key fibres, evaluate the resulting boundary, and pay the support-anchored Hall roots.

## Finite check

`scripts/verify_ri_support_local_collateral_churn.py` checks dependency incidence bounds, key-local audit bounds, carried matching disturbance, residual-root support concentration, and nonlocal-change detection.