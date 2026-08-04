# Status and honesty ledger

**Last updated:** 4 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4517**. Post-ledger finite compilers do not introduce new theorem identifiers. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

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

## Normalized side-four finite block

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

## Canonical return and dependency surfaces

```text
selected-return contract = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
selected-return rows = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea
all-pair exchange contract = b6f768bae19061ffe35e1b0b437a402e4d49c7ce4ac8fa5bc5ea005518c565f9
all-pair transition rows = 1151a0d65b228612217b484e97256d36a1a809d95338f18a28b2eb58ab2a3274
residual return contract = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
residual return rows = 72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2
dependency v4 contract = b1adfb20df51302092d9b8f7acfde9d8ed602f12895310cd54c64ab44cac4f1a
dependency v4 rows = 2cb9ef2f8a8962a1e848bfc264ec93e3c85ccbf6dccea1766185d29aa6945505
```

```text
identity-to-selected exchange entries = 344
all ordered distinct response transitions = 378
rank-three recreated return credits = 17
rank-three nonzero return-kernel entries = 13
rank-one structural return entries = 344
rank-two structural return entries = 516
unresolved rank-one background-pair incidences = 344
unresolved rank-two background-point incidences = 516
dependency records = 516
known coefficients = 86
unresolved coefficients = 430
known prerequisite occurrences in v4 = 774
missing prerequisite occurrences in v4 = 1462
```

## Additive symbolic line refinement

```text
symbolic line contract = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
line refinement v2 = 8ff0751442bfefe378a74978c710d71c9e8c0d2c04652e4dcd2202746846890c
documentation = docs/562-prime-power-side-four-symbolic-line-kernel-context.md
documentation = docs/563-prime-power-side-four-line-dependency-refinement.md
```

For each selected-response line,

```text
K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3).
```

```text
selector patterns = 6
line occurrences = 488
occupancy census = {2: 477, 3: 9, 4: 2}
rank-one multiplier total = 989
rank-two multiplier total = 516
rank-three constant total = 17
known prerequisite occurrences after refinement = 860
missing prerequisite occurrences after refinement = 1376
remaining line inputs per row = background-height profile + line-owner labels
```

The rank-three constants match the selected-return kernel row-by-row.

## Actual-background profile obligation v2

```text
contract = data/prime_power_side_four_actual_background_profile_obligation_contract.json
contract seal = e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd
checker = scripts/check_prime_power_side_four_actual_background_profile_obligations.py
documentation = docs/562-prime-power-side-four-actual-background-profile-obligations.md
workflow = .github/workflows/side-four-actual-background-profile-obligations.yml
```

The v2 compiler binds the canonical selected-return, residual-return, symbolic-line and line-refinement artifacts.

```text
host profile records = 86
rank-one incidence slots = 344
rank-two pair slots = 516
shared rank-two host-line variables = 488
unresolved background identifiers = 86
unresolved background point sets = 86
unresolved rank-one incidence witnesses = 344
unresolved rank-two line loads = 488
unresolved line owner labels = 488
unresolved interface provenance records = 86
unresolved CRT provenance records = 86
```

The 516 pair slots expand consistently from the 488 shared line variables:

```text
477*C(2,2) + 9*C(3,2) + 2*C(4,2) = 516.
```

This is a complete schema, not a populated actual-background batch.

## Exact current flags

```text
owner_fate_lineage_kernel_ancestry_proved = 1
installed_transition_kind_bank_1166_exhaustive = 1
installed_transition_regression_1166_complete = 1
side_four_raw_fibre_lineage_manifest_complete = 1
side_four_selected_response_provenance_manifest_complete = 1
side_four_return_exchange_context_complete = 1
rank_three_return_kernel_complete_for_normalized_block = 1
side_four_return_exchange_manifest_complete = 1
side_four_residual_return_credit_worklist_complete = 1
rank_one_return_structure_complete_for_normalized_block = 1
rank_two_return_structure_complete_for_normalized_block = 1
side_four_compulsory_coefficient_dependency_map_complete = 1
symbolic_line_coefficient_rule_complete_for_normalized_block = 1
rank_three_line_constants_match_return_kernel = 1
line_dependency_refinement_complete_for_normalized_block = 1
actual_background_profile_obligation_compiler_complete = 1
symbolic_line_binding_complete = 1
line_dependency_refinement_binding_complete = 1

actual_background_profiles_complete = 0
actual_background_height_profiles_complete = 0
line_owner_labels_complete = 0
rank_one_return_coefficients_complete = 0
rank_two_return_coefficients_complete = 0
numeric_rank_one_rank_two_line_coefficients_complete = 0
complete_return_coefficient_rule_complete = 0
unresolved_coefficients_populated = 0
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
populate one nontrivial actual-background batch using the v2 schema
attach background points, identifiers and retained point provenance
populate 344 rank-one incidence witnesses and 488 shared line heights
expand shared heights consistently to all 516 rank-two pair slots
attach line-owner, interface and CRT provenance
evaluate the bound symbolic kernels without double counting rank three
bind line/return child keys with positive weights
publish strict weighted rows or an exact residual provenance worklist
```

The next success criterion is one checked actual-background profile batch that numerically populates a complete non-geometric category, followed by at least one fully bound compulsory weighted row.

## Validation status

The repaired source verifiers, owner/fate checker, registry census/seal and runner manifest were reproduced during the repair pass. The canonical raw-lineage, selector, obligation, selected-return, all-pair exchange, residual-return and dependency-v4 checkers report local reproduction in their installed documentation.

The additive symbolic-line, line-refinement and background-profile v2 checker sources and Python 3.10/3.12 workflows are installed, but their complete current executions have not been independently observed. The complete 77-checker runner has not been executed, workflow success has not been observed, and CI success is not claimed.
