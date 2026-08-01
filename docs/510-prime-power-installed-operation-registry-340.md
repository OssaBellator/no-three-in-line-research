# The canonical installed construction registry contains 340 operation kinds

This chapter records **CMR3770--CMR3785** and extends the 286-kind registry through source theorem CMR1005.

Executable registry:

```text
scripts/check_prime_power_installed_operation_registry_340.py
```

Registry contract:

```text
00fa09f1477a15921b86289c2f4ff80abd803bf58eebf87b5dc7ff0b8dcd9ca0
```

Registry seal:

```text
d9ffac41011c852e26970444cf96c34632d5d44c29eb97c335d648d2b4485f56
```

## CMR3770 — immutable 286-kind base

```text
base registry = 5685f05669e75f18062790b2d14ccf50531d6f1c172e824603b17d946b043b69
base operation kinds = 286
base contracts = 26
base owner-changing kinds = 96
```

## CMR3771--CMR3774 — owner-transition and rollback operations

The registry adds exact restriction-face intersection, expansion embedding, intersection factorisation, canonical lost/added witnesses, core growth/shrinkage, same-value rollback, restoration-cycle erasure, monotone restriction budgets and minimum-loss ancestry.

## CMR3775--CMR3777 — lowering and complete host normalization

Installed kinds distinguish added-batch transversality, minimum-preserving peeling, added-edge core contraction, infeasible-base contraction, complete expansion normalization, arbitrary intersection normalization and fixed-vertex execution budgets.

## CMR3778--CMR3780 — induced product and coordinate-fibre transport

The bank records constant/pure/coupling decomposition, low-rank coupling boxes, finite coupling stock, residualisation, coupling deletion or contraction, coordinate-fibre selection, anchored deletion/contraction and strict pure-factor descent.

## CMR3781--CMR3782 — host-representable conditioning

Minimum-common prescription conditioning, induced contraction, one-layer residual hosts, joint residual systems, factorwise conditioning, exact potential transport and iterated representable core contraction are separate operations.

## CMR3783--CMR3784 — target handoff and robust signature operations

The registry includes two-label physical-cell cuts, finite target-handoff chains, restoration payment, bank-response dispatch, robust labelled-target cylinders, positive new-triple surplus, entering-edge assignment, basic and augmented signature stocks, four-way residual-pair stabilization and fixed-class contraction.

## CMR3785 — installed census and honesty boundary

```text
installed operation kinds = 340
bound checker contracts = 27
owner-changing kinds = 122
same-owner kinds = 218
new operation kinds = 54
rejected corruptions = 12
```

New payment counts:

```text
branch-cover-dispatch = 1
coordinate-fibre-descent = 1
cycle-erasure = 2
edge-reintroduction = 1
factor-product-dispatch = 3
history-budget = 10
local-family-equivalence = 2
local-family-restriction = 6
owner-witness-stock = 13
scheduler-dispatch = 5
strict-child-descent = 1
strict-factor-contraction = 9
```

Exact flags:

```text
installed_transition_kind_bank_340_exhaustive = 1
minimum_transition_product_target_operations_registered = 1
installed_payment_assignment_340_complete = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The registry entry banks are stored in `scripts/minimum_transition_registry_entries_a.py` and `scripts/minimum_transition_registry_entries_b.py`. Installed-bank exhaustiveness remains distinct from global construction exhaustiveness.
