# Side-four joint global binding input manifest

The prior checked global binding attempt ended with the result `underdetermined`. This chapter makes the missing input surface exact.

## Theorem CMR4518 -- PROVED

A global binding attempt for the two side-four sample rows requires exactly two parent records. Each parent record contains an exact installed recurrent-state key, installed parent weight, transition-occurrence provenance and parent-rule provenance.

## Theorem CMR4519 -- PROVED

The seven exact child classes remain seven distinct global binding records. In particular, the two scoped uses of the local alias `w_return_00_rank1` are not merged.

## Theorem CMR4520 -- PROVED

Each child binding record contains an exact recurrent-state key, installed child weight and transition-occurrence provenance.

## Theorem CMR4521 -- PROVED

A completed global attempt also contains a weight normalization, recurrent-block identifier and recurrent-block compatibility certificate.

## Theorem CMR4522 -- PROVED

Complete strictness of either sampled row additionally requires selector, collision, interface, local-line and geometric terms, all inner duals, one outer dual and positive slack. Return-only local feasibility is insufficient.

## Current population boundary

The manifest is complete as an interface, but none of its parent, child, global or complete-row records is populated from the installed recurrence. Therefore it proves neither a global binding nor a global incompatibility.

```text
binding_input_manifest_complete = 1
binding_input_population_complete = 0
global_binding_constructed = 0
global_binding_incompatibility_proved = 0
joint_sample_global_recurrent_compatibility_proved = 0
all_n_proved_by_checker = 0
```

The executable contract check is implemented in [`scripts/check_prime_power_side_four_joint_global_binding_input_manifest.py`](../scripts/check_prime_power_side_four_joint_global_binding_input_manifest.py).
