# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2597**, the branch contains exact
noncircular documentary work banks from T01 through T18, typed proof registries for all 43 atomic
targets, an exact 252-chamber exceptional worklist and a final dossier audit.

The branch still lacks the genuine source statements, exhaustive recurrence theorem, actual complete
population, arbitrary-`n` coverage, truth of the semantic claims, global-family exhaustiveness, chamber
proofs and the reviewed implication to `D(n)=2n`.

Every final checker permanently reports:

```text
all_n_proved_by_checker = 0
```

## 2. T01--T04: close the root and enter the actual population

For T01, transcribe each exact source statement, recompute its UTF-8 digest, supply its fixed-kind proof
artifact and complete ordinary mathematical review.

For T02, populate and prove every case, clause, finite axis, exclusion and global-parent application. Every
application must bind its exact source case, clause and operation slot. Then prove the supplied rule bank
is the genuine exhaustive recurrence.

For T03, enter every literal operation-slot field: points, removals, survivors, fate witnesses, responses,
selectors, vectors, routed credits, loads and transitions. Keep useful data `populated` until its proof
support exists.

For T04, enter every skeleton-derived recurrent block and return/interface/off-diagonal row with exact T03
ancestry. Recurrent blocks need local states, recurrent rows, return routes, interface attachments and
source-clause bindings. Interface rows need target, route, transition and source-clause data.

## 3. T05--T10: geometry, policy, state, resources and credits

Use the corrected T05 endpoint:

```text
scripts/check_prime_power_geometry_selector_frontier_v2.py
```

Prove every responsewise finite delta, threshold and selector theorem, then prove arbitrary-`n` coverage.

For T07, prove every exact fate, state and transition statement. An acyclic support graph is necessary
metadata, not semantic proof.

For T06, prove every integer candidate score, reconstruct every complete candidate set, select the least
`(score, slot_id)` pair and prove every T02 application uses that winner.

Use the combined T08--T10 endpoint:

```text
scripts/check_prime_power_transition_resource_frontier.py
```

Prove the application-derived active-row census is the genuine simultaneous family, the coordinate-
canonical resource bank is physically exhaustive, and every routed-credit assignment has the claimed
resource, witness, child-state and transition meaning.

## 4. T11 and T12: block contraction and auxiliary elimination

Use:

```text
scripts/check_prime_power_recurrent_block_closure_frontier.py
scripts/check_prime_power_auxiliary_semantics_frontier_v2.py
```

Every T11 block must bind the exact selected row population and provide primitive positive weights, one
row per recurrent parent, exact recurrent support, no recurrent exit, strong connectivity and positive
margin.

Every T12 block must reuse the exact T11 common-weight certificate, prove the recursive auxiliary graph
acyclic, prove local and effective weighted domination, forbid auxiliary credit, reconstruct every
eliminated row and preserve the selected response and strict margin.

## 5. T13--T16: global identity, scales, interfaces and rank

Use:

```text
scripts/check_prime_power_state_equivalence_frontier.py
scripts/check_prime_power_component_scale_frontier.py
scripts/check_prime_power_interface_exhaustiveness_frontier.py
scripts/check_prime_power_global_rank_frontier.py
```

T13 derives every local state from T04 and requires exact T07-supported global-state links and spanning
proof trees. T14 reconstructs all shared-state scale equations from T11 weights and T13 classes, rejects
inconsistent cycles and publishes primitive component weights.

T15 derives every interface row from T04, supplies a primitive intercomponent multiplier bank, reconstructs
final weights and margins, and covers every T11/T12 final exit. Strict rows have positive margin; zero-
margin rows remain explicit T16 work.

T16 derives every critical edge from T15, requires an explicit nonnegative-integer or fixed lexicographic
rank domain, proves exact endpoint ranks and edge descent, rejects cycles and publishes the exact longest
critical path.

The finite checks do not prove that state identities, scale equations, interface statements or ranks have
their intended recurrence meaning.

## 6. T17: exact global-state predicates

Use:

```text
scripts/check_prime_power_state_predicate_frontier.py
```

The corrected target dependency is:

```text
T13_STATE_EQUIVALENCE + T16_GLOBAL_RANK
    -> T17_STATE_PREDICATES
```

Research can begin after T13, but proof closure waits for T16. The old parallel semantic-refinement
certificate is not a T17 support requirement.

Every T13 global class contributes one canonical open/proved record containing:

```text
global_state_id
global_state_record_sha256
t13_class_artifact_id
predicate_id
status
verification_locator
verification_digest
note
```

Every proved predicate must:

1. bind the exact T13 role, stratum, owner and class artifact;
2. contain one agreement record for every literal local representative;
3. bind each representative's exact T07 state-claim support;
4. bind the exact proved T16 rank record and artifact exactly when rank-sensitive;
5. state the predicate, representative agreement and external meaning; and
6. carry one `global-state-predicate-proof` artifact with exact T13/T16 support.

The aggregate noncircular bank synchronizes `T17_STATE_PREDICATES` through:

```text
state-predicate-frontier://T17_STATE_PREDICATES
```

Representative coverage and typed evidence do not prove predicate truth.

## 7. T18: exact final row theorems

Use:

```text
scripts/check_prime_power_row_theorem_frontier.py
```

T18 does not accept an independent quotient row list. Its exact census is:

```text
all T12-eliminated selected recurrent rows
+
all T15 return/interface/off-diagonal rows
```

### 7.1 Recurrent final rows

For every selected recurrent row:

1. bind its exact T11 row bridge and selected slot;
2. bind its exact T12 row and block elimination digests;
3. map its parent and final targets through T13;
4. derive the exact integer scale from the T11 local parent weight and T14/T15 final global weight;
5. aggregate equal global targets; and
6. verify the scaled fixed offset, row load and positive margin.

### 7.2 Interface final rows

Reuse each exact T15 row. A positive-margin row remains `strict`. A zero-margin row becomes
`critical-descending` only if every positive target has its exact proved T16 descent edge.

### 7.3 Predicate and theorem semantics

Every proved row must reconstruct:

```text
parent T17 predicate
target T17 predicate multiset and multiplicities
fixed offset
row load
margin
strict/critical classification
critical T16 edge IDs, when applicable
row theorem statement
fixed-offset interpretation
external recurrence statement
evidence
```

Every proved row carries one `global-row-theorem-proof`. Recurrent rows cite the relevant T05, T07, T10,
T11, T12, T14, T15-scale and T17 artifacts. Interface rows cite the relevant T07, T14, T15, T17 and, when
critical, T16 artifacts.

The aggregate bank synchronizes:

```text
T18_ROW_THEOREMS
```

through `row-theorem-frontier://T18_ROW_THEOREMS`. Exact arithmetic and predicate multisets do not prove
the external row theorem or fixed-offset meaning.

## 8. T19: build the exact global-family exhaustiveness frontier

T19 is the next executable frontier. Do not use an independently supplied global integer family as the
population root.

### 8.1 Expected application census

Derive every expected global application from the exact T02 recurrence skeleton. Each expected item must
bind at least:

```text
source_case_id
source_clause_id
parent_global_state_id
operation_slot_id
application_identity_sha256
```

### 8.2 Exact final-row census

Take the complete T18 final-row subject bank. Partition it into recurrent and interface families and bind
each row to its exact `global-row-theorem-proof` artifact.

### 8.3 Parent-to-row coverage

For every T02 global parent, reconstruct exactly which T18 rows are permitted by its selected slot,
recurrent-block membership, return/interface attachments and source-clause bindings. Require:

1. every expected parent has at least one permitted final row or a proved terminal disposition;
2. every permitted row is present exactly once;
3. no T18 row is unrelated to the T02 skeleton;
4. no extra parent, slot, row or terminal disposition is supplied; and
5. every row theorem has the exact source-case and source-clause ancestry.

### 8.4 Exhaustiveness theorem

For each T02 case and clause, supply a statement and evidence proving that the reconstructed final-row
alternatives cover every genuine recurrence outcome. The checker can verify finite coverage and identity;
the ordinary exhaustiveness statement remains external mathematics.

### 8.5 Typed sealing

Give every proved case/clause coverage unit a typed artifact supported by its exact T02 and T18 artifacts.
Build one noncircular aggregate bank that synchronizes:

```text
EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE
T19_GLOBAL_FAMILY
```

with `global-family-exhaustiveness-proof` / `global-family-proof` artifacts and exact immediate support.

The target-artifact registry must not reintroduce the older `global_family_skeleton` or global-integer-
quotient certificate as independent proof of the final row population.

## 9. T20 and T21: exceptional chamber closure

After T19, close the exact worklist:

\[
232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.
\]

Every chamber needs one reviewed disposition and exact row ancestry. Keep fixed-response correction `17`,
rollback distance `12` and uniform correction `44` distinct.

## 10. T22--T43: final premises and handoff

Complete every genuine semantic-obligation artifact, the ten final premises, six handoff assertions and
the seven-gate dossier audit. Then prove the ordinary implication from the reviewed quotient and handoff
to `D(n)=2n`.

Do not place a target's own completion digest inside an ancestor used to seal that target.

## 11. Immediate execution order

1. Populate and prove high-use T01 source statements.
2. Close T01 and every T02 rule record; prove recurrence exhaustiveness.
3. Enter actual T03/T04 data.
4. Prove T05 arbitrary-`n` coverage and every T06/T07 theorem.
5. Prove T08/T09/T10 simultaneous resource and credit semantics.
6. Prove every T11 block and T12 auxiliary expansion.
7. Prove every T13 identity, T14 scale equation, T15 interface theorem and T16 rank theorem.
8. Populate and prove every T17 predicate and T18 final row theorem.
9. Implement exact T19 coverage from T02 and T18; prove genuine global-family exhaustiveness.
10. Prove all 252 T20/T21 chamber dispositions.
11. Complete T22--T43 and review the final implication.
