# Typed artifacts for the ten final implication premises

CMR2342--CMR2349 accept one opaque proof artifact per final implication premise. This chapter
replaces those opaque pairs with exact premise-specific typed bundles linked to the semantic
obligation artifacts.

## Theorem CMR2358 — PROVED AS AN INTERFACE

Each of the ten fixed final implication premises has one fixed required artifact kind, including
base-domain, recurrence-exhaustiveness, invariant, operation-selection, resource-credit,
contraction, cross-block, exceptional, termination and objective-translation proofs.

## Theorem CMR2359 — PROVED

A premise artifact records

\[
(\text{premise},\text{artifact ID},\text{kind},\text{locator},\text{digest},
 \text{statement},\text{support IDs},\text{finite-certificate binding},\text{evidence}).
\]

Artifact IDs are unique and every support ID resolves to a typed semantic-obligation artifact.

## Theorem CMR2360 — PROVED

A declared proved premise contains exactly one artifact of its required kind. A declared open
premise contains no premise artifact.

## Theorem CMR2361 — PROVED

The premise artifact must cite at least one semantic artifact from every obligation on which
that premise depends. Hence a premise cannot be documented independently of the proof modules
that make it effective.

## Theorem CMR2362 — PROVED

If the termination premise uses proof mode `edgewise-lex`, its premise artifact must bind the
exact CMR2334--CMR2341 edgewise certificate SHA. Semantic multiset or well-founded modes must
not claim that finite edgewise binding.

## Theorem CMR2363 — PROVED

Every proved premise binds back to its reconstructed bundle by the canonical locator

`premise-artifact-registry://PREMISE-ID`

and exact equality of its stored artifact digest with the bundle digest.

## Theorem CMR2364 — HONEST PREMISE BOUNDARY

Typed premise coverage proves exact documentary composition. It does not verify the premise
statement or establish that the cited semantic artifacts logically imply it.

## Corollary CMR2365 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_premise_artifact_registry.py` validates exact premise kinds,
semantic-artifact support, edgewise binding where applicable and premise-to-bundle digest
identity.

The checker was syntax-compiled in the publication environment. No genuine proved premise
bundle is supplied.
