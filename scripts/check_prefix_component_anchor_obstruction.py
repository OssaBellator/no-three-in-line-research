#!/usr/bin/env python3
from collections import Counter
from itertools import permutations

P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
N = len(P)

adjacency = {("r",r): set() for r in range(N)}
adjacency.update({("c",c): set() for c in range(N)})
for row in range(N):
    for column in (P[row], Q[row]):
        adjacency[("r",row)].add(("c",column))
        adjacency[("c",column)].add(("r",row))

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
assert tuple(sorted(map(len, components))) == (2,2,4,5)

internal_counts = {}
for rows in components:
    count = 0
    for image in permutations(rows):
        if all(row != target and P[row] != Q[target] for row,target in zip(rows,image)):
            count += 1
    internal_counts[rows] = count
assert sorted(internal_counts.values()) == [0,0,2,13]
assert all(internal_counts[rows] == 0 for rows in components if len(rows) == 2)

component_id = {row:index for index,rows in enumerate(components) for row in rows}
allowed = {
    row: tuple(target for target in range(N) if target != row and Q[target] != P[row])
    for row in range(N)
}
dp = {0: Counter({0:1})}
for row in range(N):
    next_dp = {}
    for mask, distribution in dp.items():
        for target in allowed[row]:
            if mask & (1 << target):
                continue
            new_mask = mask | (1 << target)
            target_distribution = next_dp.setdefault(new_mask, Counter())
            cross = int(component_id[row] != component_id[target])
            for count, ways in distribution.items():
                target_distribution[count+cross] += ways
    dp = next_dp
final = dp[(1 << N)-1]
assert min(final) == 4
assert final[4] == 104

rows = (0,1)
P2 = (0,1)
Q2 = (1,0)
assert all(
    not all(row != target and P2[row] != Q2[target] for row,target in zip(rows,image))
    for image in permutations(rows)
)

print({
    "canonical_component_pair_sizes": sorted(map(len, components)),
    "internal_anchor_matching_counts": {str(rows):count for rows,count in internal_counts.items()},
    "two_pair_component_internally_anchorable": False,
    "minimum_cross_component_anchor_pairs": 4,
    "minimum_cross_component_anchor_matchings": 104,
    "cross_component_count_distribution": dict(sorted(final.items())),
    "remaining_gap": "a uniformly nested saturated family must either avoid two-pair incidence components or coordinate at least four cross-component anchor pairs in the canonical thirteen-pair source",
    "evidence_level": "exact_component_anchor_obstruction",
    "status": "passed",
})
