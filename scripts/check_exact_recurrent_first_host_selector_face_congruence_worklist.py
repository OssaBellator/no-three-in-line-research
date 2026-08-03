#!/usr/bin/env python3
"""Compile the exact minimizer-face congruence worklist for the first host."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
SIDE = 4
HOST_ID = "s4-75b04c45c1c8eac2"
SAFE = ((0, 0), (0, 1), (1, 1), (2, 2), (3, 3))
RESPONSES = ("3012", "3210", "2031", "2310", "3201", "2301")
MENUS = {
    "restore_02": ("2031", "2310", "3012", "3210"),
    "restore_both": ("2031", "2301", "2310", "3012", "3201", "3210"),
}
SELECTOR_PATH = Path("data/exact_recurrent_first_host_selector_rule_compatibility.json")
CLOSURE_PATH = Path("data/exact_recurrent_first_host_restoration_menu_closure.json")
EVIDENCE_FIELDS = (
    "physical_occurrence_domain_ref",
    "legal_menu_state_ref",
    "operation_signature_domain_ref",
    "common_owner_ref",
    "operation_congruence_ref",
    "child_row_congruence_ref",
    "payment_congruence_ref",
    "closure_route_congruence_ref",
    "realization_status",
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def load_json(root: Path, relative: Path) -> dict[str, Any]:
    path = root / relative
    require(path.is_file(), f"missing input: {relative}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"object required: {relative}")
    return value


def response_points(name: str) -> tuple[Point, ...]:
    require(len(name) == SIDE and name.isdigit(), f"invalid response: {name}")
    return tuple((row, int(name[row])) for row in range(SIDE))


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def triple_count(points: Iterable[Point]) -> int:
    return sum(collinear(*triple) for triple in itertools.combinations(tuple(points), 3))


def score(name: str, background: tuple[Point, ...]) -> int:
    response = response_points(name)
    require(not set(response) & set(background), f"{name}: background overlap")
    return triple_count((*background, *response)) - triple_count(background)


def operation_signature(background: tuple[Point, ...]) -> tuple[int, int, int, int]:
    active = set(background)
    return (
        int({(0, 0), (0, 1)} <= active),
        int({(0, 1), (1, 1)} <= active),
        int((1, 1) in active),
        int((2, 2) in active),
    )


def backgrounds() -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(SAFE[index] for index in range(len(SAFE)) if mask >> index & 1)
        for mask in range(1 << len(SAFE))
    )


def minimizer_face(menu: tuple[str, ...], background: tuple[Point, ...]) -> tuple[str, ...]:
    values = {name: score(name, background) for name in menu}
    minimum = min(values.values())
    return tuple(name for name in menu if values[name] == minimum)


def compile_manifest(root: Path) -> dict[str, Any]:
    selector = load_json(root, SELECTOR_PATH)
    closure = load_json(root, CLOSURE_PATH)
    require(
        selector.get("schema") == "exact-recurrent-first-host-selector-rule-compatibility/v1",
        "selector schema",
    )
    require(selector.get("host_id") == HOST_ID, "selector host")
    boundary = selector.get("source_boundary", {})
    require(boundary.get("restore_02_selector_requires_tie_break") == 1, "restore 02 tie")
    require(boundary.get("restore_both_selector_requires_tie_break") == 1, "restore both tie")
    require(boundary.get("face_congruence_substitute_proved") == 0, "face substitute honesty")
    require(
        closure.get("schema") == "exact-recurrent-first-host-restoration-menu-closure/v2",
        "closure schema",
    )
    require(closure.get("scope", {}).get("host_id") == HOST_ID, "closure host")
    require(
        closure.get("aggregate", {}).get("operation_aware_signature_classes") == 10,
        "ten operation signatures",
    )
    require(
        closure.get("conclusion", {}).get("transition_payment_congruence_proved") == 0,
        "payment honesty",
    )

    signature_counts: dict[tuple[int, int, int, int], int] = {}
    grouped: dict[
        tuple[str, tuple[int, int, int, int], tuple[str, ...], str],
        int,
    ] = {}
    raw_comparisons = 0

    for background in backgrounds():
        signature = operation_signature(background)
        signature_counts[signature] = signature_counts.get(signature, 0) + 1
        for menu_name, menu in MENUS.items():
            face = minimizer_face(menu, background)
            require(len(face) > 1, f"{menu_name}: tied face required")
            anchor = min(face)
            grouped[(menu_name, signature, face, anchor)] = (
                grouped.get((menu_name, signature, face, anchor), 0) + 1
            )
            raw_comparisons += len(face) - 1

    expected_signature_counts = {
        (0, 0, 0, 0): 6,
        (0, 0, 0, 1): 6,
        (0, 0, 1, 0): 4,
        (0, 0, 1, 1): 4,
        (0, 1, 1, 0): 2,
        (0, 1, 1, 1): 2,
        (1, 0, 0, 0): 2,
        (1, 0, 0, 1): 2,
        (1, 1, 1, 0): 2,
        (1, 1, 1, 1): 2,
    }
    require(signature_counts == expected_signature_counts, "signature census")
    require(raw_comparisons == 104, "raw comparison count")

    cells: list[dict[str, Any]] = []
    pair_type_signature_counts: dict[str, int] = {}
    pair_type_raw_counts: dict[str, int] = {}
    menu_pair_domains: dict[tuple[str, str], dict[str, int]] = {}
    total_obligations = 0

    for (menu_name, signature, face, anchor), count in sorted(grouped.items()):
        obligations = []
        for other in face:
            if other == anchor:
                continue
            pair = f"{anchor}~{other}"
            obligations.append(
                {
                    "response_pair": [anchor, other],
                    "evidence": {field: None for field in EVIDENCE_FIELDS},
                    "evidence_fields_populated": 0,
                    "congruence_accepted": 0,
                }
            )
            total_obligations += 1
            pair_type_signature_counts[pair] = pair_type_signature_counts.get(pair, 0) + 1
            pair_type_raw_counts[pair] = pair_type_raw_counts.get(pair, 0) + count
            domain = menu_pair_domains.setdefault(
                (menu_name, pair), {"signature_classes": 0, "background_cases": 0}
            )
            domain["signature_classes"] += 1
            domain["background_cases"] += count
        cells.append(
            {
                "menu": menu_name,
                "operation_signature": list(signature),
                "background_count": count,
                "minimizer_face": list(face),
                "anchor_response": anchor,
                "basis_obligations": obligations,
                "basis_obligation_count": len(obligations),
            }
        )

    require(len(cells) == 20, "context/signature cell count")
    require(total_obligations == 32, "signature obligation count")
    require(
        pair_type_signature_counts
        == {"2031~2301": 2, "2031~2310": 20, "2031~3201": 10},
        "pair signature census",
    )
    require(
        pair_type_raw_counts
        == {"2031~2301": 8, "2031~2310": 64, "2031~3201": 32},
        "pair raw census",
    )
    require(len(menu_pair_domains) == 4, "menu-parametric theorem domains")

    four_way_classes = sum(len(cell["minimizer_face"]) == 4 for cell in cells)
    three_way_classes = sum(len(cell["minimizer_face"]) == 3 for cell in cells)
    restore_02_classes = sum(cell["menu"] == "restore_02" for cell in cells)
    require(four_way_classes == 2, "four-way classes")
    require(three_way_classes == 8, "three-way classes")
    require(restore_02_classes == 10, "restore 02 classes")

    return {
        "schema": "exact-recurrent-first-host-selector-face-congruence-worklist/v1",
        "host_id": HOST_ID,
        "sources": {
            "selector_rule_compatibility": str(SELECTOR_PATH),
            "restoration_menu_closure": str(CLOSURE_PATH),
        },
        "basis_rule": {
            "anchor": "lexicographically least member of each complete-score minimizer face",
            "transitive_basis": (
                "compare the anchor with every other face member; equality of operation, "
                "child-row, payment and closure-route behaviour is then sufficient for "
                "face-wide interchangeability"
            ),
            "signature_scope": (
                "the four-coordinate operation signature compresses the enumerated safe "
                "background worklist only; it is not assumed to determine physical behaviour"
            ),
        },
        "evidence_contract": {
            "fields": list(EVIDENCE_FIELDS),
            "field_count": len(EVIDENCE_FIELDS),
            "acceptance_rule": (
                "one signature-level obligation is accepted only when all evidence fields "
                "are populated for the same physical occurrence domain, legal menu state, "
                "persistent owner and response pair"
            ),
        },
        "cells": cells,
        "pair_type_census": [
            {
                "response_pair": pair.split("~"),
                "signature_obligations": pair_type_signature_counts[pair],
                "raw_background_comparisons": pair_type_raw_counts[pair],
            }
            for pair in sorted(pair_type_signature_counts)
        ],
        "menu_parametric_domains": [
            {
                "menu": menu,
                "response_pair": pair.split("~"),
                **counts,
                "uniform_theorem_imported": 0,
            }
            for (menu, pair), counts in sorted(menu_pair_domains.items())
        ],
        "aggregate": {
            "safe_backgrounds": 32,
            "tied_restoration_menus": 2,
            "raw_face_congruence_comparisons": raw_comparisons,
            "menu_signature_cells": len(cells),
            "signature_pair_obligations": total_obligations,
            "unique_response_pair_types": len(pair_type_signature_counts),
            "menu_parametric_pair_theorem_domains": len(menu_pair_domains),
            "cross_menu_pair_theorem_types": len(pair_type_signature_counts),
            "restore_02_signature_classes": restore_02_classes,
            "restore_both_signature_classes": len(cells) - restore_02_classes,
            "restore_both_four_way_signature_classes": four_way_classes,
            "restore_both_three_way_signature_classes": three_way_classes,
            "evidence_fields_per_signature_obligation": len(EVIDENCE_FIELDS),
            "total_signature_evidence_slots": total_obligations * len(EVIDENCE_FIELDS),
            "populated_signature_evidence_slots": 0,
            "accepted_signature_obligations": 0,
            "imported_menu_parametric_pair_theorems": 0,
            "imported_cross_menu_pair_theorems": 0,
        },
        "source_boundary": {
            "formal_face_basis_complete_on_safe_class": 1,
            "operation_signature_physically_complete": 0,
            "face_wide_operation_congruence_proved": 0,
            "face_wide_child_row_congruence_proved": 0,
            "face_wide_payment_congruence_proved": 0,
            "face_wide_closure_route_congruence_proved": 0,
            "selector_tie_break_substitution_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "legal_restoration_operation_proved": 0,
            "persistent_owner_identity_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(root: Path, value: dict[str, Any]) -> None:
    require(value == compile_manifest(root), "manifest differs from deterministic compiler")


def mutation_audit(root: Path, expected: dict[str, Any]) -> int:
    candidates = []

    def add(mutator) -> None:
        item = copy.deepcopy(expected)
        mutator(item)
        candidates.append(item)

    add(lambda x: x["aggregate"].__setitem__("raw_face_congruence_comparisons", 103))
    add(lambda x: x["aggregate"].__setitem__("signature_pair_obligations", 31))
    add(lambda x: x["aggregate"].__setitem__("menu_signature_cells", 19))
    add(lambda x: x["aggregate"].__setitem__("unique_response_pair_types", 2))
    add(lambda x: x["aggregate"].__setitem__("menu_parametric_pair_theorem_domains", 3))
    add(lambda x: x["aggregate"].__setitem__("restore_both_four_way_signature_classes", 1))
    add(lambda x: x["aggregate"].__setitem__("populated_signature_evidence_slots", 1))
    add(lambda x: x["aggregate"].__setitem__("accepted_signature_obligations", 1))
    add(lambda x: x["cells"][0]["basis_obligations"][0].__setitem__("congruence_accepted", 1))
    add(lambda x: x["cells"][10]["minimizer_face"].remove("2301"))
    add(lambda x: x["pair_type_census"].pop())
    add(lambda x: x["menu_parametric_domains"][0].__setitem__("uniform_theorem_imported", 1))
    add(lambda x: x["source_boundary"].__setitem__("operation_signature_physically_complete", 1))
    add(lambda x: x["source_boundary"].__setitem__("selector_tie_break_substitution_allowed", 1))
    add(lambda x: x["honesty"].__setitem__("persistent_owner_identity_proved", 1))
    add(lambda x: x["honesty"].__setitem__("all_n_proved_by_checker", 1))

    rejected = 0
    for candidate in candidates:
        try:
            validate_manifest(root, candidate)
        except AuditError:
            rejected += 1
    require(rejected == len(candidates), "mutation audit")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    manifest = compile_manifest(args.root)
    rejected = mutation_audit(args.root, manifest)
    if args.check:
        validate_manifest(args.root, json.loads(args.check.read_text(encoding="utf-8")))
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-selector-face-congruence-worklist",
                **manifest["aggregate"],
                **manifest["source_boundary"],
                **manifest["honesty"],
                "mutation_corruptions_rejected": rejected,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
