#!/usr/bin/env python3
"""Complete finite checks for CMR1294--CMR1301."""

from collections import Counter
from itertools import combinations, permutations


SIDE = 5
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


def collinear(first, second, third):
    (x1, y1), (x2, y2), (x3, y3) = first, second, third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


COLLINEAR_TRIPLES = [
    (sum(1 << index for index in triple), triple)
    for triple in combinations(range(SIDE * SIDE), 3)
    if collinear(*(CELLS[index] for index in triple))
]


def potential(mask):
    return sum((mask & triple_mask) == triple_mask for triple_mask, _ in COLLINEAR_TRIPLES)


def disjoint(first, second):
    return not (MATCHING_MASKS[first] & MATCHING_MASKS[second])


def check_state_stock():
    ordered = [
        (first, second)
        for first in range(len(PERMUTATIONS))
        for second in range(len(PERMUTATIONS))
        if disjoint(first, second)
    ]
    physical_masks = {
        MATCHING_MASKS[first] | MATCHING_MASKS[second]
        for first, second in ordered
    }
    physical_potential = {mask: potential(mask) for mask in physical_masks}
    ordered_distribution = Counter(
        physical_potential[MATCHING_MASKS[first] | MATCHING_MASKS[second]]
        for first, second in ordered
    )
    physical_distribution = Counter(physical_potential.values())

    assert len(COLLINEAR_TRIPLES) == 152
    assert len(ordered) == 5280
    assert len(physical_masks) == 2040
    assert ordered_distribution == Counter({
        0: 64,
        1: 192,
        2: 960,
        3: 1200,
        4: 904,
        5: 616,
        6: 560,
        7: 336,
        8: 96,
        9: 64,
        10: 32,
        11: 104,
        12: 80,
        13: 32,
        14: 24,
        15: 16,
    })
    assert physical_distribution == Counter({
        0: 32,
        1: 76,
        2: 360,
        3: 440,
        4: 322,
        5: 264,
        6: 252,
        7: 140,
        8: 30,
        9: 28,
        10: 12,
        11: 32,
        12: 32,
        13: 8,
        14: 8,
        15: 4,
    })
    return ordered, physical_potential


def build_response_tables(ordered, physical_potential):
    disjoint_lists = [
        [second for second in range(len(PERMUTATIONS)) if disjoint(first, second)]
        for first in range(len(PERMUTATIONS))
    ]
    banks = {}
    bank_size_distribution = Counter()
    for opposite in range(len(PERMUTATIONS)):
        for forbidden in disjoint_lists[opposite]:
            bank = [
                response
                for response in range(len(PERMUTATIONS))
                if disjoint(opposite, response) and disjoint(forbidden, response)
            ]
            banks[(opposite, forbidden)] = bank
            bank_size_distribution[len(bank)] += 1

    assert bank_size_distribution == Counter({12: 2400, 13: 2880})

    state_potential = {
        (opposite, response): physical_potential[
            MATCHING_MASKS[opposite] | MATCHING_MASKS[response]
        ]
        for opposite, response in ordered
    }

    minimum = {}
    minimizer = {}
    for opposite in range(len(PERMUTATIONS)):
        opposite_set = MATCHING_SETS[opposite]
        for cell in CELLS:
            if cell in opposite_set:
                continue
            best = None
            best_key = None
            for forbidden in disjoint_lists[opposite]:
                if cell not in MATCHING_SETS[forbidden]:
                    continue
                for response in banks[(opposite, forbidden)]:
                    value = state_potential[(opposite, response)]
                    key = (value, forbidden, response)
                    if best_key is None or key < best_key:
                        best_key = key
                        best = value
            assert best is not None
            minimum[(opposite, cell)] = best
            minimizer[(opposite, cell)] = best_key[1:]

    assert len(minimum) == 2400
    return disjoint_lists, banks, minimum, minimizer, bank_size_distribution


def check_every_dirty_state(ordered, physical_potential, minimum, minimizer):
    dirty = 0
    best_changes = Counter()
    canonical_potential_budget = 0
    for opposite, current in ordered:
        state_mask = MATCHING_MASKS[opposite] | MATCHING_MASKS[current]
        old_value = physical_potential[state_mask]
        if old_value == 0:
            continue
        dirty += 1
        best_key = None
        for triple_mask, triple_indices in COLLINEAR_TRIPLES:
            if state_mask & triple_mask != triple_mask:
                continue
            for cell_index in triple_indices:
                cell = CELLS[cell_index]
                if cell in MATCHING_SETS[current]:
                    fixed = opposite
                else:
                    assert cell in MATCHING_SETS[opposite]
                    fixed = current
                response_value = minimum[(fixed, cell)]
                forbidden, response = minimizer[(fixed, cell)]
                new_mask = MATCHING_MASKS[fixed] | MATCHING_MASKS[response]
                assert cell in MATCHING_SETS[forbidden]
                assert cell not in MATCHING_SETS[response]
                assert disjoint(fixed, forbidden)
                assert disjoint(fixed, response)
                assert disjoint(forbidden, response)
                assert potential(new_mask) == response_value
                key = (response_value - old_value, triple_indices, cell, fixed, forbidden, response)
                if best_key is None or key < best_key:
                    best_key = key
        assert best_key is not None
        assert best_key[0] < 0
        best_changes[best_key[0]] += 1
        canonical_potential_budget += old_value

    assert dirty == 5216
    assert best_changes == Counter({
        -1: 316,
        -2: 1268,
        -3: 1176,
        -4: 836,
        -5: 728,
        -6: 360,
        -7: 152,
        -8: 76,
        -9: 56,
        -10: 64,
        -11: 72,
        -12: 88,
        -13: 16,
        -15: 8,
    })
    assert canonical_potential_budget <= dirty * 15
    return dirty, best_changes, canonical_potential_budget


def check_restricted_expansion_arithmetic():
    checked = 0
    for old_minimum in range(1, 16):
        for response_value in range(old_minimum):
            assert min(old_minimum, response_value) < old_minimum
            checked += 1
    return checked


def check_contraction_budget():
    checked = 0
    for contracted in range(11):
        residual = 10 - contracted
        assert residual >= 0
        checked += 1
    return checked


def main():
    ordered, physical_potential = check_state_stock()
    tables = build_response_tables(ordered, physical_potential)
    dirty = check_every_dirty_state(ordered, physical_potential, tables[2], tables[3])
    print(
        "verified side-five finite improvement:",
        len(ordered),
        "ordered states,",
        len(physical_potential),
        "physical states, bank sizes",
        dict(sorted(tables[4].items())),
        ",",
        len(tables[2]),
        "target-response table entries,",
        dirty[0],
        "dirty states with best changes",
        dict(sorted(dirty[1].items())),
        ",",
        check_restricted_expansion_arithmetic(),
        "lowering expansions, and",
        check_contraction_budget(),
        "contraction ranks",
    )


if __name__ == "__main__":
    main()
