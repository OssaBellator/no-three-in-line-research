# Sparse joint cancellation-completion transport

This note records SAS5jv--SAS5jz. It prevents legal sign-pair execution and zero-boundary completion from independently spending the same neutral move capacity.

## Contract

Fix a canonical legal sign matching. Its matched pair classes have exact execution costs. The resulting zero-boundary residual task classes have exact completion demands. Both demand families use one finite set of boundary-neutral move classes with shared integral capacities and one complete compatibility graph.

## Theorem block SAS5jv--SAS5jz

### SAS5jv — combined demand graph

Matched-pair execution costs and residual completion tasks form one combined demand side over the shared neutral-move source side.

### SAS5jw — simultaneous Hall criterion

All pair costs and completion tasks are paid iff every combined demand subset satisfies the capacitated Hall inequality.

### SAS5jx — no double spending

An integral combined flow debits every neutral-move unit at most once. Separate feasibility of the pair and task subgraphs is insufficient.

### SAS5jy — canonical mixed cut

Failure returns the canonical maximum-deficit subset, retaining whether each demand is a pair execution or a completion task and its exact neutral-move neighbourhood.

### SAS5jz — reset boundary

Changed sign matching, boundary profile, task dictionary, move classification, compatibility or capacity returns reset.

## Proof

This is integral bipartite transportation on the union of the two demand families. Max-flow/min-cut gives the criterion and mixed failure cut.

## Finite audit

Run `python scripts/verify_sas_joint_cancellation_completion_transport.py`.

## Scope

The theorem does not prove the physical pair graph or construct the boundary-neutral move graph and capacities. It does not prove SAS6 or the no-three-in-line conjecture.
