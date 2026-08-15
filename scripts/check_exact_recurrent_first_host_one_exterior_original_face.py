#!/usr/bin/env python3
"""Classify two-point first-host backgrounds with exactly one exterior point."""
from __future__ import annotations

import argparse
import copy
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
RESPONSES: dict[str, tuple[int, ...]] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}
RESPONSE_ORDER = tuple(RESPONSES)
ORIGINAL = ("3012", "3210")
CHART = frozenset((x, y) for x in range(4) for y in range(4))
Point = tuple[int, int]
Line = tuple[int, int, int]
Vector = tuple[int, ...]


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: tuple[int, ...]) -> frozenset[Point]:
    return frozenset((row, permutation[row]) for row in range(4))


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (second[0] - first[0]) * (third[1] - first[1]) == (second[1] - first[1]) * (third[0] - first[0])


def triple_count(points: set[Point] | frozenset[Point]) -> int:
    return sum(collinear(*triple) for triple in combinations(sorted(points), 3))


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
    return line[0] * point[0] + line[1] * point[1] + line[2] == 0


def line_intersection(first: Line, second: Line) -> tuple[Fraction, Fraction] | None:
    a1, b1, c1 = first
    a2, b2, c2 = second
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    return Fraction(b1 * c2 - b2 * c1, determinant), Fraction(c1 * a2 - c2 * a1, determinant)


def add_vectors(*vectors: Vector) -> Vector:
    return tuple(sum(values) for values in zip(*vectors))


def minimizer_face(vector: Vector) -> tuple[str, ...]:
    minimum = min(vector)
    return tuple(name for name, value in zip(RESPONSE_ORDER, vector) if value == minimum)


def original_in_face(vector: Vector) -> bool:
    return any(name in minimizer_face(vector) for name in ORIGINAL)


def original_strict(vector: Vector) -> bool:
    face = minimizer_face(vector)
    return len(face) == 1 and face[0] in ORIGINAL


def direct_score(background: frozenset[Point], response_sets: dict[str, frozenset[Point]]) -> Vector:
    base = triple_count(background)
    values = []
    for name in RESPONSE_ORDER:
        require(background.isdisjoint(response_sets[name]), f"background overlaps {name}")
        values.append(triple_count(background | response_sets[name]) - base)
    return tuple(values)


def secant_lines(response_sets: dict[str, frozenset[Point]]) -> dict[Line, Vector]:
    lines: dict[Line, list[int]] = {}
    for index, name in enumerate(RESPONSE_ORDER):
        for first, second in combinations(sorted(response_sets[name]), 2):
            line = normalize_line(first, second)
            lines.setdefault(line, [0] * len(RESPONSE_ORDER))[index] += 1
    return {line: tuple(vector) for line, vector in lines.items()}


def singleton_vector(point: Point, lines: dict[Line, Vector]) -> Vector:
    result = (0,) * len(RESPONSE_ORDER)
    for line, vector in lines.items():
        if on_line(point, line):
            result = add_vectors(result, vector)
    return result


def pair_vector(line: Line, response_sets: dict[str, frozenset[Point]]) -> Vector:
    return tuple(sum(on_line(point, line) for point in response_sets[name]) for name in RESPONSE_ORDER)


def score_from_components(intrinsic: Vector, singleton: Vector, pair: Vector) -> Vector:
    return add_vectors(intrinsic, singleton, pair)


def audit_singleton_robustness(intrinsic: Vector, lines: dict[Line, Vector], union: frozenset[Point]) -> dict[str, int]:
    generic_lines = 0
    for line, vector in lines.items():
        score = add_vectors(intrinsic, vector)
        require(not original_in_face(score), f"generic singleton line makes original minimal: {line}")
        generic_lines += 1

    integer_intersections: set[Point] = set()
    for first, second in combinations(lines, 2):
        point = line_intersection(first, second)
        if point is None or point[0].denominator != 1 or point[1].denominator != 1:
            continue
        integer = int(point[0]), int(point[1])
        if integer in union:
            continue
        integer_intersections.add(integer)
    for point in integer_intersections:
        require(not original_in_face(add_vectors(intrinsic, singleton_vector(point, lines))), f"singleton intersection makes original minimal: {point}")
    return {"generic_secant_lines": generic_lines, "admissible_integer_secant_intersections": len(integer_intersections)}


def family_record(safe_point: Point, line: Line, constant: int, excluded_parameters: list[int], generic_score: Vector, exceptional: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "safe_chart_point": list(safe_point),
        "line": list(line),
        "parameterization": {"point": ["t", f"{constant}-t"], "integer_parameter": True, "excluded_parameters": excluded_parameters},
        "generic_score_vector": dict(zip(RESPONSE_ORDER, generic_score)),
        "generic_minimizer_face": list(minimizer_face(generic_score)),
        "exceptional_parameters": exceptional,
        "strict_original_minimizer": False,
    }


def compile_manifest() -> dict[str, Any]:
    response_sets = {name: response_points(permutation) for name, permutation in RESPONSES.items()}
    union = frozenset().union(*response_sets.values())
    safe = frozenset(CHART - union)
    require(safe == frozenset({(0, 0), (0, 1), (1, 1), (2, 2), (3, 3)}), "safe chart complement")
    intrinsic = tuple(triple_count(response_sets[name]) for name in RESPONSE_ORDER)
    require(intrinsic == (1, 4, 0, 0, 0), "intrinsic vector")
    lines = secant_lines(response_sets)
    require(len(lines) == 20, "secant line census")
    singleton_audit = audit_singleton_robustness(intrinsic, lines, union)
    require(singleton_audit == {"generic_secant_lines": 20, "admissible_integer_secant_intersections": 16}, "singleton audit census")

    families: list[dict[str, Any]] = []
    isolated: set[tuple[Point, Point, Vector, Line]] = set()
    pair_lines_audited = 0
    integer_exception_candidates = 0

    expected_family_lines = {((1, 1), (1, 1, -2)), ((2, 2), (1, 1, -4))}
    observed_family_lines: set[tuple[Point, Line]] = set()

    for safe_point in sorted(safe):
        pair_lines = {normalize_line(safe_point, union_point) for union_point in union}
        pair_lines_audited += len(pair_lines)
        for line in sorted(pair_lines):
            pair = pair_vector(line, response_sets)
            generic_singleton = lines.get(line, (0,) * len(RESPONSE_ORDER))
            generic_score = score_from_components(intrinsic, generic_singleton, pair)
            if original_in_face(generic_score):
                observed_family_lines.add((safe_point, line))

            exceptional_points: set[Point] = set()
            for secant in lines:
                if secant == line:
                    continue
                point = line_intersection(line, secant)
                if point is None or point[0].denominator != 1 or point[1].denominator != 1:
                    continue
                integer = int(point[0]), int(point[1])
                if integer in CHART or integer in union:
                    continue
                exceptional_points.add(integer)
            integer_exception_candidates += len(exceptional_points)

            exceptions_for_family: list[dict[str, Any]] = []
            for point in sorted(exceptional_points):
                score = score_from_components(intrinsic, singleton_vector(point, lines), pair)
                direct = direct_score(frozenset((safe_point, point)), response_sets)
                require(score == direct, f"component/direct mismatch: {safe_point},{point}")
                if original_in_face(score):
                    if (safe_point, line) in expected_family_lines:
                        parameter = point[0]
                        if score != generic_score:
                            exceptions_for_family.append({"parameter": parameter, "point": list(point), "score_vector": dict(zip(RESPONSE_ORDER, score)), "minimizer_face": list(minimizer_face(score))})
                    else:
                        isolated.add((safe_point, point, score, line))

            if (safe_point, line) in expected_family_lines:
                constant = -line[2]
                excluded = [0, 1, 2] if constant == 2 else [1, 2, 3]
                families.append(family_record(safe_point, line, constant, excluded, generic_score, sorted(exceptions_for_family, key=lambda item: item["parameter"])))

    require(observed_family_lines == expected_family_lines, "infinite family classification")
    require(pair_lines_audited == 36, "safe-point pair-line census")
    require(integer_exception_candidates == 114, "integer exception candidate census")

    expected_isolated = {
        ((0, 0), (-3, -1), (1, 4, 1, 1, 1), (1, -3, 0)),
        ((3, 3), (6, 4), (1, 4, 1, 1, 1), (1, -3, 6)),
    }
    require(isolated == expected_isolated, "isolated pair classification")

    require(len(families) == 2, "family census")
    family_by_constant = {-family["line"][2]: family for family in families}
    require([item["parameter"] for item in family_by_constant[2]["exceptional_parameters"]] == [-3, -1, 3, 5], "x+y=2 exceptions")
    require([item["parameter"] for item in family_by_constant[4]["exceptional_parameters"]] == [-2, 0, 4, 6], "x+y=4 exceptions")

    # Bounded regression: every pair with one safe chart point and one exterior
    # point in the box matches the exact family/isolated predicate.
    bounded_checked = 0
    for safe_point in sorted(safe):
        for x in range(-30, 31):
            for y in range(-30, 31):
                point = (x, y)
                if point in CHART or point in union:
                    continue
                score = direct_score(frozenset((safe_point, point)), response_sets)
                expected = (
                    safe_point == (1, 1) and x + y == 2
                ) or (
                    safe_point == (2, 2) and x + y == 4
                ) or (safe_point, point) in {((0, 0), (-3, -1)), ((3, 3), (6, 4))}
                require(original_in_face(score) == expected, f"bounded classification mismatch: {safe_point},{point}")
                require(not original_strict(score), f"one-exterior strict reversal: {safe_point},{point}")
                bounded_checked += 1

    isolated_rows = [
        {"safe_chart_point": list(safe_point), "exterior_point": list(point), "line": list(line), "score_vector": dict(zip(RESPONSE_ORDER, score)), "minimizer_face": list(minimizer_face(score)), "strict_original_minimizer": False}
        for safe_point, point, score, line in sorted(isolated)
    ]

    return {
        "schema": "exact-recurrent-first-host-one-exterior-original-face/v1",
        "scope": {"host_id": HOST_ID, "background": "two distinct integer points disjoint from response union, exactly one in the standard 4x4 chart", "classification": "original responses in the complete-score minimizer face"},
        "safe_chart_points": [list(point) for point in sorted(safe)],
        "infinite_families": sorted(families, key=lambda item: item["line"]),
        "isolated_pairs": isolated_rows,
        "aggregate": {
            "safe_chart_points": len(safe),
            "response_secant_lines": len(lines),
            "safe_point_pair_lines_audited": pair_lines_audited,
            "integer_pair_secant_exception_candidates": integer_exception_candidates,
            "infinite_original_face_families": len(families),
            "isolated_original_face_pairs": len(isolated_rows),
            "strict_original_reversals_with_one_exterior_point": 0,
            "bounded_pairs_checked": bounded_checked,
        },
        "conclusion": {"one_exterior_point_can_create_original_response_tie": 1, "one_exterior_point_can_create_strict_original_reversal": 0, "strict_two_point_reversal_requires_two_exterior_points": 1, "classification_complete_over_integer_lattice": 1},
        "honesty": {"physical_one_exterior_background_coverage_proved": 0, "physical_chart_confinement_proved": 0, "legal_operations_populated": 0, "recurrent_child_rows_populated": 0, "strict_lyapunov_certificate_proved": 0, "all_n_proved_by_checker": 0},
    }


def validate(manifest: dict[str, Any]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    require(manifest.get("aggregate", {}).get("strict_original_reversals_with_one_exterior_point") == 0, "strict census")
    require(manifest.get("honesty", {}).get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(safe_chart_points=4),
        lambda item: item["aggregate"].update(safe_point_pair_lines_audited=35),
        lambda item: item["aggregate"].update(infinite_original_face_families=1),
        lambda item: item["aggregate"].update(isolated_original_face_pairs=1),
        lambda item: item["aggregate"].update(strict_original_reversals_with_one_exterior_point=1),
        lambda item: item["infinite_families"].pop(),
        lambda item: item["infinite_families"][0]["exceptional_parameters"].pop(),
        lambda item: item["isolated_pairs"].pop(),
        lambda item: item["conclusion"].update(strict_two_point_reversal_requires_two_exterior_points=0),
        lambda item: item["conclusion"].update(classification_complete_over_integer_lattice=0),
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
        arguments.write.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed)
    print(json.dumps({"checker": "exact-recurrent-first-host-one-exterior-original-face", **manifest["aggregate"], "mutation_corruptions_rejected": mutation_audit(manifest), **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()
