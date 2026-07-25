#!/usr/bin/env python3
"""Exhaust RI5l--RI5n on small two-layer permutations."""

from itertools import combinations, permutations


def matching_cells(perm):
    return {(column, row) for column, row in enumerate(perm)}


def candidate_triples(n):
    """All three-cell partial matchings."""
    triples = []
    for columns in combinations(range(n), 3):
        for rows in combinations(range(n), 3):
            for assignment in permutations(rows):
                triples.append(
                    frozenset(zip(columns, assignment, strict=True))
                )
    return triples


def verify(maximum_size=5, triple_size=4):
    state_count = 0
    triple_count = 0

    for n in range(2, maximum_size + 1):
        triples = candidate_triples(n) if 3 <= n <= triple_size else []

        for active in permutations(range(n)):
            active_cells = matching_cells(active)

            for blocker in permutations(range(n)):
                blocker_cells = matching_cells(blocker)
                if active_cells & blocker_cells:
                    continue

                for target in permutations(range(n)):
                    target_cells = matching_cells(target)
                    blocked = target_cells & blocker_cells
                    if len(blocked) != 1:
                        continue

                    q = next(iter(blocked))
                    c0, r0 = q
                    bank_states = []
                    created_sets = []

                    for c1 in range(n):
                        if c1 == c0:
                            continue
                        r1 = blocker[c1]

                        new_blocker = list(blocker)
                        new_blocker[c0] = r1
                        new_blocker[c1] = r0
                        new_cells = matching_cells(new_blocker)

                        assert len(set(new_blocker)) == n
                        assert not (target_cells & new_cells)

                        created = new_cells - blocker_cells
                        assert created == {(c0, r1), (c1, r0)}

                        bank_states.append(new_cells)
                        created_sets.append(created)
                        state_count += 1

                    # Every newly inserted cell identifies one auxiliary state.
                    # This proves the cylinder cap for all ranks; exact
                    # rank-three candidates are additionally enumerated through
                    # size ``triple_size``.
                    seen = {}
                    for index, created in enumerate(created_sets):
                        for cell in created:
                            seen.setdefault(cell, []).append(index)
                    assert all(len(indices) == 1 for indices in seen.values())

                    for triple in triples:
                        if triple <= blocker_cells:
                            continue
                        occurrences = [
                            index
                            for index, state in enumerate(bank_states)
                            if triple <= state
                            and bool(triple & created_sets[index])
                        ]
                        assert len(occurrences) <= 1
                        triple_count += 1

    return state_count, triple_count


def main():
    states, triples = verify()
    print(
        "RI singleton auxiliary transposition: verified "
        f"{states} states and {triples} exact triple tests"
    )


if __name__ == "__main__":
    main()
