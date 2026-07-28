# Prime-power block and interface population frontier

This chapter records CMR2478--CMR2485. It makes the second population target,
`T04_BLOCK_INTERFACE_POPULATION`, an exact documentary work surface.

The checker is:

```text
scripts/check_prime_power_block_interface_population_frontier.py
```

It composes the exact T03 slot/candidate population bank with the recurrence-skeleton family
manifest and the sealed atomic-target artifact registry. It does **not** import the later integer
recurrent-block, component-scale or interface-inequality certificates. Those surfaces already depend
on geometry, policy, credit, block closure, auxiliary elimination and rank semantics; using them as
the definition of T04 population would create a dependency cycle.

The result remains documentary. It identifies and seals the exact block/interface population data
required before those later semantic proofs can begin.

## CMR2478: skeleton-derived population-unit bank

The checker reconstructs the expected T04 worklist directly from the recurrence skeleton and the
exact T02 global-parent applications.

- Every distinct `expected_block_id` occurring on a recurrent parent clause produces one
  `recurrent-block` population unit.
- Every nonrecurrent skeleton clause produces one `interface-row` population unit for its exact
  return, interface or off-diagonal row ID.

The canonical unit IDs are:

```text
block::<expected block ID>
interface::<expected interface-row ID>
```

Each unit contains the exact parent bindings determined by T02:

```text
parent_global_state_id
row_kind
source_case_id
source_clause_id
operation_slot_id
```

Thus neither the block census nor the interface-row census is copied from the later supplied quotient
certificates.

## CMR2479: open, populated and proved states

Every expected T04 unit has exactly one status.

- `open`: no assembly payload and no proof artifact;
- `populated`: one literal assembly payload, but no proof artifact;
- `proved`: one literal assembly payload and one sealed unit-specific population artifact.

A populated record uses

```text
block-interface-population-data://<unit ID>
```

and binds its exact data bundle. A proved record uses

```text
block-interface-population-registry://<unit ID>
```

and binds the unit identity, literal payload, proof artifact and exact T03 support.

This separation allows block and interface assembly research to proceed once the relevant T03 data
exist, without claiming that the assembly has been proved.

## CMR2480: exact T03 source-slot binding

Every non-open unit cites the exact T03 source slots reconstructed from its parent bindings. For each
parent the checker records:

```text
parent_global_state_id
operation_slot_id
slot_population_payload_sha256
fibre_id
source_sha256
```

All five values are taken from the exact T03 payload bank. A T04 payload is rejected if a required T03
slot is still open or if any fibre, source digest or payload digest differs.

This prevents a recurrent block or interface row from being populated using a parallel candidate
family unrelated to the one sealed at T03.

## CMR2481: literal block and interface assembly payloads

A recurrent-block payload has the exact ordered fields:

```text
local_states
recurrent_rows
return_routes
interface_attachments
source_clause_bindings
```

The recurrent-row and source-clause-binding lists must be nonempty.

An interface-row payload has the exact ordered fields:

```text
target_states
route_data
transition_data
source_clause_binding
```

All fields contain canonical JSON data and the complete payload is hashed. This layer intentionally
does not impose the later weight, margin, strong-connectivity, rank or semantic conditions; those
belong to T05 onward.

## CMR2482: exact T03 artifact support and unit sealing

A proved recurrent block requires one artifact of kind

```text
recurrent-block-population-proof
```

and a proved interface row requires one artifact of kind

```text
interface-row-population-proof
```

The support list is reconstructed as the complete unique T03 slot-population artifact set used by the
unit's parent bindings. A unit cannot be proved while one of its source T03 slots is merely populated.
Omitted, unrelated, duplicate and self support are rejected.

Each proved record's digest equals the reconstructed proof-bundle digest containing the exact unit
identity, payload digest, artifact digest and T03 artifact support.

## CMR2483: noncircular global population bank

The aggregate T04 bank binds:

- the expected operation-slot registry;
- the exact T02 record and artifact banks;
- the exact T03 record, payload, artifact and per-slot bundle banks;
- the recurrence-skeleton digest;
- the skeleton-derived T04 unit bank;
- every T04 status record, payload, artifact and per-unit bundle.

The aggregate digest deliberately excludes the current-frontier certificate, atomic completion
records and atomic-target artifact-registry certificate. Including those hashes would be circular:
the T04 target artifact contains the aggregate proof digest, while its target bundle determines the
atomic T04 completion digest contained by the current-frontier certificate.

The checker may publish those ancestor certificate hashes as diagnostic claims, but they are not
members of the sealed global bank.

## CMR2484: exact T04 target binding and synchronization

T04 readiness requires:

1. T03 slot/candidate population is ready;
2. every skeleton-derived T04 unit is proved;
3. every unit has exactly one artifact with exact T03 support; and
4. the T04 atomic target artifact binds the reconstructed global bank.

The target artifact must have kind `global-population-bank`, locator

```text
block-interface-population-registry://T04_BLOCK_INTERFACE_POPULATION
```

and proof digest equal to the noncircular aggregate T04 bank digest.

The checker requires exact equality between reconstructed readiness and effective completion of
`T04_BLOCK_INTERFACE_POPULATION`. T04 has no separate semantic obligation in the fixed nineteen-
obligation DAG, so the atomic target artifact is the unique aggregate proof binding for this layer.

## CMR2485: honesty boundary and executable endpoint

Passing the checker establishes exact worklist derivation, literal data identity, T03 ancestry,
artifact support and digest binding. It does not prove that:

- the T03 population is genuine or correct;
- the supplied local states, rows, routes or transitions have their intended meaning;
- recurrent blocks are closed, strongly connected or strict;
- return and interface rows are exhaustive or satisfy a valid global rank;
- any exceptional chamber closes; or
- the global quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_block_interface_population_frontier.py certificate.json
```

The next mathematical frontiers remain real geometry and selector correctness, fate/transition/state
semantics, candidate-policy correctness, active-row/resource/credit semantics, genuine recurrent-
block closure, cross-block semantics and interface/rank proof.