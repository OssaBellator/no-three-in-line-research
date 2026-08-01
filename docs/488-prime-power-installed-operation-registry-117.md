# The installed construction registry contains one hundred seventeen exact operation kinds

This chapter records **CMR3446--CMR3457**.

Executable registry:

```text
scripts/check_prime_power_installed_operation_registry_117.py
```

## CMR3446 — immutable ninety-eight-kind base

The extension binds registry seal

```text
4732c504824406c78b9a9e92033994f30be1c744e633a5e49dcc5531497e00ae
```

with 98 operation kinds, 20 checker contracts and 36 owner-changing kinds. The historical 110-kind checkpoint remains a narrower validation layer and is not used as the base seal of this superseding registry.

## CMR3447 — disjoint-conflict operations

```text
disjoint-conflict-local-deletion
disjoint-conflict-fully-forced-dispatch
disjoint-conflict-private-restoration-payment
```

## CMR3448 — protected-contact operations

```text
protected-contact-finite-stock
protected-contact-wall-extraction
protected-contact-heavy-token
protected-contact-dispersed-token-bank
protected-contact-reintroduction-payment
protected-contact-persistent-dispatch
```

## CMR3449 — recurrent-set operations

```text
recurrent-unavailable-set-extraction
recurrent-set-aggregate-reintroduction
recurrent-set-batch-absorption
recurrent-set-small-cover-wall
```

## CMR3450 — slack/core operations

```text
weak-slack-near-static-dispatch
persistent-core-amplification
```

## CMR3451 — owner-labelled certificate operations

```text
owner-labelled-protected-state-stock
owner-labelled-line-stock
owner-labelled-token-edge-stock
owner-labelled-certificate-recurrence
```

## CMR3452 — exact ancestry and contract binding

All nineteen entries bind nonempty CMR577--CMR604 ancestry and contract:

```text
b82d83290aa95e41743fe1db9dbbf3a26c09801f40888e42cc1c8e0f0eefd0f0
```

## CMR3453 — owner effects

```text
1 host-owner-change
3 restoration-owner-change
15 same-owner operations
```

The local deletion changes the literal host. Reintroduction changes the restoration owner. Protected growth remains a strict same-owner matching enlargement.

## CMR3454 — payment classes

```text
1 local-family-restriction
3 edge-reintroduction
7 owner-witness-stock
2 protected-core-growth
6 scheduler-dispatch
```

## CMR3455 — installed census

```text
117 operation kinds
21 checker contracts
40 owner-changing kinds
77 same-owner kinds
```

## CMR3456 — corruption rejection and seals

Eleven independent mutations are rejected.

```text
contract = 4c961b63515c0a8ac986f9ab0a11cef7ad33df3d012fbbe0ca23bcf95a2324eb
registry = 043cc0dfdc5f9509de81da436df1aec8579a7803623d0ace54d6d0dd6904bfdf
```

## CMR3457 — honesty boundary

```text
installed_transition_kind_bank_117_exhaustive = 1
selector_protected_certificate_operations_registered = 1
installed_payment_assignment_117_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Installed-bank exhaustiveness is not global construction exhaustiveness.
