#!/usr/bin/env python3
"""Classify canonical selector faces and gaps across first-host restoration menus."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
SIDE = 4
HOST_ID = "s4-75b04c45c1c8eac2"
TARGET = (0, 1)
SAFE = ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3))
MENU_DELETIONS = {
    "blocked": frozenset({(0, 2), (2, 0)}),
    "restore_02": frozenset({(2, 0)}),
    "restore_20": frozenset({(0, 2)}),
    "restore_both": frozenset(),
}
EXPECTED_MENUS = {
    "blocked": ("3012", "3210"),
    "restore_02": ("2031", "2310", "3012", "3210"),
    "restore_20": ("3012", "3201", "3210"),
    "restore_both": ("2031", "2301", "2310", "3012", "3201", "3210"),
}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(name: str) -> tuple[Point, ...]:
    return tuple((row, int(name[row])) for row in range(SIDE))


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def triple_count(points: Iterable[Point]) -> int:
    return sum(
        collinear(*triple)
        for triple in itertools.combinations(tuple(points), 3)
    )


def score(name: str, background: tuple[Point, ...]) -> int:
    response = response_points(name)
    require(not set(response) & set(background), f"{name}: background overlap")
    return triple_count((*background, *response)) - triple_count(background)


def matchings(deletions: frozenset[Point]) -> tuple[str, ...]:
    forbidden = {(index, index) for index in range(SIDE)} | {TARGET} | set(deletions)
    output = []
    for permutation in itertools.permutations(range(SIDE)):
        response = {(row, permutation[row]) for row in range(SIDE)}
        if not response & forbidden:
            output.append("".join(str(value) for value in permutation))
    return tuple(sorted(output))


def subsets() -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(
            SAFE[index]
            for index in range(len(SAFE))
            if mask >> index & 1
        )
        for mask in range(1 << len(SAFE))
    )


def selector_record(
    menu: tuple[str, ...],
    background: tuple[Point, ...],
) -> tuple[tuple[str, ...], str, int]:
    values = {name: score(name, background) for name in menu}
    minimum = min(values.values())
    face = tuple(name for name in menu if values[name] == minimum)
    selected = min(face)
    higher = sorted({value for value in values.values() if value > minimum})
    require(higher, "selector requires higher score")
    return face, selected, higher[0] - minimum


def compile_manifest() -> dict[str, object]:
    menus = {
        name: matchings(deletions)
        for name, deletions in MENU_DELETIONS.items()
    }
    require(menus == EXPECTED_MENUS, "restoration menus")

    backgrounds = subsets()
    menu_data: dict[str, dict[str, object]] = {}
    for menu_name, menu in menus.items():
        face_census: dict[tuple[str, ...], int] = {}
        selected_census: dict[str, int] = {}
        gap_census: dict[int, int] = {}
        for background in backgrounds:
            face, selected, gap = selector_record(menu, background)
            face_census[face] = face_census.get(face, 0) + 1
            selected_census[selected] = selected_census.get(selected, 0) + 1
            gap_census[gap] = gap_census.get(gap, 0) + 1
        menu_data[menu_name] = {
            "menu": list(menu),
            "minimizer_faces": [
                {"face": list(face), "background_count": count}
                for face, count in sorted(face_census.items())
            ],
            "selected_response_census": selected_census,
            "next_gap_census": {
                str(gap): count for gap, count in sorted(gap_census.items())
            },
        }

    require(
        menu_data["blocked"]["minimizer_faces"]
        == [{"face": ["3012"], "background_count": 32}],
        "blocked face",
    )
    require(
        menu_data["restore_02"]["minimizer_faces"]
        == [{"face": ["2031", "2310"], "background_count": 32}],
        "restore 02 face",
    )
    require(
        menu_data["restore_20"]["minimizer_faces"]
        == [{"face": ["3201"], "background_count": 32}],
        "restore 20 face",
    )
    require(
        menu_data["restore_both"]["minimizer_faces"]
        == [
            {
                "face": ["2031", "2301", "2310", "3201"],
                "background_count": 8,
            },
            {
                "face": ["2031", "2310", "3201"],
                "background_count": 24,
            },
        ],
        "restore both faces",
    )

    expected_selected = {
        "blocked": {"3012": 32},
        "restore_02": {"2031": 32},
        "restore_20": {"3201": 32},
        "restore_both": {"2031": 32},
    }
    expected_gaps = {
        "blocked": {"3": 32},
        "restore_02": {"1": 32},
        "restore_20": {"1": 32},
        "restore_both": {"1": 32},
    }
    for name in menus:
        require(
            menu_data[name]["selected_response_census"] == expected_selected[name],
            f"{name} selected",
        )
        require(
            menu_data[name]["next_gap_census"] == expected_gaps[name],
            f"{name} gap",
        )

    return {
        "schema": "exact-recurrent-first-host-restoration-selector-face/v1",
        "scope": {
            "host_id": HOST_ID,
            "safe_background_universe": [f"{x}{y}" for x, y in SAFE],
            "selection_rule": (
                "lexicographically least response in complete-score minimizer face"
            ),
        },
        "menus": menu_data,
        "aggregate": {
            "safe_backgrounds": len(backgrounds),
            "restoration_menus": len(menus),
            "total_distinct_minimizer_faces": sum(
                len(item["minimizer_faces"])
                for item in menu_data.values()
            ),
            "restore_both_minimizer_faces": len(
                menu_data["restore_both"]["minimizer_faces"]
            ),
            "restore_both_four_way_face_backgrounds": 8,
            "restore_both_three_way_face_backgrounds": 24,
            "menus_with_background_invariant_selected_response": sum(
                len(item["selected_response_census"]) == 1
                for item in menu_data.values()
            ),
            "menus_with_background_invariant_next_gap": sum(
                len(item["next_gap_census"]) == 1
                for item in menu_data.values()
            ),
        },
        "conclusion": {
            "canonical_selector_identity_congruent_on_safe_class_all_restoration_menus": 1,
            "positive_next_energy_gap_congruent_on_safe_class_all_restoration_menus": 1,
            "restore_both_minimizer_face_background_invariant": 0,
            "selector_identity_requires_ten_state_operation_signature": 0,
            "complete_transition_payment_congruence_proved": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "legal_restoration_operation_proved": 0,
            "physical_occurrence_coverage_proved": 0,
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
        lambda item: item["aggregate"].update(safe_backgrounds=31),
        lambda item: item["aggregate"].update(restoration_menus=3),
        lambda item: item["aggregate"].update(total_distinct_minimizer_faces=4),
        lambda item: item["aggregate"].update(restore_both_minimizer_faces=1),
        lambda item: item["aggregate"].update(
            restore_both_four_way_face_backgrounds=7
        ),
        lambda item: item["aggregate"].update(
            menus_with_background_invariant_selected_response=3
        ),
        lambda item: item["aggregate"].update(
            menus_with_background_invariant_next_gap=3
        ),
        lambda item: item["menus"]["restore_both"]["minimizer_faces"].pop(),
        lambda item: item["conclusion"].update(
            restore_both_minimizer_face_background_invariant=1
        ),
        lambda item: item["conclusion"].update(
            complete_transition_payment_congruence_proved=1
        ),
        lambda item: item["honesty"].update(
            legal_restoration_operation_proved=1
        ),
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
        "checker": "exact-recurrent-first-host-restoration-selector-face",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
