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

## Current source boundary

```text
source-closed action families             0
source-closed edges through families      0
complete scalar covers through families   0
physical transition domain known          0
promotion to recurrent closure allowed    0
all_n_proved_by_checker                    0.
```

The next source-facing shortcut is therefore concrete: prove one uniform route theorem for either restore/delete `02`, and one for either restore/delete `20`. Each theorem must populate both member edges with occurrence, owner, endpoint, operation, trace, legality and route-specific evidence.

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_action_family_route_leverage.py
data/exact_recurrent_first_host_action_family_route_leverage.json
docs/exact-recurrent-first-host-action-family-route-leverage.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```
