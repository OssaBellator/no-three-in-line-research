#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import ceil

RESOURCES = tuple(range(4))
MOTIF_TYPES = tuple(
    frozenset(items)
    for size in range(1, len(RESOURCES) + 1)
    for items in combinations(RESOURCES, size)
)

def exact_independence_number(adjacency):
    best = 0
    for mask in range(1 << len(adjacency)):
        if mask.bit_count() <= best:
            continue
        if all(not (mask & (1 << vertex)) or not (adjacency[vertex] & mask)
               for vertex in range(len(adjacency))):
            best = mask.bit_count()
    return best

def audit_family(family):
    multiplicity = {
        resource: sum(resource in motif for motif in family)
        for resource in RESOURCES
    }
    adjacency = [0] * len(family)
    degrees = [0] * len(family)
    for first, second in combinations(range(len(family)), 2):
        if family[first] & family[second]:
            adjacency[first] |= 1 << second
            adjacency[second] |= 1 << first
            degrees[first] += 1
            degrees[second] += 1
    loads = [
        sum(multiplicity[resource] - 1 for resource in motif)
        for motif in family
    ]
    assert all(degree <= load for degree, load in zip(degrees, loads))
    local_bound = ceil(sum(Fraction(1, load + 1) for load in loads))
    assert exact_independence_number(adjacency) >= local_bound
    max_size = max(map(len, family))
    max_multiplicity = max(multiplicity.values())
    uniform_bound = ceil(len(family) / (max_size * (max_multiplicity - 1) + 1))
    assert local_bound >= uniform_bound
    return local_bound

families_checked = 0
for size in range(1, 8):
    for family in combinations(MOTIF_TYPES, size):
        audit_family(family)
        families_checked += 1
assert families_checked == 16383

for group_size in range(1, 8):
    groups = 4
    family = []
    for resource in range(groups):
        family.extend([{resource}] * group_size)
    multiplicity = {
        resource: sum(resource in motif for motif in family)
        for resource in range(groups)
    }
    loads = [
        sum(multiplicity[resource] - 1 for resource in motif)
        for motif in family
    ]
    local_bound = ceil(sum(Fraction(1, load + 1) for load in loads))
    assert local_bound == groups

def required_selected_motifs(matching_loss):
    return ceil(Fraction(28 + matching_loss, 3))

assert [required_selected_motifs(m) for m in range(7)] == [10, 10, 10, 11, 11, 11, 12]

print({
    "motif_families_exhausted": families_checked,
    "local_overlap_load": "L_i=sum_{r in R_i}(mu_r-1)",
    "degree_bound": "d_i<=L_i",
    "resource_multiplicity_packing": "alpha>=ceil(sum_i 1/(L_i+1))",
    "uniform_corollary": "alpha>=ceil(M/(s*(rho-1)+1))",
    "sharpness": "disjoint resource cliques attain the local bound",
    "two_stage_hall_condition": "3*ceil(sum_i 1/(L_i+1))-m>=28",
    "status": "passed",
})
