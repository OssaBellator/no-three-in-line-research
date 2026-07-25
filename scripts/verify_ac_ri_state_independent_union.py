#!/usr/bin/env python3
"""Verify AC3cy--AC3da on exhaustive small full-I6 union banks."""

from itertools import permutations, product


def derangements(size):
    return [
        perm
        for perm in permutations(range(size))
        if all(perm[index] != index for index in range(size))
    ]


def cells(mapping):
    return {(column, row) for column, row in enumerate(mapping)}


def i6_states(m, h, closure_count=0):
    states = []
    block_size = m * h
    for coset_perm in permutations(range(m)):
        for shifts in product(range(h), repeat=m):
            mapping = {}
            for alpha in range(m):
                for group_coordinate in range(h):
                    column = alpha * h + group_coordinate
                    target_coset = coset_perm[alpha]
                    target_coordinate = (-group_coordinate - shifts[alpha]) % h
                    mapping[column] = target_coset * h + target_coordinate
            for index in range(closure_count):
                mapping[block_size + index] = block_size + index
            states.append(tuple(mapping[index] for index in range(block_size + closure_count)))
    return states


def repair_menu(blocker, active):
    selected = tuple(
        column
        for column in range(len(blocker))
        if blocker[column] == active[column]
    )
    count = len(selected)

    if count == 0:
        return [blocker], selected

    if count == 1:
        blocked = selected[0]
        menu = []
        for auxiliary in range(len(blocker)):
            if auxiliary == blocked:
                continue
            repaired = list(blocker)
            repaired[blocked], repaired[auxiliary] = (
                blocker[auxiliary],
                blocker[blocked],
            )
            menu.append(tuple(repaired))
        return menu, selected

    menu = []
    for local_perm in derangements(count):
        repaired = list(blocker)
        for local_index, column in enumerate(selected):
            repaired[column] = blocker[selected[local_perm[local_index]]]
        menu.append(tuple(repaired))
    return menu, selected


def verify_full_banks(maximum_block_size=4):
    bank_checks = 0
    closure_cells = 0
    transfer_cells = 0

    for m in range(1, maximum_block_size + 1):
        for h in range(1, maximum_block_size + 1):
            block_size = m * h
            if block_size < 2 or block_size > maximum_block_size:
                continue

            for closure_count in range(3):
                total_size = block_size + closure_count
                if total_size > 6:
                    continue
                states = i6_states(m, h, closure_count)
                common_active = set.intersection(*(cells(state) for state in states))
                expected_closure = {
                    (block_size + index, block_size + index)
                    for index in range(closure_count)
                }
                assert common_active == expected_closure

                for blocker in permutations(range(total_size)):
                    joint_states = []
                    selected_sets = []
                    for active in states:
                        menu, selected = repair_menu(blocker, active)
                        selected_sets.append(set(selected))
                        for repaired in menu:
                            joint_states.append(cells(active) | cells(repaired))

                    common_union = set.intersection(*joint_states)
                    new_common = common_union - cells(blocker)

                    for cell in new_common:
                        if cell in common_active:
                            assert cell in expected_closure
                            closure_cells += 1
                            continue

                        active_indices = [
                            index
                            for index, active in enumerate(states)
                            if cell in cells(active)
                        ]
                        if active_indices:
                            # A transferred cell forces the minimal two-state bank.
                            assert block_size == 2
                            assert m * h == 2
                            assert len(states) == 2
                            assert len(active_indices) == 1

                            absent_index = 1 - active_indices[0]
                            selected = selected_sets[absent_index]
                            assert len(selected) == 2
                            first, second = sorted(selected)
                            crossed = {
                                (first, blocker[second]),
                                (second, blocker[first]),
                            }
                            assert cell in crossed

                            # The two active states are the two diagonals of the
                            # same 2 by 2 block.
                            assert set(selected) == {0, 1}
                            block_square = {(0, 0), (0, 1), (1, 0), (1, 1)}
                            other_diagonal = cells(states[active_indices[0]]) & block_square
                            assert len(other_diagonal) == 2
                            transfer_cells += 1
                        else:
                            # A never-active common new cell comes from one fixed
                            # two-blocker pair.
                            assert all(len(selected) == 2 for selected in selected_sets)
                            pairs = selected_sets
                            assert all(pair == pairs[0] for pair in pairs)
                            first, second = sorted(pairs[0])
                            crossed = {
                                (first, blocker[second]),
                                (second, blocker[first]),
                            }
                            assert cell in crossed

                    bank_checks += 1

    return bank_checks, closure_cells, transfer_cells


def verify_universal_closure_example():
    # Two I6 columns, two fixed closure anchors, and two unchanged outside
    # active columns. The blocker sends the I6 columns to outside rows, so the
    # only desired blocker cells in every active state are the closure anchors.
    active_states = [
        (0, 1, 2, 3, 4, 5),
        (1, 0, 2, 3, 4, 5),
    ]
    blocker = (4, 5, 2, 3, 0, 1)
    unchanged_current_active = {(4, 4), (5, 5)}

    joint_states = []
    selected_sets = []
    for active in active_states:
        menu, selected = repair_menu(blocker, active)
        selected_sets.append(set(selected))
        for repaired in menu:
            joint_states.append(cells(active) | cells(repaired))

    assert selected_sets == [{2, 3}, {2, 3}]
    common_union = set.intersection(*joint_states)
    new_common = common_union - cells(blocker) - unchanged_current_active
    assert new_common == {(2, 3), (3, 2)}
    return len(new_common)


def verify_rectangle_identities(maximum=20):
    checks = 0
    for c1 in range(maximum):
        for c2 in range(maximum):
            if c1 == c2:
                continue
            for r1 in range(maximum):
                for r2 in range(maximum):
                    if r1 == r2:
                        continue
                    q1 = (c1, r1)
                    q2 = (c2, r2)
                    z12 = (c1, r2)
                    z21 = (c2, r1)
                    assert (
                        z12[0] + z21[0],
                        z12[1] + z21[1],
                    ) == (
                        q1[0] + q2[0],
                        q1[1] + q2[1],
                    )
                    assert (c1 * r2) * (c2 * r1) == (c1 * r1) * (c2 * r2)
                    checks += 1
    return checks


def verify_weight_router(maximum=36):
    checks = 0
    for total in range(1, maximum + 1):
        for first in range(total + 1):
            for second in range(total - first + 1):
                third = total - first - second
                assert max(first, second, third) * 3 >= total
                for profile_count in range(1, 8):
                    selected = max(first, second, third)
                    quotient, remainder = divmod(selected, profile_count)
                    largest = quotient + (1 if remainder else 0)
                    assert largest * profile_count >= selected
                    assert 3 * largest * profile_count >= total
                    checks += 1
    return checks


def main():
    banks, closure, transfer = verify_full_banks()
    universal = verify_universal_closure_example()
    rectangles = verify_rectangle_identities()
    weights = verify_weight_router()
    print(
        "AC RI state-independent union: verified "
        f"{banks} full-bank/blocker systems, {closure} closure cells, "
        f"{transfer} layer-transfer cells, {universal} universal-closure cells, "
        f"{rectangles} rectangle identities, and {weights} weighted routers"
    )


if __name__ == "__main__":
    main()
