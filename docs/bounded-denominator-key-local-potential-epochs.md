# Bounded-denominator key-local potential epochs

## Status

This note proves BDA5hf--BDA5hi under the exact repair-potential and incremental contracts through BDA5he. It does not construct the rational-gain key dictionary, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Give every repair incidence and potential-source token a complete coarse key `kappa` containing its restoration gate, source/gain/damping profile, arithmetic class, owner class and repair type. Assume compatibility implies equal keys. A changed key is a changed record.

Write `R'=R^circ sqcup Delta R`, `T'=T^circ sqcup Delta T`, and use key subscripts.

## BDA5hf -- exact key decomposition -- PROVED UNDER THE KEY CONTRACT

Cross-key pairs are certified nonedges and

\[
E'=\bigsqcup_k E'_k.
\]

Any compatibility edge joining unequal keys, missing key field or hidden key change is returned as the first restoration-address failure.

## BDA5hg -- key-local boundary and fibre bound -- PROVED

Fresh predicate evaluation is required exactly on

\[
\mathcal B_k=(\Delta R_k\times T'_k)\sqcup(R_k^\circ\times\Delta T_k).
\]

Therefore

\[
\boxed{|\mathcal B^\kappa|=\sum_k(|\Delta R_k||T'_k|+|R_k^\circ||\Delta T_k|).}
\]

If `a=|Delta R|`, `c=|Delta T|`, `L_T=max_k|T'_k|` and `L_R=max_k|R_k^circ|`, then

\[
\boxed{|\mathcal B^\kappa|\le aL_T+cL_R.}
\]

The copied unchanged within-key blocks plus this audit reconstruct the exact next dictionary.

## BDA5hh -- token disturbance bound -- PROVED

Let `e=|T\setminus T^circ|` count old potential tokens deleted, changed or relabelled. Since the old assignment is injective, at most `e` unchanged incidences lose their assigned unchanged token. Hence

\[
\boxed{b\le e,
\qquad
u=a+b\le a+e.}
\]

## BDA5hi -- bounded local restoration router -- PROVED UNDER THE EDIT CONTRACT

If one restoration step changes at most `A` incidences, introduces at most `C_+` changed/new next tokens, removes or changes at most `C_-` old tokens, and the key fibres are bounded by `L_R,L_T`, then one exact continuation holds:

1. the exact next dictionary is obtained with at most `AL_T+C_+L_R` new evaluations;
2. at most `A+C_-` augmenting paths restore the potential assignment;
3. otherwise the arithmetic Hall deficit is at most `A+C_-`;
4. or one restoration gate, source/gain/damping key, epoch, occurrence or predicate record fails.

Assignment maintenance creates no gain or potential mass.

## Corrected BDA6 frontier

The remaining restoration cost is controlled by concrete gate churn and compatible source/gain/damping fibre sizes. The next work is to prove those physical bounds and pay the resulting bounded arithmetic Hall cores.

## Finite check

`scripts/verify_bda_key_local_potential_epochs.py` checks exact key decomposition, key-local reconstruction, fibre bounds, token disturbance and matching deficit bounds.