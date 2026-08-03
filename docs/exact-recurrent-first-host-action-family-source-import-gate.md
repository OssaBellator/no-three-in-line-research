# First-host action-family source import gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact import audit for context-parametric action-family theorems. It does not prove any first-host transition or family physically realizable.

## Structural reduction

The preceding congruence audit requires ten fields for one uniform family theorem. Three are already fixed exactly by the normalized restoration geometry:

```text
family_id
edge_refs
quantified_context_bit.
```

For the four families:

```text
restore_02  edges 00->10,01->11  quantify r20
delete_02   edges 10->00,11->01  quantify r20
restore_20  edges 00->01,10->11  quantify r02
delete_20   edges 01->00,11->10  quantify r02.
```

This leaves exactly seven source-evidence fields per family:

```text
shared_theorem_ref
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status.
```

The three structural fields are normalized identifiers, not physical evidence.

## Audited abstract interfaces

Seven source interfaces were pinned by immutable blob ID:

```text
Boolean boundary gates
occurrence-lineage gates
physical-signature lineage quotient
installed 1,166-kind operation registry
inherited-coordinate diagonal blocks
owner/fate lineage kernel
protected-interface execution.
```

They collectively expose five abstract component types:

```text
context quantification
owner continuation
operation schema
closure-route schema
child/payment schema.
```

The exact capability census is:

```text
context-quantification interfaces   1
owner-continuation interfaces       3
operation-schema interfaces         2
closure-route interfaces            3
child/payment-schema interfaces     2.
```

No single source covers all five components. The minimum abstract cover uses three sources, and there are exactly two minimum covers:

```text
Boolean boundary + inherited-coordinate + installed registry
Boolean boundary + inherited-coordinate + protected-interface execution.
```

These are abstract schema covers only. The protected-interface source is a side-five fixture, while the installed registry is an operation-kind bank rather than an occurrence-level legality table.

## Missing join

The union of abstract contracts does not prove that their owner, operation, route and child/payment objects refer to the same first-host occurrence, the same persistent token or the same two exact family edges.

Current census:

```text
action families                           4
uniformity fields per family             10
structural fields fixed per family        3
source-evidence fields required            7
structural fields fixed in total          12
source-evidence fields populated           0
first-host family theorems found           0
source-backed uniform family imports       0.
```

For every family, candidate schema roles exist for owner, operation, route and child/payment. No role has been selected by a source-backed first-host theorem, and no theorem proves both values of the other context bit.

Therefore neither an operation-kind name nor a union of compatible-looking abstract theorems proves family uniformity.

## Import acceptance rule

One family import is accepted only when all seven evidence fields are populated and the cited theorem:

1. refers to the two exact normalized edge members;
2. proves both values of the other restoration bit;
3. preserves one occurrence-faithful owner lineage;
4. supplies a shared or explicitly context-parametric operation schema;
5. supplies one accepted closure route in both contexts;
6. proves the required child-row and payment compatibility;
7. records physical realization.

Two accepted imports, one for bit `02` and one for bit `20`, are still required for the family-level scalar shortcut.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_action_family_source_import_gate.py \
  --check data/exact_recurrent_first_host_action_family_source_import_gate.json
```

The checker reconstructs all four normalized family templates, audits seven immutable source interfaces, computes the exact five-component coverage and both minimum abstract source covers, and rejects fifteen deliberate corruptions.

Physical occurrence coverage, transition legality, owner identity, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination and `all_n_proved_by_checker` remain zero.
