#!/usr/bin/env python3
"""Classify chart-safe first-host scores under local deletion restorations."""
from __future__ import annotations

import argparse
import copy
import json
import math
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
HOST_ID = "s4-75b04c45c1c8eac2"
SIDE = 4
TARGET = (0, 1)
DELETIONS = ((0, 2), (2, 0))
SAFE = ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3))
RESPONSES = ("3012", "3210", "2031", "2310", "3201", "2301")
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
    return tuple((row, int(name[row])) for row in range(SIDE))


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def triple_count(points: Iterable[Point]) -> int:
    return sum(collinear(*triple) for triple in combinations(tuple(points), 3))


def score(name: str, background: tuple[Point, ...]) -> int:
    response = response_points(name)
    require(not set(response) & set(background), f"{name}: background overlap")
    return triple_count((*background, *response)) - triple_count(background)


def matchings(deletions: frozenset[Point]) -> tuple[str, ...]:
    forbidden = {(i, i) for i in range(SIDE)} | {TARGET} | set(deletions)
    output = []
    for permutation in permutations(range(SIDE)):
        response = {(row, permutation[row]) for row in range(SIDE)}
        if not response & forbidden:
            output.append("".join(str(value) for value in permutation))
    return tuple(sorted(output))


def subsets() -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(SAFE[index] for index in range(len(SAFE)) if mask >> index & 1)
        for mask in range(1 << len(SAFE))
    )


def line(first: Point, second: Point) -> tuple[int, int, int]:
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "line divisor")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def face(menu: tuple[str, ...], background: tuple[Point, ...]) -> tuple[str, ...]:
    values = tuple(score(name, background) for name in menu)
    minimum = min(values)
    return tuple(name for name, value in zip(menu, values) if value == minimum)


def operation_signature(background: tuple[Point, ...]) -> tuple[int, int, int, int]:
    active = set(background)
    return (
        int({(0, 0), (0, 1)} <= active),
        int({(0, 1), (1, 1)} <= active),
        int((1, 1) in active),
        int((2, 2) in active),
    )


def score_2301_formula(background: tuple[Point, ...]) -> int:
    a, b, u, v = operation_signature(background)
    return a + b + u + v


def compile_manifest() -> dict[str, object]:
    menus = {name: matchings(deletions) for name, deletions in MENU_DELETIONS.items()}
    require(
        menus
        == {
            "blocked": ("3012", "3210"),
            "restore_02": ("2031", "2310", "3012", "3210"),
            "restore_20": ("3012", "3201", "3210"),
            "restore_both": ("2031", "2301", "2310", "3012", "3201", "3210"),
        },
        "restoration menus",
    )

    restore_02_faces = set()
    restore_20_faces = set()
    score_classes: dict[tuple[int, ...], int] = {}
    signature_classes: dict[tuple[int, int, int, int], int] = {}
    score_to_signatures: dict[tuple[int, ...], set[tuple[int, int, int, int]]] = {}
    backgrounds = subsets()

    for background in backgrounds:
        require(score("2301", background) == score_2301_formula(background), "2301 formula")
        restore_02_faces.add(face(menus["restore_02"], background))
        restore_20_faces.add(face(menus["restore_20"], background))
        vector = tuple(score(name, background) for name in RESPONSES)
        signature = operation_signature(background)
        score_classes[vector] = score_classes.get(vector, 0) + 1
        signature_classes[signature] = signature_classes.get(signature, 0) + 1
        score_to_signatures.setdefault(vector, set()).add(signature)

    require(restore_02_faces == {("2031", "2310")}, "restore 02 face")
    require(restore_20_faces == {("3201",)}, "restore 20 face")
    require(len(score_classes) == 8, "expanded score class count")
    require(sorted(score_classes.values()) == [2, 2, 2, 2, 4, 4, 6, 10], "score census")
    require(len(signature_classes) == 10, "operation signature class count")
    require(sorted(signature_classes.values()) == [2, 2, 2, 2, 2, 2, 4, 4, 6, 6], "signature census")

    collisions = {
        vector: signatures
        for vector, signatures in score_to_signatures.items()
        if len(signatures) > 1
    }
    require(
        collisions
        == {
            (1, 4, 0, 0, 0, 1): {(0, 0, 0, 1), (0, 0, 1, 0)},
            (2, 5, 1, 1, 1, 2): {(0, 1, 1, 0), (1, 0, 0, 1)},
        },
        "operation score collisions",
    )

    old_lines = set()
    for name in RESPONSES[:-1]:
        old_lines.update(line(a, b) for a, b in combinations(response_points(name), 2))
    new_lines = {
        line(a, b) for a, b in combinations(response_points("2301"), 2)
    } - old_lines
    require(new_lines == {(1, 1, -4), (1, 1, -2), (3, 1, -6)}, "new secants")

    return {
        "schema": "exact-recurrent-first-host-restoration-menu-closure/v2",
        "scope": {
            "host_id": HOST_ID,
            "deletions": ["02", "20"],
            "safe_background_universe": [f"{x}{y}" for x, y in SAFE],
            "response_order": list(RESPONSES),
        },
        "menus": {name: list(menu) for name, menu in menus.items()},
        "operation_signature": {
            "coordinates": [
                "a=1[{00,01} subset B]",
                "b=1[{01,11} subset B]",
                "u=1[11 in B]",
                "v=1[22 in B]",
            ],
            "classes": [
                {"signature": list(signature), "background_count": count}
                for signature, count in sorted(signature_classes.items())
            ],
        },
        "restore_both_2301_formula": "score(2301;B)=a+b+u+v",
        "new_restore_both_secant_lines": [list(item) for item in sorted(new_lines)],
        "expanded_score_classes": [
            {"score_vector": list(vector), "background_count": count}
            for vector, count in sorted(score_classes.items())
        ],
        "score_collisions": [
            {
                "score_vector": list(vector),
                "operation_signatures": [list(signature) for signature in sorted(signatures)],
            }
            for vector, signatures in sorted(collisions.items())
        ],
        "aggregate": {
            "safe_backgrounds": len(backgrounds),
            "single_restore_02_minimizer_faces": len(restore_02_faces),
            "single_restore_20_minimizer_faces": len(restore_20_faces),
            "restore_both_responses": len(menus["restore_both"]),
            "new_restore_both_response": "2301",
            "new_secant_line_coordinates": len(new_lines),
            "five_response_signature_classes": 4,
            "six_response_score_classes": len(score_classes),
            "operation_aware_signature_classes": len(signature_classes),
            "six_response_score_collision_classes": len(collisions),
        },
        "conclusion": {
            "single_edge_restoration_selector_congruent_on_safe_class": 1,
            "four_class_five_response_signature_closed_under_restore_both": 0,
            "eight_class_six_response_score_quotient_injective_on_operation_signature": 0,
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
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(safe_backgrounds=31),
        lambda item: item["aggregate"].update(six_response_score_classes=7),
        lambda item: item["aggregate"].update(operation_aware_signature_classes=9),
        lambda item: item["aggregate"].update(six_response_score_collision_classes=1),
        lambda item: item["aggregate"].update(new_secant_line_coordinates=2),
        lambda item: item["menus"].update(restore_both=item["menus"]["restore_both"][:-1]),
        lambda item: item["new_restore_both_secant_lines"].pop(),
        lambda item: item["operation_signature"]["classes"][0].update(background_count=99),
        lambda item: item["score_collisions"].pop(),
        lambda item: item["conclusion"].update(eight_class_six_response_score_quotient_injective_on_operation_signature=1),
        lambda item: item["conclusion"].update(transition_payment_congruence_proved=1),
        lambda item: item["honesty"].update(legal_restoration_operation_proved=1),
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
        arguments.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
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
