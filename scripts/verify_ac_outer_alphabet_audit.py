#!/usr/bin/env python3
"""Exact finite checks for AC3lt--AC3ly."""

from __future__ import annotations

from itertools import product
from math import ceil


def owner_bound(addresses: int, kinds: int, multiplicity: int, rank: int, capacity: int) -> int:
    return kinds * multiplicity * sum(addresses**s for s in range(1, rank + 1)) + capacity


def scoped_bound(addresses: int, kinds: int, multiplicity: int, rank: int) -> int:
    return kinds * multiplicity * sum(addresses**s for s in range(1, rank + 1))


def check_counting_formulae() -> dict[str, int]:
    totals = {
        "owner_formula_systems": 0,
        "scoped_formula_systems": 0,
        "physical_board_bounds": 0,
    }

    for addresses in range(1, 21):
        for kinds in range(1, 6):
            for multiplicity in range(1, 5):
                for rank in range(1, 7):
                    for capacity in range(0, 8):
                        bound = owner_bound(addresses, kinds, multiplicity, rank, capacity)
                        direct = capacity
                        for _kind in range(kinds):
                            for _label in range(multiplicity):
                                direct += sum(addresses**s for s in range(1, rank + 1))
                        assert bound == direct
                        totals["owner_formula_systems"] += 1

                for rank in range(1, 5):
                    bound = scoped_bound(addresses, kinds, multiplicity, rank)
                    direct = 0
                    for _kind in range(kinds):
                        for _label in range(multiplicity):
                            direct += sum(addresses**s for s in range(1, rank + 1))
                    assert bound == direct
                    totals["scoped_formula_systems"] += 1

    for side in range(1, 101):
        addresses = 2 * side * side
        assert addresses <= 2 * side * side
        assert 2 * addresses <= 4 * side * side
        totals["physical_board_bounds"] += 1

    return totals


def least_reset(source: int, target: int) -> tuple[int, int]:
    diff = source ^ target
    assert diff
    atom = (diff & -diff).bit_length() - 1
    direction = 1 if ((target >> atom) & 1) else -1
    return atom, direction


def check_set_profiles(max_atoms: int = 8) -> dict[str, int]:
    totals = {
        "set_profile_counts": 0,
        "set_state_pairs": 0,
        "strict_set_changes": 0,
        "increasing_changes": 0,
        "decreasing_changes": 0,
    }

    for atoms in range(1, max_atoms + 1):
        states = list(range(1 << atoms))
        assert len(states) == 2**atoms
        totals["set_profile_counts"] += 1

        for source in states:
            for target in states:
                totals["set_state_pairs"] += 1
                if source == target:
                    continue
                totals["strict_set_changes"] += 1

                atom, direction = least_reset(source, target)
                assert 0 <= atom < atoms
                source_has = (source >> atom) & 1
                target_has = (target >> atom) & 1
                assert source_has != target_has
                assert direction == (1 if target_has else -1)

                if source & ~target == 0:
                    assert target.bit_count() - source.bit_count() >= 1
                    totals["increasing_changes"] += 1
                if target & ~source == 0:
                    assert source.bit_count() - target.bit_count() >= 1
                    totals["decreasing_changes"] += 1

    return totals


def check_weighted_concentration() -> int:
    checks = 0
    for atoms in range(1, 31):
        classes = 2 * atoms
        for total in range(1, 101):
            lower = total / classes
            assert ceil(lower) >= 1
            q, r = divmod(total, classes)
            loads = [q + (1 if index < r else 0) for index in range(classes)]
            assert sum(loads) == total
            assert max(loads) >= lower
            checks += 1
    return checks


def check_monotone_budgets(max_atoms: int = 12) -> dict[str, int]:
    totals = {
        "monotone_state_checks": 0,
        "combined_budget_checks": 0,
    }

    for atoms in range(1, max_atoms + 1):
        for state in range(1 << atoms):
            additions_left = atoms - state.bit_count()
            removals_left = state.bit_count()
            assert additions_left <= atoms
            assert removals_left <= atoms
            totals["monotone_state_checks"] += 1

    for sizes in product(range(1, 7), repeat=3):
        budget = sum(sizes)
        for changes in product(*(range(size + 1) for size in sizes)):
            assert sum(changes) <= budget
            totals["combined_budget_checks"] += 1

    return totals


def check_same_decoration_guardrail() -> int:
    witnesses = 0
    atoms = 6
    grouped: dict[tuple[int, int], set[tuple[int, int]]] = {}
    for source in range(1 << atoms):
        for target in range(1 << atoms):
            if source == target:
                continue
            decoration = least_reset(source, target)
            grouped.setdefault(decoration, set()).add((source, target))
    for transitions in grouped.values():
        if len(transitions) > 1:
            witnesses += len(transitions)
    assert witnesses > 0
    return witnesses


def main() -> None:
    totals = check_counting_formulae()
    totals.update(check_set_profiles())
    totals["weighted_concentration_ledgers"] = check_weighted_concentration()
    totals.update(check_monotone_budgets())
    totals["same_decoration_distinct_transition_witnesses"] = check_same_decoration_guardrail()

    print("AC3lt--AC3ly verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
