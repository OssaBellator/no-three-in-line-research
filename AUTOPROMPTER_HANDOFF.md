# Autoprompter continuity handoff

## Current goal

Continue the prime-power/composite-modulus construction in literal source order while preserving exact ownership, validation and honesty boundaries. Source CMR1510--CMR1581 is fully installed through CMR4229. Source CMR1582--CMR1629 has now been audited and bound to one labelled recurrent-certificate checker. The next unit is operation-registry installation.

## Repository and branch

```text
repository = OssaBellator/no-three-in-line-research
branch = research/all-n-composite-modulus
authoritative theorem endpoint = CMR4229
```

The no-three-in-line conjecture remains open. Every checker and manifest preserves `all_n_proved_by_checker = 0`.

## Canonical installed stack

```text
782 operation kinds
36 checker contracts
164 owner-changing kinds
618 same-owner kinds
65 installed checkers
runner = scripts/run_prime_power_installed_construction_regression_782.py
manifest = 895657e67dddbb61d802cad364656428a51f729189d5f67f2a4876830e564c38
registry contract = b15c91825d0859a979f3953139554c2e2c81a1f68ea31d0b7d35a57437f0b946
registry seal = 8da81442b93b56c48054370aa1f36f47e9ce5acbe9e5b99f01c5e6a8fd62f91f
```

## Fully installed prior bank

```text
source = CMR1510--CMR1581
checker = scripts/check_prime_power_line_clean_return_core_ancestry.py
checker contract = 0a1620bf756ec529255be95c072a8435d870762644908a5000418d084948aec4
registry = scripts/check_prime_power_installed_operation_registry_782.py
runner = scripts/run_prime_power_installed_construction_regression_782.py
theorem endpoint = CMR4229
```

This bank installs target-safe line cleaning, repeated-token atomic rows, exact line-clean rook coefficients, selector-to-return splices, rooted trace execution and returned-edge exchange kernels. The recurrent inequalities remain open.

## Newly completed unit

### CMR1582--CMR1629 labelled recurrent-certificate checker

```text
checker = scripts/check_prime_power_labelled_recurrent_certificate_ancestry.py
contract = 9bac28f07137a18a997239686785729530c242bae0f4ca551bdddb8974d971a6
commit = 2291e6ebeb02057e9cdb1f8bc95e66a6a361630e
source files = 6
verifier entrypoints = 6
rejected fixture corruptions = 13
```

The checker binds:

```text
shared return-selector assignment scalarization
strict integer assignment-dual certificate format
strong/singleton/overlap line-clean integer budgets
critical selector rank/profile/geometric localization
prime-field singleton root support and fixed-interface splice
finite exact fixed-interface/thin rational row tables
label-preserving SCC reduction and CRT certificate gluing
```

The checker source and contract compile locally and its fixture mutation audit passes. The six inherited verifier programs have not been executed together in this environment.

## Decisions that must be preserved

1. Installed exhaustiveness is not global construction exhaustiveness.
2. Exact labels for collision, local-line, fixed-interface and CRT provenance must be retained until an honest upper quotient is proved.
3. Separate worst return and selector matchings may not be added; the installed object is one combined assignment score `g_ret + T g_sel`.
4. Line-clean integer budgets are exact tests, not proof that every geometric class has positive slack.
5. Critical selectors localize to finite classes; those classes are not yet certified.
6. Prime-field root translation reduces to reused support, return, side-one operations or one exact fixed-interface atom; it does not create a diffuse root row.
7. A finite thin-table compiler is not execution or certification of the required tables.
8. CRT gluing applies only after every labelled recurrent SCC has a strict certificate.
9. All global honesty flags remain zero unless directly proved.

## Exact current flags

```text
labelled_recurrent_certificate_ancestry_proved = 1

return_selector_assignment_certificate_complete = 0
line_clean_integer_budgets_positive_all_classes = 0
critical_selector_classes_certified = 0
required_thin_tables_executed_and_certified = 0
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
new checker source/contract = compiled and reproduced locally
new checker fixture audit = executed locally and passed
consolidated six-verifier checker = not executed end to end locally
registry 782 = previously executed locally and passed
complete 65-checker runner = not executed locally
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
1. register genuine CMR1582--CMR1629 assignment, budget, localization, support, table and labelled-assembly operations
2. validate the extended registry locally with corruption rejection
3. extend the canonical runner
4. add theorem chapters, live continuations and Python 3.10/3.12 workflows
5. synchronize STATUS.md, this handoff and docs/11-open-bottlenecks.md
6. continue in literal source order after CMR1629
```
