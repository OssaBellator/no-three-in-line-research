# Sparse algebraic key-local neutral epochs

## Status

This note proves SAS5nc--SAS5nf under the exact pair/completion neutral and incremental contracts through SAS5nb. It does not construct the boundary-neutral key dictionary, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Give every pair/completion incidence and neutral token a complete coarse key containing sign, profile, move type, legality class, boundary class, orientation, repair class and occurrence type. Compatibility implies equal keys. Any changed move, sign, legality or orientation key makes the record changed.

## SAS5nc -- exact neutral-key decomposition -- PROVED UNDER THE KEY CONTRACT

Cross-key pairs are certified nonedges and the exact neutral compatibility graph is the disjoint union of within-key graphs. A cross-key edge or hidden sign/profile/move/legality change is an exact failure.

## SAS5nd -- key-local boundary and audit bound -- PROVED

For `R'=R^circ sqcup Delta R`, `T'=T^circ sqcup Delta T`, the fresh boundary is

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k).
\]

Thus

\[
\boxed{|\mathcal B^\kappa|=\sum_k(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|).}
\]

If `a=|Delta R|`, `c=|Delta T|`, `L_T=max_k|T'_k|`, and `L_R=max_k|R_k^circ|`, then

\[
\boxed{|\mathcal B^\kappa|\le aL_T+cL_R.}
\]

The copied unchanged within-key graph plus the exact fresh boundary is the complete next dictionary.

## SAS5ne -- neutral-token disturbance bound -- PROVED

Let `e=|T\setminus T^circ|` count old neutral tokens deleted, changed or relabelled. Injectivity of the old pair/completion assignment gives

\[
\boxed{b\le e,
\qquad u=a+b\le a+e.}
\]

Carrying the assignment creates no neutral mass and changes no orientation payment.

## SAS5nf -- bounded sparse-edit router -- PROVED UNDER THE EDIT CONTRACT

If one sparse move changes at most `A` pair/completion incidences, introduces at most `C_+` changed/new neutral records, changes or deletes at most `C_-` old neutral records, and has key-fibre bounds `L_R,L_T`, then:

1. at most `AL_T+C_+L_R` boundary-neutral predicate evaluations are needed;
2. at most `A+C_-` augmenting paths restore assignment;
3. otherwise the boundary-neutral Hall deficit is at most `A+C_-`;
4. or one sign, profile, move, legality, boundary, orientation, epoch or occurrence key fails.

## Corrected SAS6 frontier

Sparse assignment maintenance is now local in changed records and compatible neutral fibres. Remaining work is to prove concrete move-churn and key-fibre bounds, establish the physical predicate on the audited boundary, and pay bounded Hall cores or lineage failures.

## Finite check

`scripts/verify_sas_key_local_neutral_epochs.py` checks exact key decomposition, within-key reconstruction, fibre bounds, neutral-token disturbance and matching deficit bounds.