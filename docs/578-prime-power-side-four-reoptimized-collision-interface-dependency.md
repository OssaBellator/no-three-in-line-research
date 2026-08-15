# Collision and interface dependencies on the reoptimized sample responses

This post-ledger support artifact records the exact locally available collision and interface inputs for the four reoptimized candidate responses. It introduces no theorem identifier after CMR4517.

```text
contract = data/prime_power_side_four_reoptimized_collision_interface_dependency.json
contract seal = e76551e4c6021a3c32f3536bb7891175da419c6354031104800ab58918ca977e
checker = scripts/check_prime_power_side_four_reoptimized_collision_interface_dependency.py
```

## Candidate records

```text
zero host: 2301, 2310, 3201
blocker host: 3210
```

Every record contains the exact response edges, source fate, deletion/collision trace, blocker labels, local interface label and provenance, CRT label, and target edge. Every candidate avoids both the forbidden target edge `01` and all deleted host edges.

## Collision boundary

Known local inputs are:

```text
source fate
collision/deletion key
contained blocker labels
response edges
```

Still missing for every record:

```text
exact collision-offspring enumeration
collision coefficient rule
collision child key
collision child weight
global transition-occurrence provenance
```

The blocker key `02,20` and blocker label `b4-8a44614df456` are structural labels. They are not numerical collision coefficients.

## Interface boundary

Known local inputs are:

```text
side4-target01 interface label
sample-local interface provenance
CRT-not-applied sample label
target edge 01
response edges
```

Still missing for every record:

```text
child-interface route
interface coefficient rule
interface multiplicity
interface child key
interface child weight
factor-tuple provenance
global transition-occurrence provenance
```

A local interface label is not itself a child route or multiplicity.

## Current census

```text
candidate responses = 4
collision dependency records = 4
interface dependency records = 4
collision coefficients populated = 0
interface coefficients populated = 0
collision child bindings populated = 0
interface child bindings populated = 0
zero-host tie preserved = 1
```

## Honesty boundary

```text
joint_sample_reoptimized_collision_interface_dependency_complete = 1

collision_coefficients_complete = 0
interface_coefficients_complete = 0
collision_child_bindings_complete = 0
interface_child_bindings_complete = 0
joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
global_binding_constructed = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker reconstructs every response edge set and includes seventeen corruption cases. Complete repository execution and workflow success remain separate validation steps.