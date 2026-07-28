# Bounded-denominator telescoping local gain certificates

This note records BDA5do--BDA5ds. It converts the remaining simple-cycle gain check into edge-local rational inequalities.

## Contract

Let `G=(V,E)` be the complete finite physical source graph. Each vertex `v` carries a retained positive rational weight `q_v`. Every edge `e:u->v` has positive rational gain `g_e` and a retained damping factor `delta_e` satisfying

`g_e q_v = delta_e q_u`.

No source occurrence splits, appears without a predecessor or changes its gain data during the argument.

## BDA5do — local telescoping certificate

If `delta_e<=1` on every edge, then

`g_e q_v <= q_u`

edgewise. This is the exact gain-potential inequality required by the preceding source-conservation theorem.

## BDA5dp — simple-cycle nonamplification

For every directed cycle `C`,

`product_{e in C} g_e = product_{e in C} delta_e <= 1`.

The vertex weights telescope around the cycle. Consequently no simple or composite closed source walk amplifies.

## BDA5dq — occurrence-mass monotonicity

If a legal edge transfer satisfies `m_v'<=g_e m_u`, then

`q_v m_v' <= delta_e q_u m_u <= q_u m_u`.

Thus the weighted source account is nonincreasing edge by edge.

## BDA5dr — composition with the source banks

Under the local factorization, BDA5cz--BDA5dn apply without enumerating cycles: initial weighted mass plus exact deposits bounds terminal restoration mass and remaining live mass.

## BDA5ds — exact local failure

An edge with `g_e q_v>q_u`, changed vertex weight, changed gain, omitted source vertex, splitting or source-less creation is returned as an exact local certificate failure. The theorem does not infer an amplifying cycle from one failed edge; the existing potential-or-cycle alternative performs that global routing.

## Finite audit

Run:

`python scripts/verify_bda_telescoping_local_gain.py`

The deterministic audit checks 6,000 finite rational systems, 45,841 gain edges, 37,389 simple directed cycles and 34,792 sampled occurrence transfers.

## Scope

The theorem supplies a local arithmetic target for the concrete BDA source graph: exhibit retained rational vertex weights and damping factors at most one. It does not establish those formulas, prove BDA6 or prove the no-three-in-line conjecture.
