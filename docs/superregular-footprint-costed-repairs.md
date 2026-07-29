# Superregular footprint-costed repairs

## Status

This note proves SRR2gg--SRR2gj under the free-witness repair contracts through SRR2gf. It does not construct the conditioned repair footprints, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be endpoint-disjoint unmatched-candidate/free-witness repair pairs. Every repair `e` has a nonempty footprint `F(e)` of source candidates, endpoints, blocker occurrences, bounded-cycle edges, threshold records, burden certificates, conditioned-source fields, or repair slots; a footprint-local map restoring `e` and preserving the witness matching; and a nonnegative typed resampling-cost vector `c(e)`.

Let `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## SRR2gg -- conditioned footprint conflict bound -- PROVED

The repair-overlap graph has maximum degree at most `h(beta-1)`. Greedy selection gives a footprint-disjoint family `I` with

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## SRR2gh -- disjoint conditioned repairs commute -- PROVED UNDER THE LOCALITY CERTIFICATE

Footprint-disjoint resampling repairs read and write disjoint conditioned coordinates and therefore commute. If each restores its selected candidate-witness edge and preserves every carried witness-matching edge, the repaired graph contains `M union I`; witness-assignment deficit drops by at least `|I|`.

A hidden threshold, burden, blocker, cycle, or conditioning write; a failed restored edge; or a destroyed carried edge is returned as a certificate failure.

## SRR2gi -- typed burden reserve or exact shortage -- PROVED

Let `C(I)=sum_{e in I}c(e)` and `B` be the typed resampling reserve. If `C(I)<=B` coordinatewise, execute the whole batch. Otherwise return the least source, endpoint, blocker, cycle, threshold, burden, occurrence, or repair coordinate `a` with exact shortage `C(I)_a-B_a`.

No cost may migrate between resource types. If every repair has scalar cost at most `kappa`, batch cost is at most `kappa|I|`.

## SRR2gj -- churn-funded resampling-cost ledger -- PROVED UNDER THE MACRO CONTRACT

For post-repair deficit `Delta_j`, bounded-cycle disturbance `U_j`, executed footprint-disjoint repairs `g_j`, and cumulative scalar cost `E_J`,

\[
\Delta_j\le\Delta_{j-1}+U_j-g_j
\]

and

\[
\boxed{E_J\le\kappa\sum_{j=1}^Jg_j
\le\kappa\left(\Delta_0+\sum_{j=1}^JU_j\right).}
\]

Initial typed reserve plus replenishment must cover cumulative cost; otherwise return the least exhausted coordinate before repair.

## Corrected SRR frontier

Conditioned repair descent now survives bounded footprint overlap and has an auditable burden/source cost ledger. Remaining work is to construct actual cycle/threshold/blocker repairs and footprints, prove concrete `h,beta,kappa` bounds, and establish reserve/replenishment or direct endpoint-burden payment.

## Finite check

`scripts/verify_srr_footprint_costed_repairs.py` checks conflict degrees, commuting extraction, exact reserve shortages, and churn-funded cost.