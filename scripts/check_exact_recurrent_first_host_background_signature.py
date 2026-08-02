#!/usr/bin/env python3
"""Compile a lossless background signature for the first-host response menu.

For every finite background disjoint from the candidate response points, the
complete new-triple score of all five candidate responses is an affine-linear
function of 20 response-secant loads and 11 background-pair-through-point
counts. This does not populate an actual physical background fibre.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
Line = tuple[int, int, int]
Perm = tuple[int, ...]

HOST_ID = "s4-75b04c45c1c8eac2"
RESPONSES: dict[str, Perm] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}
AUDIT_DOMAIN = tuple((x, y) for x in range(-1, 5) for y in range(-1, 5))
AUDIT_MAX_BACKGROUND_SIZE = 3


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def normalize_line(first: Point, second: Point) -> Line:
    require(first != second, "line requires distinct points")
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "zero line")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def collinear(first: Point, second: Point, third: Point) -> bool:
    return on_line(third, normalize_line(first, second))


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if collinear(first, second, third)
    )


def line_response_occupancies(permutation: Perm) -> dict[Line, int]:
    points = response_points(permutation)
    lines = {normalize_line(first, second) for first, second in combinations(points, 2)}
    return {
        line: sum(on_line(point, line) for point in points)
        for line in lines
    }


def union_coordinates() -> tuple[tuple[Line, ...], tuple[Point, ...]]:
    lines: set[Line] = set()
    points: set[Point] = set()
    for permutation in RESPONSES.values():
        lines.update(line_response_occupancies(permutation))
        points.update(response_points(permutation))
    return tuple(sorted(lines)), tuple(sorted(points))


def background_signature(
    background: tuple[Point, ...],
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> tuple[int, ...]:
    line_loads = tuple(
        sum(on_line(background_point, line) for background_point in background)
        for line in lines
    )
    pair_counts = tuple(
        sum(
            collinear(first, second, response_point)
            for first, second in combinations(background, 2)
        )
        for response_point in points
    )
    return (*line_loads, *pair_counts)


def response_row(
    permutation: Perm,
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> tuple[int, ...]:
    occupancies = line_response_occupancies(permutation)
    line_coefficients = tuple(
        math.comb(occupancies.get(line, 0), 2)
        if occupancies.get(line, 0) >= 2
        else 0
        for line in lines
    )
    response_point_set = set(response_points(permutation))
    point_coefficients = tuple(int(point in response_point_set) for point in points)
    return (*line_coefficients, *point_coefficients)


def intrinsic_score(permutation: Perm) -> int:
    return triple_count(response_points(permutation))


def compressed_score(
    permutation: Perm,
    background: tuple[Point, ...],
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> int:
    signature = background_signature(background, lines, points)
    row = response_row(permutation, lines, points)
    return intrinsic_score(permutation) + sum(
        coefficient * value for coefficient, value in zip(row, signature)
    )


def direct_new_triple_score(permutation: Perm, background: tuple[Point, ...]) -> int:
    response = response_points(permutation)
    require(not set(response) & set(background), "background overlaps response")
    return triple_count((*background, *response)) - triple_count(background)


def matrix_rank(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    column_count = len(matrix[0]) if matrix else 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank:
                continue
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(matrix[index], matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def exhaustive_audit(
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> int:
    available = tuple(point for point in AUDIT_DOMAIN if point not in set(points))
    checked = 0
    for size in range(AUDIT_MAX_BACKGROUND_SIZE + 1):
        for background in combinations(available, size):
            for name, permutation in RESPONSES.items():
                require(
                    compressed_score(permutation, background, lines, points)
                    == direct_new_triple_score(permutation, background),
                    f"{name}: compressed score mismatch on {background}",
                )
            checked += 1
    return checked


def line_code(line: Line) -> str:
    return ",".join(str(value) for value in line)


def point_code(point: Point) -> str:
    return f"{point[0]},{point[1]}"


def compile_manifest() -> dict[str, object]:
    lines, points = union_coordinates()
    require(len(lines) == 20, "twenty secant coordinates")
    require(len(points) == 11, "eleven point coordinates")

    rows = tuple(response_row(permutation, lines, points) for permutation in RESPONSES.values())
    rank = matrix_rank(rows)
    first = rows[0]
    difference_rows = tuple(
        tuple(value - baseline for value, baseline in zip(row, first))
        for row in rows[1:]
    )
    difference_rank = matrix_rank(difference_rows)
    require(rank == 5, "score row rank")
    require(difference_rank == 4, "selector difference rank")

    checked_backgrounds = exhaustive_audit(lines, points)
    require(checked_backgrounds == 2626, "audit background census")

    response_rows = []
    for (name, permutation), row in zip(RESPONSES.items(), rows):
        response_rows.append(
            {
                "response": name,
                "intrinsic_score": intrinsic_score(permutation),
                "response_points": [list(point) for point in response_points(permutation)],
                "coefficient_vector": list(row),
                "nonzero_line_coefficients": {
                    line_code(line): coefficient
                    for line, coefficient in zip(lines, row[: len(lines)])
                    if coefficient
                },
                "pair_through_point_coordinates": [
                    point_code(point)
                    for point, coefficient in zip(points, row[len(lines) :])
                    if coefficient
                ],
            }
        )

    return {
        "schema": "exact-recurrent-first-host-background-signature/v1",
        "scope": {
            "host_id": HOST_ID,
            "responses": list(RESPONSES),
            "score": "new collinear triples containing at least one response point",
            "background_requirement": "finite and disjoint from each evaluated response",
        },
        "identity": (
            "score(Q;B)=intrinsic(Q)+sum_secant C(k_Q(line),2)*h_B(line)"
            "+sum_{q in Q} pair_B(q)"
        ),
        "line_load_coordinates": [
            {"id": f"L{index:02d}", "line": list(line)}
            for index, line in enumerate(lines)
        ],
        "pair_through_point_coordinates": [
            {"id": f"P{index:02d}", "point": list(point)}
            for index, point in enumerate(points)
        ],
        "response_rows": response_rows,
        "aggregate": {
            "responses": 5,
            "line_load_coordinates": 20,
            "pair_through_point_coordinates": 11,
            "signature_coordinates": 31,
            "score_matrix_rank": rank,
            "selector_difference_rank": difference_rank,
            "audit_domain_points": len(AUDIT_DOMAIN),
            "audit_available_background_points": len(AUDIT_DOMAIN) - len(points),
            "audit_max_background_size": AUDIT_MAX_BACKGROUND_SIZE,
            "exhaustive_backgrounds_checked": checked_backgrounds,
        },
        "honesty": {
            "lossless_background_score_signature_proved": 1,
            "finite_exhaustive_implementation_audit_complete": 1,
            "actual_background_signature_populated": 0,
            "physical_deletion_causes_populated": 0,
            "legal_operations_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    honesty = manifest.get("honesty")
    require(isinstance(honesty, dict), "honesty object")
    require(honesty.get("actual_background_signature_populated") == 0, "background honesty")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(line_load_coordinates=19),
        lambda item: item["aggregate"].update(pair_through_point_coordinates=10),
        lambda item: item["aggregate"].update(signature_coordinates=30),
        lambda item: item["aggregate"].update(score_matrix_rank=4),
        lambda item: item["aggregate"].update(selector_difference_rank=3),
        lambda item: item["line_load_coordinates"].pop(),
        lambda item: item["pair_through_point_coordinates"].pop(),
        lambda item: item["response_rows"][0]["coefficient_vector"].__setitem__(0, 99),
        lambda item: item["response_rows"][0].update(intrinsic_score=0),
        lambda item: item["honesty"].update(actual_background_signature_populated=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    manifest = compile_manifest()

    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed)

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-background-signature",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
