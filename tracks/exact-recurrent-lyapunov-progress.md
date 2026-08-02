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

## Active work queue

- Issue #18: attach owner, fate, collision, line, interface, CRT and background
  provenance; enumerate installed legal transitions.
- Issue #19: preserve proof-or-refutation posture and publish any realizable
  non-strict SCC rather than hiding it behind another conditional interface.
- Issue #20: classify the unique depth-two overlap under installed operations.
- Issue #21: compile exact offspring rows and solve or refute the strict rational
  Lyapunov system.

## Next acceptance test

A provenance compiler for at least one of the eleven residual hosts must output:

1. a stable labelled state identifier;
2. the exact physical reason for every unavailable cell;
3. every installed legal operation and intermediate state;
4. the exact resulting child labels and multiplicities;
5. a complete row suitable for `scripts/check_exact_recurrent_manifest.py`;
6. either positive exact slack or an explicit failed row/SCC.

No progress entry may set `all_n_proved_by_checker` to one.
