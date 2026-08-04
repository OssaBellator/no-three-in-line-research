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
registry seal = b67dc8f667a5e3e51914b8dba928825f8e8d7de0aa5a43f0e79994eca22ac18e
```

## Normalized side-four finite block

```text
raw lineage seal = 84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f
selected-response seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
hosts = 86
zero-response hosts = 75
blocker-alternative hosts = 11
response occurrences = 206
```

Canonical support seals:

```text
selected-return = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
all-pair exchange = b6f768bae19061ffe35e1b0b437a402e4d49c7ce4ac8fa5bc5ea005518c565f9
residual return = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
symbolic line = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
actual-background obligation = e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd
```

## Zero-response explicit sample

```text
sample seal = 71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0
host = s4-fc915f89dec31fec
selector = 2031
background = {(4,4),(6,5)}
rank totals = (2,2,0)
line total = 4
return charges = {00:1, 22:3}
routing seal = f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5
weight seal = d85580884ba95d368350ee1230890e4b54b86c33466c55fb20cb837de46b7316
```

The four credits compress to three exact classes with coefficient vector `(1,1,2)`. The local witness `(8;1,1,1)` has weighted total `4` and slack `4`.

## Blocker-alternative explicit sample

```text
sample seal = 39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf
host = s4-75b04c45c1c8eac2
selector = 3012
collision key = 02,20
blocker = b4-8a44614df456
background = {(-1,6),(-2,9)}
rank totals = (2,2,1)
line total = 5
return charges = {00:1, 11:3, 33:1}
routing seal = 4b8da717b59a47d8c5f1d4db1308e934c26390804611b0906c81c30cce136aa5
weight seal = f879314c3ab11b96e3fc09df0c5f540cde441055c6af00f631c4cbbee4deafb5
```

The selected response contains the intrinsic rank-three triple `10|21|32`, routed once to `return:33`. The five credits compress to four exact classes with coefficient vector `(1,1,2,1)`. The local witness `(10;1,1,1,1)` has weighted total `5` and slack `5`.

## Joint exact-class weight compatibility

```text
contract = data/prime_power_side_four_joint_sample_weight_compatibility_contract.json
contract seal = 1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5
checker = scripts/check_prime_power_side_four_joint_sample_weight_compatibility.py
```

The local alias `w_return_00_rank1` occurs in both sample contracts, but the corresponding full child keys differ. The joint namespace therefore has

```text
local aliases = 6
exact child classes = 7
colliding aliases = 1
```

The two `return:00` classes remain distinct.

A shared local witness is

```text
both parent weights = 16
all seven exact child-class weights = 1
zero row total/slack = 4/12
blocker row total/slack = 5/11
```

After normalization, each child weight is `1/16`; the zero row total is `1/4` and the blocker row total is `5/16`.

This proves simultaneous local return-only feasibility only. Sixteen global and compulsory bindings remain unresolved.

## Accounting rule

For both samples:

```text
line energy = certificate source
geometric rank-three count = certificate source when present
return classes = offspring destination
```

Each recreated credit is charged exactly once.

## Exact current flags

```text
side_four_actual_background_sample_batch_complete = 1
sample_credit_partition_complete = 1
sample_child_routing_complete = 1
sample_return_only_weight_feasibility_proved = 1

side_four_blocker_actual_background_sample_batch_complete = 1
blocker_sample_credit_partition_complete = 1
blocker_sample_child_routing_complete = 1
blocker_sample_return_only_weight_feasibility_proved = 1

joint_sample_exact_weight_namespace_complete = 1
joint_sample_local_positive_assignment_complete = 1
joint_sample_return_only_rows_strict_under_local_witness = 1

actual_background_profiles_complete = 0
joint_sample_global_weight_bindings_complete = 0
joint_sample_full_compulsory_rows_complete = 0
joint_sample_global_recurrent_compatibility_proved = 0
sample_full_compulsory_row_complete = 0
blocker_sample_full_compulsory_row_complete = 0
sample_weighted_row_strict = 0
blocker_sample_weighted_row_strict = 0
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
identify exact parent recurrent-state keys for both samples
map all seven exact child classes to installed global states without alias projection
bind globally compatible weights or publish a checked incompatibility certificate
populate selector coefficients on full minimizer faces
populate collision and interface coefficients and child keys
extend to another blocker collision class
claim complete row strictness only after every compulsory term is bound
```

## Validation status

The zero-response coefficient and routing compilers were functionally executed locally and each rejected fourteen corruptions. Sample, blocker and joint weight arithmetic, seals and namespace counts were reproduced locally. The newly added checker sources were syntax-compiled locally.

Complete repository execution of all new checkers has not been independently observed. The complete 77-checker runner has not been executed. Workflow success has not been observed, so CI success is not claimed.
