# Installed construction regression 1166

```text
runner = scripts/run_prime_power_installed_construction_regression_1166.py
base manifest = ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b
77-checker manifest = e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d
```

## Theorem CMR4502 -- PROVED

The runner imports the canonical 1094-kind runner and verifies its chained-manifest seal.

## Theorem CMR4503 -- PROVED

The imported base contains exactly 75 checker entries.

## Theorem CMR4504 -- PROVED

The extension contains exactly the owner/fate-lineage-kernel checker and the 1166-kind registry.

## Theorem CMR4505 -- PROVED

The ancestry checker is bound to contract `8f52372765f2877c48c32f417fcca27e068ac4675cc98263fd9044e30f28d828` and flag `owner_fate_lineage_kernel_ancestry_proved`.

## Theorem CMR4506 -- PROVED

The registry is bound to contract `383afc9477f5b52cf60f500c55f51005e4a3020dc34051a04437bdaf503a619b` and flag `installed_transition_kind_bank_1166_exhaustive`.

## Theorem CMR4507 -- PROVED

The complete manifest has exactly 77 distinct checker paths and expected flags.

## Theorem CMR4508 -- PROVED

Every bound contract is a lowercase 64-character SHA-256 digest.

## Theorem CMR4509 -- PROVED

The chained manifest `e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d` was reproduced locally from the 75-checker base and ordered two-entry extension.

## Theorem CMR4510 -- PROVED

Static mode requires every checker path to exist and compile without executing checker subprocesses.

## Theorem CMR4511 -- PROVED

Execution mode requires successful JSON, exact contract binding, the expected proved flag and `all_n_proved_by_checker = 0` for every checker.

## Theorem CMR4512 -- PROVED

Every owner/fate population, compulsory-certificate, raw-lineage, blocker-resolution, recurrent-strictness and global honesty flag reported by the extension is required to remain zero.

## Theorem CMR4513 -- PROVED

The canonical installed surface is

```text
operation kinds = 1166
checker contracts = 42
owner-changing kinds = 164
same-owner kinds = 1002
installed checkers = 77
```

## Theorem CMR4514 -- VALIDATION BOUNDARY

The complete owner/fate checker, registry contract/census/seal and chained runner manifest were reproduced locally. The complete 77-checker execution was not observed.

## Theorem CMR4515 -- PROVED

A future successful complete execution reports `installed_transition_regression_1166_complete = 1` only after all 77 contract, flag and honesty checks pass.

## Theorem CMR4516 -- PROVED

The runner preserves zero population, certificate-completeness, raw-lineage, blocker-resolution, recurrent strictness, global exhaustiveness, termination and all-n claims.

## Theorem CMR4517 -- HONEST ENDPOINT

The runner is a regression interface, not proof that every recurrent state has a complete compulsory weighted row or that every raw-fibre blocker is globally resolved.
