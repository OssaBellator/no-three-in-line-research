# Alternating-core synchronized repair epochs

## Status

This note proves AC5fu--AC5fy under the incremental exact-dictionary contracts for the local AC repair track and the RI, BDA, GC, OP, SRR and SAS repair tracks. It does not prove the concrete churn bounds or compatibility predicates, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Let

\[
\mathcal S=\{AC,RI,BDA,GC,OP,SRR,SAS\}
\]

be the seven typed repair ledgers active in one macro epoch. For each track `s`, let `R_s,T_s,E_s,d_s` be its incidence set, token set, exact compatibility graph and injective compatible assignment. Token types are disjoint across tracks; a cross-track pair is not a compatibility edge and cannot transfer source mass.

At the next macro epoch, track `s` has changed pair boundary `B_s`, new-incidence count `a_s`, disturbed old-assignment count `b_s`, churn

\[
u_s=a_s+b_s,
\]

and maximum matching deficit `delta_s`.

## AC5fu -- disjoint exact dictionary composition -- PROVED

The synchronized compatibility graph is the disjoint union

\[
E=\bigsqcup_{s\in\mathcal S}E_s.
\]

If each track copies its unchanged block and exactly audits its changed boundary, then the synchronized dictionary is exact. The exact number of newly evaluated pairs is

\[
\boxed{|B|=\sum_{s\in\mathcal S}|B_s|.}
\]

### Proof

Every incidence and token has one fixed track type, so the complete synchronized pair universe is the disjoint union of the seven within-track products. Exactness is therefore trackwise, and the changed boundaries are disjoint. QED.

## AC5fv -- exact synchronized deficit additivity -- PROVED

The union of the seven carried matchings is a matching. Moreover the maximum synchronized matching deficit is exactly

\[
\boxed{\delta=\sum_{s\in\mathcal S}\delta_s}
\]

and satisfies

\[
\boxed{0\le\delta\le U:=\sum_{s\in\mathcal S}u_s.}
\]

### Proof

The track graphs have disjoint incidence and token vertices, so maximum matching sizes add over connected components. Each track theorem gives `delta_s<=u_s`; sum. QED.

## AC5fw -- bounded synchronized reaugmentation or concentrated track core -- PROVED

Exactly one continuation holds:

1. all tracks are fully assignable, and the union assignment is restored using at most `U` augmenting paths in total;
2. the synchronized deficit is positive, one track satisfies
   \[
   \boxed{\delta_s\ge\lceil\delta/7\rceil,}
   \]
   and that track returns its canonical typed Hall core and missing-compatibility rectangle;
3. one pair is assigned across track types, one supposedly unchanged record is false, or one track dictionary is not exact.

### Proof

At most `u_s` augmentations are required on track `s`; sum over tracks. If `delta>0`, pigeonhole the exact additive deficit over seven tracks and apply the corresponding track Hall theorem. QED.

## AC5fx -- cumulative macro-churn budget -- PROVED

For macro epochs `j`, synchronized exact dictionaries and assignments can be maintained with at most

\[
\boxed{\sum_j\sum_{s\in\mathcal S}|B_{s,j}|}
\]

new compatibility evaluations and at most

\[
\boxed{\sum_j\sum_{s\in\mathcal S}u_{s,j}}
\]

augmenting paths.

No full seven-track product recomputation is required after bounded physical change.

### Proof

Apply AC5fu and AC5fw independently at every macro transition and sum the exact costs. QED.

## AC5fy -- no cross-ledger cancellation router -- PROVED UNDER THE TYPED TOKEN CONTRACT

Carrying, deleting or augmenting compatibility assignments creates no source, collateral, potential, donor, witness or neutral mass. Every actual debit remains in its own occurrence-faithful track ledger. Therefore one exact continuation holds:

1. every track preserves its source conservation and the synchronized repair assignment advances within the macro-churn budget;
2. one track returns a typed Hall core with deficit at most its `u_s`;
3. one track returns a boundary, repeated-debit, hidden-deposit, stale-epoch or relabelled-address failure;
4. a proposed cross-track substitution or cancellation is returned as a type violation and resets the macro argument.

### Proof

The synchronized graph is a disjoint union and matching operations only rearrange proposed pairings. They do not modify any track's issuance log. A cross-track edge would contradict the typed vertex partition. QED.

## Corrected AC6 frontier

All seven current repair frontiers now admit incremental exact-dictionary maintenance, and their synchronized deficit and work budgets add exactly. Remaining work is to prove concrete per-menu churn bounds, construct the six side-track and local AC predicates on changed boundaries, and convert the returned concentrated track Hall cores into geometric payment or descent.

## Finite check

`scripts/verify_ac_synchronized_track_epochs.py` generates seven disjoint incremental compatibility systems per macro epoch and verifies boundary additivity, exact deficit additivity, the total churn bound and deficient-track concentration.