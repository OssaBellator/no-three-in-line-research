#!/usr/bin/env python3
"""Verify the minimal two-point affine reversal witnesses for the first host."""
from __future__ import annotations

import argparse
import copy
import json
import math
from itertools import combinations
from pathlib import Path

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
MINIMAL_RADIUS = 5


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def response_union() -> set[Point]:
    return {
        point
        for permutation in RESPONSES.values()
        for point in response_points(permutation)
    }


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


def response_secant_lines(name: str) -> tuple[Line, ...]:
    points = response_points(RESPONSES[name])
    return tuple(normalize_line(first, second) for first, second in combinations(points, 2))


def intrinsic_score(name: str) -> int:
    points = response_points(RESPONSES[name])
    return sum(
        1
        for first, second, third in combinations(points, 3)
        if on_line(third, normalize_line(first, second))
    )


INTRINSIC = {name: intrinsic_score(name) for name in RESPONSES}
SECANTS = {name: response_secant_lines(name) for name in RESPONSES}


def singleton_increment(name: str, point: Point) -> int:
    return sum(on_line(point, line) for line in SECANTS[name])


def pair_through_increment(name: str, first: Point, second: Point) -> int:
    line = normalize_line(first, second)
    return sum(on_line(point, line) for point in response_points(RESPONSES[name]))


def complete_score(name: str, background: tuple[Point, Point]) -> int:
    first, second = background
    return (
        INTRINSIC[name]
        + singleton_increment(name, first)
        + singleton_increment(name, second)
        + pair_through_increment(name, first, second)
    )


def score_vector(background: tuple[Point, Point]) -> tuple[int, ...]:
    return tuple(complete_score(name, background) for name in RESPONSES)


def minimizer_face(scores: tuple[int, ...]) -> tuple[str, ...]:
    minimum = min(scores)
    return tuple(name for name, score in zip(RESPONSES, scores) if score == minimum)


def is_strict_original_reversal(scores: tuple[int, ...]) -> bool:
    reopening_minimum = min(
        scores[list(RESPONSES).index(name)] for name in REOPENINGS
    )
    return min(scores[0], scores[1]) < reopening_minimum


def points_in_radius(radius: int) -> tuple[Point, ...]:
    forbidden = response_union()
    return tuple(
        (x, y)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        if (x, y) not in forbidden
    )


def reversal_witnesses(radius: int) -> tuple[tuple[Point, Point], ...]:
    return tuple(
        (first, second)
        for first, second in combinations(points_in_radius(radius), 2)
        if is_strict_original_reversal(score_vector((first, second)))
    )


def incidence_decomposition(background: tuple[Point, Point]) -> dict[str, object]:
    first, second = background
    pair_line = normalize_line(first, second)
    union_points = tuple(
        sorted(point for point in response_union() if on_line(point, pair_line))
    )
    return {
        "background": [list(point) for point in background],
        "pair_line": list(pair_line),
        "response_union_points_on_pair_line": [list(point) for point in union_points],
        "singleton_increments": [
            {
                "point": list(point),
                "increment_vector": {
                    name: singleton_increment(name, point) for name in RESPONSES
                },
            }
            for point in background
        ],
        "pair_through_point_vector": {
            name: pair_through_increment(name, first, second) for name in RESPONSES
        },
        "complete_score_vector": {
            name: value for name, value in zip(RESPONSES, score_vector(background))
        },
        "minimizer_face": list(minimizer_face(score_vector(background))),
    }


def compile_manifest() -> dict[str, object]:
    require(
        INTRINSIC == {"3012": 1, "3210": 4, "2031": 0, "2310": 0, "3201": 0},
        "intrinsic scores",
    )
    lower_points = points_in_radius(MINIMAL_RADIUS - 1)
    lower_pairs = math.comb(len(lower_points), 2)
    lower_witnesses = reversal_witnesses(MINIMAL_RADIUS - 1)
    require(len(lower_points) == 70, "radius-four point census")
    require(lower_pairs == 2415, "radius-four pair census")
    require(not lower_witnesses, "unexpected radius-four reversal")

    radius_points = points_in_radius(MINIMAL_RADIUS)
    radius_pairs = math.comb(len(radius_points), 2)
    witnesses = reversal_witnesses(MINIMAL_RADIUS)
    require(len(radius_points) == 110, "radius-five point census")
    require(radius_pairs == 5995, "radius-five pair census")
    require(
        witnesses
        == (
            ((-3, 5), (5, -3)),
            ((-1, 3), (5, -3)),
        ),
        "minimal reversal witness set",
    )

    records = [incidence_decomposition(witness) for witness in witnesses]
    for record in records:
        require(
            record["complete_score_vector"]
            == {"3012": 1, "3210": 4, "2031": 2, "2310": 2, "3201": 2},
            "reversal score vector",
        )
        require(record["minimizer_face"] == ["3012"], "unique original minimizer")
        require(record["pair_line"] == [1, 1, -2], "pair line")
        require(
            record["response_union_points_on_pair_line"] == [[0, 2], [2, 0]],
            "pair-line response points",
        )

    return {
        "schema": "exact-recurrent-first-host-two-point-reversal-witness/v1",
        "scope": {
            "host_id": HOST_ID,
            "responses": list(RESPONSES),
            "background": "two integer points disjoint from response union",
            "minimality_measure": "maximum absolute coordinate",
        },
        "minimal_radius": MINIMAL_RADIUS,
        "witnesses": records,
        "aggregate": {
            "radius_four_available_points": len(lower_points),
            "radius_four_background_pairs_checked": lower_pairs,
            "radius_four_strict_original_reversals": len(lower_witnesses),
            "radius_five_available_points": len(radius_points),
            "radius_five_background_pairs_checked": radius_pairs,
            "radius_five_strict_original_reversals": len(witnesses),
            "minimal_reversal_witnesses": len(witnesses),
        },
        "honesty": {
            "minimal_affine_integer_two_point_reversal_proved": 1,
            "witness_physically_realizable": 0,
            "physical_two_point_background_coverage_proved": 0,
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
    require(honesty.get("witness_physically_realizable") == 0, "realizability honesty")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item.update(minimal_radius=4),
        lambda item: item["aggregate"].update(radius_four_available_points=69),
        lambda item: item["aggregate"].update(radius_four_background_pairs_checked=2414),
        lambda item: item["aggregate"].update(radius_four_strict_original_reversals=1),
        lambda item: item["aggregate"].update(radius_five_strict_original_reversals=1),
        lambda item: item["witnesses"].pop(),
        lambda item: item["witnesses"][0]["complete_score_vector"].update({"2031": 1}),
        lambda item: item["witnesses"][0].update(minimizer_face=["2031"]),
        lambda item: item["witnesses"][0].update(pair_line=[1, 1, -3]),
        lambda item: item["honesty"].update(witness_physically_realizable=1),
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
                "checker": "exact-recurrent-first-host-two-point-reversal-witness",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
