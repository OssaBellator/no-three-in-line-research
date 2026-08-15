# First-host action-family source import gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact import audit for context-parametric action-family theorems. It does not prove any first-host transition or family physically realizable.

## Structural reduction

The family congruence contract has ten fields. Exact restoration geometry determines three:

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

The remaining seven fields are physical source evidence:

```text
shared_theorem_ref
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status.
```

Exact total census:

```text
action families                           4
contract fields per family               10
total contract slots                     40
geometry-prefilled slots                 12
source-evidence slots                    28
populated source-evidence slots           0
fully imported families                   0.
```

The three structural fields are normalized identifiers. They do not count as transition legality, owner identity, operation compatibility, payment compatibility or realization evidence.

## Audited abstract interfaces

Seven source interfaces are pinned by immutable blob ID.

Three external alternating-core blobs provide abstract contracts:

```text
Boolean boundary gates
occurrence-lineage gates
physical-signature lineage quotient.
```

Four current-branch documents are additionally checked for exact theorem markers:

```text
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

The capability census is:

```text
context-quantification interfaces   1
owner-continuation interfaces       3
operation-schema interfaces         2
closure-route interfaces            3
child/payment-schema interfaces     2.
```

No single source covers all five components. The minimum abstract cover uses three sources, with exactly two minimum covers:

```text
Boolean boundary + inherited-coordinate + installed registry
Boolean boundary + inherited-coordinate + protected-interface execution.
```

These are schema covers only. Neither cover supplies one occurrence-faithful theorem joining its components to the same first-host owner and the same two exact family edges.

## Missing occurrence-faithful join

For every family, candidate abstract roles exist for owner, operation, route and child/payment schemas. Current sources provide none of:

```text
first-host shared theorem reference
proof covering both values of the other restoration bit
selected first-host owner schema
selected first-host operation schema
selected accepted route schema
first-host child/payment compatibility
physical realization status.
```

Accordingly:

```text
first-host family theorems found           0
occurrence-faithful family joins           0
source-backed uniform family imports       0.
```

An operation-kind name does not prove family uniformity. A union of compatible-looking abstract theorems also does not prove that their objects refer to the same occurrence or lineage.

## Minimum scalar-closure import burden

Family-level scalar closure requires one directed family for bit `02` and one for bit `20`. The exact minimum pairs are

```text
delete_02  + delete_20
delete_02  + restore_20
restore_02 + delete_20
restore_02 + restore_20.
```

Each pair has:

```text
theorem-contract slots                    20
structurally prefilled slots               6
remaining source-evidence slots           14.
```

The transition-domain contract requires twelve fields per separately ingested edge. The two-family shortcut contains four member edges, so the alternative edge-by-edge surface is

```text
4 edges x 12 fields = 48 field slots.
```

The twenty-slot family theorem is a contract compression, but not an evidentiary waiver. Its fourteen evidence slots must imply the occurrence, owner, operation, route, child and payment facts required for both members of each imported family.

## Import acceptance rule

One family import is accepted only when all seven evidence fields are populated and the cited theorem:

1. refers to both exact edge members;
2. proves both values of the other restoration bit;
3. preserves one occurrence-faithful owner lineage;
4. supplies a shared or explicitly context-parametric operation schema;
5. supplies one accepted closure route in both contexts;
6. proves child-row and payment compatibility;
7. records physical realization.

Two accepted imports on different restoration bits are still required for the family scalar shortcut.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_action_family_source_import_gate.py \
  --check data/exact_recurrent_first_host_action_family_source_import_gate.json
```

The checker joins the congruence, transition-domain and family-leverage manifests; verifies four local source documents by theorem markers; pins three external alternating-core theorem blobs; computes the exact five-component coverage and both minimum abstract source covers; reconstructs all four minimum scalar import pairs; and rejects eighteen deliberate corruptions.

Physical occurrence coverage, transition legality, owner identity, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination and `all_n_proved_by_checker` remain zero.
