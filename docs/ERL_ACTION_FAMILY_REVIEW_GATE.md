# ERL action-family review gate

A proposed first-host family theorem is admissible only if all conditions below hold.

- The family is exactly one of `restore_02`, `delete_02`, `restore_20`, `delete_20`.
- Both context edges listed in `data/exact_recurrent_first_host_action_family_route_leverage.json` are covered.
- Each member edge has a physical occurrence, persistent owner, source and target state, operation kind, registry entry, trace, changed cell, action, legality proof, intermediate states and realization status.
- Each member edge passes one accepted closure route from the closure-route source gate.
- Any claimed shared capacity, potential, output theorem or reset schema is proved uniform across both members.
- No family certificate is inferred from one member edge or from fixture restoration at another side.

For scalar closure, the accepted family set must contain one directed family for bit `02` and one directed family for bit `20`.

The four minimum accepted sets are:

```text
restore_02 + restore_20
restore_02 + delete_20
delete_02  + restore_20
delete_02  + delete_20.
```

Both directions of only one bit are insufficient.

Current accepted family certificates: **0**.

This gate does not authorize physical transition legality, recurrent child rows, strict Lyapunov closure, global termination or `all_n_proved_by_checker=1`.
