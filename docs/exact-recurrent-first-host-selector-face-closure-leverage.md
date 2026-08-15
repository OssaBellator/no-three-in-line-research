# First-host selector-face closure leverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional consequence audit for the minimizer-face congruence worklist. It classifies what proved response-pair congruence would remove and what it would leave unchanged. No response-pair theorem is currently imported.

## Pair-type leverage

The tied restored menus use three anchored response-pair types:

```text
2031 ~ 2301
2031 ~ 2310
2031 ~ 3201.
```

All eight subsets have been classified. Their exact coverage distribution over the 64 tied menu/background cases is

```text
tied cases discharged   subset patterns
0                       4
32                      2
56                      1
64                      1.
```

The sharp useful chain is

```text
2031 ~ 2310
  discharges all 32 restore_02 cases
  leaves all 32 restore_both cases

2031 ~ 2310 and 2031 ~ 3201
  additionally discharges the 24 restore_both three-way cases
  total 56
  leaves the eight restore_both four-way cases

all three pair types
  additionally discharges the final eight four-way cases
  total 64.
```

Thus all three pair types are indispensable for complete tie-break substitution. The `2031~2301` pair is a final-eight bottleneck: by itself it discharges no case, but after the other two pairs it is exactly what remains.

## Menu-local versus global congruence

The face-congruence worklist compares response candidates **inside one legal menu state**. Even a complete proof of all three pair types would establish only that the scheduler may choose any minimizer in those tied faces without changing the recurrent certificate.

It would not identify

```text
state 01 selected response 3201
```

with

```text
states 10 and 11 selected response 2031
```

across their different legal menu states. Such a quotient requires a separate occurrence-faithful selected-state theorem.

Therefore complete face congruence alone leaves unchanged:

```text
menu states                              4
directed menu edges                      8
selector-changing edges                  6
selector-neutral edges                   2
selected-label scalar route covers       6
external changing routes per label cover 3
menu scalar route covers                14
external routes per menu cover           4.
```

No route-cover reduction follows automatically from resolving the selector tie.

## Hypothetical global selected-state quotient

For completeness, the checker also computes the consequence of an additional theorem identifying selected `3201` in state `01` with selected `2031` in states `10` and `11` across their distinct legal menus.

The selected classes would become

```text
{3012}
{2031,3201}.
```

The resulting menu-edge census would be

```text
selector-changing edges                    4
selector-neutral edges                     4
label-scalar orders                        2
changing edges payable by label descent    2
changing edges requiring another route     2
total edges requiring a non-label route    6.
```

The current selected-label method requires another route for

```text
3 external changing edges + 2 neutral edges = 5.
```

Thus this stronger quotient would increase, not decrease, the total menu-edge burden from five to six. The menu-state scalar burden remains four external routes.

This conditional calculation is not a reason to seek the quotient. It prevents a future congruence claim from being advertised as an automatic closure simplification.

## Global selected-state quotient contract

The stronger quotient would require ten source fields:

```text
physical_occurrence_domain_ref
selected_state_domain_ref
menu_state_refs
common_owner_ref
operation_congruence_ref
child_row_congruence_ref
payment_congruence_ref
closure_route_congruence_ref
theorem_ref
realization_status.
```

Current populated fields: **0 of 10**.

## Current source state

```text
accepted face-congruence proof modes       0
accepted pair types                        0
tied cases source-discharged                0 of 64
global selected-state quotients             0
selector tie-break substitution             0
promotion to recurrent closure              0.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_selector_face_closure_leverage.py \
  --check data/exact_recurrent_first_host_selector_face_closure_leverage.json
```

The checker joins the face-congruence worklist, source-import gate, Boolean selector boundary, and scalar route-cover classification; enumerates all eight pair subsets; verifies the unique complete pair set; compiles the hypothetical global quotient; and rejects eighteen deliberate corruptions.

Physical occurrence coverage, restoration legality, persistent owner identity, recurrent child rows, payment and closure-route congruence, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
