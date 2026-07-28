# Source-truth synchronization at the all-frontier root

The exact source-statement registry makes every cited statement explicit, but an all-frontier
certificate could still be reviewed without presenting that registry. This chapter adds a narrow
source-root execution gate that requires the source bank, semantic obligation stack and atomic
source target to be the same dossier.

## Theorem CMR2446 — PROVED

The source-root certificate validates both:

- the synchronized current-frontier execution certificate; and
- the exact source-statement truth registry certificate.

It extracts the typed obligation-artifact registry nested inside the current-frontier dossier and
requires its certificate digest to equal the obligation registry used by the source-truth
certificate. Thus the source bank cannot be attached to a different obligation closure.

## Theorem CMR2447 — PROVED

The checker reconstructs the atomic target result for `T01_SOURCE_STATEMENTS` and requires exact
equality between:

- effective completion of `T01_SOURCE_STATEMENTS`; and
- readiness of the exact source-statement truth registry.

Since the source registry separately synchronizes its all-proved census with
`SOURCE_STATEMENTS_TRUE`, the source statements, semantic obligation and atomic target now form one
strict three-layer identity.

## Theorem CMR2448 — PROVED

The source-root gate contains four exact flags:

- synchronized current-frontier readiness;
- source-statement truth readiness;
- `T01_SOURCE_STATEMENTS` completion; and
- source-root execution readiness.

The final source-root flag is one only when all three prerequisite flags are one. Presenting an
otherwise ready frontier dossier without the exact source bank cannot pass this gate.

## Theorem CMR2449 — PROVED

The source-root blocker record publishes:

- proved source-statement count;
- open source-statement count;
- open source IDs ordered by decreasing downstream provenance use; and
- the current atomic source target.

While any statement remains open, the current target is `T01_SOURCE_STATEMENTS`. Only after the
complete source census closes does the record advance to `T02_RULE_EXHAUSTIVENESS`.

## Theorem CMR2450 — PROVED

The gate binds the exact certificate digests of:

- the synchronized current-frontier execution surface;
- the source-statement truth registry; and
- their shared typed obligation-artifact registry.

These bindings prevent source verification results from being silently transplanted between
independent frontier dossiers.

## Theorem CMR2451 — PROVED

The source-root synchronization is noncircular. The source-statement bundles determine the digest
stored by the existing `source-truth-proof` artifact. The obligation registry then feeds the
semantic closure and atomic target stack. The source-root wrapper reads and compares those already
formed descendants; no source bundle contains the wrapper certificate or its own descendant
digest.

## Theorem CMR2452 — HONEST EXECUTION BOUNDARY

A ready source-root gate certifies documentary agreement, not the validity of any source proof or
the exhaustiveness of the recurrence rule. It permanently publishes

```text
all_n_proved_by_checker = 0
```

The actual parent rule remains absent from the repository, and neither `T01_SOURCE_STATEMENTS` nor
`T02_RULE_EXHAUSTIVENESS` is claimed complete for genuine data.

## Corollary CMR2453 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_source_truth_frontier_execution.py` validates shared obligation-registry
identity, exact source-census/T01 synchronization, the strict source-root gate and the prioritized
source blocker record.

The script syntax-compiled in the publication environment. A complete dependency-backed source
certificate suite was not available.
