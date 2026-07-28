# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2581**, the branch contains exact
noncircular documentary work banks from T01 through T16, typed proof registries for all 43 atomic
targets, an exact 252-chamber exceptional worklist and a final dossier audit.

The branch still lacks the genuine source statements, exhaustive recurrence theorem, actual complete
population, arbitrary-`n` coverage, truth of the semantic claims, complete predicate and row theorems,
chamber proofs and the reviewed implication to `D(n)=2n`.

Every final checker permanently reports:

```text
all_n_proved_by_checker = 0
```

## 2. T01 and T02: close the source and recurrence root

For every cited source, transcribe the exact statement, recompute its UTF-8 SHA-256, supply the fixed
source-kind artifact, prove its support noncircular and complete ordinary mathematical review.

For T02, populate and prove every parent case, clause, finite parameter axis, excluded parameter row and
global-parent application. Every application must bind:

```text
source_case_id
source_clause_id
operation_slot_id
```

Then prove the supplied rule bank is the genuine exhaustive recurrence.

## 3. T03 and T04: enter the actual finite population

### T03

Every operation slot is `open`, `populated` or `proved`. Enter the literal point, removal, survivor,
fate-witness, response, selector, vector, credit, load and transition fields. Keep useful data
`populated` until exact T02 support and proof review exist.

### T04

For every skeleton-derived recurrent block and return/interface/off-diagonal row, enter the exact
assembly payload and T03 ancestry.

Recurrent-block fields include:

```text
local_states
recurrent_rows
return_routes
interface_attachments
source_clause_bindings
```

Interface-row fields include:

```text
target_states
route_data
transition_data
source_clause_binding
```

## 4. T05--T07: geometry, state semantics and candidate policy

Use the corrected T05 endpoint:

```text
scripts/check_prime_power_geometry_selector_frontier_v2.py
```

Prove every finite responsewise delta, threshold and selector statement, then prove that the finite bank
covers every genuine recurrence geometry for arbitrary `n`.

For every T07 fate, state and transition subject, provide one canonical statement, evidence and acyclic
support list. Acyclic support is not semantic proof.

For T06, prove every integer `minimum_labelled_row_load`, reconstruct every complete candidate set,
select the least pair

```text
(minimum_labelled_row_load, slot_id)
```

and prove every T02 application uses that winner.

## 5. T08--T10: simultaneous rows, resources and routed credits

Use:

```text
scripts/check_prime_power_transition_resource_frontier.py
```

Prove the T06-application-derived active-row census is the genuine simultaneous family. Prove the
coordinate-canonical destroyed triples and overlap scopes are the complete physical resource model.
For every routed-credit subject, prove its destroyed resource, fate/state/transition support, child
state and route statement, including all local and global injectivity claims.

## 6. T11 and T12: block contraction and auxiliary elimination

Use:

```text
scripts/check_prime_power_recurrent_block_closure_frontier.py
scripts/check_prime_power_auxiliary_semantics_frontier_v2.py
```

Every T11 block must bind the exact selected row population and provide primitive positive weights,
one row per recurrent parent, exact recurrent support, no recurrent exit, strong connectivity and
positive margin.

Every T12 block must reuse the exact T11 common-weight certificate, cover the recursive auxiliary
closure, prove acyclic weighted domination, forbid auxiliary credit, reconstruct every eliminated row
and preserve the selected response, load bound and strict margin.

## 7. T13: cross-block state equivalence

Use:

```text
scripts/check_prime_power_state_equivalence_frontier.py
```

For every T04 local state enter one exact T07-supported global-state link. For every derived global
class, prove semantic-core agreement, at most one member per block, and one connected
`member_count - 1` spanning tree. Singleton classes also require proof review.

## 8. T14: component scales

Use:

```text
scripts/check_prime_power_component_scale_frontier.py
```

Using exact T11 weights and T13 classes, reconstruct every equation

\[
\alpha_b w_b(s)=\alpha_c w_c(t),
\]

reject inconsistent cycles, clear denominators, divide the componentwise gcd and prove every equation
and normalization statement. Disconnected components remain independently normalized.

## 9. T15: interface-row exhaustiveness

Use:

```text
scripts/check_prime_power_interface_exhaustiveness_frontier.py
```

The corrected proof root is:

```text
T04_BLOCK_INTERFACE_POPULATION
T07_FATE_TRANSITION_STATE
T12_AUXILIARY_SEMANTICS
T14_COMPONENT_SCALES
    -> T15_INTERFACE_EXHAUSTIVENESS
```

The obligation root is:

```text
FATE_TRANSITION_STATE_SEMANTICS
AUXILIARY_EXPANSIONS_SEMANTIC
COMPONENT_SCALE_SEMANTIC
    -> INTERFACE_RETURN_ROWS_EXHAUSTIVE
```

Concrete certificates carrying the previous obligation or target-definition digests must be
regenerated.

### 9.1 Exact row census

Take every T04 unit of kind `interface-row` in canonical order. Every T15 record binds:

```text
unit_id
row_id
row_kind
unit_identity_sha256
parent_global_state_id
operation_slot_id
t04_population_payload_sha256
```

No independent row list is allowed.

### 9.2 Intercomponent multipliers

For every T14 component provide one positive integer `interface_multiplier`, statement and evidence.
The full vector must have gcd one. Seal it with one:

```text
global-interface-component-scale-proof
```

supported by every T14 component artifact. The final global weight is

\[
\widehat W_g=m_{C(g)}W_g.
\]

### 9.3 Exact row semantics

Every proved row must bind its exact T04 field digests, exact slot T07 claims, exact T13 parent and target
classes, exact T14 weights, one integer fixed offset, positive target multiplicities, statements and
evidence.

Reconstruct

\[
L=B+\sum_g a_g\widehat W_g,
\qquad
M=\widehat W_p-L.
\]

Reject negative margins. Mark positive margins `strict`. Mark zero margins `critical-unranked`; do not
invent a T15 rank witness.

### 9.4 Exact final-exit coverage

Derive final exits from T11 and the selected T12 eliminated rows. Verify that every T11 auxiliary exit
appears in the T12 closure and every T11 nonauxiliary exit remains visible after elimination.

Give every final exit exactly one disposition:

```text
interface-row
terminal-sink
```

A row disposition must use a proved row with the exact source and sufficient target multiplicity. A
terminal disposition is allowed only for an exact T13 sink.

### 9.5 Typed sealing

Every proved row requires one `interface-row-semantic-proof` with exact T04/T07/T12/T13/T14 and
interface-scale support. Bind the aggregate bank through:

```text
INTERFACE_RETURN_ROWS_EXHAUSTIVE
T15_INTERFACE_EXHAUSTIVENESS
```

with `interface-exhaustiveness-proof` artifacts and noncircular digests.

## 10. T16: global-rank well-foundedness

Use:

```text
scripts/check_prime_power_global_rank_frontier.py
```

T16 consumes T15 directly and does not accept an independent support graph or rank table.

### 10.1 Derived critical-edge census

Every T15 semantic row classified `critical-unranked` contributes one subject for every positive target
multiplicity. Each subject binds:

```text
row_id
parent_global_state_id
target_global_state_id
multiplicity
interface_row_semantic_certificate_sha256
interface_target_semantic_sha256
t15_interface_row_artifact_id
parent_t13_class_artifact_id
target_t13_class_artifact_id
parent_final_global_weight
target_final_global_weight
```

Reject missing, duplicate, reordered or independently supplied edges. Strict T15 rows need no rank edge.

### 10.2 Exact rank domain

A nonempty edge bank requires one open/proved domain of kind:

```text
nonnegative-integer
lexicographic-nonnegative-integers
```

The lexicographic domain uses a fixed finite coordinate count and nonnegative integer coordinates. A
proved domain requires one:

```text
rank-domain-well-foundedness-proof
```

with statement, locator, digest and evidence. A finite state table alone is not the external
well-foundedness proof.

If the T15 critical bank is empty, T16 is vacuous and requires no artificial domain.

### 10.3 Exact state-rank bank

The state census is the sorted union of all critical-edge endpoints. Every record binds its exact T13
class artifact and the single rank domain.

Open records have null rank and verification fields. A proved state requires one:

```text
global-state-rank-proof
```

supported by the domain artifact and its exact T13 class artifact.

### 10.4 Exact edgewise descent

Every edge is open or proved. A proved edge must satisfy:

```text
rank(target) < rank(parent)
```

and requires one:

```text
critical-edge-rank-descent-proof
```

supported by the exact T15 row artifact and both endpoint rank artifacts.

### 10.5 Complete graph audit

When all T16 work is proved, reconstruct the complete critical graph and require:

1. exact T15-derived edge coverage;
2. no self-edge;
3. strict rank descent on every edge;
4. no directed cycle;
5. a deterministic topological order; and
6. the exact longest critical path.

Strict descent forces every critical strongly connected component to be a singleton. The finite audit is
not a substitute for proving that the rank has its claimed recurrence meaning.

### 10.6 Typed sealing

The aggregate bank commits to the independent T15 proof-bank digest, the domain/state/edge records and
artifacts, and the graph audit. It synchronizes:

```text
GLOBAL_RANK_WELL_FOUNDED
T16_GLOBAL_RANK
```

through `rank-well-foundedness-proof` artifacts with exact T15 obligation support.

## 11. T17: exact global-state predicates

The older `check_prime_power_global_quotient_semantic_refinement.py` reads a separately assembled global
family and opaque predicate locators. Do not use it as the final T17 endpoint.

The new T17 checker should:

1. derive the complete state census from exact T13 classes;
2. bind every predicate to the exact T13 class core and member bank;
3. require agreement across every local representative;
4. bind rank-sensitive predicates to the exact T16 state-rank record and artifact;
5. use open/proved state-predicate records;
6. require one `global-state-predicate-proof` artifact per proved state; and
7. publish one noncircular aggregate predicate bank.

For each state, record at least:

```text
global_state_id
global_state_record_sha256
t13_class_artifact_id
predicate_id
predicate_statement
representative_agreement_statement
support_state_claim_ids
status
verification_locator
verification_digest
evidence
```

The predicate theorem remains external mathematics even after exact documentary sealing.

## 12. T18: exact final row theorems

T18 must derive its row census from the exact selected recurrent and interface surfaces rather than an
older global quotient package.

The row bank should include:

- every exact T11 recurrent row after T12 elimination;
- every exact T15 interface/return/off-diagonal row;
- exact T16 rank data for every critical interface target; and
- exact T17 parent/target predicate records.

Every row theorem must bind the relevant T05, T07, T10, T11, T12, T14, T15, T16 and T17 artifacts. It
must reconstruct the parent predicate, target predicate multiset, fixed offset, multiplicities, weight
margin, strict/critical classification and rank descent where applicable.

Use open/proved row-theorem records and one:

```text
global-row-theorem-proof
```

per proved row. The aggregate bank must bind `T18_ROW_THEOREMS` without importing a parallel global
family or treating an opaque theorem digest as proof.

## 13. T19--T21: global family and exceptional chambers

Prove the skeleton-derived global family exhaustive and close the exact worklist

\[
232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.
\]

Every chamber needs one reviewed disposition. Keep fixed-response correction `17`, rollback distance
`12` and uniform correction `44` distinct.

## 14. T22--T43: typed support and final handoff

Complete every genuine semantic-obligation artifact, the ten final premises, six handoff assertions and
the seven-gate dossier audit. Then prove the ordinary implication from the reviewed quotient and
handoff to `D(n)=2n`.

Do not place a target's own completion digest inside an ancestor used to seal that target.

## 15. Immediate execution order

1. Populate and prove high-use T01 source statements.
2. Close T01 and every T02 rule record; prove recurrence exhaustiveness.
3. Enter actual T03/T04 data.
4. Prove T05 arbitrary-`n` coverage and every T07/T06 theorem.
5. Prove T08/T09/T10 simultaneous resource and credit semantics.
6. Prove every T11 block and T12 auxiliary expansion.
7. Populate and prove every T13 identity and T14 scale equation.
8. Populate and prove every T15 multiplier, row theorem and exit disposition.
9. Populate and prove every T16 domain, state rank and critical-edge theorem.
10. Implement exact T17 predicates from T13/T16.
11. Implement exact T18 row theorems from T11/T12/T15/T16/T17 and all semantic ancestors.
12. Prove T19 global-family exhaustiveness and all 252 chamber dispositions.
13. Complete T22--T43 and review the final implication.
