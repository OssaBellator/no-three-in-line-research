# Bounded-denominator footprint-costed repairs

## Status

This note proves BDA5hz--BDA5ic under the free-potential repair contracts through BDA5hy. It does not construct the rational-gain repair footprints, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be endpoint-disjoint repair-incidence/free-potential pairs. Every repair `e` has a nonempty footprint `F(e)` of context cells, restoration gates, line records, owner occurrences, gain/damping fields, arithmetic certificates, or boundary resources; a footprint-local state map restoring `e` while preserving the carried matching; and a nonnegative typed potential-cost vector `c(e)`.

Put `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## BDA5hz -- restoration footprint conflict bound -- PROVED

The overlap graph on repairs has maximum degree at most

\[
\boxed{h(\beta-1)}.
\]

Hence greedy selection returns a footprint-disjoint family `I` with

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## BDA5ia -- disjoint restoration repairs commute -- PROVED UNDER THE LOCALITY CERTIFICATE

Footprint-disjoint repair maps read and write disjoint physical coordinates, so they commute. If every map restores its selected repair-potential edge and preserves all carried matching edges, the repaired graph contains `M union I`; the potential-assignment deficit drops by at least `|I|`.

A missing footprint, undeclared write, failed restored edge, or destroyed carried edge is returned as the first exact certificate failure.

## BDA5ib -- typed potential reserve or shortage -- PROVED

Let `C(I)=sum_{e in I} c(e)` and let `B` be the available typed restoration reserve. If `C(I)<=B` coordinatewise, execute the whole batch. Otherwise the least coordinate `a` with `C(I)_a>B_a` returns exact shortage `C(I)_a-B_a`.

No cost may migrate between gate, source, gain, damping, line, owner, arithmetic, occurrence, or boundary ledgers. If every repair has scalar cost at most `kappa`, batch cost is at most `kappa|I|`.

## BDA5ic -- churn-funded restoration-cost ledger -- PROVED UNDER THE MACRO CONTRACT

Let `Delta_j` be post-repair potential deficit, `U_j` physical matching disturbance, `g_j` executed footprint-disjoint repairs, and `E_J` cumulative scalar repair cost. Then

\[
\Delta_j\le\Delta_{j-1}+U_j-g_j
\]

and

\[
\boxed{E_J\le\kappa\sum_{j=1}^J g_j
\le\kappa\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

If initial typed reserve plus replenishment fails to cover cumulative cost, return the least exhausted coordinate rather than performing an uncharged repair.

## Corrected BDA6 frontier

Restoration repair descent now survives bounded physical overlap and carries an explicit potential-cost ledger. Remaining work is to construct the real repair maps and footprints, prove numerical `h,beta,kappa` bounds, and establish sufficient restoration reserve/replenishment or direct payment.

## Finite check

`scripts/verify_bda_footprint_costed_repairs.py` checks conflict bounds, commuting extraction, exact reserve shortages, and churn-funded repair cost.