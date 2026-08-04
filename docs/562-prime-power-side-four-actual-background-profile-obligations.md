# Side-four actual-background profile obligations

This post-ledger artifact defines the complete actual-background profile required to turn the exact side-four response and return structures into numerical rank-one, rank-two and line coefficients. It does not manufacture a background from the normalized host and it does not interpret a null incidence as zero.

```text
selected-response manifest seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
return-context contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
residual-return contract seal = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
compiled residual rows seal = 72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2
contract = data/prime_power_side_four_actual_background_profile_obligation_contract.json
contract seal = 090adf1124d186d0eb8c16a4f7ae286d167583540386832c642b4eac2d24922f
checker = scripts/check_prime_power_side_four_actual_background_profile_obligations.py
```

## Required profile record

Every normalized host/provenance refinement requires one record containing:

```text
host identifier
background identifier
exact background point set
background-point provenance
rank-one incidence witnesses
rank-two exact line loads
line owner labels
interface provenance
CRT provenance
```

The background identifier and point set must identify one actual inherited state. The identity matching, deletion trace and normalized response host are not substitutes for this data.

## Rank-one witness obligation

For each selected entering edge `x`, the profile must list every relevant nonaxis background line through `x`, its exact background load `h_ell`, and certify

```text
rank-one coefficient at x = sum_ell binomial(h_ell, 2).
```

The structural worklist contains:

```text
rank-one incidence slots = 344
unresolved rank-one witnesses = 344
```

Each slot already retains the entering edge, returned identity predecessor and matching-cycle label. The background lines and pair incidence remain unresolved.

## Rank-two line-load compression

All response pairs lying on one exact real line share the same background point incidence. Therefore the 516 pair slots compress losslessly to one line-load variable per host-line class.

```text
rank-two pair slots = 516
rank-two host-line classes = 488
unresolved rank-two line loads = 488
```

Host-line classes by response occupancy:

```text
occupancy 2 = 477 classes
occupancy 3 = 9 classes
occupancy 4 = 2 classes
```

The exact pair-slot expansion is:

```text
477 * binomial(2,2) = 477
9 * binomial(3,2) = 27
2 * binomial(4,2) = 12
                              ----
                              516
```

A line load must be populated once and then reused by every pair on that exact host-line. Independently assigning values to the pairs would be inconsistent.

## Complete line-kernel obligation

For an exact host-line with background load `h` and response occupancy `k`, the complete local new-triple contribution is

```text
k * binomial(h,2) + binomial(k,2) * h + binomial(k,3).
```

All three ranks remain coupled unless a labelled child route separately pays one of them. The profile must retain line owner, interface and CRT labels before the result enters a weighted row.

## Exact unresolved census

```text
host profile records = 86
unresolved background identifiers = 86
unresolved background point sets = 86
unresolved background-point provenance records = 86
unresolved rank-one incidence witnesses = 344
unresolved rank-two line loads = 488
unresolved line owner labels = 488
unresolved interface provenance records = 86
unresolved CRT provenance records = 86
```

These are obligations, not zero-valued coefficients.

## Honesty boundary

```text
actual_background_profile_obligation_compiler_complete = 1

actual_background_profiles_complete = 0
rank_one_return_coefficients_complete = 0
rank_two_return_coefficients_complete = 0
line_coefficients_complete = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract seal, all 86 profile records, the 344 rank-one slots, the 488 line classes, the exact 516-pair expansion and twelve corruption cases are checked by the profile-obligation checker. The next task is to supply one actual background/provenance batch rather than another normalized-host surrogate.
