# Installed construction regression 782

This chapter chains the line-clean/return-core checker and the 782-kind registry above the 63-checker installed base.

```text
runner = scripts/run_prime_power_installed_construction_regression_782.py
base manifest = c8a579625e9fba23b4526bf3a1465df985dd1897224104cbc8e863d6873f0811
65-checker manifest = 895657e67dddbb61d802cad364656428a51f729189d5f67f2a4876830e564c38
```

## Theorem CMR4214 -- PROVED

The runner imports the canonical 714-kind runner and verifies its chained-manifest seal before extending it.

## Theorem CMR4215 -- PROVED

The imported base manifest contains exactly 63 checker entries.

## Theorem CMR4216 -- PROVED

The extension contains exactly these two entries:

```text
scripts/check_prime_power_line_clean_return_core_ancestry.py
scripts/check_prime_power_installed_operation_registry_782.py
```

## Theorem CMR4217 -- PROVED

The first extension entry is bound to contract

```text
0a1620bf756ec529255be95c072a8435d870762644908a5000418d084948aec4
```

and expected flag

```text
line_clean_return_core_ancestry_proved
```

## Theorem CMR4218 -- PROVED

The second extension entry is bound to contract

```text
b15c91825d0859a979f3953139554c2e2c81a1f68ea31d0b7d35a57437f0b946
```

and expected flag

```text
installed_transition_kind_bank_782_exhaustive
```

## Theorem CMR4219 -- PROVED

The complete chained manifest contains exactly 65 distinct checker paths and 65 distinct expected flags.

## Theorem CMR4220 -- PROVED

Every manifest contract is a lowercase 64-character SHA-256 digest.

## Theorem CMR4221 -- PROVED

The chained manifest seal is

```text
895657e67dddbb61d802cad364656428a51f729189d5f67f2a4876830e564c38
```

computed from the 63-checker base seal and the ordered two-entry extension.

## Theorem CMR4222 -- PROVED

In static-only mode every checker path is required to exist and compile, while no checker subprocess is executed.

## Theorem CMR4223 -- PROVED

In execution mode every checker must return successful JSON, the bound contract, the expected proved flag and

```text
all_n_proved_by_checker = 0
```

## Theorem CMR4224 -- PROVED

Whenever a report contains one of the new recurrent-core honesty flags, the runner requires that flag to remain zero.

## Theorem CMR4225 -- PROVED

The runner source compiles locally and its chained-manifest digest was reproduced locally.

## Theorem CMR4226 -- VALIDATION BOUNDARY

The complete 65-checker runner was not executed in the current environment. Therefore no claim is made that all inherited checker subprocesses completed successfully here.

## Theorem CMR4227 -- PROVED

The canonical installed execution surface after this extension is

```text
operation kinds = 782
checker contracts = 36
owner-changing kinds = 164
same-owner kinds = 618
installed checkers = 65
```

## Theorem CMR4228 -- PROVED

A successful future execution reports

```text
installed_transition_regression_782_complete = 1
```

only after all 65 contract and honesty checks have passed.

## Theorem CMR4229 -- HONEST ENDPOINT

The runner is an execution and regression interface. Its manifest, even when successfully executed, does not prove global transition exhaustiveness, global termination, the recurrent line-clean inequalities, the return-selector inequality, or the all-`n` conjecture.
