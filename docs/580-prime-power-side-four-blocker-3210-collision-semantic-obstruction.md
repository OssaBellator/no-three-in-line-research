# Blocker response 3210 collision semantic obstruction

This unit attempts the next required collision-offspring step for the blocker sample

```text
host = s4-75b04c45c1c8eac2
response = 3210
response edges = 03,12,21,30
collision/deletion trace = 02,20
blocker = b4-8a44614df456
```

The response avoids both deleted edges and the target edge `01`. Its reoptimized return routing is already exact, with one `return:22` rank-three charge and three `return:33` rank-three charges. Those return charges do not determine collision offspring or collision multiplicity.

The installed artifacts do not currently define the instance-level semantic map needed to enumerate physical collision offspring. Six inputs remain missing:

```text
collision event domain
physical offspring constructor
collision multiplicity rule
owner/fate/collision child-key constructor
interface/provenance constructor
global transition-occurrence witness
```

Therefore the correct result is a checked semantic-input obstruction, not a zero collision coefficient and not a collision incompatibility proof.

Canonical files:

```text
data/prime_power_side_four_blocker_3210_collision_semantic_obstruction.json
scripts/check_prime_power_side_four_blocker_3210_collision_semantic_obstruction.py
```

The checker verifies the exact response and deletion data, confirms the existing return charges, checks all six missing semantic inputs, and preserves:

```text
semantic_input_obstruction_complete = 1
physical_collision_offspring_enumerated = 0
collision_multiplicities_complete = 0
collision_child_keys_complete = 0
collision_coefficient_complete = 0
collision_child_weight_binding_complete = 0
global_transition_occurrence_complete = 0
collision_incompatibility_proved = 0
all_n_proved_by_checker = 0
```

A future enumerator must supply all six semantic inputs and construct complete owner/fate/collision/interface/provenance child keys before any numerical collision term can enter the compulsory row.
