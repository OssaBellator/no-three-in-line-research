# Prime-power transition, resource and routed-credit frontier

This chapter records CMR2510--CMR2533. It makes the three consecutive atomic targets

```text
T08_ACTIVE_ROW_FAMILY
T09_RESOURCE_MODEL
T10_CREDIT_ROUTING
```

and their semantic obligations exact documentary proof surfaces.

The checker is:

```text
scripts/check_prime_power_transition_resource_frontier.py
```

It composes the exact T06 candidate-policy bank, T05 finite geometry, T07 fate/state/transition
semantics, T04 block/interface assembly and T03 literal slot payloads. The three aggregate proof
banks are sealed separately so that no downstream target is included in an upstream proof digest.

## T08 active-row family

### CMR2510: application-derived active-row census

Every exact T06 global-parent application produces exactly one active-row record. The canonical row
ID is

```text
active::<parent global state ID>
```

The checker therefore does not accept a freely supplied list of simultaneously active rows. Missing,
extra, duplicated or reordered rows are rejected against the complete T06 application bank.

### CMR2511: exact selected-row identity

Every active-row record binds:

```text
parent_global_state_id
local_parent_state_id
selected_slot_id
candidate_policy_application_record_sha256
slot_population_payload_sha256
row_loads_sha256
response_family_sha256
routed_credits_sha256
transitions_sha256
slot_semantic_certificate_sha256
using_t04_unit_ids
```

The selected slot is the T06 policy winner actually used by the corresponding T02 application. The
literal row-load, response, routed-credit and transition digests are reconstructed from the selected
T03 payload. The T04 unit list is reconstructed from every skeleton-derived block or interface unit
containing that global parent.

### CMR2512: exact active-row artifact support

A proved row requires one artifact of kind:

```text
active-row-member-proof
```

Its exact support is:

1. the T06 application artifact for the global parent;
2. every proved T04 block/interface population artifact containing that parent; and
3. the selected slot's T07 semantic artifact.

The support lists are sorted, duplicate-free and exact. A row cannot close while the selected policy,
using assembly unit or semantic slot remains unproved.

### CMR2513: row-to-bundle sealing

The active-row status record uses

```text
active-row-family-registry://active::<parent global state ID>
```

and its verification digest equals the reconstructed row proof-bundle digest. The bundle commits to
the active-row record, active-row artifact and all three support lists.

### CMR2514: noncircular active-family bank

The aggregate T08 bank binds the noncircular T06 policy bank, exact T06 application records and
artifacts, exact T04 unit/artifact bank, exact T07 semantic bank, and all active-row records,
artifacts and bundles.

It deliberately excludes the obligation registry, current-frontier certificate, atomic completion
records and target-artifact registry. Those ancestors may already contain the T08 completion digest.

### CMR2515: active-family obligation synchronization

When `ACTIVE_ROW_FAMILY_EXHAUSTIVE` closes, its unique required artifact must have kind

```text
active-family-exhaustiveness-proof
```

locator

```text
active-row-family-frontier://ACTIVE_ROW_FAMILY_EXHAUSTIVE
```

and digest equal to the reconstructed active-family bank. Its support is exactly the
`CANDIDATE_POLICY_CORRECT` obligation-artifact bundle.

### CMR2516: T08 atomic-target sealing

The T08 target artifact must have kind

```text
active-family-proof
```

locator

```text
active-row-family-frontier://T08_ACTIVE_ROW_FAMILY
```

and proof digest equal to the same noncircular active-family bank. Reconstructed T08 readiness must
agree with both semantic closure and effective atomic-target completion.

### CMR2517: active-family honesty boundary

The checker proves exact documentary identity between the supplied skeleton, candidate policy and
active-row proof records. It does not prove that the supplied global-parent applications are the
genuine simultaneous obligations of the all-`n` recurrence.

## T09 destroyed-resource model

### CMR2518: literal destroyed-resource reconstruction

For each active row, the checker reads the selected slot's exact T05 linked-operation geometry
certificate and reconstructs every literal destroyed current triple. It does not derive resources
from the subset later used by routed credits.

### CMR2519: coordinate-canonical resource identity

Every literal destroyed triple receives one resource key obtained from its sorted point coordinates:

```text
resource-<first 24 hexadecimal characters of SHA256(sorted point triple)>
```

Thus equal physical triples agree across different local point-index systems, destroyed IDs and
active rows.

### CMR2520: exact row-overlap graph

The resource-overlap graph has one vertex per T08 active row and an edge exactly when the two complete
literal destroyed-resource universes intersect. The edge bank is reconstructed before any scope
record is published.

### CMR2521: canonical overlap scopes

Resource scopes are exactly the connected components of the overlap graph. Every component receives
a canonical ID determined by its complete row-ID and resource-key sets. Distinct components are
resource-disjoint by construction.

The older `check_prime_power_resource_overlap_scope_partition.py` remains a useful lower-level audit,
but T09 no longer accepts its active-row census as an independent input.

### CMR2522: exact row resource-model artifacts

Each active row has one open/proved resource-model record. A proved row requires one artifact of kind

```text
row-destroyed-resource-model-proof
```

citing exactly the row's T08 active-row artifact and selected slot's T05 geometry artifact. Its
verification digest seals the row record, complete literal resource universe, artifact and support.

### CMR2523: noncircular destroyed-resource bank

The aggregate T09 bank binds the T08 active-family bank, T05 geometry bank, every row resource-model
record, every literal resource record, the exact overlap graph, derived scopes, artifacts and
per-row bundles. It excludes all ancestors that can contain the T09 completion digest.

### CMR2524: T09 obligation and target synchronization

The `DESTROYED_RESOURCE_MODEL_EXHAUSTIVE` artifact must have kind `resource-model-proof`, locator

```text
destroyed-resource-model-frontier://DESTROYED_RESOURCE_MODEL_EXHAUSTIVE
```

and support exactly the `ACTIVE_ROW_FAMILY_EXHAUSTIVE` and `GEOMETRY_SELECTOR_CORRECT` obligation
artifact bundles.

The T09 atomic target artifact also has kind `resource-model-proof`, locator

```text
destroyed-resource-model-frontier://T09_RESOURCE_MODEL
```

and the same noncircular proof-bank digest. Both readiness flags must agree exactly.

### CMR2525: destroyed-resource honesty boundary

Literal coordinate triples, an overlap graph and canonical scopes do not prove that destroyed triples
are the complete physical shared-resource model. That completeness statement remains an ordinary
mathematical theorem represented by the row and aggregate proof artifacts.

## T10 routed-credit semantics

### CMR2526: exact literal routed-credit subjects

Every literal entry in the selected T03 payload's `routed_credits` list becomes one exact subject with
its active-row ID, selected slot, occurrence index and literal JSON value. Equal values at different
indices remain distinct subjects.

Every active row receives one open/proved routed-credit semantic record, including rows whose literal
credit list is empty.

### CMR2527: exact route-to-semantics linkage

A proved row contains exactly one route assignment per literal credit subject. Every assignment binds:

```text
credit_subject_sha256
destroyed_resource_key
fate_claim_id
state_claim_id
transition_claim_ids
child_state_id
route_statement
evidence
```

The destroyed resource must belong to that row's complete T09 universe. Fate, state and transition
claim IDs must belong to the selected slot's exact T07 semantic certificate. Transition support is
nonempty, sorted and duplicate-free.

### CMR2528: row-local injectivity

Inside one active row, no destroyed resource may be reused by two routed-credit subjects and no T07
fate witness claim may be reused. This is checked after exact subject-to-assignment coverage.

### CMR2529: global simultaneous injectivity

Across every proved active row:

1. canonical destroyed-resource keys are globally injective over assignments; and
2. the tuple `(fate claim, state claim, child state)` is globally injective.

This separates alternative-response reuse from simultaneous-row reuse and removes freely named
resource scopes from the final injectivity test.

### CMR2530: exact routed-credit row artifacts

A proved routed-credit row requires one artifact of kind

```text
row-routed-credit-semantics-proof
```

with exact support from:

1. its T08 active-row artifact;
2. its T09 resource-model artifact; and
3. its T07 semantic artifact.

The row verification digest seals the full subject bank, route assignments, artifact and support.

### CMR2531: noncircular routed-credit bank

The aggregate T10 bank binds the T09 destroyed-resource bank, separate T07 state and transition
banks, all routed-credit records, all assignments, all artifacts and bundles, and the global resource
and obligation key banks.

It excludes the obligation and atomic-target registries so that the T10 target artifact does not hash
itself indirectly.

### CMR2532: T10 obligation and target synchronization

The `CREDIT_ROUTING_SEMANTIC` obligation artifact must have kind `credit-routing-proof`, locator

```text
routed-credit-semantics-frontier://CREDIT_ROUTING_SEMANTIC
```

and support exactly the `DESTROYED_RESOURCE_MODEL_EXHAUSTIVE` and
`FATE_TRANSITION_STATE_SEMANTICS` obligation artifact bundles.

The T10 target artifact has kind `credit-routing-proof`, locator

```text
routed-credit-semantics-frontier://T10_CREDIT_ROUTING
```

and the same reconstructed proof-bank digest. Semantic closure and effective target completion must
agree with exact T10 readiness.

### CMR2533: honesty boundary and executable endpoint

Passing the checker establishes exact T08 row coverage, exact T09 literal resource geometry, exact
T10 credit-subject coverage, route linkage, injectivity, typed support and digest synchronization. It
does not prove that:

- the T02 recurrence or T06 score theorem is genuine;
- the T08 rows are the true complete simultaneous recurrence family;
- destroyed triples are the only physical shared resources;
- any route statement or T07 semantic claim is mathematically true;
- the selected child state has the intended external meaning;
- any recurrent block is closed, strongly connected or strict; or
- the quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_transition_resource_frontier.py certificate.json
```

The next exact fronts are T11 recurrent-block closure, T12 auxiliary semantics and the T13--T18
cross-block/interface/rank theorem banks.
