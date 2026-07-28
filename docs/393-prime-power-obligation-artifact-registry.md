# Typed proof-artifact registry for the all-n obligation DAG

CMR2310--CMR2317 allow one opaque artifact locator and digest per proved semantic obligation.
This chapter replaces that opaque slot with an exact obligation-specific typed bundle.

## Theorem CMR2318 — PROVED AS AN INTERFACE

The nineteen fixed semantic obligations retain their exact IDs and dependency DAG. Each
obligation has a fixed ordered list of required artifact kinds. Examples include source-truth,
rule-exhaustiveness, geometry, transition, credit-routing, block-closure, state-equivalence,
rank-well-foundedness, exceptional-row and final implication artifacts.

## Theorem CMR2319 — PROVED

Every proof artifact has the canonical record

\[
(\text{artifact ID},\text{obligation ID},\text{kind},\text{locator},\text{digest},
 \text{statement},\text{support IDs},\text{evidence}).
\]

Artifact IDs are globally unique. Support IDs are sorted, duplicate-free, resolve to known
artifacts and may not contain the artifact itself.

## Theorem CMR2320 — PROVED

For a declared proved obligation, the artifact kinds must equal its fixed required kind list
exactly. A missing kind, extra kind or reordered kind is rejected.

A declared open obligation must have an empty artifact bundle. Placeholder artifacts cannot be
stored under an open obligation.

## Theorem CMR2321 — PROVED

Every obligation receives one canonical bundle record containing its required kinds, actual
artifact IDs, artifact count and complete artifact-list digest.

The bundle digest is reconstructed from the artifact records rather than supplied as an
independent assertion.

## Theorem CMR2322 — PROVED

A proved obligation in the CMR2310 closure certificate must bind back to its typed bundle by

\[
\texttt{artifact\_locator}=\texttt{artifact-registry://OBLIGATION-ID}
\]

and by exact equality between the closure artifact digest and the reconstructed bundle digest.
Thus the closure DAG cannot cite one artifact while the typed registry validates another.

## Theorem CMR2323 — PROVED

The registry publishes exact counts of artifacts, proved/open bundles, artifact-kind
multiplicities and complete artifact/bundle digests.

## Theorem CMR2324 — HONEST ARTIFACT BOUNDARY

Typed coverage proves that every declared proved obligation has the required documentary
components and that all digests compose. It does not prove any artifact statement true,
complete or mathematically sufficient.

## Corollary CMR2325 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_obligation_artifact_registry.py` validates exact typed bundle
coverage and binds every proved bundle back into the fixed closure certificate.

The checker was syntax-compiled in the publication environment. No genuine proved obligation
bundle is supplied.
