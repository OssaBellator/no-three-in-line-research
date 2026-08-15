#!/usr/bin/env python3
"""Reconstruct exact occupancy moments for the first side-four residual host."""
from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from typing import Any


Point = tuple[int, int]
Line = tuple[int, int, int]


class OccupancyMomentError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise OccupancyMomentError(message)


def line_signature(first: Point, second: Point) -> Line:
    require(first != second, "line requires distinct points")
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "zero line")
    a //= divisor
    b //= divisor
    c //= divisor
    for value in (a, b, c):
        if value:
            if value < 0:
                a, b, c = -a, -b, -c
            break
    return a, b, c


def on_line(line: Line, point: Point) -> bool:
    return line[0] * point[0] + line[1] * point[1] + line[2] == 0


def line_text(line: Line) -> str:
    return ",".join(str(value) for value in line)


def parse_line(value: str) -> Line:
    require(isinstance(value, str), "line key must be string")
    pieces = value.split(",")
    require(
        len(pieces) == 3 and all(piece.lstrip("-").isdigit() for piece in pieces),
        f"invalid line key {value!r}",
    )
    return int(pieces[0]), int(pieces[1]), int(pieces[2])


def response_points(permutation: str) -> tuple[Point, ...]:
    require(
        isinstance(permutation, str)
        and len(permutation) == 4
        and set(permutation) == set("0123"),
        f"invalid response {permutation!r}",
    )
    return tuple((row, int(column)) for row, column in enumerate(permutation))


def compile_moments(side: int, response_family: list[str]) -> dict[str, Any]:
    require(side == 4, "this compiler is normalized to side four")
    require(response_family == ["3012", "3210"], "first-host response family mismatch")
    grid = tuple((row, column) for row in range(side) for column in range(side))
    lines = {
        line_signature(first, second)
        for first, second in combinations(grid, 2)
        if first[0] != second[0] and first[1] != second[1]
    }
    responses = tuple(response_points(permutation) for permutation in response_family)
    capacities: dict[Line, int] = {}
    for line in lines:
        capacity = max(
            sum(1 for point in response if on_line(line, point))
            for response in responses
        )
        if capacity:
            capacities[line] = capacity

    m1 = sum(capacities.values())
    m2 = sum(comb(capacity, 2) for capacity in capacities.values())
    m3 = sum(comb(capacity, 3) for capacity in capacities.values())
    return {
        "all_lines": lines,
        "capacities": capacities,
        "M1": m1,
        "M2": m2,
        "M3": m3,
        "E2": m1 + 2 * m2 + m3,
    }


def validate(manifest: dict[str, Any]) -> dict[str, Any]:
    require(
        manifest.get("schema") == "exact-recurrent-first-host-occupancy-moments/v1",
        "schema mismatch",
    )
    require(
        manifest.get("line_scope")
        == "all nonhorizontal nonvertical real lines containing at least two cells of the standard 4x4 grid",
        "line scope mismatch",
    )

    host = manifest.get("host")
    require(isinstance(host, dict), "host object required")
    require(host.get("upstream_id") == "s4-75b04c45c1c8eac2", "host id mismatch")
    require(host.get("deletions") == ["02", "20"], "deletions mismatch")
    require(host.get("ambient_side") == 4, "ambient side mismatch")
    require(host.get("response_family") == ["3012", "3210"], "response family mismatch")

    compiled = compile_moments(host["ambient_side"], host["response_family"])
    declared_capacities = manifest.get("active_line_capacities")
    require(isinstance(declared_capacities, dict), "capacity table required")
    parsed_capacities: dict[Line, int] = {}
    for key, value in declared_capacities.items():
        line = parse_line(key)
        require(line_text(line) == key, f"line key is not normalized: {key}")
        require(isinstance(value, int) and value > 0, f"invalid capacity for {key}")
        require(line not in parsed_capacities, f"duplicate line {key}")
        parsed_capacities[line] = value
    require(parsed_capacities == compiled["capacities"], "capacity table mismatch")

    census = Counter(compiled["capacities"].values())
    expected_aggregate = {
        "nonaxis_grid_lines": len(compiled["all_lines"]),
        "active_lines": len(compiled["capacities"]),
        "capacity_census": {str(key): value for key, value in sorted(census.items())},
        "maximum_capacity": max(compiled["capacities"].values()),
        "M1": compiled["M1"],
        "M2": compiled["M2"],
        "M3": compiled["M3"],
        "E2": compiled["E2"],
    }
    require(manifest.get("aggregate") == expected_aggregate, "aggregate mismatch")
    require(expected_aggregate == {
        "nonaxis_grid_lines": 54,
        "active_lines": 35,
        "capacity_census": {"1": 31, "2": 2, "3": 1, "4": 1},
        "maximum_capacity": 4,
        "M1": 42,
        "M2": 11,
        "M3": 5,
        "E2": 69,
    }, "unexpected exact first-host moment values")

    certificate = manifest.get("uniform_background_certificate")
    require(isinstance(certificate, dict), "uniform background certificate required")
    require(
        certificate.get("assumption")
        == "every relevant nonaxis background line has load at most H",
        "certificate assumption mismatch",
    )
    require(
        certificate.get("bound") == "C(H,2)*M1+H*M2+M3",
        "certificate formula mismatch",
    )
    h = certificate.get("triple_free_background_H")
    require(h == 2, "triple-free background height must be two")
    bound = comb(h, 2) * compiled["M1"] + h * compiled["M2"] + compiled["M3"]
    require(
        certificate.get("triple_free_background_bound") == bound == 69,
        "triple-free background bound mismatch",
    )

    expected_honesty = {
        "first_host_occupancy_moments_complete": 1,
        "triple_free_background_upper_certificate_complete": 1,
        "actual_background_profile_populated": 0,
        "complete_coupled_row_exact": 0,
        "destroyed_load_or_parent_budget_populated": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    require(manifest.get("honesty") == expected_honesty, "honesty mismatch")

    return {
        "host": host["upstream_id"],
        **expected_aggregate,
        "triple_free_background_bound": bound,
        "first_host_occupancy_moments_complete": 1,
        "complete_coupled_row_exact": 0,
        "strict_lyapunov_certificate_proved": 0,
        "all_n_proved_by_checker": 0,
    }


def mutation_audit(manifest: dict[str, Any]) -> int:
    first_line = next(iter(manifest["active_line_capacities"]))
    mutations = [
        lambda item: item.update(schema="wrong"),
        lambda item: item["host"].update(upstream_id="wrong"),
        lambda item: item["host"].update(response_family=["3012"]),
        lambda item: item["active_line_capacities"].pop(first_line),
        lambda item: item["active_line_capacities"].update(**{first_line: 9}),
        lambda item: item["aggregate"].update(nonaxis_grid_lines=53),
        lambda item: item["aggregate"].update(M1=41),
        lambda item: item["aggregate"].update(E2=68),
        lambda item: item["uniform_background_certificate"].update(triple_free_background_H=3),
        lambda item: item["uniform_background_certificate"].update(triple_free_background_bound=68),
        lambda item: item["honesty"].update(complete_coupled_row_exact=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (OccupancyMomentError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit accepted corrupted moments")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = validate(manifest)
    result["mutation_corruptions_rejected"] = mutation_audit(manifest)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
