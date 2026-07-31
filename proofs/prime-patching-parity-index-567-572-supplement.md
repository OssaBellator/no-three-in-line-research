# Prime-patching parity index supplement: `docs/567--572`

This supplement continues the cumulative parity index after `docs/566`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cpx--PP3cpz | Band-offset four/seven seams admit a finite transition graph, but every shortest zero-drift controller has a long-range collinearity witness | PROVED / CANDIDATE OBSTRUCTION | `docs/567-band-offset-boundary-cycle-obstruction.md` |
| PP3cqa--PP3cqc | Cylinder Hall syndrome-choice labels biject with complete four-by-four choice-grid pairs and lift to two orientation witnesses | PROVED / TYPED CANDIDATE DECODER | `docs/568-choice-grid-decoder-for-cylinder-hall-states.md` |
| PP3cqd--PP3cqf | One conservative threshold matrix has 84 aligned permutation decompositions, sharp discrepancy one, and an exact normal row-space oracle | PROVED / SOURCE-ALIGNED BENCHMARK | `docs/569-aligned-conservative-threshold-layer-benchmark.md` |
| PP3cqg--PP3cqi | Original leaf grading and encoded node grading are reconciled by a size-preserving encoding, and structural risk is separated from missing geometric incidence risk | PROVED / RECONCILED SOURCE COMBINATORICS | `docs/570-prefix-grading-propagation-and-risk-interface.md` |
| PP3cqj--PP3cql | The shell service multiset has a canonical identity incidence, exact reserve optimum `6/5`, and all-length repetition | PROVED / SOURCE-DERIVED BENCHMARK | `docs/571-canonical-source-service-shell-incidence.md` |
| PP3cqm--PP3cqo | Source conversions preserve 22/30 candidate fields and positive fixture slack but promote no actual row | PROVED / EVIDENCE GATE CLOSED | `docs/572-source-conversion-evidence-gate.md` |

## Exact diagnostics

Run

```bash
python scripts/check_frontier_567_572.py
```

or the six new audits individually:

```bash
python scripts/check_boundary_band_offset_cycles.py
python scripts/check_hall_choice_grid_decoder.py
python scripts/check_aligned_threshold_decompositions.py
python scripts/check_prefix_grading_propagation.py
python scripts/check_canonical_shell_service_incidence.py
python scripts/check_source_conversion_evidence_gate.py
```

The new audits cover 282 legal adjacent boundary transitions, 1498 short
zero-drift boundary cycles, all twelve compatible Hall grid pairs, all 84 aligned
threshold decompositions and 1120 primitive normals, the reconciled
30-leaf/30-encoded-node prefix profile, all thirty canonical shell orders with
five hundred repeated prefixes, and the exact coupled evidence gate.

The next available theorem identifier is `PP3cqp`.
