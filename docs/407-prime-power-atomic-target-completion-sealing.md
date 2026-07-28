# Noncircular sealing of atomic target completions

The first target-artifact registry draft required the artifact locator/digest to equal the atomic
completion locator/digest. That equality identified the same opaque pair twice but did not force
the completion digest to commit to the reconstructed artifact, support lists or certificate
bindings. This chapter records the version-2 correction.

## Theorem CMR2430 — DEFECT ISOLATION

Equality between an atomic completion locator/digest and fields copied into its target artifact is
not a cryptographic bundle binding. The target statement, evidence, immediate support and external
bindings could change while the repeated pair remained unchanged.

The branch therefore does not treat the version-1 echo condition as sufficient documentary
closure.

## Theorem CMR2431 — PROVED

Version 2 separates two roles:

1. `proof_locator` and `proof_digest` identify the external mathematical proof object carried by
   the target artifact; and
2. the atomic completion locator/digest identify the canonical target-artifact registry bundle.

The proof pointer may be hashed inside the bundle without being required to equal the bundle hash.

## Theorem CMR2432 — PROVED

For every effectively complete target `T`, the completion fields are fixed by

```text
artifact_locator = atomic-target-artifact-registry://T
artifact_digest  = atomic_target_artifact_bundle_sha256(T)
```

The bundle digest is reconstructed from the target definition, completion state, immediate proof
dependencies, linked external modules, exact support references and the canonical target artifact.
An arbitrary or stale completion digest is rejected.

## Theorem CMR2433 — PROVED

External artifact support is namespace-qualified:

```text
obligation:<artifact ID>
premise:<artifact ID>
handoff:<artifact ID>
```

Thus a raw ID collision between registries cannot merge two semantically different dependencies.
Exact support is reconstructed from the validated nested registries.

## Theorem CMR2434 — PROVED

Certificate support is role-qualified as `<role>:<certificate SHA-256>`. This preserves why a
certificate is required, rather than checking an unlabelled set of hashes.

The roles include semantic refinement, global-family skeleton, exceptional-chamber registry,
zero-selector and hard-core disposition aggregates, obligation registry, obligation support DAG,
premise registry, handoff artifact registry, final handoff and final dossier.

## Theorem CMR2435 — PROVED

A target bundle may bind only independent or strictly lower documentary surfaces. It may not bind
an ancestor certificate that already contains the target completion digest.

In particular, the root target does not include the current-frontier certificate hash in its own
bundle. The target-artifact registry certificate contains and binds that current-frontier
certificate at the registry level instead. This removes the self-referential equation

```text
root bundle digest -> current-frontier digest -> root completion digest -> root bundle digest.
```

## Theorem CMR2436 — PROVED

The strengthened registry publishes independent claims for:

- exact completion-to-bundle binding;
- namespace-qualified external artifact support;
- role-qualified certificate binding;
- noncircular ancestor-certificate binding; and
- the complete forty-three-target artifact bank.

The post-frontier gate remains conditional on both synchronized current-frontier readiness and a
complete typed target-artifact bank.

## Corollary CMR2437 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_atomic_target_artifact_registry.py` now requires certificate version 2
and enforces the noncircular completion-sealing rules above.

The script syntax-compiled and isolated schema tests rejected wrong target artifact kinds. A full
nested certificate regression suite was not available. These results repair documentary binding
only and do not establish any mathematical frontier target or the all-`n` conjecture.
