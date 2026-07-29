# Sparse algebraic support-local neutral churn

## Status

This note proves SAS5ng--SAS5nj under the key-local boundary-neutral and incremental contracts through SAS5nf. It does not construct the boundary-neutral dependency dictionary, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the primitive sparse-move resource set: moved rows or cells, swap positions, arithmetic profile fields, orientation records, legality guards, boundary records, pair/completion slots and owner occurrences. One sparse edit has support `S subseteq X`, with `1<=|S|<=H`.

Every changed/new pair or completion incidence, changed/new next neutral token, and changed/deleted old neutral token declares a dependency set meeting `S`. A changed record whose dependency misses the support is returned as a nonlocal sparse-change or lineage witness.

## SAS5ng -- exact sparse-support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed record has a least touched primitive cause. Missing dependencies, a hidden sign or orientation change, undeclared move/legality change, boundary relabelling or lineage-only mutation are first exact failures.

## SAS5nh -- primitive neutral-churn bounds -- PROVED

Let `alpha_R`, `alpha_+`, and `alpha_-` be the maximum numbers of changed pair/completion incidences, changed/new next neutral tokens, and changed/deleted old neutral tokens depending on one touched primitive. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\qquad |\Delta T|\le H\alpha_+,\qquad |T\setminus T^\circ|\le H\alpha_-.}
\]

Every changed record meets the support and is counted at least once among at most `H` primitive incidences.

## SAS5ni -- support-local neutral audit -- PROVED

With neutral key-fibre bounds `L_T,L_R` from SAS5nd, one sparse edit requires at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}
\]

fresh boundary-neutral compatibility evaluations. The carried pair/completion matching leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

incidences unmatched. At most this many augmenting paths restore a complete neutral assignment, or the boundary-neutral Hall deficit is at most this quantity. Matching maintenance creates no neutral mass and changes no orientation payment.

## SAS5nj -- support-anchored sparse obstruction -- PROVED

After maximal reaugmentation, every unmatched incidence is initially support-disturbed: it is changed/new, or its old assigned neutral token changed or disappeared. Assign its least support cause.

If the residual deficit is `delta>0`, one moved row or cell, swap position, arithmetic profile field, orientation record, legality guard, boundary record or pair/completion slot anchors at least

\[
\boxed{\lceil\delta/H\rceil}
\]

unmatched roots. Each root has a closed alternating search with no free neutral token and is an explicit support-local sparse obstruction.

## Corrected SAS6 frontier

Sparse maintenance is now bounded by physical move support and primitive dependency incidence. Remaining work is to construct actual dependency sets, prove support, incidence and neutral key-fibre bounds, evaluate the small boundary, and pay support-anchored Hall roots or lineage failures.

## Finite check

`scripts/verify_sas_support_local_neutral_churn.py` checks support incidence bounds, key-local audit bounds, carried neutral disturbance, residual-root concentration and nonlocal-change detection.