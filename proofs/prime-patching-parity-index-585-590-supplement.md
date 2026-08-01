# Prime-patching parity index supplement: `docs/585--590`

This supplement continues the cumulative parity index after `docs/584`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3crz--PP3csb | Radius-32 sixth-block extensions require at least three point deletions; four sharp repairs exist and create a five-resource saturation defect | PROVED | `docs/585-three-point-boundary-seam-repair-catalogue.md` |
| PP3csc--PP3cse | The coordinate Hall decoder has a six/six robustness dichotomy under one residual-cell exclusion, and microscopic orientation cannot repair fragile pairs | PROVED | `docs/586-single-exclusion-robustness-of-hall-grid-decoder.md` |
| PP3csf--PP3csh | The nearest fully legal four-layer conservative threshold matrices are at entrywise distance six; a canonical replacement has prefix discrepancy one | PROVED FOR REPLACEMENT SEARCH | `docs/587-nearest-legal-conservative-threshold-matrix.md` |
| PP3csi--PP3csk | An ancestry-aware dynamic program reconstructs the exact support-nesting count and canonical interval-span aggregate | PROVED FOR THE ENCODED MODEL | `docs/588-ancestry-labelled-support-interval-risk.md` |
| PP3csl--PP3csn | The `docs/517` shell actions span the even-sum index-two cycle lattice; unit cycle resources have half-integral preimages | PROVED / TYPE MISMATCH | `docs/589-index-two-shell-resource-lattice-obstruction.md` |
| PP3cso--PP3csq | Replacement outcomes are exact, candidate completion remains 23/30, and zero global rows are promoted despite positive fixture slack | PROVED | `docs/590-replacement-search-evidence-gate.md` |

## Exact diagnostics

Run

```bash
python scripts/check_frontier_585_590.py
```

or individually with

```bash
python scripts/check_boundary_three_point_seam_repair.py
python scripts/check_hall_single_exclusion_robustness.py
python scripts/check_nearest_legal_threshold_matrix.py
python scripts/check_prefix_ancestry_span_dp.py
python scripts/check_shell_index_two_resource_lattice.py
python scripts/check_replacement_evidence_gate.py
```

The next available theorem identifier is `PP3csr`.
