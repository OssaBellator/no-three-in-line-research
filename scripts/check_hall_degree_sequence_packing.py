#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import ceil


def independence_number(n, edges):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    best = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best:
            continue
        vertices = [vertex for vertex in range(n) if mask >> vertex & 1]
        if all((vertices[i], vertices[j]) not in edge_set for i in range(size) for j in range(i + 1, size)):
            best = size
    return best


def degree_sequence(n, edges):
    degrees = [0] * n
    for first, second in edges:
        degrees[first] += 1
        degrees[second] += 1
    return tuple(degrees)


def caro_wei(degrees):
    return sum((Fraction(1, degree + 1) for degree in degrees), Fraction(0))


def ceil_fraction(value):
    return (value.numerator + value.denominator - 1) // value.denominator

# Exhaust all labelled graphs on six vertices.
n = 6
possible_edges = tuple(combinations(range(n), 2))
checked = 0
equality = 0
for mask in range(1 << len(possible_edges)):
    edges = tuple(possible_edges[index] for index in range(len(possible_edges)) if mask >> index & 1)
    degrees = degree_sequence(n, edges)
    alpha = independence_number(n, edges)
    bound = caro_wei(degrees)
    assert alpha >= bound
    assert alpha >= ceil_fraction(bound)
    average_bound = Fraction(n * n, n + sum(degrees))  # n/(1+average degree)
    assert bound >= average_bound
    equality += int(Fraction(alpha) == bound)
    checked += 1

# Disjoint unions of equal cliques attain both bounds.
for clique_size, clique_count in ((2, 5), (3, 4), (4, 3), (5, 2)):
    total = clique_size * clique_count
    edges = []
    for component in range(clique_count):
        vertices = range(component * clique_size, (component + 1) * clique_size)
        edges.extend(combinations(vertices, 2))
    degrees = degree_sequence(total, edges)
    assert independence_number(total, edges) == clique_count
    assert caro_wei(degrees) == clique_count
    assert Fraction(total * total, total + sum(degrees)) == clique_count

REQUIRED_GOOD = 28

def required_motifs(matching_loss):
    return ceil(Fraction(REQUIRED_GOOD + matching_loss, 3))

examples = {}
for matching_loss in (0, 2, 3, 5, 6):
    q = required_motifs(matching_loss)
    examples[matching_loss] = q
    assert 3 * q - matching_loss >= REQUIRED_GOOD
    assert 3 * (q - 1) - matching_loss < REQUIRED_GOOD

# An irregular degree sequence can improve on a maximum-degree-only estimate.
degrees = (0,) * 9 + (9,) * 10
bound = caro_wei(degrees)
assert bound == 10
assert max(degrees) == 9
assert ceil_fraction(Fraction(len(degrees), max(degrees) + 1)) == 2

print({
    "labelled_six_vertex_graphs_checked": checked,
    "caro_wei_equality_graphs": equality,
    "motif_independent_set_lower_bound": "ceil(sum_v 1/(d_v+1))",
    "average_degree_corollary": "ceil(M/(average_degree+1))",
    "two_stage_retained_centres": "3*q-m where q is the motif bound and m bounds the bipartite centre-conflict matching",
    "required_selected_motifs_by_matching_loss": examples,
    "irregular_degree_example": {"vertices": 19, "maximum_degree_bound": 2, "degree_sequence_bound": 10},
    "sharpness": "disjoint unions of equal cliques",
    "remaining_gap": "the conditional host must supply the motif degree sequence and a certified centre-conflict matching bound from coordinates",
    "evidence_level": "exact_degree_sequence_hall_packing_interface",
    "status": "passed",
})
