# Typed artifacts for the six induction-handoff assertions

CMR2374--CMR2381 allow one opaque locator/digest pair on each final induction-handoff
assertion. This chapter replaces those opaque pairs with exact assertion-specific artifact
bundles supported by the typed final-premise artifacts.

## Theorem CMR2390 — PROVED AS AN INTERFACE

Each of the six fixed handoff assertions has one fixed required artifact kind:

1. base-domain handoff proof;
2. nonbase-coverage handoff proof;
3. invariant handoff proof;
4. termination handoff proof;
5. exceptional handoff proof; and
6. objective-translation handoff proof.

## Theorem CMR2391 — PROVED

A handoff artifact has the canonical record

\[
(\text{assertion ID},\text{artifact ID},\text{kind},\text{locator},\text{digest},
 \text{statement},\text{premise support IDs},\text{evidence}).
\]

Artifact IDs are globally unique and at most one artifact may belong to one assertion.

## Theorem CMR2392 — PROVED

Every premise-support ID must resolve in the exact typed premise-artifact registry already
embedded in the handoff certificate. Parallel premise registries cannot be substituted by
matching IDs alone.

## Theorem CMR2393 — PROVED

A declared proved assertion must contain exactly one artifact of its required kind. A declared
open assertion must contain no handoff artifact.

## Theorem CMR2394 — PROVED

For a proved assertion, the support IDs must equal exactly the complete premise-artifact list of
its fixed premise dependencies. Citing only a subset, an extra premise or a premise outside the
assertion dependency list is rejected.

## Theorem CMR2395 — PROVED

Each assertion receives one canonical artifact-bundle digest. A proved assertion must bind
back to that bundle with

`handoff-artifact-registry://ASSERTION-ID`

and exact digest equality.

## Theorem CMR2396 — HONEST HANDOFF-ARTIFACT BOUNDARY

Exact typed linkage proves documentary composition from final premises to handoff assertions.
It does not verify a premise artifact, establish an assertion statement or prove that those
premises logically imply the assertion.

## Corollary CMR2397 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_handoff_assertion_artifact_registry.py` validates exact artifact
kinds, proved/open coverage, complete dependent-premise support and assertion-to-bundle digest
identity.

The checker was syntax-compiled locally. No genuine proved handoff-assertion artifact bank or
dependency-backed execution is claimed.
