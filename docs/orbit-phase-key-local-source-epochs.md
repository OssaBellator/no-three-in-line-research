# Orbit-phase key-local source epochs

## Status

This note proves OP4gc--OP4gf under the exact typed source and incremental contracts through OP4gb. It does not construct the unit-sensitive key dictionary, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Give every residual/edit incidence and source token a complete coarse key containing residual/edit type, quotient class, unit, valuation band, holonomy class, owner and repair type. Compatibility implies equal keys. Any changed key places the record in the changed set.

## OP4gc -- exact unit-sensitive key decomposition -- PROVED UNDER THE KEY CONTRACT

Cross-key pairs are certified nonedges and the exact source graph is the disjoint union of within-key graphs. A cross-key edge or hidden quotient/unit/holonomy key change is an exact failure.

## OP4gd -- key-local boundary and audit bound -- PROVED

For `R'=R^circ sqcup Delta R`, `T'=T^circ sqcup Delta T`, fresh evaluation is required exactly on

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k).
\]

Thus

\[
\boxed{|\mathcal B^\kappa|=\sum_k(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|).}
\]

With `a=|Delta R|`, `c=|Delta T|`, `L_T=max_k|T'_k|`, `L_R=max_k|R_k^circ|`,

\[
\boxed{|\mathcal B^\kappa|\le aL_T+cL_R.}
\]

The copied unchanged blocks plus this boundary reconstruct the exact dictionary.

## OP4ge -- source disturbance bound -- PROVED

Let `e=|T\setminus T^circ|` count old source tokens changed, deleted or relabelled. Injectivity of the old assignment gives

\[
\boxed{b\le e,
\qquad u=a+b\le a+e.}
\]

No source, residual payment or edit credit is created by carrying the matching.

## OP4gf -- bounded quotient-edit router -- PROVED UNDER THE EDIT CONTRACT

If one quotient-repair step changes at most `A` incidences, introduces at most `C_+` changed/new source records, changes or deletes at most `C_-` old source records, and has key-fibre bounds `L_R,L_T`, then:

1. at most `AL_T+C_+L_R` unit-sensitive predicate evaluations are needed;
2. at most `A+C_-` augmenting paths restore the source assignment;
3. otherwise the typed Hall deficit is at most `A+C_-`;
4. or one quotient, unit, valuation, holonomy, owner, epoch or occurrence key fails.

## Corrected OP5 frontier

OP recurrence maintenance is now local in changed typed records and compatible quotient fibres. Remaining work is to prove concrete fibre and edit bounds and pay the resulting bounded residual/edit Hall cores.

## Finite check

`scripts/verify_op_key_local_source_epochs.py` checks exact key decomposition, within-key boundary reconstruction, fibre bounds, source disturbance and matching deficit bounds.