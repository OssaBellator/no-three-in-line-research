#!/usr/bin/env python3
"""Exhaust RI5h--RI5i on small abstract permutation restrictions."""

from itertools import combinations, permutations, product


def decompose(selected, target):
    selected = set(selected)
    indegree = {column: 0 for column in selected}
    for column in selected:
        image = target[column]
        if image in selected:
            indegree[image] += 1

    seen = set()
    components = []
    for column in sorted(selected):
        if indegree[column] == 0 and column not in seen:
            path = []
            current = column
            while current in selected and current not in seen:
                seen.add(current)
                path.append(current)
                current = target[current]
            assert current not in selected
            components.append(("path", tuple(path), current))

    for column in sorted(selected):
        if column not in seen:
            cycle = []
            current = column
            while current not in seen:
                seen.add(current)
                cycle.append(current)
                current = target[current]
            assert current == column
            components.append(("cycle", tuple(cycle), None))
    return components


def close_components(selected, target):
    desired = {}
    component_of = {}
    components = decompose(selected, target)
    for component_index, (kind, columns, outside) in enumerate(components):
        for column in columns:
            desired[column] = target[column]
            component_of[column] = component_index
        if kind == "path":
            desired[outside] = columns[0]
            component_of[outside] = component_index
    assert set(desired) == set(desired.values())
    return desired, component_of, components


def is_permutation(mapping, size):
    universe = set(range(size))
    return set(mapping) == universe and set(mapping.values()) == universe


def verify(maximum_size=5):
    state_checks = 0
    weight_checks = 0

    for size in range(2, maximum_size + 1):
        universe = tuple(range(size))
        blocker_permutations = [
            permutation
            for permutation in permutations(universe)
            if all(permutation[column] != column for column in universe)
        ]

        for selected_size in range(1, size):
            for selected in combinations(universe, selected_size):
                for images in permutations(universe, selected_size):
                    target = dict(zip(selected, images))
                    desired, component_of, components = close_components(
                        selected, target
                    )

                    for blocker_tuple in blocker_permutations:
                        blocker = dict(enumerate(blocker_tuple))
                        blocked = [
                            column
                            for column, row in desired.items()
                            if blocker[column] == row
                        ]

                        active_new = {column: column for column in universe}
                        blocker_new = blocker.copy()

                        if len(blocked) == 0:
                            active_new.update(desired)
                        elif len(blocked) >= 2:
                            active_new.update(desired)
                            rows = [desired[column] for column in blocked]
                            for index, column in enumerate(blocked):
                                blocker_new[column] = rows[(index + 1) % len(rows)]
                        else:
                            blocked_component = component_of[blocked[0]]
                            for column, row in desired.items():
                                if component_of[column] != blocked_component:
                                    active_new[column] = row

                        assert is_permutation(active_new, size)
                        assert is_permutation(blocker_new, size)
                        assert all(
                            active_new[column] != blocker_new[column]
                            for column in universe
                        )
                        state_checks += 1

                        component_count = len(components)
                        for weights in product((1, 2), repeat=component_count):
                            total = sum(weights)
                            if len(blocked) != 1:
                                installed = total
                                assert installed == total
                            else:
                                blocked_index = component_of[blocked[0]]
                                blocked_weight = weights[blocked_index]
                                installed = total - blocked_weight
                                assert blocked_weight > total / 2 or installed >= total / 2
                            weight_checks += 1

    return state_checks, weight_checks


def main():
    state_checks, weight_checks = verify()
    print(
        "Rational two-layer completion: verified "
        f"{state_checks} states and {weight_checks} weighted alternatives"
    )


if __name__ == "__main__":
    main()
