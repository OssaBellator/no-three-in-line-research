# Exact recurrent raw-lineage bridge progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

The classical no-three-in-line conjecture remains open. This addendum records schema and source-completeness results only.

## ERL1p — installed promotion-gap theorem

For first host `s4-75b04c45c1c8eac2`, the side-four projection has nine response-eligible edges and excludes target `01`. Its exact response family is

```text
3012:1
3210:4.
```

The installed raw-lineage validator instead requires target membership in `host_edges` and enumerates responses from all host edges.

```text
direct projected-edge copy -> rejected: target in host
add target 01              -> response family expands to 1032,1230,3012,3210
reuse projected count 2    -> rejected: response linkage.
```

The new responses have intrinsic energies

```text
1032:0
1230:1.
```

Thus direct field-copy promotion is invalid. The installed schema conflates physical lineage membership with response eligibility.

The same validator bounds host edges but checks background points only for uniqueness. With target added and response count four, it accepts an empty background and all four exterior strict-reversal backgrounds. This is schema acceptance only, not physical realization.

Artifacts:

```text
scripts/check_exact_recurrent_first_host_raw_lineage_promotion_gap.py
data/exact_recurrent_first_host_raw_lineage_promotion_gap.json
docs/exact-recurrent-first-host-raw-lineage-promotion-gap.md
.github/workflows/exact-recurrent-first-host-raw-lineage-promotion-gap.yml
```

## ERL1q — minimal dual-edge bridge

The corrected bridge separates

```text
lineage_host_edges: 10, including target 01
response_edges:      9, excluding target 01.
```

It enforces `response_edges` as a subset of the lineage host and reconstructs exactly

```text
3012:1
3210:4.
```

Using the lineage edges as response edges would still produce the incorrect four-response family `1032,1230,3012,3210`.

The bridge is expressive for both an empty-background schema completion and the strict-reversal completion `{(-3,5),(5,-3)}`. Their identifiers are distinct, while their response family remains identical.

Each record is missing exactly sixteen physical fields:

```text
coordinate_domain.physical_embedding_ref
physical_source_ref
deletion_causes.02
deletion_causes.20
provenance.owner
provenance.fate
provenance.collision
provenance.line
provenance.interface
provenance.crt
legal_operations
intermediate_states
child_row
positive_weights
parent_budget
realization_status
```

Artifacts:

```text
scripts/check_exact_recurrent_first_host_dual_edge_bridge.py
data/exact_recurrent_first_host_dual_edge_bridge.json
docs/exact-recurrent-first-host-dual-edge-bridge.md
.github/workflows/exact-recurrent-first-host-dual-edge-bridge.yml
```

## Current exact boundary

The target/response-edge convention now has an executable repair. The remaining proof dependency is a source-backed batch of every physical `{02,20}` occurrence using that convention and filling all sixteen fields.

No current artifact establishes:

```text
physical occurrence count
physical coordinate domain
physical exclusion of the four strict backgrounds
legal transition closure
exact recurrent child rows
strict Lyapunov slack
global termination
all-side transfer.
```

All corresponding flags, including `all_n_proved_by_checker`, remain zero.
