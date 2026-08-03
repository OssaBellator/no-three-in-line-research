# First-host restoration selector-face congruence

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact on the chart-safe background class. It does not prove that any restoration is a legal physical operation.

## Canonical selector rule

For each restoration menu, take the complete-score minimizer face and then select the lexicographically least response in that face.

The four response menus are

```text
blocked:
  3012,3210

restore 02:
  2031,2310,3012,3210

restore 20:
  3012,3201,3210

restore both:
  2031,2301,2310,3012,3201,3210.
```

## Exact minimizer faces

Across all 32 chart-safe backgrounds:

```text
blocked:
  face {3012} on 32 backgrounds

restore 02:
  face {2031,2310} on 32 backgrounds

restore 20:
  face {3201} on 32 backgrounds

restore both:
  face {2031,2301,2310,3201} on 8 backgrounds
  face {2031,2310,3201}      on 24 backgrounds.
```

The four-way simultaneous-restoration face occurs exactly when neither `11` nor `22` is present in the background. Otherwise `2301` has positive excess score and leaves the minimizer face.

Thus the restore-both minimizer face is not background-invariant.

## Selected response is invariant

Despite the face split, the canonical selected response is constant for every background in each menu:

```text
blocked       -> 3012
restore 02    -> 2031
restore 20    -> 3201
restore both  -> 2031.
```

Consequently all four restoration menus have background-invariant selector identity on the safe class.

The ten-state operation-aware signature is therefore not needed merely to identify the selected response. It remains necessary for exact score geometry, complete minimizer faces and any child or payment data that depend on those distinctions.

## Exact next-energy gaps

The gap from the minimum to the next distinct score is also background-invariant:

```text
blocked       gap 3
restore 02    gap 1
restore 20    gap 1
restore both  gap 1.
```

Every menu therefore retains a positive selector-stability gap throughout the safe class.

## Consequence for the cross-branch interface

The alternating-core selector component can be quotiented more aggressively than the complete geometric state:

```text
selector identity alphabet: one state per restoration menu
complete face alphabet:     five total faces across four menus
operation-aware geometry:   ten safe signatures.
```

This is a genuine partial congruence theorem. It does not imply congruence of legal operations, intermediate states, child multiplicities, positive weights, budgets, continuation edges or capacities.

In particular, selector stability does not populate a recurrent offspring row and does not prove Lyapunov strictness.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_restoration_selector_face.py \
  --check data/exact_recurrent_first_host_restoration_selector_face.json
```

The checker enumerates all four restoration menus and all 32 safe backgrounds, verifies the five exact minimizer faces, canonical selected responses and next-energy gaps, and rejects twelve deliberate corruptions.

Physical chart confinement, restoration legality, occurrence coverage, recurrent child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
