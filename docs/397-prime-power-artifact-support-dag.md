# Acyclic dependency-aligned proof-artifact support

CMR2318--CMR2325 require exact typed artifact bundles but a bare support-ID list does not by
itself exclude circular evidence, downstream citations or incomplete prerequisite support. This
chapter fixes one canonical support DAG with exact dependency-artifact coverage.

## Theorem CMR2350 — PROVED AS AN INTERFACE

Every support reference defines a directed edge

\[
\text{support artifact}\longrightarrow\text{supported artifact}.
\]

Both endpoints are reconstructed from the typed obligation-artifact registry. Each edge retains
both artifact IDs, both obligation IDs and whether the support remains inside one obligation.

## Theorem CMR2351 — PROVED

An artifact assigned to obligation `o` may cite only an artifact belonging to `o` itself or to
an obligation in the transitive dependency set of `o`. Documentary support may not flow from an
unrelated or downstream semantic module.

## Theorem CMR2352 — PROVED

The complete artifact support graph must be acyclic. The checker publishes one canonical
support-first topological order and rejects every direct or indirect circular support chain,
including a cycle contained inside one obligation bundle.

## Theorem CMR2353 — PROVED

For every artifact, the checker reconstructs its direct supports, complete transitive support
closure, support roots and support depth. A support root has no predecessor, and the maximum
support depth is an exact finite measure of documentary proof nesting.

## Theorem CMR2354 — PROVED

For a proved obligation `o`, let `A(d)` be the complete typed artifact bundle of an immediate
prerequisite `d`. The union of the transitive support closures of `o`'s artifacts must contain

\[
\boxed{\bigcup_{d\in D(o)} A(d).}
\]

It is not enough to cite one representative artifact from each prerequisite module: every
artifact in every immediate prerequisite bundle must be reachable.

## Theorem CMR2355 — PROVED

Every obligation receives one exact support record containing its immediate dependencies,
local artifact IDs, required dependency-artifact IDs, reachable dependency artifacts, missing
artifacts and complete bundle-support closure. The certificate publishes exact edge, root,
depth and proved-bundle coverage counts plus all graph and record digests.

## Theorem CMR2356 — HONEST SUPPORT BOUNDARY

Acyclic dependency-aligned support proves noncircular documentary composition. It does not prove
that a support citation is logically sufficient, that any artifact statement is true, or that
the genuine mathematical recurrence has been established.

## Corollary CMR2357 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_obligation_artifact_support_dag.py` is the canonical exact-coverage
checker. `scripts/check_prime_power_artifact_support_dag.py` is a compatibility entrypoint that
delegates to the same implementation rather than maintaining a weaker second algorithm.

The canonical checker was syntax-compiled and its graph logic was exercised on empty,
valid-chain, missing-support, downstream-support and cyclic-support fixtures. No genuine proved
artifact DAG is supplied.
