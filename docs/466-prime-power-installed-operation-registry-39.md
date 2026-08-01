# The installed operation registry now contains thirty-nine kinds

This chapter records CMR3138--CMR3149.

Executable checker:

```text
scripts/check_prime_power_installed_operation_registry_39.py
```

## CMR3138 — sealed predecessor registry

The extension binds the exact thirty-three-kind predecessor registry seal:

```text
5fa644a7cd340834eec7aa1776b1dcdad102749878664e3259c9be5c5a9b5ae2
```

## CMR3139 — exact new checker contract

All six level/colour operations bind contract:

```text
b97b2553cf5548cfc32a022172d2e011bc60952021d87178ae0e0fdc673ecc23
```

## CMR3140 — six unique operation identifiers

The registry adds exactly the six kinds installed in CMR3137. Duplicate identifiers, omitted entries and substituted contracts are rejected.

## CMR3141 — owner effects

Three kinds remain in the same owner and three enter factor-child owners. The complete installed bank therefore has 27 owner-changing and 12 same-owner kinds.

## CMR3142 — payment assignment

The extension assigns:

```text
owner-witness-stock: 1
scheduler-dispatch: 4
strict-child-descent: 1
```

## CMR3143 — skeleton stock

The level-skeleton restriction receives finite owner-witness stock from CMR466 rather than being treated as free state motion.

## CMR3144 — residual factor dispatch

Residual-level and colour-separated products require explicit continuation into their independent factor schedulers.

## CMR3145 — mixed-cycle dispatch

The source split and cycle-batch kinds require the mixed-cycle or conflict scheduler. They are not declared terminal or descending.

## CMR3146 — sparse-tail descent

Deleting the cyclic-boundary tails removes literal matched source/target pairs and enters strict lower-dimensional colour-separated factors.

## CMR3147 — exact census

```text
base kinds: 33
new kinds: 6
installed kinds: 39
bound contracts: 14
owner-changing kinds: 27
same-owner kinds: 12
```

Registry seal:

```text
aa7b4d1b0d7c1e7c76b8e22e547c132db5ee848c633cfc5cb45b41a76e522144
```

## CMR3148 — corruption rejection

Nine mutations are rejected, including duplicate and missing entries, false contract, empty ancestry, anonymous owner, free payment and terminal scheduler metadata.

Contract digest:

```text
92bea6f0961abd2c2c6799cd7171ff6c16a05e5cb37da9378ebe21545ace8437
```

## CMR3149 — honesty boundary

```text
installed_transition_kind_bank_39_exhaustive = 1
installed_payment_assignment_39_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The first flag applies only to the thirty-nine installed identifiers.
