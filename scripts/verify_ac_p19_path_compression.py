#!/usr/bin/env python3
from __future__ import annotations

from collections import deque
from pathlib import Path
import json

import verify_ac_explicit_p19_zero_certificate as base

N = base.N


def raw_path() -> tuple[list[base.State], list[int]]:
    seed = json.loads(Path("data/ac-explicit-p19-an-seed.json").read_text())
    trajectory = json.loads(Path("data/ac-p19-switch-trajectory.json").read_text())
    certificate = json.loads(Path("data/ac-p19-zero-certificate.json").read_text())
    moves = (
        trajectory["monotone_moves"]
        + trajectory["barrier_moves"]
        + certificate["checkpoint_5_to_4"]["path"]
        + certificate["checkpoint_4_to_2"]["path"]
        + certificate["checkpoint_2_to_1"]["path"]
        + certificate["checkpoint_1_to_0"]["path"]
    )
    state = base.installed_seed(seed)
    states = [state]
    potentials = [base.potential(state)]
    for move in moves:
        state, current = base.move_with_potential(state, potentials[-1], move)
        states.append(state)
        potentials.append(current)
    assert potentials[-1] == 0
    return states, potentials


def transform_point(x: int, y: int, action: int) -> tuple[int, int]:
    if action == 0:
        return x, y
    if action == 1:
        return N + 1 - x, y
    if action == 2:
        return x, N + 1 - y
    if action == 3:
        return N + 1 - x, N + 1 - y
    if action == 4:
        return y, x
    if action == 5:
        return N + 1 - y, N + 1 - x
    if action == 6:
        return y, N + 1 - x
    if action == 7:
        return N + 1 - y, x
    raise ValueError(action)


def transform_layer(layer: tuple[int, ...], action: int) -> tuple[int, ...]:
    transformed = [0] * N
    for x, y in enumerate(layer, 1):
        new_x, new_y = transform_point(x, y, action)
        transformed[new_x - 1] = new_y
    assert set(transformed) == set(range(1, N + 1))
    return tuple(transformed)


def transform_state(state: base.State, action: int, swap_layers: bool) -> base.State:
    red = transform_layer(state[0], action)
    blue = transform_layer(state[1], action)
    return (blue, red) if swap_layers else (red, blue)


def canonical_orbit(state: base.State) -> base.State:
    return min(
        transform_state(state, action, swap)
        for action in range(8)
        for swap in (False, True)
    )


def derive_move(first: base.State, second: base.State) -> str:
    for layer_index, layer_name in enumerate(("r", "b")):
        other = 1 - layer_index
        changed = [
            row
            for row, (old, new) in enumerate(zip(first[layer_index], second[layer_index]))
            if old != new
        ]
        if len(changed) != 2 or first[other] != second[other]:
            continue
        row_a, row_b = changed
        if (
            first[layer_index][row_a] == second[layer_index][row_b]
            and first[layer_index][row_b] == second[layer_index][row_a]
        ):
            return f"{layer_name}:{row_a + 1},{row_b + 1}"
    raise AssertionError("states are not joined by one two-row switch")


def main() -> None:
    record = json.loads(Path("data/ac-p19-path-compression.json").read_text())
    states, potentials = raw_path()
    assert len(states) == record["raw_state_occurrences"] == 390
    assert len(states) - 1 == record["raw_switch_moves"] == 389

    first_occurrence: dict[base.State, int] = {}
    repeats: list[tuple[int, int]] = []
    unique_states: list[base.State] = []
    for index, state in enumerate(states):
        if state in first_occurrence:
            repeats.append((first_occurrence[state], index))
        else:
            first_occurrence[state] = index
            unique_states.append(state)
    assert len(unique_states) == record["distinct_exact_states"] == 389
    assert repeats == [
        (
            record["only_repeated_state"]["first_index"],
            record["only_repeated_state"]["second_index"],
        )
    ]

    orbit_representatives = {canonical_orbit(state) for state in unique_states}
    assert len(orbit_representatives) == record["dihedral_layer_orbits"] == 389

    vertex = {state: index for index, state in enumerate(unique_states)}
    adjacency: list[list[int]] = [[] for _ in unique_states]
    for index, state in enumerate(unique_states):
        current = base.potential(state)
        for successor, _ in base.legal_neighbors(state, current, 10**9):
            target = vertex.get(successor)
            if target is not None:
                adjacency[index].append(target)

    start = vertex[states[0]]
    terminal = vertex[states[-1]]
    queue = deque([start])
    predecessor: dict[int, int | None] = {start: None}
    while queue:
        current = queue.popleft()
        if current == terminal:
            break
        for successor in adjacency[current]:
            if successor in predecessor:
                continue
            predecessor[successor] = current
            queue.append(successor)
    assert terminal in predecessor

    shortest_vertices: list[int] = []
    current: int | None = terminal
    while current is not None:
        shortest_vertices.append(current)
        current = predecessor[current]
    shortest_vertices.reverse()
    shortest_states = [unique_states[index] for index in shortest_vertices]
    assert len(shortest_states) - 1 == record["induced_shortest_switch_moves"] == 357
    assert record["saved_switch_moves"] == 32

    raw_index: dict[base.State, int] = {}
    for index, state in enumerate(states):
        raw_index.setdefault(state, index)
    shortcuts = []
    for first, second in zip(shortest_states, shortest_states[1:]):
        left, right = raw_index[first], raw_index[second]
        move = derive_move(first, second)
        successor = base.apply_move(first, move)
        assert successor == second
        if right != left + 1:
            shortcuts.append({"from_index": left, "to_index": right, "move": move})
    assert shortcuts == record["shortcut_edges"]

    compressed_potentials = [base.potential(state) for state in shortest_states]
    assert max(compressed_potentials) == record["compressed_maximum_potential"] == 41
    assert compressed_potentials[-1] == record["compressed_final_potential"] == 0

    print("AC p=19 path-compression audit")
    print(f"raw_state_occurrences: {len(states)}")
    print(f"distinct_exact_states: {len(unique_states)}")
    print(f"dihedral_layer_orbits: {len(orbit_representatives)}")
    print(f"shortcut_edges: {len(shortcuts)}")
    print(f"raw_switch_moves: {len(states) - 1}")
    print(f"compressed_switch_moves: {len(shortest_states) - 1}")
    print(f"saved_switch_moves: {record['saved_switch_moves']}")
    print(f"compressed_maximum_potential: {max(compressed_potentials)}")
    print(f"compressed_final_potential: {compressed_potentials[-1]}")


if __name__ == "__main__":
    main()
