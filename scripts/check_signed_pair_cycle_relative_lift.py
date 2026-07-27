#!/usr/bin/env python3
"""Verify the exact lift from signed pair cycles to full relative cycles."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_quarter_turn_seed_normal_forms as qt


def cycles_with_vertices(permutation: list[int]) -> list[list[int]]:
    seen = [False] * len(permutation)
    cycles: list[list[int]] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        cycle: list[int] = []
        current = start
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = permutation[current]
        cycles.append(cycle)
    return sorted(cycles, key=lambda cycle: (-len(cycle), cycle))


def lift_contribution(length: int, parity: int) -> list[int]:
    if length % 2:
        return [2 * length]
    half = length // 2
    if parity == (half % 2):
        return [half, half, half, half]
    return [length, length]


def layers_from_record(raw: Any, ordinal: int) -> tuple[int, list[int], list[int]]:
    if not isinstance(raw, dict):
        raise ValueError(f"case {ordinal}: expected object")
    p = raw.get("p")
    if isinstance(p, bool) or not isinstance(p, int) or not qt.prime(p):
        raise ValueError(f"case {ordinal}: invalid prime")
    n = p - 1

    code = raw.get("code")
    if isinstance(code, str):
        _, points = qt.decode(code, n)
        answer = qt.colour(points, n, 1)
        if answer is None:
            raise ValueError(f"case {ordinal}: no swapped-equivariant colouring")
        return p, answer[0], answer[1]

    sigma_raw = raw.get("sigma")
    tau_raw = raw.get("tau")
    if not isinstance(sigma_raw, list) or not isinstance(tau_raw, list):
        raise ValueError(f"case {ordinal}: expected code or two layers")
    if len(sigma_raw) != n or len(tau_raw) != n:
        raise ValueError(f"case {ordinal}: layer length mismatch")
    sigma = [int(value) - 1 for value in sigma_raw]
    tau = [int(value) - 1 for value in tau_raw]
    if sorted(sigma) != list(range(n)) or sorted(tau) != list(range(n)):
        raise ValueError(f"case {ordinal}: layers are not permutations")

    reversal = [n - 1 - value for value in range(n)]
    inverse = [0] * n
    for column, row in enumerate(sigma):
        inverse[row] = column
    if any(sigma[reversal[x]] != reversal[sigma[x]] for x in range(n)):
        raise ValueError(f"case {ordinal}: sigma does not commute with reversal")
    if tau != [inverse[reversal[x]] for x in range(n)]:
        raise ValueError(f"case {ordinal}: tau is not the forced swapped layer")
    return p, sigma, tau


def verify_case(raw: Any, ordinal: int) -> dict[str, Any]:
    p, sigma, tau = layers_from_record(raw, ordinal)
    n = p - 1
    m = n // 2

    pair_permutation: list[int] = []
    signs: list[int] = []
    for pair in range(m):
        image = sigma[pair]
        pair_permutation.append(image if image < m else n - 1 - image)
        signs.append(0 if image < m else 1)
    if sorted(pair_permutation) != list(range(m)):
        raise ValueError(f"case {ordinal}: pair map is not a permutation")

    signed_cycles: list[dict[str, Any]] = []
    predicted: list[int] = []
    for cycle in cycles_with_vertices(pair_permutation):
        parity = 0
        for pair in cycle:
            parity ^= signs[pair]
        contribution = lift_contribution(len(cycle), parity)
        signed_cycles.append(
            {
                "length": len(cycle),
                "orientation_parity": parity,
                "predicted_relative_cycles": contribution,
            }
        )
        predicted.extend(contribution)
    predicted.sort(reverse=True)

    direct = sorted(
        (len(cycle) for cycle in cycles_with_vertices(qt.rel(sigma, tau))),
        reverse=True,
    )
    if predicted != direct:
        raise ValueError(
            f"case {ordinal}: predicted partition {predicted} != direct {direct}"
        )

    collision_cycles = [
        cycle
        for cycle in signed_cycles
        if cycle["length"] == 2 and cycle["orientation_parity"] == 1
    ]
    cell_collision = any(sigma[x] == tau[x] for x in range(n))
    if bool(collision_cycles) != cell_collision:
        raise ValueError(f"case {ordinal}: collision criterion mismatch")

    return {
        "p": p,
        "n": n,
        "pair_cycle_partition": sorted(
            [cycle["length"] for cycle in signed_cycles], reverse=True
        ),
        "signed_pair_cycles": signed_cycles,
        "predicted_relative_cycle_partition": predicted,
        "direct_relative_cycle_partition": direct,
        "edge_disjoint": not collision_cycles,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path, nargs="+")
    args = parser.parse_args()
    try:
        records: list[Any] = []
        for path in args.inputs:
            raw = json.loads(path.read_text(encoding="utf-8"))
            records.extend(raw if isinstance(raw, list) else [raw])
        if not records:
            raise ValueError("expected at least one record")
        checked = [verify_case(raw, index + 1) for index, raw in enumerate(records)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "signed_pair_cycle_relative_lifts_verified",
                "case_count": len(checked),
                "cases": checked,
                "all_lifts_exact": True,
                "asymptotic_seed_theorem_proved": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
