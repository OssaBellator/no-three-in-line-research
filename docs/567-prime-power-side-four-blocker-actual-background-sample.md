# Side-four blocker-alternative actual-background sample

This post-ledger support artifact adds one explicitly declared coordinate background for a normalized blocker-alternative host. It does not introduce a theorem identifier after CMR4517 and does not claim that the sample occurs in the global recurrent process.

```text
sample = data/prime_power_side_four_blocker_actual_background_sample_batch.json
sample seal = 39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf
checker = scripts/check_prime_power_side_four_blocker_actual_background_sample.py
```

## Bound normalized host

```text
host = s4-75b04c45c1c8eac2
selected response = 3012
selected fate = blocker-alternative
collision/deletion key = 02,20
minimal blocker = b4-8a44614df456
```

The selected response consists of

```text
(0,3), (1,0), (2,1), (3,2).
```

The last three points are collinear on

```text
x - y - 1 = 0,
```

so the selected response has one exact rank-three credit.

## Declared background

```text
background points = {(-1,6), (-2,9)}
active background line = 3x + y - 3 = 0
background load h = 2
response occupancy k = 2
```

The background is declared with explicit point provenance. It is not inferred from the normalized host or from the identity matching.

## Exact coefficients

The active background line contributes

```text
rank one = 2
rank two = 2
rank three = 0
line total = 4.
```

The intrinsic selected-response triple contributes one further rank-three credit, giving

```text
rank-one total = 2
rank-two total = 2
rank-three total = 1
complete line-kernel total = 5.
```

The exact returned-predecessor charges are

```text
rank one = {00:1, 11:1, 22:0, 33:0}
rank two = {00:0, 11:2, 22:0, 33:0}
rank three = {00:0, 11:0, 22:0, 33:1}
total = {00:1, 11:3, 22:0, 33:1}.
```

Line energy and return routing describe the same five recreated credits and must not be added as separate offspring currencies.

## Honesty boundary

```text
side_four_blocker_actual_background_sample_batch_complete = 1
blocker_sample_line_coefficients_complete = 1
blocker_sample_rank_one_rank_two_rank_three_return_coefficients_complete = 1

actual_background_profiles_complete = 0
global_child_provenance_complete = 0
child_keys_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract digest and coordinate arithmetic were reproduced locally, and the checker source was syntax-compiled. Complete repository execution and workflow success were not independently observed.
