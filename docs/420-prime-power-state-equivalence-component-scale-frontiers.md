# Prime-power state-equivalence and component-scale frontiers

This chapter records CMR2550--CMR2565. It makes

```text
T13_STATE_EQUIVALENCE
CROSS_BLOCK_STATE_IDENTITY_SEMANTIC
T14_COMPONENT_SCALES
COMPONENT_SCALE_SEMANTIC
```

exact documentary proof surfaces over the already fixed T04, T07 and T11 banks.

The canonical executable endpoints are:

```text
scripts/check_prime_power_state_equivalence_frontier.py
scripts/check_prime_power_component_scale_frontier.py
```

Both checkers permanently report:

```text
all_n_proved_by_checker = 0
```

## CMR2550: parallel cross-block population defect

The older cross-block identification checker accepts a list of independently supplied denominator-cleared
integer blocks and one opaque evidence string for every local-to-global link. The older spanning-evidence
checker then accepts source locators and statement digests without binding those edges to the exact T07
state-claim bank.

Those modules remain useful finite consistency audits, but using them directly for T13 would permit a
second block and state population parallel to the exact T04/T07 frontier.

T13 therefore derives its block census and local-state census before reading any global-state links.

## CMR2551: exact T04 local-state census

Every T04 unit of kind `recurrent-block` contributes its literal `population_data.local_states` list.
For each local state the checker reconstructs:

```text
block_id
unit_id
local_state_id
role
stratum
owner
t04_local_state_value_sha256
local_state_subject_sha256
```

The state list of each block must be nonempty, canonically ordered by local state ID and duplicate-free.
Every local state receives exactly one local-to-global link. Missing links, duplicate links and links to
states outside the exact T04 census are rejected.

The checker does not import the older integer-block family to define the T13 population.

## CMR2552: exact T07-supported local identity claims

For every recurrent block, the checker derives the exact set of operation slots appearing in its T04
parent bindings. It then reconstructs the union of the T07 state claims belonging to those slots.

Every local-to-global link contains:

```text
block_id
unit_id
local_state_id
local_state_subject_sha256
global_state_id
support_state_claim_ids
identity_statement
evidence
```

The support list must be nonempty, sorted, duplicate-free and contained in the exact T07 state-claim bank
of that block. A link cannot cite an unrelated slot or a state claim from another block.

This establishes exact documentary ancestry. It does not prove that the identity statement follows from
the cited T07 claims.

## CMR2553: canonical global-state classes

The global classes are derived from the complete link bank. For every class the checker publishes:

```text
global_state_id
role
stratum
owner
members
member_count
member_blocks
global_state_record_sha256
```

All class members must have the same semantic core `(role, stratum, owner)`. At most one local state from
each block may appear in one global class; distinct local quotient coordinates inside one block cannot be
collapsed merely by assigning the same global name.

Singleton classes remain explicit. They also require proof review because the supplied partition asserts
that no further cross-block identification is needed for that local state.

## CMR2554: exact spanning proof tree per class

Every derived global class receives one open/proved status record. A proved class uses:

```text
state-equivalence-class-registry://<global state ID>
```

A class with `n` members must contain exactly `n-1` pairwise equivalence edges. Every edge binds its two
member links and therefore the exact T07 state claims supporting both endpoints.

The checker rejects:

- self-edges;
- repeated unordered member pairs;
- endpoints outside the class;
- two endpoints from the same block; and
- disconnected evidence graphs.

The lexicographically first member is the canonical root. The unique root-to-member path is published for
every member, giving an exact finite decomposition of the asserted transitive identification.

For a singleton class the canonical tree has zero edges and one length-zero root path.

## CMR2555: typed per-class T13 artifacts

Every proved class requires one internal artifact of kind:

```text
global-state-equivalence-class-proof
```

Its exact support is every T07 semantic artifact belonging to a slot used by any member block. The
per-class verification digest seals:

1. the class status-record core;
2. the derived global-state record;
3. the canonical spanning tree;
4. the typed artifact; and
5. the complete T07 semantic-artifact support bank.

The status-record core excludes the verification digest itself, avoiding a hash fixed point.

## CMR2556: T13 aggregate synchronization

The aggregate T13 proof bank commits to:

- the exact T04 recurrent-block census and payloads;
- the independent T07 state-semantics proof bank;
- every local-state subject;
- every local-to-global link;
- every derived global class;
- every open/proved class record;
- every pairwise edge and spanning tree;
- every typed class artifact; and
- every per-class proof bundle.

When `CROSS_BLOCK_STATE_IDENTITY_SEMANTIC` closes, its unique artifact must have kind
`state-equivalence-proof`, locator

```text
state-equivalence-frontier://CROSS_BLOCK_STATE_IDENTITY_SEMANTIC
```

and the reconstructed aggregate digest. Its immediate support is exactly the two T07 obligation
artifacts.

The T13 target artifact has kind `state-equivalence-proof`, locator

```text
state-equivalence-frontier://T13_STATE_EQUIVALENCE
```

and the same proof-bank digest. Obligation closure, effective target completion and reconstructed T13
readiness must agree exactly.

## CMR2557: T13 honesty boundary and endpoint

Passing T13 proves exact T04 local-state coverage, exact T07 claim ancestry, one link per local state,
semantic-core consistency, one canonical proof tree per class and noncircular artifact synchronization.

It does not prove that:

- any local-to-global identity statement is true;
- the cited T07 claims are true or sufficient;
- the supplied partition is the genuine mathematical state quotient;
- unlinked local states are genuinely distinct;
- the equivalence relation has its intended external meaning; or
- the quotient implies `D(n)=2n`.

Run:

```bash
python scripts/check_prime_power_state_equivalence_frontier.py certificate.json
```

## CMR2558: exact shared T11/T13 root

The older cross-block weight-synchronization checker scales the independently supplied integer-block
family embedded in the older identification certificate. T14 instead takes the exact T11 recurrent-block
closure certificate and the exact T13 state-equivalence certificate as separate inputs.

The checker requires the T07 certificate nested under T11 to equal the T07 root used by T13. The set of
blocks occurring in the T13 local-state census must equal the set of T11 common-weight blocks, and every
T13 local state must have one exact T11 primitive weight.

This prevents a scale proof over a different block family or different state partition.

## CMR2559: canonical component graph and scale equations

Two T11 blocks are adjacent exactly when a T13 global class contains one local member from each block.
The checker derives all connected components of this block-overlap graph, including isolated one-block
components.

For every shared global class, the lexicographically first member is compared with every other member.
If local weights are `w_b(s)` and `w_c(t)`, the exact scale equation is

\[
\alpha_b w_b(s)=\alpha_c w_c(t).
\]

Every equation record publishes both local weights, both block multipliers, both scaled weights and the
T13 global-state digest.

## CMR2560: exact rational propagation and cycle consistency

Inside each connected component, the lexicographically first block receives rational scale `1`. Every
shared-state equation propagates an exact `Fraction` scale to neighbouring blocks.

If a block is reached by two paths, both paths must give the same rational scale. Any inconsistent cycle
is rejected. The propagation must reach every block in the derived component.

The ratio graph is not supplied independently; it is reconstructed from exact T13 class membership and
exact T11 local weights.

## CMR2561: primitive componentwise integer multipliers

For one connected component, the checker takes the least common multiple of all propagated denominators,
converts every rational scale to a positive integer multiplier and divides the common gcd.

The resulting multiplier vector is therefore the canonical primitive positive integer solution within
that connected component. An isolated block receives multiplier `1`.

Distinct connected components remain independently normalized. T14 does not invent a relative multiplier
between components that share no state.

## CMR2562: global component weights and strict-margin scaling

Every T13 global state receives one exact component weight:

\[
W_g=m_b w_b(s),
\]

which must agree across all of its local members. The checker publishes the role, stratum, owner, member
count and exact component weight for every global class.

For each T11 block it also scales the positive minimum recurrent margin by the component multiplier. The
scaled margin must remain strictly positive.

These are exact integer consequences of the supplied T11 weights and T13 classes. They do not choose a
global scale across disconnected components.

## CMR2563: equation semantics and typed component artifacts

Every proved component requires one semantic certificate containing:

```text
component_id
scale_component_arithmetic_sha256
component_t13_class_artifact_ids
component_t11_common_weight_artifact_ids
component_t11_block_closure_artifact_ids
equation_semantics
normalization_statement
evidence
```

Each shared-state equation receives one statement and evidence record supported by:

1. the exact T13 class artifact; and
2. the exact T11 common-weight artifacts of the two endpoint blocks.

The component certificate additionally cites every T13 class artifact and every T11 common-weight and
closure artifact belonging to the complete component.

Every proved component requires one internal artifact of kind:

```text
component-scale-synchronization-proof
```

The per-component verification digest seals the status-record core, arithmetic record, semantic
certificate, typed artifact and all T11/T13 support banks.

## CMR2564: T14 aggregate synchronization

The aggregate T14 bank commits to:

- the exact T11 recurrent-block closure proof bank;
- the exact T13 state-equivalence proof bank;
- every component arithmetic record;
- every global component weight;
- every open/proved component record;
- every component semantic certificate;
- every typed component artifact; and
- every per-component proof bundle.

When `COMPONENT_SCALE_SEMANTIC` closes, its unique artifact must have kind `component-scale-proof`,
locator

```text
component-scale-frontier://COMPONENT_SCALE_SEMANTIC
```

and the reconstructed aggregate digest. Its support is exactly the T13 state-equivalence obligation
artifact and the two T11 recurrent-block obligation artifacts.

The T14 target artifact has kind `component-scale-proof`, locator

```text
component-scale-frontier://T14_COMPONENT_SCALES
```

and the same proof-bank digest. T11 readiness, T13 readiness, obligation closure, effective target
completion and reconstructed T14 readiness must agree.

## CMR2565: T14 honesty boundary and endpoint

Passing T14 proves exact T11/T13 root identity, exact scale-equation reconstruction, rational cycle
consistency, primitive componentwise integer multipliers, exact global component weights, positive scaled
block margins and noncircular artifact synchronization.

It does not prove that:

- the T13 global-state identifications are mathematically true;
- the T11 local weights represent the intended recurrence potential;
- the scale equations have the intended external meaning;
- disconnected components have any particular relative scale;
- the return/interface row family is complete;
- the global rank is well founded; or
- the final quotient implies `D(n)=2n`.

Run:

```bash
python scripts/check_prime_power_component_scale_frontier.py certificate.json
```

The next exact front is T15 interface-row exhaustiveness, which must derive the complete nonrecurrent row
bank from T04 and use T14 component weights to choose or constrain relative component scales without
silently identifying disconnected components.
