#!/usr/bin/env python3
from collections import Counter

MICROSTATES = tuple((syndrome, orientation) for syndrome in range(3) for orientation in range(2))
CHOICES = tuple(range(4))


def target_syndrome(gadget, syndrome, choice):
    if gadget == "A":
        return syndrome if choice < 3 else (syndrome + 1) % 3
    if gadget == "B":
        return (-syndrome) % 3 if choice < 3 else (1 - syndrome) % 3
    raise ValueError(gadget)


def target_orientation(orientation, choice):
    return orientation ^ (choice % 2)


def decode_choice_pair(syndrome, choice):
    # Ordered distinct cells in a complete four-by-four same-side choice grid.
    return choice, (choice + syndrome + 1) % 4


compatible_pairs = tuple((a, b) for a in range(4) for b in range(4) if a != b)
decoded_pairs = tuple(decode_choice_pair(syndrome, choice) for syndrome in range(3) for choice in CHOICES)
assert len(compatible_pairs) == 12
assert len(set(decoded_pairs)) == 12
assert set(decoded_pairs) == set(compatible_pairs)

# Six states cannot themselves encode all twelve compatible pairs.
assert len(MICROSTATES) == 6 < len(compatible_pairs)

for gadget in ("A", "B"):
    pair_multiplicity = Counter()
    transition_records = []
    for syndrome, orientation in MICROSTATES:
        for choice in CHOICES:
            pair = decode_choice_pair(syndrome, choice)
            target = (
                target_syndrome(gadget, syndrome, choice),
                target_orientation(orientation, choice),
            )
            pair_multiplicity[pair] += 1
            transition_records.append(((syndrome, orientation), choice, pair, target))
    assert len(transition_records) == 24
    assert set(pair_multiplicity) == set(compatible_pairs)
    assert set(pair_multiplicity.values()) == {2}

# After quotienting orientation, each compatible pair has exactly one witness.
quotient_records = [
    (syndrome, choice, decode_choice_pair(syndrome, choice), target_syndrome("A", syndrome, choice))
    for syndrome in range(3)
    for choice in CHOICES
]
assert len({record[2] for record in quotient_records}) == 12

print({
    "cylinder_states": len(MICROSTATES),
    "choice_labels": len(CHOICES),
    "complete_grid_pairs": len(compatible_pairs),
    "state_level_decoder_possible": False,
    "quotient_choice_pair_decoder": "(s,c) -> (c,c+s+1 mod 4)",
    "decoder_is_bijection": True,
    "microscopic_witnesses_per_pair_per_gadget": 2,
    "remaining_type_gap": "no map from abstract pair coordinates to prime-patching endpoint cells",
    "evidence_level": "repository_typed_candidate_decoder",
    "status": "passed",
})
