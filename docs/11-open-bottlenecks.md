# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through CMR2493 the branch has a finite certificate
architecture from source-traceable rule clauses to a global integer quotient, semantic predicates
and row theorems, typed obligation/premise/handoff artifacts, a seven-gate pre-root integrity audit,
an exact 252-chamber worklist, a 43-target execution schedule, synchronized chamber/target gates,
sealed atomic-target evidence, and exact work banks for T01 through T05.

The branch still lacks the literal genuine source statements, the genuine exhaustive recurrence,
complete real T03 and T04 population, proof that the finite T05 bank covers the genuine recurrence,
candidate-policy and fate/transition/resource semantics, strict recurrent blocks, complete interface
semantics, mathematically closed chamber proofs and the reviewed implication to `D(n)=2n`.

## 2. Close the exact source-statement bank

CMR2438--CMR2461 make `T01_SOURCE_STATEMENTS` executable. For every source in the rule-provenance
certificate:

1. transcribe the exact mathematical statement;
2. recompute its SHA-256 from the exact UTF-8 text;
3. retain the exact source ID, kind and locator;
4. mark the statement `open` or `proved`; and
5. for a proved statement, supply the fixed source-kind-specific verification artifact.

| Source kind | Required artifact |
|---|---|
| `definition` | `definition-conformance-proof` |
| `case-split` | `case-split-exhaustiveness-proof` |
| `lemma` | `lemma-proof` |
| `domain` | `domain-characterization-proof` |
| `exclusion` | `exclusion-proof` |
| `computation` | `reproducible-computation-proof` |

For source ID `S`, a proved record binds

```text
source-verification-artifact-registry://S
```

and the reconstructed artifact-bundle digest. The artifact carries a separate external proof
pointer, the exact statement hash, a proof statement, evidence and a sorted list of supporting
source-verification artifact IDs. The complete support graph must be acyclic.

The source registry reconstructs every case/clause/axis/exclusion use and orders open sources by
decreasing downstream use. Use that order to choose high-leverage proof work, not as an estimate of
difficulty.

The complete source bank must be bound by the unique `source-truth-proof` artifact for
`SOURCE_STATEMENTS_TRUE`. The source-root gate requires exact agreement with
`T01_SOURCE_STATEMENTS`.

## 3. Close the exact T02 rule-exhaustiveness bank

CMR2462--CMR2469 make `T02_RULE_EXHAUSTIVENESS` an exact proof-work interface. Populate one
open/proved record for every:

- parent case;
- rule clause;
- finite parameter axis;
- excluded parameter row; and
- global recurrence-skeleton parent.

Internal support is fixed by

```text
axis/exclusion -> clause -> case -> global-parent application.
```

For every global parent provide:

```text
source_case_id
source_clause_id
operation_slot_id
```

The selected slot must be generated from an admitted parameter row and must match the skeleton case,
case/clause incidence, local parent state, expected host, ordered labels and operation kind.

The existing `RULE_EXHAUSTIVE` artifacts bind:

```text
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-manifest
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-exhaustiveness-proof
```

Reconstructed readiness must agree exactly with `RULE_EXHAUSTIVE` and
`T02_RULE_EXHAUSTIVENESS`. The actual parent rule is still absent, so exact slot identity remains a
review surface rather than proof of genuine exhaustiveness.

## 4. Close the exact T03 slot/candidate bank

CMR2470--CMR2477 give every expected operation slot one status:

- `open`: no payload or proof artifact;
- `populated`: one literal payload, but no T02-backed proof artifact;
- `proved`: one literal payload and one sealed slot-specific proof artifact.

Every non-open slot supplies:

```text
points
removals
survivor_background
owner_fate_witnesses
response_family
feasibility_signatures
selector_data
labelled_vectors
routed_credits
row_loads
transitions
```

The source digest is recomputed from these fields. For expected host `H` and payload digest `s`, the
fibre ID is

```text
H:<first 16 hexadecimal characters of s>
```

A proved slot requires one `slot-candidate-population-proof` artifact citing its exact T02 case,
clause and global-parent-application artifacts.

The unique `population-certificate` for `SLOT_AND_CANDIDATE_POPULATION` uses

```text
slot-candidate-population-registry://SLOT_AND_CANDIDATE_POPULATION
```

and binds the complete expected-slot, T02, slot-record, literal-payload, slot-artifact and per-slot
bundle banks. Readiness must agree with `SLOT_AND_CANDIDATE_POPULATION` and
`T03_SLOT_CANDIDATE_POPULATION`.

Enter genuine payloads as soon as available. Keep them `populated` until exact T02 support and
ordinary proof review exist.

## 5. Close the exact T04 block/interface bank

CMR2478--CMR2485 reconstruct the T04 worklist from the recurrence skeleton:

- one unit for every expected recurrent block;
- one unit for every expected return row;
- one unit for every expected interface row; and
- one unit for every expected off-diagonal row.

Canonical unit IDs are:

```text
block::<expected block ID>
interface::<expected row ID>
```

Every unit is `open`, `populated` or `proved`. Each non-open unit binds the exact T03 ancestry:

```text
parent_global_state_id
operation_slot_id
slot_population_payload_sha256
fibre_id
source_sha256
```

A recurrent-block payload contains:

```text
local_states
recurrent_rows
return_routes
interface_attachments
source_clause_bindings
```

An interface-row payload contains:

```text
target_states
route_data
transition_data
source_clause_binding
```

A proved recurrent block requires `recurrent-block-population-proof`; a proved interface row
requires `interface-row-population-proof`. Support is the complete unique T03 slot-artifact set used
by the unit.

The T04 aggregate bank excludes current-frontier, atomic-completion and target-registry hashes to
avoid indirect self-hashing. The T04 target artifact has kind `global-population-bank`, locator

```text
block-interface-population-registry://T04_BLOCK_INTERFACE_POPULATION
```

and proof digest equal to the noncircular aggregate bank. Readiness must agree with
`T04_BLOCK_INTERFACE_POPULATION`.

## 6. Close the exact T05 finite geometry/selector bank

CMR2486--CMR2493 give every expected slot one open/proved T05 record. A proved slot requires one
validated linked-operation selector certificate and one `slot-geometry-selector-proof` artifact.

The finite certificate must project exactly into T03:

```text
pre-response points       -> points
removed point indices     -> removals
surviving background      -> survivor_background
rank-1/2/3 fate records   -> owner_fate_witnesses
all perfect matchings     -> response_family
finite minima/thresholds  -> selector_data
```

The nested finite checkers verify every responsewise identity

```text
direct_delta(Q) = new_background_triples(Q) - destroyed_current_triples
```

and the equivalence

```text
minimum_delta < 0
```

if and only if

```text
minimum_new_triples < destroyed_current_triples.
```

Each slot artifact cites the exact T03 population artifact and every T04 assembly artifact whose
skeleton parent uses that slot.

The two required `GEOMETRY_SELECTOR_CORRECT` artifacts are:

```text
geometry-proof
selector-proof
```

with locators

```text
geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/geometry-proof
geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/selector-proof
```

and digests equal to the separate reconstructed geometry and selector banks. Both cite exactly the
`SLOT_AND_CANDIDATE_POPULATION` artifact bank.

The T05 target artifact has kind `geometry-selector-proof`, locator

```text
geometry-selector-frontier://T05_GEOMETRY_SELECTORS
```

and proof digest equal to the noncircular combined T05 bank. The sealed digest excludes ancestor
obligation/current-frontier/target-registry certificates that contain the T05 obligation or
completion digests.

Readiness must agree with `GEOMETRY_SELECTOR_CORRECT` and `T05_GEOMETRY_SELECTORS`.

After the documentary bank closes, prove the ordinary theorem that the finite raw-host bank covers
the genuine recurrence geometry for arbitrary `n`. Finite arithmetic alone does not establish that
coverage.

## 7. Prove candidate policy and fate/transition/state semantics

T05 does not prove `T06_CANDIDATE_POLICY` or `T07_FATE_TRANSITION_STATE`.

For every parent and candidate, prove that the intended recurrence policy really minimizes the
relevant load with the declared deterministic tie-break. The existing finite policy checker computes
the least exact common-weight row load, but the external theorem must identify that quantity with the
intended recurrence objective.

Separately prove every owner/fate, deletion, domination, transfer, child-state and transition
statement. Exact state labels, witness records and transition payloads are documentary objects until
their mathematical meanings are proved.

## 8. Prove active-row, resource and routed-credit semantics

Publish the complete simultaneously active row family and prove that it is exhaustive. Prove that
destroyed triples are the complete shared-resource model, establish global resource/obligation
injectivity and prove every routed credit's child-state meaning.

This closes the atomic fronts for:

- `T08_ACTIVE_ROW_FAMILY`;
- `T09_RESOURCE_MODEL`; and
- `T10_CREDIT_ROUTING`.

## 9. Close recurrent blocks and auxiliary expansions

For every recurrent block prove exact parent coverage and

\[
\boxed{\text{closed}\land\text{strongly connected}\land\min_p\mu_p>0.}
\]

T04 supplies literal block assembly only. It does not establish closure, connectivity,
common-weight positivity or strictness.

Prove every recursive auxiliary expansion semantically, eliminate all auxiliaries and regenerate
literal routes whenever elimination changes a selected response.

## 10. Prove cross-block and interface semantics

Prove every state-equivalence edge, component scale, global-state predicate, final-row theorem and
signed fixed-offset interpretation. Publish and prove the complete return/interface/off-diagonal
family and a genuinely well-founded rank.

T04 population does not establish `T15_INTERFACE_EXHAUSTIVENESS`; finite strict-or-ranked rows do not
establish `T16_GLOBAL_RANK`.

## 11. Close all 252 exceptional chambers

The exact worklist is

\[
232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.
\]

Give and prove one disposition for every chamber: final-row theorem, direct proof,
survivor-signature infeasibility or host-union proof.

All 232 zero-selector dispositions are required for `EXCEPTIONAL_ZERO_ROWS_CLOSED`; all 20 hard-core
dispositions are required for `HARD_CORE_ROWS_CLOSED`.

The hard core retains distinct scalar measurements: fixed-response correction 17, minimum rollback
distance 12 and uniform correction 44.

## 12. Maintain the noncircular typed proof stack

Every proved semantic obligation requires its exact artifact kinds and exact dependency support.
Every final premise and every handoff assertion requires one typed artifact bundle.

Every completed atomic target requires a sealed artifact with:

- a separate external proof pointer;
- exact immediate target-artifact support;
- namespace-qualified external artifact references;
- role-qualified certificate references; and
- completion digest equal to the reconstructed target bundle.

Key registry locators now include:

```text
source-verification-artifact-registry://<source ID>
rule-exhaustiveness-artifact-registry://<T02 record ID>
slot-candidate-population-registry://<T03 slot ID>
block-interface-population-registry://<T04 unit ID>
geometry-selector-slot-registry://<T05 slot ID>
```

Aggregate T04 and T05 proof digests must exclude ancestor certificates containing their own target
completion or obligation digests.

## 13. Complete the ten premises and six handoff assertions

Close the ten final premises:

1. base cases;
2. recurrence exhaustiveness;
3. invariant preservation;
4. operation selection;
5. resource/credit soundness;
6. block/auxiliary contraction;
7. cross-block assembly;
8. exceptional closure;
9. termination; and
10. objective translation.

Then close the six handoff assertions: base domain, nonbase recurrence coverage, invariant
preservation, branch termination, exceptional closure and translation to `D(n)=2n`.

## 14. Use the atomic schedule and synchronized gates

The atomic checker fixes thirteen frontier groups and forty-three targets. It publishes separate
acyclic proof-closure and research-start graphs, proof/research actionable sets, parallel waves,
longest blocker chains and downstream impact.

A claimed all-frontier dossier must agree with:

- six handoff artifact bundles;
- independent 232/20 chamber readiness flags;
- the sealed artifact bank for completed targets;
- the exact T01 source census and sealed source artifacts;
- the exact T02 case/clause/axis/exclusion/application bank;
- the exact T03 slot census, payload and proof bank;
- the exact T04 skeleton-derived unit census and proof bank; and
- the exact T05 geometry/selector records, finite certificates, T03/T04 support, two obligation banks
  and noncircular target artifact.

Passing these gates proves documentary identity and coverage only.

## 15. Immediate execution order

1. Populate and prove the highest-use T01 source statements.
2. Close all source statements and pass T01 synchronization.
3. Populate and prove every T02 record.
4. Review the ordinary recurrence-exhaustiveness theorem.
5. Enter literal T03 payloads and retain useful unproved data as `populated`.
6. Prove every T03 slot and pass T03 synchronization.
7. Enter literal T04 assembly payloads.
8. Prove every T04 unit and pass T04 synchronization.
9. Enter and prove every T05 finite geometry/selector record.
10. Prove that the T05 finite bank covers the genuine recurrence geometry.
11. Prove candidate policy and fate/transition/state semantics.
12. Prove active-row, resource and routed-credit semantics.
13. Close strict recurrent blocks and auxiliary expansions.
14. Prove cross-block identities, scales, interfaces, ranks, predicates and row theorems.
15. Populate and prove all 252 chamber dispositions.
16. Populate genuine noncircular obligation, premise, handoff and atomic-target artifacts.
17. Close all ten premises, six handoff assertions and 43 atomic targets.
18. Pass the source-root, T02, T03, T04, T05, synchronized current-frontier, sealed target-artifact
    and seven-gate pre-root audits.
19. Write and review the ordinary proof that the quotient and handoff imply `D(n)=2n`.

## 16. Fixed semantic obligation DAG

The nineteen exact obligations are:

`SOURCE_STATEMENTS_TRUE`, `RULE_EXHAUSTIVE`, `SLOT_AND_CANDIDATE_POPULATION`,
`GEOMETRY_SELECTOR_CORRECT`, `FATE_TRANSITION_STATE_SEMANTICS`,
`CANDIDATE_POLICY_CORRECT`, `ACTIVE_ROW_FAMILY_EXHAUSTIVE`,
`DESTROYED_RESOURCE_MODEL_EXHAUSTIVE`, `CREDIT_ROUTING_SEMANTIC`,
`CLOSED_STRICT_RECURRENT_BLOCKS`, `AUXILIARY_EXPANSIONS_SEMANTIC`,
`CROSS_BLOCK_STATE_IDENTITY_SEMANTIC`, `COMPONENT_SCALE_SEMANTIC`,
`INTERFACE_RETURN_ROWS_EXHAUSTIVE`, `GLOBAL_RANK_WELL_FOUNDED`,
`EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE`, `EXCEPTIONAL_ZERO_ROWS_CLOSED`,
`HARD_CORE_ROWS_CLOSED`, and `GLOBAL_QUOTIENT_IMPLIES_ALL_N`.

T01, T02, T03 and T05 now have explicit internal evidence censuses. T04 has no separate semantic
obligation; its aggregate proof binding is the atomic `T04_BLOCK_INTERFACE_POPULATION` target.
These interfaces do not change the DAG.

## 17. Honesty boundaries

- A source locator and unattached digest do not identify literal text.
- Exact text and a matching hash do not prove the statement true.
- Sealed source artifacts do not verify mathematical validity.
- Exact global-parent-to-slot binding does not prove the rule genuine or exhaustive.
- Literal T03 data and canonical fibre hashes do not prove the payload correct or exhaustive.
- A `populated` T03 slot is research progress, not proof completion.
- Literal T04 assembly data do not prove geometry or recurrence semantics.
- A `populated` T04 unit is research progress, not a proved block or interface row.
- Exact finite T05 arithmetic does not prove the bank covers every all-`n` recurrence geometry.
- A proved T05 record does not establish candidate-policy, state-label or transition semantics.
- Candidate coverage does not prove the intended policy.
- Resource scopes do not prove active-row or resource-model exhaustiveness.
- Common weights do not imply closure, connectivity or strictness.
- Auxiliary elimination does not prove transition semantics.
- State links and predicate records do not prove external state identity.
- Strict-or-ranked rows do not prove interface exhaustiveness.
- Support condensation does not prove the quotient models the recurrence.
- Typed artifact support does not prove truth or logical sufficiency.
- A target proof digest cannot include an ancestor containing that target's own completion digest.
- A closed chamber disposition does not verify its proof.
- Atomic completion, synchronization and dependency waves are documentary metadata.
- Every final checker reports `all_n_proved_by_checker = 0`.
- Syntax compilation does not imply dependency-backed suites ran.

## 18. Current endpoint

Through CMR2493 the finite interface reaches a noncircular global quotient dossier, typed support
through final handoff assertions and every atomic target, an explicit 252-chamber registry,
synchronized execution/evidence gates, exact T01 and T02 banks, exact T03 and T04 population banks,
and an exact T05 finite geometry/selector bank with literal T03 projection, exact T04-use support,
separate semantic-obligation seals and a noncircular target seal.

The unresolved center remains genuine mathematics: literal source content, valid source and rule
proofs, the actual exhaustive recurrence, actual T03/T04 population, proof that T05 covers every
recurrence geometry, candidate-policy and fate/transition/resource semantics, strict block closure,
cross-block and interface/rank semantics, every chamber disposition and the reviewed implication to
all `n`.
