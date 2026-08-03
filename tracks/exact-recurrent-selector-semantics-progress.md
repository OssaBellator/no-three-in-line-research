# Exact recurrent selector-semantics progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track separates normalized selected-response provenance from restored-menu scheduling semantics.

## ERL2p — selector-rule compatibility

The source selected-provenance rule is

```text
minimum intrinsic triple count, then lexicographically least response.
```

Its source-backed scope is the original residual response family. The restoration audit instead uses

```text
lexicographically least response in the complete-score minimizer face.
```

Formally extending the intrinsic rule across all four restoration menus gives exact agreement with the complete-score selector on selected identity and next gap in all 128 safe menu/background cases.

```text
selected-identity agreements  128 of 128
next-gap agreements           128 of 128
minimizer-face agreements     104 of 128
face disagreements             24 of 128.
```

All face disagreements occur under simultaneous restoration, where complete score removes `2301` on 24 backgrounds while preserving selected response `2031` and gap one.

## ERL2q — tie-break source boundary

Exactly 64 complete-score cases have unique minimizers:

```text
blocked       32
restore 20    32.
```

Exactly 64 require a tie-break:

```text
restore 02    32
restore both  32.
```

The installed scheduler and owner/fate sources do not specify the lexicographic tie-break used by the audit. They provide complete-kernel scheduling and exact minimizer-face stability interfaces only.

Current source census:

```text
directly source-authorized cases     32
formal extension-only cases          96
restored selector imports             0
source scheduler tie-break rules      0.
```

For `restore_02` and `restore_both`, recurrence use of selected response `2031` requires either a source-backed tie-break or complete operation, child-row and payment congruence across the entire minimizer face.

`restore_20` is uniquely minimized, but still requires a physical occurrence, legal menu state, source response family and score semantics.

## Import boundary

Each restored menu must populate eight fields:

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

Output agreement alone is not a selector-semantics import.

```text
physical_selector_rule_import_allowed = 0
operation_congruence_proved = 0
payment_congruence_proved = 0
all_n_proved_by_checker = 0
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_selector_rule_compatibility.py
data/exact_recurrent_first_host_selector_rule_compatibility.json
docs/exact-recurrent-first-host-selector-rule-compatibility.md
docs/ERL_SELECTOR_RULE_REVIEW_GATE.md
```
