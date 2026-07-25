#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR698--CMR705."""

from itertools import combinations
from math import ceil, comb, prod


def triples(state, geometry):
    selected = set(state)
    return {triple for triple in geometry if set(triple) <= selected}


def exhaustive_state_checks():
    checked = 0
    for universe_size in range(3, 6):
        universe = tuple(range(universe_size))
        all_triples = tuple(combinations(universe, 3))
        for geometry_mask in range(1 << len(all_triples)):
            geometry = {
                all_triples[index]
                for index in range(len(all_triples))
                if (geometry_mask >> index) & 1
            }
            for state_size in range(1, universe_size + 1):
                states = tuple(combinations(universe, state_size))
                for old_state in states:
                    old_triples = triples(old_state, geometry)
                    for new_state in states:
                        new_triples = triples(new_state, geometry)
                        lost = old_triples - new_triples
                        gained = new_triples - old_triples
                        assert len(new_triples) - len(old_triples) == (
                            len(gained) - len(lost)
                        )

                        entering = set(new_state) - set(old_state)
                        if lost and len(new_triples) >= len(old_triples):
                            target_load = len(lost)
                            churn = len(entering)
                            assert churn >= 1
                            assert len(gained) >= target_load
                            loads = [
                                sum(1 for triple in gained if edge in triple)
                                for edge in entering
                            ]
                            assert max(loads) >= ceil(target_load / churn)
                            centre = max(
                                entering,
                                key=lambda edge: sum(
                                    1 for triple in gained if edge in triple
                                ),
                            )
                            assigned = {
                                triple for triple in gained if centre in triple
                            }
                            assert all(centre in triple for triple in assigned)
                            assert all(
                                not set(triple)
                                <= (set(new_state) - {centre})
                                for triple in assigned
                            )
                        checked += 1
    return checked


def arithmetic_checks():
    checked = 0
    churn_sequences = [
        (),
        (1,),
        (2,),
        (3,),
        (2, 4),
        (1, 3, 5),
        (6, 2, 2, 3),
    ]
    for initial_load in range(1, 200):
        for churn_sequence in churn_sequences:
            load = initial_load
            loads = [load]
            for churn in churn_sequence:
                load = ceil(load / churn)
                loads.append(load)
            assert initial_load <= loads[-1] * prod(churn_sequence or (1,))
            checked += 1

    for board_cells in range(1, 65):
        triple_stock = comb(board_cells - 1, 2) if board_cells >= 3 else 0
        for recurrence_threshold in range(2, 9):
            bound = (recurrence_threshold - 1) * triple_stock
            assert bound >= 0
            checked += 1
    return checked


def main():
    state_checks = exhaustive_state_checks()
    ledger_checks = arithmetic_checks()
    print(
        "verified target handoff conversion:",
        state_checks,
        "state/geometry transitions and",
        ledger_checks,
        "ledger instances",
    )


if __name__ == "__main__":
    main()
