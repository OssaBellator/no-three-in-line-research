#!/usr/bin/env python3
"""Finite checks for CMR982--CMR989."""

from math import comb
import random


def minimum_face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def physical_cells(state):
    return {cell for _layer, cell in state}


def random_joint_state(cell_count, cardinality, rng):
    cells = rng.sample(range(cell_count), cardinality)
    return frozenset((rng.randint(0, 1), cell) for cell in cells)


def random_joint_family(cell_count, cardinality, maximum, rng):
    state_count = comb(cell_count, cardinality) * (2 ** cardinality)
    target = rng.randint(1, min(maximum, state_count))
    family = set()
    while len(family) < target:
        family.add(random_joint_state(cell_count, cardinality, rng))
    return family


def cell_cut(family, cell):
    labels = {(0, cell), (1, cell)}
    return {state for state in family if set(state).isdisjoint(labels)}


def check_target_variability_and_cut():
    rng = random.Random(983)
    checked = 0
    for cell_count in range(3, 80):
        for cardinality in range(3, min(cell_count, 15) + 1):
            for _ in range(80):
                family = random_joint_family(cell_count, cardinality, 100, rng)
                potential = {state: rng.randint(0, 20) for state in family}
                face, value = minimum_face(family, potential)
                selected = rng.choice(tuple(face))
                target = frozenset(rng.sample(tuple(physical_cells(selected)), 3))
                alternatives = [
                    state for state in face if not set(target) <= physical_cells(state)
                ]
                if not alternatives:
                    assert all(set(target) <= physical_cells(state) for state in face)
                    checked += 1
                    continue
                alternative = rng.choice(alternatives)
                cell = min(set(target) - physical_cells(alternative))
                restricted = cell_cut(family, cell)
                restricted_face, restricted_value = minimum_face(restricted, potential)
                assert alternative in restricted
                assert restricted_value == value
                labels = {(0, cell), (1, cell)}
                assert restricted_face == {
                    state for state in face if set(state).isdisjoint(labels)
                }
                assert all(not set(target) <= physical_cells(state) for state in restricted)
                assert any(label in selected for label in labels)
                checked += 1
    return checked


def check_monotone_handoff_depth():
    rng = random.Random(984)
    checked = 0
    for labelled_universe in range(2, 500):
        for survivor_size in range(1, labelled_universe + 1):
            survivor = set(rng.sample(range(labelled_universe), survivor_size))
            deletable = list(set(range(labelled_universe)) - survivor)
            rng.shuffle(deletable)
            transitions = 0
            for edge in deletable:
                transitions += 1
                assert edge not in survivor
                assert transitions <= labelled_universe - survivor_size
            checked += 1
    return checked


def check_expansion_response():
    rng = random.Random(986)
    checked = 0
    for cell_count in range(3, 50):
        for cardinality in range(3, min(cell_count, 12) + 1):
            for _ in range(80):
                old_family = random_joint_family(cell_count, cardinality, 60, rng)
                potential = {state: rng.randint(0, 20) for state in old_family}
                old_face, old_value = minimum_face(old_family, potential)
                selected = rng.choice(tuple(old_face))
                target = frozenset(rng.sample(tuple(physical_cells(selected)), 3))

                expanded = set(old_family)
                for _new in range(rng.randint(1, 30)):
                    state = random_joint_state(cell_count, cardinality, rng)
                    expanded.add(state)
                    potential.setdefault(state, rng.randint(0, 20))
                expanded_face, expanded_value = minimum_face(expanded, potential)
                assert expanded_value <= old_value
                if expanded_value == old_value:
                    target_destroying = [
                        state
                        for state in expanded_face
                        if not set(target) <= physical_cells(state)
                    ]
                    if target_destroying:
                        alternative = rng.choice(target_destroying)
                        cell = min(set(target) - physical_cells(alternative))
                        restricted = cell_cut(expanded, cell)
                        _face, value = minimum_face(restricted, potential)
                        assert value == old_value
                    else:
                        assert all(
                            set(target) <= physical_cells(state)
                            for state in expanded_face
                        )
                checked += 1
    return checked


def check_label_assignments_and_conditioning():
    rng = random.Random(987)
    checked = 0
    for cell_count in range(3, 100):
        for _ in range(200):
            target = tuple(rng.sample(range(cell_count), 3))
            family = set()
            for _state in range(rng.randint(1, 100)):
                assignment = tuple(rng.randint(0, 1) for _ in range(3))
                target_edges = {
                    (assignment[index], cell) for index, cell in enumerate(target)
                }
                available = list(set(range(cell_count)) - set(target))
                extras = {
                    (rng.randint(0, 1), cell)
                    for cell in rng.sample(
                        available, rng.randint(0, min(10, len(available)))
                    )
                }
                family.add(frozenset(target_edges | extras))
            assignments = {}
            for state in family:
                assignment = tuple(
                    next(layer for layer, physical in state if physical == cell)
                    for cell in target
                )
                assignments.setdefault(assignment, set()).add(state)
            assert len(assignments) <= 8
            potential = {state: rng.randint(0, 20) for state in family}
            face, value = minimum_face(family, potential)
            selected = rng.choice(tuple(face))
            prescription = frozenset(
                next(edge for edge in selected if edge[1] == cell) for cell in target
            )
            conditioned = {
                state for state in family if set(prescription) <= set(state)
            }
            conditioned_face, conditioned_value = minimum_face(conditioned, potential)
            assert selected in conditioned_face
            assert conditioned_value == value
            residual = {
                frozenset(set(state) - set(prescription)) for state in conditioned
            }
            assert len(residual) == len(conditioned)
            checked += 1
    return checked


def check_recurrence_arithmetic():
    checked = 0
    for side in range(1, 500):
        for threshold in range(2, 50):
            maximum = (threshold - 1) * side * side
            assert maximum < threshold * side * side
            checked += 1
    return checked


def main():
    print(
        "verified minimum-face target handoff:",
        check_target_variability_and_cut(),
        "target cuts,",
        check_monotone_handoff_depth(),
        "monotone depths,",
        check_expansion_response(),
        "expansion responses,",
        check_label_assignments_and_conditioning(),
        "label conditions, and",
        check_recurrence_arithmetic(),
        "recurrence cases",
    )


if __name__ == "__main__":
    main()
