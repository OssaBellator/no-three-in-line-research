#!/usr/bin/env python3
"""Classify strict original-response minimizers for every integer two-point background."""
from __future__ import annotations

import argparse
import copy
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
Line = tuple[int, int, int]
Vector = tuple[int, ...]
Perm = tuple[int, ...]

HOST_ID = "s4-75b04c45c1c8eac2"
RESPONSES: dict[str, Perm] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}


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


def line_intersection(first: Line, second: Line) -> tuple[Fraction, Fraction] | None:
    a, b, c = first
    d, e, f = second
    determinant = a * e - b * d
    if determinant == 0:
        return None
    return (
        Fraction(b * f - c * e, determinant),
        Fraction(c * d - a * f, determinant),
    )


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if on_line(third, normalize_line(first, second))
    )


def intrinsic_vector() -> Vector:
    return tuple(
        triple_count(response_points(permutation))
        for permutation in RESPONSES.values()
    )


def response_union() -> tuple[Point, ...]:
    return tuple(
        sorted(
            {
                point
                for permutation in RESPONSES.values()
                for point in response_points(permutation)
            }
        )
    )


def response_secant_occupancies() -> dict[str, dict[Line, int]]:
    rows: dict[str, dict[Line, int]] = {}
    for name, permutation in RESPONSES.items():
        points = response_points(permutation)
        lines = {
            normalize_line(first, second)
            for first, second in combinations(points, 2)
        }
        rows[name] = {
            line: sum(on_line(point, line) for point in points)
            for line in lines
        }
    return rows


def secant_lines(occupancies: dict[str, dict[Line, int]]) -> tuple[Line, ...]:
    return tuple(sorted({line for row in occupancies.values() for line in row}))


def singleton_increment(
    point: Point,
    occupancies: dict[str, dict[Line, int]],
) -> Vector:
    return tuple(
        sum(
            math.comb(load, 2)
            for line, load in occupancies[name].items()
            if load >= 2 and on_line(point, line)
        )
        for name in RESPONSES
    )


def generic_secant_vector(
    line: Line,
    occupancies: dict[str, dict[Line, int]],
) -> Vector:
    return tuple(
        math.comb(occupancies[name].get(line, 0), 2)
        if occupancies[name].get(line, 0) >= 2
        else 0
        for name in RESPONSES
    )


def pair_vector(line: Line) -> Vector:
    return tuple(
        sum(on_line(point, line) for point in response_points(permutation))
        for permutation in RESPONSES.values()
    )


def union_incidence(line: Line, union: tuple[Point, ...]) -> tuple[Point, ...]:
    return tuple(point for point in union if on_line(point, line))


def score_vector(first: Vector, second: Vector, pair: Vector) -> Vector:
    base = intrinsic_vector()
    return tuple(
        base[index] + first[index] + second[index] + pair[index]
        for index in range(5)
    )


def minimizer_face(scores: Vector) -> tuple[str, ...]:
    minimum = min(scores)
    return tuple(name for name, value in zip(RESPONSES, scores) if value == minimum)


def integer_secant_intersections(
    lines: tuple[Line, ...],
    union: tuple[Point, ...],
) -> tuple[Point, ...]:
    forbidden = set(union)
    points: set[Point] = set()
    for first, second in combinations(lines, 2):
        result = line_intersection(first, second)
        if result is None:
            continue
        x, y = result
        if x.denominator == 1 and y.denominator == 1:
            point = int(x), int(y)
            if point not in forbidden:
                points.add(point)
    return tuple(sorted(points))


def singleton_alphabet(
    lines: tuple[Line, ...],
    occupancies: dict[str, dict[Line, int]],
    intersections: tuple[Point, ...],
) -> tuple[set[Vector], dict[Vector, tuple[Line, ...]], dict[Vector, tuple[Point, ...]]]:
    alphabet: set[Vector] = {(0, 0, 0, 0, 0)}
    vector_lines: dict[Vector, list[Line]] = defaultdict(list)
    vector_points: dict[Vector, list[Point]] = defaultdict(list)
    for line in lines:
        vector = generic_secant_vector(line, occupancies)
        alphabet.add(vector)
        vector_lines[vector].append(line)
    for point in intersections:
        vector = singleton_increment(point, occupancies)
        alphabet.add(vector)
        vector_points[vector].append(point)
    return (
        alphabet,
        {vector: tuple(sorted(rows)) for vector, rows in vector_lines.items()},
        {vector: tuple(sorted(rows)) for vector, rows in vector_points.items()},
    )


def pair_sources(
    union: tuple[Point, ...],
) -> tuple[set[Vector], dict[Vector, tuple[Line, ...]], dict[Vector, tuple[Point, ...]]]:
    alphabet: set[Vector] = {(0, 0, 0, 0, 0)}
    multi: dict[Vector, set[Line]] = defaultdict(set)
    single: dict[Vector, set[Point]] = defaultdict(set)
    union_lines: set[Line] = set()
    for first, second in combinations(union, 2):
        union_lines.add(normalize_line(first, second))
    for line in union_lines:
        vector = pair_vector(line)
        alphabet.add(vector)
        multi[vector].add(line)
    for point in union:
        vector = tuple(
            int(point in response_points(permutation))
            for permutation in RESPONSES.values()
        )
        alphabet.add(vector)
        single[vector].add(point)
    require(len(alphabet) == 39, "pair vector alphabet")
    return (
        alphabet,
        {vector: tuple(sorted(rows)) for vector, rows in multi.items()},
        {vector: tuple(sorted(rows)) for vector, rows in single.items()},
    )


def abstract_strict_triples(
    singleton_vectors: set[Vector],
    pair_vectors: set[Vector],
) -> tuple[list[tuple[Vector, Vector, Vector, Vector]], list[tuple[Vector, Vector, Vector, Vector]]]:
    strict_3012 = []
    strict_3210 = []
    for first in sorted(singleton_vectors):
        for second in sorted(singleton_vectors):
            if first > second:
                continue
            for pair in sorted(pair_vectors):
                scores = score_vector(first, second, pair)
                face = minimizer_face(scores)
                record = first, second, pair, scores
                if face == ("3012",):
                    strict_3012.append(record)
                if face == ("3210",):
                    strict_3210.append(record)
    return strict_3012, strict_3210


def integer_points_on_fixed_line(
    line: Line,
    secants: tuple[Line, ...],
    union: tuple[Point, ...],
    occupancies: dict[str, dict[Line, int]],
) -> tuple[Vector, tuple[Point, ...]]:
    generic = (
        generic_secant_vector(line, occupancies)
        if line in secants
        else (0, 0, 0, 0, 0)
    )
    forbidden = set(union)
    exceptional: set[Point] = set()
    for secant in secants:
        result = line_intersection(line, secant)
        if result is None:
            continue
        x, y = result
        if x.denominator == 1 and y.denominator == 1:
            point = int(x), int(y)
            if point not in forbidden:
                exceptional.add(point)
    return generic, tuple(sorted(exceptional))


def direct_score(name: str, background: tuple[Point, Point]) -> int:
    response = response_points(RESPONSES[name])
    require(not set(background) & set(response), "background overlaps response")
    return triple_count((*background, *response)) - triple_count(background)


def compile_manifest() -> dict[str, object]:
    intrinsic = intrinsic_vector()
    require(intrinsic == (1, 4, 0, 0, 0), "intrinsic vector")
    union = response_union()
    require(len(union) == 11, "union size")
    occupancies = response_secant_occupancies()
    secants = secant_lines(occupancies)
    require(len(secants) == 20, "secant count")
    intersections = integer_secant_intersections(secants, union)
    require(len(intersections) == 16, "integer intersection count")

    singleton_vectors, _vector_lines, vector_points = singleton_alphabet(
        secants, occupancies, intersections
    )
    require(len(singleton_vectors) == 15, "singleton alphabet")
    pair_vectors, multi_sources, single_sources = pair_sources(union)
    strict_3012, strict_3210 = abstract_strict_triples(
        singleton_vectors, pair_vectors
    )
    require(len(strict_3012) == 43, "abstract 3012 strict triples")
    require(len(strict_3210) == 0, "abstract 3210 strict triples")

    allowed_by_pair: dict[Vector, set[tuple[Vector, Vector]]] = defaultdict(set)
    for first, second, pair, _scores in strict_3012:
        allowed_by_pair[pair].add((first, second))
        allowed_by_pair[pair].add((second, first))

    fixed_line_records = []
    strict_pairs: set[tuple[Point, Point]] = set()
    generic_strict_families = 0
    fixed_line_candidate_pairs = 0

    for pair in sorted(allowed_by_pair):
        for line in multi_sources.get(pair, ()):
            generic, exceptional = integer_points_on_fixed_line(
                line, secants, union, occupancies
            )
            exceptional_rows = [
                (point, singleton_increment(point, occupancies))
                for point in exceptional
            ]
            generic_compatible = (generic, generic) in allowed_by_pair[pair]
            generic_exceptional = [
                point
                for point, vector in exceptional_rows
                if (generic, vector) in allowed_by_pair[pair]
                or (vector, generic) in allowed_by_pair[pair]
            ]
            if generic_compatible or generic_exceptional:
                generic_strict_families += 1

            line_strict: list[tuple[Point, Point]] = []
            for (first_point, first_vector), (second_point, second_vector) in combinations(
                exceptional_rows, 2
            ):
                fixed_line_candidate_pairs += 1
                if (first_vector, second_vector) not in allowed_by_pair[pair]:
                    continue
                require(normalize_line(first_point, second_point) == line, "fixed line")
                scores = score_vector(first_vector, second_vector, pair)
                require(minimizer_face(scores) == ("3012",), "abstract strictness")
                direct = tuple(
                    direct_score(name, (first_point, second_point))
                    for name in RESPONSES
                )
                require(direct == scores, "direct fixed-line score")
                ordered = tuple(sorted((first_point, second_point)))
                strict_pairs.add(ordered)
                line_strict.append(ordered)

            fixed_line_records.append(
                {
                    "line": list(line),
                    "pair_vector": list(pair),
                    "generic_singleton_vector": list(generic),
                    "exceptional_integer_points": [
                        {"point": list(point), "singleton_vector": list(vector)}
                        for point, vector in exceptional_rows
                    ],
                    "generic_strict_family": bool(
                        generic_compatible or generic_exceptional
                    ),
                    "strict_pairs": [
                        [list(first), list(second)]
                        for first, second in sorted(set(line_strict))
                    ],
                }
            )

    require(generic_strict_families == 0, "no generic strict family")

    single_source_candidates = 0
    single_source_strict = []
    for pair in sorted(allowed_by_pair):
        for union_point in single_sources.get(pair, ()):
            for first_vector, second_vector in sorted(allowed_by_pair[pair]):
                first_points = vector_points.get(first_vector, ())
                second_points = vector_points.get(second_vector, ())
                if not first_points or not second_points:
                    continue
                pairs = (
                    combinations(first_points, 2)
                    if first_vector == second_vector
                    else product(first_points, second_points)
                )
                for first_point, second_point in pairs:
                    if first_point == second_point:
                        continue
                    single_source_candidates += 1
                    line = normalize_line(first_point, second_point)
                    if union_incidence(line, union) != (union_point,):
                        continue
                    scores = score_vector(first_vector, second_vector, pair)
                    require(minimizer_face(scores) == ("3012",), "single source strictness")
                    direct = tuple(
                        direct_score(name, (first_point, second_point))
                        for name in RESPONSES
                    )
                    require(direct == scores, "direct single-source score")
                    ordered = tuple(sorted((first_point, second_point)))
                    strict_pairs.add(ordered)
                    single_source_strict.append(ordered)

    require(not single_source_strict, "single-union-point strict pairs absent")
    expected = {
        ((-3, 5), (5, -3)),
        ((-1, 3), (5, -3)),
        ((-2, 6), (4, 0)),
        ((-2, 6), (6, -2)),
    }
    require(strict_pairs == expected, "complete strict pair set")

    strict_records = []
    for first, second in sorted(strict_pairs):
        scores = tuple(direct_score(name, (first, second)) for name in RESPONSES)
        require(scores == (1, 4, 2, 2, 2), "strict score vector")
        strict_records.append(
            {
                "background": [list(first), list(second)],
                "line": list(normalize_line(first, second)),
                "singleton_vectors": [
                    list(singleton_increment(first, occupancies)),
                    list(singleton_increment(second, occupancies)),
                ],
                "pair_vector": list(pair_vector(normalize_line(first, second))),
                "complete_score_vector": {
                    name: value for name, value in zip(RESPONSES, scores)
                },
                "minimum_coordinate_radius": max(
                    abs(coordinate)
                    for point in (first, second)
                    for coordinate in point
                ),
            }
        )

    strict_pair_vector_types = sorted(
        {tuple(record["pair_vector"]) for record in strict_records}
    )
    require(strict_pair_vector_types == [(0, 0, 1, 1, 1)], "strict pair vector")

    return {
        "schema": "exact-recurrent-first-host-global-integer-two-point-strict-reversal/v1",
        "scope": {
            "host_id": HOST_ID,
            "background": "two distinct integer points disjoint from the five-response union",
            "coverage": "full integer lattice",
            "responses": list(RESPONSES),
            "classification": "strict original-response minimizers only",
        },
        "intrinsic_score_vector": {
            name: value for name, value in zip(RESPONSES, intrinsic)
        },
        "strict_reversals": strict_records,
        "fixed_pair_line_audit": fixed_line_records,
        "aggregate": {
            "singleton_vector_classes": len(singleton_vectors),
            "pair_vector_classes": len(pair_vectors),
            "abstract_strict_3012_vector_triples": len(strict_3012),
            "abstract_strict_3210_vector_triples": len(strict_3210),
            "strict_pair_vector_types": len(strict_pair_vector_types),
            "fixed_union_lines_audited": len(fixed_line_records),
            "fixed_line_exceptional_pair_candidates": fixed_line_candidate_pairs,
            "generic_strict_families": generic_strict_families,
            "single_union_point_candidate_pairs": single_source_candidates,
            "single_union_point_strict_pairs": len(single_source_strict),
            "global_integer_strict_3012_pairs": len(strict_pairs),
            "global_integer_strict_3210_pairs": 0,
            "radius_census": {
                str(key): value
                for key, value in sorted(
                    Counter(
                        record["minimum_coordinate_radius"]
                        for record in strict_records
                    ).items()
                )
            },
        },
        "honesty": {
            "global_integer_two_point_strict_reversal_classification_complete": 1,
            "full_two_point_score_signature_classification_complete": 0,
            "physical_two_point_background_coverage_proved": 0,
            "deletion_causes_populated": 0,
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
    require(
        honesty.get("global_integer_two_point_strict_reversal_classification_complete") == 1,
        "classification honesty",
    )
    require(
        honesty.get("full_two_point_score_signature_classification_complete") == 0,
        "full atlas honesty",
    )
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(singleton_vector_classes=14),
        lambda item: item["aggregate"].update(pair_vector_classes=38),
        lambda item: item["aggregate"].update(abstract_strict_3012_vector_triples=42),
        lambda item: item["aggregate"].update(abstract_strict_3210_vector_triples=1),
        lambda item: item["aggregate"].update(generic_strict_families=1),
        lambda item: item["aggregate"].update(global_integer_strict_3012_pairs=3),
        lambda item: item["aggregate"].update(global_integer_strict_3210_pairs=1),
        lambda item: item["strict_reversals"].pop(),
        lambda item: item["strict_reversals"][0]["complete_score_vector"].update({"3012": 2}),
        lambda item: item["fixed_pair_line_audit"].pop(),
        lambda item: item["honesty"].update(full_two_point_score_signature_classification_complete=1),
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
                "checker": "exact-recurrent-first-host-global-integer-two-point-strict-reversal",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
