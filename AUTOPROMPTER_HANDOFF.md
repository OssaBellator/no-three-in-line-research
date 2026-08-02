# Autoprompter continuity handoff

## Current goal

Continue the prime-power/composite-modulus construction in literal source order while preserving exact ownership, validation and honesty boundaries. Source CMR1510--CMR1581 is fully installed through CMR4229. A pre-existing but unindexed canonical implementation for source CMR1582--CMR1629 has now been audited and adopted. The next unit is theorem-ledger installation, workflows and authoritative status synchronization.

## Repository and branch

```text
repository = OssaBellator/no-three-in-line-research
branch = research/all-n-composite-modulus
authoritative theorem endpoint = CMR4229
```

The no-three-in-line conjecture remains open. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

## Last fully indexed stack

```text
782 operation kinds
36 checker contracts
164 owner-changing kinds
618 same-owner kinds
65 installed checkers
runner = scripts/run_prime_power_installed_construction_regression_782.py
manifest = 895657e67dddbb61d802cad364656428a51f729189d5f67f2a4876830e564c38
```

## Canonical unindexed 830 stack now adopted

```text
checker = scripts/check_prime_power_recurrent_certificate_assembly_ancestry.py
checker contract = 195b9f8ce43391860ea28b7b0d882250fc0f13222b16e67f432c786cc2d80285
registry = scripts/check_prime_power_installed_operation_registry_830.py
registry contract = e533e625b1f430ba72eb6c0c3a5821cbe9c0316e0d1284d65becc4f3e00c7e67
registry seal = ab7be2d96abc4c31d70cbc2c13db579eb417474bdb6944a0d48bea83537cc362
runner = scripts/run_prime_power_installed_construction_regression_830.py
67-checker manifest = 9fe8e73ea57a7386c9c90d637d02037f5d96018ab904218f08f4fbec78446583
```

```text
48 new same-owner operation kinds
830 installed operation kinds
37 checker contracts
164 owner-changing kinds
666 same-owner kinds
67 installed checkers
```

The canonical checker binds CMR1582--CMR1629:

```text
shared return-selector assignment scalarization
strict rational/integer assignment-dual certificate format
strong/singleton/overlap line-clean integer budgets and slacks
critical selector finite profile/geometric localization
prime-field singleton root support and exact fixed-interface splice
finite rational fixed-interface/thin table compiler
label-preserving SCC reduction and CRT certificate gluing
```

The checker contract, registry contract, registry seal and chained runner manifest were reproduced locally. The registry validation logic and all fourteen declared corruption mutations were reproduced locally and passed. The six inherited verifier programs and complete 67-checker runner were not executed end to end in this environment.

## Reconciliation decision

A parallel checker created during this work pass was redundant with the canonical pre-existing implementation and was removed in commit:

```text
a53d9edc1623ab692917696dc79a94e9c102d709
```

Do not restore or register `scripts/check_prime_power_labelled_recurrent_certificate_ancestry.py`. The canonical checker is `scripts/check_prime_power_recurrent_certificate_assembly_ancestry.py` with contract `195b9f8c...`.

## Decisions that must be preserved

1. Installed exhaustiveness is not global construction exhaustiveness.
2. Separate worst return and selector matchings may not be added; use one combined score `g_ret + T g_sel`.
3. Line-clean integer budgets are exact tests, not proof that all geometric classes have positive slack.
4. Critical selector localization produces a finite worklist, not closure of those classes.
5. Prime-field root translation reduces to reused support, return, side-one operations or one exact fixed-interface atom.
6. A finite thin-table compiler is not execution or certification of required tables.
7. Collision, local-line, fixed-interface and CRT labels must be retained until an honest upper quotient is proved.
8. CRT gluing applies only after every labelled recurrent SCC has a strict certificate.
9. All CMR1582--CMR1629 registry operations preserve structural owner.
10. Workflow configuration is not CI success.
11. All global honesty flags remain zero unless directly proved.

## Exact current flags

```text
recurrent_certificate_assembly_ancestry_proved = 1
installed_transition_kind_bank_830_exhaustive = 1
installed_payment_assignment_830_complete = 1
installed_transition_regression_830_complete = 1

return_selector_assignment_dual_globally_strict = 0
line_clean_integer_slacks_globally_positive = 0
critical_selector_classes_closed = 0
fixed_interface_thin_table_subcritical = 0
labelled_crt_recurrent_blocks_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## Validation boundary

```text
checker contract = reproduced locally
registry contract/seal/census = reproduced locally
registry corruption audit = reproduced locally and passed
runner 830 manifest = reproduced locally
six-verifier checker = not executed end to end locally
complete 67-checker runner = not executed locally
workflow success = not observed
```

## Uncommitted work

```text
uncommitted repository files = none known
uncommitted generated artifacts = none known
```

No completed implementation exists only in chat.

## Exact next steps

```text
1. add theorem chapters for the canonical 830 checker, registry and runner
2. add live theorem-index continuations and Python 3.10/3.12 workflows
3. synchronize STATUS.md, this handoff and docs/11-open-bottlenecks.md
4. resolve the exact literal source frontier after CMR1629
```
