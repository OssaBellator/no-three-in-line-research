# Autoprompter continuity handoff

## Current goal

Repair the installed CMR1894--CMR1965 owner/fate-lineage-kernel bank so its declared source chapters and verifier entrypoints actually exist, then revalidate the 1166-kind stack without weakening honesty boundaries.

## Repository state

```text
repository = OssaBellator/no-three-in-line-research
branch = research/all-n-composite-modulus
authoritative indexed theorem endpoint = CMR4517
```

The no-three-in-line conjecture remains open. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

## Canonical indexed stack

```text
1166 operation kinds
42 checker contracts
164 owner-changing kinds
1002 same-owner kinds
77 installed checkers
runner = scripts/run_prime_power_installed_construction_regression_1166.py
manifest = 6bea37ee2abf2a6eff122fcf07bcd11348b6dc39378e8bab94f290d41e93d2c3
registry contract = 29d41e186b0ab1be5b755f6c751a0cbb6ef6db89574e8f39f91ff1325e24be9f
registry seal = cfdc409b28c15ff3a421d0d2cbed1592ac8d5c5d7404d87958c14cc245f4799e
```

## Installed CMR1894--CMR1965 layer

```text
checker = scripts/check_prime_power_owner_fate_lineage_kernel_ancestry.py
contract = a81184108c06638fe3b44754b80c0fe271d8a92d7b78db6befb681890dd810eb
registry = scripts/check_prime_power_installed_operation_registry_1166.py
runner = scripts/run_prime_power_installed_construction_regression_1166.py
ledger = CMR4470--CMR4517
```

## Current blocker

The checker, registry, runner, theorem chapters, live continuations and workflows exist, but all nine source chapters and all nine verifier entrypoints declared by the checker currently return 404 on the branch:

```text
docs/340-prime-power-owner-fate-collision-class-compression.md
scripts/verify_prime_power_owner_fate_class_compression.py

docs/341-prime-power-compulsory-weighted-assignment-certificates.md
scripts/verify_prime_power_compulsory_weighted_assignment.py

docs/342-prime-power-slack-preconditioned-assignment-manifest.md
scripts/verify_prime_power_slack_preconditioned_manifest.py

docs/343-prime-power-complete-line-energy-kernel.md
scripts/verify_prime_power_complete_line_energy_kernel.py

docs/344-prime-power-background-increment-line-energy-kernel.md
scripts/verify_prime_power_background_increment_kernel.py

docs/345-prime-power-line-energy-selector-stability.md
scripts/verify_prime_power_line_energy_selector_stability.py

docs/346-prime-power-background-normalized-line-energy-kernel.md
scripts/verify_prime_power_background_normalized_kernel.py

docs/347-prime-power-raw-fibre-background-lineage.md
scripts/verify_prime_power_raw_fibre_background_lineage.py

docs/348-prime-power-rank-three-zero-response-blockers.md
scripts/verify_prime_power_rank_three_zero_response_blockers.py
```

Therefore the complete nine-verifier checker and the 77-checker runner are not currently executable from the branch even though their interfaces are indexed.

## Decisions to preserve

1. Owner/fate/collision/local-line/interface/provenance compression is lossless only with the full declared key.
2. Dropping fate or geometric labels may create artificial recurrent loops; incomplete fibres use componentwise maxima only.
3. Every compulsory weighted coefficient, child weight, inner dual and allowed outer edge must be present.
4. Rank-three slack is allocated once inside the same row; negative, duplicate or unallocated claimed slack is invalid.
5. Complete line-energy kernels retain exact background and response line profiles.
6. Selector stability is conditional on accumulated perturbation remaining below the response gap; ties retain the exact minimizer face.
7. Raw-fibre lineage must identify the coordinate-labelled host, target, background and response family.
8. All 72 CMR1894--CMR1965 registry operations preserve structural owner.
9. Workflow configuration is not CI success.

## Exact current flags

```text
owner_fate_lineage_kernel_ancestry_proved = 1  # indexed interface only until dependencies are restored
installed_transition_kind_bank_1166_exhaustive = 1
installed_payment_assignment_1166_complete = 1
installed_transition_regression_1166_complete = 1  # runner interface only; execution not observed

owner_fate_rows_populated_all_recurrent_states = 0
compulsory_weighted_certificates_complete = 0
raw_fibre_backgrounds_cover_all_provenance = 0
rank_three_zero_blockers_globally_resolved = 0
complete_labelled_recurrent_lp_strict = 0
all_labelled_recurrent_blocks_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Validation boundary

```text
1166 checker contract = present
1166 registry contract/seal/census = present
1166 runner manifest = present
nine declared source chapters = missing
nine declared verifier entrypoints = missing
complete owner/fate checker = not executable until repair
complete 77-checker runner = not executed
workflow success = not observed
```

## Uncommitted work

```text
uncommitted repository files = none known
uncommitted generated artifacts = none known
```

## Exact next steps

```text
1. reconstruct each missing source chapter from its literal CMR1894--CMR1965 contract and installed registry operations
2. add one independently executable arithmetic/finite-structure verifier per chapter
3. commit and push each completed source/verifier pair promptly
4. execute all nine verifiers and the consolidated checker locally against the reconstructed tree
5. synchronize STATUS.md, this handoff and docs/11-open-bottlenecks.md to the repaired 1166 stack
6. continue in literal source order after CMR1965
```
