# Status and honesty ledger

**Last updated:** 2 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4421**. Every checker, fixture, bridge, manifest and regression preserves `all_n_proved_by_checker = 0`.

## Canonical construction execution

```text
runner = scripts/run_prime_power_installed_construction_regression_1030.py
manifest = cb57bcbf2eb5278b8265975f948fec9970ba8539c4bc3c7e1ff12f5128d31626
operation kinds = 1030
checker contracts = 40
owner-changing kinds = 164
same-owner kinds = 866
installed checkers = 73
```

## Latest installed bank: CMR4374--CMR4421

Source CMR1774--CMR1829 installs:

```text
matching-versus-geometric orbit correction
exact coordinate-labelled geometric fibres and honest upper-fibre rows
exact line-energy marginal rook numerators
nested rank-two and rank-three assignment certificates
740 raw side-four/five geometric hosts
exact denominator-specific rank-three fibre tables
line-occupancy assignment capacities
one unified outer return-selector-geometric response score
```

The matching-fibre layer contains 86 side-four and 654 side-five raw hosts. Matching denominators may be reused inside a fibre; Euclidean numerators and labelled offspring rows remain fibre-specific.

## Canonical contracts and seals

```text
checker = f03ab61fabb4ad8727f239a31474466f3074f2397762a63fd4255c683176e3eb
registry contract = c93c2c8d69260ecc2c2c4b0709af26c16a9c054b2ec7f85f4cea83a36dcb8084
registry seal = 60172375358504d3c697b73cf45d0d7df60441a01f09a0fa46140d720852245b
73-checker manifest = cb57bcbf2eb5278b8265975f948fec9970ba8539c4bc3c7e1ff12f5128d31626
```

## Current exact flags

```text
geometric_fibre_outer_assignment_ancestry_proved = 1
installed_transition_kind_bank_1030_exhaustive = 1
installed_payment_assignment_1030_complete = 1
installed_transition_regression_1030_complete = 1

geometric_fibre_rows_complete_all_provenance = 0
rank_one_two_geometric_fibre_rows_subcritical = 0
unified_outer_assignment_globally_strict = 0
all_labelled_recurrent_blocks_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Exact next source frontier

```text
docs/332-prime-power-geometric-fibre-occupancy-moment-census.md
docs/333-prime-power-label-weighted-unified-assignment-lp.md
docs/334-prime-power-diagonal-parity-line-occupancy-census.md
docs/335-prime-power-geometric-fibre-moment-pareto-envelopes.md
docs/336-prime-power-labelled-assignment-certificate-manifest.md
docs/337-prime-power-rank-three-fibre-slack-classification.md
docs/338-prime-power-exact-response-averaged-line-moment-census.md
docs/339-prime-power-rank-three-slack-line-budget-allocation.md
```

The next success criterion is an exact labelled recurrent LP or strict moment/slack allocation certificate on the coordinate-labelled fibre catalogue.

## Validation status

The checker contract, registry contract/census/seal and runner manifest were reproduced locally. The consolidated seven-verifier checker and complete 73-checker runner were not executed locally. Python 3.10/3.12 workflows are configured, but no successful workflow run has been observed and CI success is not claimed.
