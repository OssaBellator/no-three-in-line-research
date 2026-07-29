#!/usr/bin/env python3
"""Verify the arbitrary-background pivot-line energy form for the side-four hard core.

For every finite outside-grid background B, the hard-core exchange delta equals
positive pivot-line pair energy minus negative pivot-line pair energy, plus the
four relevant-line point weights, minus three. This yields sharp cardinality
bounds and exact one-point insertion/deletion marginals. It is finite scalar
geometry only and permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from collections import Counter
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
EXPECTED_MANIFEST_SHA256 = "a88ddee378c70d2713734a836aa3c18683d6db193ebbb89d52921efa55efa4f3"


class HardCoreEnergyError(ValueError):
    """Raised when the arbitrary-background energy theorem is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreEnergyError(message)


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
    require(first != second, "line requires distinct points")
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


def pair_cross(first: Point, second: Point) -> int:
    return (
        sum(collinear(point, first, second) for point in POSITIVE_PIVOTS)
        - sum(collinear(point, first, second) for point in NEGATIVE_PIVOTS)
    )


def direct_delta(background: tuple[Point, ...]) -> int:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    return (
        sum(pair_cross(first, second) for first, second in combinations(background, 2))
        + sum(point_weight(point) for point in background)
        - 3
    )


def pivot_line_counts(pivot: Point, background: tuple[Point, ...]) -> Counter[Line]:
    return Counter(normalized_line(pivot, point) for point in background)


def pivot_energy(pivot: Point, background: tuple[Point, ...]) -> int:
    return sum(count * (count - 1) // 2 for count in pivot_line_counts(pivot, background).values())


def energy_terms(background: tuple[Point, ...]) -> dict[str, int]:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    positive = sum(pivot_energy(pivot, background) for pivot in POSITIVE_PIVOTS)
    negative = sum(pivot_energy(pivot, background) for pivot in NEGATIVE_PIVOTS)
    weights = sum(point_weight(point) for point in background)
    return {
        "positive_pivot_energy": positive,
        "negative_pivot_energy": negative,
        "point_weight_sum": weights,
        "delta": positive - negative + weights - 3,
    }


def marginal(background: tuple[Point, ...], point: Point) -> int:
    require(point not in background, "marginal point already present")
    require(point not in GRID, "marginal point must avoid response grid")
    return point_weight(point) + sum(pair_cross(point, other) for other in background)


def lower_bound(size: int) -> int:
    return -(size + 1) * (size + 3)


def upper_bound(size: int) -> int:
    return (size - 1) * (size + 3)


def exact_manifest() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "version": 1,
        "pivots": {
            "positive": [list(point) for point in POSITIVE_PIVOTS],
            "negative": [list(point) for point in NEGATIVE_PIVOTS],
        },
        "energy_identity": "Delta=E_positive-E_negative+W-3",
        "integer_selector": "Q4 iff E_positive+W>=E_negative+4",
        "marginal_identity": "Delta(B union {x})-Delta(B)=omega(x)+sum_y chi(x,y)",
        "cardinality_bounds": {
            "lower": "-(m+1)(m+3)",
            "upper": "(m-1)(m+3)",
            "lower_equality_support": "K_plus",
            "upper_equality_support": "K_minus",
        },
        "claims": {
            "positive_pivots": 2,
            "negative_pivots": 2,
            "sharp_cardinality_extremes": 2,
            "all_n_proved_by_checker": 0,
        },
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest must be an object")
    expected = exact_manifest()
    require(manifest == expected, "canonical energy manifest mismatch")
    require(
        expected["claims"]
        == {
            "positive_pivots": 2,
            "negative_pivots": 2,
            "sharp_cardinality_extremes": 2,
            "all_n_proved_by_checker": 0,
        },
        "claims drift",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256, "built-in manifest digest drift")
    return copy.deepcopy(expected["claims"])


def legal_line_points(line: Line, limit: int) -> list[Point]:
    output = [
        (x, y)
        for x in range(-80, 81)
        for y in range(-80, 81)
        if (x, y) not in GRID and on_line((x, y), line)
    ]
    output.sort()
    require(len(output) >= limit, f"insufficient legal points on line {line}")
    return output[:limit]


def verify_extremes() -> dict[str, int]:
    minus_points = legal_line_points(K_MINUS, 9)
    plus_points = legal_line_points(K_PLUS, 9)
    checked = 0
    for size in range(0, 9):
        upper_background = tuple(minus_points[:size])
        lower_background = tuple(plus_points[:size])
        require(direct_delta(upper_background) == upper_bound(size), f"upper extreme drift at m={size}")
        require(direct_delta(lower_background) == lower_bound(size), f"lower extreme drift at m={size}")
        require(energy_terms(upper_background)["delta"] == upper_bound(size), "upper energy drift")
        require(energy_terms(lower_background)["delta"] == lower_bound(size), "lower energy drift")
        checked += 2
    return {"extreme_formula_cases": checked}


def verify_exhaustive_small_sets() -> dict[str, int]:
    points = [
        (x, y)
        for x in range(-2, 5)
        for y in range(-2, 5)
        if (x, y) not in GRID
    ]
    require(len(points) == 33, "small-set point census drift")
    checked = 0
    upper_equalities = 0
    lower_equalities = 0
    marginal_checks = 0
    q4_cases = 0
    for size in range(0, 6):
        for background in combinations(points, size):
            direct = direct_delta(background)
            terms = energy_terms(background)
            require(direct == terms["delta"], f"energy identity failed: {background}")
            require(lower_bound(size) <= direct <= upper_bound(size), f"cardinality bound failed: {background}")
            require(
                (direct > 0)
                == (
                    terms["positive_pivot_energy"] + terms["point_weight_sum"]
                    >= terms["negative_pivot_energy"] + 4
                ),
                f"integer selector failed: {background}",
            )
            if direct == upper_bound(size):
                upper_equalities += 1
                require(size == 0 or all(on_line(point, K_MINUS) for point in background), "false upper equality")
            if direct == lower_bound(size):
                lower_equalities += 1
                require(size == 0 or all(on_line(point, K_PLUS) for point in background), "false lower equality")
            if size:
                previous = background[:-1]
                point = background[-1]
                require(direct - direct_delta(previous) == marginal(previous, point), "marginal identity failed")
                marginal_checks += 1
            q4_cases += int(direct > 0)
            checked += 1
    require(checked == 284274, "exhaustive small-set count drift")
    return {
        "exhaustive_backgrounds": checked,
        "marginal_checks": marginal_checks,
        "upper_equality_cases": upper_equalities,
        "lower_equality_cases": lower_equalities,
        "strict_Q4_cases": q4_cases,
    }


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
    add(lambda data: data["pivots"]["positive"].pop())
    add(lambda data: data.update(energy_identity="Delta=E_positive+E_negative+W-3"))
    add(lambda data: data["cardinality_bounds"].update(upper="m(m+1)"))
    add(lambda data: data["cardinality_bounds"].update(lower_equality_support="K_minus"))
    add(lambda data: data["claims"].update(sharp_cardinality_extremes=1))
    add(lambda data: data["claims"].update(all_n_proved_by_checker=1))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreEnergyError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    extremes = verify_extremes()
    exhaustive = verify_exhaustive_small_sets()
    rejected = mutation_tests()
    print(json.dumps({
        **claims,
        **extremes,
        **exhaustive,
        "rejected_mutations": rejected,
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
