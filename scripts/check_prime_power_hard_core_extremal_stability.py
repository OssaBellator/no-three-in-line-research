#!/usr/bin/env python3
"""Verify sharp support-line stability for the side-four hard-core energy.

For every finite legal background B, the exact upper and lower extremal defects
split into nonnegative pivot-energy and point-weight terms.  Any background not
fully supported on K_MINUS loses at least 2|B| from the global upper extreme;
any background not fully supported on K_PLUS rises at least 2|B|+3 above the
global lower extreme.  Equality mechanisms are classified.  This is finite
scalar geometry only and permanently reports all_n_proved_by_checker=0.
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
EXPECTED_MANIFEST_SHA256 = "0bddec3bea04c1e38a6b3d11919d9f1f23566e6284644f37223a7c290b4a6131"


class HardCoreStabilityError(ValueError):
    """Raised when the support-line stability theorem is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreStabilityError(message)


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
    return sum(
        LINE_WEIGHTS[line] * int(on_line(point, line))
        for line in RELEVANT_LINES
    )


def pivot_line_counts(pivot: Point, background: tuple[Point, ...]) -> Counter[Line]:
    return Counter(normalized_line(pivot, point) for point in background)


def pivot_energy(pivot: Point, background: tuple[Point, ...]) -> int:
    return sum(
        count * (count - 1) // 2
        for count in pivot_line_counts(pivot, background).values()
    )


def energy_terms(background: tuple[Point, ...]) -> dict[str, int]:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    positive = sum(pivot_energy(pivot, background) for pivot in POSITIVE_PIVOTS)
    negative = sum(pivot_energy(pivot, background) for pivot in NEGATIVE_PIVOTS)
    weight = sum(point_weight(point) for point in background)
    return {
        "positive_pivot_energy": positive,
        "negative_pivot_energy": negative,
        "point_weight_sum": weight,
        "delta": positive - negative + weight - 3,
    }


def upper_bound(size: int) -> int:
    return (size - 1) * (size + 3)


def lower_bound(size: int) -> int:
    return -(size + 1) * (size + 3)


def upper_defect_terms(background: tuple[Point, ...]) -> dict[str, int]:
    size = len(background)
    terms = energy_terms(background)
    choose2 = size * (size - 1) // 2
    output = {
        "positive_dispersion": 2 * choose2 - terms["positive_pivot_energy"],
        "negative_energy": terms["negative_pivot_energy"],
        "weight_defect": 3 * size - terms["point_weight_sum"],
    }
    output["upper_defect"] = sum(output.values())
    return output


def lower_defect_terms(background: tuple[Point, ...]) -> dict[str, int]:
    size = len(background)
    terms = energy_terms(background)
    choose2 = size * (size - 1) // 2
    output = {
        "positive_energy": terms["positive_pivot_energy"],
        "negative_dispersion": 2 * choose2 - terms["negative_pivot_energy"],
        "weight_excess": terms["point_weight_sum"] + 5 * size,
    }
    output["lower_defect"] = sum(output.values())
    return output


def upper_gap_equality(background: tuple[Point, ...]) -> bool:
    off = [point for point in background if not on_line(point, K_MINUS)]
    if len(off) != 1:
        return False
    terms = energy_terms(background)
    return point_weight(off[0]) == 1 and terms["negative_pivot_energy"] == 0


def lower_gap_equality(background: tuple[Point, ...]) -> bool:
    off = [point for point in background if not on_line(point, K_PLUS)]
    if len(off) != 1:
        return False
    terms = energy_terms(background)
    return point_weight(off[0]) == 0 and terms["positive_pivot_energy"] == 0


def exact_manifest() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "version": 1,
        "upper_defect_identity": (
            "U_m-Delta=(2*C(m,2)-E_positive)+E_negative+(3m-W)"
        ),
        "lower_defect_identity": (
            "Delta-L_m=E_positive+(2*C(m,2)-E_negative)+(W+5m)"
        ),
        "off_support_bounds": {
            "upper": "U_m-Delta>=2a(m-a+1), a=|B\\K_minus|",
            "lower": "Delta-L_m>=b(2m-2b+5), b=|B\\K_plus|",
        },
        "stability_gaps": {
            "not_K_minus": "Delta<=U_m-2m",
            "not_K_plus": "Delta>=L_m+2m+3",
        },
        "equality_mechanisms": {
            "upper_gap": (
                "one point off K_minus, off-point weight one, zero negative energy"
            ),
            "lower_gap": (
                "one point off K_plus, off-point weight zero, zero positive energy"
            ),
        },
        "claims": {
            "sharp_support_gaps": 2,
            "classified_gap_equalities": 2,
            "all_n_proved_by_checker": 0,
        },
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest must be an object")
    expected = exact_manifest()
    require(manifest == expected, "canonical stability manifest mismatch")
    require(
        expected["claims"]
        == {
            "sharp_support_gaps": 2,
            "classified_gap_equalities": 2,
            "all_n_proved_by_checker": 0,
        },
        "claims drift",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(
            expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256,
            "built-in manifest digest drift",
        )
    return copy.deepcopy(expected["claims"])


def good_points_on_line(
    line: Line,
    *,
    avoid_pivots: tuple[Point, ...],
    off_point: Point,
    limit: int,
) -> list[Point]:
    points: list[Point] = []
    for x in range(-160, 161):
        for y in range(-160, 161):
            point = (x, y)
            if point in GRID or point == off_point or not on_line(point, line):
                continue
            if any(collinear(pivot, off_point, point) for pivot in avoid_pivots):
                continue
            points.append(point)
    points.sort()
    require(len(points) >= limit, "insufficient sharpness witness points")
    return points[:limit]


def verify_sharp_witnesses() -> dict[str, int]:
    upper_off = (-1, 6)
    lower_off = (10, 10)
    require(point_weight(upper_off) == 1, "upper off-point weight drift")
    require(point_weight(lower_off) == 0, "lower off-point weight drift")
    upper_line_points = good_points_on_line(
        K_MINUS,
        avoid_pivots=NEGATIVE_PIVOTS,
        off_point=upper_off,
        limit=9,
    )
    lower_line_points = good_points_on_line(
        K_PLUS,
        avoid_pivots=POSITIVE_PIVOTS,
        off_point=lower_off,
        limit=9,
    )
    checked = 0
    for size in range(1, 10):
        upper_background = tuple([upper_off, *upper_line_points[: size - 1]])
        lower_background = tuple([lower_off, *lower_line_points[: size - 1]])
        upper_delta = energy_terms(upper_background)["delta"]
        lower_delta = energy_terms(lower_background)["delta"]
        require(
            upper_bound(size) - upper_delta == 2 * size,
            f"upper sharpness drift at m={size}",
        )
        require(
            lower_delta - lower_bound(size) == 2 * size + 3,
            f"lower sharpness drift at m={size}",
        )
        require(upper_gap_equality(upper_background), "upper equality mechanism drift")
        require(lower_gap_equality(lower_background), "lower equality mechanism drift")
        checked += 2
    return {"sharp_gap_witnesses": checked}


def verify_exhaustive_small_sets() -> dict[str, int]:
    points = [
        (x, y)
        for x in range(-2, 5)
        for y in range(-2, 5)
        if (x, y) not in GRID
    ]
    require(len(points) == 33, "small-set point census drift")
    checked = 0
    nonmaximal_upper = 0
    nonminimal_lower = 0
    upper_equalities = 0
    lower_equalities = 0
    for size in range(0, 6):
        for background in combinations(points, size):
            terms = energy_terms(background)
            delta = terms["delta"]
            upper_terms = upper_defect_terms(background)
            lower_terms = lower_defect_terms(background)
            require(
                upper_terms["upper_defect"] == upper_bound(size) - delta,
                "upper defect identity failed",
            )
            require(
                lower_terms["lower_defect"] == delta - lower_bound(size),
                "lower defect identity failed",
            )
            require(
                all(value >= 0 for key, value in upper_terms.items() if key != "upper_defect"),
                "negative upper defect component",
            )
            require(
                all(value >= 0 for key, value in lower_terms.items() if key != "lower_defect"),
                "negative lower defect component",
            )
            off_minus = sum(not on_line(point, K_MINUS) for point in background)
            off_plus = sum(not on_line(point, K_PLUS) for point in background)
            require(
                upper_terms["upper_defect"]
                >= 2 * off_minus * (size - off_minus + 1),
                "upper off-support bound failed",
            )
            require(
                lower_terms["lower_defect"]
                >= off_plus * (2 * size - 2 * off_plus + 5),
                "lower off-support bound failed",
            )
            if size and off_minus:
                require(delta <= upper_bound(size) - 2 * size, "upper stability gap failed")
                require(
                    (upper_bound(size) - delta == 2 * size)
                    == upper_gap_equality(background),
                    "upper equality classification failed",
                )
                nonmaximal_upper += 1
                upper_equalities += int(upper_gap_equality(background))
            if size and off_plus:
                require(
                    delta >= lower_bound(size) + 2 * size + 3,
                    "lower stability gap failed",
                )
                require(
                    (delta - lower_bound(size) == 2 * size + 3)
                    == lower_gap_equality(background),
                    "lower equality classification failed",
                )
                nonminimal_lower += 1
                lower_equalities += int(lower_gap_equality(background))
            checked += 1
    require(checked == 284274, "exhaustive small-set count drift")
    return {
        "exhaustive_backgrounds": checked,
        "upper_gap_backgrounds": nonmaximal_upper,
        "lower_gap_backgrounds": nonminimal_lower,
        "upper_gap_equalities": upper_equalities,
        "lower_gap_equalities": lower_equalities,
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
    add(lambda data: data.update(upper_defect_identity="U_m-Delta=E_positive"))
    add(lambda data: data["off_support_bounds"].update(upper="U_m-Delta>=a"))
    add(lambda data: data["stability_gaps"].update(not_K_minus="Delta<=U_m-m"))
    add(lambda data: data["equality_mechanisms"].update(lower_gap="unclassified"))
    add(lambda data: data["claims"].update(sharp_support_gaps=1))
    add(lambda data: data["claims"].update(all_n_proved_by_checker=1))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreStabilityError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    witnesses = verify_sharp_witnesses()
    exhaustive = verify_exhaustive_small_sets()
    rejected = mutation_tests()
    print(json.dumps({
        **claims,
        **witnesses,
        **exhaustive,
        "rejected_mutations": rejected,
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
