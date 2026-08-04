# Side-four line dependency refinement

This post-ledger refinement chains the exact symbolic line-kernel context onto the canonical compulsory coefficient dependency map v4. The v4 map remains sealed; the refinement records the exact prerequisite delta.

```text
base dependency contract = b1adfb20df51302092d9b8f7acfde9d8ed602f12895310cd54c64ab44cac4f1a
base dependency records = 2cb9ef2f8a8962a1e848bfc264ec93e3c85ccbf6dccea1766185d29aa6945505
symbolic line contract = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
refinement = data/prime_power_side_four_coefficient_dependency_line_refinement.json
refinement sha256 = 8ff0751442bfefe378a74978c710d71c9e8c0d2c04652e4dcd2202746846890c
checker = scripts/check_prime_power_side_four_coefficient_dependency_line_refinement.py
```

The newly available prerequisite is the exact line coefficient rule

```text
K(h,k) = k*C(h,2) + C(k,2)*h + C(k,3).
```

It refines all 86 line-category records. Relative to dependency map v4:

```text
known prerequisite occurrence delta = +86
missing prerequisite occurrence delta = -86
known prerequisite occurrences = 860
missing prerequisite occurrences = 1376
```

The line category now has:

```text
records = 86
known prerequisites per row = selected-response line signature + exact coefficient rule
remaining missing prerequisites per row = background-height profile + line-owner labels
known line prerequisite occurrences = 172
missing line prerequisite occurrences = 172
```

No line coefficient is numerically populated until the actual background height on each coordinate line is supplied. No child key or positive child weight is inferred from the parent context.

## Honesty boundary

```text
line_dependency_refinement_complete_for_normalized_block = 1

actual_background_height_profiles_complete = 0
line_owner_labels_complete = 0
numeric_rank_one_rank_two_line_coefficients_complete = 0
unresolved_coefficients_populated = 0
global_child_provenance_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker validates canonical dependency map v4, the symbolic line catalogue, the exact 86-record delta and twelve corruption cases.