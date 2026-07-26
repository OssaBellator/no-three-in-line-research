# Geometric-cleaning theorem index

This index is branch-specific. The shared proved inputs remain documented on `main`; only the additional geometric-cleaning statements are classified here.

| ID | Statement | Status | Location |
|---|---|---|---|
| GC1-wall | Installed bounded blocks can eliminate every partner | PROVED | `docs/geometric-cleaning-budget-and-wall.md` |
| GC1a | Separate partner-blocker caps imply uniform admissible density | PROVED | `docs/geometric-cleaning-load-accounting.md` |
| GC1b | Restricting a pool to fraction `rho` changes blocker density `delta` to at most `delta/rho` | PROVED | `docs/geometric-cleaning-pool-and-shadow-stability.md` |
| GC1c–GC1f | Physical support, exact non-axis lines and explicit residual partners give a complete per-target blocker budget and direct `K/p`-spread entry criterion | PROVED | `docs/geometric-cleaning-partner-blocker-inventory.md` |
| GC2-wall | Uniform latent anchor load survives small target deletion | PROVED | `docs/geometric-cleaning-load-accounting.md` |
| GC2a | Target and partner restriction is monotone for possible-cell pair-shadow | PROVED | `docs/geometric-cleaning-pool-and-shadow-stability.md` |
| GC2b | One genuinely new possible cell contributes at most `3(ell_H-2)_+/2` pair-shadow at one unchanged anchor | PROVED | `docs/geometric-cleaning-new-cell-event-inventory.md` |
| GC2c–GC2f | Weighted line-blocked partners route to one role-pure current-anchor star or an endpoint-disjoint secant matching retaining `1/[2(2Delta-1)]` of the weight | PROVED | `docs/geometric-cleaning-line-blocker-router.md` |
| GC2g–GC2j | Incidence-resolved correction gain pays at least a `1/r` fraction on current factors; paid stars/matchings recur only through ledger growth or executable chargeback | PROVED; LATENT USE REQUIRES THE SOURCE-PAYMENT CONTRACT | `docs/geometric-cleaning-paid-secant-chargeback.md` |
| GC2k–GC2n | A dangerous cross-cell secant line avoids both removed cells, so direct same-line payment is impossible; any valid transfer must use a different destroyed factor with bounded source congestion | PROVED; PAYMENT AFTER A CROSS-LINE SOURCE MAP | `docs/geometric-cleaning-source-transfer-wall.md` |
| GC2o–GC2r | Partner-private destroyed factors have reuse at most their rank and give automatic `r*kappa`-congestion payment; failure localizes to source-free, target-common or private-underweight mass | PROVED UNDER THE LOCAL DOMINANCE PARAMETER `kappa` | `docs/geometric-cleaning-partner-private-source-transfer.md` |
| GC2s–GC2v | Aggregate private capacity pays fractionally with rank loss `r`; all target-common factors form one shared pool paying with loss `kappa`, and failure is an exact source-free or capacity-overload witness | PROVED UNDER THE AGGREGATE DOMINANCE PARAMETER `kappa` | `docs/geometric-cleaning-shared-source-capacity.md` |
| GC2w–GC2aa | Source-free corrections are exactly isolated deleted pairs; aggregate-private and target-link failures produce exact factor families with demand/capacity ratio greater than `kappa` | PROVED | `docs/geometric-cleaning-overload-structure.md` |
| GC2ab–GC2af | Capacity overload has positive exact excess equal to the dominance deficit; a rank split sends it to lower-rank concentration, high pair codegree or a GC4 endpoint-disjoint overload-demand star | PROVED; PAYMENT STILL REQUIRES CAPACITY NORMALIZATION OR HALL-DEFICIENCY USE | `docs/geometric-cleaning-overload-anchor-import.md` |
| GC3a | Paid partner consumption bounds total pool depletion | PROVED | `docs/geometric-cleaning-budget-and-wall.md` |
| GC3b | Paid incidence bounds creation of exceptional anchors | PROVED | `docs/geometric-cleaning-load-accounting.md` |
| GC3c–GC3d | Pair-shadow threshold crossings equal new-cell pair incidence and admit a margin/reuse charging bound | PROVED | `docs/geometric-cleaning-pool-and-shadow-stability.md` |
| GC3e–GC3f | `k` newly possible assignments increase one anchor load by at most `3k(ell_H-2)_+` and give an explicit threshold-crossing inventory | PROVED | `docs/geometric-cleaning-new-cell-event-inventory.md` |
| GC3g–GC3i | Newly enabled assignments route to exact changed causes; bounded cause degree and finite atom tickets give pathwise pair-shadow stability | PROVED UNDER THE CAUSE-TICKET CONTRACT FOR GC3i | `docs/geometric-cleaning-admissibility-cause-router.md` |
| GC3j–GC3n | Rectangle cells have exact role degrees, bounded physical supports and non-axis lines have explicit cause loads, and all excess load localizes to one global context/generator atom | PROVED | `docs/geometric-cleaning-rectangle-cause-degrees.md` |
| GC4a | High-load peeling yields a capped residual or fresh-weight witness | PROVED | `docs/geometric-cleaning-conflict-peeling.md` |
| GC4b | A high-load triple anchor yields pair concentration or an endpoint-disjoint star | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4c | Bounded pair codegree preserves weighted load in an endpoint-disjoint star | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4d | A bounded-codegree peeling prefix yields disjoint fresh stars with linear total weight | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4e | Weighted star conflicts yield a paid overload or a constant-fraction installable family | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4f | A paid cross-star overload localizes and descends inside one certificate label | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4g | Certificate-labelled star recursion has a strict finite-support potential | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4h | One scalar potential terminates strict star descents mixed with bounded paid reopenings | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4i | Capacitated Hall inequalities characterize current-incidence payments for star reopenings | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4j | Minimum paid incidence and bounded token reuse imply the star-reopening Hall condition | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4k | A Hall-deficient paid incidence contains a same-label compatible fan or a conflict overload | PROVED | `docs/geometric-cleaning-anchor-link.md` |
| GC4l | A weighted deficient fibre retains at least `1/(T(Γ+1))` of its star weight in one compatible role class, unless it has degree greater than `Γ` | PROVED | `docs/geometric-cleaning-weighted-labelled-fan.md` |
| GC5a–GC5c | Near-complete clone local load or dense two-layer global triple mass gives an exact all-`n` endpoint; endpoint failure returns explicit hole/load/mass witnesses | PROVED | `docs/geometric-cleaning-all-n-endpoint-router.md` |
| GC5 | Clean-host endpoint theorem | OPEN; FIXED-TARGET CAPACITY OVERLOAD NOW LOCALIZES TO LOWER-RANK, HIGH-PAIR OR ENDPOINT-DISJOINT GC4 DEMAND STRUCTURE, WITH CAPACITY-NORMALIZED PAYMENT/HALL USE, GC4 LABELLED RECURSION, ISOLATED-CELL PROSPECTIVE STARS, POOL DEPLETION, GLOBAL CONTEXT CAUSES AND LOCAL SUPERREGULAR RESAMPLING REMAINING | `docs/geometric-cleaning.md` |

No row in this file upgrades the global conjecture.
