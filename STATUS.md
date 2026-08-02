# Status and honesty ledger

**Last updated:** 2 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4373**. Every checker, fixture, bridge, manifest and regression preserves `all_n_proved_by_checker = 0`.

## Canonical construction execution

```text
runner = scripts/run_prime_power_installed_construction_regression_974.py
manifest = 58a5c6eaa877331a9c4711835d9a3ce84c9def64001eea9ffb301325b7620be5
operation kinds = 974
checker contracts = 39
owner-changing kinds = 164
same-owner kinds = 810
installed checkers = 71
```

## Latest installed bank: CMR4326--CMR4373

Source CMR1702--CMR1773 installs:

```text
exact prescription rank-mass conservation
multiplicity-aware line-clean large-load thresholds
owner-support matching-number and vertex-cover capacities
small-support and prime-field reused-support thresholds
rank-one secant, rank-two line-load and rank-three injective multiplicities
exact packed secant bounds
labelled bounded-congestion background-triple charges
background-potential multiplicity bounds
exact line-energy profile census and profile charges
```

These results prove genuine strict-response regimes under explicit host, load, support, multiplicity and profile hypotheses. They do not prove those hypotheses cover every recurrent row.

## Canonical contracts and seals

```text
checker = 681a56e37003368e62a92ae7df349488e03e03eec34c2cddf2ab39b8d6622bdd
registry contract = 5bff249b3ada147307677bb59979f034b1c2587c4cc0a8643b903dbcd6eaf96e
registry seal = 240be08e0fe0e6e061d55a245cd544880b8612f9575099faa011e10d47ec77c6
71-checker manifest = 58a5c6eaa877331a9c4711835d9a3ce84c9def64001eea9ffb301325b7620be5
```

## Current exact flags

```text
rank_mass_multiplicity_line_energy_ancestry_proved = 1
installed_transition_kind_bank_974_exhaustive = 1
installed_payment_assignment_974_complete = 1
installed_transition_regression_974_complete = 1

all_line_clean_large_load_rows_closed = 0
all_owner_support_rows_closed = 0
geometric_multiplicity_caps_globally_sufficient = 0
triple_free_response_policy_globally_available = 0
line_energy_profile_rows_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Exact next source frontier

```text
docs/325-prime-power-geometric-orbit-fibre-correction.md
docs/326-prime-power-line-energy-marginal-rook-compiler.md
docs/327-prime-power-nested-assignment-line-energy-certificates.md
docs/328-prime-power-geometric-fibre-host-census-and-line-caps.md
docs/329-prime-power-exact-rank-three-geometric-fibre-census.md
docs/330-prime-power-line-occupancy-capacity-certificate.md
docs/331-prime-power-unified-outer-assignment-response-score.md
```

The next success criterion is an exact coordinate-labelled geometric fibre certificate or strict unified outer assignment, not matching normalization alone.

## Validation status

The checker contract, registry contract/census/seal and runner manifest were reproduced locally. The consolidated nine-verifier checker and complete 71-checker runner were not executed locally. Python 3.10/3.12 workflows are configured, but no successful workflow run has been observed and CI success is not claimed.
