# Typed proof artifacts for every atomic all-frontier target

CMR2406--CMR2421 introduced forty-three atomic targets and synchronized their completion states
with the semantic, premise, handoff and exceptional-chamber layers. The target completion records
still contained opaque locator/digest pairs. This chapter assigns those pairs one canonical,
noncircular meaning through a typed target-artifact registry.

## Theorem CMR2422 — PROVED AS AN INTERFACE

Each of the forty-three atomic targets has one fixed required artifact kind, inherited directly
from its atomic target definition. A target may have at most one target artifact, and artifact IDs
are globally unique.

Every artifact contains:

- its target ID and exact required kind;
- a separate external proof locator and proof digest;
- a mathematical statement and nonempty evidence description;
- exact immediate target-artifact support;
- namespace-qualified obligation, premise or handoff-artifact support; and
- role-qualified selected certificate support.

## Theorem CMR2423 — PROVED

Artifact presence is synchronized with effective target completion.

- Every effectively complete target must have exactly one typed target artifact.
- Every open or ineffective target must have no target artifact.
- A completed target's atomic completion locator must be exactly
  `atomic-target-artifact-registry://<target ID>`.
- Its atomic completion digest must equal the reconstructed target-artifact bundle digest.

The artifact's external proof locator/digest is therefore distinct from the completion seal. This
avoids a self-referential bundle hash while preventing an arbitrary completion digest from merely
being repeated inside the artifact record.

## Theorem CMR2424 — PROVED

For every completed target, the target-artifact support list is reconstructed from the atomic
proof-dependency DAG and must equal the artifact IDs of every immediate proof dependency.

Omission of one dependency artifact, addition of an unrelated target artifact, self-support and
duplicate support are rejected. Since the target proof graph is acyclic, this produces an exact
acyclic target-artifact support graph without trusting a separately supplied edge list.

## Theorem CMR2425 — PROVED

Targets linked to semantic obligations, final premises or handoff assertions must cite the exact
artifacts in the corresponding authoritative registries. References are namespace-qualified as
`obligation:...`, `premise:...` or `handoff:...`, so equal raw artifact IDs in different registries
cannot be confused.

Consequently:

- semantic targets cite the complete typed obligation-artifact bundle of their linked obligation;
- premise targets cite the unique typed artifact of their linked premise; and
- handoff targets cite the unique assertion-specific handoff artifact.

## Theorem CMR2426 — PROVED

Selected integration targets additionally bind role-qualified certificate surfaces:

- state-predicate and row-theorem targets bind the quotient semantic refinement;
- the global-family target binds the source-independent skeleton;
- exceptional-zero and hard-core targets bind the chamber registry and their separate 232/20
  aggregate disposition digests;
- typed-support targets bind the obligation registry, support DAG and premise registry; and
- handoff-review and dossier targets bind the exact final handoff and dossier certificates.

The current-frontier certificate is an ancestor containing the atomic completion records, so it is
bound by the registry as a whole and is not inserted into the root target bundle. This avoids a
circular equation in which the root bundle digest would depend on a certificate that already
contains that same digest.

## Theorem CMR2427 — PROVED

The registry publishes one canonical bundle record for every target, including its frontier,
completion state, required kind, immediate dependencies, linked external modules, exact required
support lists and bundle digest.

It separately reports:

- completed and open target-artifact bundle counts;
- exact typed target-artifact coverage;
- exact immediate dependency-artifact support;
- namespace-qualified external registry binding;
- role-qualified certificate binding;
- exact completion-to-bundle binding;
- completeness of the forty-three-artifact bank; and
- a post-frontier target-artifact gate requiring both the synchronized current-frontier gate and
  a complete target-artifact bank.

## Theorem CMR2428 — HONEST EXECUTION BOUNDARY

A typed artifact, exact support list, bundle digest or certificate binding does not prove that the
artifact statement is true, logically sufficient or correctly reviewed. This checker is a
documentary integrity layer and permanently publishes

```text
all_n_proved_by_checker = 0
```

## Corollary CMR2429 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_atomic_target_artifact_registry.py` version 2 validates the complete
typed artifact bank for all forty-three atomic targets, exact immediate support, namespace- and
role-qualified external support, and exact completion-to-bundle sealing.

The script syntax-compiled in the publication environment and isolated schema rejection tests
passed. A full dependency-backed certificate suite was not available here. No atomic target,
exceptional chamber, handoff assertion or all-`n` implication is claimed proved by this chapter.
