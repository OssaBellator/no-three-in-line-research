#!/usr/bin/env python3
from collections import Counter, defaultdict
from functools import lru_cache

P = (8,3,4,11,13,6,1,12,7,0,10,5,2,9)
Q = (4,11,8,3,7,12,13,0,1,6,2,9,10,5)
N = len(P)

adjacency = {("r", row): set() for row in range(N)}
adjacency.update({("c", column): set() for column in range(N)})
for row in range(N):
    for column in (P[row], Q[row]):
        adjacency[("r", row)].add(("c", column))
        adjacency[("c", column)].add(("r", row))

seen = set()
components = []
for vertex in adjacency:
    if vertex in seen:
        continue
    stack = [vertex]
    seen.add(vertex)
    rows = []
    while stack:
        current = stack.pop()
        if current[0] == "r":
            rows.append(current[1])
        for neighbour in adjacency[current]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    components.append(tuple(sorted(rows)))
components = tuple(sorted(components, key=lambda rows: rows[0]))
assert tuple(sorted(map(len, components))) == (2,2,2,2,3,3)

component_id = {row:index for index, rows in enumerate(components) for row in rows}
allowed = {
    row: tuple(target for target in range(N) if target != row and P[row] != Q[target])
    for row in range(N)
}

def internal_count(rows):
    rows = tuple(rows)
    count = 0
    def visit(index, used):
        nonlocal count
        if index == len(rows):
            count += 1
            return
        row = rows[index]
        for target in rows:
            if target not in used and target in allowed[row]:
                visit(index + 1, used | {target})
    visit(0, set())
    return count

internal_counts = tuple(internal_count(rows) for rows in components)
assert sorted(internal_counts) == [0,0,0,0,1,1]

@lru_cache(None)
def minimum_cross_suffix(row, mask):
    if row == N:
        return 0
    best = N + 1
    for target in allowed[row]:
        if mask & (1 << target):
            continue
        cross = int(component_id[row] != component_id[target])
        best = min(best, cross + minimum_cross_suffix(row + 1, mask | (1 << target)))
    return best

minimum_cross = minimum_cross_suffix(0, 0)
assert minimum_cross == 8

minimum_matchings = []
def enumerate_minimum(row, mask, image):
    if row == N:
        minimum_matchings.append(tuple(image))
        return
    optimum = minimum_cross_suffix(row, mask)
    for target in allowed[row]:
        if mask & (1 << target):
            continue
        cross = int(component_id[row] != component_id[target])
        if cross + minimum_cross_suffix(row + 1, mask | (1 << target)) == optimum:
            image.append(target)
            enumerate_minimum(row + 1, mask | (1 << target), image)
            image.pop()

enumerate_minimum(0, 0, [])
assert len(minimum_matchings) == 4752

def assignment_cost(cost):
    n = len(cost)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)
    for i in range(1, n + 1):
        p[0] = i
        minv = [10**9] * (n + 1)
        used = [False] * (n + 1)
        j0 = 0
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = 10**9
            j1 = 0
            for j in range(1, n + 1):
                if used[j]:
                    continue
                current = cost[i0 - 1][j - 1] - u[i0] - v[j]
                if current < minv[j]:
                    minv[j] = current
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    return -v[0]

two_components = tuple(rows for rows in components if len(rows) == 2)
distribution = Counter()
per_component = defaultdict(Counter)
for image in minimum_matchings:
    for deleted in two_components:
        rows = tuple(row for row in range(N) if row not in deleted)
        targets = rows
        cost = []
        for row in rows:
            line = []
            for target in targets:
                if target not in allowed[row]:
                    line.append(100)
                else:
                    line.append(0 if image[row] == target else 1)
            cost.append(line)
        distance = assignment_cost(cost)
        assert distance < 100
        distribution[distance] += 1
        per_component[deleted][distance] += 1

assert distribution == Counter({2:15744,3:3072,4:192})
assert all(counts == Counter({2:3936,3:768,4:48}) for counts in per_component.values())

print({
    "component_pair_sizes": sorted(map(len, components)),
    "component_rows": components,
    "internal_anchor_matching_counts": internal_counts,
    "minimum_cross_component_anchor_pairs": minimum_cross,
    "minimum_cross_component_anchor_matchings": len(minimum_matchings),
    "two_pair_components": len(two_components),
    "deletion_cases": len(minimum_matchings) * len(two_components),
    "minimum_rerouting_distance_distribution": dict(sorted(distribution.items())),
    "per_two_component_distribution": {"2":3936,"3":768,"4":48},
    "maximum_rerouting_radius": max(distribution),
    "remaining_gap": "the bounded assignment repairs still lack a uniform integer insertion realization",
    "evidence_level": "exact_second_reservoir_rerouting_radius",
    "status": "passed",
})
