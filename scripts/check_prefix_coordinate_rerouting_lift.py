#!/usr/bin/env python3
from itertools import combinations
from math import gcd

P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
COMPONENTS = ((0,2),(1,4,6,7),(3,5),(8,9,10,11,12))
COMPONENT_ID = {row:index for index,rows in enumerate(COMPONENTS) for row in rows}
DELETED_ROWS = frozenset((0,2))
REMAINING = tuple(row for row in range(13) if row not in DELETED_ROWS)
ORIGINAL = (3,6,5,0,1,2,7,4,10,8,12,9,11)
REROUTED = (3,1,5,6,7,4,10,8,12,9,11)


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def compositions(total):
    if total == 0:
        yield ()
        return
    for first in range(1,total+1):
        for suffix in compositions(total-first):
            yield (first,) + suffix


def allowed(row,target):
    return row != target and P[row] != Q[target]


assert sorted(ORIGINAL) == list(range(13))
assert all(allowed(row,ORIGINAL[row]) for row in range(13))
assert sum(COMPONENT_ID[row] != COMPONENT_ID[ORIGINAL[row]] for row in range(13)) == 4
assert set(REROUTED) == set(REMAINING)
assert all(allowed(row,target) for row,target in zip(REMAINING,REROUTED))
assert sum(target != ORIGINAL[row] for row,target in zip(REMAINING,REROUTED)) == 4
assert [row for row,target in zip(REMAINING,REROUTED) if target != ORIGINAL[row]] == [1,3,4,5]

SOURCE = tuple((row,column) for row in REMAINING for column in (P[row],Q[row]))
assert len(SOURCE) == 22 and len(set(SOURCE)) == 22
assert all(cross(SOURCE[i],SOURCE[j],SOURCE[k]) != 0 for i,j,k in combinations(range(len(SOURCE)),3))

IMAGE = dict(zip(REMAINING,REROUTED))
ANCHORS = tuple(((row,P[row]),(IMAGE[row],Q[IMAGE[row]])) for row in REMAINING)
assert len({point for anchor in ANCHORS for point in anchor}) == 22


def embed(lengths):
    points = list(SOURCE)
    labels = [-1] * len(points)
    for run in range(len(lengths)):
        first,second = ANCHORS[run]
        for index,point in enumerate(points):
            if point == first or point == second:
                labels[index] = run

    rows = {point[0] for point in points}
    columns = {point[1] for point in points}
    maximum_coordinate = max(max(abs(x),abs(y)) for x,y in points)

    for run,length in enumerate(lengths):
        first,second = ANCHORS[run]
        dx = second[0]-first[0]
        dy = second[1]-first[1]
        divisor = gcd(abs(dx),abs(dy))
        dx //= divisor
        dy //= divisor
        inserted = 0
        for magnitude in range(1,50000):
            for sign in (1,-1):
                candidate = (first[0]+sign*magnitude*dx, first[1]+sign*magnitude*dy)
                if candidate[0] in rows or candidate[1] in columns or candidate in points:
                    continue
                bad = False
                for left in range(len(points)):
                    for right in range(left+1,len(points)):
                        if cross(points[left],points[right],candidate) == 0:
                            if labels[left] == run and labels[right] == run:
                                continue
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    continue
                points.append(candidate)
                labels.append(run)
                rows.add(candidate[0])
                columns.add(candidate[1])
                maximum_coordinate = max(maximum_coordinate,abs(candidate[0]),abs(candidate[1]))
                inserted += 1
                break
            if inserted == length:
                break
        assert inserted == length

    for first,second,third in combinations(range(len(points)),3):
        if cross(points[first],points[second],points[third]) == 0:
            assert labels[first] >= 0 and labels[first] == labels[second] == labels[third]
    return maximum_coordinate


maximum_coordinate = 0
compositions_checked = 0
for composition in compositions(11):
    maximum_coordinate = max(maximum_coordinate,embed(composition))
    compositions_checked += 1

assert compositions_checked == 2 ** 10
assert maximum_coordinate == 132

print({
    "deleted_incidence_component_rows": sorted(DELETED_ROWS),
    "remaining_source_pairs": len(REMAINING),
    "original_minimum_cross_matching": ORIGINAL,
    "rerouted_image_by_remaining_row": dict(zip(REMAINING,REROUTED)),
    "changed_anchor_assignments": [1,3,4,5],
    "rerouting_distance": 4,
    "induced_source_cells": len(SOURCE),
    "compositions_checked": compositions_checked,
    "maximum_coordinate": maximum_coordinate,
    "all_compositions_pass": True,
    "remaining_gap": "this is one finite 13-to-11 coordinate lift; no uniform choice rule or recurrence across arbitrary source sizes is proved",
    "evidence_level": "exact_coordinate_lift_of_one_optimal_anchor_rerouting",
    "status": "passed",
})
