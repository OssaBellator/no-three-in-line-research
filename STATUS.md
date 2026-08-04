# Status and honesty ledger

**Last updated:** 4 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4517**. Post-ledger finite compilers do not introduce theorem identifiers. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

## Canonical installed construction stack

```text
runner = scripts/run_prime_power_installed_construction_regression_1166.py
manifest = e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d
operation kinds = 1166
checker contracts = 42
owner-changing kinds = 164
same-owner kinds = 1002
installed checkers = 77
owner/fate checker = 8f52372765f2877c48c32f417fcca27e068ac4675cc98263fd9044e30f28d828
registry contract = 383afc9477f5b52cf60f500c55f51005e4a3020dc34051a04437bdaf503a619b
registry seal = b67dc8f667a5e3e51914b8dba928825f8e8d7de0aa5a43f0e79994eca22ac18e
```

## Complete normalized side-four structure

```text
raw lineage seal = 84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f
selected-response seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
hosts = 86
response occurrences = 206
zero-response hosts = 75
blocker-alternative hosts = 11
unique minimum selectors = 42
tied minimizer faces = 44
positive next-energy gaps = 47
```

The canonical structural surfaces include exact identity-to-selected and all-pair return exchange, 344 rank-one and 516 rank-two residual return slots, a 516-record compulsory dependency map, the symbolic line kernel, line refinement and the 86-record actual-background obligation schema.

```text
selected-return contract = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
all-pair exchange contract = b6f768bae19061ffe35e1b0b437a402e4d49c7ce4ac8fa5bc5ea005518c565f9
residual return contract = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
symbolic line contract = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
line refinement = 8ff0751442bfefe378a74978c710d71c9e8c0d2c04652e4dcd2202746846890c
actual-background obligation v2 = e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd
```

## Newly populated actual-background sample

```text
sample = data/prime_power_side_four_actual_background_sample_batch.json
sample seal = 71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0
checker = scripts/check_prime_power_side_four_actual_background_sample_batch.py
routing = data/prime_power_side_four_sample_credit_routing_contract.json
routing seal = f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5
routing checker = scripts/check_prime_power_side_four_sample_credit_routing.py
```

The sample is explicitly declared and is not inferred from the host or identity matching:

```text
host = s4-fc915f89dec31fec
selected response = 2031
background points = {(4,4), (6,5)}
active line = x - 2y + 4 = 0
background load = 2
response occupancy = 2
```

Exact numeric coefficients:

```text
rank-one total = 2
rank-two total = 2
rank-three total = 0
complete line-kernel total = 4
total return charges = {00:1, 11:0, 22:3, 33:0}
```

The four recreated credits are routed once to three exact child classes. The line kernel is the certificate source and the return category is the offspring destination; the same credits are not counted twice.

```text
return:00 | rank1:1,-2,4:h2:k2 -> coefficient 1
return:22 | rank1:1,-2,4:h2:k2 -> coefficient 1
return:22 | rank2:1,-2,4:h2:k2 -> coefficient 2
```

The symbolic weighted expression is

```text
w_return_00_rank1 + w_return_22_rank1 + 2*w_return_22_rank2.
```

All three weights must be positive, but no numeric values or parent budget are currently bound.

## Exact current flags

```text
side_four_actual_background_sample_batch_complete = 1
sample_line_coefficients_complete = 1
sample_rank_one_rank_two_return_coefficients_complete = 1
sample_credit_partition_complete = 1
sample_child_routing_complete = 1
sample_child_keys_complete_for_populated_credits = 1

actual_background_profiles_complete = 0
sample_child_weights_complete = 0
sample_weighted_row_strict = 0
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
extend the explicit background batch to additional selector and blocker classes
bind a scoped positive-weight and parent-budget certificate for the sample, if justified
attach collision and interface child routing
compute complete coupled selector scores on full minimizer faces
publish one fully bound strict weighted row or an exact residual binding worklist
```

## Validation status

The sample coefficient compiler and credit-routing compiler were functionally executed locally. Each rejects fourteen independent corruptions. The sample, routing, documentation and Python 3.10/3.12 workflow configurations are committed.

The complete 77-checker runner has not been executed. Workflow success has not been observed, so CI success is not claimed.