# Status and honesty ledger

**Last updated:** 5 August 2026

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4517**. Post-ledger support artifacts introduce no theorem identifiers. Every checker preserves `all_n_proved_by_checker = 0`.

## Canonical installed construction stack

```text
runner = scripts/run_prime_power_installed_construction_regression_1166.py
manifest = e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d
operation kinds = 1166
checker contracts = 42
owner-changing kinds = 164
same-owner kinds = 1002
installed checkers = 77
owner/fate contract = 8f52372765f2877c48c32f417fcca27e068ac4675cc98263fd9044e30f28d828
registry contract = 383afc9477f5b52cf60f500c55f51005e4a3020dc34051a04437bdaf503a619b
registry seal = b67dc8f667a5e3e51914b8dba928825f8e8d7de0aa5a43f0e79994eca22ac18e
```

## Global binding status

The checked two-parent/seven-child binding attempt is underdetermined, not incompatible.

```text
qualifying installed recurrent-state population sources = 0
parent population records = 0
child population records = 0
candidate admission envelope = null
global binding constructed = 0
global binding incompatibility proved = 0
```

Local sample weights and coordinate labels are not installed global recurrent-state bindings.

## Complete-line selector scores

Explicit sample hosts:

```text
zero host = s4-fc915f89dec31fec
zero background = {(4,4),(6,5)}
old response-only selector = 2031

blocker host = s4-75b04c45c1c8eac2
collision key = 02,20
blocker = b4-8a44614df456
blocker background = {(-1,6),(-2,9)}
old response-only selector = 3012
```

```text
selector-score contract = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
checker = scripts/check_prime_power_side_four_joint_sample_complete_line_selector_scores.py
```

Under `K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)`:

```text
zero scores:
2031:4  2301:0  2310:0  3012:4  3201:0  3210:4
zero complete-line minimizer face = {2301,2310,3201}

blocker scores:
3012:5  3210:4
blocker complete-line minimizer = {3210}
```

Neither old selector remains stable under the declared complete-line score.

## Reoptimized return routing

```text
routing contract = de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6
checker = scripts/check_prime_power_side_four_reoptimized_minimizer_return_routing.py
```

For zero candidates `2301`, `2310`, `3201`:

```text
all recreated credit ranks = 0
return charges = {00:0,11:0,22:0,33:0}
```

Return terms preserve the three-way tie.

For blocker candidate `3210`, four rank-three credits route as:

```text
03|12|21 -> return:22
03|12|30 -> return:33
03|21|30 -> return:33
12|21|30 -> return:33
```

Therefore:

```text
return charges = {00:0,11:0,22:1,33:3}
return:22 | rank3:1,1,-3:h0:k4 | collision:02,20 -> 1
return:33 | rank3:1,1,-3:h0:k4 | collision:02,20 -> 3
weighted expression = w_reopt_return_22_rank3_k4 + 3*w_reopt_return_33_rank3_k4
```

Both child weights remain unresolved.

## Collision and interface dependency surface

```text
dependency contract = e76551e4c6021a3c32f3536bb7891175da419c6354031104800ab58918ca977e
checker = scripts/check_prime_power_side_four_reoptimized_collision_interface_dependency.py
```

The four records cover `2301`, `2310`, `3201`, and `3210`. Each retains exact response edges, fate, deletion/collision key, blockers, interface provenance, CRT label and target edge.

```text
collision dependency records = 4
interface dependency records = 4
collision coefficients populated = 0
interface coefficients populated = 0
collision child bindings populated = 0
interface child bindings populated = 0
zero tie preserved = 1
```

A blocker label or interface label is not a numerical coefficient, multiplicity or child route.

## Exact flags

```text
joint_sample_complete_line_selector_score_tables_complete = 1
joint_sample_reoptimized_return_routing_complete = 1
zero_reoptimized_return_rows_complete = 1
blocker_reoptimized_return_row_complete = 1
joint_sample_reoptimized_collision_interface_dependency_complete = 1

joint_sample_canonical_selectors_stable_under_complete_line_score = 0
reoptimized_child_weights_complete = 0
collision_coefficients_complete = 0
interface_coefficients_complete = 0
collision_child_bindings_complete = 0
interface_child_bindings_complete = 0
joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
joint_sample_global_weight_bindings_complete = 0
joint_sample_global_recurrent_compatibility_proved = 0
complete_weighted_rows_strict = 0
complete_labelled_recurrent_lp_strict = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Exact next frontier

```text
construct exact collision-offspring semantics for blocker response 3210
identify physical collision offspring and exact child keys/multiplicities
construct exact child-interface routes and multiplicities for all four candidates
preserve the zero three-way tie until complete weighted terms break it
bind global states and weights only through repository-proven population records
claim row strictness only after all compulsory terms, duals and weights are bound
```

If installed transition semantics are insufficient, record the exact semantic-input obstruction rather than assigning zero.

## Validation boundary

```text
contract arithmetic = reproduced during construction
selector-score and reoptimized-routing checker sources = syntax-checked before installation
collision/interface dependency checker source = installed; complete execution not independently observed
allowed responses, credit ownership and dependency edge sets = reconstructed during construction
mutation audits = installed in all three checkers
fresh repository clone/runtime execution = unavailable in the current container
complete 77-checker runner = not executed
workflow success = not observed
visible status entries on the latest checked head = none
```

Workflow configuration is not CI success.
