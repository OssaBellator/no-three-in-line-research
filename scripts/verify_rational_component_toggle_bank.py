#!/usr/bin/env python3
"""Exhaust RI5s--RI5u on small permutation systems."""

from itertools import combinations, permutations, product


def matching_cells(perm: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(column, row) for column, row in enumerate(perm)}


def relative_components(
    current: tuple[int, ...], target: tuple[int, ...]
) -> list[tuple[int, ...]]:
    inverse = [0] * len(current)
    for column, row in enumerate(current):
        inverse[row] = column

    relative = [inverse[target[column]] for column in range(len(current))]
    seen = [False] * len(current)
    components: list[tuple[int, ...]] = []

    for start in range(len(current)):
        if seen[start]:
            continue
        cycle = []
        column = start
        while not seen[column]:
            seen[column] = True
            cycle.append(column)
            column = relative[column]
        if len(cycle) > 1:
            components.append(tuple(cycle))

    return components


def toggle_state(
    current: tuple[int, ...],
    target: tuple[int, ...],
    components: list[tuple[int, ...]],
    bits: tuple[int, ...],
) -> tuple[int, ...]:
    state = list(current)
    for component, bit in zip(components, bits, strict=True):
        if bit:
            for column in component:
                state[column] = target[column]
    return tuple(state)


def verify_active_toggles(maximum_size: int = 5) -> tuple[int, int]:
    state_count = 0
    triple_count = 0

    for size in range(2, maximum_size + 1):
        all_permutations = list(permutations(range(size)))

        for current in all_permutations:
            for target in all_permutations:
                components = relative_components(current, target)
                component_by_column = {
                    column: index
                    for index, component in enumerate(components)
                    for column in component
                }
                bank = []

                for bits in product((0, 1), repeat=len(components)):
                    state = toggle_state(current, target, components, bits)
                    assert sorted(state) == list(range(size))
                    bank.append(state)
                    state_count += 1

                if size < 3:
                    continue

                occurrences: dict[tuple[tuple[int, int], ...], int] = {}
                for state in bank:
                    for triple in combinations(sorted(matching_cells(state)), 3):
                        occurrences[triple] = occurrences.get(triple, 0) + 1

                for triple, count in occurrences.items():
                    prescribed_components = set()
                    for column, row in triple:
                        if column not in component_by_column:
                            continue
                        component_index = component_by_column[column]
                        assert row in (current[column], target[column])
                        prescribed_components.add(component_index)

                    rank = len(prescribed_components)
                    assert rank <= 3
                    assert count == 2 ** (len(components) - rank)
                    triple_count += 1

    return state_count, triple_count


def verify_blocker_repairs(maximum_size: int = 4) -> tuple[int, int]:
    toggle_count = 0
    repair_count = 0

    for size in range(2, maximum_size + 1):
        all_permutations = list(permutations(range(size)))

        for current in all_permutations:
            current_cells = matching_cells(current)

            for blocker in all_permutations:
                blocker_cells = matching_cells(blocker)
                if current_cells & blocker_cells:
                    continue

                for target in all_permutations:
                    components = relative_components(current, target)

                    for bits in product((0, 1), repeat=len(components)):
                        active = toggle_state(current, target, components, bits)
                        active_cells = matching_cells(active)
                        blocked = sorted(active_cells & blocker_cells)
                        blocked_count = len(blocked)
                        toggle_count += 1

                        if blocked_count == 0:
                            assert not active_cells & blocker_cells
                            repair_count += 1
                            continue

                        if blocked_count == 1:
                            fixed_column, fixed_row = blocked[0]
                            for auxiliary_column in range(size):
                                if auxiliary_column == fixed_column:
                                    continue
                                auxiliary_row = blocker[auxiliary_column]
                                repaired = list(blocker)
                                repaired[fixed_column] = auxiliary_row
                                repaired[auxiliary_column] = fixed_row
                                assert sorted(repaired) == list(range(size))
                                assert not active_cells & matching_cells(tuple(repaired))
                                repair_count += 1
                            continue

                        blocked_columns = [column for column, _ in blocked]
                        blocked_rows = [row for _, row in blocked]
                        derangement_count = 0

                        for assignment in permutations(range(blocked_count)):
                            if any(
                                assignment[index] == index
                                for index in range(blocked_count)
                            ):
                                continue

                            repaired = list(blocker)
                            for index, column in enumerate(blocked_columns):
                                repaired[column] = blocked_rows[assignment[index]]

                            assert sorted(repaired) == list(range(size))
                            assert not active_cells & matching_cells(tuple(repaired))
                            repair_count += 1
                            derangement_count += 1

                        assert derangement_count > 0

    return toggle_count, repair_count


def verify_failed_router(maximum_weight: int = 5) -> int:
    checks = 0
    for terms in product(range(maximum_weight + 1), repeat=4):
        total = sum(terms)
        if total == 0:
            continue
        assert max(terms) * 4 >= total
        checks += 1
    return checks


def main() -> None:
    active_states, active_triples = verify_active_toggles()
    blocker_states, blocker_repairs = verify_blocker_repairs()
    routers = verify_failed_router()
    print(
        "RI component toggle bank verified: "
        f"{active_states} active states, "
        f"{active_triples} exact triple probabilities, "
        f"{blocker_states} blocker toggle states, "
        f"{blocker_repairs} valid repairs, and "
        f"{routers} failed-bank routers"
    )


if __name__ == "__main__":
    main()
