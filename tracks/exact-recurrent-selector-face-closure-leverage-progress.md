# Exact recurrent selector-face closure leverage progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records the exact recurrence consequences of replacing the absent restored-menu tie-break by complete minimizer-face congruence.

## ERL2u — pair-subset leverage

All eight subsets of the three anchored pair types have been classified.

```text
pair theorem stock                         tied cases discharged
2031~2310                                  32
2031~2310 and 2031~3201                    56
all three pairs                            64.
```

The unique complete set is

```text
2031~2301
2031~2310
2031~3201.
```

`2031~2301` is the final-eight four-way-face bottleneck. Current source-discharge remains zero of 64 tied cases.

## ERL2v — menu-local boundary

Face congruence proves interchangeability only inside one legal menu state. It does not identify selected `3201` in state `01` with selected `2031` in states `10` and `11`.

Therefore even complete face congruence leaves unchanged:

```text
menu states                              4
directed menu edges                      8
selector-changing edges                  6
selector-neutral edges                   2
selected-label scalar route covers       6
menu scalar route covers                14.
```

No route-cover reduction follows from tie-break substitution alone.

## ERL2w — global quotient warning

A separate occurrence-faithful selected-state theorem would be needed to merge selected `2031` and `3201` across their distinct legal menus.

Under that hypothetical quotient:

```text
selector-changing menu edges                    4
selector-neutral menu edges                     4
changing edges requiring another route          2
total menu edges requiring a non-label route    6.
```

The current label method has total burden five: three external changing edges and two neutral edges. The quotient therefore increases the burden by one. Menu-state scalar burden remains four.

The global quotient contract has ten evidence fields; zero are populated.

## Current boundary

```text
accepted face-congruence pair types          0 of 3
source-discharged tied cases                 0 of 64
selected-state quotient fields               0 of 10
selected-state quotient accepted             0
promotion to recurrent closure               0
all_n_proved_by_checker                      0.
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_selector_face_closure_leverage.py
data/exact_recurrent_first_host_selector_face_closure_leverage.json
docs/exact-recurrent-first-host-selector-face-closure-leverage.md
docs/ERL_SELECTOR_FACE_CLOSURE_LEVERAGE_REVIEW_GATE.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
