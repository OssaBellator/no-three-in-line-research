# Installed construction regression 974

```text
runner = scripts/run_prime_power_installed_construction_regression_974.py
base manifest = f8ab06f6f46e08b91b425c10e53c55779e66be9acea6bbc0017d7216130f4857
71-checker manifest = 58a5c6eaa877331a9c4711835d9a3ce84c9def64001eea9ffb301325b7620be5
```

## Theorem CMR4358 -- PROVED

The runner imports the canonical 902-kind runner and verifies its chained-manifest seal.

## Theorem CMR4359 -- PROVED

The imported base contains exactly 69 checker entries.

## Theorem CMR4360 -- PROVED

The extension contains exactly the rank-mass/multiplicity checker and 974-kind registry.

## Theorem CMR4361 -- PROVED

The ancestry checker is bound to contract `681a56e37003368e62a92ae7df349488e03e03eec34c2cddf2ab39b8d6622bdd` and its proved flag.

## Theorem CMR4362 -- PROVED

The registry is bound to contract `5bff249b3ada147307677bb59979f034b1c2587c4cc0a8643b903dbcd6eaf96e` and its installed-bank flag.

## Theorem CMR4363 -- PROVED

The complete manifest has exactly 71 distinct paths and flags.

## Theorem CMR4364 -- PROVED

Every bound contract is a lowercase 64-character SHA-256 digest.

## Theorem CMR4365 -- PROVED

The chained manifest `58a5c6eaa877331a9c4711835d9a3ce84c9def64001eea9ffb301325b7620be5` was reproduced locally.

## Theorem CMR4366 -- PROVED

Static mode compiles every checker without subprocess execution.

## Theorem CMR4367 -- PROVED

Execution mode requires successful JSON, exact contract, expected flag and zero all-n claim from every checker.

## Theorem CMR4368 -- PROVED

Every conditional closure and global honesty flag reported by the extension is required to remain zero.

## Theorem CMR4369 -- PROVED

The canonical installed surface is

```text
operation kinds = 974
checker contracts = 39
owner-changing kinds = 164
same-owner kinds = 810
installed checkers = 71
```

## Theorem CMR4370 -- VALIDATION BOUNDARY

The source and manifest were reproduced locally. The complete 71-checker execution was not observed.

## Theorem CMR4371 -- PROVED

A future successful complete execution reports `installed_transition_regression_974_complete = 1` only after all checks pass.

## Theorem CMR4372 -- PROVED

The runner preserves zero global closure, exhaustiveness, termination and all-n claims.

## Theorem CMR4373 -- HONEST ENDPOINT

The runner is a regression interface, not proof that all multiplicity or support hypotheses hold globally.
