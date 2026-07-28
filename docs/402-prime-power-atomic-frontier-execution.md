# Atomic execution manifest for every current all-n frontier

The status ledger identifies thirteen genuine mathematical frontiers. They range from source
truth and real population through geometry, transition semantics, recurrent blocks, exceptional
closure, proof-artifact support, final premises and the root implication. This chapter replaces
that prose-only list with one exact executable target system.

## Theorem CMR2390 — PROVED AS AN INTERFACE

The checker fixes exactly thirteen frontier groups and forty-three atomic proof targets. Every
target has a permanent ID, title, required artifact kind and one frontier owner. Supplied input
cannot add, remove, rename or reorder targets.

The target system covers source truth, rule exhaustiveness, genuine population, geometry and
policy, transition/resource/credit semantics, recurrent blocks, auxiliary expansions,
cross-block semantics, interface/rank arguments, typed proof support, global-family
exhaustiveness, exceptional/hard-core closure, the ten final premises, six induction-handoff
assertions, the seven-gate dossier audit and the root implication.

## Theorem CMR2391 — PROVED

Each target has two exact dependency lists:

1. a **research-start dependency list**, describing which earlier results are needed before that
   work package can be attacked non-vacuously; and
2. a **proof-closure dependency list**, describing which targets must be complete before the
   target may be declared proved.

Both directed graphs are code-defined and acyclic. This distinguishes useful parallel research
from formal proof closure instead of forcing every frontier into one artificial serial order.

## Theorem CMR2392 — PROVED

The atomic targets cover each existing external proof gate exactly once:

- all nineteen semantic obligations;
- all ten final implication premises;
- all six induction-handoff assertions; and
- the final dossier-integrity gate.

The root target is bound specifically to `GLOBAL_QUOTIENT_IMPLIES_ALL_N`. Missing, duplicated or
extraneous external-gate coverage is rejected by the definition self-test.

## Theorem CMR2393 — PROVED

Every target has one canonical completion record

\[
(\text{target ID},\text{status},\text{artifact locator},\text{artifact digest},\text{note}).
\]

A proved target requires nonempty artifact fields. An open target requires null artifact fields
and a nonempty blocker note. Completion records occur in exact target order and carry canonical
digests.

## Theorem CMR2394 — PROVED

A target becomes effectively complete only when

\[
\boxed{
\text{declared proved}
\land
\text{every proof dependency complete}
\land
\text{every linked external gate satisfied}.
}
\]

For targets bound to a semantic obligation, final premise, handoff assertion or the dossier gate,
the declared status must agree exactly with the corresponding existing certificate. Thus the new
frontier ledger cannot claim completion independently of the authoritative closure stack.

## Theorem CMR2395 — PROVED

The checker publishes two exact schedules:

- the current **research-actionable** target set and earliest research-start wave; and
- the current **proof-actionable** target set, earliest proof-completion wave, canonical longest
  open dependency chain and downstream unclosed impact.

Each frontier record publishes its complete, open, research-actionable and proof-actionable
targets. The root target's wave is the minimum number of dependency stages remaining under the
one-target-per-wave abstraction; it is not a time or difficulty estimate.

## Theorem CMR2396 — HONEST EXECUTION BOUNDARY

Exact target coverage and scheduling do not prove any mathematical statement, estimate research
difficulty or imply that a cited artifact is true or sufficient. A target marked complete remains
subject to ordinary mathematical review through the existing semantic, premise, handoff and root
proof layers.

The checker permanently publishes

\[
\boxed{\texttt{all\_n\_proved\_by\_checker}=0.}
\]

## Corollary CMR2397 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_atomic_frontier_execution.py` validates the fixed thirteen-frontier,
forty-three-target manifest, exact external-gate coverage, both acyclic dependency graphs,
canonical target records, completion synchronization, research/proof schedules and the final
root work chain.

The `--self-test` mode checks the complete code-defined manifest without requiring a certificate.
It reports thirteen frontiers, forty-three targets and complete topological coverage of both
dependency graphs. No genuine frontier target is claimed complete by this chapter.
