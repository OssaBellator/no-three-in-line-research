#!/usr/bin/env python3
"""Complete finite checks for CMR1310--CMR1317."""

from collections import Counter, deque
from itertools import combinations, permutations

SIDE = 6
CELLS = [(x, y) for x in range(SIDE) for y in range(SIDE)]
INDEX = {cell: index for index, cell in enumerate(CELLS)}
PERMS = list(permutations(range(SIDE)))
SETS = [frozenset((x, permutation[x]) for x in range(SIDE)) for permutation in PERMS]
MASKS = [sum(1 << INDEX[cell] for cell in state) for state in SETS]
FULL = (1 << (SIDE * SIDE)) - 1


def collinear(first, second, third):
    (x1, y1), (x2, y2), (x3, y3) = first, second, third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


TRIPLES = [
    sum(1 << index for index in triple)
    for triple in combinations(range(SIDE * SIDE), 3)
    if collinear(*(CELLS[index] for index in triple))
]


def state_info(mask):
    value = 0
    target_cells = 0
    for triple in TRIPLES:
        if mask & triple == triple:
            value += 1
            target_cells |= triple
    return value, target_cells


def build_data():
    disjoint = [
        [second for second in range(len(PERMS)) if not MASKS[first] & MASKS[second]]
        for first in range(len(PERMS))
    ]
    assert all(len(values) == 265 for values in disjoint)

    ordered = []
    information = {}
    for opposite in range(len(PERMS)):
        for current in disjoint[opposite]:
            mask = MASKS[opposite] | MASKS[current]
            ordered.append((opposite, current, mask))
            if mask not in information:
                information[mask] = state_info(mask)

    assert len(TRIPLES) == 372
    assert len(ordered) == 190800
    assert len(information) == 67950
    assert sum(information[mask][0] == 0 for _, _, mask in ordered) == 116
    assert sum(value == 0 for value, _ in information.values()) == 50
    assert max(value for value, _ in information.values()) == 40
    return disjoint, ordered, information


def build_minimum_table(disjoint, information):
    minimum = {}
    for opposite in range(len(PERMS)):
        opposite_mask = MASKS[opposite]
        outside = FULL ^ opposite_mask
        bits = outside
        while bits:
            bit = bits & -bits
            minimum[(opposite, bit.bit_length() - 1)] = 10**9
            bits -= bit
        for response in disjoint[opposite]:
            response_mask = MASKS[response]
            value = information[opposite_mask | response_mask][0]
            bits = outside & ~response_mask
            while bits:
                bit = bits & -bits
                key = (opposite, bit.bit_length() - 1)
                minimum[key] = min(minimum[key], value)
                bits -= bit
    assert len(minimum) == 21600
    assert all(value < 10**9 for value in minimum.values())
    return minimum


def best_change(opposite, current, information, minimum):
    value, targets = information[MASKS[opposite] | MASKS[current]]
    if value == 0:
        return None
    answer = 10**9
    bits = targets
    while bits:
        bit = bits & -bits
        fixed = opposite if MASKS[current] & bit else current
        answer = min(answer, minimum[(fixed, bit.bit_length() - 1)] - value)
        bits -= bit
    return answer


def classify_traps(disjoint, ordered, information, minimum):
    changes = {
        (opposite, current): best_change(opposite, current, information, minimum)
        for opposite, current, _ in ordered
    }
    assert sum(change is not None and change < 0 for change in changes.values()) == 189476
    traps = {state for state, change in changes.items() if change == 0}
    assert len(traps) == 1208
    assert Counter(
        information[MASKS[first] | MASKS[second]][0]
        for first, second in traps
    ) == Counter({1: 1128, 2: 80})

    destinations = {}
    reverse = {state: set() for state in traps}
    direct_exit = set()
    for opposite, current in traps:
        value, target_cells = information[MASKS[opposite] | MASKS[current]]
        found = set()
        bits = target_cells
        while bits:
            bit = bits & -bits
            fixed = opposite if MASKS[current] & bit else current
            for response in disjoint[fixed]:
                if MASKS[response] & bit:
                    continue
                if information[MASKS[fixed] | MASKS[response]][0] == value:
                    found.add((fixed, response))
            bits -= bit
        assert found
        destinations[(opposite, current)] = found
        if any(changes[state] is not None and changes[state] < 0 for state in found):
            direct_exit.add((opposite, current))
        for state in found:
            if state in traps:
                reverse[state].add((opposite, current))

    distance = {state: 1 for state in direct_exit}
    queue = deque(direct_exit)
    while queue:
        state = queue.popleft()
        for previous in reverse[state]:
            if previous not in distance:
                distance[previous] = distance[state] + 1
                queue.append(previous)
    assert Counter(distance.values()) == Counter({1: 1120, 2: 64})
    closed = traps - set(distance)
    assert len(closed) == 24
    assert len({MASKS[first] | MASKS[second] for first, second in closed}) == 12
    assert all(information[MASKS[first] | MASKS[second]][0] == 1 for first, second in closed)

    successor = {}
    for state in closed:
        internal = [candidate for candidate in destinations[state] if candidate in closed]
        assert len(internal) == 1
        successor[state] = internal[0]

    cycle_nodes = set()
    cycles = []
    globally_seen = set()
    for start in closed:
        if start in globally_seen:
            continue
        path = []
        position = {}
        state = start
        while state not in position and state not in globally_seen:
            position[state] = len(path)
            path.append(state)
            state = successor[state]
        if state in position:
            cycle = path[position[state]:]
            cycles.append(cycle)
            cycle_nodes.update(cycle)
        globally_seen.update(path)

    assert Counter(len(cycle) for cycle in cycles) == Counter({2: 6})
    assert len(cycle_nodes) == 12
    assert Counter(
        0 if state in cycle_nodes else 1
        for state in closed
    ) == Counter({0: 12, 1: 12})
    assert all(successor[state] in cycle_nodes for state in closed - cycle_nodes)
    return changes, traps, distance, closed, cycles


def verify_clean_construction():
    first = PERMS.index((4, 3, 5, 0, 2, 1))
    second = PERMS.index((3, 1, 0, 5, 4, 2))
    assert not MASKS[first] & MASKS[second]
    assert state_info(MASKS[first] | MASKS[second]) == (0, 0)


def main():
    disjoint, ordered, information = build_data()
    minimum = build_minimum_table(disjoint, information)
    result = classify_traps(disjoint, ordered, information, minimum)
    verify_clean_construction()
    print(
        "verified side-six target-response traps:",
        len(ordered),
        "ordered states,",
        len(information),
        "physical states,",
        len(minimum),
        "response entries,",
        sum(change is not None and change < 0 for change in result[0].values()),
        "immediate improvements,",
        len(result[1]),
        "immediate traps, distances",
        dict(sorted(Counter(result[2].values()).items())),
        ",",
        len(result[3]),
        "closed ordered traps with",
        len(result[4]),
        "two-cycles and twelve feeders, plus one clean CMF1 escape",
    )


if __name__ == "__main__":
    main()
