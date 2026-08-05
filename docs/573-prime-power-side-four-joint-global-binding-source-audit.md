# Joint side-four global binding source audit

This post-ledger support artifact audits the source availability of every field required by the joint global binding input manifest. It introduces no theorem identifier after CMR4517.

```text
audit = data/prime_power_side_four_joint_global_binding_source_audit.json
audit seal = 0b469d33d245962f83f03a9f8969a2b64a17e34e39cd40f37d49d2c1b1f9f2a6
checker = scripts/check_prime_power_side_four_joint_global_binding_source_audit.py
binding input manifest = 743e049de6211b8333fcb2f85e03d9deb2204715a35d2e3a0a50423902edd870
```

## Field census

The required binding surface contains:

```text
2 parent records with 8 field occurrences
7 child records with 21 field occurrences
3 global records
2 row-completion records with 16 field occurrences
48 total field occurrences
```

The two explicit coordinate samples provide four exact local row inputs:

```text
zero local-line terms
zero geometric terms
blocker local-line terms
blocker geometric terms
```

These are marked `available-local-only`. They are not installed global recurrent-state bindings.

The remaining forty-four field occurrences lack an installed source. In particular:

```text
all parent recurrent-state keys and weights are missing
all parent transition and parent-rule provenance is missing
all seven child recurrent-state keys and installed weights are missing
all seven child transition-occurrence records are missing
weight normalization, recurrent-block identity and compatibility are missing
selector, collision and interface terms are missing for both rows
inner duals, outer duals and positive slack are missing for both rows
```

## Why no record can be populated yet

The installed owner/fate ancestry and labelled-assignment ancestry preserve:

```text
owner_fate_rows_populated_all_recurrent_states = 0
compulsory_weighted_certificates_complete = 0
actual_global_parent_rule_complete = 0
labelled_assignment_manifest_populated_all_recurrent_states = 0
complete_labelled_recurrent_lp_strict = 0
```

Therefore the exact local child classes cannot be promoted to installed global state keys or weights. The first complete parent or child binding record remains unavailable.

## Result

```text
result = installed-source-gap
first complete binding record available = 0
available local-only field occurrences = 4
missing installed-source field occurrences = 44
```

The next required source is a populated global recurrent-state manifest containing exact parent and child keys, positive installed weights and transition-occurrence provenance.

## Honesty boundary

```text
joint_global_binding_source_audit_complete = 1

binding_input_population_complete = 0
global_binding_constructed = 0
global_binding_incompatibility_proved = 0
joint_sample_global_recurrent_compatibility_proved = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker source was syntax-compiled before installation. Complete repository execution and workflow success remain separate validation steps.