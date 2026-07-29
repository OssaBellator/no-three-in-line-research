# Alternating-core synchronized key-local epochs

## Status

This note proves AC5fz--AC5gc under the synchronized incremental contracts through AC5fy and the six side-track key-local contracts. It does not prove the concrete physical key-fibre or churn bounds, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Let `S={AC,RI,BDA,GC,OP,SRR,SAS}`. For each track `s`, let `K_s` be its ordered coarse compatibility-key set. Compatibility is allowed only inside one track and one equal key. Write `R'_{s,k}`, `T'_{s,k}`, `Delta R_{s,k}`, `Delta T_{s,k}` and `R^circ_{s,k}` for the corresponding fibres.

## AC5fz -- exact track-key decomposition -- PROVED UNDER THE KEY CONTRACTS

The synchronized compatibility graph is the disjoint union

\[
\boxed{
E'=\bigsqcup_{s\in S}\bigsqcup_{k\in K_s}E'_{s,k}.
}
\]

Cross-track and cross-key pairs are certified nonedges. A changed key is a changed record; a proposed edge across a track or key boundary is an exact type failure.

## AC5ga -- exact synchronized key-local boundary -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B_{s,k}=
(\Delta R_{s,k}\times T'_{s,k})
\sqcup
(R^\circ_{s,k}\times\Delta T_{s,k}).
\]

Therefore the total number of new predicate evaluations is exactly

\[
\boxed{
|\mathcal B^\kappa|=
\sum_s\sum_k
\bigl(|\Delta R_{s,k}||T'_{s,k}|+
|R^\circ_{s,k}||\Delta T_{s,k}|\bigr).
}
\]

Copying every exact unchanged track-key block and auditing this boundary reconstructs the complete synchronized dictionary.

## AC5gb -- bounded macro-edit work and deficit -- PROVED

For track `s`, put

\[
A_s\ge |\Delta R_s|,
\quad C^+_s\ge|\Delta T_s|,
\quad C^-_s\ge|T_s\setminus T_s^\circ|,
\]

and let `L^T_s=max_k|T'_{s,k}|`, `L^R_s=max_k|R^circ_{s,k}|`. Then one macro transition needs at most

\[
\boxed{
\sum_s(A_sL^T_s+C^+_sL^R_s)
}
\]

new compatibility evaluations. Its total carried matching disturbance and maximum synchronized deficit satisfy

\[
\boxed{
\delta\le U\le\sum_s(A_s+C^-_s).
}
\]

At most this many augmenting paths restore all assignments when complete assignment is possible. Matching maintenance creates no track resource mass.

## AC5gc -- exact track-key deficit localization -- PROVED

Let `delta_{s,k}` be the maximum matching deficit in component `(s,k)`. Then

\[
\boxed{
delta=\sum_s\sum_k\delta_{s,k}.
}
\]

If `delta>0` and `M` track-key components are active, one component satisfies

\[
\boxed{
\delta_{s,k}\ge\left\lceil\frac{\delta}{M}\right\rceil.
}
\]

That exact track and key return their canonical typed Hall core and missing-compatibility rectangle. Thus a synchronized failure is localized not merely to one frontier but to one physical compatibility key inside that frontier.

Across macro epochs, the displayed key-local evaluation and churn bounds add. Cross-ledger or cross-key cancellation remains forbidden.

## Corrected AC6 frontier

All current repair dictionaries now admit track-key-local incremental maintenance. The remaining AC6 task is to prove concrete menu-step bounds `A_s,C_s^+,C_s^-`, compatible fibre bounds `L_s^R,L_s^T`, and geometric payment or descent for the returned bounded track-key Hall core.

## Finite check

`scripts/verify_ac_synchronized_key_local_epochs.py` generates seven keyed incremental systems per macro epoch and checks exact key-boundary additivity, fibre bounds, disturbance bounds, exact track-key deficit additivity and deficient-component concentration.