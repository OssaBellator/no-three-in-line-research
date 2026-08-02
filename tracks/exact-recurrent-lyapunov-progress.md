# Exact recurrent Lyapunov progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

## ERL1 finite seed — PROVED LOCALLY

The first exact physical host compiler is installed.

```text
script   = scripts/check_exact_recurrent_side_four_kernel.py
manifest = data/exact_recurrent_side_four_kernel.json
chapter  = docs/exact-recurrent-side-four-kernel.md
workflow = .github/workflows/exact-recurrent-side-four-kernel.yml
```

Exact output:

```text
feasible side-four hosts       86
response incidences           206
hosts with good response       75
residual hosts                 11
minimal blocker patterns        3
maximum local reopening depth   2
```

The minimal blocker basis is

```text
{02,20}, {02,31}, {13,31}.
```

The unique depth-two overlap is

```text
{02,13,20,31}.
```

The compiler reconstructs the host family from first principles, compares the
complete deterministic manifest, and rejects seven mutation corruptions. It
certifies only coordinate-host-response completeness. All global provenance,
legal-reopening, recurrent-row, Lyapunov and all-`n` flags remain zero.

## ERL1a lineage projection — PROVED EXACTLY

The local residual kernel now joins bijectively to the stable host and blocker
identifiers in the composite-modulus side-four raw-fibre lineage manifest.

```text
script     = scripts/check_exact_recurrent_side_four_lineage_projection.py
projection = data/exact_recurrent_side_four_lineage_projection.json
chapter    = docs/exact-recurrent-side-four-lineage-projection.md
workflow   = .github/workflows/exact-recurrent-side-four-lineage-projection.yml
```

The audit checks deletion sets, response spectra, blocker dispatch and contained
blocker identifiers for all eleven residual hosts. It rejects nine mutation
corruptions.

The exact unresolved provenance inventory is

```text
physical deletion-cause assignments                 32
background records                                  11
owner/fate/collision/line/interface/CRT fields       66
legal operation families                            11
recurrent child rows                                11
```

This is a missing-data certificate, not a proof of legal reopening. Unsupported
provenance slots remain null and every global proof flag remains zero.

## Active work queue

- Issue #18: populate the first complete physical lineage fibre, beginning with
  upstream host `s4-75b04c45c1c8eac2` for deletion set `{02,20}`; then enumerate
  installed legal transitions.
- Issue #19: preserve proof-or-refutation posture and publish any realizable
  non-strict SCC rather than hiding it behind another conditional interface.
- Issue #20: classify the unique depth-two overlap under installed operations.
- Issue #21: compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Next acceptance test

A provenance compiler for upstream host `s4-75b04c45c1c8eac2` must output:

1. every physically realizable background fibre over deletion set `{02,20}`;
2. the exact physical cause and owner of unavailable cells `02` and `20`;
3. the complete fate/collision/line/interface/CRT compression key;
4. every installed legal operation and intermediate state;
5. exact resulting child labels and multiplicities;
6. either a complete row suitable for `scripts/check_exact_recurrent_manifest.py`
   or a source-backed witness that the present repository data do not determine
   such a row.

No progress entry may set `all_n_proved_by_checker` to one.
