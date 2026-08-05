# Status and honesty ledger

**Last updated:** 5 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4517**. Post-ledger support artifacts do not introduce theorem identifiers. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

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

Canonical interfaces are:

```text
data/prime_power_side_four_joint_global_binding_input_manifest.json
data/prime_power_side_four_joint_binding_source_coverage_contract.json
data/prime_power_side_four_recurrent_state_population_table.json
data/prime_power_side_four_population_record_candidate.json
```

Local sample weights and coordinate labels are not installed global recurrent-state bindings.

## Explicit side-four sample backgrounds

```text
zero host = s4-fc915f89dec31fec
zero background = {(4,4),(6,5)}
old response-only selector = 2031

blocker host = s4-75b04c45c1c8eac2
blocker collision key = 02,20
blocker label = b4-8a44614df456
blocker background = {(-1,6),(-2,9)}
old response-only selector = 3012
```

The old `2031` and `3012` credit-routing artifacts remain exact historical rows, but neither response remains selected after complete-line scoring.

## Complete-line selector scoring

```text
contract = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
checker = scripts/check_prime_power_side_four_joint_sample_complete_line_selector_scores.py
```

Using

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3),
```

the zero-host response totals are

```text
2031:4  2301:0  2310:0  3012:4  3201:0  3210:4
```

and the exact complete-line minimizer face is

```text
{2301,2310,3201}.
```

The blocker-host totals are

```text
3012:5  3210:4,
```

so `3210` is the unique complete-line minimizer.

```text
joint_sample_complete_line_selector_score_tables_complete = 1
joint_sample_canonical_selectors_stable_under_complete_line_score = 0
joint_sample_complete_coupled_selector_terms_complete = 0
```

Return, collision, interface and global child-weight terms are still absent from the complete coupled selector score.

## Reoptimized return routing

```text
contract = de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6
checker = scripts/check_prime_power_side_four_reoptimized_minimizer_return_routing.py
```

For each zero candidate `2301`, `2310`, `3201`:

```text
rank-one credits = 0
rank-two credits = 0
rank-three credits = 0
return charges = {00:0,11:0,22:0,33:0}
```

Return terms preserve the three-way zero tie.

For blocker response `3210`, four rank-three credits route as

```text
03|12|21 -> return:22
03|12|30 -> return:33
03|21|30 -> return:33
12|21|30 -> return:33
```

Thus

```text
return charges = {00:0,11:0,22:1,33:3}
```

with exact classes

```text
return:22 | rank3:1,1,-3:h0:k4 | collision:02,20 -> 1
return:33 | rank3:1,1,-3:h0:k4 | collision:02,20 -> 3
```

and unresolved symbolic expression

```text
w_reopt_return_22_rank3_k4 + 3*w_reopt_return_33_rank3_k4.
```

```text
joint_sample_reoptimized_return_routing_complete = 1
zero_reoptimized_return_rows_complete = 1
blocker_reoptimized_return_row_complete = 1
reoptimized_child_weights_complete = 0
```

## Collision and interface dependency surface

```text
contract = e76551e4c6021a3c32f3536bb7891175da419c6354031104800ab58918ca977e
checker = scripts/check_prime_power_side_four_reoptimized_collision_interface_dependency.py
```

The four exact records cover

```text
zero: 2301,2310,3201
blocker: 3210
```

and retain response edges, source fate, deletion/collision key, blocker labels, target/interface provenance and CRT labels. Every response avoids target edge `01` and every deleted edge.

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

## Accounting rule

Line, geometric and return representations of one recreated credit are accounting views, not separate offspring currencies. Every physical credit is charged exactly once.

## Exact current flags

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
actual_background_profiles_complete = 0
global_child_provenance_complete = 0
compulsory_coefficients_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
complete_labelled_recurrent_lp_strict = 0
all_labelled_recurrent_blocks_subcritical = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Exact next frontier

No literal source chapter after CMR1965 has been confirmed.

```text
construct an exact collision-offspring enumerator for blocker response 3210
identify physical collision offspring and exact child keys/multiplicities
construct exact child-interface routes and multiplicities for all four candidates
preserve the three-way zero tie until complete weighted terms break it
bind the two new blocker return child classes to global states only through repository-proven population records
claim complete row strictness only after all compulsory terms, duals and weights are bound
```

If installed transition semantics are insufficient to enumerate collision offspring, record the exact semantic-input obstruction rather than assigning a zero coefficient.

## Validation status

The selector-score, reoptimized-routing and collision/interface dependency arithmetic were reproduced during construction. Their checker sources were syntax-compiled and contain mutation audits.

Complete repository execution of all new checkers has not been independently observed. The complete 77-checker runner has not been executed. Workflow success has not been observed, so CI success is not claimed.
