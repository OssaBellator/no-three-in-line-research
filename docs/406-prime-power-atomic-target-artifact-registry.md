# Typed proof artifacts for every atomic all-frontier target

CMR2406--CMR2421 introduced forty-three atomic targets and synchronized their completion states
with the semantic, premise, handoff and exceptional-chamber layers. The target completion records
still contained opaque locator/digest pairs. This chapter replaces that final opaque link with one
canonical typed artifact bundle for every effectively complete target.

## Theorem CMR2422 — PROVED AS AN INTERFACE

Each of the forty-three atomic targets has one fixed required artifact kind, inherited directly
from its atomic target definition. A target may have at most one target artifact, and artifact IDs
are globally unique.

Every artifact contains:

- its target ID and exact required kind;
- a locator, digest and mathematical statement;
- exact immediate target-artifact support;
- exact external obligation, premise or handoff-artifact support;
- exact selected certificate-digest support; and
- a nonempty evidence description.

## Theorem CMR2423 — PROVED

Artifact presence is synchronized with effective target completion.

- Every effectively complete target must have exactly one typed target artifact.
- Every open or ineffective target must have no target artifact.
- The target-artifact locator and digest must equal the locator and digest in the atomic target
  completion record.

Thus a target cannot close using an untyped or differently identified evidence object.

## Theorem CMR2424 — PROVED

For every completed target, the target-artifact support list is reconstructed from the atomic
proof-dependency DAG and must equal the artifact IDs of every immediate proof dependency.

Omission of one dependency artifact, addition of an unrelated target artifact, self-support and
duplicate support are rejected. Since the target proof graph is acyclic, this produces an exact
acyclic target-artifact support graph without trusting a separately supplied edge list.

## Theorem CMR2425 — PROVED

Targets linked to semantic obligations, final premises or handoff assertions must cite the exact
artifacts in the corresponding authoritative registries.

Consequently:

- semantic targets cite the complete typed obligation-artifact bundle of their linked obligation;
- premise targets cite the unique typed artifact of their linked premise; and
- handoff targets cite the unique assertion-specific handoff artifact.

The checker reconstructs these support sets from the nested validated registries.

## Theorem CMR2426 — PROVED

Selected integration targets additionally bind the exact certificate surfaces on which their
meaning depends:

- state-predicate and row-theorem targets bind the quotient semantic refinement;
- the global-family target binds the source-independent skeleton;
- exceptional-zero and hard-core targets bind the chamber registry and their separate 232/20
  aggregate disposition digests;
- typed-support targets bind the obligation registry, support DAG and premise registry;
- handoff-review and dossier targets bind the exact final handoff and dossier certificates; and
- the root target binds the synchronized current-frontier certificate.

These bindings prevent evidence prepared for one finite dossier from being silently reused in a
different dossier.

## Theorem CMR2427 — PROVED

The registry publishes one canonical bundle record for every target, including its frontier,
completion state, required kind, immediate dependencies, linked external modules, exact required
support lists and bundle digest.

It separately reports:

- completed and open target-artifact bundle counts;
- exact typed target-artifact coverage;
- exact immediate dependency-artifact support;
- exact external registry binding;
- completeness of the forty-three-artifact bank; and
- a post-frontier target-artifact gate requiring both the synchronized current-frontier gate and
  a complete target-artifact bank.

## Theorem CMR2428 — HONEST EXECUTION BOUNDARY

A typed artifact, exact support list, locator/digest equality or certificate binding does not prove
that the artifact statement is true, logically sufficient or correctly reviewed. This checker is
a documentary integrity layer and permanently publishes

```text
all_n_proved_by_checker = 0
```

## Corollary CMR2429 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_atomic_target_artifact_registry.py` validates the complete typed
artifact bank for all forty-three atomic targets, exact immediate target support and exact external
registry/certificate bindings.

The script syntax-compiled in the publication environment. A full dependency-backed certificate
suite was not available here. No atomic target, exceptional chamber, handoff assertion or all-`n`
implication is claimed proved by this chapter.
