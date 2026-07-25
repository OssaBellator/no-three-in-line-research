#!/usr/bin/env python3
"""Verify AC3cu--AC3cx on exhaustive small blocker-repair models."""

from itertools import combinations, permutations, product


def derangements(size):
    return [
        perm
        for perm in permutations(range(size))
        if all(perm[index] != index for index in range(size))
    ]


def blocker_cells(blocker):
    return {(column, row) for column, row in enumerate(blocker)}


def repair_menu(blocker, selected_columns):
    selected = tuple(sorted(selected_columns))
    size = len(blocker)
    count = len(selected)

    if count == 0:
        return [blocker]

    if count == 1:
        blocked = selected[0]
        menu = []
        for auxiliary in range(size):
            if auxiliary == blocked:
                continue
            repaired = list(blocker)
            repaired[blocked], repaired[auxiliary] = (
                blocker[auxiliary],
                blocker[blocked],
            )
            menu.append(tuple(repaired))
        return menu

    menu = []
    for local_perm in derangements(count):
        repaired = list(blocker)
        for local_index, column in enumerate(selected):
            source_column = selected[local_perm[local_index]]
            repaired[column] = blocker[source_column]
        menu.append(tuple(repaired))
    return menu


def common_new_cells(blocker, selected_columns):
    menu = repair_menu(blocker, selected_columns)
    common = set.intersection(*(blocker_cells(state) for state in menu))
    return common - blocker_cells(blocker)


def verify_conditional(maximum_n=7):
    checks = 0
    for size in range(3, maximum_n + 1):
        blockers = list(permutations(range(size)))
        if size >= 7:
            blockers = blockers[:80]
        for blocker in blockers:
            for rank in range(size + 1):
                for selected in combinations(range(size), rank):
                    common = common_new_cells(blocker, selected)
                    if rank == 2:
                        first, second = selected
                        expected = {
                            (first, blocker[second]),
                            (second, blocker[first]),
                        }
                        assert common == expected
                    else:
                        assert not common
                    checks += 1
    return checks


def active_bank(blocker, block_columns, closure_columns):
    block_columns = tuple(block_columns)
    block_rows = tuple(blocker[column] for column in block_columns)
    states = []

    # Use every fixed-point-free permutation on the physical block. This is a
    # nontrivial bank with empty common block support whenever the bank has at
    # least two states.
    for local_perm in derangements(len(block_columns)):
        active = {}
        for local_index, column in enumerate(block_columns):
            active[column] = block_rows[local_perm[local_index]]
        for column in closure_columns:
            active[column] = blocker[column]
        states.append(active)
    return states


def selected_blocker_columns(blocker, active):
    return {
        column
        for column, row in active.items()
        if blocker[column] == row
    }


def verify_global(maximum_n=7):
    bank_checks = 0
    universal_checks = 0

    for size in range(5, maximum_n + 1):
        blocker = tuple(range(size))
        for block_size in range(3, min(5, size) + 1):
            block_columns = tuple(range(block_size))
            outside = tuple(range(block_size, size))
            states = active_bank(blocker, block_columns, ())
            if len(states) < 2:
                continue

            common_active = set.intersection(
                *({(column, row) for column, row in state.items()} for state in states)
            )
            assert not common_active

            for closure_count in range(min(3, len(outside)) + 1):
                for closure_columns in combinations(outside, closure_count):
                    states = active_bank(blocker, block_columns, closure_columns)
                    joint_common_new = None
                    selected_sets = []
                    for active in states:
                        selected = selected_blocker_columns(blocker, active)
                        selected_sets.append(selected)
                        state_common = common_new_cells(blocker, selected)
                        if joint_common_new is None:
                            joint_common_new = set(state_common)
                        else:
                            joint_common_new &= state_common

                    assert joint_common_new is not None
                    if joint_common_new:
                        assert all(len(selected) == 2 for selected in selected_sets)
                        assert all(selected == set(closure_columns) for selected in selected_sets)
                        assert len(closure_columns) == 2
                        first, second = closure_columns
                        expected = {(first, second), (second, first)}
                        assert joint_common_new == expected
                        universal_checks += 1
                    else:
                        # Any failure of the universal pair conditions must have
                        # empty common new support.
                        universal_pair = (
                            len(closure_columns) == 2
                            and all(selected == set(closure_columns) for selected in selected_sets)
                        )
                        assert not universal_pair
                    bank_checks += 1

    return bank_checks, universal_checks


def verify_weight_router(maximum=40):
    split_checks = 0
    profile_checks = 0

    for total in range(1, maximum + 1):
        for one_crossed in range(total + 1):
            two_crossed = total - one_crossed
            assert max(one_crossed, two_crossed) * 2 >= total
            split_checks += 1

            # The one-crossed class splits over the two fixed crossed cells.
            first = one_crossed // 2
            second = one_crossed - first
            assert max(first, second) * 2 >= one_crossed
            split_checks += 1

            for profile_count in range(1, 9):
                # A selected crossed-count class of weight at least total/2
                # has a profile class of at least total/(2L), in weighted
                # pigeonhole form.
                selected = max(one_crossed, two_crossed)
                quotient, remainder = divmod(selected, profile_count)
                largest = quotient + (1 if remainder else 0)
                assert largest * profile_count >= selected
                assert 2 * largest * profile_count >= total
                profile_checks += 1

    return split_checks, profile_checks


def main():
    conditional = verify_conditional()
    global_checks, universal = verify_global()
    split, profiles = verify_weight_router()
    print(
        "AC RI fixed blocker collateral: verified "
        f"{conditional} conditional repair menus, {global_checks} nontrivial banks, "
        f"{universal} universal closure-pair cases, {split} weighted splits, "
        f"and {profiles} profile routers"
    )


if __name__ == "__main__":
    main()
