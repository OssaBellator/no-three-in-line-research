# Acyclic dependency-aligned proof-artifact support

CMR2318--CMR2325 require exact typed artifact bundles but permit arbitrary support references.
This chapter makes the artifact support relation acyclic and aligns it with the fixed semantic
obligation DAG.

## Theorem CMR2350 — PROVED AS AN INTERFACE

Every support reference defines a directed edge

\[
\text{support artifact}\longrightarrow\text{supported artifact}.
\]

Both endpoints are reconstructed from the typed obligation-artifact registry; unknown and
self-support references remain rejected by the underlying registry.

## Theorem CMR2351 — PROVED

An artifact assigned to obligation `o` may cite only an artifact belonging to `o` itself or to
an obligation in the transitive dependency set of `o`. Documentary support may not flow from an
unrelated or downstream semantic module.

## Theorem CMR2352 — PROVED

The complete artifact support graph must be acyclic. The checker publishes one canonical
topological order and rejects every direct or indirect circular support chain.

## Theorem CMR2353 — PROVED

For every artifact, the checker reconstructs its direct supports, complete transitive support
closure, support depth and foundation status. A foundation artifact has no support predecessor.

## Theorem CMR2354 — PROVED

For every declared proved obligation, its complete artifact bundle must cite at least one
artifact from each immediate semantic dependency obligation. Thus exact typed coverage is also
connected documentarily to every prerequisite module.

## Theorem CMR2355 — PROVED

The certificate publishes artifact and support-edge counts, foundation count, maximum support
depth, every obligation support record and all graph, artifact and registry digests.

## Theorem CMR2356 — HONEST SUPPORT BOUNDARY

Acyclic dependency-aligned support prevents documentary circularity and disconnected proved
bundles. It does not prove that any artifact statement is true or that cited support is
mathematically sufficient.

## Corollary CMR2357 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_artifact_support_dag.py` validates admissible support obligations,
acyclicity, transitive support closures and immediate dependency-artifact coverage.

The checker was syntax-compiled in the publication environment. No genuine proved artifact DAG
is supplied.
