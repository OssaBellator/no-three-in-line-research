# First-host physical fibre batch gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact reject-by-default ingestion contract. The current batch is empty and incomplete.

## Purpose

The source-coverage audit shows that normalized or structural evidence cannot
populate a physical occurrence. This gate defines the minimum source-backed
record that can enter recurrent-row compilation.

## Batch completeness

A batch may set `batch_complete=true` only when it supplies all of the following:

```text
source-defined occurrence domain
exact expected occurrence count
source-backed completeness proof
one unique record for every occurrence
```

The expected count must equal the number of accepted records. A claimed empty
batch is valid only when an external source proves that the occurrence domain is
empty.

## Per-occurrence requirements

Each record must preserve the dual-edge convention:

```text
lineage host edges: 10, including target 01
response edges:      9, excluding target 01
response family:     3012, 3210
```

It must also provide source-backed values for:

```text
physical embedding and physical source trace
deleting causes and owners for 02 and 20
owner/fate/collision/line/interface/CRT provenance
complete legal-operation enumeration
complete intermediate-state enumeration
complete labelled child row
strictly positive parent and child weights
parent budget
realization status equal to realized
```

Operation or intermediate-state lists may be empty only when their source-backed
scope is explicitly complete. Child rows may be empty only as a complete exact
row, with matching positive-weight labels.

Placeholder values such as `unknown`, `todo`, `schema-completion-only`,
`normalized-only`, `catalog-only`, `local-candidate-only`, and
`upper-bound-only` are rejected as source references.

## Current exact result

```text
records                               0
accepted physical records             0
expected occurrence count known       0
schema-completion candidates rejected 2
batch complete                         0
promotion allowed                      0
```

Both records from the dual-edge bridge fail before row analysis because their
physical source fields are null and their realization status is only
`schema-completion-only`.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_physical_fibre_batch_gate.py \
  --check data/exact_recurrent_first_host_physical_fibre_batch_gate.json
```

The checker validates exact edge conventions, rational multiplicities and
weights, source references, occurrence-domain completeness, and the two current
rejections. It rejects eleven deliberate corruptions.

The next admissible contribution is a source-backed occurrence batch or a
source-backed proof that the occurrence domain is empty. No schema completion,
normalized projection, or local affine witness can pass this gate by itself.

Physical realizability, exclusion, recurrent rows, strict Lyapunov slack,
global termination, and `all_n_proved_by_checker` remain zero.
