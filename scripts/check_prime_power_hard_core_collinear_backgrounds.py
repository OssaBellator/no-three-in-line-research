#!/usr/bin/env python3
"""Verify the collinear-background normal form for the side-four hard core.

For every finite collinear outside-grid background B on a supporting line L,
the hard-core exchange delta is the pivot balance of L times C(|B|,2), plus
the four relevant-line point weights, minus three.  This yields exact pure-line
thresholds for K_MINUS, K_30, K_03 and K_PLUS and clean pivot pencils.  It is
finite scalar geometry only and permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from itertools import combinations
from typing import Any

Point = tuple[int, int]
Line = tuple[int, int, int]

GRID = {(x, y) for x in range(4) for y in range(4)}
K_MINUS: Line = (1, -1, -1)
K_PLUS: Line = (1, 1, -3)
K_30: Line = (3, 1, -3)
K_03: Line = (1, 3, -9)
RELEVANT_LINES = (K_MINUS, K_PLUS, K_30, K_03)
LINE_WEIGHTS = {K_MINUS: 3, K_PLUS: -5, K_30: 1, K_03: 1}
POSITIVE_PIVOTS: tuple[Point, Point] = ((3, 2), (1, 0))
NEGATIVE_PIVOTS: tuple[Point, Point] = ((3, 0), (1, 2))
EXPECTED_MANIFEST_SHA256 = "3e818c8ece650173676e3afaa94b0adfb65fd0185146dc4b49485131a020c99a"


class HardCoreCollinearError(ValueError):
    """Raised when the exact collinear-background theorem is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreCollinearError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def normalized_line(first: Point, second: Point) -> Line:
    require(first != second, "supporting line needs distinct points")
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "degenerate line")
    a //= divisor
    b //= divisor
    c //= divisor
    for value in (a, b, c):
        if value < 0:
            a, b, c = -a, -b, -c
            break
        if value > 0:
            break
    return a, b, c


def point_weight(point: Point) -> int:
    return sum(LINE_WEIGHTS[line] * int(on_line(point, line)) for line in RELEVANT_LINES)


def pivot_balance(line: Line) -> int:
    return (
        sum(on_line(point, line) for point in POSITIVE_PIVOTS)
        - sum(on_line(point, line) for point in NEGATIVE_PIVOTS)
    )


def pair_cross(first: Point, second: Point) -> int:
    return (
        sum(collinear(point, first, second) for point in POSITIVE_PIVOTS)
        - sum(collinear(point, first, second) for point in NEGATIVE_PIVOTS)
    )


def delta(background: tuple[Point, ...]) -> int:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    return (
        sum(pair_cross(first, second) for first, second in combinations(background, 2))
        + sum(point_weight(point) for point in background)
        - 3
    )


def collinear_delta(background: tuple[Point, ...], supporting_line: Line | None = None) -> int:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    if len(background) >= 2:
        line = normalized_line(background[0], background[1])
        require(all(on_line(point, line) for point in background), "background is not collinear")
        if supporting_line is not None:
            require(line == supporting_line, "supporting line mismatch")
    else:
        require(supporting_line is not None, "sub-two-point background needs a named line")
        line = supporting_line
        require(all(on_line(point, line) for point in background), "background misses named line")
    size = len(background)
    return pivot_balance(line) * (size * (size - 1) // 2) + sum(
        point_weight(point) for point in background
    ) - 3


def legal_line_points(line: Line, limit: int = 10) -> list[Point]:
    points: list[Point] = []
    for x in range(-120, 121):
        for y in range(-120, 121):
            point = (x, y)
            if point not in GRID and on_line(point, line):
                points.append(point)
    points.sort()
    require(len(points) >= limit, f"insufficient legal points on line {line}")
    return points[:limit]


def exact_manifest() -> dict[str, Any]:
    clean_positive: Line = (2, -1, -4)  # through P1=(3,2), no other pivot
    clean_negative: Line = (2, -1, -6)  # through N1=(3,0), no other pivot
    clean_neutral: Line = (0, 1, -10)
    payload: dict[str, Any] = {
        "version": 1,
        "pivot_balances": {
            "K_minus": pivot_balance(K_MINUS),
            "K_30": pivot_balance(K_30),
            "K_03": pivot_balance(K_03),
            "K_plus": pivot_balance(K_PLUS),
            "clean_positive": pivot_balance(clean_positive),
            "clean_negative": pivot_balance(clean_negative),
            "clean_neutral": pivot_balance(clean_neutral),
        },
        "pure_line_polynomials": {
            "K_minus": "(m-1)(m+3)",
            "K_30": "(m-2)(m+3)/2",
            "K_03": "(m-2)(m+3)/2",
            "K_plus": "-(m+1)(m+3)",
            "clean_positive": "m(m-1)/2-3",
            "clean_negative": "-m(m-1)/2-3",
            "clean_neutral": "-3",
        },
        "strict_Q4_thresholds": {
            "K_minus": 2,
            "K_30": 3,
            "K_03": 3,
            "clean_positive": 4,
            "K_plus": None,
            "clean_negative": None,
            "clean_neutral": None,
        },
        "claims": {
            "named_line_families": 7,
            "positive_threshold_families": 4,
            "all_n_proved_by_checker": 0,
        },
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest must be an object")
    expected = exact_manifest()
    require(manifest == expected, "canonical collinear manifest mismatch")
    require(
        expected["pivot_balances"]
        == {
            "K_minus": 2,
            "K_30": 1,
            "K_03": 1,
            "K_plus": -2,
            "clean_positive": 1,
            "clean_negative": -1,
            "clean_neutral": 0,
        },
        "pivot balance census drift",
    )
    require(
        expected["claims"]
        == {
            "named_line_families": 7,
            "positive_threshold_families": 4,
            "all_n_proved_by_checker": 0,
        },
        "claims drift",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256, "built-in manifest digest drift")
    return copy.deepcopy(expected["claims"])


def verify_named_line_formulas() -> dict[str, Any]:
    named = {
        "K_minus": K_MINUS,
        "K_30": K_30,
        "K_03": K_03,
        "K_plus": K_PLUS,
    }
    thresholds: dict[str, int | None] = {}
    checks = 0
    for name, line in named.items():
        points = legal_line_points(line, 8)
        first_positive: int | None = None
        for size in range(0, 8):
            background = tuple(points[:size])
            exact = delta(background)
            formula = collinear_delta(background, supporting_line=line)
            require(exact == formula, f"{name}: collinear formula mismatch at m={size}")
            if name == "K_minus":
                expected = (size - 1) * (size + 3)
            elif name in {"K_30", "K_03"}:
                expected = (size - 2) * (size + 3) // 2
            else:
                expected = -(size + 1) * (size + 3)
            require(exact == expected, f"{name}: polynomial mismatch at m={size}")
            if exact > 0 and first_positive is None:
                first_positive = size
            checks += 1
        thresholds[name] = first_positive
    require(
        thresholds == {"K_minus": 2, "K_30": 3, "K_03": 3, "K_plus": None},
        "named-line thresholds drift",
    )
    return {"named_line_formula_cases": checks, "named_line_thresholds": thresholds}


def clean_points(line: Line, limit: int) -> list[Point]:
    return [point for point in legal_line_points(line, 30) if point_weight(point) == 0][:limit]


def verify_clean_pencils() -> dict[str, Any]:
    lines = {
        "clean_positive": (2, -1, -4),
        "clean_negative": (2, -1, -6),
        "clean_neutral": (0, 1, -10),
    }
    first_positive: dict[str, int | None] = {}
    checks = 0
    for name, line in lines.items():
        points = clean_points(line, 8)
        require(len(points) >= 8, f"{name}: insufficient clean points")
        threshold: int | None = None
        for size in range(0, 8):
            background = tuple(points[:size])
            exact = delta(background)
            formula = collinear_delta(background, supporting_line=line)
            require(exact == formula, f"{name}: formula mismatch at m={size}")
            choose2 = size * (size - 1) // 2
            expected = {"clean_positive": choose2 - 3, "clean_negative": -choose2 - 3, "clean_neutral": -3}[name]
            require(exact == expected, f"{name}: polynomial mismatch at m={size}")
            if exact > 0 and threshold is None:
                threshold = size
            checks += 1
        first_positive[name] = threshold
    require(
        first_positive == {"clean_positive": 4, "clean_negative": None, "clean_neutral": None},
        "clean-pencil thresholds drift",
    )
    return {"clean_pencil_formula_cases": checks, "clean_pencil_thresholds": first_positive}


def verify_bounded_collinear_sets() -> int:
    points = [
        (x, y)
        for x in range(-5, 8)
        for y in range(-5, 8)
        if (x, y) not in GRID
    ]
    groups: dict[Line, set[Point]] = {}
    for first, second in combinations(points, 2):
        line = normalized_line(first, second)
        groups.setdefault(line, set()).update((first, second))
    checked = 0
    for line, point_set in groups.items():
        ordered = sorted(point for point in points if on_line(point, line))
        for size in range(2, min(6, len(ordered)) + 1):
            background = tuple(ordered[:size])
            require(delta(background) == collinear_delta(background), "bounded collinear identity failed")
            checked += 1
    require(checked == 7442, "bounded collinear census drift")
    return checked


def mutation_tests() -> int:
    manifest = exact_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(version=2))
    add(lambda data: data.update(manifest_sha256="0" * 64))
    add(lambda data: data["pivot_balances"].update(K_minus=1))
    add(lambda data: data["pure_line_polynomials"].update(K_30="m"))
    add(lambda data: data["strict_Q4_thresholds"].update(K_minus=1))
    add(lambda data: data["strict_Q4_thresholds"].update(K_plus=2))
    add(lambda data: data["claims"].update(named_line_families=6))
    add(lambda data: data["claims"].update(all_n_proved_by_checker=1))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreCollinearError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    named = verify_named_line_formulas()
    clean = verify_clean_pencils()
    bounded = verify_bounded_collinear_sets()
    rejected = mutation_tests()
    print(json.dumps({
        **claims,
        **named,
        **clean,
        "bounded_collinear_cases": bounded,
        "rejected_mutations": rejected,
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
