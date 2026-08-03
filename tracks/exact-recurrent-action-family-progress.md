# Exact recurrent action-family progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records uniform source certificates for directed restoration-action families after the physical transition-domain and state-exclusion audits.

## ERL2l — directed family quotient

The eight symbolic menu edges split into four two-edge families:

```text
restore_02: 00->10, 01->11
delete_02:  10->00, 11->01
restore_20: 00->01, 10->11
delete_20:  01->00, 11->10.
```

A family certificate is valid only when one source theorem closes both context edges through the same accepted physical route schema. Shared cell/action labels alone do not establish uniformity.

## ERL2m — exact family leverage

All sixteen family subsets were classified against the six label-scalar and fourteen menu-scalar residual covers.

The four minimum complete sets are

```text
restore_02 + restore_20
restore_02 + delete_20
delete_02  + restore_20
delete_02  + delete_20.
```

Each contains exactly one label cover and one menu cover. Equivalently, two uniform family certificates suffice precisely when they choose one directed family for each restoration bit.

Closing both directions of only one bit does not suffice. The other bit leaves two menu reversal pairs uncovered.

Exact census:

```text
directed families                         4
family subsets                           16
two-family subsets                        6
two-family label shortcuts                4
two-family menu shortcuts                 4
minimum families for label closure        2
minimum families for menu closure         2.
```

## ERL2n — family congruence obstruction

The two member edges of each family were joined to exact selected responses, gaps, complete minimizer-face profiles and the exact first-host automorphism group.

Exact census:

```text
families homogeneous in changed cell/action      4
families homogeneous in selector-change flag     2
families homogeneous in ordered selected pair    0
families homogeneous in ordered gap pair         0
families homogeneous in ordered face profile     0
families related by exact host automorphism       0
families touching state 11                       4.
```

The `20` families contain one selector-changing and one selector-neutral edge. The `02` families have a common selector-change flag but distinct ordered selected-response pairs. Every family contains one edge incident to state `11`, whose complete minimizer face has the exact 8/24 background split.

Therefore same changed cell and action do not imply one context-free operation row. A family proof must either provide two complete member-edge records or a theorem explicitly quantified over both values of the other restoration bit.

The context-parametric theorem has a ten-field source contract covering its edge references, quantified context, owner schema, operation schema, route schema, child/payment compatibility and realization status.

## Current source boundary

```text
source-closed action families                 0
source-uniformity records                     0
source-closed edges through families          0
complete scalar covers through families       0
physical transition domain known              0
operation/payment congruence proved            0
promotion to recurrent closure allowed        0
all_n_proved_by_checker                        0.
```

The next source-facing shortcut is concrete but strict: prove one context-parametric route theorem for either restore/delete `02`, and one for either restore/delete `20`. Each must cover both member edges with occurrence, owner, endpoint, operation, trace, legality and route-specific evidence.

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_action_family_route_leverage.py
data/exact_recurrent_first_host_action_family_route_leverage.json
docs/exact-recurrent-first-host-action-family-route-leverage.md

scripts/check_exact_recurrent_first_host_action_family_congruence_obstruction.py
data/exact_recurrent_first_host_action_family_congruence_obstruction.json
docs/exact-recurrent-first-host-action-family-congruence-obstruction.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
