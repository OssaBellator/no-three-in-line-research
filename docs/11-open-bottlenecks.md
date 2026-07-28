# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through CMR2477 the branch has a complete finite
certificate architecture from source-traceable rule clauses to a global integer quotient,
semantic predicates and row theorems, typed obligation/premise/handoff artifacts, a seven-gate
pre-root integrity audit, an exact 252-chamber exceptional worklist, a 43-target execution schedule
over thirteen genuine research frontiers, synchronized chamber/target gates, sealed atomic-target
evidence, an exact source-statement/T01 root bank, an exact T02 rule-exhaustiveness work bank, and
an exact T03 slot/candidate population work bank.

The branch still lacks the literal genuine source statements, the genuine exhaustive recurrence,
complete real population, proved external semantics, complete strict blocks and interface rows,
mathematically closed chamber proofs and the reviewed implication to `D(n)=2n`.

## 2. Close the exact source-statement bank

CMR2438--CMR2445 make `T01_SOURCE_STATEMENTS` executable. For every source in the rule-provenance
certificate:

1. transcribe the exact mathematical statement text;
2. recompute its SHA-256 from the exact UTF-8 text and match the stored provenance digest;
3. retain the exact source ID, kind and locator;
4. mark the statement `open` or `proved`; and
5. for a proved statement, supply the fixed source-kind-specific verification artifact.

The required artifact kinds are:

| Source kind | Required artifact |
|---|---|
| `definition` | `definition-conformance-proof` |
| `case-split` | `case-split-exhaustiveness-proof` |
| `lemma` | `lemma-proof` |
| `domain` | `domain-characterization-proof` |
| `exclusion` | `exclusion-proof` |
| `computation` | `reproducible-computation-proof` |

CMR2454--CMR2461 require each proved statement to have one canonical verification artifact. For
source ID `S`, the statement record must bind

```text
source-verification-artifact-registry://S
```

and the reconstructed artifact-bundle digest. The artifact carries a separate external proof
locator/digest, the exact statement hash, a proof statement, evidence and a sorted list of
supporting source-verification artifact IDs. Open statements carry no artifacts. The complete
support graph must be acyclic.

The registry reconstructs the exact case/clause/axis/exclusion footprint of every source and orders
open source IDs by decreasing downstream use. Use that order to choose high-leverage proof work,
not as an estimate of difficulty.

The complete source-truth bundle must be bound by the unique `source-truth-proof` artifact for
`SOURCE_STATEMENTS_TRUE`. CMR2446--CMR2453 require the same obligation registry to appear in the
current-frontier stack and require exact agreement with `T01_SOURCE_STATEMENTS`.

## 3. Close the exact T02 rule-exhaustiveness bank

CMR2462--CMR2469 make `T02_RULE_EXHAUSTIVENESS` an exact proof-work interface. After the source bank
closes, populate one open/proved record for every:

- parent case;
- rule clause;
- finite parameter axis;
- excluded parameter row; and
- global parent in the recurrence skeleton.

Each proved record requires one artifact of its fixed kind. Its exact source support is reconstructed
from the provenance certificate. Internal support is fixed by

```text
axis/exclusion -> clause -> case -> global-parent application.
```

For every global parent, provide the exact triple

```text
source_case_id
source_clause_id
operation_slot_id
```

The selected slot must be one of the source-independent expected slots generated from an admitted
parameter row. It must match the skeleton case, case/clause incidence, local parent state, expected
host, ordered labels and operation kind.

The existing typed artifacts for `RULE_EXHAUSTIVE` must bind:

```text
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-manifest
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-exhaustiveness-proof
```

The first digest seals the rule source, clause manifest, expected slot registry, recurrence skeleton,
cases and clauses. The second seals the complete T02 record and artifact banks together with the
source-statement registry.

Reconstructed readiness must agree exactly with both `RULE_EXHAUSTIVE` and
`T02_RULE_EXHAUSTIVENESS`. The existing clause enumerator explicitly states that the actual parent
rule is not yet present. Exact application-to-slot identity is therefore a review surface, not proof
that the supplied cases and clauses are the genuine exhaustive recurrence.

## 4. Complete genuine population

### Close the exact T03 slot/candidate bank

CMR2470--CMR2477 make `T03_SLOT_CANDIDATE_POPULATION` executable without collapsing research data
entry into a proof claim. Every independently expected operation slot has one state:

- `open`: no payload or proof artifact;
- `populated`: one literal payload, but no T02-backed proof artifact;
- `proved`: one literal payload and one sealed slot-specific proof artifact.

Every non-open slot must supply the exact ordered payload fields:

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

The source digest is recomputed from those literal fields. For expected host `H` and payload digest
`s`, the fibre ID must be

```text
H:<first 16 hexadecimal characters of s>
```

A proved slot requires one `slot-candidate-population-proof` artifact. Its exact T02 support is the
slot's case artifact, clause artifact and every global-parent-application artifact selecting that
slot. Slots not selected by a global parent still require their case and clause artifacts because
they belong to the complete candidate family.

The unique `population-certificate` for `SLOT_AND_CANDIDATE_POPULATION` must use

```text
slot-candidate-population-registry://SLOT_AND_CANDIDATE_POPULATION
```

and bind the complete expected-slot, T02 record, T02 artifact, slot record, literal payload,
slot-proof-artifact and per-slot bundle banks. Reconstructed readiness must agree exactly with both
`SLOT_AND_CANDIDATE_POPULATION` and `T03_SLOT_CANDIDATE_POPULATION`.

Enter genuine T03 payloads as soon as they are available. Keep them in state `populated` until the
required T02 artifacts and ordinary proof review exist. Counts, host equality or an unattached
source digest are not sufficient.

### Complete the separate T04 block/interface bank

After the T03 candidate family is populated, build the distinct
`T04_BLOCK_INTERFACE_POPULATION` bank. Populate every recurrent block, return row and interface row
with the actual parent coverage, geometry, fate, route, transition and source-clause identity.

T04 must not be inferred from T03 slot coverage. Candidate-operation population and recurrent-
block/interface assembly are separate proof surfaces with different downstream uses.

## 5. Geometry, selectors and candidate policy

Prove every real geometric identity, threshold and selector chamber. Compute

\[
\lambda_s=\min_Q L_s(Q)
\]

for every candidate and prove that minimizing `(lambda_s, slot ID)` is the intended recurrence
policy. This closes `GEOMETRY_SELECTOR_CORRECT` and `CANDIDATE_POLICY_CORRECT`.

## 6. Fate, transition, resource and credit semantics

Prove all owner/fate, deletion, domination, transfer, child-state and transition statements.
Publish the complete simultaneously active row family and prove destroyed triples are the complete
shared-resource model. Prove global resource/obligation injectivity and every routed credit's
child-state meaning.

This includes the atomic targets for fate/transition/state, active rows, resource exhaustiveness
and routed-credit semantics.

## 7. Closed recurrent blocks and auxiliary elimination

For every recurrent block prove exact parent coverage and

\[
\boxed{\text{closed}\land\text{strongly connected}\land\min_p\mu_p>0.}
\]

Prove every recursive auxiliary expansion semantically, eliminate all auxiliaries and regenerate
literal routes whenever elimination changes a selected response.

## 8. Cross-block and interface semantics

Prove every state-equivalence edge, relative block/component scale, global-state predicate,
final-row theorem and signed fixed-offset interpretation. Publish and prove the complete return,
interface and off-diagonal family and a genuinely well-founded rank.

The finite quotient, state predicates, row theorem records and support condensation remain
interfaces until these external statements are proved.

## 9. Close all 252 exceptional chambers

CMR2398--CMR2405 fix

\[
232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.
\]

Give one exact disposition for every chamber: final row theorem, direct proof, survivor-signature
infeasibility or host-union proof. Prove every disposition. All 232 zero-selector dispositions are
required for `EXCEPTIONAL_ZERO_ROWS_CLOSED`; all 20 hard-core dispositions are required for
`HARD_CORE_ROWS_CLOSED`.

The hard core retains three distinct scalar measurements: fixed-response correction 17, minimum
rollback distance 12 and uniform correction 44.

## 10. Noncircular typed proof stack

Supply and prove the exact required artifact kinds for every semantic obligation. The obligation-
artifact support graph must be acyclic, dependency aligned and complete over every immediate
prerequisite bundle.

Supply one typed artifact for each final premise and one typed artifact for each handoff assertion.
Each proved handoff assertion must cite exactly the complete premise-artifact set of its fixed
dependencies and bind its reconstructed bundle digest.

Every effectively complete atomic target must have one sealed artifact of its fixed kind. Its
external proof pointer is separate from the completion seal; immediate target support is exact;
external artifact references are namespace-qualified; and certificate references are role-
qualified. The atomic completion locator is
`atomic-target-artifact-registry://<target ID>` and the completion digest equals the reconstructed
bundle digest.

For each proved source statement `S`, the verification locator is
`source-verification-artifact-registry://S` and its digest equals the reconstructed per-source
artifact bundle. The artifact's external proof pointer is separate, and source-proof support must
be acyclic.

For each proved T02 record `R`, the verification locator is
`rule-exhaustiveness-artifact-registry://R`. Source and internal rule support must equal the
reconstructed support sets; neither omitted nor unrelated support is accepted.

For each proved T03 slot `S`, the population locator is
`slot-candidate-population-registry://S`. Its digest binds the exact slot, literal payload,
slot-proof artifact and reconstructed T02 support. A merely `populated` slot instead uses the data
URI and cannot carry a proof artifact.

For the source root, the `source-truth-proof` artifact locator is
`source-statement-truth-registry://SOURCE_STATEMENTS_TRUE` and its digest equals the complete source
truth bundle digest.

## 11. Complete the ten premises and six handoff assertions

Close the ten final premises: base cases, recurrence exhaustiveness, invariant preservation,
operation selection, resource/credit soundness, block/auxiliary contraction, cross-block assembly,
exceptional closure, termination and objective translation.

Then close the six handoff assertions: base domain, nonbase recurrence coverage, invariant
preservation, branch termination, exceptional closure and translation to `D(n)=2n`.

## 12. Use the atomic all-frontier schedule

CMR2406--CMR2413 refine the work into thirteen frontier groups and forty-three atomic targets. The
checker publishes:

- separate acyclic proof-closure and research-start dependency graphs;
- exact links to all 19 obligations, 10 premises, 6 handoff assertions and one dossier gate;
- proof-actionable and research-actionable target sets;
- parallel completion/start waves and canonical longest blocker chains; and
- per-frontier downstream impact.

Use research-actionable targets to begin independent work without claiming closure. Use proof-
actionable targets and proof waves to sequence completion. These quantities are planning
arithmetic, not time or difficulty estimates.

## 13. Use the synchronized execution gates

CMR2414--CMR2421 synchronize the atomic schedule with the typed handoff-assertion artifact registry
and exact 252-chamber disposition registry. CMR2422--CMR2437 add sealed target-artifact evidence.
CMR2446--CMR2461 add the exact and sealed source-root path. CMR2462--CMR2469 add the exact T02 bank.
CMR2470--CMR2477 add the exact T03 slot/candidate population bank.

A claimed all-frontier dossier must therefore agree with:

- six handoff artifact bundles;
- independent 232/20 chamber readiness flags;
- the exact sealed artifact bank for completed targets;
- the exact literal source statement census used by `T01_SOURCE_STATEMENTS`;
- one sealed, acyclically supported verification artifact for every proved source statement;
- the exact case/clause/axis/exclusion/application census used by `T02_RULE_EXHAUSTIVENESS`, with
  every global parent bound to one expected operation slot; and
- the exact T03 slot census, literal payload bank and T02-backed slot-proof bank used by
  `SLOT_AND_CANDIDATE_POPULATION` and `T03_SLOT_CANDIDATE_POPULATION`.

Passing these gates proves documentary identity and coverage only, not the mathematics.

## 14. Immediate execution order

1. Populate the literal source statement bank and prove the highest-use open source statements
   using sealed, noncircular verification artifacts.
2. Close all source statements and pass the source-root/T01 synchronization gate.
3. Populate the exact T02 case, clause, axis, exclusion and global-parent application bank.
4. Prove each T02 record with exact source/internal support and pass the T02 synchronization gate.
5. Review the ordinary theorem that the resulting parent-rule bank is genuinely exhaustive.
6. Enter literal T03 payloads for every expected slot and keep independently useful data in state
   `populated` until exact T02 support is available.
7. Prove every T03 slot, bind the aggregate population certificate and pass T03 synchronization.
8. Populate and prove the separate T04 recurrent-block and interface-row bank.
9. Prove geometry, selectors, fate, transitions, resources and candidate policy.
10. Close strict recurrent blocks and semantic auxiliary expansions.
11. Prove cross-block identities, scales, interface rows, ranks, predicates and row theorems.
12. Populate and prove all 252 exceptional chamber dispositions.
13. Populate genuine noncircular obligation, premise, handoff and sealed atomic-target artifacts.
14. Close all ten premises, all six handoff assertions and all 43 atomic targets.
15. Pass the source-root, T02, T03, synchronized current-frontier, sealed target-artifact and seven-
    gate pre-root audits.
16. Write and review the ordinary proof that the quotient and handoff imply `D(n)=2n`.

## 15. Fixed semantic obligation DAG

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

An obligation cannot close while an exact dependency remains open. The source, T02 and T03
registries make the first three obligations' internal evidence censuses explicit; they do not change
the DAG.

## 16. Honesty boundaries

- A source locator and unattached statement digest do not identify literal text.
- Exact text and a matching SHA-256 do not prove the statement true.
- Repeating an external proof locator/digest is not statement-to-proof binding.
- Typed and sealed source artifacts do not verify mathematical validity.
- Acyclic source-proof support does not prove logical sufficiency.
- Exact global-parent-to-slot binding does not prove the supplied rule genuine or exhaustive.
- Sealed T02 records do not verify their external proof artifacts.
- Literal T03 population data and canonical fibre hashes do not prove the payload genuine, correct
  or exhaustive.
- A `populated` T03 slot is research progress, not proof completion.
- Exact T03 slot coverage does not populate T04 recurrent blocks or interface rows.
- Source-truth readiness does not establish recurrence exhaustiveness.
- Rule and family completeness remain relative to supplied data until proved externally.
- Candidate coverage does not prove the intended policy.
- Resource scopes do not prove active-row or resource-model exhaustiveness.
- Common weights do not imply closure, connectivity or strictness.
- Auxiliary elimination does not prove transition semantics.
- State links and predicate records do not prove external state identity.
- Strict-or-ranked rows do not prove the interface family exhaustive.
- Support condensation does not prove the quotient models the recurrence.
- Typed artifact support does not prove truth or logical sufficiency.
- A closed chamber disposition does not verify its proof.
- Atomic completion, synchronization records, sealed target artifacts and dependency waves are
  documentary metadata.
- Edgewise lexicographic descent is sufficient, not necessary.
- A ready contract, handoff or audit remains subject to mathematical review.
- Every final checker reports `all_n_proved_by_checker = 0`.
- Syntax compilation does not imply dependency-backed suites ran here.

## 17. Current endpoint

Through CMR2477 the finite interface reaches a noncircular global quotient dossier, typed support
through final handoff assertions and every atomic frontier target, an explicit 252-chamber closure
registry, synchronized execution/evidence gates, an exact statement-by-statement source root
synchronized with T01, an exact T02 case/clause/axis/exclusion/application bank, and an exact T03
slot/candidate population bank with literal payload and T02-backed proof sealing. Every proved
source, T02 or T03 entry requires a sealed artifact with exact support. The unresolved center is the
genuine mathematics: literal source content, valid proofs of those statements and rule records,
actual T03 population data and review, the separate T04 block/interface population, proof of every
semantic statement and chamber disposition, strict block closure and the reviewed implication to
all `n`.
