#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache

P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
N = len(P)
COMPONENTS = ((0,2),(1,4,6,7),(3,5),(8,9,10,11,12))
COMPONENT_ID = {row:index for index,rows in enumerate(COMPONENTS) for row in rows}
TWO_PAIR_COMPONENTS = tuple(rows for rows in COMPONENTS if len(rows) == 2)
ALLOWED = {
    row: tuple(target for target in range(N) if target != row and Q[target] != P[row])
    for row in range(N)
}

@lru_cache(None)
def minimum_cross_completion_count(row, used_mask, cross_count):
    if cross_count > 4:
        return 0
    if row == N:
        return int(cross_count == 4)
    total = 0
    for target in ALLOWED[row]:
        bit = 1 << target
        if used_mask & bit:
            continue
        total += minimum_cross_completion_count(
            row + 1,
            used_mask | bit,
            cross_count + int(COMPONENT_ID[row] != COMPONENT_ID[target]),
        )
    return total

minimum_cross_matchings = []
def generate(row=0, used_mask=0, cross_count=0, image=None):
    if image is None:
        image = []
    if row == N:
        if cross_count == 4:
            minimum_cross_matchings.append(tuple(image))
        return
    for target in ALLOWED[row]:
        bit = 1 << target
        next_cross = cross_count + int(COMPONENT_ID[row] != COMPONENT_ID[target])
        if used_mask & bit:
            continue
        if minimum_cross_completion_count(row + 1, used_mask | bit, next_cross) == 0:
            continue
        image.append(target)
        generate(row + 1, used_mask | bit, next_cross, image)
        image.pop()

generate()
assert len(minimum_cross_matchings) == 104

def optimal_rerouting(image, deleted_rows):
    remaining = tuple(row for row in range(N) if row not in deleted_rows)
    target_index = {target:index for index,target in enumerate(remaining)}

    @lru_cache(None)
    def solve(position, used_mask):
        if position == len(remaining):
            return (0, 1) if used_mask == (1 << len(remaining)) - 1 else (N + 1, 0)
        row = remaining[position]
        best = N + 1
        ways = 0
        for target in ALLOWED[row]:
            if target not in target_index:
                continue
            bit = 1 << target_index[target]
            if used_mask & bit:
                continue
            suffix, count = solve(position + 1, used_mask | bit)
            cost = suffix + int(target != image[row])
            if cost < best:
                best, ways = cost, count
            elif cost == best:
                ways += count
        return best, ways

    return solve(0, 0)

rerouting_costs = Counter()
optimal_way_counts = Counter()
boundary_flow = Counter()
for deleted in TWO_PAIR_COMPONENTS:
    deleted = frozenset(deleted)
    for image in minimum_cross_matchings:
        outgoing = sum(image[row] not in deleted for row in deleted)
        incoming = sum(image[row] in deleted for row in range(N) if row not in deleted)
        boundary_flow[(outgoing,incoming)] += 1
        cost, ways = optimal_rerouting(image, deleted)
        rerouting_costs[cost] += 1
        optimal_way_counts[ways] += 1

assert boundary_flow == Counter({(2,2): 208})
assert rerouting_costs == Counter({4:208})
assert optimal_way_counts == Counter({144:208})

print({
    "minimum_cross_component_anchor_matchings": len(minimum_cross_matchings),
    "two_pair_components": [list(component) for component in TWO_PAIR_COMPONENTS],
    "deletion_cases_checked": 208,
    "boundary_flow_per_deletion": {"outgoing":2,"incoming":2},
    "minimum_remaining_assignment_changes": 4,
    "optimal_reroutings_per_case": 144,
    "all_cases_have_same_radius": True,
    "remaining_gap": "the four-assignment anchor rerouting is combinatorial; a uniform coordinate insertion rule must realize it while preserving all mixed-run no-three constraints",
    "evidence_level": "exact_anchor_rerouting_radius",
    "status": "passed",
})
