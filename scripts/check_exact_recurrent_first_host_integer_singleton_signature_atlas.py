#!/usr/bin/env python3
"""Classify every integer singleton-background score signature for the first host.

The classification is exact over the full integer lattice. A singleton point is
either off all 20 response secants, on exactly one secant, or at an intersection
of at least two secants. Generic integer witnesses are supplied for every line,
and every admissible integer line intersection is enumerated.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from collections import Counter, defaultdict
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
REOPENINGS = ("2031", "2310", "3201")
AUDIT_RADIUS = 50


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


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if on_line(third, normalize_line(first, second))
    )


def line_occupancies(permutation: Perm) -> dict[Line, int]:
    points = response_points(permutation)
    lines = {normalize_line(first, second) for first, second in combinations(points, 2)}
    return {line: sum(on_line(point, line) for point in points) for line in lines}


def secant_data() -> tuple[tuple[Line, ...], dict[str, dict[Line, int]], tuple[Point, ...]]:
    occupancies = {name: line_occupancies(permutation) for name, permutation in RESPONSES.items()}
    lines = tuple(sorted({line for row in occupancies.values() for line in row}))
    points = tuple(sorted({point for permutation in RESPONSES.values() for point in response_points(permutation)}))
    require(len(lines) == 20, "twenty distinct secants")
    require(len(points) == 11, "eleven response-union points")
    return lines, occupancies, points


def line_increment_vector(
    line: Line,
    occupancies: dict[str, dict[Line, int]],
) -> tuple[int, ...]:
    return tuple(
        math.comb(occupancies[name].get(line, 0), 2)
        if occupancies[name].get(line, 0) >= 2
        else 0
        for name in RESPONSES
    )


def incident_lines(point: Point, lines: tuple[Line, ...]) -> tuple[Line, ...]:
    return tuple(line for line in lines if on_line(point, line))


def increment_vector(
    point: Point,
    lines: tuple[Line, ...],
    occupancies: dict[str, dict[Line, int]],
) -> tuple[int, ...]:
    total = [0] * len(RESPONSES)
    for line in incident_lines(point, lines):
        total = [
            value + increment
            for value, increment in zip(total, line_increment_vector(line, occupancies))
        ]
    return tuple(total)


def intrinsic_vector() -> tuple[int, ...]:
    return tuple(triple_count(response_points(permutation)) for permutation in RESPONSES.values())


def score_vector(increments: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(base + delta for base, delta in zip(intrinsic_vector(), increments))


def minimizer_face(scores: tuple[int, ...]) -> tuple[str, ...]:
    minimum = min(scores)
    return tuple(name for name, value in zip(RESPONSES, scores) if value == minimum)


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


def rational_intersections(lines: tuple[Line, ...]) -> tuple[tuple[Fraction, Fraction], ...]:
    points = {
        point
        for first, second in combinations(lines, 2)
        if (point := line_intersection(first, second)) is not None
    }
    return tuple(sorted(points))


def integer_intersections(
    lines: tuple[Line, ...],
    forbidden_points: tuple[Point, ...],
) -> tuple[Point, ...]:
    forbidden = set(forbidden_points)
    points = {
        (int(x), int(y))
        for x, y in rational_intersections(lines)
        if x.denominator == 1 and y.denominator == 1 and (int(x), int(y)) not in forbidden
    }
    return tuple(sorted(points))


def nearest_generic_witness(
    line: Line,
    lines: tuple[Line, ...],
    forbidden_points: tuple[Point, ...],
) -> Point:
    forbidden = set(forbidden_points)
    candidates = []
    for x in range(-30, 31):
        for y in range(-30, 31):
            point = (x, y)
            if point in forbidden:
                continue
            if incident_lines(point, lines) == (line,):
                candidates.append(point)
    require(candidates, f"generic integer witness missing for {line}")
    return min(
        candidates,
        key=lambda point: (
            max(abs(point[0]), abs(point[1])),
            abs(point[0]) + abs(point[1]),
            point,
        ),
    )


def nearest_off_secant_witness(
    lines: tuple[Line, ...],
    forbidden_points: tuple[Point, ...],
) -> Point:
    forbidden = set(forbidden_points)
    candidates = []
    for x in range(-10, 11):
        for y in range(-10, 11):
            point = (x, y)
            if point not in forbidden and not incident_lines(point, lines):
                candidates.append(point)
    require(candidates, "off-secant integer witness missing")
    return min(
        candidates,
        key=lambda point: (
            max(abs(point[0]), abs(point[1])),
            abs(point[0]) + abs(point[1]),
            point,
        ),
    )


def direct_score(name: str, point: Point) -> int:
    response = response_points(RESPONSES[name])
    require(point not in response, "singleton overlaps response")
    return triple_count((*response, point))


def signature_record(
    identifier: str,
    increments: tuple[int, ...],
    realizers: list[dict[str, object]],
) -> dict[str, object]:
    scores = score_vector(increments)
    face = minimizer_face(scores)
    zero_reopenings = [
        name
        for name, value in zip(RESPONSES, scores)
        if name in REOPENINGS and value == 0
    ]
    return {
        "id": identifier,
        "increment_vector": {
            name: value for name, value in zip(RESPONSES, increments)
        },
        "complete_score_vector": {
            name: value for name, value in zip(RESPONSES, scores)
        },
        "minimum_score": min(scores),
        "minimizer_face": list(face),
        "zero_score_reopenings": zero_reopenings,
        "realizers": realizers,
    }


def compile_manifest() -> dict[str, object]:
    lines, occupancies, forbidden_points = secant_data()
    intrinsic = intrinsic_vector()
    require(intrinsic == (1, 4, 0, 0, 0), "intrinsic vector")

    intersections = rational_intersections(lines)
    require(len(intersections) == 103, "rational intersection census")
    all_integer_intersections = tuple(
        sorted(
            {
                (int(x), int(y))
                for x, y in intersections
                if x.denominator == 1 and y.denominator == 1
            }
        )
    )
    require(len(all_integer_intersections) == 27, "all integer intersection census")
    admissible_intersections = integer_intersections(lines, forbidden_points)
    require(len(admissible_intersections) == 16, "admissible integer intersection census")

    grouped: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)
    off_witness = nearest_off_secant_witness(lines, forbidden_points)
    grouped[(0, 0, 0, 0, 0)].append(
        {"kind": "off-all-secants", "witness": list(off_witness)}
    )

    for line in lines:
        vector = line_increment_vector(line, occupancies)
        witness = nearest_generic_witness(line, lines, forbidden_points)
        grouped[vector].append(
            {
                "kind": "generic-line",
                "line": list(line),
                "witness": list(witness),
            }
        )

    for point in admissible_intersections:
        grouped[increment_vector(point, lines, occupancies)].append(
            {
                "kind": "integer-intersection",
                "point": list(point),
                "incident_lines": [list(line) for line in incident_lines(point, lines)],
            }
        )

    require(len(grouped) == 15, "fifteen singleton signatures")
    records = [
        signature_record(f"S{index:02d}", vector, grouped[vector])
        for index, vector in enumerate(sorted(grouped))
    ]

    minimum_census = Counter(record["minimum_score"] for record in records)
    zero_reopening_census = Counter(
        len(record["zero_score_reopenings"]) for record in records
    )
    original_minimizer_classes = sum(
        bool({"3012", "3210"} & set(record["minimizer_face"]))
        for record in records
    )
    no_zero_classes = [
        record for record in records if not record["zero_score_reopenings"]
    ]
    require(minimum_census == Counter({0: 14, 1: 1}), "minimum-score census")
    require(len(no_zero_classes) == 1, "unique no-zero class")
    require(
        no_zero_classes[0]["complete_score_vector"]
        == {"3012": 2, "3210": 10, "2031": 1, "2310": 1, "3201": 1},
        "unique no-zero score vector",
    )
    no_zero_integer_points = sorted(
        tuple(realizer["point"])
        for realizer in no_zero_classes[0]["realizers"]
        if realizer["kind"] == "integer-intersection"
    )
    require(no_zero_integer_points == [(-1, 4), (4, -1)], "no-zero witnesses")
    require(original_minimizer_classes == 0, "original response never singleton-minimal")

    checked_points = 0
    observed_vectors = set()
    forbidden = set(forbidden_points)
    for x in range(-AUDIT_RADIUS, AUDIT_RADIUS + 1):
        for y in range(-AUDIT_RADIUS, AUDIT_RADIUS + 1):
            point = (x, y)
            if point in forbidden:
                continue
            vector = increment_vector(point, lines, occupancies)
            require(vector in grouped, f"unclassified audit vector at {point}")
            for name, expected in zip(RESPONSES, score_vector(vector)):
                require(direct_score(name, point) == expected, f"direct score mismatch {name} {point}")
            observed_vectors.add(vector)
            checked_points += 1
    require(checked_points == 10190, "audit point census")
    require(observed_vectors == set(grouped), "audit realizes every signature")

    return {
        "schema": "exact-recurrent-first-host-integer-singleton-signature-atlas/v1",
        "scope": {
            "host_id": HOST_ID,
            "responses": list(RESPONSES),
            "background": "one integer point disjoint from the five-response union",
            "coverage": "full integer lattice",
        },
        "intrinsic_score_vector": {
            name: value for name, value in zip(RESPONSES, intrinsic)
        },
        "secant_lines": [
            {
                "line": list(line),
                "increment_vector": {
                    name: value
                    for name, value in zip(RESPONSES, line_increment_vector(line, occupancies))
                },
                "generic_integer_witness": list(
                    nearest_generic_witness(line, lines, forbidden_points)
                ),
            }
            for line in lines
        ],
        "admissible_integer_intersections": [
            {
                "point": list(point),
                "incident_lines": [list(line) for line in incident_lines(point, lines)],
                "increment_vector": {
                    name: value
                    for name, value in zip(
                        RESPONSES, increment_vector(point, lines, occupancies)
                    )
                },
            }
            for point in admissible_intersections
        ],
        "signature_classes": records,
        "aggregate": {
            "distinct_secant_lines": 20,
            "distinct_rational_line_intersections": 103,
            "integer_line_intersections_including_response_points": 27,
            "excluded_response_union_points": 11,
            "admissible_integer_line_intersections": 16,
            "integer_singleton_signature_classes": 15,
            "classes_with_minimum_zero": 14,
            "classes_with_minimum_one": 1,
            "classes_with_original_response_minimizer": 0,
            "unique_no_zero_reopening_integer_points": 2,
            "audit_radius": AUDIT_RADIUS,
            "audit_integer_points_checked": checked_points,
            "zero_reopening_count_census": {
                str(key): value for key, value in sorted(zero_reopening_census.items())
            },
        },
        "critical_class": no_zero_classes[0],
        "honesty": {
            "full_integer_singleton_signature_classification_complete": 1,
            "singleton_original_response_exclusion_proved": 1,
            "singleton_zero_reopening_exception_classified": 1,
            "physical_singleton_background_coverage_proved": 0,
            "multi_point_background_classification_complete": 0,
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
    require(honesty.get("physical_singleton_background_coverage_proved") == 0, "coverage honesty")
    require(honesty.get("multi_point_background_classification_complete") == 0, "multipoint honesty")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(distinct_secant_lines=19),
        lambda item: item["aggregate"].update(distinct_rational_line_intersections=102),
        lambda item: item["aggregate"].update(admissible_integer_line_intersections=15),
        lambda item: item["aggregate"].update(integer_singleton_signature_classes=14),
        lambda item: item["aggregate"].update(classes_with_minimum_zero=13),
        lambda item: item["aggregate"].update(classes_with_original_response_minimizer=1),
        lambda item: item["signature_classes"].pop(),
        lambda item: item["critical_class"]["complete_score_vector"].update({"2031": 0}),
        lambda item: item["critical_class"]["realizers"].pop(),
        lambda item: item["secant_lines"][0]["increment_vector"].update({"2031": 99}),
        lambda item: item["honesty"].update(physical_singleton_background_coverage_proved=1),
        lambda item: item["honesty"].update(multi_point_background_classification_complete=1),
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
                "checker": "exact-recurrent-first-host-integer-singleton-signature-atlas",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
