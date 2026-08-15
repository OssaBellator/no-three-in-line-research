# ERL action-family review gate

A proposed first-host family theorem is admissible only if all conditions below hold.

- The family is exactly one of `restore_02`, `delete_02`, `restore_20`, `delete_20`.
- Both context edges listed in `data/exact_recurrent_first_host_action_family_route_leverage.json` are covered.
- Each member edge has a physical occurrence, persistent owner, source and target state, operation kind, registry entry, trace, changed cell, action, legality proof, intermediate states and realization status.
- Each member edge passes one accepted closure route from the closure-route source gate.
- Any claimed shared capacity, potential, output theorem or reset schema is proved uniform across both members.
- The theorem explicitly quantifies over both values of the other restoration bit.
- Shared owner, operation and route schemas preserve all context-dependent child-row and payment data required by the proof.
- No family certificate is inferred from one member edge or from fixture restoration at another side.

The ten-field family contract is split as follows.

Normalized geometry already fixes:

```text
family_id
edge_refs
quantified_context_bit.
```

The source must still populate all seven evidence fields:

```text
shared_theorem_ref
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status.
```

Across all four families, geometry fixes 12 of 40 contract slots. The remaining 28 slots are source evidence and currently all are empty. Structural prefill never counts as physical evidence.

A union of abstract schemas is not sufficient. The cited objects must be joined occurrence-faithfully to the same first-host occurrence, persistent owner and both exact family edges. The source gate pins three external alternating-core theorem blobs and verifies four local execution interfaces by exact theorem markers; this source coverage still provides zero family-specific joins.

The following are not sufficient evidence of family congruence:

```text
same changed cell and action
same selector-change flag
same selected response at one endpoint
same next gap
same complete-score minimizer face label
ambient row/column/axis symmetry
one operation-kind name
one abstract owner theorem plus an unrelated route theorem
an abstract three-source component cover without a first-host join.
```

The exact first-host automorphism group is trivial, every family has distinct ordered selected-response, gap and face-profile pairs, and every family touches the context-sensitive restore-both state `11`.

For scalar closure, the accepted family set must contain one directed family for bit `02` and one directed family for bit `20`.

The four minimum accepted sets are:

```text
restore_02 + restore_20
restore_02 + delete_20
delete_02  + restore_20
delete_02  + delete_20.
```

Every minimum pair has exactly:

```text
theorem-contract slots                    20
structurally prefilled slots               6
remaining source-evidence slots           14.
```

The alternative edge-by-edge route contains four member edges and exposes 48 twelve-field edge-promotion slots. The compressed theorem contract must still imply all physical facts needed by those members.

Both directions of only one bit are insufficient.

Current accepted family certificates: **0**.

Current source-evidence fields populated: **0 of 28**.

This gate does not authorize physical transition legality, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination or `all_n_proved_by_checker=1`.
