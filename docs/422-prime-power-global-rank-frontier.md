# Prime-power global-rank well-foundedness frontier

This chapter records CMR2574--CMR2581. It makes

```text
GLOBAL_RANK_WELL_FOUNDED
T16_GLOBAL_RANK
```

an exact documentary proof surface over the fixed T15 interface-row bank.

The executable endpoint is:

```text
scripts/check_prime_power_global_rank_frontier.py
```

It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2574: independently supplied rank defect

The older interface and support-condensation checkers accept a separate state-rank table and then verify
finite integer descent. That permits a valid-looking rank certificate whose state universe or support
edges differ from the exact T15 interface family.

T16 removes that freedom. Every critical edge is derived before any rank value, rank theorem or proof
artifact is read.

## CMR2575: exact T15-derived critical-edge census

Every T15 semantic row classified `critical-unranked` contributes one critical-edge subject for every
positive target multiplicity. The subject binds:

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

Subjects are canonically ordered and receive digest-derived IDs. Missing, duplicate, reordered or
independently supplied critical edges are rejected. Strict T15 rows contribute no rank edge because their
row decrease is already certified by positive weight margin.

## CMR2576: explicit well-founded rank domain

If the derived critical-edge bank is nonempty, T16 requires one open/proved rank-domain record. The
supported exact domains are:

```text
nonnegative-integer
lexicographic-nonnegative-integers
```

The lexicographic domain has one fixed finite coordinate count, at least two. Every coordinate is a
nonnegative integer.

A proved domain uses:

```text
global-rank-domain-registry://<rank domain ID>
```

and requires one internal artifact of kind:

```text
rank-domain-well-foundedness-proof
```

with a well-foundedness statement, proof locator, digest and evidence. The finite rank table by itself is
not accepted as the external well-foundedness theorem.

When T15 contains no critical row, T16 treats rank closure as genuinely vacuous and requires no artificial
domain or state table.

## CMR2577: exact critical-state rank bank

The rank-state census is the sorted union of all derived critical-edge endpoints. Every state record binds
its exact T13 class artifact and the single rank domain.

A state is `open` or `proved`. An open state has null rank and verification fields. A proved state has one
canonical rank value, locator

```text
global-rank-state-registry://<global state ID>
```

and one artifact of kind:

```text
global-state-rank-proof
```

supported by the rank-domain artifact and the state's exact T13 class artifact. The verification digest
seals the record core and artifact.

## CMR2578: exact edgewise descent proofs

Every derived edge is `open` or `proved`. A proved edge requires proved endpoint ranks and verifies

```text
rank(target) < rank(parent)
```

using ordinary integer order or the fixed lexicographic tuple order.

The edge semantic certificate binds the exact T15 row and target records, the exact endpoint rank records,
the two rank values, a descent statement and evidence. One artifact of kind

```text
critical-edge-rank-descent-proof
```

must cite the exact T15 row artifact and the two endpoint rank artifacts. The edge verification digest
seals the edge record, descent certificate and proof artifact.

## CMR2579: complete critical-graph audit

When all T16 work is proved, the checker reconstructs the complete directed critical graph. It rejects a
directed cycle, publishes one deterministic topological order, computes the exact longest critical path
and records the canonical singleton strongly connected components forced by strict rank descent.

The graph audit is not performed over a supplied support graph. It uses only the T15-derived edge bank.
The finite acyclicity calculation is a consequence of supplied rank statements; it is not a substitute for
the external semantic theorem that the chosen rank measures recurrence progress.

## CMR2580: typed noncircular sealing and synchronization

The aggregate T16 proof bank commits to:

- the independent T15 interface-exhaustiveness proof-bank digest;
- the derived critical-edge subjects;
- the rank-domain record, artifact and proof bundle;
- every state-rank record, artifact and proof bundle;
- every edge record, descent certificate, artifact and proof bundle;
- the topological order, longest critical path and component audit.

It excludes certificates containing T16's own completion digest.

When ready, the semantic obligation uses one `rank-well-foundedness-proof` artifact at:

```text
global-rank-frontier://GLOBAL_RANK_WELL_FOUNDED
```

with exact support from the T15 obligation artifact. The atomic target uses the same kind and the locator:

```text
global-rank-frontier://T16_GLOBAL_RANK
```

Both bind the aggregate T16 proof-bank digest.

## CMR2581: honesty boundary and executable endpoint

Passing the checker establishes exact critical-edge derivation, rank-domain identity, endpoint coverage,
strict rank comparison, graph acyclicity, longest-path arithmetic, typed support and readiness
synchronization relative to supplied certificates.

It does not prove that:

- the T15 interface rows are genuinely exhaustive;
- the stated rank domain theorem has been proved correctly;
- a state rank has its intended recurrence meaning;
- a critical edge represents a genuine recurrence transition;
- strict weight rows and critical rank rows form the complete global family;
- the state predicates or final row theorems are true;
- all exceptional chambers close; or
- the quotient implies `D(n)=2n` for every `n`.

The next exact fronts are T17 global-state predicates and T18 final row theorems. They must bind every
predicate and theorem to the exact T13 state quotient, T15 rows and T16 rank records rather than reuse the
older independently supplied global quotient package.
