# Side-four operation registry instance gap

The installed 1166-kind operation registry is an exhaustive registry of operation kinds through CMR1965. Its records contain operation-kind names, theorem sources, owner effects, payment classes, continuations and contract seals.

That registry is not a table of recurrent transition instances. In particular, it does not provide the exact recurrent-state keys, installed weights, transition-occurrence witnesses, normalization identifiers, recurrent-block identifiers or parent-rule witnesses required by the side-four population candidate envelope.

The checked contract is `data/prime_power_side_four_operation_registry_instance_gap_contract.json`, and the checker is `scripts/check_prime_power_side_four_operation_registry_instance_gap.py`.

The result is a typed source exclusion:

```text
installed operation kinds = 1166
new owner/fate operation kinds = 72
instance population fields present = 0
registry_instance_gap_checked = 1
first_manifest_record_populated = 0
global_binding_constructed = 0
global_binding_incompatibility_proved = 0
all_n_proved_by_checker = 0
```

This does not show that a recurrent-state population table cannot exist. It shows only that operation-kind exhaustiveness does not supply transition-instance provenance and therefore cannot populate the first candidate record by itself.
