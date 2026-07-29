# Alternating-core synchronized footprint-costed repairs

## Status

This note proves AC5gt--AC5gw under the synchronized free-token repair contracts through AC5gs and the six side-track footprint-cost contracts. It does not construct the physical repair maps, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Let `Q` be a synchronized endpoint-disjoint family of unmatched-incidence/free-token repair pairs, possibly drawn from several of the AC, RI, BDA, GC, OP, SRR, and SAS tracks. Every repair `e` carries:

- its fixed track type `s(e)`;
- a nonempty global physical footprint `F(e)` containing every track-local and shared-state primitive read or written;
- a footprint-local map restoring `e`, preserving the synchronized matching and every other track dictionary;
- a nonnegative typed cost vector `c(e)` supported only on the ledger coordinates of `s(e)`.

Put `h=max_e |F(e)|` and `beta=max_x |{e:x in F(e)}|`, where shared physical primitives are not duplicated by track labels.

## AC5gt -- global repair-footprint conflict bound -- PROVED

Join two repairs when their global footprints intersect. Every repair conflicts with at most

\[
\boxed{h(\beta-1)}
\]

others. Greedy selection gives a globally footprint-disjoint family `I` satisfying

\[
\boxed{|I|\ge\left\lceil\frac{|Q|}{h(\beta-1)+1}\right\rceil.}
\]

This bound includes both within-track and cross-track physical interference.

## AC5gu -- synchronized disjoint repairs commute and descend -- PROVED UNDER THE LOCALITY CERTIFICATES

Repairs in `I` read and write disjoint global physical coordinates, hence commute. Each preserves the old synchronized matching, restores its own unmatched-incidence/free-token edge, and preserves every other track dictionary. Therefore the repaired union contains `M union I` and synchronized deficit drops by at least `|I|`.

A hidden shared-state write, cross-track dictionary change, destroyed carried edge, failed restored edge, or incorrect track type is returned as the first exact certificate failure.

## AC5gv -- typed reserve or exact synchronized shortage -- PROVED

Let `C(I)=sum_{e in I}c(e)` and `B` be the synchronized typed reserve. If `C(I)<=B` coordinatewise, execute the entire commuting family. Otherwise the least typed coordinate `(s,a)` with `C(I)_{s,a}>B_{s,a}` returns exact shortage

\[
\boxed{C(I)_{s,a}-B_{s,a}>0.}
\]

Costs cannot migrate across tracks or between resource types within a track.

## AC5gw -- trackwise churn-funded cost envelope -- PROVED UNDER THE MACRO CONTRACT

Let `Delta_j` be synchronized post-repair deficit, `U_j` physical matching disturbance, and `g_{s,j}` the executed footprint-disjoint repairs of track `s`. Then

\[
\Delta_j\le\Delta_{j-1}+U_j-\sum_s g_{s,j}.
\]

If every track-`s` repair has scalar cost at most `kappa_s`, its cumulative expenditure satisfies

\[
\boxed{E_{s,J}\le\kappa_s\sum_{j=1}^Jg_{s,j}.}
\]

Writing `kappa_* = max_s kappa_s`,

\[
\boxed{\sum_sE_{s,J}
\le\kappa_*\left(\Delta_0+\sum_{j=1}^JU_j\right).}
\]

For every typed coordinate, initial reserve plus cumulative replenishment must cover cumulative expenditure. Otherwise the first exhausted track-coordinate is returned and no uncharged repair is performed.

## Corrected AC6 frontier

Synchronized repair descent now survives bounded physical overlap, including cross-track shared-state interference, and every successful repair has a typed churn-funded cost. Remaining work is to construct the actual track repair maps and global footprints, prove concrete overlap and cost constants, establish reserve/replenishment inequalities, and combine the resulting cost envelope with finite macro-state recurrence.

## Finite check

`scripts/verify_ac_footprint_costed_repairs.py` generates seven-track typed repair systems and checks global conflict degrees, commuting extraction, typed reserve shortages, trackwise costs, and the cumulative churn-funded envelope.