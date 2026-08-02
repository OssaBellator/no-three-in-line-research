# Status and honesty ledger

**Last updated:** 2 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4469**. Every checker, fixture, manifest and regression preserves `all_n_proved_by_checker = 0`.

## Canonical construction execution

```text
runner = scripts/run_prime_power_installed_construction_regression_1094.py
manifest = ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b
operation kinds = 1094
checker contracts = 41
owner-changing kinds = 164
same-owner kinds = 930
installed checkers = 75
```

## Latest installed bank: CMR4422--CMR4469

Source CMR1830--CMR1893 installs:

```text
exact geometric-host occupancy moment vectors
label-weighted unified nested assignment LPs
diagonal-parity line-occupancy laws
finite moment Pareto envelopes and active-height phases
an executable labelled assignment certificate manifest
exact rank-three fibre slack classes
exact response-averaged line moments
rank-three residual line-budget allocation
```

These interfaces reduce the surviving computation to actual background-height and provenance population. They do not assert that every recurrent state already has a complete strict labelled row.

## Canonical contracts and seals

```text
checker = fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f
registry contract = df6134106c292aa93711dcb060e013b6c6d700cc65813ae1943af2bdc8cb260f
registry seal = a4d652ef07e5a78e53d7b674e0fc50b97e714e2797270db72fe540a26d40bbb5
75-checker manifest = ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b
```

## Current exact flags

```text
labelled_moment_slack_assignment_ancestry_proved = 1
installed_transition_kind_bank_1094_exhaustive = 1
installed_payment_assignment_1094_complete = 1
installed_transition_regression_1094_complete = 1

labelled_assignment_manifest_populated_all_recurrent_states = 0
rank_three_slack_allocates_all_geometric_rows = 0
actual_background_height_profiles_certified = 0
complete_labelled_recurrent_lp_strict = 0
all_labelled_recurrent_blocks_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Exact next mathematical frontier

Continue after CMR1893 by populating the executable labelled recurrent certificate rather than adding another abstract interface:

```text
enumerate every surviving labelled recurrent state and its parent weight
attach the actual background-height, owner, collision, line, interface and CRT profile
build one complete child-labelled coefficient row per state
use exact rook, nested-assignment, moment, parity and occupancy bounds per row
allocate rank-three slack to lower-rank and return-selector terms without double counting
search and publish strict positive integer row inequalities
route every failed row to an explicit residual class or strict descendant
```

The next success criterion is a populated strict labelled manifest for a nontrivial complete recurrent block, or an exact finite residual worklist identifying every row that still fails.

## Validation status

The checker contract, registry contract/census/seal and runner manifest were reproduced locally. The consolidated eight-entrypoint checker and complete 75-checker runner were not executed locally. Python 3.10/3.12 workflows are configured, but no successful workflow run has been observed and CI success is not claimed.
