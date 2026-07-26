#!/usr/bin/env python3
"""Check exact current-reference defect growth and epoch reset."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def apply_cycle(permutation: list[int], cycle: list[int]) -> list[int]:
    result = permutation.copy()
    for index, row in enumerate(cycle):
        result[row] = permutation[cycle[(index + 1) % len(cycle)]]
    return result


def defect(reference: list[int], current: list[int]) -> set[int]:
    return {i for i, (a, b) in enumerate(zip(reference, current)) if a != b}


def is_permutation(values: list[int]) -> bool:
    return sorted(values) == list(range(len(values)))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    m = int(data["m"])
    shift = int(data["complement_shift"])
    q = int(data["q"])
    seed = [int(x) for x in data["seed_rows"]]
    growth_moves = [[int(x) for x in move] for move in data["growth_moves"]]
    next_seed = [int(x) for x in data["next_seed_rows"]]
    R = int(data["R"])
    W = int(data["W"])

    if len(seed) != q or any(len(move) != q for move in growth_moves) or len(next_seed) != q:
        raise AssertionError("every stored move must have size q")

    reference = list(range(m))
    current = reference.copy()
    complement = [(i + shift) % m for i in range(m)]
    if any(reference[i] == complement[i] for i in range(m)):
        raise AssertionError("the two initial layers are not edge-disjoint")

    selected: set[int] = set()
    defect_sizes: list[int] = []

    current = apply_cycle(current, seed)
    selected.update(seed)
    defect_sizes.append(len(defect(reference, current)))

    for move in growth_moves:
        centre = move[0]
        helpers = set(move[1:])
        current_defect = defect(reference, current)
        if centre not in current_defect:
            raise AssertionError("growth centre is not currently defective")
        if helpers & current_defect:
            raise AssertionError("growth helper is not fresh")
        current = apply_cycle(current, move)
        selected.update(move)
        defect_sizes.append(len(defect(reference, current)))

    expected_sizes = [q + i * (q - 1) for i in range(len(defect_sizes))]
    if defect_sizes != expected_sizes:
        raise AssertionError(f"unexpected defect growth: {defect_sizes} != {expected_sizes}")
    if len(selected) != defect_sizes[-1]:
        raise AssertionError("selected-index count differs from final defect size")
    if not is_permutation(current):
        raise AssertionError("active layer ceased to be a permutation")
    if any(current[i] == complement[i] for i in range(m)):
        raise AssertionError("active and complementary layers collide")

    punctures = len(selected)
    if punctures > W:
        raise AssertionError("stored epoch exceeds the target selected-index budget")
    if punctures >= R:
        raise AssertionError("stored puncture cost is not sub-domain-scale")

    new_reference = current.copy()
    reset_defect = len(defect(new_reference, current))
    if reset_defect != 0:
        raise AssertionError("reference reset did not clear the relative defect")

    second_current = apply_cycle(current, next_seed)
    second_defect = len(defect(new_reference, second_current))
    if second_defect != q:
        raise AssertionError("new epoch seed did not create a q-cycle defect")
    if not is_permutation(second_current):
        raise AssertionError("second epoch active layer ceased to be a permutation")
    if any(second_current[i] == complement[i] for i in range(m)):
        raise AssertionError("second epoch collides with the complementary layer")

    print("m", m)
    print("q", q)
    print("first epoch defect sizes", defect_sizes)
    print("first epoch selected indices", len(selected))
    print("selected punctures", punctures)
    print("puncture to R ratio", punctures / R)
    print("defect after reference reset", reset_defect)
    print("next epoch seed defect", second_defect)
    print("complementary layer preserved", True)
    print("outcome current_reference_epoch_reset")


if __name__ == "__main__":
    main()
