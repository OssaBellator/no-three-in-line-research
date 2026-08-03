# First-host selector-rule compatibility audit

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact compatibility audit between normalized intrinsic selected-response provenance and the complete-score selector used on the four restoration menus. It proves output agreement on the enumerated safe class, not physical authorization of restored selector semantics.

## Two distinct rules

The upstream selected-provenance projection records

```text
minimum triple count, then lexicographically least response permutation.
```

This rule is source-backed only for the original residual response family of each normalized side-four host.

The restoration selector-face artifact uses

```text
lexicographically least response in the complete-score minimizer face.
```

Complete score includes background-response triples and therefore is not the same objective as intrinsic response triple count.

For the first host, the source-backed blocked record is

```text
menu                 3012,3210
intrinsic face       {3012}
selected response    3012
next gap             3.
```

## Formal extension census

For comparison only, the intrinsic rule was extended to every response in each restoration menu.

```text
blocked:
  intrinsic face {3012}
  selected 3012
  gap 3

restore 02:
  intrinsic face {2031,2310}
  selected 2031
  gap 1

restore 20:
  intrinsic face {3201}
  selected 3201
  gap 1

restore both:
  intrinsic face {2031,2301,2310,3201}
  selected 2031
  gap 1.
```

Across the exact 32 safe backgrounds in each of four menus:

```text
menu/background cases                  128
selected-identity agreements           128
next-gap agreements                    128
minimizer-face agreements              104
minimizer-face disagreements            24.
```

All 24 face disagreements occur in `restore_both`. Its intrinsic four-way face agrees with the complete-score face on eight backgrounds. On the other 24 backgrounds, complete score removes `2301` while retaining the same lexicographically selected response `2031` and the same next gap.

Thus selected identity and gap compatibility do not imply equality of minimizer faces or equality of scoring semantics.

## Tie-break dependency

The complete-score minimizer is unique in exactly 64 cases:

```text
blocked       32 unique cases
restore 20    32 unique cases.
```

The other 64 cases require a tie-break:

```text
restore 02    32 tied cases
restore both  32 tied cases.
```

Therefore every use of selected response `2031` in the restored `02` and restore-both menus depends on the lexicographic convention or on a substitute theorem proving all responses in the complete minimizer face congruent for operation, child-row and payment purposes.

The installed operation-registry source says scheduler operations select only after a complete kernel or an exact zero-response/blocker alternative. It does not specify the audit's lexicographic tie-break. The owner/fate ancestry source preserves exact minimizer faces and threshold crossings, but likewise supplies no first-host tie-breaking rule.

## Source boundary

Exact source census:

```text
directly source-authorized cases        32
formal extension-only cases             96
restored selector rules imported         0
scheduler tie-break rules found          0.
```

The blocked normalized selector is compatible with the complete-score selector on the safe class. That does not authorize extending the source rule to restored menus.

`restore_20` has a unique formal intrinsic and complete-score minimizer, but still lacks a physical occurrence, legal restoration state and source-defined restored response family.

`restore_02` and `restore_both` additionally require either a source scheduler tie-break or complete face congruence.

## Restored selector import contract

Each restored menu requires eight source fields:

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

For a non-singleton minimizer face, `selector_rule_ref` must supply a source-backed tie-break, or `child_payment_congruence_ref` must prove that every member of the entire minimizer face is interchangeable for the recurrent proof.

Current populated restored-selector fields: **0**.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_rule_compatibility.py \
  --check data/exact_recurrent_first_host_selector_rule_compatibility.json
```

The checker joins the selected-provenance and restoration-selector manifests, reconstructs intrinsic response energies, verifies two local scheduler-source documents by exact markers, compiles all 128 compatibility cases and rejects fifteen deliberate corruptions.

Physical occurrence coverage, legal restoration operations, source scheduler tie-breaking, operation/payment congruence, recurrent child rows, strict Lyapunov closure, global termination and `all_n_proved_by_checker` remain zero.
