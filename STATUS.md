# Status and honesty ledger

**Last updated:** 28 July 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not**
contain a complete proof. The authoritative theorem ledger reaches CMR2549; CMR2390 onward is in
`proofs/composite-modulus-theorem-index-live-continuation-8.md`.

## Current finite endpoint

The branch contains a finite, noncircular certificate architecture from source-traceable rule clauses
through a global integer quotient and final induction handoff. The exact executable work surfaces now
include:

- one literal statement and sealed proof slot for every cited source;
- exact T01 source-root synchronization;
- exact T02 case, clause, axis, exclusion and global-parent application records;
- exact T03 open/populated/proved slot payloads;
- exact T04 open/populated/proved block and interface assembly;
- exact T05 finite geometry and selector records, using the corrected closure-record endpoint;
- exact T07 fate, state and transition semantic subjects and claims;
- exact T06 candidate scores, complete candidate sets, deterministic winners and T02
  application-to-winner records;
- exact T08 active rows derived from every T06 global-parent application;
- exact T09 literal destroyed-resource universes, overlap graph and canonical scopes;
- exact T10 routed-credit subjects, semantic route assignments and global injectivity tests;
- exact T11 common-weight row bridges, primitive block weights, recurrent support and strict margins;
- exact T12 recursive auxiliary closure, T07 edge support and selected-response stability;
- typed artifact registries for obligations, premises, handoff assertions and all 43 atomic targets;
- an exact 252-chamber exceptional worklist; and
- a synchronized current-frontier gate and seven-gate final dossier audit.

These interfaces expose and seal proof work. They do not supply the missing genuine mathematical data
or verify external proof statements.

## Corrected T05 execution

The original T05 checker reconstructed the correct geometry and selector banks but read the field
`closed` from raw `proof_obligations`. The closure checker publishes that field in
`obligation_closure_records`.

The canonical executable endpoint is:

```text
scripts/check_prime_power_geometry_selector_frontier_v2.py
```

The adapter changes no T05 certificate field or digest. It supplies the correct closure view only to
the T05 module and preserves:

```text
all_n_proved_by_checker = 0
```

## Exact T07 fate, transition and state semantic frontier

CMR2495--CMR2501 give every expected slot one open/proved semantic record.

For each non-open T03 payload, the checker reconstructs:

- one fate subject per literal owner/fate witness;
- one parent-state subject and one state subject per labelled vector; and
- one transition subject per literal transition.

Every subject has exactly one canonical claim containing a statement, evidence and sorted support
claim IDs. The checker reconstructs the complete support graph and canonical topological order and
rejects cycles, unknown support, duplicates and self-support.

A proved slot requires one `slot-fate-transition-state-proof` artifact. Its exact support is the
slot's T03 population artifact plus every T04 assembly artifact whose skeleton parent uses that slot.

The aggregate state and transition banks are bound by the required
`FATE_TRANSITION_STATE_SEMANTICS` artifacts:

```text
state-semantics-proof
transition-proof
```

The combined noncircular digest is bound by the T07 `transition-state-proof` target artifact.
Reconstructed readiness must equal both semantic closure and effective completion of
`T07_FATE_TRANSITION_STATE`.

A sealed semantic claim is not a proof that its statement is true.

## Exact T06 candidate-policy frontier

The fixed atomic proof DAG requires:

```text
T05_GEOMETRY_SELECTORS + T07_FATE_TRANSITION_STATE
    -> T06_CANDIDATE_POLICY
    -> T11_RECURRENT_BLOCK_CLOSURE
```

The older common-weight candidate-policy checker imports recurrent-block common weights and therefore
cannot define T06 without a dependency cycle. It remains a later recurrent-block consistency audit.

Every expected slot has one open/proved candidate-score record. A proved record binds the exact T03
payload and `row_loads` digest, the exact T05 selector summary, the exact T07 semantic certificate, an
externally proved integer `minimum_labelled_row_load`, and one `candidate-score-proof` artifact.

For every local parent, the complete candidate set is reconstructed from all expected slots with that
`parent_state_id`. A proved parent record computes the winner by:

```text
(minimum_labelled_row_load, slot_id)
```

and publishes the minimum, minimizer count, selected slot and every nonnegative score gap. Every T02
global-parent application must use that reconstructed winner.

The aggregate bank is bound by the `CANDIDATE_POLICY_CORRECT` obligation artifact and the T06 target
artifact, both of kind `candidate-policy-proof`.

This verifies candidate-set and minimization identity. It does not verify the external score theorem.

## Exact T08 active-row frontier

CMR2510--CMR2517 derive exactly one active row from every T06 global-parent application. The active-row
list is therefore not supplied independently.

Every row binds the global and local parent IDs, selected slot, exact T06 application record, T03
payload plus row-load/response/credit/transition digests, selected-slot T07 semantic certificate, and
every T04 assembly unit containing that global parent.

A proved row requires one `active-row-member-proof` citing exactly:

- the T06 application artifact;
- every using T04 population artifact; and
- the selected slot's T07 semantic artifact.

The aggregate bank is bound by the `ACTIVE_ROW_FAMILY_EXHAUSTIVE`
`active-family-exhaustiveness-proof` and the T08 `active-family-proof` target artifact. The bank
excludes ancestors containing the T08 completion digest.

This proves exact row identity relative to the supplied recurrence skeleton. It does not prove that
those rows are the genuine complete simultaneous recurrence family.

## Exact T09 destroyed-resource frontier

CMR2518--CMR2525 reconstruct every literal destroyed current triple from the selected slot's T05
linked geometry certificate. Equal triples are identified by sorted point coordinates rather than
local point indices or destroyed IDs.

The checker reconstructs the complete active-row overlap graph and defines resource scopes as its
connected components. Arbitrary supplied scope names no longer determine the partition.

Every proved row requires one `row-destroyed-resource-model-proof` citing its T08 active-row artifact
and T05 geometry artifact. The aggregate `resource-model-proof` binds
`DESTROYED_RESOURCE_MODEL_EXHAUSTIVE` and `T09_RESOURCE_MODEL` through separate obligation and target
locators.

Literal triple reconstruction and canonical scopes do not prove that destroyed triples are the
complete physical shared-resource model.

## Exact T10 routed-credit frontier

CMR2526--CMR2533 give every literal selected-slot `routed_credits` entry one indexed subject. Equal
literal values at different indices remain distinct proof obligations.

A proved row assigns every subject to:

```text
one T09 destroyed resource
one T07 fate claim
one T07 state claim
nonempty T07 transition-claim support
one declared child state
```

No destroyed resource or fate witness may repeat inside one row. Across the complete proved active-row
family, canonical destroyed-resource keys and child-bearing witness-obligation keys are injective.

Each proved row requires one `row-routed-credit-semantics-proof` with exact T08/T09/T07 support. The
aggregate `credit-routing-proof` binds `CREDIT_ROUTING_SEMANTIC` and `T10_CREDIT_ROUTING` through
separate obligation and target locators.

Exact route linkage and injectivity do not prove the route statements, T07 claims or child-state
meanings mathematically true.

## Exact T11 recurrent-block closure frontier

CMR2534--CMR2541 derive every T11 block from the T04 recurrent-block census and every block row from the
exact T08 active-row bank. The older common-weight checker cannot introduce a second row population.

For every active row, the common-weight bridge requires:

- the same local parent and selected T03 fibre;
- the exact selected T05 linked-operation certificate;
- exact equality of the T03 `labelled_vectors` and common exposure table;
- exact equality of the T03 `row_loads` and complete common row arithmetic table;
- equality of the common minimum load and proved T06 score; and
- exact aggregation of unit-level T10 credits to the selected common response's credit vector.

The exact T11 routed-credit unit schema is:

```text
child_state_id
unit_index
selected_response_sha256
```

For each selected response and child, the indices must be exactly `0` through `count - 1`.

Every proved block has one primitive positive common state-weight vector, one common row for every
local SCC parent, the exact recurrent support graph, no external recurrent edge, strong connectivity
and positive margin on every row. The T04 `local_states` and `recurrent_rows` fields must equal the
common state registry and exact T08 row IDs.

A proved block requires separate `recurrent-block-common-weight-proof` and
`recurrent-block-closure-proof` artifacts. Separate noncircular aggregate banks bind the required
`common-weight-proof` and `block-closure-proof` obligation artifacts; the T11 target binds their
combined digest.

Recurrent-core closure does not erase nonrecurrent exits. Auxiliary and interface exits remain visible
T12 and T15 work, and the checker does not prove their semantic validity.

## Exact T12 auxiliary-semantics frontier

CMR2542--CMR2549 give every exact T11 block one open/proved T12 record. The canonical endpoint is:

```text
scripts/check_prime_power_auxiliary_semantics_frontier_v2.py
```

The version-2 adapter preserves the base T12 record and arithmetic schemas while correcting the fixed
proof flow to:

```text
T07_FATE_TRANSITION_STATE + T11_RECURRENT_BLOCK_CLOSURE
    -> T12_AUXILIARY_SEMANTICS
```

The `AUXILIARY_EXPANSIONS_SEMANTIC` obligation has the corresponding T07 and T11 immediate dependency
bundles.

Every proved block must reuse the exact T11 common-weight certificate. The auxiliary expansion table
must cover exactly the recursive closure of all positively used auxiliary states. The checker rejects
cycles, verifies local and effective common-weight domination, forbids routed credit to eliminated
auxiliaries, and reconstructs every fully substituted response row.

Every expansion source, fixed-load term and target edge has explicit support from the selected slots'
exact T07 state and transition claim banks. Every target edge requires nonempty state and transition
support.

Complete elimination must preserve the exact T11 selected response and satisfy:

```text
eliminated selected load <= T11 minimum load
eliminated selected margin >= T11 strict margin
```

Every proved block requires one `recurrent-block-auxiliary-elimination-proof` citing its T11
common-weight artifact, T11 closure artifact and every selected-slot T07 semantic artifact. The
aggregate `auxiliary-expansion-proof` obligation artifact cites the two T07 and two T11 immediate
obligation artifacts; the T12 `auxiliary-semantics-proof` target binds the same noncircular proof bank.

Exact acyclic weighted substitution and claim support do not prove expansion statements,
multiplicities or target-state meanings mathematically true.

## Remaining semantic fronts

The next exact fronts are:

- T13: cross-block state-equivalence truth;
- T14: cross-block component scales;
- T15--T18: interface exhaustiveness, global rank, state predicates and final row theorems;
- T19--T21: global-family exhaustiveness and all 252 exceptional chambers; and
- T22--T43: final premises, handoff assertions, dossier audit and reviewed root implication.

## Genuine current frontier

1. Transcribe and prove every genuine source statement with sealed noncircular support.
2. Populate and prove every T02 rule record and review genuine recurrence exhaustiveness.
3. Enter actual T03 slot payloads and prove complete candidate population.
4. Enter actual T04 block/interface assembly and prove complete population identity.
5. Populate every T05 finite geometry record and prove the finite bank covers the genuine recurrence.
6. Populate every T07 semantic claim and prove all owner, fate, state and transition statements.
7. Supply genuine T06 score proofs, close every parent policy and verify every T02 application uses
   the winner.
8. Populate and prove every T08 active row, T09 resource model and T10 routed-credit semantic record.
9. Populate every T11 common-weight bridge and prove every recurrent core closed, strongly connected
   and strict.
10. Populate and prove every T12 expansion semantic record and selected-response stability record.
11. Prove cross-block state identity, component scales, interfaces, rank, predicates and row theorems.
12. Prove all 232 zero-selector and 20 hard-core chamber dispositions.
13. Complete every genuine obligation, premise, handoff and atomic-target artifact.
14. Review the ordinary proof that the quotient and handoff imply `D(n)=2n` for every `n`.

## Corrections retained

- A source locator and unattached digest do not identify literal mathematical text.
- Exact source text and a matching hash do not prove the source statement true.
- Repeating an external proof pointer is not statement-to-proof binding.
- Exact global-parent-to-slot identity does not prove recurrence exhaustiveness.
- Literal T03 and T04 data do not prove their intended semantics.
- Exact finite T05 arithmetic does not prove coverage for arbitrary `n`.
- T05 closure must be read from `obligation_closure_records`.
- Acyclic T07 claim support does not prove semantic truth or logical sufficiency.
- A T06 integer score remains an external theorem requiring ordinary mathematical review.
- Deterministic minimization does not prove that the score is the intended recurrence objective.
- The old common-weight candidate checker cannot define T06 without reversing the proof DAG.
- A T06-application-derived T08 census remains relative to the supplied recurrence skeleton.
- Coordinate-canonical T09 scopes do not prove physical resource-model exhaustiveness.
- T10 route linkage and injectivity do not prove route statements or child-state semantics.
- A standalone common-weight certificate does not identify the exact T08/T10 row population.
- Exact T11 bridges and strict margins remain relative to supplied T07/T10 semantics.
- Recurrent-core closure does not prove auxiliary or interface exits semantically valid.
- The original T12 aggregate support check predates the corrected T07+T11 dependency root.
- Exact T12 edge support and weighted domination do not prove expansion truth or target-state meaning.
- Selected-response stability does not prove the selected recurrence is the genuine all-`n` policy.
- State links and predicate records do not prove external state identity.
- Strict-or-ranked rows do not prove interface exhaustiveness.
- A closed chamber disposition does not verify its proof.
- Typed artifacts and synchronization gates are documentary metadata.
- Every final checker reports `all_n_proved_by_checker = 0`.
- Syntax compilation and isolated helper tests are not a dependency-backed certificate suite.

## Bottom line

There is no complete proof. Through **CMR2549**, the finite certificate surface reaches exact work
banks from T01 through T12, including corrected executable T05 and T12 paths, literal T07 semantic
coverage, noncircular T06 policy, application-derived T08 rows, literal T09 resources, exact T10 routed
credits, T11 strict recurrent cores and T12 acyclic auxiliary substitution tied to exact T07/T11 data.

Completion still requires genuine source and recurrence theorems, actual T03/T04 data, proof of T05
all-`n` geometric coverage, truth of every T07 claim and T06 score, genuine T08 simultaneous-row
completeness, T09 physical resource exhaustiveness, T10 route semantics, genuine T11 and T12 semantics,
all cross-block, interface, rank and chamber semantics, and ordinary review of the final implication to
all `n`.
