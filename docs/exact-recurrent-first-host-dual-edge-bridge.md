# First-host dual-edge raw-lineage bridge

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact schema bridge. It resolves the target/response-edge convention but does not populate a physical fibre.

## Why two edge sets are required

The first side-four residual host needs target `01` retained in its physical lineage record, but target `01` must not be eligible for response matching.

The bridge therefore stores

```text
lineage_host_edges: 10 edges, including target 01
response_edges:      9 edges, excluding target 01.
```

The response edges are required to be a subset of the lineage host edges.

Enumerating perfect matchings on `response_edges` gives exactly

```text
3012: intrinsic triples 1
3210: intrinsic triples 4.
```

Enumerating on all lineage host edges instead would incorrectly give

```text
1032, 1230, 3012, 3210.
```

Thus the bridge reconciles the target convention without changing the projected blocker response family.

## Background-sensitive identifiers

The bridge identifier includes both edge sets, the coordinate-domain declaration, background, source reference, deletion causes, and provenance labels.

It distinguishes an empty-background schema completion from the strict-reversal completion

```text
{(-3,5),(5,-3)}.
```

Both retain the same response family `3012,3210`, because response eligibility is independent of the background field.

## Fixed physical completeness worklist

Each schema completion is still missing exactly sixteen required physical fields:

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

A record is not physically complete merely because it satisfies the dual-edge structural schema.

## Consequence

The target-convention ambiguity now has a precise repair. The remaining obstruction is data, not response-host syntax: every actual occurrence must supply the sixteen physical fields from a source-backed construction trace.

The two included records are schema completions only. Neither the empty background nor the strict background is asserted to occur physically.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_dual_edge_bridge.py \
  --check data/exact_recurrent_first_host_dual_edge_bridge.json
```

The checker validates both edge sets, reconstructs the two-response and four-response families, verifies background-sensitive identifiers, audits the sixteen-field worklist, and rejects ten deliberate corruptions.

Physical realization, physical exclusion, legal operations, recurrent child rows, strict Lyapunov weights, global termination, all-side transfer, and `all_n_proved_by_checker` remain zero.
