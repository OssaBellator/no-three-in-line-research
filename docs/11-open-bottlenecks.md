# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. The authoritative theorem ledger reaches **CMR4469**. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

## 2. Canonical validation surface

```text
runner = scripts/run_prime_power_installed_construction_regression_1094.py
manifest = ae6023ffcf2eed5fca0e2cd1a3050b29d4db3098370f8bb39c8a0fd59aef376b
operation kinds = 1094
checker contracts = 41
owner-changing kinds = 164
same-owner kinds = 930
checkers = 75
```

## 3. Installed labelled moment/slack surface

Source CMR1830--CMR1893 installs exact host occupancy moments, label-weighted nested assignment LPs, diagonal-parity refinements, finite Pareto envelopes, an executable labelled manifest checker, exact rank-three slack classes, response-averaged line moments and hostwise residual line-budget allocation.

The certificate formats and finite host tables are exact. Complete labelled recurrent-state population and global strictness remain open.

## 4. Active frontier

```text
populate every surviving labelled recurrent state
attach actual background-height and provenance profiles
build one complete child-labelled coefficient row per state
combine exact rook, nested, moment, parity and occupancy bounds
allocate rank-three slack without double counting
solve strict positive integer labelled row inequalities
route every failed row to a finite residual class or strict descendant
```

## 5. Exact blockers

1. The executable assignment manifest is not populated for every recurrent state.
2. Actual background-height profiles are not yet certified across all geometric/provenance fibres.
3. Rank-three slack does not yet pay every lower-rank and return-selector row.
4. A complete positive-vector certificate for every labelled recurrent block is still missing.
5. Labelled SCCs must remain consistent through auxiliary elimination, CRT assembly and owner routing.
6. Global transition exhaustiveness and global termination remain open.

## 6. Validation boundary

```text
checker contract = locally reproduced
registry 1094 contract/census/seal = locally reproduced
runner 1094 manifest = locally reproduced
eight-entrypoint checker = not executed end to end locally
complete 75-checker runner = not executed locally
workflow success = not observed
```

Workflow configuration is not CI success. No local checker, manifest format or finite table substitutes for the missing populated strict recurrent certificate.
