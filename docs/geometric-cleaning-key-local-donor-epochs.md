# Geometric-cleaning key-local donor epochs

## Status

This note proves GC2md--GC2mg under the exact donor/remedy/height and incremental contracts through GC2mc. It does not construct the geometric key dictionary, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Assign complete coarse keys to remedy incidences and donor tokens using donor class, remedy type, protected-height band, geometric chart, certificate class and occurrence type. Compatibility implies equal keys; a changed key is a changed record.

## GC2md -- exact geometric key decomposition -- PROVED UNDER THE KEY CONTRACT

Cross-key pairs are certified nonedges, so the exact compatibility graph is the disjoint union of within-key graphs. A cross-key edge or hidden chart/height-key change is a first dictionary failure.

## GC2me -- key-local boundary formula -- PROVED

For `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`, fresh evaluation is needed exactly on

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k).
\]

Hence

\[
\boxed{|\mathcal B^\kappa|=\sum_k(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|).}
\]

The copied unchanged within-key blocks and this audit reconstruct the exact next dictionary.

## GC2mf -- fibre and donor-disturbance bounds -- PROVED

Let `a=|Delta R|`, `c=|Delta T|`, `L_T=max_k|T'_k|`, and `L_R=max_k|R_k^circ|`. Then

\[
\boxed{|\mathcal B^\kappa|\le aL_T+cL_R.}
\]

If `e=|T\setminus T^circ|` counts deleted, changed or relabelled old donor tokens, injectivity of the old assignment gives

\[
\boxed{b\le e,
\qquad u=a+b\le a+e.}
\]

## GC2mg -- bounded cleaning-edit router -- PROVED UNDER THE EDIT CONTRACT

If one cleaning operation changes at most `A` remedy incidences, introduces at most `C_+` changed/new donor records, removes or changes at most `C_-` old donor records, and has key-fibre bounds `L_R,L_T`, then:

1. at most `AL_T+C_+L_R` new geometric predicate evaluations are needed;
2. at most `A+C_-` augmenting paths restore donor assignment;
3. otherwise the geometric Hall deficit is at most `A+C_-`;
4. or one donor, remedy, height, chart, certificate, epoch or occurrence key fails.

Matching maintenance creates no donor mass and does not alter height accounting.

## Corrected GC5 frontier

The cleaning audit is now local in changed records and compatible geometric fibres. Remaining work is to prove actual chart/height fibre bounds and pay bounded donor/remedy Hall cores.

## Finite check

`scripts/verify_gc_key_local_donor_epochs.py` checks exact keyed reconstruction, fibre bounds, donor disturbance and matching deficit bounds.