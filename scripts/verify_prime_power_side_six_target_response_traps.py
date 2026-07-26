#!/usr/bin/env python3
"""Complete finite checks for CMR1310--CMR1317."""

from collections import Counter, deque
from itertools import combinations, permutations


SIDE = 6
CELLS = [(row, column) for row in range(SIDE) for column in range(SIDE)]
CELL_INDEX = {cell: index for index, cell in enumerate(CELLS)}
PERMUTATIONS = list(permutations(range(SIDE)))
MATCHING_SETS = [
    frozenset((row, permutation[row]) for row in range(SIDE))
    for permutation in PERMUTATIONS
]
MATCHING_MASKS = [
    sum(1 << CELL_INDEX[cell] for cell in matching)
    for matching in MATCHING_SETS
]
FULL_MASK = (1 << (SIDE * SIDE)) - 1


def collinear(first, second, third):
    (x1, y1), (x2, y2), (x3, y3) = first, second, third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


COLLINEAR_TRIPLES = [
    (sum(1 << index for index in triple), triple)
    for triple in combinations(range(SIDE * SIDE), 3)
    if collinear(*(CELLS[index] for index in triple))
]


def potential_and_target_cells(mask):
    value = 0
    target_cells = 0
    for triple_mask, _triple in COLLINEAR_TRIPLES:
        if mask & triple_mask == triple_mask:
            value += 1
            target_cells |= triple_mask
    return value, target_cells


def disjoint_lists():
    return [
        [
            second
            for second in range(len(PERMUTATIONS))
            if not MATCHING_MASKS[first] & MATCHING_MASKS[second]
        ]
        for first in range(len(PERMUTATIONS))
    ]


def build_state_stock(disjoint):
    ordered = []
    state_info = {}
    for opposite in range(len(PERMUTATIONS)):
        for current in disjoint[opposite]:
            mask = MATCHING_MASKS[opposite] | MATCHING_MASKS[current]
            ordered.append((opposite, current, mask))
            if mask not in state_info:
                state_info[mask] = potential_and_target_cells(mask)

    ordered_distribution = Counter(state_info[mask][0] for _, _, mask in ordered)
    physical_distribution = Counter(value for value, _targets in state_info.values())
    assert len(COLLINEAR_TRIPLES) == 372
    assert len(ordered) == 190800
    assert len(state_info) == 67950
    assert ordered_distribution == Counter({
        0: 116,
        1: 1880,
        2: 11616,
        3: 24544,
        4: 30356,
        5: 26920,
        6: 27164,
        7: 22360,
        8: 13688,
        9: 7192,
        10: 4828,
        11: 4152,
        12: 5380,
        13: 3160,
        14: 2080,
        15: 1680,
        16: 1248,
        17: 240,
        18: 32,
        19: 64,
        20: 332,
        21: 312,
        22: 768,
        23: 200,
        24: 248,
        25: 96,
        26: 80,
        27: 16,
        30: 40,
        40: 8,
    })
    assert physical_distribution == Counter({
        0: 50,
        1: 712,
        2: 4060,
        3: 8936,
        4: 10752,
        5: 9356,
        6: 9308,
        7: 8116,
        8: 4857,
        9: 2616,
        10: 1810,
        11: 1544,
        12: 2120,
        13: 1252,
        14: 752,
        15: 580,
        16: 416,
        17: 72,
        18: 8,
        19: 16,
        20: 88,
        21: 108,
        22: 228,
        23: 76,
        24: 66,
        25: 24,
        26: 14,
        27: 4,
        30: 8,
        40: 1,
    })
    return ordered, state_info, ordered_distribution, physical_distribution


def build_extension_free_minima(disjoint, state_info):
    minimum = {}
    minimizer = {}
    for opposite in range(len(PERMUTATIONS)):
        opposite_mask = MATCHING_MASKS[opposite]
        outside = FULL_MASK ^ opposite_mask
        bits = outside
        while bits:
            bit = bits & -bits
            cell_index = bit.bit_length() - 1
            minimum[(opposite, cell_index)] = 10**9
            minimizer[(opposite, cell_index)] = None
            bits -= bit

        for response in disjoint[opposite]:
            response_mask = MATCHING_MASKS[response]
            value = state_info[opposite_mask | response_mask][0]
            eligible = outside & ~response_mask
            bits = eligible
            while bits:
                bit = bits & -bits
                cell_index = bit.bit_length() - 1
                if value < minimum[(opposite, cell_index)]:
                    minimum[(opposite, cell_index)] = value
                    minimizer[(opposite, cell_index)] = response
                bits -= bit

    assert len(minimum) == 21600
    assert all(value < 10**9 for value in minimum.values())
    return minimum, minimizer


def state_best_change(opposite, current, state_info, minimum):
    mask = MATCHING_MASKS[opposite] | MATCHING_MASKS[current]
    value, target_cells = state_info[mask]
    if value == 0:
        return None
    best = 10**9
    bits = target_cells
    while bits:
        bit = bits & -bits
        cell_index = bit.bit_length() - 1
        fixed = opposite if MATCHING_MASKS[current] & bit else current
        best = min(best, minimum[(fixed, cell_index)] - value)
        bits -= bit
    return best


def classify_immediate_traps(ordered, state_info, minimum):
    best_change = {}
    distribution = Counter()
    for opposite, current, _mask in ordered:
        change = state_best_change(opposite, current, state_info, minimum)
        best_change[(opposite, current)] = change
        if change is not None:
            distribution[change] += 1

    immediate_traps = {
        state for state, change in best_change.items() if change == 0
    }
    assert sum(count for change, count in distribution.items() if change < 0) == 189476
    assert len(immediate_traps) == 1208
    trap_potentials = Counter(
        state_info[MATCHING_MASKS[first] | MATCHING_MASKS[second]][0]
        for first, second in immediate_traps
    )
    assert trap_potentials == Counter({1: 1128, 2: 80})
    return best_change, immediate_traps, distribution


def build_equal_graph(immediate_traps, best_change, disjoint, state_info):
    equal_destinations = {}
    reverse = {state: set() for state in immediate_traps}
    direct_exit = set()

    for opposite, current in immediate_traps:
        mask = MATCHING_MASKS[opposite] | MATCHING_MASKS[current]
        value, target_cells = state_info[mask]
        destinations = set()
        bits = target_cells
        while bits:
            bit = bits & -bits
            cell_index = bit.bit_length() - 1
            fixed = opposite if MATCHING_MASKS[current] & bit else current
            for response in disjoint[fixed]:
                if MATCHING_MASKS[response] & bit:
                    continue
                new_mask = MATCHING_MASKS[fixed] | MATCHING_MASKS[response]
                if state_info[new_mask][0] == value:
                    destinations.add((fixed, response))
            bits -= bit
        assert destinations
        equal_destinations[(opposite, current)] = destinations
        if any(
            best_change[destination] is not None
            and best_change[destination] < 0
            for destination in destinations
        ):
            direct_exit.add((opposite, current))
        for destination in destinations:
            if destination in immediate_traps:
                reverse[destination].add((opposite, current))

    distance = {state: 1 for state in direct_exit}
    queue = deque(direct_exit)
    while queue:
        state = queue.popleft()
        for predecessor in reverse[state]:
            if predecessor not in distance:
                distance[predecessor] = distance[state] + 1
                queue.append(predecessor)

    assert Counter(distance.values()) == Counter({1: 1120, 2: 64})
    closed = immediate_traps - set(distance)
    assert len(closed) == 24
    return equal_destinations, distance, closed


def classify_closed_core(equal_destinations, closed, state_info):
    assert len({MATCHING_MASKS[first] | MATCHING_MASKS[second] for first, second in closed}) == 12
    assert all(
        state_info[MATCHING_MASKS[first] | MATCHING_MASKS[second]][0] == 1
        for first, second in closed
    )
    successor = {}
    for state in closed:
        internal = [destination for destination in equal_destinations[state] if destination in closed]
        assert len(internal) == 1
        successor[state] = internal[0]

    unvisited = set(closed)
    cycle_lengths = []
    while unvisited:
        start = next(iter(unvisited))
        order = {}
        path = []
        state = start
        while state not in order:
            order[state] = len(path)
            path.append(state)
            state = successor[state]
        cycle = path[order[state]:]
        cycle_lengths.append(len(cycle))
        unvisited -= set(path)
    assert Counter(cycle_lengths) == Counter({1: 12, 2: 6})
    return Counter(cycle_lengths)


def verify_clean_construction():
    first = (4, 3, 5, 0, 2, 1)
    second = (3, 1, 0, 5, 4, 2)
    first_index = PERMUTATIONS.index(first)
    second_index = PERMUTATIONS.index(second)
    assert not MATCHING_MASKS[first_index] & MATCHING_MASKS[second_index]
    mask = MATCHING_MASKS[first_index] | MATCHING_MASKS[second_index]
    value, target_cells = potential_and_target_cells(mask)
    assert value == 0
    assert target_cells == 0
    return mask


def main():
    disjoint = disjoint_lists()
    assert all(len(values) == 265 for values in disjoint)
    stock = build_state_stock(disjoint)
    minima = build_extension_free_minima(disjoint, stock[1])
    traps = classify_immediate_traps(stock[0], stock[1], minima[0])
    equal = build_equal_graph(traps[1], traps[0], disjoint, stock[1])
    cycles = classify_closed_core(equal[0], equal[2], stock[1])
    verify_clean_construction()
    print(
        "verified side-six target-response traps:",
        len(stock[0]),
        "ordered states,",
        len(stock[1]),
        "physical states,",
        len(minima[0]),
        "response-table entries,",
        sum(count for change, count in traps[2].items() if change < 0),
        "immediate improvements,",
        len(traps[1]),
        "immediate traps, distances",
        dict(sorted(Counter(equal[1].values()).items())),
        ",",
        len(equal[2]),
        "closed ordered traps with cycles",
        dict(sorted(cycles.items())),
        "and one clean CMF1 escape",
    )


if __name__ == "__main__":
    main()
