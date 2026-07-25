#!/usr/bin/env python3
"""Exhaust BDA5k--BDA5l on small occupancy/profile systems."""

from itertools import product


OCCUPANCY_TYPES = ((0, 0), (0, 2), (2, 0), (2, 2))


def verify(maximum_envelopes=6, maximum_profiles=3, maximum_cost=3):
    checked = 0
    for profile_count in range(1, maximum_profiles + 1):
        classes = [
            (occupancy, profile)
            for occupancy in OCCUPANCY_TYPES
            for profile in range(profile_count)
        ]
        for envelope_count in range(1, maximum_envelopes + 1):
            for class_choices in product(classes, repeat=envelope_count):
                # Exhaust a compact but nontrivial role-cost alphabet.
                for role_costs in product(
                    range(1, maximum_cost + 1), repeat=2 * envelope_count
                ):
                    left = role_costs[::2]
                    right = role_costs[1::2]
                    floor = [min(a, b) for a, b in zip(left, right)]
                    total_floor = sum(floor)

                    class_floor = {}
                    class_left = {}
                    class_right = {}
                    for index, key in enumerate(class_choices):
                        class_floor[key] = class_floor.get(key, 0) + floor[index]
                        class_left[key] = class_left.get(key, 0) + left[index]
                        class_right[key] = class_right.get(key, 0) + right[index]

                    selected = max(class_floor, key=class_floor.get)
                    lower_bound = total_floor / (4 * profile_count)
                    assert class_floor[selected] >= lower_bound
                    assert class_left[selected] >= class_floor[selected]
                    assert class_right[selected] >= class_floor[selected]
                    checked += 1
    return checked


def main():
    checked = verify(maximum_envelopes=4, maximum_profiles=2, maximum_cost=2)
    print(f"BDA balanced-floor localization: verified {checked} systems")


if __name__ == "__main__":
    main()
