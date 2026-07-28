# Typed artifacts for the ten final implication premises

CMR2342--CMR2349 give each final premise an opaque locator/digest pair. This chapter replaces
that pair with one exact premise-specific artifact bundle linked to the semantic-obligation
artifacts on which the premise depends.

## Theorem CMR2374 — PROVED AS AN INTERFACE

Each of the ten fixed implication premises has one fixed required artifact kind, from
`base-case-domain-proof` through `objective-translation-proof`.

A premise artifact has the canonical record

\[
(\text{premise ID},\text{artifact ID},\text{kind},\text{locator},\text{digest},
 \text{statement},\text{obligation support IDs},\text{finite certificate},\text{evidence}).
\]

## Theorem CMR2375 — PROVED

Artifact IDs are globally unique and at most one artifact may belong to each premise. Every
support ID must resolve to a typed artifact in the exact obligation-artifact registry used by
the final premise contract.

## Theorem CMR2376 — PROVED

A declared proved premise must have exactly one artifact of its required kind. A declared open
premise must have no premise artifact. Missing, extra and placeholder artifacts are rejected.

## Theorem CMR2377 — PROVED

For every proved premise, the cited obligation artifacts must include at least one artifact
from every semantic obligation in the premise's exact dependency list.

Thus premise-level prose cannot cite only a convenient subset of its closed semantic modules.

## Theorem CMR2378 — PROVED

When the termination premise uses `edgewise-lex`, its artifact must bind the exact
CMR2334--CMR2341 edgewise certificate SHA. All other premise modes require a null finite-
certificate field.

## Theorem CMR2379 — PROVED

Each premise receives a canonical artifact-bundle digest. A proved premise in the contract must
use

\[
\texttt{premise-artifact-registry://PREMISE-ID}
\]

and must cite the reconstructed bundle digest exactly.

## Theorem CMR2380 — HONEST PREMISE-ARTIFACT BOUNDARY

Exact typed linkage proves documentary coverage from semantic obligations to final premises. It
does not prove the cited obligation artifacts true, prove the premise statement, or verify that
one cited artifact per dependency is logically sufficient.

## Corollary CMR2381 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_premise_artifact_registry.py` validates exact premise-artifact
coverage, dependency-artifact citations, optional finite-certificate binding and contract
digest equality.

The committed schema was audited in the publication environment. No genuine proved premise
artifact bank or dependency-backed execution is claimed.
