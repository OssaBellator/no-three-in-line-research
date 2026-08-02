# Exact side-four residual lineage projection

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact coordinate-lineage join proved; global provenance remains absent.

## Result

The eleven states in `data/exact_recurrent_side_four_kernel.json` join
bijectively, by their deletion sets, to eleven stable host identifiers in the
composite-modulus raw-fibre lineage manifest.

The three local blocker classes likewise join to the stable upstream blocker
identifiers

```text
{02,20} -> b4-8a44614df456
{02,31} -> b4-557232b8e56a
{13,31} -> b4-4b72675a7313
```

For every residual host, the checker verifies all of the following:

1. the deletion set agrees exactly;
2. the surviving response permutations and intrinsic triple counts agree;
3. the blocker-alternative dispatch agrees;
4. the contained minimal-blocker identifiers agree;
5. no local residual state is missing or duplicated.

Thus the coordinate host/response residual kernel is no longer disconnected
from the upstream lineage namespace.

## Exact missing-data certificate

The upstream source manifest explicitly certifies coordinate host/response
lineage but retains zero for global owner/fate/collision/interface/CRT
provenance and recurrent weighted rows. The projection therefore keeps every
unsupported provenance slot null.

Across the eleven residual hosts, the unresolved inputs are exactly

```text
physical deletion-cause assignments                 32
background records                                  11
owner/fate/collision/line/interface/CRT fields       66
legal operation families                            11
recurrent child rows                                11
```

These are not estimates. The first count is the sum of the deletion-set sizes;
the other counts follow from the required schema per joined host.

## Why this matters

The local blocker theorem says which cells would have to be reopened to expose
a triple-free response. It does not say why those cells are unavailable, who
owns the corresponding obstruction, whether reopening is legal, what collateral
is created, or whether the same host can recur later.

The new projection prevents those missing facts from being silently replaced by
anonymous labels. A future provenance compiler must populate the null slots with
source-backed records and then enumerate installed operations. Merely assigning
synthetic owner names or copying one representative background is rejected.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_lineage_projection.py \
  --kernel data/exact_recurrent_side_four_kernel.json \
  --projection data/exact_recurrent_side_four_lineage_projection.json
```

Expected structural output includes

```text
joined_residual_hosts                                      11
joined_blocker_classes                                      3
missing_deletion_cause_assignments                         32
missing_background_records                                11
missing_owner_fate_collision_line_interface_crt_fields     66
missing_legal_operation_families                          11
missing_recurrent_child_rows                              11
mutation_corruptions_rejected                              9
```

All global proof and strict-Lyapunov flags remain zero.

## Next theorem target

Choose one stable upstream host, beginning with
`s4-75b04c45c1c8eac2` for deletion set `{02,20}`, and enumerate every physically
realizable lineage fibre over that host. Each record must include the exact
background, a cause for both unavailable cells, the complete compression key,
and every installed legal operation. The first acceptable output is either a
complete exact offspring row or a source-backed witness showing that the current
manifests do not determine one.
