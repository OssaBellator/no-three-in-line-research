# Alternating-core synchronized support-local churn

## Status

This note proves AC5gd--AC5gg under the synchronized track-key contracts through AC5gc and the six side-track support-local contracts. It does not construct the concrete physical dependency dictionaries, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Let `S={AC,RI,BDA,GC,OP,SRR,SAS}` be the seven typed repair tracks. For each track `s`, one macro edit has a declared primitive support `P_s`, with `1<=|P_s|<=H_s`. Changed/new incidence records, changed/new next tokens, and changed/deleted old tokens declare dependency sets meeting `P_s`.

Let `alpha^R_s`, `alpha^+_s`, and `alpha^-_s` be the maximum numbers of those three record types depending on one touched primitive. Let `L^T_s,L^R_s` be the compatible track-key fibre bounds.

## AC5gd -- exact synchronized support witness -- PROVED UNDER THE DEPENDENCY CONTRACTS

Every changed record has one least typed support cause `(s,x)` with `x in P_s`. A missing dependency, changed record disjoint from its support, hidden track or key change, cross-track relabelling, or undeclared global reset is returned as a first exact failure.

No support cause may migrate between track types, because the synchronized compatibility graph and the occurrence-faithful ledgers are disjoint by track.

## AC5ge -- synchronized support-local work and deficit bounds -- PROVED

For one macro transition, the total number of fresh compatibility evaluations is at most

\[
\boxed{
\sum_s H_s(\alpha^R_sL^T_s+\alpha^+_sL^R_s).
}
\]

The total initially disturbed matching roots and the maximum synchronized deficit satisfy

\[
\boxed{
\delta\le U\le\sum_s H_s(\alpha^R_s+\alpha^-_s).
}
\]

When complete assignment is possible, at most the displayed upper bound on `U` augmenting paths restores all seven assignments. Matching maintenance creates no collateral, potential, donor, source, witness or neutral mass.

### Proof

Apply the support-incidence bounds and key-local audit theorem separately on every track, then sum over the disjoint track graphs. The synchronized matching deficit is the sum of the track-key deficits. QED.

## AC5gf -- typed support concentration of residual deficit -- PROVED

Extend the synchronized carried matching to a maximum matching using within-track augmenting paths. Every remaining unmatched incidence belongs to the initial support-disturbed set on its own track. Give it the least typed support cause `(s,x)`.

Put

\[
P=\sum_s |P_s|.
\]

If the synchronized deficit is `delta>0`, one typed primitive `(s,x)` anchors at least

\[
\boxed{\left\lceil\delta/P\right\rceil}
\]

unmatched roots. Each root has a closed alternating search inside one track-key component and no path to a free compatible token. Thus failure is localized to one frontier, one compatibility key, and one touched physical primitive.

### Proof

Augmentations start from initially unmatched roots, so residual roots remain a subset of that set. Their least causes lie in the `P` typed support primitives. Pigeonhole, then use maximality of the matching. QED.

## AC5gg -- cumulative support-budget router -- PROVED UNDER THE MACRO CONTRACT

Across macro epochs `j`, exact dictionaries and assignments require at most

\[
\boxed{
\sum_j\sum_s H_{s,j}(\alpha^R_{s,j}L^T_{s,j}+\alpha^+_{s,j}L^R_{s,j})
}
\]

fresh predicate evaluations and at most

\[
\boxed{
\sum_j\sum_s H_{s,j}(\alpha^R_{s,j}+\alpha^-_{s,j})
}
\]

augmenting paths. One exact continuation holds:

1. all track ledgers remain conserved and the macro repair advances inside the support budget;
2. one track-key component returns a Hall core whose unmatched roots are anchored to one touched primitive;
3. one nonlocal dependency, boundary, stale-epoch, repeated-debit, hidden-deposit or relabelled-address failure occurs;
4. a proposed cross-track or cross-support cancellation is returned as a type violation.

## Corrected AC6 frontier

The synchronized repair cost is now controlled by physical support size, primitive record incidence and compatible key fibres. Remaining work is to construct the concrete dependency dictionaries, prove the numerical `H_s,alpha_s,L_s` bounds for each menu operation, and convert the support-anchored track-key obstruction into payment, descent, reset or replenishment sufficient for a recurrent AC6 macro cycle.

## Finite check

`scripts/verify_ac_synchronized_support_local_churn.py` generates seven keyed support-local matching systems per macro epoch and checks support incidence bounds, synchronized audit and deficit bounds, and typed primitive concentration of every residual deficit.