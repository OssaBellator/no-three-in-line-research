# Rational-inverse footprint-costed repairs

## Status

This note proves RI5hq--RI5ht under the free-token repair contracts through RI5hp. It does not construct the arithmetic repair footprints, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be an endpoint-disjoint family of repairable unmatched-incidence/free-collateral pairs from RI5ho. Each repair `e` carries:

- a nonempty physical footprint `F(e)` of grid cells, owner occurrences, blocker slots, arithmetic fields, charge resources, or boundary records;
- a local state map which reads and writes only `F(e)`, restores the edge `e`, and preserves every carried matching edge;
- a nonnegative typed cost vector `c(e)` in the occurrence-faithful RI resource ledger.

Put `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## RI5hq -- footprint conflict bound -- PROVED

Join two repairs when their footprints intersect. Every repair conflicts with at most

\[
\boxed{h(\beta-1)}
\]

other repairs. Indeed each of at most `h` primitives lies in at most `beta-1` other footprints, and the union bound may only overcount.

Consequently greedy selection gives a footprint-disjoint subfamily `I` with

\[
\boxed{|I|\ge \left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## RI5hr -- disjoint footprints commute and descend -- PROVED UNDER THE LOCALITY CERTIFICATE

Repairs in `I` read and write disjoint state coordinates, so their maps commute. Each preserves the old matching and restores one edge joining an unmatched incidence to a free collateral token. Therefore all repairs in `I` may be executed in any order and the repaired graph contains the matching

\[
M\cup I.
\]

The collateral deficit drops by at least `|I|`. A missing footprint, an undeclared write, failure to restore the selected edge, or destruction of a carried edge is returned as the first exact repair-certificate failure.

## RI5hs -- typed reserve or exact shortage -- PROVED

Let

\[
C(I)=\sum_{e\in I}c(e)
\]

and let `B` be the available typed RI reserve. If `C(I)<=B` coordinatewise, the whole commuting batch is admissible and gives deficit descent `|I|`. Otherwise the least coordinate `a` with `C(I)_a>B_a` gives the exact shortage

\[
\boxed{C(I)_a-B_a>0.}
\]

No cost may migrate between collateral, blocker, owner, arithmetic, charge, or boundary coordinates.

If every repair has scalar cost at most `kappa`, then the batch cost is at most `kappa|I|`.

## RI5ht -- churn-funded repair-cost ledger -- PROVED UNDER THE MACRO CONTRACT

Across epochs, let `Delta_j` be the post-repair collateral deficit, `U_j` the support-local disturbance, `g_j` the number of executed footprint-disjoint repairs, and `E_J` their cumulative scalar cost. Then

\[
\Delta_j\le \Delta_{j-1}+U_j-g_j,
\]

and if every repair costs at most `kappa`,

\[
\boxed{E_J\le \kappa\sum_{j=1}^J g_j
\le \kappa\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

Thus repair expenditure is funded by initial deficit and declared physical churn. If initial reserve plus replenishment does not cover the typed cumulative vector, the least exhausted coordinate is returned instead of an uncharged repair.

## Corrected RI6 frontier

RI repair descent now survives bounded footprint overlap and has an explicit typed cost ledger. Remaining work is to construct the actual arithmetic repair maps and footprints, prove numerical `h,beta,kappa` bounds, and show the physical reserve/replenishment covers the cost or yields direct geometric payment.

## Finite check

`scripts/verify_ri_footprint_costed_repairs.py` checks conflict degrees, greedy commuting extraction, exact reserve shortages, deficit descent, and the churn-funded cost inequality.