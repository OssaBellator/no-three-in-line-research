# Exact recurrent selector-rule progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track separates normalized source selector provenance from formal complete-score selection on restored response menus.

## ERL2p — exact compatibility census

The source-selected provenance rule is

```text
minimum intrinsic triple count,
then lexicographically least response permutation.
```

The restoration audit rule is

```text
minimum complete score on the safe background,
then lexicographically least response in the minimizer face.
```

The blocked first-host source record selects `3012` uniquely with intrinsic energy one and next gap three.

Formal extension of the intrinsic rule to the four restoration menus gives the exact comparison:

```text
menu/background cases                  128
selected-identity agreements           128
next-gap agreements                    128
minimizer-face agreements              104
minimizer-face disagreements            24
complete unique-minimizer cases         64
complete tie-break-dependent cases      64.
```

All 24 face disagreements occur in `restore_both`: intrinsic scoring retains `2301` in a four-way face, while complete scoring removes it on 24 of 32 safe backgrounds. The selected label remains `2031`.

## ERL2q — tie-break and provenance boundary

The complete minimizer is unique for:

```text
blocked       32 cases
restore_20    32 cases.
```

A tie-break is required for:

```text
restore_02    32 cases
restore_both  32 cases.
```

The installed scheduler registry requires a complete kernel or exact blocker alternative before selection, but does not install the lexicographic tie-break used by the audit. Owner/fate ancestry retains exact minimizer faces and threshold crossings but supplies no first-host restored selector rule.

Exact source census:

```text
directly source-authorized cases        32
formal extension-only cases             96
restored selector rules imported         0
scheduler tie-break rules found          0.
```

Agreement of selected labels and next gaps is therefore compatibility, not provenance or physical authorization.

## ERL2r — restored selector import contract

Each restored menu requires:

```text
physical_occurrence_ref
legal_menu_state_ref
response_family_ref
score_semantics_ref
selector_rule_ref
scheduler_operation_ref
child_payment_congruence_ref
realization_status.
```

For a non-singleton minimizer face, either:

1. `selector_rule_ref` supplies a source-backed tie-break; or
2. `child_payment_congruence_ref` proves every response in the complete minimizer face interchangeable for the recurrent argument.

Current populated restored-selector fields: **0 of 24**.

## Current boundary

```text
physical occurrence coverage              0
legal restored menu states                 0
source-restored selector semantics          0
source scheduler tie-break                  0
complete-face operation/payment congruence  0
promotion to recurrent closure              0
all_n_proved_by_checker                     0.
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_selector_rule_compatibility.py
data/exact_recurrent_first_host_selector_rule_compatibility.json
docs/exact-recurrent-first-host-selector-rule-compatibility.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
