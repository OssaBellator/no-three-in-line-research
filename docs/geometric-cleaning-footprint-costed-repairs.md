# Geometric-cleaning footprint-costed repairs

## Status

This note proves GC2mx--GC2na under the free-donor repair contracts through GC2mw. It does not construct the geometric repair footprints, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be endpoint-disjoint unmatched-remedy/free-donor repair pairs. Every repair `e` has a nonempty footprint `F(e)` of moved cells, protected events, chart records, donor occurrences, remedy slots, height certificates, or boundary resources; a footprint-local map restoring `e` and preserving the donor matching; and a nonnegative typed geometric cost vector `c(e)`.

Let `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## GC2mx -- geometric footprint conflict bound -- PROVED

The repair-overlap graph has maximum degree at most `h(beta-1)`. Hence greedy selection returns a footprint-disjoint family `I` satisfying

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## GC2my -- disjoint cleaning repairs commute -- PROVED UNDER THE LOCALITY CERTIFICATE

Footprint-disjoint cleaning maps read and write disjoint geometric coordinates and therefore commute. If each restores its remedy-donor edge and preserves every carried donor-matching edge, the repaired graph contains `M union I`; donor-assignment deficit drops by at least `|I|`.

A hidden chart write, undeclared protected-event change, failed restored edge, or destroyed carried edge is returned as a certificate failure.

## GC2mz -- geometric reserve or exact shortage -- PROVED

Put `C(I)=sum_{e in I}c(e)` and let `B` be the typed cleaning reserve. If `C(I)<=B` coordinatewise, execute the batch. Otherwise return the least chart, height, donor, remedy, protected-event, occurrence, or boundary coordinate `a` with exact shortage `C(I)_a-B_a`.

If every repair has scalar cost at most `kappa`, total batch cost is at most `kappa|I|`. Repair extraction creates no donor mass and cannot transfer credit between geometric ledger types.

## GC2na -- churn-funded geometric-cost ledger -- PROVED UNDER THE MACRO CONTRACT

For post-repair deficit `Delta_j`, physical disturbance `U_j`, executed footprint-disjoint repairs `g_j`, and cumulative scalar cost `E_J`,

\[
\Delta_j\le\Delta_{j-1}+U_j-g_j
\]

and

\[
\boxed{E_J\le\kappa\sum_{j=1}^Jg_j
\le\kappa\left(\Delta_0+\sum_{j=1}^JU_j\right).}
\]

Initial typed reserve and replenishment must cover the cumulative vector; otherwise the least exhausted coordinate is returned before repair.

## Corrected GC5 frontier

Cleaning repair descent now survives bounded footprint overlap and has an auditable typed geometric cost. Remaining work is to construct actual chart/protected-event repairs and footprints, prove concrete `h,beta,kappa` bounds, and establish reserve/replenishment or direct protected-height payment.

## Finite check

`scripts/verify_gc_footprint_costed_repairs.py` checks overlap degrees, greedy commuting extraction, exact reserve shortages, and the churn-funded cost ledger.