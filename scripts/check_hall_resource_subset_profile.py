#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement
from math import ceil

RESOURCES = range(4)
TYPES = tuple(
    frozenset(resource for resource in RESOURCES if mask & (1 << resource))
    for mask in range(1, 1 << len(tuple(RESOURCES)))
)


def independence_number(motifs):
    size = len(motifs)
    best = 0
    for mask in range(1 << size):
        if mask.bit_count() <= best:
            continue
        chosen = [index for index in range(size) if mask & (1 << index)]
        if all(
            not (motifs[first] & motifs[second])
            for offset, first in enumerate(chosen)
            for second in chosen[offset + 1 :]
        ):
            best = len(chosen)
    return best


def loads_on(motifs, active):
    multiplicities = [0] * len(tuple(RESOURCES))
    for index in active:
        for resource in motifs[index]:
            multiplicities[resource] += 1
    return {
        index: sum(multiplicities[resource] - 1 for resource in motifs[index])
        for index in active
    }


def resource_subset_profile(motifs):
    active = set(range(len(motifs)))
    removal_loads = []
    while active:
        loads = loads_on(motifs, active)
        selected = min(active, key=lambda index: (loads[index], index))
        removal_loads.append(loads[selected])
        active.remove(selected)
    resource_degeneracy = max(removal_loads, default=-1)
    bound = ceil(Fraction(len(motifs), resource_degeneracy + 1)) if motifs else 0
    return resource_degeneracy, bound, tuple(removal_loads)


def incidence_caro_wei(motifs):
    loads = loads_on(motifs, set(range(len(motifs))))
    return (
        ceil(sum(Fraction(1, loads[index] + 1) for index in range(len(motifs)))),
        tuple(loads[index] for index in range(len(motifs))),
    )


families_checked = 0
strict_profile_improvements = 0
strict_caro_wei_improvements = 0
ties = 0
profile_example = None
caro_wei_example = None

for size in range(1, 7):
    for indices in combinations_with_replacement(range(len(TYPES)), size):
        motifs = tuple(TYPES[index] for index in indices)
        alpha = independence_number(motifs)
        resource_degeneracy, peeling_bound, removal_loads = resource_subset_profile(motifs)
        caro_wei_bound, initial_loads = incidence_caro_wei(motifs)
        combined_bound = max(peeling_bound, caro_wei_bound)
        assert alpha >= combined_bound

        if peeling_bound > caro_wei_bound:
            strict_profile_improvements += 1
            if profile_example is None:
                profile_example = (
                    motifs,
                    alpha,
                    resource_degeneracy,
                    peeling_bound,
                    caro_wei_bound,
                    removal_loads,
                    initial_loads,
                )
        elif caro_wei_bound > peeling_bound:
            strict_caro_wei_improvements += 1
            if caro_wei_example is None:
                caro_wei_example = (
                    motifs,
                    alpha,
                    resource_degeneracy,
                    peeling_bound,
                    caro_wei_bound,
                    removal_loads,
                    initial_loads,
                )
        else:
            ties += 1
        families_checked += 1

assert families_checked == 54263
assert strict_profile_improvements == 1884
assert strict_caro_wei_improvements == 6142
assert ties == 46237
assert profile_example[0] == (
    frozenset({0}),
    frozenset({0}),
    frozenset({0, 1}),
    frozenset({1, 2, 3}),
    frozenset({0, 1, 2, 3}),
)
assert profile_example[1:5] == (2, 3, 2, 1)
assert caro_wei_example[0] == (
    frozenset({0}),
    frozenset({1, 2}),
    frozenset({1, 2}),
)
assert caro_wei_example[1:5] == (2, 2, 1, 2)

print({
    "resource_types": len(TYPES),
    "families_checked": families_checked,
    "maximum_family_size": 6,
    "resource_degeneracy": "max_nonempty_U min_{v in U} sum_{r in R(v)}(mu_r(U)-1)",
    "peeling_certificate": "ceil(M/(kappa_R+1))",
    "families_where_peeling_strictly_improves_incidence_caro_wei": strict_profile_improvements,
    "families_where_incidence_caro_wei_is_strictly_better": strict_caro_wei_improvements,
    "families_where_bounds_tie": ties,
    "combined_certificate": "max(ceil(sum_v 1/(L_v+1)), ceil(M/(kappa_R+1)))",
    "profile_example": {"alpha": 2, "kappa_R": 3, "peeling_bound": 2, "incidence_caro_wei": 1},
    "caro_wei_example": {"alpha": 2, "kappa_R": 2, "peeling_bound": 1, "incidence_caro_wei": 2},
    "two_stage_hall_condition": "3*q_profile-m>=28",
    "remaining_gap": "actual coordinate motif lists and selected-centre conflicts are still absent",
    "evidence_level": "exact_resource_subset_peeling_profile",
    "status": "passed",
})
