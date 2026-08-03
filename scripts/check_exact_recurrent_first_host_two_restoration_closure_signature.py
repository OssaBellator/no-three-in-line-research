#!/usr/bin/env python3
"""Compile the first-host safe signature after two-restoration response closure."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
from fractions import Fraction
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
    "2301": (2, 3, 0, 1),
}
SAFE_POINTS = ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3))


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def normalize_line(first: Point, second: Point) -> Line:
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "line divisor")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(point: Point, line: Line) -> bool:
    return line[0] * point[0] + line[1] * point[1] + line[2] == 0


def collinear(first: Point, second: Point, third: Point) -> bool:
    return on_line(third, normalize_line(first, second))


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(collinear(*triple) for triple in itertools.combinations(sequence, 3))


def union_coordinates(names: tuple[str, ...]) -> tuple[tuple[Line, ...], tuple[Point, ...]]:
    lines: set[Line] = set()
    points: set[Point] = set()
    for name in names:
        response = response_points(RESPONSES[name])
        lines.update(normalize_line(*pair) for pair in itertools.combinations(response, 2))
        points.update(response)
    return tuple(sorted(lines)), tuple(sorted(points))


def signature(
    background: tuple[Point, ...],
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> tuple[int, ...]:
    line_loads = tuple(
        sum(on_line(point, line) for point in background)
        for line in lines
    )
    pair_counts = tuple(
        sum(
            collinear(first, second, point)
            for first, second in itertools.combinations(background, 2)
        )
        for point in points
    )
    return (*line_loads, *pair_counts)


def response_row(
    permutation: Perm,
    lines: tuple[Line, ...],
    points: tuple[Point, ...],
) -> tuple[int, ...]:
    response = response_points(permutation)
    line_coefficients = tuple(
        math.comb(sum(on_line(point, line) for point in response), 2)
        for line in lines
    )
    response_set = set(response)
    point_coefficients = tuple(int(point in response_set) for point in points)
    return (*line_coefficients, *point_coefficients)


def score(name: str, background: tuple[Point, ...]) -> int:
    response = response_points(RESPONSES[name])
    return triple_count((*background, *response)) - triple_count(background)


def matrix_rank(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
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
            if index == rank or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(matrix[index], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def point_code(point: Point) -> str:
    return f"{point[0]},{point[1]}"


def line_code(line: Line) -> str:
    return ",".join(str(value) for value in line)


def activation_bits(background: tuple[Point, ...]) -> tuple[int, int, int, int]:
    cells = set(background)
    left = int({(0, 0), (0, 1)} <= cells)
    right = int({(0, 1), (1, 1)} <= cells)
    has_11 = int((1, 1) in cells)
    has_22 = int((2, 2) in cells)
    return left, right, has_11, has_22


def compile_manifest() -> dict[str, object]:
    five_names = tuple(RESPONSES)[:5]
    six_names = tuple(RESPONSES)
    five_lines, _ = union_coordinates(five_names)
    lines, points = union_coordinates(six_names)
    new_lines = tuple(line for line in lines if line not in set(five_lines))

    require(len(five_lines) == 20, "five-response line census")
    require(len(lines) == 23, "six-response line census")
    require(len(points) == 11, "response point census")
    require(
        new_lines == ((1, 1, -4), (1, 1, -2), (3, 1, -6)),
        "new secant lines",
    )
    require(
        triple_count(response_points(RESPONSES["2301"])) == 0,
        "2301 intrinsic score",
    )

    rows = tuple(response_row(RESPONSES[name], lines, points) for name in six_names)
    require(matrix_rank(rows) == 6, "six-response matrix rank")
    difference_rows = tuple(
        tuple(value - baseline for value, baseline in zip(row, rows[0]))
        for row in rows[1:]
    )
    require(matrix_rank(difference_rows) == 5, "selector difference rank")

    signature_classes: dict[tuple[int, ...], list[tuple[Point, ...]]] = {}
    score_classes: dict[tuple[int, ...], list[tuple[Point, ...]]] = {}
    bit_classes: dict[tuple[int, int, int, int], list[tuple[Point, ...]]] = {}
    for size in range(len(SAFE_POINTS) + 1):
        for background in itertools.combinations(SAFE_POINTS, size):
            observed_signature = signature(background, lines, points)
            observed_scores = tuple(score(name, background) for name in six_names)
            bits = activation_bits(background)
            signature_classes.setdefault(observed_signature, []).append(background)
            score_classes.setdefault(observed_scores, []).append(background)
            bit_classes.setdefault(bits, []).append(background)

            left, right, has_11, has_22 = bits
            offset = left + right
            require(
                observed_scores[:5]
                == (1 + offset, 4 + offset, offset, offset, offset),
                "five-score formula",
            )
            require(
                observed_scores[5] == offset + has_11 + has_22,
                "2301 score formula",
            )

    require(sum(map(len, signature_classes.values())) == 32, "safe background census")
    require(len(bit_classes) == 10, "realized four-bit states")
    require(len(signature_classes) == 10, "six-response signature classes")
    require(len(score_classes) == 8, "six-response score classes")

    classes = []
    for observed_signature, backgrounds in sorted(
        signature_classes.items(),
        key=lambda item: (activation_bits(item[1][0]), item[1][0]),
    ):
        representative = backgrounds[0]
        line_values = observed_signature[: len(lines)]
        point_values = observed_signature[len(lines) :]
        classes.append({
            "activation_bits": list(activation_bits(representative)),
            "background_count": len(backgrounds),
            "representative": [point_code(point) for point in representative],
            "score_vector": [score(name, representative) for name in six_names],
            "nonzero_line_loads": {
                line_code(line): value
                for line, value in zip(lines, line_values)
                if value
            },
            "nonzero_pair_through_points": {
                point_code(point): value
                for point, value in zip(points, point_values)
                if value
            },
        })

    return {
        "schema": "exact-recurrent-first-host-two-restoration-closure-signature/v1",
        "scope": {
            "host_id": HOST_ID,
            "response_order": list(six_names),
            "new_response": "2301",
            "safe_background_universe": [point_code(point) for point in SAFE_POINTS],
            "activation_bits": [
                "pair-00-01",
                "pair-01-11",
                "cell-11",
                "cell-22",
            ],
        },
        "closure": {
            "five_response_line_coordinates": len(five_lines),
            "six_response_line_coordinates": len(lines),
            "new_secant_lines": [list(line) for line in new_lines],
            "pair_through_point_coordinates": len(points),
            "signature_coordinates": len(lines) + len(points),
            "score_formula": {
                "first_five": "(1+c,4+c,c,c,c), c=a+b",
                "2301": "a+b+u+v",
            },
        },
        "signature_classes": classes,
        "aggregate": {
            "safe_backgrounds": 32,
            "responses": 6,
            "five_response_signature_coordinates": 31,
            "closure_signature_coordinates": 34,
            "new_line_coordinates": 3,
            "response_matrix_rank": 6,
            "selector_difference_rank": 5,
            "realized_activation_bit_states": len(bit_classes),
            "exact_34_coordinate_signature_classes": len(signature_classes),
            "complete_six_response_score_classes": len(score_classes),
            "maximum_signatures_per_score_class": max(
                sum(
                    1
                    for signature_backgrounds in signature_classes.values()
                    if tuple(
                        score(name, signature_backgrounds[0])
                        for name in six_names
                    )
                    == score_vector
                )
                for score_vector in score_classes
            ),
        },
        "conclusion": {
            "five_response_four_signature_quotient_transition_closed": 0,
            "adding_2301_splits_safe_signature_classes": 1,
            "cells_11_and_22_visible_to_2301": 1,
            "cell_33_invisible_to_six_response_signature": 1,
            "exact_ten_signature_candidate_available": 1,
            "promotion_to_recurrent_row_allowed": 0,
        },
        "honesty": {
            "physical_two_restoration_operation_proved": 0,
            "physical_chart_confinement_proved": 0,
            "legal_operations_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(responses=5),
        lambda item: item["aggregate"].update(closure_signature_coordinates=33),
        lambda item: item["aggregate"].update(new_line_coordinates=2),
        lambda item: item["aggregate"].update(response_matrix_rank=5),
        lambda item: item["aggregate"].update(realized_activation_bit_states=9),
        lambda item: item["aggregate"].update(exact_34_coordinate_signature_classes=9),
        lambda item: item["aggregate"].update(complete_six_response_score_classes=7),
        lambda item: item["conclusion"].update(
            five_response_four_signature_quotient_transition_closed=1
        ),
        lambda item: item["conclusion"].update(cells_11_and_22_visible_to_2301=0),
        lambda item: item["honesty"].update(physical_two_restoration_operation_proved=1),
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
        validate(json.loads(arguments.check.read_text(encoding="utf-8")))

    print(json.dumps({
        "checker": "exact-recurrent-first-host-two-restoration-closure-signature",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
