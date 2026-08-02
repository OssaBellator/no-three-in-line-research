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
        chosen = [index for index in range(size) if mask & (1 << index)]
        if all(not (motifs[first] & motifs[second]) for offset, first in enumerate(chosen) for second in chosen[offset + 1 :]):
            best = max(best, len(chosen))
    return best


def audit_family(motifs):
    loads = {resource: sum(resource in motif for motif in motifs) for resource in RESOURCES}
    exact_degrees = []
    raw_load_degrees = []
    duplicate_corrections = []
    for index, motif in enumerate(motifs):
        neighbours = [other for other in range(len(motifs)) if other != index and motif & motifs[other]]
        raw = sum(loads[resource] - 1 for resource in motif)
        correction = sum(max(0, len(motif & motifs[other]) - 1) for other in range(len(motifs)) if other != index)
        exact = raw - correction
        assert exact == len(neighbours)
        assert exact <= raw
        exact_degrees.append(exact)
        raw_load_degrees.append(raw)
        duplicate_corrections.append(correction)

    alpha = independence_number(motifs)
    exact_caro_wei = ceil(sum(Fraction(1, degree + 1) for degree in exact_degrees))
    incidence_only = ceil(sum(Fraction(1, degree + 1) for degree in raw_load_degrees))
    assert alpha >= exact_caro_wei >= incidence_only

    maximum_size = max(map(len, motifs), default=0)
    maximum_load = max(loads.values(), default=0)
    uniform_denominator = maximum_size * max(0, maximum_load - 1) + 1
    uniform_bound = ceil(Fraction(len(motifs), uniform_denominator)) if motifs else 0
    assert incidence_only >= uniform_bound
    return alpha, exact_caro_wei, incidence_only, tuple(duplicate_corrections)


families_checked = 0
strict_incidence_improvements = 0
strict_pair_corrections = 0
for size in range(1, 7):
    for indices in combinations_with_replacement(range(len(TYPES)), size):
        motifs = tuple(TYPES[index] for index in indices)
        alpha, exact_bound, incidence_bound, corrections = audit_family(motifs)
        strict_incidence_improvements += int(incidence_bound > 1)
        strict_pair_corrections += int(any(corrections))
        families_checked += 1

assert families_checked == 54263


def selected_motifs_needed(matching_loss):
    return ceil(Fraction(28 + matching_loss, 3))

assert selected_motifs_needed(0) == 10
assert selected_motifs_needed(2) == 10
assert selected_motifs_needed(3) == 11
assert selected_motifs_needed(5) == 11
assert selected_motifs_needed(6) == 12

print({
    "resource_types": len(TYPES),
    "families_checked": families_checked,
    "maximum_family_size": 6,
    "exact_degree_formula": "sum_{r in R(v)}(mu_r-1)-sum_{u!=v}max(|R(u) intersect R(v)|-1,0)",
    "incidence_only_degree_upper_bound": "L_v=sum_{r in R(v)}(mu_r-1)",
    "host_auditable_packing_bound": "ceil(sum_v 1/(L_v+1))",
    "uniform_load_corollary": "ceil(M/(s*(lambda-1)+1))",
    "two_stage_hall_condition": "3*q-m>=28",
    "selected_motifs_needed_by_matching_loss": {0: 10, 2: 10, 3: 11, 5: 11, 6: 12},
    "families_with_nontrivial_incidence_bound": strict_incidence_improvements,
    "families_with_duplicate_overlap_correction": strict_pair_corrections,
    "remaining_gap": "the conditional host must provide actual motif resource sets and certify that all centre conflicts are covered by the second-stage graph",
    "evidence_level": "exact_local_resource_incidence_packing_interface",
    "status": "passed",
})
