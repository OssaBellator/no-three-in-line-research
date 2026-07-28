# Atomic execution schedule for all current proof frontiers

The status ledger names thirteen genuine mathematical frontiers. This chapter refines them into
forty-three exact proof targets, separates proof-closure dependencies from dependencies needed
to begin useful research, and binds completed targets to the existing semantic, premise,
handoff and dossier gates.

## Theorem CMR2406 — PROVED AS AN INTERFACE

The checker fixes exactly thirteen frontier groups and forty-three atomic targets. Every target
has:

- one frontier ID and title;
- one required artifact kind;
- exact proof-dependency target IDs;
- exact research-start dependency target IDs;
- zero or more linked semantic obligations, final premises or handoff assertions; and
- an optional final-dossier gate.

## Theorem CMR2407 — PROVED

Both target dependency graphs are checked independently for acyclicity. Every target ID is
unique, every dependency resolves and self-dependencies are rejected.

The semantic bindings cover all nineteen closure obligations exactly once. The premise bindings
cover all ten final premises exactly once, and the assertion bindings cover all six induction-
handoff assertions exactly once. Exactly one target is bound to the final dossier gate.

## Theorem CMR2408 — PROVED

Every target has one canonical completion record with status `proved` or `open`, an artifact
locator/digest pair when proved and one note. A linked target's declared status must equal the
state of its exact external obligation, premise, assertion or dossier gate.

A target cannot become effectively complete before all proof dependencies are complete.

## Theorem CMR2409 — PROVED

For every incomplete target, the checker computes:

- its open proof dependencies;
- earliest parallel proof-completion wave; and
- one canonical longest open proof-dependency chain.

The root target `T43_ROOT_IMPLICATION` therefore receives an exact dependency-wave depth over
the fixed target graph.

## Theorem CMR2410 — PROVED

A separate research-start schedule uses the weaker research-dependency graph. It publishes the
currently research-actionable targets and the earliest research-start wave for every target.

Thus work may begin on a target before all dependencies needed for mathematical closure are
finished, without misclassifying that target as proved.

## Theorem CMR2411 — PROVED

Every frontier record publishes its complete, completed, open, research-actionable and
proof-actionable target sets, together with the maximum number of downstream unclosed targets
blocked by one target in that frontier.

The complete certificate also publishes exact target, schedule, frontier and completion
digests.

## Theorem CMR2412 — HONEST EXECUTION BOUNDARY

The atomic schedule is documentary planning arithmetic. A completion locator/digest is not a
typed proof-artifact validation and the checker does not verify mathematical truth, proof
difficulty, elapsed time or logical sufficiency. It permanently publishes
`all_n_proved_by_checker = 0`.

## Corollary CMR2413 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_atomic_frontier_execution.py` validates the fixed thirteen-frontier,
forty-three-target system, exact external-gate bindings and both parallel schedules.

Its committed schema and dependency definitions were audited in the publication environment.
The dependency-backed certificate suite and `--self-test` mode were not executed here, and no
frontier completion or all-`n` proof is claimed.
