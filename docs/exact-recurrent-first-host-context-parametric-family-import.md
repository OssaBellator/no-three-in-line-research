# First-host context-parametric family import gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact source-import audit for the four two-edge restoration action families. It does not import any physical family theorem and does not prove recurrent closure.

## Geometry-determined contract fields

The action-family congruence audit requires ten fields for a context-parametric theorem. Three are already determined by exact first-host geometry:

```text
family_id
edge_refs
quantified_context_bit.
```

For example,

```text
restore_02
  edge_refs = 00->10, 01->11
  quantified_context_bit = r20

restore_20
  edge_refs = 00->01, 10->11
  quantified_context_bit = r02.
```

The same rule fixes the two delete families. Therefore the four family records contain

```text
total contract slots                 40
geometry-prefilled slots             12
source-evidence slots                28.
```

This is a schema reduction only. Knowing the family name, its member edges and the other context bit is not a physical legality, owner, operation or payment proof.

## Seven remaining evidence fields

Every family still requires

```text
shared_theorem_ref
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status.
```

All seven must refer to one occurrence-faithful result proving the same closure conclusion for both values of the other restoration bit. A theorem may retain context-dependent selector, minimizer-face, operation, child-row or payment data; it need not pretend the two contexts have identical geometry.

Current census:

```text
families                                   4
source-evidence fields per family          7
source-evidence slots                     28
populated source-evidence slots            0
fully imported families                    0.
```

## Alternating-core schema audit

Seven source layers were audited.

Three immutable blobs on `research/alternating-core-chain` supply abstract contracts:

```text
occurrence-lineage continuation and closure routes
physical-signature identity/payment quotient
finite Boolean boundary gates.
```

Four marker-audited documents on the current branch supply installed execution schemas:

```text
1,166-kind operation registry
protected-interface execution ancestry
inherited-coordinate owner and exact-row ancestry
owner/fate child-payment ancestry.
```

Together they provide candidate schemas for owner identity, operation kinds, generic closure routes and child/payment compatibility. They do not provide:

```text
a first-host shared theorem reference
proof of both restoration contexts
an occurrence-faithful join selecting owner, operation and route schemas
first-host child/payment compatibility
physical realization status.
```

In particular:

- a registered operation kind is not a mapping to both family edges;
- a generic continuation relation is not a first-host persistent-owner witness;
- a generic Boolean boundary theorem is not proof that this physical token follows both context edges;
- conditional exact-row and payment schemas are not populated recurrent rows.

No context-parametric first-host family theorem was found in the audited sources.

## Minimum scalar-closure import burden

A scalar cover requires one directed family for bit `02` and one directed family for bit `20`. The four possible minimum pairs are

```text
delete_02  + delete_20
delete_02  + restore_20
restore_02 + delete_20
restore_02 + restore_20.
```

Each pair has

```text
structurally prefilled slots              6
remaining source-evidence slots          14.
```

For comparison, ingesting all four member edges separately would expose

```text
4 edges x 12 edge-promotion fields = 48 field slots.
```

The fourteen-slot theorem interface is therefore a genuine contract compression. It is not an evidentiary waiver: the shared theorem must imply the occurrence, owner, operation, route and child/payment facts needed for both member edges.

## Exact current boundary

```text
abstract schema layers audited                         7
context-parametric first-host family theorems          0
occurrence-faithful family joins                       0
imported action families                               0
complete scalar closure pairs                          0
promotion to recurrent closure                         0.
```

The next admissible source result is one complete seven-field theorem record for a named family. Scalar closure requires two such imported families on different restoration bits, unless the physical transition domain is reduced by separately sourced impossibility results.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_context_parametric_family_import.py \
  --check data/exact_recurrent_first_host_context_parametric_family_import.json
```

The checker joins the exact family-leverage and congruence manifests, verifies four local source documents by theorem markers, pins three external alternating-core theorem blobs, reconstructs all four contract records and rejects sixteen deliberate corruptions.

Physical occurrence coverage, transition legality, persistent owner identity, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination and `all_n_proved_by_checker` remain zero.
