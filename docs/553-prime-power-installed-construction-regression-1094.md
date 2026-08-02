# Installed construction regression 1094

```text
runner = scripts/run_prime_power_installed_construction_regression_1094.py
base manifest = cb57bcbf2eb5278b8265975f948fec9970ba8539c4bc3c7e1ff12f5128d31626
75-checker manifest = ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b
```

## Theorem CMR4454 -- PROVED

The runner imports the canonical 1030-kind runner and verifies its chained-manifest seal.

## Theorem CMR4455 -- PROVED

The imported base contains exactly 73 checker entries.

## Theorem CMR4456 -- PROVED

The extension contains exactly the labelled moment/slack/assignment checker and the 1094-kind registry.

## Theorem CMR4457 -- PROVED

The ancestry checker is bound to contract `fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f` and its proved flag.

## Theorem CMR4458 -- PROVED

The registry is bound to contract `df6134106c292aa93711dcb060e013b6c6d700cc65813ae1943af2bdc8cb260f` and its installed-bank flag.

## Theorem CMR4459 -- PROVED

The complete manifest has exactly 75 distinct paths and expected flags.

## Theorem CMR4460 -- PROVED

Every bound contract is a lowercase 64-character SHA-256 digest.

## Theorem CMR4461 -- PROVED

The chained manifest `ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b` was reproduced locally.

## Theorem CMR4462 -- PROVED

Static mode compiles every checker without executing checker subprocesses.

## Theorem CMR4463 -- PROVED

Execution mode requires successful JSON, exact contract, expected flag and zero all-n claim from every checker.

## Theorem CMR4464 -- PROVED

Every manifest-population, slack-allocation, background-profile, recurrent-strictness and global honesty flag reported by the extension is required to remain zero.

## Theorem CMR4465 -- PROVED

The canonical installed surface is

```text
operation kinds = 1094
checker contracts = 41
owner-changing kinds = 164
same-owner kinds = 930
installed checkers = 75
```

## Theorem CMR4466 -- VALIDATION BOUNDARY

The source and manifest were reproduced locally. The complete 75-checker execution was not observed.

## Theorem CMR4467 -- PROVED

A future successful complete execution reports `installed_transition_regression_1094_complete = 1` only after all checks pass.

## Theorem CMR4468 -- PROVED

The runner preserves zero population, allocation, recurrent strictness, global exhaustiveness, termination and all-n claims.

## Theorem CMR4469 -- HONEST ENDPOINT

The runner is a regression interface, not proof that the labelled recurrent manifest is populated or globally strict.
