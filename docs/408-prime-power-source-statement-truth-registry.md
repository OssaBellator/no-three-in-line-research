# Exact source-statement truth registry

The parent-rule provenance layer identifies every cited source and records a locator and statement
SHA-256, but it does not contain the statement text and does not check that the recorded digest is
the digest of that text. The first atomic frontier target therefore still lacked an executable
statement-by-statement proof bank. This chapter supplies that missing root interface.

## Theorem CMR2438 — PROVED AS AN INTERFACE

Every source in the rule-provenance certificate has exactly one source-statement record in the
same canonical source-ID order. The record contains:

- the exact provenance source ID, source kind and source locator;
- the literal mathematical statement text;
- its lowercase SHA-256 computed from the exact UTF-8 text;
- an open/proved verification status;
- the exact required verification-artifact kind;
- the supplied verification artifact locator and digest when proved; and
- a nonempty verification note.

The statement digest must equal both the recomputed text digest and the digest already stored in
the provenance source record. Thus an arbitrary unattached 64-character digest is no longer an
acceptable source statement.

## Theorem CMR2439 — PROVED

Verification artifacts are fixed by source kind:

| Source kind | Required verification artifact |
|---|---|
| `definition` | `definition-conformance-proof` |
| `case-split` | `case-split-exhaustiveness-proof` |
| `lemma` | `lemma-proof` |
| `domain` | `domain-characterization-proof` |
| `exclusion` | `exclusion-proof` |
| `computation` | `reproducible-computation-proof` |

A proved statement must carry the exact required kind and nonempty artifact locator and digest. An
open statement must carry no verification artifact fields. Placeholder artifacts on open
statements and wrong proof kinds are rejected.

## Theorem CMR2440 — PROVED

The source registry and the all-`n` semantic dossier must refer to the same recurrence skeleton.
The checker requires:

- every global skeleton clause to use the exact rule ID of the provenance clause manifest; and
- the set of source case IDs used by the global skeleton to equal the complete parent-case set of
  the provenance manifest.

This prevents a source-truth bank for one recurrence rule from being attached to a different
finite quotient dossier.

## Theorem CMR2441 — PROVED

For every source, the checker reconstructs the complete provenance-use footprint:

- parent cases citing the source;
- clauses citing the source;
- parameter axes citing the source; and
- excluded parameter rows citing the source.

Each source bundle publishes its exact use lists and total use count. Open source IDs are ordered
by decreasing downstream use, with source ID as the deterministic tie-breaker. This produces an
executable proof-prioritization list without estimating proof difficulty or claiming mathematical
progress.

## Theorem CMR2442 — PROVED

The source-statement census is synchronized with the fixed semantic obligation
`SOURCE_STATEMENTS_TRUE`.

The obligation may close if and only if every canonical source statement is marked proved. Since
this obligation has no semantic predecessors, the all-proved source census and the effective
closure flag must agree exactly.

## Theorem CMR2443 — PROVED

The synchronization uses the existing typed obligation-artifact path rather than creating a
parallel closure locator.

When all source statements are proved, the unique `source-truth-proof` artifact for
`SOURCE_STATEMENTS_TRUE` must use

```text
source-statement-truth-registry://SOURCE_STATEMENTS_TRUE
```

and its digest must equal the canonical digest of the complete source-truth bundle list. The
ordinary obligation-artifact registry continues to seal the closure obligation itself. This
composition is noncircular and preserves one authoritative artifact path.

## Theorem CMR2444 — HONEST EXECUTION BOUNDARY

Exact statement text, a matching digest, a typed proof artifact and a complete source-use footprint
do not establish that the supplied proof is correct. The checker validates documentary identity,
coverage and composition only. It permanently reports

```text
all_n_proved_by_checker = 0
```

The repository still states that the actual exhaustive parent rule is absent. No source statement
or recurrence-exhaustiveness theorem is declared proved by this interface.

## Corollary CMR2445 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_source_statement_truth_registry.py` validates the exact source text
bank, source-kind-specific verification artifacts, recurrence-dossier identity, downstream-use
footprints and the binding of the complete source-truth bundle to the existing
`source-truth-proof` obligation artifact.

The script syntax-compiled in the publication environment. Isolated schema tests accepted a
canonical open statement and rejected an incorrect statement digest. A complete dependency-backed
certificate suite was not available.
