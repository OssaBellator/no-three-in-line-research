# Autoprompter continuity handoff

## Repository and branch

```text
repository = OssaBellator/no-three-in-line-research
branch = research/all-n-composite-modulus
project branch role = independent all-n composite modulus line
main focus elsewhere = alternating core
```

The no-three-in-line conjecture remains open. Preserve `all_n_proved_by_checker = 0`.

## Canonical installed construction surface

```text
operation kinds = 1166
checker contracts = 42
installed checkers = 77
runner manifest = e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d
owner/fate contract = 8f52372765f2877c48c32f417fcca27e068ac4675cc98263fd9044e30f28d828
registry contract = 383afc9477f5b52cf60f500c55f51005e4a3020dc34051a04437bdaf503a619b
```

Installed honesty remains:

```text
owner_fate_rows_populated_all_recurrent_states = 0
compulsory_weighted_certificates_complete = 0
actual_global_parent_rule_complete = 0
complete_labelled_recurrent_lp_strict = 0
all_n_proved_by_checker = 0
```

## Two explicit sample rows

### Zero-response sample

```text
host = s4-fc915f89dec31fec
response-only selector = 2031
background = {(4,4),(6,5)}
rank totals on 2031 = (2,2,0)
return charges on 2031 = {00:1,22:3}
```

### Blocker-alternative sample

```text
host = s4-75b04c45c1c8eac2
collision key = 02,20
blocker = b4-8a44614df456
response-only selector = 3012
background = {(-1,6),(-2,9)}
rank totals on 3012 = (2,2,1)
return charges on 3012 = {00:1,11:3,33:1}
```

The existing joint compatibility unit has seven exact child classes. One local alias collision is preserved: the two `w_return_00_rank1` occurrences have different full child keys and must never be merged globally.

The local witness with both parent weights 16 and all seven child weights 1 proves only simultaneous return-only local feasibility. It is not an installed global Lyapunov vector.

## Global binding status

The checked global binding attempt remains underdetermined:

```text
checked_global_binding_attempt_complete = 1
global_binding_constructed = 0
global_binding_incompatibility_proved = 0
joint_sample_global_weight_bindings_complete = 0
joint_sample_global_recurrent_compatibility_proved = 0
```

Canonical population interfaces:

```text
data/prime_power_side_four_joint_global_binding_input_manifest.json
data/prime_power_side_four_joint_binding_source_coverage_contract.json
data/prime_power_side_four_recurrent_state_population_table.json
data/prime_power_side_four_population_record_candidate.json
```

Current population state:

```text
qualifying installed population sources = 0
parent records populated = 0
child records populated = 0
candidate = null
candidate admissible = 0
binding_input_population_complete = 0
```

Do not invent recurrent-state keys, installed weights, transition provenance, normalization witnesses or recurrent-block witnesses merely to populate these interfaces.

## Newly completed complete-line selector score unit

```text
contract = data/prime_power_side_four_joint_sample_complete_line_selector_scores.json
contract seal = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
checker = scripts/check_prime_power_side_four_joint_sample_complete_line_selector_scores.py
documentation = docs/576-prime-power-side-four-joint-sample-complete-line-selector-scores.md
workflow = .github/workflows/side-four-joint-sample-complete-line-selector-scores.yml
contract commit = 83ad24e63eef8480efc978d32b2ae34c08714675
checker commit = f09d9ba9649c9a64522d3379fc9eea1910ac59d9
documentation commit = 13dc2d7079ff9d96ee5c5b8ea0c750a31db0a14d
workflow commit = 7c3159de0c69c03108e6947930a09b3bf1ddc2f9
```

The checker reconstructs every allowed response from the normalized host and evaluates

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)
```

on the declared sample backgrounds.

### Zero sample exact scores

```text
2031 -> (2,2,0,total 4)
2301 -> (0,0,0,total 0)
2310 -> (0,0,0,total 0)
3012 -> (0,3,1,total 4)
3201 -> (0,0,0,total 0)
3210 -> (0,0,4,total 4)
```

Complete-line minimizer face:

```text
{2301,2310,3201}
```

The prior selector `2031` has disadvantage 4.

### Blocker sample exact scores

```text
3012 -> (2,2,1,total 5)
3210 -> (0,0,4,total 4)
```

Complete-line minimizer face:

```text
{3210}
```

The prior selector `3012` has disadvantage 1.

Therefore:

```text
joint_sample_complete_line_selector_score_tables_complete = 1
joint_sample_canonical_selectors_stable_under_complete_line_score = 0
joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
```

The line/geometric tables do not include return, collision, interface or globally weighted child terms. They prove reoptimization is required, not that the displayed line minimizers are final coupled selectors.

## Reconciliation decisions

Two temporary duplicate audit layers were removed after concurrent canonical units appeared. The surviving canonical files are:

```text
data/prime_power_side_four_joint_global_binding_attempt_contract.json
data/prime_power_side_four_joint_global_binding_input_manifest.json
data/prime_power_side_four_joint_binding_source_coverage_contract.json
scripts/check_prime_power_side_four_joint_binding_source_coverage.py
docs/573-prime-power-side-four-joint-binding-source-coverage.md
docs/574-prime-power-side-four-recurrent-state-population-table.md
docs/575-prime-power-side-four-population-record-candidate.md
```

No duplicate chapter 571 or 573 should be recreated.

## Decisions to preserve

1. Do not invent global recurrent-state keys or occurrence provenance.
2. Do not promote local sample weights to installed global weights.
3. Do not merge exact child classes through reused local aliases.
4. Missing compulsory terms, incidences, weights and duals are unresolved, not zero.
5. Coordinate samples are not global recurrence occurrence claims.
6. Return, line and geometric views of one credit must not be double-counted.
7. The old response-only selectors are invalid for the declared complete-line score.
8. Complete-line minimizers are not final coupled minimizers until return, collision and interface terms are included.
9. Workflow configuration is not CI success.

## Validation boundary

```text
complete-line score contract arithmetic = reproduced locally
checker source = syntax-compiled locally
allowed response families = reconstructed locally
mutation audit = installed in checker
complete repository execution = not independently observed
complete 77-checker runner = not executed
workflow success = not observed
```

## Exact next step

Recompute the exact return-credit routing for every response in the new complete-line minimizer faces:

```text
zero: 2301, 2310, 3201
blocker: 3210
```

Then compare those return rows and attach collision/interface dependency records. Preserve all three zero-sample minimizers until the complete coupled score breaks the tie. Do not reuse routing derived from `2031` or `3012` as though those responses remained selected.
