#!/usr/bin/env python3
"""Classify chart-safe first-host scores under local deletion restorations."""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]

HOST_ID = "s4-75b04c45c1c8eac2"
SIDE = 4
TARGET = (0, 1)
DELETIONS = ((0, 2), (2, 0))
SAFE_BACKGROUND = ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3))
RESPONSE_ORDER = ("3012", "3210", "2031", "2310", "3201", "2301")
MENU_DELETIONS = {
    "blocked": frozenset(DELETIONS),
    "restore_02": frozenset({(2, 0)}),
    "restore_20": frozenset({(0, 2)}),
    "restore_both": frozenset(),
}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(name: str) -> tuple[Point, ...]:
    require(len(name) == SIDE, f"{name}: response length")
    return tuple((row, int(name[row])) for row in range(SIDE))


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        collinear(first, second, third)
        for first, second, third in combinations(sequence, 3)
    )


def new_triple_score(response: str, background: tuple[Point, ...]) -> int:
    points = response_points(response)
    require(not set(points) & set(background), f"{response}: background overlap")
    return triple_count((*background, *points)) - triple_count(background)


def perfect_matchings(deletions: frozenset[Point]) -> tuple[str, ...]:
    forbidden = {(index, index) for index in range(SIDE)} | {TARGET} | set(deletions)
    names = []
    for permutation in permutations(range(SIDE)):
        response = tuple((row, permutation[row]) for row in range(SIDE))
        if not set(response) & forbidden:
            names.append("".join(str(value) for value in permutation))
    return tuple(sorted(names))


def subsets(points: tuple[Point, ...]) -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(points[index] for index in range(len(points)) if mask >> index & 1)
        for mask in range(1 << len(points))
    )


def point_code(point: Point) -> str:
    return f"{point[0]}{point[1]}"


def score_vector(background: tuple[Point, ...], menu: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(new_triple_score(response, background) for response in menu)


def minimizer_face(menu: tuple[str, ...], scores: tuple[int, ...]) -> tuple[str, ...]:
    minimum = min(scores)
    return tuple(response for response, score in zip(menu, scores) if score == minimum)


def restore_both_formula(background: tuple[Point, ...]) -> int:
    active = set(background)
    return (
        int((1, 1) in active)
        + int((2, 2) in active)
        + int({(0, 0), (0, 1)} <= active)
        + int({(0, 1), (1, 1)} <= active)
    )


def normalized_line(first: Point, second: Point) -> tuple[int, int, int]:
    require(first != second, "line points distinct")
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    from math import gcd

    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "line divisor")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def compile_manifest() -> dict[str, object]:
    menus = {name: perfect_matchings(deletions) for name, deletions in MENU_DELETIONS.items()}
    expected_menus = {
        "blocked": ("3012", "3210"),
        "restore_02": ("2031", "2310", "3012", "3210"),
        "restore_20": ("3012", "3201", "3210"),
        "restore_both": ("2031", "2301", "2310", "3012", "3201", "3210"),
    }
    require(menus == expected_menus, "restoration menus")

    rows = []
    single_faces: dict[str, set[tuple[str, ...]]] = {
        "restore_02": set(),
        "restore_20": set(),
    }
    expanded_classes: dict[tuple[int, ...], list[list[str]]] = {}

    for background in subsets(SAFE_BACKGROUND):
        response_scores = {
            response: new_triple_score(response, background)
            for response in RESPONSE_ORDER
        }
        require(response_scores["2301"] == restore_both_formula(background), "2301 safe formula")
        menu_records = {}
        for menu_name, menu in menus.items():
            scores = score_vector(background, menu)
            face = minimizer_face(menu, scores)
            menu_records[menu_name] = {
                "menu": list(menu),
                "scores": list(scores),
                "minimizer_face": list(face),
            }
            if menu_name in single_faces:
                single_faces[menu_name].add(face)

        expanded_vector = tuple(response_scores[response] for response in RESPONSE_ORDER)
        expanded_classes.setdefault(expanded_vector, []).append(
            [point_code(point) for point in background]
        )
        rows.append(
            {
                "background": [point_code(point) for point in background],
                "response_scores": response_scores,
                "menus": menu_records,
            }
        )

    require(single_faces["restore_02"] == {("2031", "2310")}, "restore 02 face")
    require(single_faces["restore_20"] == {("3201",)}, "restore 20 face")
    require(len(expanded_classes) == 8, "eight expanded score classes")
    class_census = sorted((list(vector), len(members)) for vector, members in expanded_classes.items())
    require(sorted(count for _, count in class_census) == [2, 2, 2, 2, 4, 4, 6, 10], "class census")

    old_union = set()
    for response in RESPONSE_ORDER[:-1]:
        points = response_points(response)
        old_union.update(
            normalized_line(first, second) for first, second in combinations(points, 2)
        )
    new_lines = {
        normalized_line(first, second)
        for first, second in combinations(response_points("2301"), 2)
    } - old_union
    require(new_lines == {(1, 1, -4), (1, 1, -2), (3, 1, -6)}, "new 2301 secant lines")

    return {
        "schema": "exact-recurrent-first-host-restoration-menu-closure/v1",
        "scope": {
            "host_id": HOST_ID,
            "deletions": ["02", "20"],
            "safe_background_universe": [point_code(point) for point in SAFE_BACKGROUND],
            "response_order": list(RESPONSE_ORDER),
        },
        "menus": {name: list(menu) for name, menu in menus.items()},
        "restore_both_2301_formula": (
            "1[11 in B]+1[22 in B]+1[{00,01} subset B]+1[{01,11} subset B]"
        ),
        "new_restore_both_secant_lines": [list(line) for line in sorted(new_lines)],
        "expanded_score_classes": [
            {"score_vector": vector, "background_count": count}
            for vector, count in class_census
        ],
        "aggregate": {
            "safe_backgrounds": len(rows),
            "single_restore_02_minimizer_faces": 1,
            "single_restore_20_minimizer_faces": 1,
            "restore_both_responses": len(menus["restore_both"]),
            "new_restore_both_response": "2301",
            "new_secant_line_coordinates": len(new_lines),
            "five_response_signature_classes": 4,
            "six_response_score_classes": len(expanded_classes),
        },
        "conclusion": {
            "single_edge_restoration_selector_congruent_on_safe_class": 1,
            "four_class_five_response_signature_closed_under_restore_both": 0,
            "operation_menu_expansion_requires_signature_refinement": 1,
            "transition_payment_congruence_proved": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "legal_restoration_operation_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
        "rows": rows,
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(safe_backgrounds=31),
        lambda item: item["aggregate"].update(six_response_score_classes=7),
        lambda item: item["aggregate"].update(new_secant_line_coordinates=2),
        lambda item: item["menus"].update(restore_both=item["menus"]["restore_both"][:-1]),
        lambda item: item["new_restore_both_secant_lines"].pop(),
        lambda item: item["expanded_score_classes"][0].update(background_count=99),
        lambda item: item["conclusion"].update(four_class_five_response_signature_closed_under_restore_both=1),
        lambda item: item["conclusion"].update(transition_payment_congruence_proved=1),
        lambda item: item["honesty"].update(legal_restoration_operation_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
        lambda item: item["rows"][0]["response_scores"].update({"2301": 99}),
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

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-restoration-menu-closure",
                **manifest["aggregate"],
                **manifest["conclusion"],
                **manifest["honesty"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
