# Prime-power canonical frontier roots

## Scope

This chapter removes a cross-frontier consistency hazard in the T01--T43 documentary execution stack.
The original atomic target table predates the exact T19 global-family and T20/T21 exceptional-chamber
frontiers. Later checkers therefore used scoped `corrected_roots()` contexts to replace those dependencies
during validation and to suppress obsolete special-certificate support.

The canonical structural audit is:

```text
scripts/check_prime_power_canonical_frontier_roots.py
```

The canonical final endpoint is:

```text
scripts/check_prime_power_final_support_handoff_frontiers_v2.py
```

Both remain documentary checkers and permanently report:

```text
all_n_proved_by_checker = 0
```

## CMR2648--CMR2663

### CMR2648 — fixed canonical-root registry

The audit fixes exactly three corrected atomic targets:

```text
T19_GLOBAL_FAMILY
T20_EXCEPTIONAL_ZERO_ROWS
T21_HARD_CORE_ROWS
```

No fourth target is silently rewritten.

### CMR2649 — exact T19 proof roots

The canonical proof dependencies are:

```text
T19_GLOBAL_FAMILY <- T02_RULE_EXHAUSTIVENESS, T18_ROW_THEOREMS
```

The former direct roots through T11 and T15 are not accepted as the exact T19 definition. They remain
transitive mathematical support inside T18 where appropriate, but they are not substitutes for the exact
T02 parent census and T18 final-row census.

### CMR2650 — exact T19 research root

T19 becomes research-actionable only after:

```text
T18_ROW_THEOREMS
```

T02 may be developed in parallel. Proof closure still requires both T02 and T18.

### CMR2651 — exact T20 proof roots

The zero-selector chamber target uses:

```text
T20_EXCEPTIONAL_ZERO_ROWS
  <- T05_GEOMETRY_SELECTORS
  <- T18_ROW_THEOREMS
  <- T19_GLOBAL_FAMILY
```

This means a closed chamber must be traced to exact host geometry and, for row-based modes, to the exact
final-row and parent-coverage banks.

### CMR2652 — exact T21 proof roots

The hard-core chamber target has the same exact roots:

```text
T21_HARD_CORE_ROWS
  <- T05_GEOMETRY_SELECTORS
  <- T18_ROW_THEOREMS
  <- T19_GLOBAL_FAMILY
```

The twenty hard-core chambers therefore cannot bypass the final-row or global-family layers.

### CMR2653 — exact exceptional research roots

Both chamber targets become research-actionable only after T19. This prevents a chamber disposition from
being treated as an isolated proof object before its canonical parent-to-row universe exists.

### CMR2654 — obsolete special support removed

The following legacy special-certificate bindings are suppressed for canonical execution:

```text
T19: global-family-skeleton
T20: exceptional-chamber-disposition-registry and aggregate zero-disposition digest
T21: exceptional-chamber-disposition-registry and aggregate hard-core-disposition digest
```

The exact T19--T21 frontier proof banks and their typed artifacts are the canonical support surfaces.

### CMR2655 — one-time canonical installation

Importing the audit installs the corrected dependency tuples and a stable legacy-free special-support
dispatcher once for the shared Python module graph. Every nested checker then sees the same target definitions.

The certificate schema remains version 1. Target-definition, target-result, completion and artifact-bundle
digests derived from the former roots are stale and must be regenerated.

### CMR2656 — definition-context idempotence

The older `T19.corrected_roots()` and `T20/T21.corrected_roots()` contexts are retained for compatibility.
The audit enters both contexts and requires the canonical T19--T21 target-definition records to be byte-for-
byte unchanged before, during and after the nested contexts.

### CMR2657 — special-support-context idempotence

During those same nested contexts, all three corrected targets must continue to return an empty legacy
special-support list. Exiting the contexts must not restore obsolete support.

### CMR2658 — complete DAG acyclicity

After canonical installation, both the 43-target proof dependency graph and research dependency graph must
remain topologically sortable. The correction cannot introduce a cycle or remove any frontier group.

### CMR2659 — T32 obligation census stability

T32 is derived from every pre-T22 target carrying a semantic obligation. The audit reconstructs that census
after canonical installation and requires it to match the canonical target table exactly.

The T19--T21 root correction changes ancestry and hashes, not the membership of the typed-obligation bank.

### CMR2660 — exact proof-descendant census

For each corrected root, the audit publishes every transitive proof descendant in canonical target order.
This exposes every target whose definition or result digest is affected by the correction.

### CMR2661 — exact research-descendant census

For each corrected root, the audit separately publishes every transitive research descendant. Research-start
ancestry is not conflated with proof-closure ancestry.

### CMR2662 — propagation to T43

T19, T20 and T21 must each have `T43_ROOT_IMPLICATION` as a transitive proof descendant. T19 must also have
both exceptional targets as proof and research descendants.

Thus the correction is checked across the complete endpoint rather than only inside the three local scripts.

### CMR2663 — canonical v2 endpoint

The v2 final endpoint imports and validates the canonical-root audit before loading the T32--T43 checker:

```text
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

A structural check requiring no certificate is also exposed:

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py --self-test-roots
```

The v2 wrapper reuses the existing certificate schema and proof-bank logic. It does not create T44, does not
close any mathematical target and does not prove the no-three-in-line conjecture.

## Current mathematical status

This correction strengthens dependency integrity across all current frontiers, but every genuine mathematical
blocker remains:

```text
T01--T02 source truth and genuine recurrence exhaustiveness
T03--T04 actual complete population
T05 arbitrary-n geometry coverage
T06--T18 semantic, score, rank, predicate and row theorems
T19 genuine global-family exhaustiveness
T20--T21 all 252 chamber theorems
T22--T31 all ten final premise implications
T35--T40 all six handoff arguments
T41 final mathematical review
T42 dossier sign-off
T43 the reviewed implication to D(n)=2n
```

Canonical roots and hashes do not prove any item in this list.
