# Superregular key-local witness epochs

## Status

This note proves SRR2fm--SRR2fp under the exact candidate/witness and incremental contracts through SRR2fl. It does not construct the conditioned key dictionary, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Assign every candidate incidence and witness token a complete coarse key containing threshold band, burden class, conditioned-source class, repair class and occurrence type. Compatibility implies equal keys. A changed threshold, burden or conditioning key makes the record changed.

## SRR2fm -- exact conditioned-key decomposition -- PROVED UNDER THE KEY CONTRACT

Cross-key candidate/witness pairs are certified nonedges and the compatibility graph is the disjoint union of its within-key graphs. Any cross-key edge or hidden threshold/conditioning key change is a first failure.

## SRR2fn -- key-local boundary formula -- PROVED

For `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`, fresh evaluation is needed exactly on

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k).
\]

Hence

\[
\boxed{|\mathcal B^\kappa|=\sum_k(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|).}
\]

Copying exact unchanged within-key blocks and auditing this boundary gives the exact next dictionary.

## SRR2fo -- fibre and witness-disturbance bounds -- PROVED

Let `a=|Delta R|`, `c=|Delta T|`, `L_T=max_k|T'_k|`, and `L_R=max_k|R_k^circ|`. Then

\[
\boxed{|\mathcal B^\kappa|\le aL_T+cL_R.}
\]

If `e=|T\setminus T^circ|` counts old witnesses changed, deleted or relabelled, injectivity gives

\[
\boxed{b\le e,
\qquad u=a+b\le a+e.}
\]

## SRR2fp -- bounded resampling-edit router -- PROVED UNDER THE EDIT CONTRACT

If one bounded-cycle resampling step changes at most `A` candidate incidences, introduces at most `C_+` changed/new witness records, changes or deletes at most `C_-` old witnesses, and has key-fibre bounds `L_R,L_T`, then:

1. at most `AL_T+C_+L_R` conditioned predicate evaluations are needed;
2. at most `A+C_-` augmenting paths restore witness assignment;
3. otherwise the conditioned Hall deficit is at most `A+C_-`;
4. or one threshold, burden, conditioned-source, repair-class, epoch or occurrence key fails.

Matching maintenance creates no witness mass and does not pay endpoint burden.

## Corrected SRR frontier

Recurrent candidate/witness maintenance is now local in physical record churn and conditioned key fibres. Remaining work is to prove concrete menu-churn and fibre bounds and pay bounded conditioned Hall cores.

## Finite check

`scripts/verify_srr_key_local_witness_epochs.py` checks exact key decomposition, key-local reconstruction, fibre bounds, witness disturbance and matching deficit bounds.