# Installed construction regression 1030

```text
runner = scripts/run_prime_power_installed_construction_regression_1030.py
base manifest = 58a5c6eaa877331a9c4711835d9a3ce84c9def64001eea9ffb301325b7620be5
73-checker manifest = cb57bcbf2eb5278b8265975f948fec9970ba8539c4bc3c7e1ff12f5128d31626
```

## Theorem CMR4406 -- PROVED

The runner imports the canonical 974-kind runner and verifies its chained-manifest seal.

## Theorem CMR4407 -- PROVED

The imported base contains exactly 71 checker entries.

## Theorem CMR4408 -- PROVED

The extension contains exactly the geometric-fibre/outer-assignment checker and the 1030-kind registry.

## Theorem CMR4409 -- PROVED

The ancestry checker is bound to contract `f03ab61fabb4ad8727f239a31474466f3074f2397762a63fd4255c683176e3eb` and its proved flag.

## Theorem CMR4410 -- PROVED

The registry is bound to contract `c93c2c8d69260ecc2c2c4b0709af26c16a9c054b2ec7f85f4cea83a36dcb8084` and its installed-bank flag.

## Theorem CMR4411 -- PROVED

The complete manifest has exactly 73 distinct paths and expected flags.

## Theorem CMR4412 -- PROVED

Every bound contract is a lowercase 64-character SHA-256 digest.

## Theorem CMR4413 -- PROVED

The chained manifest `cb57bcbf2eb5278b8265975f948fec9970ba8539c4bc3c7e1ff12f5128d31626` was reproduced locally.

## Theorem CMR4414 -- PROVED

Static mode compiles every checker without executing checker subprocesses.

## Theorem CMR4415 -- PROVED

Execution mode requires successful JSON, exact contract, expected flag and zero all-n claim from every checker.

## Theorem CMR4416 -- PROVED

Every geometric-fibre completeness, unified strictness and global honesty flag reported by the extension is required to remain zero.

## Theorem CMR4417 -- PROVED

The canonical installed surface is

```text
operation kinds = 1030
checker contracts = 40
owner-changing kinds = 164
same-owner kinds = 866
installed checkers = 73
```

## Theorem CMR4418 -- VALIDATION BOUNDARY

The source and manifest were reproduced locally. The complete 73-checker execution was not observed.

## Theorem CMR4419 -- PROVED

A future successful complete execution reports `installed_transition_regression_1030_complete = 1` only after all checks pass.

## Theorem CMR4420 -- PROVED

The runner preserves zero provenance-completeness, recurrent strictness, global exhaustiveness, termination and all-n claims.

## Theorem CMR4421 -- HONEST ENDPOINT

The runner is a regression interface, not proof that every coordinate-labelled geometric fibre has been populated or certified strict.
