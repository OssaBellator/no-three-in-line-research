# Bounded-denominator support-local restoration churn

## Status

This note proves BDA5hj--BDA5hm under the key-local potential and incremental contracts through BDA5hi. It does not construct the rational-gain dependency dictionary, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the finite set of primitive restoration resources: context cells, restoration gates, connector or resonant line records, owner occurrences, gain/damping fields and arithmetic certificates. One restoration edit has support `S subseteq X`, with `1<=|S|<=H`.

Every changed/new repair incidence, changed/new next potential token, and changed/deleted old potential token declares a dependency set meeting `S`. A changed record whose dependency misses `S` is returned as a nonlocal restoration witness.

## BDA5hj -- exact restoration-support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed record has a least touched primitive cause in the fixed order on `S`. Missing dependencies, an empty intersection, a hidden gate change or a global arithmetic relabelling are first exact failures.

## BDA5hk -- primitive-incidence churn bounds -- PROVED

Let `alpha_R`, `alpha_+`, and `alpha_-` be the maximum, over `x in S`, of the number of changed incidences, changed/new next potential tokens, and changed/deleted old potential tokens depending on `x`. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\quad |\Delta T|\le H\alpha_+,\quad |T\setminus T^\circ|\le H\alpha_-.}
\]

Every changed record is counted by at least one touched primitive, and the sum over at most `H` primitives is bounded by `H` times the largest incidence.

## BDA5hl -- support-local potential audit -- PROVED

With key-fibre bounds `L_T,L_R` from BDA5hg, one restoration edit needs at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}
\]

fresh rational-gain compatibility evaluations. The carried potential assignment leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

incidences unmatched. Thus at most this many augmenting paths restore a complete assignment, or the arithmetic Hall deficit is at most this quantity. Assignment maintenance creates no gain or potential mass.

## BDA5hm -- support-anchored residual obstruction -- PROVED

After maximal reaugmentation, every unmatched incidence is one of the initially changed incidences or an unchanged incidence whose old potential token changed or disappeared. Give it the least support cause of that change.

If the final deficit is `delta>0`, some touched gate, cell, owner occurrence, line record or arithmetic field anchors at least

\[
\boxed{\lceil\delta/H\rceil}
\]

unmatched roots. Each has a closed alternating search with no free compatible token and is an explicit support-local restoration obstruction.

## Corrected BDA6 frontier

Restoration churn is now bounded by touched primitive resources and their dependency incidences. Remaining work is to construct the physical dependency dictionary, prove the support and incidence caps and key-fibre bounds, evaluate the small boundary, and pay the support-anchored arithmetic obstruction.

## Finite check

`scripts/verify_bda_support_local_restoration_churn.py` checks support incidence bounds, key-local audit bounds, carried potential matching disturbance, residual-root concentration and nonlocal-change detection.