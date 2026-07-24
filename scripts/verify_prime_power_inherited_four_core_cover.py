#!/usr/bin/env python3
"""Exact finite checks for CMR181--CMR185."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


def derangements_four() -> list[tuple[int, ...]]:
    return [
        state
        for state in permutations(range(4))
        if all(state[row] != row for row in range(4))
    ]


def cylinder_events(states):
    events = []
    for rank in (1, 2, 3):
        for rows in combinations(range(4), rank):
            for columns in permutations(range(4), rank):
                mask = 0
                for index, state in enumerate(states):
                    if all(
                        state[row] == column
                        for row, column in zip(rows, columns)
                    ):
                        mask |= 1 << index
                if mask:
                    events.append((mask, rank, tuple(zip(rows, columns))))
    return events


def verify_cylinder_sizes(states, events) -> None:
    histogram = Counter((rank, mask.bit_count()) for mask, rank, _ in events)
    assert histogram == Counter(
        {
            (1, 3): 12,
            (2, 2): 12,
            (2, 1): 9,
            (3, 1): 36,
        }
    )
    # Rank-three prescriptions repeat the same nine singleton state cylinders.
    rank_three_masks = {mask for mask, rank, _ in events if rank == 3}
    assert len(rank_three_masks) == 9


def verify_minimum_covers(states, events) -> None:
    full = (1 << len(states)) - 1
    rank_one = [(mask, prescription) for mask, rank, prescription in events if rank == 1]

    assert all(mask != full for mask, _, _ in events)
    assert not any(
        first[0] | second[0] == full
        for first, second in combinations(events, 2)
    )

    covers = []
    for selected in combinations(rank_one, 3):
        mask = selected[0][0] | selected[1][0] | selected[2][0]
        if mask == full:
            covers.append(tuple(item[1][0] for item in selected))

    expected = {
        ((0, 1), (0, 2), (0, 3)),
        ((1, 0), (1, 2), (1, 3)),
        ((2, 0), (2, 1), (2, 3)),
        ((3, 0), (3, 1), (3, 2)),
        ((1, 0), (2, 0), (3, 0)),
        ((0, 1), (2, 1), (3, 1)),
        ((0, 2), (1, 2), (3, 2)),
        ((0, 3), (1, 3), (2, 3)),
    }
    assert {tuple(sorted(cover)) for cover in covers} == {
        tuple(sorted(cover)) for cover in expected
    }


def pareto_frontier(states, events):
    full = (1 << len(states)) - 1
    # Deduplicate identical cylinders at the same rank.
    unique_events = sorted({(mask, rank) for mask, rank, _ in events})
    profiles = [set() for _ in range(full + 1)]
    profiles[0].add((0, 0, 0))

    changed = True
    while changed:
        changed = False
        for covered in range(full + 1):
            for profile in list(profiles[covered]):
                for event_mask, rank in unique_events:
                    new_covered = covered | event_mask
                    new_profile = list(profile)
                    new_profile[rank - 1] += 1
                    new_profile = tuple(new_profile)

                    if any(
                        all(old[index] <= new_profile[index] for index in range(3))
                        for old in profiles[new_covered]
                    ):
                        continue

                    dominated = {
                        old
                        for old in profiles[new_covered]
                        if all(new_profile[index] <= old[index] for index in range(3))
                    }
                    profiles[new_covered].difference_update(dominated)
                    profiles[new_covered].add(new_profile)
                    changed = True

    return profiles[full]


def verify_pareto(states, events) -> None:
    expected = {
        (3, 0, 0),
        (2, 1, 1),
        (2, 2, 0),
        (2, 0, 3),
        (1, 2, 2),
        (1, 3, 1),
        (1, 4, 0),
        (1, 1, 4),
        (1, 0, 6),
        (0, 3, 3),
        (0, 4, 2),
        (0, 5, 1),
        (0, 6, 0),
        (0, 2, 5),
        (0, 1, 7),
        (0, 0, 9),
    }
    assert pareto_frontier(states, events) == expected
    for first, second, third in expected:
        assert 3 * first + 2 * second + third >= 9


def main() -> None:
    states = derangements_four()
    assert len(states) == 9
    events = cylinder_events(states)

    verify_cylinder_sizes(states, events)
    verify_minimum_covers(states, events)
    verify_pareto(states, events)

    print(
        "verified inherited four-core cover: nine derangements, atoms 1/3,2/9,1/9, "
        "eight minimum row/column covers, and 16 Pareto profiles"
    )


if __name__ == "__main__":
    main()
