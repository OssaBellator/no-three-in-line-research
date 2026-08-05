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

## Global binding and population status

The checked global binding attempt is underdetermined, not incompatible.

```text
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

Current population:

```text
qualifying installed population sources = 0
parent records populated = 0
child records populated = 0
candidate = null
candidate admissible = 0
binding_input_population_complete = 0
```

Do not invent recurrent-state keys, installed weights, transition provenance, normalization witnesses or recurrent-block witnesses.

## Explicit sample backgrounds

### Zero-response host

```text
host = s4-fc915f89dec31fec
background = {(4,4),(6,5)}
old response-only selector = 2031
```

### Blocker-alternative host

```text
host = s4-75b04c45c1c8eac2
collision key = 02,20
blocker = b4-8a44614df456
background = {(-1,6),(-2,9)}
old response-only selector = 3012
```

The old return-routing contracts remain historical exact rows for `2031` and `3012`; they are not selected rows after the complete-line reoptimization below.

## Complete-line selector scores

```text
contract = data/prime_power_side_four_joint_sample_complete_line_selector_scores.json
contract seal = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
checker = scripts/check_prime_power_side_four_joint_sample_complete_line_selector_scores.py
documentation = docs/576-prime-power-side-four-joint-sample-complete-line-selector-scores.md
workflow = .github/workflows/side-four-joint-sample-complete-line-selector-scores.yml
```

Exact zero-host scores:

```text
2031 -> 4
2301 -> 0
2310 -> 0
3012 -> 4
3201 -> 0
3210 -> 4
```

Complete-line zero minimizer face:

```text
{2301,2310,3201}
```

Exact blocker-host scores:

```text
3012 -> 5
3210 -> 4
```

Complete-line blocker minimizer:

```text
{3210}
```

Therefore neither old response-only selector is stable under the declared background line score.

## Newly completed reoptimized return routing

```text
contract = data/prime_power_side_four_reoptimized_minimizer_return_routing.json
contract seal = de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6
checker = scripts/check_prime_power_side_four_reoptimized_minimizer_return_routing.py
documentation = docs/577-prime-power-side-four-reoptimized-minimizer-return-routing.md
workflow = .github/workflows/side-four-reoptimized-minimizer-return-routing.yml
contract commit = 82422791fc70e2e0dd8ab172c2eb44cb79c0d32a
checker commit = 6e42dcc342f9519ee5df2ff540c55879086be404
documentation commit = 2a342d6928909ac4b1b881652a0f5a80e242b37c
workflow commit = fadb3fae3da0f7ff40f962fc76a85cdca29ffed1
```

### Zero minimizers

For each of

```text
2301, 2310, 3201
```

the declared background creates no rank-one or rank-two credit and the response creates no rank-three credit.

```text
return charges = {00:0,11:0,22:0,33:0}
weighted return expression = 0
```

The return category preserves the three-way zero-host tie.

### Blocker minimizer

For response `3210`, all four response points lie on `x+y-3=0`. Its four rank-three credits route as:

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

with exact compressed classes

```text
return:22 | rank3:1,1,-3:h0:k4 | collision:02,20 -> coefficient 1
return:33 | rank3:1,1,-3:h0:k4 | collision:02,20 -> coefficient 3
```

and symbolic row

```text
w_reopt_return_22_rank3_k4 + 3*w_reopt_return_33_rank3_k4.
```

The old `3012` return total was five; the reoptimized `3210` return total is four. The two new child weights are unresolved.

Exact flags:

```text
joint_sample_reoptimized_return_routing_complete = 1
zero_reoptimized_return_rows_complete = 1
blocker_reoptimized_return_row_complete = 1
reoptimized_child_weights_complete = 0
joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

## Reconciliation decisions

Concurrent canonical binding/source/population interfaces superseded two temporary duplicate audit layers, which were removed. Do not recreate duplicate chapters 571 or 573.

Surviving canonical source/population paths include:

```text
data/prime_power_side_four_joint_global_binding_attempt_contract.json
data/prime_power_side_four_joint_global_binding_input_manifest.json
data/prime_power_side_four_joint_binding_source_coverage_contract.json
scripts/check_prime_power_side_four_joint_binding_source_coverage.py
docs/573-prime-power-side-four-joint-binding-source-coverage.md
docs/574-prime-power-side-four-recurrent-state-population-table.md
docs/575-prime-power-side-four-population-record-candidate.md
```

## Decisions to preserve

1. Do not invent global recurrent-state keys, weights or occurrence provenance.
2. Do not promote local sample witnesses to installed global Lyapunov weights.
3. Do not merge exact child classes through reused local aliases.
4. Missing compulsory terms, incidences, weights and duals are unresolved, not zero.
5. Coordinate samples are not global recurrence occurrence claims.
6. Return, line and geometric views of one credit must not be double-counted.
7. Do not reuse routing from obsolete responses `2031` or `3012` as selected routing.
8. Preserve all three zero-host minimizers until collision, interface and global-weight terms break the tie.
9. The blocker response `3210` is only the line-plus-unweighted-return candidate; it is not yet the complete coupled selector.
10. Workflow configuration is not CI success.

## Validation boundary

```text
complete-line and reoptimized-routing contract arithmetic = reproduced locally
checker sources = syntax-compiled locally
allowed response families and credit ownership = reconstructed locally
mutation audits = installed in checkers
complete repository execution = not independently observed
complete 77-checker runner = not executed
workflow success = not observed
```

## Exact next step

Attach exact collision and interface dependency records to the four reoptimized candidate responses:

```text
zero: 2301, 2310, 3201
blocker: 3210
```

Record every locally known field and every missing coefficient rule, child key, child weight and global provenance field. Preserve the zero tie. Do not treat the blocker collision key `02,20` as a numerical collision coefficient without an exact offspring-routing rule.
