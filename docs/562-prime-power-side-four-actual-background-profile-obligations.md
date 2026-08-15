# Side-four actual-background profile obligations

This post-ledger artifact defines the complete actual-background profile required to turn the exact side-four response and return structures into numerical rank-one, rank-two and line coefficients. Version 2 binds the canonical symbolic line-kernel context and line-category dependency refinement; it does not independently reinterpret the coefficient rule.

```text
selected-response manifest seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
return-context contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
residual-return contract seal = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
compiled residual rows seal = 72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2
symbolic-line contract seal = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
line-refinement seal = 8ff0751442bfefe378a74978c710d71c9e8c0d2c04652e4dcd2202746846890c
contract = data/prime_power_side_four_actual_background_profile_obligation_contract.json
contract seal = e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd
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

## Symbolic line binding

The canonical symbolic catalogue contains exactly:

```text
line occurrences = 488
response occupancy census = {2: 477, 3: 9, 4: 2}
rank-one multiplier total = 989
rank-two multiplier total = 516
rank-three constant total = 17
```

The profile obligation imports the exact rule

```text
K(h,k) = k*C(h,2) + C(k,2)*h + C(k,3).
```

The line-refinement artifact already moves this rule from a missing prerequisite to a known input for all 86 line dependency records. The remaining line-category prerequisites are actual background heights and line owner labels.

## Rank-one witness obligation

For each selected entering edge `x`, the profile must list every relevant nonaxis background line through `x`, its exact background load `h_ell`, and certify

```text
rank-one coefficient at x = sum_ell C(h_ell,2).
```

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
occupancy 2 = 477
occupancy 3 = 9
occupancy 4 = 2
```

Exact expansion:

```text
477*C(2,2) + 9*C(3,2) + 2*C(4,2) = 516.
```

A line load is populated once and reused by every pair on that exact host-line. Independently assigning values to the pairs is inconsistent.

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
symbolic_line_binding_complete = 1
line_dependency_refinement_binding_complete = 1

actual_background_profiles_complete = 0
rank_one_return_coefficients_complete = 0
rank_two_return_coefficients_complete = 0
line_coefficients_complete = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The v2 checker validates the symbolic-line and line-refinement seals, all 86 profile records, the 344 rank-one slots, the 488 line classes, the exact multiplier totals and thirteen corruption cases. The next task is to supply one actual background/provenance batch rather than another normalized-host surrogate.
