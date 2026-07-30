#!/usr/bin/env python3
from __future__ import annotations

from collections import deque
from itertools import combinations
from math import comb, gcd
from pathlib import Path
import json

P = 19
N = P - 1


def point_id(point: tuple[int, int]) -> int:
    x, y = point
    return (x - 1) * N + (y - 1)


def primitive(dx: int, dy: int) -> tuple[int, int]:
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def build_line_masks() -> tuple[list[int], list[list[int]]]:
    points = [(x, y) for x in range(1, N + 1) for y in range(1, N + 1)]
    line_cells: dict[tuple[int, int, int], set[tuple[int, int]]] = {}
    for first, second in combinations(points, 2):
        dx, dy = primitive(second[0] - first[0], second[1] - first[1])
        intercept = dy * first[0] - dx * first[1]
        line_cells.setdefault((dx, dy, intercept), set()).update((first, second))

    masks: list[int] = []
    cell_lines: list[list[int]] = [[] for _ in range(N * N)]
    for cells in line_cells.values():
        if len(cells) < 3:
            continue
        line_id = len(masks)
        mask = 0
        for point in cells:
            identifier = point_id(point)
            mask |= 1 << identifier
            cell_lines[identifier].append(line_id)
        masks.append(mask)
    return masks, cell_lines


LINE_MASKS, CELL_LINES = build_line_masks()
State = tuple[tuple[int, ...], tuple[int, ...]]


def state_mask(state: State) -> int:
    mask = 0
    for layer in state:
        for x, y in enumerate(layer, 1):
            mask |= 1 << point_id((x, y))
    return mask


def potential(state: State) -> int:
    mask = state_mask(state)
    return sum(comb((mask & line).bit_count(), 3) for line in LINE_MASKS)


def parse_move(move: str) -> tuple[str, int, int]:
    layer, rows = move.split(":", 1)
    first, second = (int(value) - 1 for value in rows.split(","))
    if layer not in {"r", "b"} or not (0 <= first < second < N):
        raise ValueError(f"malformed move: {move}")
    return layer, first, second


def apply_move(state: State, move: str) -> State:
    layer, first, second = parse_move(move)
    red, blue = map(list, state)
    active = red if layer == "r" else blue
    opposite = blue if layer == "r" else red
    y_first, y_second = active[first], active[second]
    if y_second == opposite[first] or y_first == opposite[second]:
        raise AssertionError(f"opposite-layer collision on {move}")
    active[first], active[second] = y_second, y_first
    successor = (tuple(red), tuple(blue))
    assert set(successor[0]) == set(range(1, N + 1))
    assert set(successor[1]) == set(range(1, N + 1))
    assert all(successor[0][row] != successor[1][row] for row in range(N))
    return successor


def move_with_potential(
    state: State, old_potential: int, move: str, *, verify_full: bool = False
) -> tuple[State, int]:
    successor = apply_move(state, move)
    old_mask = state_mask(state)
    new_mask = state_mask(successor)
    changed = old_mask ^ new_mask
    changed_cells: list[int] = []
    while changed:
        bit = changed & -changed
        changed_cells.append(bit.bit_length() - 1)
        changed -= bit

    affected_lines: set[int] = set()
    for cell in changed_cells:
        affected_lines.update(CELL_LINES[cell])

    delta = 0
    for line_id in affected_lines:
        line = LINE_MASKS[line_id]
        delta += comb((new_mask & line).bit_count(), 3)
        delta -= comb((old_mask & line).bit_count(), 3)
    new_potential = old_potential + delta
    if verify_full:
        assert new_potential == potential(successor)
    return successor, new_potential


def replay(
    state: State,
    start_potential: int,
    moves: list[str],
    expected_potentials: list[int],
) -> tuple[State, int]:
    assert len(expected_potentials) == len(moves) + 1
    assert expected_potentials[0] == start_potential
    current = start_potential
    for move, expected in zip(moves, expected_potentials[1:]):
        state, current = move_with_potential(
            state, current, move, verify_full=True
        )
        assert current == expected, (move, current, expected)
    return state, current


def legal_neighbors(state: State, old_potential: int, barrier: int):
    red, blue = state
    for layer in ("r", "b"):
        active = red if layer == "r" else blue
        opposite = blue if layer == "r" else red
        for first, second in combinations(range(N), 2):
            if active[second] == opposite[first] or active[first] == opposite[second]:
                continue
            move = f"{layer}:{first + 1},{second + 1}"
            successor, new_potential = move_with_potential(state, old_potential, move)
            if new_potential <= barrier:
                yield successor, new_potential


def sublevel_component(start: State, start_potential: int, barrier: int) -> tuple[int, int]:
    queue = deque([(start, start_potential)])
    seen = {start}
    minimum = start_potential
    while queue:
        state, current = queue.popleft()
        minimum = min(minimum, current)
        for successor, new_potential in legal_neighbors(state, current, barrier):
            if successor in seen:
                continue
            seen.add(successor)
            queue.append((successor, new_potential))
    return len(seen), minimum


def hyperbola(channel: int) -> tuple[int, ...]:
    return tuple(channel * pow(x, -1, P) % P for x in range(1, P))


def installed_seed(seed: dict) -> State:
    red = list(hyperbola(seed["layers"]["anchor_channel"]))
    blue = list(hyperbola(seed["layers"]["switch_channel"]))
    for x, y in seed["switch"]["inserted"]:
        blue[x - 1] = y
    for x, y in seed["best_replacement_cells"]:
        red[x - 1] = y
    state = (tuple(red), tuple(blue))
    assert potential(state) == seed["best_potential"] == 41
    return state


def pairs_to_layer(pairs: list[list[int]]) -> tuple[int, ...]:
    ordered = sorted((int(x), int(y)) for x, y in pairs)
    assert [x for x, _ in ordered] == list(range(1, N + 1))
    return tuple(y for _, y in ordered)


def main() -> None:
    seed = json.loads(Path("data/ac-explicit-p19-an-seed.json").read_text())
    trajectory = json.loads(Path("data/ac-p19-switch-trajectory.json").read_text())
    certificate = json.loads(Path("data/ac-p19-zero-certificate.json").read_text())

    assert seed["p"] == certificate["p"] == P
    assert seed["n"] == certificate["n"] == N
    assert len(LINE_MASKS) == 4398

    state = installed_seed(seed)
    current = 41
    state, current = replay(
        state,
        current,
        trajectory["monotone_moves"],
        trajectory["monotone_potentials"],
    )
    assert current == trajectory["local_minimum"]["potential"] == 10
    assert state[0] == pairs_to_layer(trajectory["local_minimum"]["red"])
    assert state[1] == pairs_to_layer(trajectory["local_minimum"]["blue"])

    state, current = replay(
        state,
        current,
        trajectory["barrier_moves"],
        trajectory["barrier_potentials"],
    )
    assert current == trajectory["final"]["potential"] == 5
    assert state[0] == pairs_to_layer(trajectory["final"]["red"])
    assert state[1] == pairs_to_layer(trajectory["final"]["blue"])

    checkpoint_5 = state
    size, minimum = sublevel_component(checkpoint_5, current, 6)
    assert (size, minimum) == (5, 5)

    first = certificate["checkpoint_5_to_4"]
    state, current = replay(state, current, first["path"], first["potentials"])
    assert current == 4
    assert first["lower_barrier_exhaustion"] == {
        "barrier": 6,
        "component_states": 5,
    }

    checkpoint_4 = state
    size, minimum = sublevel_component(checkpoint_4, current, 5)
    assert (size, minimum) == (16, 4)

    second = certificate["checkpoint_4_to_2"]
    state, current = replay(state, current, second["path"], second["potentials"])
    assert current == 2
    assert second["lower_barrier_exhaustion"] == {
        "barrier": 5,
        "component_states": 16,
    }

    checkpoint_2 = state
    size, minimum = sublevel_component(checkpoint_2, current, 5)
    assert (size, minimum) == (181, 2)

    third = certificate["checkpoint_2_to_1"]
    state, current = replay(state, current, third["path"], third["potentials"])
    assert current == 1
    assert third["lower_barrier_exhaustion"] == {
        "barrier": 5,
        "component_states": 181,
    }

    checkpoint_1 = state
    expected_components = {2: 2, 3: 5, 4: 56}
    for barrier, expected_size in expected_components.items():
        size, minimum = sublevel_component(checkpoint_1, current, barrier)
        assert (size, minimum) == (expected_size, 1)

    final = certificate["checkpoint_1_to_0"]
    state, current = replay(state, current, final["path"], final["potentials"])
    expected_final = (
        pairs_to_layer(certificate["final_red"]),
        pairs_to_layer(certificate["final_blue"]),
    )
    assert state == expected_final
    assert current == certificate["final_potential"] == 0
    assert state_mask(state).bit_count() == 36
    assert all(state[0][row] != state[1][row] for row in range(N))

    summary = certificate["switch_path_summary"]
    assert len(trajectory["monotone_moves"]) == summary["strict_41_to_10_moves"] == 11
    assert len(trajectory["barrier_moves"]) == summary["barrier_10_to_5_moves"] == 247
    assert (
        len(first["path"])
        + len(second["path"])
        + len(third["path"])
        + len(final["path"])
        == summary["new_5_to_0_moves"]
        == 131
    )
    assert 11 + 247 + 131 == summary["raw_post_an_switch_moves"] == 389
    assert summary["total_operations_including_an_install"] == 390

    print("AC explicit p=19 zero-certificate audit")
    print(f"board_lines_with_at_least_three_cells: {len(LINE_MASKS)}")
    print("an_install_potential: 41")
    print(f"post_install_switches: {summary['raw_post_an_switch_moves']}")
    print("barrier_5_to_lower: 7")
    print("barrier_4_to_lower: 6")
    print("barrier_2_to_lower: 6")
    print("barrier_1_to_zero: 5")
    print("lower_component_sizes: 5, 16, 181, 2, 5, 56")
    print(f"final_selected_cells: {state_mask(state).bit_count()}")
    print(f"final_triple_potential: {current}")


if __name__ == "__main__":
    main()
