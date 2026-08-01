# The installed construction registry now contains Hall-wall and rollback operations

This chapter records CMR3060--CMR3071. It extends the sealed twenty-kind installed registry by the five Hall-wall and four rollback operations proved in CMR3034--CMR3059.

The executable checker is:

```text
scripts/check_prime_power_extended_installed_operation_registry.py
```

## CMR3060 — sealed predecessor registry

The extension binds the predecessor installed registry digest

```text
2e92c974075217ac510e37d72dcc4f77fbb4f5bb529d56a727eadbc7dcb70da3
```

and its twenty unique operation identifiers. The predecessor bank is not silently rewritten.

## CMR3061 — exact new contract binding

The extension binds two new executable contracts:

```text
essential-unit-wall
97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5

sparse-rollback
35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267
```

The complete extended registry references twelve construction contracts.

## CMR3062 — twenty-nine unique installed kinds

The checker verifies that the twenty predecessor kinds and nine new kinds are pairwise distinct. The resulting installed bank contains exactly twenty-nine operation kinds.

## CMR3063 — Hall-wall operation registration

The following kinds are registered with CMR727--CMR747 ancestry:

```text
essential-return-unit-wall-extraction
essential-unit-wall-factor-split
unit-wall-local-edge-deletion
unit-wall-forced-target-dispatch
unit-wall-factor-tree-split
```

## CMR3064 — rollback operation registration

The following kinds are registered with CMR439--CMR447 ancestry:

```text
minimum-rollback-restoration
cheap-rollback-certificate-escape
rollback-forced-core-contraction
rollback-recreated-conflict-support
```

## CMR3065 — exact owner effects

The nine new kinds use only theorem-derived owner effects:

```text
same owner
host owner change
factor-child owner change
restoration owner change
contraction owner change
```

Across the full twenty-nine-kind bank, twenty-three kinds change owner and six preserve owner.

## CMR3066 — complete new payment assignment

Every new kind receives exactly one payment or dispatch class:

```text
owner-witness stock       2
strict child descent      2
host-edge deletion        1
scheduler dispatch        1
edge reintroduction       2
factor contraction        1
```

The forced-target dispatch is accepted only because its continuation explicitly enters the installed target scheduler.

## CMR3067 — Hall-tree stock attachment

For initial factor side seven, the registry carries the exact installed bounds:

```text
split bound                7
node bound                15
leaf bound                 8
depth bound                7
edge stock               140
certificate stock     28,512
```

## CMR3068 — rollback stock attachment

For the sample parent side eight with `p=2,h=3`, the registry carries:

```text
per-edge rollback bound                8
whole-core restored-edge incidence    64
whole-core token incidence           384
```

## CMR3069 — corruption rejection

Ten corruptions are rejected, including duplicate kinds, collision with a predecessor kind, unknown contract, substituted digest, missing theorem ancestry, anonymous owner migration, free payment, empty dispatch, terminal dispatch and missing entry.

## CMR3070 — exact extended registry seals

The extension contract digest is:

```text
4df61b20f4d3b2bad19a296a18e00f817ac1a20feda02b77f8486783bb561487
```

The resulting extended installed registry digest is:

```text
e655f1de7ac0a67bae16907e3bd5fae105cbaf8d7d4a2c604c76b9dae2da9d2e
```

## CMR3071 — installed-bank consequence and global boundary

The checker proves only:

```text
extended_installed_transition_kind_bank_exhaustive = 1
hall_wall_operations_registered = 1
rollback_restoration_operations_registered = 1
extended_installed_payment_assignment_complete = 1
```

The permanent boundary remains:

```text
all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_returned_edge_operations_proved = 0
all_envelope_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The next audit must inspect rollback optimal-face, line-clean restoration, unavailable-edge absorption, ancestor resets and any scheduler actions not represented by the twenty-nine kinds. No all-`n` theorem is claimed.
