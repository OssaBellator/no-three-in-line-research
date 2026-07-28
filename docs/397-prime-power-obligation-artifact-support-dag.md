# Noncircular dependency support for typed proof artifacts

CMR2318--CMR2325 type every proof-artifact bundle, but a bare support-ID list does not by itself
exclude circular evidence or citations from unrelated downstream obligations. This chapter adds
the exact support graph required before the typed registry can serve as a noncircular proof
dossier.

## Theorem CMR2350 — PROVED AS AN INTERFACE

For every typed proof artifact, the checker reconstructs one directed edge

\[
\boxed{a\longrightarrow b}
\]

when artifact `b` lists artifact `a` as direct support. Every edge retains both artifact IDs,
both obligation IDs and whether the support remains inside one obligation.

## Theorem CMR2351 — PROVED

A support edge is admissible only when its supporting artifact belongs either to the same
semantic obligation or to a transitive prerequisite obligation in the fixed nineteen-node DAG.

Thus an artifact may not use an unrelated or downstream proof module as evidence for an earlier
module.

## Theorem CMR2352 — PROVED

The complete artifact-support graph must be acyclic. The checker computes a canonical
support-first topological order and rejects every directed support cycle, including cycles
contained inside one obligation bundle.

## Theorem CMR2353 — PROVED

For every artifact, the checker publishes its exact direct support set, transitive support
closure, support roots and support depth. The maximum support depth is therefore an exact finite
measure of documentary proof nesting.

## Theorem CMR2354 — PROVED

For a proved obligation `o`, let `A(d)` be the complete typed artifact bundle of an immediate
prerequisite `d`. The union of the transitive support closures of `o`'s artifacts must contain

\[
\boxed{\bigcup_{d\in D(o)} A(d).}
\]

A proved module therefore cannot merely have closed prerequisites in the obligation ledger; its
own artifact bundle must actually support every artifact in each immediate prerequisite bundle.

## Theorem CMR2355 — PROVED

Every obligation receives one exact support record containing its immediate dependencies,
local artifact IDs, required dependency-artifact IDs, reachable dependency artifacts, missing
artifacts and complete bundle-support closure. All graph, record and topological-order digests
are reconstructed.

## Theorem CMR2356 — HONEST SUPPORT BOUNDARY

Acyclic dependency-aligned support proves noncircular documentary composition. It does not prove
that a support citation is logically sufficient, that any artifact statement is true, or that
the genuine mathematical recurrence has been established.

## Corollary CMR2357 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_obligation_artifact_support_dag.py` validates support-edge alignment,
rejects cycles, computes exact support closures and requires complete immediate-dependency
artifact support for every declared proved obligation.

The checker was syntax-compiled and its graph logic was exercised on empty, valid-chain,
missing-support, downstream-support and cyclic-support fixtures. No genuine proved artifact
bundle is claimed.
