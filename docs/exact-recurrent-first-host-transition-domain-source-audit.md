# First-host transition-domain source audit

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact source audit for the four symbolic restoration states and their eight directed single-bit edges. It does not prove that any state or edge is physically realized.

## Symbolic state domain

The restoration bits are `r02,r20`:

```text
00  blocked       deleted 02,20  selected 3012
01  restore 20    deleted 02     selected 3201
10  restore 02    deleted 20     selected 2031
11  restore both  deleted none   selected 2031
```

These are exact local response-menu states. They are not physical occurrence records.

The directed symbolic edge set is

```text
00->01  restore 20
01->00  delete 20
00->10  restore 02
10->00  delete 02
01->11  restore 02
11->01  delete 02
10->11  restore 20
11->10  delete 20.
```

All eight edges are candidates only.

## Installed operation registry boundary

The installed registry contains 1,166 declared operation kinds with payment and continuation classes. Its own honesty endpoint limits exhaustiveness to that declared kind bank. It is not an occurrence-level table saying which kind acts on this host, which cell changes, or which source and target states are legal.

Therefore

```text
installed operation kinds              1166
first-host operation-kind mappings         0
first-host legality proofs                 0.
```

A registered kind cannot be attached to an edge by name similarity alone.

## Fixture restoration is not edge promotion

Five upstream interfaces were audited:

```text
installed operation-kind registry
protected-interface execution
 target-anchor lineage
inherited-coordinate diagonal blocks
owner/fate lineage and line kernels.
```

The protected-interface execution checker is a side-five fixture and factorization audit. The target-anchor checker includes 4,608 restoration subsets, but those are side-three anchor fixtures followed by bulk redeletion and private normalization. They do not identify cells `02` and `20` in host `s4-75b04c45c1c8eac2` or provide an operation trace for one of the eight edges.

The inherited-coordinate theorem supplies an owner-DAG and exact quotient interface while explicitly leaving same-owner diagonal-block subcriticality and the actual global parent rule open. The owner/fate lineage theorem supplies lossless row-key contracts while recurrent rows and raw-fibre provenance coverage remain incomplete.

None of the five interfaces contains a first-host state record or directed edge record.

## Exact source census

Joining physical-source coverage, closure-route coverage and route-cover admission gives

```text
symbolic menu states                       4
physical menu states                       0
symbolic directed edges                    8
physical directed edges                    0
exact edge owner tokens                    0
exact edge operation traces                0
source-reduced edge domain                 0
route-closed edges                         0
complete scalar covers                     0.
```

Thus the route-cover admission classification cannot yet be applied to a physical edge mask.

## Edge promotion contract

Promoting one symbolic edge requires twelve source-backed fields:

```text
physical_occurrence_id
persistent_owner_token
source_state_ref
target_state_ref
operation_kind
operation_registry_entry_ref
operation_trace_ref
changed_cell
action
legality_proof_ref
intermediate_state_refs
realization_status.
```

Both endpoints must first be physical state records for the same occurrence and owner lineage. The changed cell and restore/delete action must agree with the endpoint bit change.

Any edge incident to state `11` has an additional prerequisite: the restore-both state itself must be source-realized. Local enumeration of response `2301` does not establish that prerequisite.

## Consequence

The current source does not prove that the legal domain is the full square, a proper subgraph, or empty. Therefore none of the following may be inferred:

```text
individual restoration is legal
individual deletion is legal
simultaneous restoration is reachable
reverse transitions preserve owner identity
one scalar-compatible route cover is physically relevant.
```

The next source-facing task is to emit exact state and edge records from the construction trace, or prove source-backed exclusions. Once a physical edge mask exists, the route-cover admission checker decides whether its route-closed subset contains a scalar-compatible cover.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_transition_domain_source_audit.py \
  --check data/exact_recurrent_first_host_transition_domain_source_audit.json
```

The checker pins the five upstream source boundaries, joins the three first-host source gates, reconstructs all four states and eight edges, verifies the twelve-field promotion contract and rejects fifteen deliberate corruptions.

Physical occurrence coverage, transition legality, persistent owner identity, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
