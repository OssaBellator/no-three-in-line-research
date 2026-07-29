# Orbit-phase footprint-costed repairs

## Status

This note proves OP4gw--OP4gz under the free-source repair contracts through OP4gv. It does not construct the unit-sensitive repair footprints, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be endpoint-disjoint unmatched residual/edit-incidence to free-source repair pairs. Every repair `e` has a nonempty footprint `F(e)` of quotient coordinates, residual/edit slots, action records, owner occurrences, unit/valuation fields, holonomy records, carry fields, or boundary contexts; a footprint-local map restoring `e` and preserving the source matching; and a nonnegative typed phase-cost vector `c(e)`.

Let `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`.

## OP4gw -- phase footprint conflict bound -- PROVED

The overlap graph on candidate repairs has maximum degree at most `h(beta-1)`. Greedy selection therefore gives a footprint-disjoint family `I` with

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

## OP4gx -- disjoint phase repairs commute -- PROVED UNDER THE LOCALITY CERTIFICATE

Repairs in `I` read and write disjoint quotient-phase coordinates, so their maps commute. If each restores its selected residual/edit-source edge and preserves every carried source-matching edge, the repaired graph contains `M union I` and the source-assignment deficit drops by at least `|I|`.

An undeclared quotient, unit, valuation, holonomy, carry, or boundary write; a failed restored edge; or a destroyed carried edge is returned as a certificate failure.

## OP4gy -- typed phase reserve or exact shortage -- PROVED

Let `C(I)=sum_{e in I}c(e)` and let `B` be the available typed phase reserve. If `C(I)<=B` coordinatewise, execute the entire commuting batch. Otherwise the least coordinate `a` with `C(I)_a>B_a` returns exact shortage `C(I)_a-B_a`.

No cost may migrate between source, residual, edit, unit, valuation, holonomy, carry, owner, occurrence, or boundary ledgers. If every repair has scalar cost at most `kappa`, the batch cost is at most `kappa|I|`.

## OP4gz -- churn-funded phase-cost ledger -- PROVED UNDER THE MACRO CONTRACT

For post-repair deficit `Delta_j`, support-local disturbance `U_j`, executed footprint-disjoint repairs `g_j`, and cumulative scalar phase cost `E_J`,

\[
\Delta_j\le\Delta_{j-1}+U_j-g_j
\]

and

\[
\boxed{E_J\le\kappa\sum_{j=1}^Jg_j
\le\kappa\left(\Delta_0+\sum_{j=1}^JU_j\right).}
\]

If initial phase reserve plus replenishment does not cover the cumulative typed vector, return the least exhausted coordinate before repair.

## Corrected OP5 frontier

Phase repair descent now survives bounded footprint overlap and has an auditable typed cost ledger. Remaining work is to construct the actual quotient/action/unit/holonomy repair maps and footprints, prove concrete `h,beta,kappa` bounds, and establish phase reserve/replenishment or direct ledger payment.

## Finite check

`scripts/verify_op_footprint_costed_repairs.py` checks conflict degrees, commuting extraction, exact reserve shortages, and churn-funded cost.