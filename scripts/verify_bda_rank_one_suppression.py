#!/usr/bin/env python3
"""Exhaust the abstract BDA5h--BDA5i rank-one suppression identities."""

from itertools import product


def verify_floor_identity(maximum_envelopes=5, maximum_cost=3):
    checked = 0
    for envelope_count in range(1, maximum_envelopes + 1):
        for costs in product(
            range(maximum_cost + 1), repeat=2 * envelope_count
        ):
            left_costs = costs[::2]
            right_costs = costs[1::2]
            uniform_rank_one = sum(
                (left + right) / 2
                for left, right in zip(left_costs, right_costs)
            )
            floor = sum(
                min(left, right)
                for left, right in zip(left_costs, right_costs)
            )
            imbalance = sum(
                abs(left - right)
                for left, right in zip(left_costs, right_costs)
            )
            assert uniform_rank_one == floor + imbalance / 2

            cheaper_assignment = [
                0 if left <= right else 1
                for left, right in zip(left_costs, right_costs)
            ]
            chosen_cost = sum(
                (left_costs[index], right_costs[index])[choice]
                for index, choice in enumerate(cheaper_assignment)
            )
            assert chosen_cost == floor
            checked += 1
    return checked


def verify_event_factors(maximum_rank=3):
    checked = 0
    for rank in range(1, maximum_rank + 1):
        assignments = list(product((0, 1), repeat=rank))
        for event_mask in range(1, 1 << len(assignments)):
            event = {
                assignments[index]
                for index in range(len(assignments))
                if event_mask & (1 << index)
            }
            uniform_probability = len(event) / (2**rank)
            for assignment in assignments:
                indicator = int(assignment in event)
                assert indicator <= (2**rank) * uniform_probability
                checked += 1
    return checked


def main():
    floor_cases = verify_floor_identity()
    event_cases = verify_event_factors()
    print(
        "BDA rank-one suppression: verified "
        f"{floor_cases} menu systems and {event_cases} event checks"
    )


if __name__ == "__main__":
    main()
