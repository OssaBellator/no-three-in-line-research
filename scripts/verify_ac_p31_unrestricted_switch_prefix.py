#!/usr/bin/env python3
from __future__ import annotations

from collections import deque
from itertools import combinations
from math import comb, gcd
from pathlib import Path
import json

N = 30


def primitive(dx, dy):
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def build_lines():
    points = [(x, y) for x in range(1, N + 1) for y in range(1, N + 1)]
    line_cells = {}
    for first, second in combinations(points, 2):
        dx, dy = primitive(second[0] - first[0], second[1] - first[1])
        intercept = dy * first[0] - dx * first[1]
        line_cells.setdefault((dx, dy, intercept), set()).update((first, second))
    masks = []
    cell_lines = [[] for _ in range(N * N)]
    for cells in line_cells.values():
        if len(cells) < 3:
            continue
        line_id = len(masks)
        mask = 0
        for x, y in cells:
            point_id = (x - 1) * N + (y - 1)
            mask |= 1 << point_id
            cell_lines[point_id].append(line_id)
        masks.append(mask)
    return masks, cell_lines


LINE_MASKS, CELL_LINES = build_lines()


def state_mask(state):
    mask = 0
    for layer in state:
        for x, y in enumerate(layer, 1):
            mask |= 1 << ((x - 1) * N + (y - 1))
    return mask


def potential_from_mask(mask):
    return sum(comb((mask & line).bit_count(), 3) for line in LINE_MASKS)


def parse_move(move):
    layer, rows = move.split(":", 1)
    first, second = (int(value) - 1 for value in rows.split(","))
    assert layer in {"r", "b"}
    assert 0 <= first < second < N
    return layer, first, second


def apply_move(state, old_mask, old_potential, move):
    layer, first, second = parse_move(move)
    red, blue = state
    layer_index = 0 if layer == "r" else 1
    active = red if layer_index == 0 else blue
    opposite = blue if layer_index == 0 else red
    assert active[second] != opposite[first]
    assert active[first] != opposite[second]

    old_cells = ((first + 1, active[first]), (second + 1, active[second]))
    new_cells = ((first + 1, active[second]), (second + 1, active[first]))
    new_mask = old_mask
    changed_ids = []
    for x, y in old_cells + new_cells:
        point_id = (x - 1) * N + (y - 1)
        new_mask ^= 1 << point_id
        changed_ids.append(point_id)

    affected_lines = set()
    for point_id in changed_ids:
        affected_lines.update(CELL_LINES[point_id])
    delta = sum(
        comb((new_mask & LINE_MASKS[line_id]).bit_count(), 3)
        - comb((old_mask & LINE_MASKS[line_id]).bit_count(), 3)
        for line_id in affected_lines
    )

    changed = list(active)
    changed[first], changed[second] = changed[second], changed[first]
    successor = (tuple(changed), blue) if layer_index == 0 else (red, tuple(changed))
    new_potential = old_potential + delta
    assert state_mask(successor) == new_mask
    return successor, new_mask, new_potential


def neighbors(state, mask, current_potential, barrier=None):
    red, blue = state
    for layer_index, layer_name in ((0, "r"), (1, "b")):
        active = red if layer_index == 0 else blue
        opposite = blue if layer_index == 0 else red
        for first, second in combinations(range(N), 2):
            if active[second] == opposite[first] or active[first] == opposite[second]:
                continue
            move = f"{layer_name}:{first + 1},{second + 1}"
            successor, successor_mask, successor_potential = apply_move(
                state, mask, current_potential, move
            )
            if barrier is not None and successor_potential > barrier:
                continue
            yield move, successor, successor_mask, successor_potential


def sublevel_component(start_state, start_mask, start_potential, barrier):
    queue = deque([(start_state, start_mask, start_potential)])
    seen = {start_state}
    minimum = start_potential
    while queue:
        state, mask, current = queue.popleft()
        minimum = min(minimum, current)
        for _, successor, successor_mask, successor_potential in neighbors(
            state, mask, current, barrier
        ):
            if successor in seen:
                continue
            seen.add(successor)
            queue.append((successor, successor_mask, successor_potential))
    return len(seen), minimum


def main():
    record = json.loads(Path("data/ac-p31-ratio23-switch-prefix.json").read_text())
    state = (tuple(record["initial_red"]), tuple(record["initial_blue"]))
    mask = state_mask(state)
    current = potential_from_mask(mask)
    assert current == record["initial_potential"] == 82
    assert len(LINE_MASKS) == 34270

    assert len(record["moves"]) == record["switch_moves"] == 92
    assert len(record["potentials"]) == len(record["moves"]) + 1
    assert record["potentials"][0] == current
    for move, expected in zip(record["moves"], record["potentials"][1:]):
        state, mask, current = apply_move(state, mask, current, move)
        assert current == expected
        assert potential_from_mask(mask) == current

    assert list(state[0]) == record["final_red"]
    assert list(state[1]) == record["final_blue"]
    assert current == record["final_potential"] == 10
    assert record["strict_initial_descent_moves"] == 11
    assert record["strict_initial_potentials"] == record["potentials"][:12]
    assert all(
        first > second
        for first, second in zip(
            record["strict_initial_potentials"],
            record["strict_initial_potentials"][1:],
        )
    )

    final_neighbors = list(neighbors(state, mask, current))
    assert len(final_neighbors) == record["final_legal_neighbors"] == 810
    assert sum(value < current for _, _, _, value in final_neighbors) == record[
        "final_improving_neighbors"
    ] == 0
    assert min(value for _, _, _, value in final_neighbors) == record[
        "final_best_neighbor_potential"
    ] == 11

    for expected in record["sublevel_components"]:
        size, minimum = sublevel_component(
            state, mask, current, expected["barrier"]
        )
        assert size == expected["states"]
        assert minimum == expected["minimum_potential"] == 10
    assert record["certified_lower_barrier_to_improvement"] == 13

    print("AC p=31 unrestricted switch-prefix audit")
    print(f"board_lines_with_at_least_three_cells: {len(LINE_MASKS)}")
    print("initial_final_potential: 82, 10")
    print("switch_moves: 92")
    print("strict_initial_descent_moves: 11")
    print("final_legal_improving_neighbors: 810, 0")
    print("final_best_neighbor_potential: 11")
    print("sublevel_component_sizes_at_11_12: 2, 21")
    print("certified_next_barrier_lower_bound: 13")


if __name__ == "__main__":
    main()
