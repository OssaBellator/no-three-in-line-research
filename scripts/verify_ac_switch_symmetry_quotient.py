#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from itertools import combinations, permutations


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def potential(state):
    red, blue = state
    points = [(i, red[i]) for i in range(len(red))] + [(i, blue[i]) for i in range(len(blue))]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def coordinate_transform(action, x, y, n):
    maximum = n - 1
    return (
        (x, y),
        (y, maximum - x),
        (maximum - x, maximum - y),
        (maximum - y, x),
        (maximum - x, y),
        (x, maximum - y),
        (y, x),
        (maximum - y, maximum - x),
    )[action]


def transform(state, action, swap_layers=False):
    n = len(state[0])
    output = [[None] * n, [None] * n]
    for layer, permutation in enumerate(state):
        target_layer = 1 - layer if swap_layers else layer
        for x, y in enumerate(permutation):
            new_x, new_y = coordinate_transform(action, x, y, n)
            output[target_layer][new_x] = new_y
    return tuple(tuple(layer) for layer in output)


def orbit(state):
    return {
        transform(state, action, swap)
        for action in range(8)
        for swap in (False, True)
    }


def canonical(state):
    return min(orbit(state))


def legal_neighbors(state):
    red, blue = state
    n = len(red)
    for layer in range(2):
        current = list(state[layer])
        opposite = state[1 - layer]
        for first, second in combinations(range(n), 2):
            if current[second] == opposite[first] or current[first] == opposite[second]:
                continue
            successor = current[:]
            successor[first], successor[second] = successor[second], successor[first]
            yield (tuple(successor), opposite) if layer == 0 else (opposite, tuple(successor))


def adjacent(first, second):
    for layer in range(2):
        if first[1 - layer] != second[1 - layer]:
            continue
        differences = [
            index
            for index, (left, right) in enumerate(zip(first[layer], second[layer]))
            if left != right
        ]
        if len(differences) == 2:
            i, j = differences
            if first[layer][i] == second[layer][j] and first[layer][j] == second[layer][i]:
                return True
    return False


def component(start, barrier, quotient=False):
    key = canonical if quotient else (lambda state: state)
    initial = key(start)
    seen = {initial}
    queue = deque([initial])
    while queue:
        state = queue.popleft()
        for successor in legal_neighbors(state):
            if potential(successor) > barrier:
                continue
            successor = key(successor)
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return seen


def main():
    n = 5
    all_permutations = list(permutations(range(n)))
    states = [
        (red, blue)
        for red in all_permutations
        for blue in all_permutations
        if all(left != right for left, right in zip(red, blue))
    ]
    assert len(states) == 5280

    orbit_images = 0
    canonical_checks = 0
    for state in states:
        state_potential = potential(state)
        representative = canonical(state)
        assert canonical(representative) == representative
        canonical_checks += 1
        images = orbit(state)
        assert 1 <= len(images) <= 16
        for image in images:
            assert potential(image) == state_potential
            assert all(sorted(layer) == list(range(n)) for layer in image)
            assert all(left != right for left, right in zip(*image))
            orbit_images += 1

    transformed_edge_checks = 0
    for state in states[::26]:
        for successor in legal_neighbors(state):
            assert adjacent(state, successor)
            for action in range(8):
                for swap in (False, True):
                    assert adjacent(
                        transform(state, action, swap),
                        transform(successor, action, swap),
                    )
                    transformed_edge_checks += 1

    starts = [states[0], states[137], states[1024], states[-1]]
    reachability_checks = 0
    raw_component_total = 0
    quotient_component_total = 0
    for start in starts:
        initial_potential = potential(start)
        for barrier in range(initial_potential, initial_potential + 4):
            raw = component(start, barrier, quotient=False)
            quotient = component(start, barrier, quotient=True)
            assert {canonical(state) for state in raw} == quotient
            raw_component_total += len(raw)
            quotient_component_total += len(quotient)
            reachability_checks += 1
            for target in range(initial_potential + 1):
                assert any(potential(state) < target for state in raw) == any(
                    potential(state) < target for state in quotient
                )

    print("AC switch symmetry quotient audit")
    print(f"n: {n}")
    print(f"ordered_disjoint_states: {len(states)}")
    print(f"canonical_checks: {canonical_checks}")
    print(f"orbit_images_checked: {orbit_images}")
    print(f"transformed_edge_checks: {transformed_edge_checks}")
    print(f"reachability_checks: {reachability_checks}")
    print(f"raw_component_state_sum: {raw_component_total}")
    print(f"quotient_component_state_sum: {quotient_component_total}")


if __name__ == "__main__":
    main()
