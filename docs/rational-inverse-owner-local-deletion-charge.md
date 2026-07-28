# Rational-inverse owner-local deletion charge

This note records RI5cv--RI5cz. It localizes compatibility-perturbation loss to exact owners.

## Contract

Fix a reference owner/collateral graph `G_0` and an actual graph `G_1` on the same owner demands `d_u` and collateral capacities `c_s`. Added arcs are free monotone improvements. For each owner `u`, retain the deleted-capacity charge

`q_u = sum { c_s : (u,s) is an arc of G_0 deleted from G_1 }`.

Repeated collateral capacities are counted in each owner-local charge; this deliberate overcount keeps the bound local.

## Theorem block RI5cv--RI5cz

For every owner subset `X`,

`delta_1(X) - delta_0(X) <= sum_{u in X} q_u`,

where `delta_k(X)=d(X)-c(N_k(X))`.

Therefore:

1. the actual maximum Hall deficit is at most the reference maximum deficit plus `sum_u q_u`;
2. if every owner has `q_u <= lambda`, then every subset loses at most `lambda |X|`;
3. if the actual maximum deficit exceeds the reference maximum by `r>0`, the canonical actual deficient subset `X` contains an owner with
   `q_u >= r/|X|`;
4. adding compatibility arcs cannot worsen any deficit.

The proof charges each source that leaves `N_0(X)` to any deleted incident arc from an owner in `X`.

## Consequence

A global RI compatibility failure now returns one owner with a quantified local deleted-capacity charge. The remaining arithmetic target is to bound that charge for the concrete secant/context compatibility graph.

## Finite audit

Run:

`python scripts/verify_ri_owner_local_deletion_charge.py`

The audit checks every owner subset in random reference/actual systems and verifies the local witness extracted from every worsened maximum deficit.

## Scope

The result assumes fixed retained owner, source and capacity fields. It does not prove the arithmetic reference graph, its local deletion bounds, RI6 or the no-three-in-line conjecture.
