# Exact recurrent transition-domain progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records the boundary between symbolic first-host restoration states and source-backed physical transitions.

## ERL2h — route-cover admission

The route-cover admission compiler classifies every set of route-closed directed edges.

For selected labels:

```text
edge masks                         64
pair-covered masks                 27
masks containing a scalar cover    25
cycle obstructions                  2.
```

For full menu states:

```text
edge masks                         256
pair-covered masks                  81
masks containing a scalar cover     79
cycle obstructions                   2.
```

Pair coverage is necessary and sufficient except when the selected directions form one of the two directed cycles. One bidirectionally closed reversal pair breaks the cycle obstruction.

The current route-closed edge set is empty, so no scalar cover is complete.

## ERL2i — transition-domain source audit

The four symbolic states are

```text
00 blocked
01 restore 20
10 restore 02
11 restore both.
```

They induce eight directed single-bit candidate edges. Five construction interfaces were audited:

```text
installed operation registry 1166
protected-interface execution
target-anchor lineage
inherited-coordinate diagonal blocks
owner/fate lineage and line kernels.
```

The installed registry is a finite operation-kind and payment-class bank, not an occurrence-level legality table. Protected-interface and target-anchor restoration results are finite fixtures at other sides and do not identify this host's cells or operation trace. The owner/fate and inherited-coordinate interfaces remain unpopulated at the recurrent-row level.

Exact current census:

```text
symbolic states                     4
physical state records              0
symbolic directed edges             8
physical legal edges                0
edge-to-operation-kind mappings     0
persistent edge owner tokens        0
edge operation traces               0
source-reduced edge domain          0.
```

Promoting one edge requires twelve fields:

```text
physical occurrence
persistent owner
source and target state references
operation kind and registry entry
operation trace
changed cell and action
legality proof
intermediate states
realization status.
```

Both endpoint states must be physically realized. Edges incident to `11` additionally require an exact physical restore-both state; local exposure of response `2301` is not enough.

## Current boundary

The exact Boolean state, selector and cover calculations are complete, but the physical transition graph is unknown. It may be the full square, a proper subgraph, or empty.

Therefore

```text
physical_transition_domain_known = 0
route_cover_admission_applicable_to_physical_mask = 0
physical_route_assignment_complete = 0
promotion_to_recurrent_closure_allowed = 0
all_n_proved_by_checker = 0.
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_route_cover_admission.py
data/exact_recurrent_first_host_route_cover_admission.json
docs/exact-recurrent-first-host-route-cover-admission.md

scripts/check_exact_recurrent_first_host_transition_domain_source_audit.py
data/exact_recurrent_first_host_transition_domain_source_audit.json
docs/exact-recurrent-first-host-transition-domain-source-audit.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
