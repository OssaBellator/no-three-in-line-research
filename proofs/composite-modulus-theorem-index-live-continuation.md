# Live composite-modulus theorem ledger continuation

The authoritative live ledger through CMR747 is
[`composite-modulus-theorem-index-live.md`](composite-modulus-theorem-index-live.md).
This continuation is authoritative for CMR748 onward on branch
`research/all-n-composite-modulus`.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR748--754 | Degree-bounded simultaneous target-line avoidance, exact linear protected-line capacity, full-envelope target-line handoff, recurrence payment, reserve saturation, dyadic height localisation, and the envelope-chain endpoint | PROVED | `docs/197-prime-power-recurrent-target-line-reserve.md` |
| CMR755--762 | Common-layer historical target-pair extraction, fan/compatible-bank dichotomy, physical-cell fan refinement, global ordered two-layer neutralisation, quantitative reserve extraction, return-edge payment, and the protected-line saturation endpoint | PROVED | `docs/198-prime-power-protected-line-pair-neutralization.md` |
| CMR763--769 | Finite neutralisation-certificate stock, permanent-until-return witnesses, fresh-key discipline, exact cell--absence-run slots, finite certificate capacity per run, repeated-cell-star run accounting, and exact token payment | PROVED | `docs/199-prime-power-neutralized-pair-temporal-ledger.md` |
| CMR770--776 | Six labelled same-layer pair types per physical target, labelled recurrence, nonessential pair-edge deletion, exact double-essential contraction, rank-one transfer, returned-edge payment, and the recurrent-target endpoint | PROVED | `docs/200-prime-power-recurrent-labelled-target-pair.md` |
| CMR777--784 | Owner-independent physical restorations, returned-edge response classification, forward loss-time ancestry, recurrent-edge path bounds, branch-wide fresh-root stock, forest-size bounds, repeated-edge deletion/contraction, and the global returned-edge endpoint | PROVED | `docs/201-prime-power-global-return-ancestry-forest.md` |
| CMR785--792 | Joint-state entering-set size, anchor-preserving batch rejection, target-destroying scheduler, quadratic fixed-owner deletion budget, forced physical target, labelled-pair normalisation, exact double contraction, and the fixed-owner target-churn endpoint | PROVED | `docs/202-prime-power-anchor-state-batch-rejection.md` |
| CMR793--799 | Pairwise-disjoint private entering batches, permanent closure until restoration, reopening injection, cumulative recurrence bounds, exact token payment, permanent-depletion split, and the anchor-batch return endpoint | PROVED | `docs/203-prime-power-anchor-batch-restoration-ledger.md` |
| CMR800--806 | Stored-anchor simultaneous redeletion, canonical anchor-loss witnesses, forward loss classification, finite monotone anchor replacement, reopening dichotomy, restoration thresholds, and the stored-anchor endpoint | PROVED | `docs/204-prime-power-stored-anchor-bulk-redeletion.md` |
| CMR807--813 | Canonical private-batch projection, pure-reopening invariance and cycle erasure, nonprivate context witnesses, finite context stock, normalized reset alternatives, and the private-normalization endpoint | PROVED | `docs/205-prime-power-private-batch-normalization-projection.md` |
| CMR814--821 | State-activation support, immediate absorption of enabling edges, finite private growth, monotone deactivation, repeated activation payment, fixed-anchor active-transition bounds, and local/branch-wide context endpoints | PROVED | `docs/206-prime-power-active-context-absorption.md` |
| CMR822--829 | Unique edge ownership in exact products, strict single-child edge lineage, static-stage and envelope owner bounds, restoration concentration, fixed-owner response, interface escape payment, and the physical-edge lineage endpoint | PROVED | `docs/207-prime-power-physical-edge-lineage.md` |

The branch still does not prove the all-`n` conjecture. Through CMR829, owner
relabelling, routing variation, repeated private-batch reopening, anchor failure,
and factor-tree branching can no longer duplicate one physical restoration.
Returned structural deletions form a forward acyclic ancestry forest. At a fixed
owner, every rejected nonimproving state contributes a private entering batch of
at least two edges; the batches are disjoint, can be reclosed simultaneously by
a surviving anchor, and normalize away pure reopening cycles. Any active
nonprivate context edge is absorbed after a nonimproving activation or pays a
genuine absence run.

One recurrent physical edge has only

\[
(h+1)\left(1+\sum_{m=1}^{N}(2m^2+m+1)\right)
\]

structural owner slots, because exact products give unique edge ownership and a
nonfixed edge follows one strict side-descending factor lineage. Hence many
branch-wide restorations concentrate at one fixed owner, where bulk redeletion,
private absorption, anchor-loss ancestry, matching-preserving deletion, or
essential contraction applies.

The remaining prime-power frontier is the final fixed-owner, fixed-edge loop:
prove that an edge which is genuinely restored often enough to survive every
private normalization and deletion/contraction response forces inherited target-
load decrease, protected-reserve exhaustion, or strict global potential
improvement. Prime-field transfer and arbitrary side-length assembly remain
necessary afterward.
