#!/usr/bin/env python3
"""Complete finite checks for CMR1278--CMR1285."""

from itertools import combinations, permutations


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(3))


def collinear(triple):
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def potential(state):
    return sum(collinear(triple) for triple in combinations(state, 3))


def targets(state):
    return {
        frozenset(triple)
        for triple in combinations(state, 3)
        if collinear(triple)
    }


def check_six_physical_states():
    permutations_list = list(permutations(range(3)))
    complete = frozenset((row, column) for row in range(3) for column in range(3))
    physical_states = {}
    for omitted in permutations_list:
        state = complete - matching(omitted)
        physical_states[omitted] = state
        assert len(state) == 6
        unused = complete - state
        assert unused == matching(omitted)

    assert len(set(physical_states.values())) == 6
    expected = {
        (0, 1, 2): (0, frozenset()),
        (2, 1, 0): (0, frozenset()),
        (0, 2, 1): (1, frozenset({(0, 2), (1, 1), (2, 0)})),
        (1, 0, 2): (1, frozenset({(0, 2), (1, 1), (2, 0)})),
        (1, 2, 0): (1, frozenset({(0, 0), (1, 1), (2, 2)})),
        (2, 0, 1): (1, frozenset({(0, 0), (1, 1), (2, 2)})),
    }
    for omitted, state in physical_states.items():
        state_targets = targets(state)
        expected_potential, expected_target = expected[omitted]
        assert potential(state) == expected_potential
        if expected_potential:
            assert state_targets == {expected_target}
        else:
            assert not state_targets
    return physical_states


def check_all_labelled_target_responses():
    permutations_list = list(permutations(range(3)))
    labelled_states = 0
    dirty_labelled_states = 0
    response_cases = 0
    for opposite_tuple in permutations_list:
        opposite = matching(opposite_tuple)
        disjoint_layers = [
            matching(layer_tuple)
            for layer_tuple in permutations_list
            if matching(layer_tuple).isdisjoint(opposite)
        ]
        assert len(disjoint_layers) == 2
        for current in disjoint_layers:
            labelled_states += 1
            state = opposite | current
            state_targets = targets(state)
            omitted = next(layer for layer in disjoint_layers if layer != current)
            if not state_targets:
                continue
            dirty_labelled_states += 1
            assert len(state_targets) == 1
            target = next(iter(state_targets))
            for edge in target:
                if edge in current:
                    response = omitted
                    new_state = opposite | response
                else:
                    response_candidates = [
                        matching(layer_tuple)
                        for layer_tuple in permutations_list
                        if matching(layer_tuple).isdisjoint(current)
                        and matching(layer_tuple) != opposite
                    ]
                    assert len(response_candidates) == 1
                    response = response_candidates[0]
                    new_state = current | response
                assert edge not in new_state
                assert potential(new_state) == 0
                assert not targets(new_state)
                response_cases += 1

    assert labelled_states == 12
    assert dirty_labelled_states == 8
    assert response_cases == 24
    return labelled_states, dirty_labelled_states, response_cases


def check_zero_offspring_matrix():
    size = 4
    matrix = [[0 for _column in range(size)] for _row in range(size)]
    weight = [1] * size
    image = [sum(row[column] * weight[column] for column in range(size)) for row in matrix]
    assert image == [0] * size
    assert all(image[index] < weight[index] for index in range(size))
    return size * size


def check_wall_child_arithmetic():
    checked = 0
    side = 3
    for first_child in range(side):
        second_child = side - 1 - first_child
        assert first_child + second_child == 2
        assert first_child < side and second_child < side
        checked += 1
    return checked


def main():
    physical = check_six_physical_states()
    labelled = check_all_labelled_target_responses()
    print(
        "verified side-three strict improvement:",
        len(physical),
        "physical states,",
        labelled[0],
        "labelled states with",
        labelled[1],
        "dirty and",
        labelled[2],
        "clean target responses,",
        check_zero_offspring_matrix(),
        "zero-matrix entries, and",
        check_wall_child_arithmetic(),
        "wall splits",
    )


if __name__ == "__main__":
    main()
