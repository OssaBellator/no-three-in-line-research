# Superregular support-local witness churn

## Status

This note proves SRR2fq--SRR2ft under the conditioned key-local witness and incremental contracts through SRR2fp. It does not construct the conditioned dependency dictionary, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the primitive resampling resource set: source candidates, endpoints, blocker occurrences, bounded-cycle edges, threshold records, burden certificates, conditioned-source fields and repair slots. One resampling edit has support `S subseteq X`, with `1<=|S|<=H`.

Every changed/new candidate incidence, changed/new next witness token, and changed/deleted old witness token declares a dependency set meeting `S`. A changed record whose declared dependency misses `S` is a nonlocal conditioning witness.

## SRR2fq -- exact resampling-support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed record has a least touched primitive cause. Missing dependencies, a hidden threshold or burden change, an undeclared conditioned-source change, or global witness relabelling are first exact failures.

## SRR2fr -- primitive witness-churn bounds -- PROVED

Let `alpha_R`, `alpha_+`, and `alpha_-` be the maximum numbers of changed candidate incidences, changed/new next witness tokens, and changed/deleted old witness tokens depending on one touched primitive. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\qquad |\Delta T|\le H\alpha_+,\qquad |T\setminus T^\circ|\le H\alpha_-.}
\]

Every changed record meets the support and is counted at least once among at most `H` primitive incidences.

## SRR2fs -- support-local conditioned audit -- PROVED

With conditioned key-fibre bounds `L_T,L_R` from SRR2fo, one bounded-cycle edit requires at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}
\]

fresh candidate/witness predicate evaluations. The carried witness matching leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

candidates unmatched. At most this many augmenting paths restore a complete witness assignment, or the conditioned Hall deficit is at most this quantity. Matching maintenance creates no witness mass and pays no endpoint burden.

## SRR2ft -- support-anchored resampling obstruction -- PROVED

After maximal reaugmentation, every unmatched candidate is initially support-disturbed: it is changed/new, or its old assigned witness changed or disappeared. Assign its least support cause.

If the final deficit is `delta>0`, one source candidate, endpoint, blocker occurrence, cycle edge, threshold record, burden certificate or conditioned-source field anchors at least

\[
\boxed{\lceil\delta/H\rceil}
\]

unmatched roots. Each root has a closed alternating search with no free compatible witness and is an explicit support-local conditioned obstruction.

## Corrected SRR frontier

Resampling churn is now bounded by bounded-cycle support and primitive dependency incidence. Remaining work is to construct the actual dependency sets, prove support, incidence and conditioned key-fibre bounds, evaluate the small boundary, and pay the support-anchored burden core.

## Finite check

`scripts/verify_srr_support_local_witness_churn.py` checks support incidence bounds, key-local audit bounds, carried witness disturbance, residual-root concentration and nonlocal-change detection.