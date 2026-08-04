# Side-four actual-background profile schema

This post-ledger artifact defines the exact input format required before rank-one or rank-two side-four coefficients may be populated. The current batch is intentionally empty because no actual background-point records have been found in the repository.

```text
batch = data/prime_power_side_four_actual_background_profile_batch.json
batch sha256 = ace0a65dd4b6ce8dfa634a370cb531670aa824c7c83dd44f45b81f95bd57c6e4
checker = scripts/check_prime_power_side_four_actual_background_profile_batch.py
selected-response seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
residual-return seal = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
symbolic-line seal = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
```

## Required record

Every future profile must contain exactly:

```text
profile_id
host_id
provenance_key
background_points
retained_incidence_labels
line_owner_labels
selected_response
```

`background_points` is the authoritative coordinate list. The checker rejects duplicate points, unknown hosts, response mismatches, absent provenance and independently supplied incidence totals.

## Derived quantities

All numerical incidence data must be recomputed from the coordinate list:

```text
line height = number of listed background points on the canonical line
rank-one incidence = number of unordered background-point pairs collinear with the entering point
rank-two incidence = background height on the exact response-pair line
complete local kernel = k*C(h,2)+C(k,2)*h+C(k,3)
```

A built-in synthetic derivation audit checks:

```text
three collinear background points give line height 3
an entering point on their line sees three background pairs
K(3,2) = 9
K(0,4) = 4
```

The synthetic fixture validates arithmetic only. It is not published as an actual normalized provenance profile.

## Current batch boundary

```text
expected normalized hosts = 86
provided actual profiles = 0
missing actual profiles = 86
populated background points = 0
populated rank-one incidences = 0
populated rank-two incidences = 0
```

## Honesty boundary

```text
actual_background_profile_schema_complete = 1

actual_background_profile_batch_complete = 0
actual_background_profiles_complete = 0
rank_one_return_coefficients_complete = 0
rank_two_return_coefficients_complete = 0
numeric_rank_one_rank_two_line_coefficients_complete = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The next valid update is a new checked batch version containing genuine coordinate-labelled background records. Counts without coordinates are not accepted.