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

## ERL2s — exact face-congruence basis

The tied faces admit a minimum anchored comparison basis with anchor `2031`.

At raw-background level:

```text
restore_02 comparisons                    32
restore_both four-way comparisons         24
restore_both three-way comparisons        48
raw comparisons total                    104.
```

Joining to the ten exact operation signatures compresses this to:

```text
menu/signature cells                      20
signature-level response-pair obligations 32.
```

Exact pair census:

```text
2031 ~ 2301   2 signature obligations,  8 raw comparisons
2031 ~ 2310  20 signature obligations, 64 raw comparisons
2031 ~ 3201  10 signature obligations, 32 raw comparisons.
```

The finite worklist can be discharged by 32 signature-specific proofs, four explicitly menu-parametric pair theorems, or three cross-menu pair-type theorems. The latter two are valid only when source theorems prove their stated uniformity.

Each signature obligation has nine source-evidence fields, for 288 exact slots. Current populated slots: **0**.

The four-coordinate operation signature is a score-worklist index, not a proved physical owner/child/payment signature.

## ERL2t — source-import gate

The owner/fate ancestry and installed operation-registry documents jointly expose all five required abstract components:

```text
common owner
operation
child row
payment
closure route.
```

The unique minimum abstract source cover uses both documents. Neither source alone is complete, neither document names any first-host face response, and neither supplies an occurrence-faithful response-pair join.

The exact import modes are now registered with stable IDs:

```text
signature-specific   32 records, 288 evidence slots
menu-parametric       4 records,  40 evidence slots
cross-menu            3 records,  30 evidence slots.
```

A mode is accepted only when every record required by that mode is complete. Partial records from different modes do not combine into a proof.

Current source-import census:

```text
abstract component union complete         1
occurrence-faithful pair joins             0
first-host response-pair theorems          0
accepted signature records                0 of 32
accepted menu-parametric theorems          0 of 4
accepted cross-menu theorems               0 of 3
accepted import modes                      0 of 3.
```

The schema cover does not authorize selector substitution.

## Current boundary

```text
physical occurrence coverage              0
legal restored menu states                 0
source-restored selector semantics          0
source scheduler tie-break                  0
complete-face operation/payment congruence  0
accepted face-congruence obligations        0 of 32
accepted face-congruence import modes        0 of 3
promotion to recurrent closure              0
all_n_proved_by_checker                     0.
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_selector_rule_compatibility.py
data/exact_recurrent_first_host_selector_rule_compatibility.json
docs/exact-recurrent-first-host-selector-rule-compatibility.md

scripts/check_exact_recurrent_first_host_selector_face_congruence_worklist.py
data/exact_recurrent_first_host_selector_face_congruence_worklist.json
docs/exact-recurrent-first-host-selector-face-congruence-worklist.md

scripts/check_exact_recurrent_first_host_selector_face_source_import_gate.py
data/exact_recurrent_first_host_selector_face_source_import_gate.json
docs/exact-recurrent-first-host-selector-face-source-import-gate.md

docs/ERL_SELECTOR_RULE_REVIEW_GATE.md
docs/ERL_SELECTOR_FACE_CONGRUENCE_REVIEW_GATE.md
docs/ERL_SELECTOR_FACE_SOURCE_IMPORT_REVIEW_GATE.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
