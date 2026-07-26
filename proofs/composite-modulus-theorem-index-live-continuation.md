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
| CMR785--792 | Joint-state entering-set size, anchor-preserving aggressive batch rejection, quadratic subbranch deletion budget, branch-local target/pair forcing, exact branch-local double contraction, and the corrected aggressive-subbranch endpoint | PROVED, explicitly branch-local | `docs/202-prime-power-anchor-state-batch-rejection.md` |
| CMR793--799 | Pairwise-disjoint private entering batches, permanent closure until restoration, reopening injection, cumulative recurrence bounds, exact token payment, permanent-depletion split, and the anchor-batch return endpoint | PROVED on the aggressive branch | `docs/203-prime-power-anchor-batch-restoration-ledger.md` |
| CMR800--806 | Stored-anchor simultaneous redeletion, canonical anchor-loss witnesses, forward loss classification, finite monotone anchor replacement, reopening dichotomy, restoration thresholds, and the stored-anchor endpoint | PROVED on the aggressive branch | `docs/204-prime-power-stored-anchor-bulk-redeletion.md` |
| CMR807--813 | Canonical private-batch projection, pure-reopening invariance and cycle erasure, nonprivate context witnesses, finite context stock, normalized reset alternatives, and the private-normalization endpoint | PROVED on the aggressive branch | `docs/205-prime-power-private-batch-normalization-projection.md` |
| CMR814--821 | State-activation support, immediate absorption of enabling edges, finite private growth, monotone deactivation, repeated activation payment, fixed-anchor active-transition bounds, and local/branch-wide context endpoints | PROVED on the aggressive branch | `docs/206-prime-power-active-context-absorption.md` |
| CMR822--829 | Unique edge ownership in exact products, strict single-child edge lineage, static-stage and envelope owner bounds, restoration concentration, fixed-owner response, interface escape payment, and the physical-edge lineage endpoint | PROVED | `docs/207-prime-power-physical-edge-lineage.md` |
| CMR830--837 | Exact state-exclusion union, viable-child coverage, preservation of every improving state, polynomial root-to-leaf depth, witness-guided viable paths, aggressive-branch containment, leaf-local forcing, and the completeness-corrected endpoint | PROVED | `docs/208-prime-power-complete-state-exclusion-branching.md` |
| CMR838--845 | Compatible common core, exact viability/nonessentiality equivalence, complete-core contraction, empty residual core, contraction-width conservation, deterministic zero/one-child cases, telescoping contraction rank, and the essential-core branch normal form | PROVED | `docs/209-prime-power-viable-branch-essential-core.md` |

The branch still does not prove the all-`n` conjecture. Through CMR845, owner
relabelling and factor-tree branching cannot duplicate one physical restoration,
and one aggressive anchor subbranch has exact private deletion, bulk redeletion,
normalization, and active-context payment. That aggressive subbranch is not by
itself a completeness-preserving search: deleting a complete entering batch may
remove other untested states.

Completeness is restored by the exact viable-child identity

\[
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q,\,\mathcal F-f\ne\varnothing}(\mathcal F-f).
\]

Every alternative state, including every improving state, survives in at least
one child. Each root-to-leaf path has at most `2n^2-2n` single-edge deletions.
The viable children are exactly the nonessential edges of `Q`. After contracting
the full common core, the residual family has empty core and

\[
\text{contracted rank}+\text{viable child count}=2n.
\]

Hence essential-edge proliferation and completeness width have been separated.
The active prime-power frontier is now twofold:

1. compress or control the width of the core-free viable-child branching tree, or
   prove that a canonical aggressive branch retains an improving witness;
2. inside a retained branch, close the final fixed-owner, fixed-edge restoration
   loop by forcing target-load decrease, reserve exhaustion, or strict potential
   improvement.

Prime-field transfer and arbitrary side-length assembly remain necessary.
