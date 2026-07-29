# Sparse algebraic footprint-costed repairs

## Status

This note proves SAS5nw--SAS5nz under the free-neutral repair contracts through SAS5nv. It does not construct the sparse repair footprints, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be endpoint-disjoint unmatched pair/completion-incidence to free-neutral repair pairs. Every repair `e` has a nonempty footprint `F(e)` of moved rows or cells, swap positions, arithmetic-profile fields, orientation records, legality guards, boundary records, pair/completion slots, owner occurrences, or lineage records; a footprint-local map restoring `e` and preserving the neutral matching; and a nonnegative typed sparse-cost vector `c(e)`.

Let `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## SAS5nw -- sparse footprint conflict bound -- PROVED

The overlap graph on repairs has maximum degree at most `h(beta-1)`. Hence greedy selection gives a footprint-disjoint family `I` satisfying

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## SAS5nx -- disjoint sparse repairs commute -- PROVED UNDER THE LOCALITY CERTIFICATE

Repairs in `I` read and write disjoint sparse-state coordinates and therefore commute. If every repair restores its selected pair/completion-neutral edge and preserves every carried neutral-matching edge, the repaired graph contains `M union I`; neutral-assignment deficit drops by at least `|I|`.

A hidden sign, profile, move, orientation, legality, boundary, or lineage write; a failed restored edge; or a destroyed carried edge is returned as a certificate failure.

## SAS5ny -- typed sparse reserve or exact shortage -- PROVED

Let `C(I)=sum_{e in I}c(e)` and let `B` be the typed sparse reserve. If `C(I)<=B` coordinatewise, execute the whole batch. Otherwise return the least row/cell, swap, profile, orientation, legality, boundary, owner, occurrence, neutral, or lineage coordinate `a` with exact shortage `C(I)_a-B_a`.

No cost may migrate between resource types. If every repair has scalar cost at most `kappa`, total batch cost is at most `kappa|I|`.

## SAS5nz -- churn-funded sparse-cost ledger -- PROVED UNDER THE MACRO CONTRACT

For post-repair deficit `Delta_j`, sparse-move disturbance `U_j`, executed footprint-disjoint repairs `g_j`, and cumulative scalar cost `E_J`,

\[
\Delta_j\le\Delta_{j-1}+U_j-g_j
\]

and

\[
\boxed{E_J\le\kappa\sum_{j=1}^Jg_j
\le\kappa\left(\Delta_0+\sum_{j=1}^JU_j\right).}
\]

Initial typed reserve plus replenishment must cover cumulative cost; otherwise return the least exhausted coordinate before repair.

## Corrected SAS6 frontier

Sparse repair descent now survives bounded footprint overlap and has an auditable neutral/orientation/lineage cost ledger. Remaining work is to construct actual move/legality/orientation repairs and footprints, prove concrete `h,beta,kappa` bounds, and establish reserve/replenishment or direct sparse payment.

## Finite check

`scripts/verify_sas_footprint_costed_repairs.py` checks conflict degrees, commuting extraction, exact reserve shortages, and churn-funded cost.