# Sealed verification artifacts for the source-statement root

CMR2438--CMR2453 made the source-statement census explicit and synchronized it with
`SOURCE_STATEMENTS_TRUE` and `T01_SOURCE_STATEMENTS`. The first version still allowed a proved
statement to carry an arbitrary verification locator/digest pair. Repeating that pair inside a
statement record did not bind the statement to a reconstructed proof object. This chapter removes
that remaining opaque evidence step.

## Theorem CMR2454 — OPAQUE VERIFICATION-POINTER DEFECT

A nonempty source-kind-specific artifact kind together with an arbitrary locator/digest proves only
that a pointer was supplied. It does not commit to:

- the proof statement;
- the external proof object;
- supporting source-proof artifacts; or
- a canonical bundle for the cited source statement.

Consequently the version-1 verification pointer was insufficient as completion-to-evidence
binding.

## Theorem CMR2455 — PROVED AS A TYPED INTERFACE

Every proved source statement now has exactly one canonical source-verification artifact containing:

- the exact source ID;
- a globally unique artifact ID;
- the source-kind-specific artifact kind;
- the exact source-statement SHA-256;
- a separate external `proof_locator` and `proof_digest`;
- a nonempty proof statement and evidence description; and
- a sorted duplicate-free list of supporting source-verification artifact IDs.

The fixed source-kind-to-artifact-kind map remains unchanged.

## Theorem CMR2456 — PROVED

Artifact presence is exact:

- a proved source statement has exactly one verification artifact;
- an open source statement has none;
- no two sources share one artifact;
- artifact IDs are globally unique; and
- every artifact's statement SHA-256 equals the literal statement record it verifies.

Thus open statements cannot carry placeholders and proved statements cannot close using an
artifact for a different source or statement.

## Theorem CMR2457 — PROVED

For a proved source statement with source ID `S`, the statement record must use

```text
source-verification-artifact-registry://S
```

as its verification locator. Its verification digest must equal the reconstructed per-source
verification-artifact bundle digest.

The artifact itself carries the external proof locator/digest. Therefore the completion seal is
separate from the external proof pointer and commits to the artifact kind, proof statement,
external pointer, support list and evidence description.

## Theorem CMR2458 — PROVED

The checker reconstructs the source-verification support graph from artifact support IDs.

- Unknown support artifacts are rejected.
- Self-support and duplicate support are rejected.
- The complete graph must be acyclic.
- A canonical topological artifact order and exact support-edge count are published.

This prevents circular documentary justification among the cited source proofs. It does not prove
that the supplied support is logically sufficient.

## Theorem CMR2459 — PROVED

Each source-truth bundle now includes both the canonical statement record and the exact sealed
verification-artifact bundle. The aggregate source-truth digest therefore changes whenever the
proof pointer, proof statement, evidence or support changes.

The existing `source-truth-proof` obligation artifact remains the unique aggregate binding:

```text
source-statement-truth-registry://SOURCE_STATEMENTS_TRUE
```

Its digest must equal the complete reconstructed source-truth bundle digest. No parallel closure
path is introduced.

## Theorem CMR2460 — HONEST EXECUTION BOUNDARY

Exact statement text, matching hashes, typed artifacts, canonical bundle seals and an acyclic
support graph do not verify mathematical truth or logical sufficiency. The checker remains a
documentary source-proof interface and permanently publishes

```text
all_n_proved_by_checker = 0
```

The genuine parent rule and its source proofs are still absent from the repository.

## Corollary CMR2461 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_source_statement_truth_registry.py` version 2 validates:

- exact literal source statements and hashes;
- exact proved/open artifact coverage;
- source-kind-specific verification artifacts;
- statement-to-artifact-bundle sealing;
- acyclic source-proof support;
- complete source-use footprints;
- aggregate `source-truth-proof` binding; and
- the permanent nonproof boundary.

The script syntax-compiled in the publication environment. Isolated tests accepted a canonical
sealed record and rejected an incorrect digest and a cyclic artifact-support graph. A complete
dependency-backed certificate suite was not available. No source statement, recurrence
exhaustiveness theorem or all-`n` implication is claimed proved.
