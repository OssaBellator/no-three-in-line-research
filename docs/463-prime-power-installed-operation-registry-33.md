# The installed construction registry now contains thirty-three operation kinds

This chapter records CMR3098--CMR3109. It extends the twenty-nine-kind registry by the four CMR448--CMR461 optimal-face and SCC operations.

The executable checker is:

```text
scripts/check_prime_power_installed_operation_registry_33.py
```

## CMR3098 — sealed twenty-nine-kind predecessor

The extension binds the predecessor registry digest

```text
e655f1de7ac0a67bae16907e3bd5fae105cbaf8d7d4a2c604c76b9dae2da9d2e
```

and its exact count of twenty-nine installed kinds and twelve contracts.

## CMR3099 — exact optimal-face contract binding

The new operations are bound to:

```text
scripts/check_prime_power_rollback_optimal_face_scc_ancestry.py
1281001711d4312dd98b8434e20dffb226b0608a893ffe5cf13f8b8e13940feb
```

## CMR3100 — minimum-cost face restriction kind

`rollback-minimum-cost-face-restriction` remains at the restoration owner and requires continuation into the tight-host/SCC scheduler. It is not labelled as descent.

## CMR3101 — tight-host restriction kind

`rollback-tight-host-restriction` removes positive reduced-cost excursions while preserving exactly the minimum rollback family. It also requires SCC scheduler continuation.

## CMR3102 — SCC factor split kind

`rollback-optimal-scc-factor-split` changes to factor-child ownership. Because one SCC may still occupy the whole host, the registry records a mandatory rollback-free/small-block/active-level scheduler instead of claiming unconditional strict descent.

## CMR3103 — marked ancestor-reset kind

`marked-ancestor-reset-optimal-face` preserves the current marked-reset owner and spends the finite marked witness structure by normalizing to one canonical tight face.

## CMR3104 — thirty-three unique kinds

The predecessor kinds and four new identifiers are pairwise distinct. The complete installed count is exactly thirty-three.

## CMR3105 — thirteen bound contracts

The installed bank now references thirteen exact construction contracts.

## CMR3106 — owner-effect census

Across the thirty-three kinds:

```text
owner-changing kinds = 24
same-owner kinds = 9
```

The new SCC split is the only additional owner-changing kind.

## CMR3107 — payment and dispatch honesty

The four new kinds receive:

```text
scheduler dispatch = 3
owner-witness stock = 1
```

Every dispatch string names the next scheduler. Empty or terminal continuations are rejected.

## CMR3108 — registry seal and corruption rejection

The checker rejects nine independent corruptions. Its contract digest and resulting registry digest are:

```text
5f9d98c0b964f207fc4ac2d493b51fef5c3caaccf1464cf8bd351a477af93583
5fa644a7cd340834eec7aa1776b1dcdad102749878664e3259c9be5c5a9b5ae2
```

## CMR3109 — installed-bank consequence and global boundary

The checker proves:

```text
installed_transition_kind_bank_33_exhaustive = 1
rollback_optimal_face_operations_registered = 1
installed_payment_assignment_33_complete = 1
```

It does not prove:

```text
all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The next operation audit begins with CMR462--CMR521: level skeletons, colour-separated factors, mixed-cycle/fan operations, line-clean restoration, unavailable-edge absorption and temporal reintroduction. No all-`n` theorem is claimed.
