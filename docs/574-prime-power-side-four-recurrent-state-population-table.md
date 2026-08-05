# Side-four recurrent-state population table

The joint side-four binding work now has a checked population-table interface.
It is deliberately empty: the installed ancestry sources do not yet supply a
qualifying recurrent-state population record.

## Table contract

The table targets exactly two parent records and seven exact child classes.
Parent records require an exact recurrent-state key, positive installed weight,
transition-occurrence provenance, parent-rule provenance, recurrent-block ID
and normalization ID. Child records require the same fields except parent-rule
provenance, plus the exact child class.

The two rank-one `return:00` targets remain distinct because their full class
keys differ. Local weight aliases are not accepted as recurrent-state keys.

## Current checked state

```text
population_table_schema_complete = 1
parent_records_populated = 0
child_records_populated = 0
first_manifest_record_populated = 0
binding_input_population_complete = 0
global_binding_constructed = 0
global_binding_incompatibility_proved = 0
all_n_proved_by_checker = 0
```

An empty table records missing installed population data. It is neither a
constructive binding nor an incompatibility certificate. The local witness with
parent weights 16 and child weights 1 must not be inserted as installed data.

The executable checker is
[`scripts/check_prime_power_side_four_recurrent_state_population_table.py`](../scripts/check_prime_power_side_four_recurrent_state_population_table.py).
The table is
[`data/prime_power_side_four_recurrent_state_population_table.json`](../data/prime_power_side_four_recurrent_state_population_table.json).

## Next admissible increment

Add one repository-proven parent or child record with every required field and
update the population counts and first-record flag. A coordinate sample, local
alias, unproved weight, or provenance-free state label is rejected.
