#!/usr/bin/env python3
from collections import Counter

VERTICES = 30
TYPES = tuple(("P", size) for size in range(1, VERTICES + 1)) + tuple(
    ("C", size) for size in range(4, VERTICES + 1, 2)
)


def independent_number(component):
    kind, size = component
    if kind == "P":
        return (size + 1) // 2
    assert kind == "C" and size % 2 == 0
    return size // 2


def odd_path_count(components):
    return sum(kind == "P" and size % 2 == 1 for kind, size in components)


signatures = []


def enumerate_signatures(start, remaining, chosen):
    if remaining == 0:
        signatures.append(tuple(chosen))
        return
    for index in range(start, len(TYPES)):
        component = TYPES[index]
        if component[1] > remaining:
            continue
        chosen.append(component)
        enumerate_signatures(index, remaining - component[1], chosen)
        chosen.pop()


enumerate_signatures(0, VERTICES, [])
assert len(signatures) == 18170

qualifying = []
for signature in signatures:
    alpha_direct = sum(independent_number(component) for component in signature)
    odd = odd_path_count(signature)
    alpha_formula = (VERTICES + odd) // 2
    assert alpha_direct == alpha_formula
    if alpha_direct >= 28:
        qualifying.append((Counter(signature), alpha_direct, odd))

expected = (
    (Counter({("P", 1): 30}), 30, 30),
    (Counter({("P", 1): 28, ("P", 2): 1}), 29, 28),
    (Counter({("P", 1): 27, ("P", 3): 1}), 29, 28),
    (Counter({("P", 1): 26, ("P", 2): 2}), 28, 26),
    (Counter({("P", 1): 26, ("P", 4): 1}), 28, 26),
    (Counter({("P", 1): 26, ("C", 4): 1}), 28, 26),
    (Counter({("P", 1): 25, ("P", 2): 1, ("P", 3): 1}), 28, 26),
    (Counter({("P", 1): 25, ("P", 5): 1}), 28, 26),
    (Counter({("P", 1): 24, ("P", 3): 2}), 28, 26),
)
assert tuple(qualifying) == expected
assert Counter(alpha for _, alpha, _ in qualifying) == Counter({28: 6, 29: 2, 30: 1})
assert min(signature[("P", 1)] for signature, _, _ in qualifying) == 24
assert max(
    VERTICES - signature[("P", 1)] for signature, _, _ in qualifying
) == 6

print({
    "centres": VERTICES,
    "path_even_cycle_component_signatures_checked": len(signatures),
    "retention_at_least_28_signatures": len(qualifying),
    "retention_histogram": {28: 6, 29: 2, 30: 1},
    "exact_28_signatures": (
        "26P1+2P2",
        "26P1+P4",
        "26P1+C4",
        "25P1+P2+P3",
        "25P1+P5",
        "24P1+2P3",
    ),
    "minimum_isolated_centres": 24,
    "maximum_nonisolated_centres": 6,
    "host_filter": "at least 24 centres must have both source and host defect labels private",
    "evidence_level": "exact_thirty_centre_degree_two_extremal_classification",
    "status": "passed",
})
