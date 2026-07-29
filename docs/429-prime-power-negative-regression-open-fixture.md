# Prime-power negative regression and all-open target fixture

## Scope

This chapter strengthens the branch-wide T01--T43 regression in two ways:

```text
scripts/test_prime_power_current_frontier_regression.py
scripts/check_prime_power_all_open_target_fixture.py
```

The first proves that the validator rejects deliberate source and subprocess corruptions. The second exercises
all forty-three canonical target definitions and open completion records without supplying any proof artifact.
Both are validation infrastructure only and permanently report or preserve:

```text
all_n_proved_by_checker = 0
```

## CMR2676--CMR2691

### CMR2676 — negative regression harness

A standard-library `unittest` harness now tests the regression helpers independently of the happy-path branch
run. The workflow executes it before the complete regression runner.

### CMR2677 — pure target/frontier validator

The exact target-table checks are factored into `validate_target_frontier_literals`. Tests can mutate parsed
literal values directly without importing or rewriting the atomic checker module.

### CMR2678 — missing-target rejection

Deleting any row from the literal target bank must fail the exact forty-three-target census.

### CMR2679 — sequential identity rejection

Duplicating a target ID or breaking the `T01` through `T43` sequential prefix rule must fail before any
certificate logic runs.

### CMR2680 — frontier corruption rejection

Unknown frontier references, missing frontier groups and empty frontier titles are rejected. Every one of the
thirteen frontier groups must own at least one target.

### CMR2681 — endpoint honesty rejection

A canonical endpoint source that loses the literal `all_n_proved_by_checker` marker fails the regression.
This checks retention of the honesty boundary, not the validity of any mathematical proof.

### CMR2682 — endpoint syntax rejection

A canonical endpoint carrying invalid Python syntax is rejected even when its honesty marker is still present.

### CMR2683 — document synchronisation rejection

The document helper is mutation-tested by removing a required CMR or honesty marker and requiring failure.

### CMR2684 — failing subprocess rejection

A structural self-test returning nonzero is rejected with its command, standard output and standard error
captured for diagnosis.

### CMR2685 — silent subprocess rejection

A self-test returning zero but producing no output is rejected. Successful execution must leave an explicit,
reviewable structural summary.

### CMR2686 — successful subprocess recording

A successful test is required to preserve its script, argument, output and zero return code in the regression
result bank.

### CMR2687 — canonical all-open fixture

The fixed fixture installs the canonical T19--T21 roots and reconstructs all forty-three target-definition
records in canonical order.

### CMR2688 — exact open completion bank

For every target the fixture reconstructs one completion record with:

```text
status = open
artifact_locator = null
artifact_digest = null
```

No proof locator, digest or artifact is fabricated.

### CMR2689 — fixture honesty claims

The fixture requires exactly thirteen frontiers, forty-three targets, forty-three open targets, zero proved
targets and `fixture_contains_mathematical_proofs = 0`.

### CMR2690 — fixture mutation bank

The fixture self-test rejects seven mutations:

```text
missing target completion
premature proved status
nonnull open artifact locator
missing target definition
canonical-root digest drift
honesty-claim flip
certificate-digest corruption
```

### CMR2691 — continuous negative validation

The Python 3.10 and 3.12 workflow now runs the mutation harness before the complete branch regression. The
complete runner also executes the all-open fixture self-test alongside both canonical-root self-tests.

A passing mutation suite proves only that these validator failures are detected. It does not prove any T01--T43
mathematical statement.

## Current mathematical status

All genuine blockers remain unchanged:

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
