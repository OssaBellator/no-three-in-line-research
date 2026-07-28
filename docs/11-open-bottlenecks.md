# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2573**, the branch contains exact
noncircular documentary work banks from T01 through T15, typed proof registries for all 43 atomic
targets, an exact 252-chamber exceptional worklist and a final dossier audit.

The branch still lacks the genuine source statements, exhaustive recurrence theorem, actual complete
population, arbitrary-`n` coverage, truth of the semantic claims, a genuine rank theorem, complete
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

Every proved row must bind:

- its exact T04 payload and the separate target/route/transition/source-clause digests;
- its exact slot's T07 state and transition claims;
- exact T13 parent and target classes;
- exact T14 component and final weights;
- one integer fixed offset and positive target multiplicities; and
- row statements and evidence.

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

When later T12 population introduces new exit subjects, affected T15 verification bundles must be
regenerated.

### 9.5 Typed sealing

Every proved row requires one `interface-row-semantic-proof` with exact T04/T07/T12/T13/T14 and
interface-scale support. Bind the aggregate bank through:

```text
INTERFACE_RETURN_ROWS_EXHAUSTIVE
T15_INTERFACE_EXHAUSTIVENESS
```

with `interface-exhaustiveness-proof` artifacts and noncircular digests.

## 10. T16: prove genuine global-rank well-foundedness

T16 is the next executable frontier. It must consume T15 rather than accept an independent rank table.

### 10.1 Derived critical-edge census

Take every T15 semantic row classified `critical-unranked`. For every positive target multiplicity,
derive one exact critical edge containing:

```text
row_id
parent_global_state_id
target_global_state_id
interface_row_semantic_certificate_sha256
interface_target_semantic_sha256
```

Reject missing, duplicate, reordered or independently supplied critical edges.

Strict T15 rows need no rank edge because their weight margin is already positive.

### 10.2 Exact rank domain

Give every global state occurring in a critical edge one exact rank value and theorem. The rank domain
must be explicitly well founded—for example a nonnegative integer or a proved lexicographic product of
well-founded domains. A finite list alone is not the external well-foundedness proof.

### 10.3 Edgewise descent

For every derived critical edge prove:

```text
rank(target) < rank(parent)
```

Bind the proof to the exact T15 row artifact, exact T13 parent/target classes and all semantic evidence
needed to interpret the edge.

### 10.4 Graph audit

Reconstruct the critical support graph and require:

1. every edge has strict rank descent;
2. no self-edge;
3. no directed cycle;
4. every critical target is in the declared rank domain; and
5. the rank theorem applies under the genuine recurrence semantics.

The graph acyclicity check is a finite consistency audit, not a substitute for the external rank theorem.

### 10.5 Typed proof bank

Every proved rank subject should receive a typed artifact such as:

```text
global-rank-state-proof
critical-edge-rank-descent-proof
```

The aggregate bank must synchronize:

```text
GLOBAL_RANK_WELL_FOUNDED
T16_GLOBAL_RANK
```

through `rank-well-foundedness-proof` artifacts with exact T15 support.

## 11. T17 and T18: predicates and final rows

Give every T13 global class one exact predicate theorem and prove agreement across all representatives
and scaled occurrences. Bind every final row and fixed offset to the exact T05, T07, T10, T11, T12,
T14, T15, T16 and T17 banks, then prove its external recurrence interpretation.

## 12. T19--T21: global family and exceptional chambers

Prove the skeleton-derived global family exhaustive and close the exact worklist

\[
232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.
\]

Every chamber needs one reviewed disposition. Keep fixed-response correction `17`, rollback distance
`12` and uniform correction `44` distinct.

## 13. T22--T43: typed support and final handoff

Complete every genuine semantic-obligation artifact, the ten final premises, six handoff assertions and
the seven-gate dossier audit. Then prove the ordinary implication from the reviewed quotient and
handoff to `D(n)=2n`.

Do not place a target's own completion digest inside an ancestor used to seal that target.

## 14. Immediate execution order

1. Populate and prove high-use T01 source statements.
2. Close T01 and every T02 rule record; prove recurrence exhaustiveness.
3. Enter actual T03/T04 data.
4. Prove T05 arbitrary-`n` coverage and every T07/T06 theorem.
5. Prove T08/T09/T10 simultaneous resource and credit semantics.
6. Prove every T11 block and T12 auxiliary expansion.
7. Populate and prove every T13 identity and T14 scale equation.
8. Populate and prove every T15 multiplier, row theorem and exit disposition.
9. Implement T16 from the exact T15 critical-edge census and prove genuine rank descent.
10. Prove T17 predicates and T18 final rows.
11. Prove T19 global-family exhaustiveness and all 252 chamber dispositions.
12. Complete T22--T43 and review the final implication.
