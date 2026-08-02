#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import product
from math import gcd

P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
N = 13
COMPONENTS = ((0,2),(1,4,7,6),(3,5),(8,9,11,12,10))
CID = {row:index for index,cycle in enumerate(COMPONENTS) for row in cycle}
ALLOWED = {
    row: tuple(target for target in range(N) if target != row and Q[target] != P[row])
    for row in range(N)
}

@lru_cache(None)
def completion_count(row, used, crossings):
    if crossings > 4:
        return 0
    if row == N:
        return int(crossings == 4)
    return sum(
        completion_count(
            row + 1,
            used | (1 << target),
            crossings + (CID[row] != CID[target]),
        )
        for target in ALLOWED[row]
        if not used & (1 << target)
    )

matchings = []
def generate(row=0, used=0, crossings=0, image=()):
    if row == N:
        if crossings == 4:
            matchings.append(image)
        return
    for target in ALLOWED[row]:
        if used & (1 << target):
            continue
        next_crossings = crossings + (CID[row] != CID[target])
        if completion_count(row + 1, used | (1 << target), next_crossings):
            generate(row + 1, used | (1 << target), next_crossings, image + (target,))
generate()
assert len(matchings) == 104

A, C, B, D = COMPONENTS
AUTOMORPHISMS = []
for swap, rotation_a, rotation_b, rotation_c, rotation_d in product(
    range(2), range(2), range(2), range(4), range(5)
):
    sigma = [None] * N
    target_a, target_b = (B, A) if swap else (A, B)
    for index, row in enumerate(A):
        sigma[row] = target_a[(index + rotation_a) % 2]
    for index, row in enumerate(B):
        sigma[row] = target_b[(index + rotation_b) % 2]
    for index, row in enumerate(C):
        sigma[row] = C[(index + rotation_c) % 4]
    for index, row in enumerate(D):
        sigma[row] = D[(index + rotation_d) % 5]
    AUTOMORPHISMS.append(tuple(sigma))
assert len(set(AUTOMORPHISMS)) == 160

def act(image, sigma):
    inverse = [0] * N
    for row, target in enumerate(sigma):
        inverse[target] = row
    return tuple(sigma[image[inverse[row]]] for row in range(N))

matching_set = set(matchings)
unseen = set(matchings)
representatives = []
orbit_sizes = []
while unseen:
    representative = min(unseen)
    orbit = {act(representative, sigma) for sigma in AUTOMORPHISMS}
    assert orbit <= matching_set
    representatives.append(representative)
    orbit_sizes.append(len(orbit))
    unseen -= orbit
assert len(representatives) == 20
assert Counter(orbit_sizes) == Counter({2:12, 10:8})

DELETION_CASES = (
    (1,3,4,5,6,7,8,9,10,11,12),
    (0,1,2,4,6,7,8,9,10,11,12),
)

def first_optimal_route(image, rows):
    index = {row: position for position, row in enumerate(rows)}

    @lru_cache(None)
    def best(position, used):
        if position == len(rows):
            return 0 if used == (1 << len(rows)) - 1 else 99
        row = rows[position]
        candidates = [
            (target != image[row]) + best(position + 1, used | (1 << index[target]))
            for target in ALLOWED[row]
            if target in index and not used & (1 << index[target])
        ]
        return min(candidates, default=99)

    assert best(0, 0) == 4
    route = []
    used = 0
    for position, row in enumerate(rows):
        goal = best(position, used)
        for target in ALLOWED[row]:
            if target not in index or used & (1 << index[target]):
                continue
            bit = 1 << index[target]
            if (target != image[row]) + best(position + 1, used | bit) == goal:
                route.append(target)
                used |= bit
                break
    return tuple(route)

def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )

def primitive(first, second):
    dx, dy = second[0] - first[0], second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    return dx // divisor, dy // divisor

def embed_unit(rows, route):
    source = [
        point
        for row in rows
        for point in ((row, P[row]), (row, Q[row]))
    ]
    for first in range(len(source)):
        for second in range(first + 1, len(source)):
            for third in range(second + 1, len(source)):
                assert not collinear(source[first], source[second], source[third])

    anchors = []
    for row, target in zip(rows, route):
        first = (row, P[row])
        second = (target, Q[target])
        assert first[0] != second[0] and first[1] != second[1]
        anchors.append((first, second))
    assert len({point for pair in anchors for point in pair}) == 22

    points = list(source)
    labels = [-1] * len(points)
    for run, (first, second) in enumerate(anchors):
        for index, point in enumerate(points):
            if point in (first, second):
                labels[index] = run

    occupied_rows = {x for x, _ in points}
    occupied_columns = {y for _, y in points}
    for run, (first, second) in enumerate(anchors):
        dx, dy = primitive(first, second)
        inserted = False
        for magnitude in range(1, 50000):
            for sign in (1, -1):
                candidate = (
                    first[0] + sign * magnitude * dx,
                    first[1] + sign * magnitude * dy,
                )
                if (
                    candidate[0] in occupied_rows
                    or candidate[1] in occupied_columns
                    or candidate in points
                ):
                    continue
                bad = False
                for first_index in range(len(points)):
                    for second_index in range(first_index + 1, len(points)):
                        if collinear(points[first_index], points[second_index], candidate):
                            if labels[first_index] == run and labels[second_index] == run:
                                continue
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    continue
                points.append(candidate)
                labels.append(run)
                occupied_rows.add(candidate[0])
                occupied_columns.add(candidate[1])
                inserted = True
                break
            if inserted:
                break
        assert inserted

    for first in range(len(points)):
        for second in range(first + 1, len(points)):
            for third in range(second + 1, len(points)):
                if collinear(points[first], points[second], points[third]):
                    assert labels[first] >= 0 and labels[first] == labels[second] == labels[third]
    return max(max(abs(x), abs(y)) for x, y in points)

histograms = [Counter(), Counter()]
audits = 0
for representative in representatives:
    for case_index, rows in enumerate(DELETION_CASES):
        route = first_optimal_route(representative, rows)
        histograms[case_index][embed_unit(rows, route)] += 1
        audits += 1

assert audits == 40
assert histograms[0] == Counter({84:10, 50:4, 52:4, 66:2})
assert histograms[1] == Counter({44:10, 48:10})

print({
    "minimum_crossing_matchings": 104,
    "source_automorphisms": 160,
    "matching_orbits": 20,
    "orbit_size_histogram": {2:12, 10:8},
    "deletion_cases": 2,
    "representative_routes": 40,
    "optimal_rerouting_distance": 4,
    "unit_composition_coordinate_audits": 40,
    "case_0_maximum_coordinate_histogram": dict(sorted(histograms[0].items())),
    "case_1_maximum_coordinate_histogram": dict(sorted(histograms[1].items())),
    "remaining_gap": "only the all-unit composition is audited orbit-wide; arbitrary compositions and all 104 physical coordinate labelings remain open",
    "evidence_level": "exact_prefix_automorphism_orbits_and_unit_lifts",
    "status": "passed",
})
