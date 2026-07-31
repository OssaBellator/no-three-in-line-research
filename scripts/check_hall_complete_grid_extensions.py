#!/usr/bin/env python3
from itertools import permutations

SYNDROMES = range(3)
ORIENTATIONS = range(2)
CHOICES = range(4)
LEFT_RESOURCES = (0, 1)
RIGHT_RESOURCES = range(4)


def decoded_pair(syndrome, choice):
    return choice, (choice + syndrome + 1) % 4


pairs = {
    (syndrome, choice): decoded_pair(syndrome, choice)
    for syndrome in SYNDROMES
    for choice in CHOICES
}
compatible_pairs = {(a, b) for a in RIGHT_RESOURCES for b in RIGHT_RESOURCES if a != b}
assert set(pairs.values()) == compatible_pairs
assert len(pairs) == len(compatible_pairs) == 12


def residual_matchings(a, b):
    remaining_left = (2, 3)
    remaining_right = tuple(value for value in RIGHT_RESOURCES if value not in (a, b))
    out = []
    for image in permutations(remaining_right):
        matching = ((0, a), (1, b)) + tuple(zip(remaining_left, image))
        assert len({left for left, _ in matching}) == 4
        assert len({right for _, right in matching}) == 4
        out.append(matching)
    return tuple(out)


extension_counts = {}
canonical_extensions = {}
for key, (a, b) in pairs.items():
    extensions = residual_matchings(a, b)
    assert len(extensions) == 2
    extension_counts[key] = len(extensions)
    canonical_extensions[key] = min(extensions)

assert set(extension_counts.values()) == {2}

microscopic_witnesses = {}
for syndrome in SYNDROMES:
    for orientation in ORIENTATIONS:
        for choice in CHOICES:
            pair = pairs[(syndrome, choice)]
            microscopic_witnesses[(syndrome, orientation, choice)] = {
                "cells": ((0, pair[0]), (1, pair[1])),
                "extension": canonical_extensions[(syndrome, choice)],
            }

assert len(microscopic_witnesses) == 24
assert all(
    witness["cells"][:2] == witness["extension"][:2]
    for witness in microscopic_witnesses.values()
)

assert len(tuple((s, o) for s in SYNDROMES for o in ORIENTATIONS)) == 6
assert 6 < len(compatible_pairs)

print(
    {
        "host": "complete bipartite grid K_4,4",
        "fixed_left_resources": LEFT_RESOURCES,
        "compatible_grid_pairs": len(compatible_pairs),
        "quotient_choice_pairs": len(pairs),
        "decoder_is_bijection": True,
        "residual_host": "K_2,2",
        "matching_extensions_per_pair": 2,
        "microscopic_orientation_witnesses": len(microscopic_witnesses),
        "canonical_extension_example": canonical_extensions[(0, 0)],
        "remaining_gap": "the four choice labels are not yet identified with coordinate-level prime-patching endpoint cells",
        "evidence_level": "repository_typed_complete_grid_decoder",
        "status": "passed",
    }
)
