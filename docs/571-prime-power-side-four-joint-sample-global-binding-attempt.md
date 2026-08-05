# Joint side-four sample global binding audit

This post-ledger support artifact audits whether the two exact side-four sample parent rows and their seven exact return-child classes can be bound to the currently installed global recurrent Lyapunov system. It introduces no theorem identifier after CMR4517.

```text
contract = data/prime_power_side_four_joint_sample_global_binding_attempt_contract.json
contract seal = 2cafda35faf9e888828cbe531e0274fea3f82b79275adece31e745b1248cf85d
checker = scripts/check_prime_power_side_four_joint_sample_global_binding_attempt.py
joint sample source = 1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5
```

## Audit surface

The checker binds and inspects:

```text
canonical 77-checker runner manifest
the labelled moment/slack/assignment ancestry contract
the standalone labelled assignment certificate validator
the 1166-kind operation registry
the exact two-parent, seven-child joint sample namespace
```

The installed labelled certificate checker has two modes:

1. with no argument it validates a built-in one-state example and mutation tests;
2. with a JSON path it validates an externally supplied completed manifest.

The canonical runner and ancestry checker preserve:

```text
labelled_assignment_manifest_populated_all_recurrent_states = 0
complete_labelled_recurrent_lp_strict = 0
```

The operation registry enumerates operation kinds and payment classes. It is not a populated recurrent-state or state-weight manifest.

## Exact binding attempt

The audit covers exactly nine bindings:

```text
two parent recurrent-state keys
seven exact child-class global weight bindings
```

All seven child attempts use the complete exact class identifiers. Local weight aliases are not accepted as global keys.

No binding is available from the installed canonical stack. The result is therefore:

```text
outcome = residual-not-incompatible
global binding succeeded = 0
mathematical incompatibility proved = 0
```

This means the repository presently lacks the populated global manifest required to decide these bindings. It does not mean that no compatible global Lyapunov vector exists.

## Remaining obligations

```text
publish exact global recurrent state keys for both sample parents
publish exact global state keys and positive weights for all seven child classes
publish one complete labelled coefficient manifest containing the two parent rows
bind selector, collision and interface terms for both rows
prove that the sample transitions occur in the global recurrence
verify compatibility with one common global normalization
```

## Honesty boundary

```text
joint_sample_global_binding_audit_complete = 1

joint_sample_global_weight_bindings_complete = 0
joint_sample_global_incompatibility_proved = 0
joint_sample_global_recurrent_compatibility_proved = 0
joint_sample_full_compulsory_rows_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker source was syntax-compiled before installation. Complete repository execution and workflow success remain separate validation steps.