# Live composite-modulus theorem ledger continuation 2

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869; and
- this file from CMR870 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR870--877 | Nine-atom triple support, multiplicity/support alternatives, disjoint support packing versus small cover, atom concentration, wall/cell-star refinement, global compatibility, branch-path payment, and the support endpoint | PROVED | `docs/213-prime-power-new-triple-support-packing.md` |
| CMR878--885 | Deletion/contraction path resources, disjoint-support path bound, polynomial support matching and cover, atom concentration, explicit episode bound, geometric interpretation, and the constant-arity path endpoint | PROVED | `docs/214-prime-power-constant-arity-path-budget.md` |
| CMR886--893 | Physical-cell and matching-vertex edge stabilisation, uniform labelled-edge concentration, exact binary edge split, conditioned edge contraction, rank-two transfer, residual-pair multiplicity, and the support-atom batching endpoint | PROVED | `docs/215-prime-power-support-atom-edge-batching.md` |
| CMR894--901 | Ordered disjoint prescription partitions, fixed-prefix normalisation, undecided-edge progress, finite target-resolution depth, forced-target leaves, physical-target grouping, eight layer-assignment classes, and polynomial terminal-certificate compression | PROVED | `docs/216-prime-power-disjoint-leaf-certificate-compression.md` |
| CMR902--909 | Minimum-anchor preservation, outside-anchor target witnesses, quadratic target and prescription forcing, induced-objective contraction, target contraction, restoration response, and the minimum-anchor endpoint | PROVED | `docs/217-prime-power-minimum-anchor-preserving-path.md` |
| CMR910--917 | Minimum-face witness characterisation, exact edge dichotomy, complete minimum-core contraction, residual core-freeness, recurrent-edge deletion or contraction, paid reopening, finite core growth, and the fixed-owner minimum-face endpoint | PROVED | `docs/218-prime-power-minimum-face-edge-dichotomy.md` |
| CMR918--925 | One free edge closure per owner, active-occurrence/restoration bounds, threshold and token forms, recurrent-owner response, total active-edge episode bound, finite core-rank budget, and the minimum-face edge-lineage endpoint | PROVED | `docs/219-prime-power-minimum-face-edge-lineage-budget.md` |
| CMR926--933 | Restriction/expansion minimum-face formulas, arbitrary-transition witnesses, canonical minimum changes, minimum-core growth and shrinkage, finite witness stock, and the owner-transition minimum-face endpoint | PROVED | `docs/220-prime-power-minimum-face-owner-transition.md` |
| CMR934--941 | Same-value expansion rollback, restoration-cycle erasure, intersection normalization, finite monotone restrictions, minimum-loss ancestry, and the expansion-rollback endpoint | PROVED | `docs/221-prime-power-minimum-expansion-rollback.md` |
| CMR942--949 | Added-batch transversality under lowering expansion, minimum-preserving peeling, forced added-edge core contraction, peel budgets, record alternatives, mixed-transition transfer, and the lowering-expansion endpoint | PROVED | `docs/222-prime-power-lowering-expansion-core-contraction.md` |
| CMR950--957 | Infeasible-base transversality, complete expansion normalization, arbitrary host-transition normal form, nested restriction segments, polynomial fixed-vertex execution bounds, restoration-capacity removal, and the complete same-vertex-set endpoint | PROVED | `docs/223-prime-power-complete-host-transition-normalization.md` |
| CMR958--965 | Exact constant/pure/coupling decomposition, low local ranks, Cartesian coupling boxes, finite stock, contraction transport, minimum-preserving coupling deletion or minimum-face contraction, finite normalization, and the coupling-normalized endpoint | PROVED | `docs/224-prime-power-induced-product-potential-transport.md` |
| CMR966--973 | Coordinate-fibre minimum inheritance, exact one-factor induced potential, target location trichotomy, anchored deletion/contraction, finite fibre normalization, pure residual potential, strict factor descent, and the coordinate-fibre endpoint | PROVED | `docs/225-prime-power-minimum-coordinate-fibre-descent.md` |
| CMR974--981 | Conditioning preserves the exact minimum face, induced contraction, one-layer and joint two-layer host representation, factorwise conditioning, potential transport, iterated representable contraction, and the host-representable minimum-core endpoint | PROVED | `docs/226-prime-power-minimum-core-host-representability.md` |
| CMR982--989 | Minimum-face target variability, physical two-label cell cuts, finite same-value handoff depth, restoration payment, bank-expansion trichotomy, labelled target conditioning, physical-cell recurrence, and the target-handoff endpoint | PROVED | `docs/227-prime-power-minimum-face-target-handoff.md` |
| CMR990--997 | Exact robust energy-gap surplus, entering-edge support, cumulative incidence, finite basic signature stock, recurrence bounds, corrected four-class residual-pair refinement, and the robust-surplus endpoint | PROVED; corrected pair scope | `docs/228-prime-power-minimum-robust-target-surplus.md` |
| CMR998--1005 | Unique residual pair per occurrence, four pair types, exact assignment-class partition, fixed-class host-representable contraction, owner-independent augmented signatures, finite stock, and the absolute-signature endpoint | PROVED; conditioning on `e` alone does not fix `P` | `docs/229-prime-power-absolute-signature-pair-stabilization.md` |
| CMR1006--1013 | Entry-rank partition, rank-one line-clique decomposition, old-line load versus disjoint geometric secant-star extraction, higher-rank entering-pair concentration, cubic line load, gap bounds, and the entry-rank endpoint | PROVED | `docs/230-prime-power-robust-surplus-entry-rank-dichotomy.md` |
| CMR1014--1021 | Exact layer-pattern polarization, common-layer compatible outside-pair banks, protected star execution, cross-layer rooted paid pairs, explicit two-layer line-clean response, and the polarized-star endpoint | PROVED | `docs/231-prime-power-secant-star-layer-polarization.md` |
| CMR1022--1029 | Loaded-line layer split, majority-layer matching compatibility, protected-touch bound, simultaneous line absorption, robust-surplus growth formula, large-core alternative, finite two-layer line capacity, and the entering-pair endpoint | PROVED | `docs/232-prime-power-entering-pair-line-absorption.md` |
| CMR1030--1037 | Parameterized robust rank-one and higher-rank execution scales, layer-polarized protected alternatives, two-layer protected-capacity budget, finite large-growth episodes, no-growth certificates, and the robust protected-execution endpoint | PROVED | `docs/233-prime-power-robust-surplus-protected-execution.md` |

The branch still does not prove the all-`n` conjecture. Same-vertex-set dynamics,
minimum-core contraction, cross-factor potential transport, and host
representability have exact normal forms.

A minimum-robust target-destroying bank state creates at least one more new triple
than the destroyed target load. The resulting surplus is no longer anonymous.
It splits by physical entry rank:

- rank-one surplus gives one entering-cell line decomposition, hence an old loaded
  target line or a cell-disjoint geometric secant star;
- higher-rank surplus gives one entering pair with many third cells on a nonaxis
  line and therefore a majority-layer heavy-line profile.

The rank-one star is polarized by actual layer labels. A common-layer subbank
enters protected star absorption; a cross-layer subbank gives rooted same-layer
paid pairs plus an explicit opposite-layer cell response. The higher-rank line
absorbs every majority-layer cell outside the protected core.

Across both layers, total fresh protected growth is at most

\[
2n-k_0^{(0)}-k_0^{(1)}.
\]

After this capacity is saturated, further robust episodes must produce a loaded
old target line, matching-vertex wall, large protected core, cross-layer rooted
bank, cubic bank-state line load, restoration/rollback payment, structural descent,
envelope expansion, or strict potential improvement.

The active prime-power frontier is therefore the **post-saturation large-core and
cross-layer rooted-bank endpoint**. It remains to turn those outputs into an
unconditional minimum decrease, Hall/prefix/carry factorization, finite reserve
exhaustion, or closure-envelope progress. Prime-field transfer and arbitrary
side-length assembly remain necessary.
