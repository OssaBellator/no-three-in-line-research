#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

RESOURCE_TYPES = tuple(
    frozenset(resource for resource in range(4) if mask & (1 << resource))
    for mask in range(1, 16)
)

def overlap_graph(resource_sets):
    adjacency = [0] * len(resource_sets)
    for first in range(len(resource_sets)):
        for second in range(first + 1, len(resource_sets)):
            if resource_sets[first] & resource_sets[second]:
                adjacency[first] |= 1 << second
                adjacency[second] |= 1 << first
    return tuple(adjacency)

def components(adjacency):
    seen = 0
    result = []
    for start in range(len(adjacency)):
        if seen & (1 << start):
            continue
        stack = [start]
        seen |= 1 << start
        component = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            unseen = adjacency[vertex] & ~seen
            while unseen:
                bit = unseen & -unseen
                neighbour = bit.bit_length() - 1
                seen |= bit
                stack.append(neighbour)
                unseen -= bit
        result.append(tuple(component))
    return tuple(result)

def independence_number(adjacency, vertices):
    best = 0
    for local_mask in range(1 << len(vertices)):
        size = local_mask.bit_count()
        if size <= best:
            continue
        independent = True
        for first in range(len(vertices)):
            if not (local_mask & (1 << first)):
                continue
            for second in range(first + 1, len(vertices)):
                if (
                    local_mask & (1 << second)
                    and adjacency[vertices[first]] & (1 << vertices[second])
                ):
                    independent = False
                    break
            if not independent:
                break
        if independent:
            best = size
    return best

def ceiling(value):
    return (value.numerator + value.denominator - 1) // value.denominator

def certificates(resource_sets):
    adjacency = overlap_graph(resource_sets)
    overlap_components = components(adjacency)
    weights = tuple(Fraction(1, adjacency[v].bit_count() + 1) for v in range(len(adjacency)))
    global_caro_wei = ceiling(sum(weights, Fraction(0)))
    component_caro_wei = sum(
        ceiling(sum((weights[v] for v in component), Fraction(0)))
        for component in overlap_components
    )
    exact_component_sum = sum(
        independence_number(adjacency, component)
        for component in overlap_components
    )
    return global_caro_wei, component_caro_wei, exact_component_sum, tuple(
        sorted(len(component) for component in overlap_components)
    )

checked = 0
strict_improvements = 0
exact_component_cases = 0
for motif_count in range(1, 7):
    for type_indices in combinations_with_replacement(range(len(RESOURCE_TYPES)), motif_count):
        resource_sets = tuple(RESOURCE_TYPES[index] for index in type_indices)
        global_bound, component_bound, exact, component_sizes = certificates(resource_sets)
        assert global_bound <= component_bound <= exact
        checked += 1
        strict_improvements += int(component_bound > global_bound)
        exact_component_cases += int(component_bound == exact)

example = (
    frozenset({0}),
    frozenset({1}),
    frozenset({0, 1}),
    frozenset({2}),
    frozenset({3}),
    frozenset({2, 3}),
)
assert certificates(example) == (3, 4, 4, (3, 3))
assert checked == 54263
assert strict_improvements == 3
assert exact_component_cases == 50387

for q in range(1, 20):
    for matching_loss in range(0, 10):
        assert (3 * q - matching_loss >= 28) == (q >= (28 + matching_loss + 2) // 3)

print({
    "resource_types": len(RESOURCE_TYPES),
    "motif_multisets_checked": checked,
    "component_caro_wei_dominates_global": True,
    "strict_improvement_cases": strict_improvements,
    "component_bound_exact_cases": exact_component_cases,
    "strict_example_component_sizes": (3, 3),
    "strict_example_global_bound": 3,
    "strict_example_component_bound": 4,
    "exact_component_identity": "alpha(G)=sum_C alpha(G[C])",
    "two_stage_hall_condition": "3*q-m>=28",
    "remaining_gap": "coordinate host families must supply resource lists with uniformly controlled overlap components and a selected-centre matching bound",
    "evidence_level": "exact_component_resource_packing_interface",
    "status": "passed",
})
