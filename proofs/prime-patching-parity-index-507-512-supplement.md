# Prime-patching parity index supplement: `docs/507--512`

This supplement continues the cumulative parity index after `docs/506`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ciz--PP3cjb | Based marker-cycle mixtures admit largest-remainder quantization, deterministic periodic realization, and explicit rational rate-error certificates | PROVED | `docs/507-quantized-cycle-mixtures-for-marker-flows.md` |
| PP3cjc--PP3cje | Repeated Hall syndrome blocks have exact Walsh powers, exponential uniformity tails, and finite reverse-load mixing horizons | PROVED | `docs/508-spectral-mixing-bounds-for-repeated-hall-blocks.md` |
| PP3cjf--PP3cjh | Rational threshold schedule matrices admit two-margin integral rounding, additive-potential quotient bounds, and residual matching certificates | PROVED | `docs/509-conservative-matrix-rounding-for-threshold-schedules.md` |
| PP3cji--PP3cjk | Unequal-survival prefix codes under regular-language constraints admit exact automaton--multiplicity dynamic programming and reconstruction | PROVED | `docs/510-regular-language-constrained-prefix-code-dp.md` |
| PP3cjl--PP3cjn | Shell chamber gaps give exact perturbation radii, denominator thresholds, and localized quantization-stability witnesses | PROVED | `docs/511-quantization-stability-inside-shell-chambers.md` |
| PP3cjo--PP3cjq | Critical interaction cycles admit finite residue-corrector shortest paths and exact all-length scalar and vector formulas | PROVED | `docs/512-residue-correctors-for-finite-interaction-lengths.md` |

## Frontier update

### Boundary recleaning

Real or high-denominator marker cycle mixtures now have finite deterministic
implementations.  The stored target mixture `(7/20,1/3,19/60)` has action rate
`(21/89,30/89,38/89)`.  Denominator 17 gives period 50 and rate
`(6/25,9/25,2/5)`; denominator 60 is exact with period 178.  Every denominator
through 120 satisfies the exact cycle-ratio error certificate.

### Localized Hall transport

Repeated Hall blocks now have a spectral stopping rule.  The stored rank-three
block has Walsh spectrum `(10,0,2,0,2,0,2,0)` and nontrivial radius `1/5`.
Its exact deviations from uniformity are `3/(8*5^n)`, so three blocks are both
necessary and sufficient for the one-percent target.  With Hall degree 20, the
certified load envelope is `4/625`.

### Fractional direct-clean layers

Threshold schedules can now preserve exact source totals and exact global action
totals simultaneously.  The stored `3 x 4` matrix at denominator four has eight
fractional residual edges and exactly three conservative integral roundings.
The selected rounding has row totals `(4,4,4)` and column totals `(4,3,3,2)`.
Load error ignores every additive row-plus-column potential exactly.

### Support-chord repair words

Finite automata now constrain the marker words during prefix-code optimization.
For the language avoiding `00`, survivals `(3/4,2/3)`, risks
`(1/32,1/16,1/8)`, and multiplicities `(3,2,1)`, the unconstrained optimum
`3/16` becomes the exact legal optimum `243/1024`.  The stored recurrence has 26
feasible product states and reconstructs one six-word legal code.

### Clean-macro shells

Quantized shell targets now retain their active chamber once the denominator
exceeds a computable dual-gap threshold.  At `(3/5,1/2,2/5)`, the central chamber
has gap `3/20` and dual radius `3/2`, so every denominator at least 11 preserves
the same dual vertex and marginal prices.  The audit checks denominators through
100.

### Integration

The asymptotic critical interaction cycle now has exact finite-length residue
correctors.  The stored length-two cycle `BC` has mean `5/2`; residue defects are
`0` and `1/2`.  Thus `(BC)^(N/2)` is optimal for every even length and
`A(BC)^((N-1)/2)` is optimal for every odd length, with exact odd overhead
`1/(2N)`.  Independent dynamic programming verifies every length through 64.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_507_512.py
```

or individually with

```bash
python scripts/check_quantized_marker_cycle_mixtures.py
python scripts/check_spectral_hall_mixing_bounds.py
python scripts/check_conservative_matrix_rounding.py
python scripts/check_regular_language_prefix_code_dp.py
python scripts/check_shell_chamber_quantization_stability.py
python scripts/check_interaction_residue_correctors.py
```

The local audits verify 120 marker denominators, twelve exact Walsh powers, all
256 residual rounding choices, the complete regular-language product recurrence,
100 shell denominators, and every interaction length through 64.

The next available theorem identifier is `PP3cjr`.
