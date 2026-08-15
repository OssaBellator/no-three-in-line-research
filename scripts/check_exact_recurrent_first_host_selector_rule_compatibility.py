#!/usr/bin/env python3
"""Audit compatibility of intrinsic selected provenance and complete-score restoration selectors."""
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
SELECTED_PATH = Path("data/exact_recurrent_side_four_selected_provenance_projection.json")
RESTORATION_PATH = Path("data/exact_recurrent_first_host_restoration_selector_face.json")
REGISTRY_DOC = Path("docs/555-prime-power-installed-operation-registry-1166.md")
ANCESTRY_DOC = Path("docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md")

EXPECTED_MENUS = {
    "blocked": ("3012", "3210"),
    "restore_02": ("2031", "2310", "3012", "3210"),
    "restore_20": ("3012", "3201", "3210"),
    "restore_both": ("2031", "2301", "2310", "3012", "3201", "3210"),
}
SOURCE_RULE = "minimum triple count then lexicographically least response permutation"
COMPLETE_RULE = "lexicographically least response in complete-score minimizer face"

RESTORED_IMPORT_FIELDS = (
    "physical_occurrence_ref",
    "legal_menu_state_ref",
    "response_family_ref",
    "score_semantics_ref",
    "selector_rule_ref",
    "scheduler_operation_ref",
    "child_payment_congruence_ref",
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
    value = json.loads(path.read_text())
    require(isinstance(value, dict), f"object required: {relative}")
    return value


def response_points(name: str) -> tuple[Point, ...]:
    require(len(name) == SIDE and name.isdigit(), f"invalid response {name}")
    return tuple((row, int(name[row])) for row in range(SIDE))


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def triple_count(points: Iterable[Point]) -> int:
    return sum(collinear(*triple) for triple in itertools.combinations(tuple(points), 3))


def intrinsic_record(menu: tuple[str, ...]) -> tuple[list[str], str, int]:
    values = {name: triple_count(response_points(name)) for name in menu}
    minimum = min(values.values())
    face = sorted(name for name, value in values.items() if value == minimum)
    selected = min(face)
    higher = sorted({value for value in values.values() if value > minimum})
    require(higher, "higher intrinsic level required")
    return face, selected, higher[0] - minimum


def complete_face_case_count(menu_data: dict[str, Any], face: list[str]) -> int:
    return sum(
        row["background_count"]
        for row in menu_data["minimizer_faces"]
        if row["face"] == face
    )


def compile_manifest(root: Path) -> dict[str, Any]:
    selected = load_json(root, SELECTED_PATH)
    restoration = load_json(root, RESTORATION_PATH)

    require(selected.get("schema") == "exact-recurrent-side-four-selected-provenance-projection/v1", "selected schema")
    require(selected.get("source", {}).get("selection_rule") == SOURCE_RULE, "selected rule")
    require(restoration.get("schema") == "exact-recurrent-first-host-restoration-selector-face/v1", "restoration schema")
    require(restoration.get("scope", {}).get("host_id") == HOST_ID, "restoration host")
    require(restoration.get("scope", {}).get("selection_rule") == COMPLETE_RULE, "complete rule")

    first = next(
        (row for row in selected.get("residual_hosts", []) if row.get("upstream_id") == HOST_ID),
        None,
    )
    require(first is not None, "first host selected provenance")
    require(
        {
            "selector": first.get("selector"),
            "minimizer_face": first.get("minimizer_face"),
            "minimum_energy": first.get("minimum_energy"),
            "next_energy_gap": first.get("next_energy_gap"),
        }
        == {
            "selector": "3012",
            "minimizer_face": ["3012"],
            "minimum_energy": 1,
            "next_energy_gap": 3,
        },
        "first-host selected provenance",
    )

    menus = restoration.get("menus")
    require(isinstance(menus, dict) and set(menus) == set(EXPECTED_MENUS), "menu bank")

    registry_text = (root / REGISTRY_DOC).read_text()
    ancestry_text = (root / ANCESTRY_DOC).read_text()
    registry_markers = (
        "Two scheduler operations select strict responses only after a complete kernel or exact zero-response/blocker alternative is established.",
        "Installed-bank exhaustiveness applies only to the declared 1166-kind registry.",
    )
    ancestry_markers = (
        "Ties retain an exact minimizer face and selector switches require an explicit threshold crossing.",
        "owner_fate_rows_populated_all_recurrent_states = 0",
    )
    for marker in registry_markers:
        require(marker in registry_text, f"registry marker: {marker}")
    for marker in ancestry_markers:
        require(marker in ancestry_text, f"ancestry marker: {marker}")

    rows = []
    selected_agreement = gap_agreement = face_agreement = 0
    unique_complete = tie_break_cases = source_authorized = 0

    for menu_name in ("blocked", "restore_02", "restore_20", "restore_both"):
        data = menus[menu_name]
        menu = tuple(data["menu"])
        require(menu == EXPECTED_MENUS[menu_name], f"menu order: {menu_name}")
        intrinsic_face, intrinsic_selected, intrinsic_gap = intrinsic_record(menu)
        complete_selected_census = data["selected_response_census"]
        complete_gap_census = data["next_gap_census"]
        require(len(complete_selected_census) == 1, f"selected invariant: {menu_name}")
        require(len(complete_gap_census) == 1, f"gap invariant: {menu_name}")
        complete_selected = next(iter(complete_selected_census))
        complete_gap = int(next(iter(complete_gap_census)))
        cases = sum(row["background_count"] for row in data["minimizer_faces"])
        require(cases == 32, f"background cases: {menu_name}")

        face_match_cases = complete_face_case_count(data, intrinsic_face)
        selected_match_cases = cases if intrinsic_selected == complete_selected else 0
        gap_match_cases = cases if intrinsic_gap == complete_gap else 0
        unique_cases = sum(
            row["background_count"]
            for row in data["minimizer_faces"]
            if len(row["face"]) == 1
        )
        tied_cases = cases - unique_cases
        authorized = cases if menu_name == "blocked" else 0

        selected_agreement += selected_match_cases
        gap_agreement += gap_match_cases
        face_agreement += face_match_cases
        unique_complete += unique_cases
        tie_break_cases += tied_cases
        source_authorized += authorized

        rows.append(
            {
                "menu": menu_name,
                "responses": list(menu),
                "intrinsic_minimizer_face": intrinsic_face,
                "intrinsic_selected_response": intrinsic_selected,
                "intrinsic_next_gap": intrinsic_gap,
                "complete_minimizer_faces": data["minimizer_faces"],
                "complete_selected_response": complete_selected,
                "complete_next_gap": complete_gap,
                "menu_background_cases": cases,
                "selected_identity_agreement_cases": selected_match_cases,
                "next_gap_agreement_cases": gap_match_cases,
                "minimizer_face_agreement_cases": face_match_cases,
                "minimizer_face_disagreement_cases": cases - face_match_cases,
                "complete_unique_minimizer_cases": unique_cases,
                "complete_tie_break_dependent_cases": tied_cases,
                "source_rule_directly_authorized_cases": authorized,
                "formal_rule_extension_only_cases": cases - authorized,
                "restored_selector_import_fields": (
                    {field: None for field in RESTORED_IMPORT_FIELDS}
                    if menu_name != "blocked"
                    else None
                ),
                "restored_selector_import_accepted": 0,
            }
        )

    require(selected_agreement == 128, "selected agreement")
    require(gap_agreement == 128, "gap agreement")
    require(face_agreement == 104, "face agreement")
    require(unique_complete == 64, "unique complete cases")
    require(tie_break_cases == 64, "tie-break cases")
    require(source_authorized == 32, "authorized cases")

    return {
        "schema": "exact-recurrent-first-host-selector-rule-compatibility/v1",
        "host_id": HOST_ID,
        "sources": {
            "selected_provenance": str(SELECTED_PATH),
            "restoration_selector_faces": str(RESTORATION_PATH),
            "installed_operation_registry": str(REGISTRY_DOC),
            "owner_fate_lineage_kernel": str(ANCESTRY_DOC),
        },
        "rules": {
            "source_selected_provenance_rule": SOURCE_RULE,
            "complete_score_audit_rule": COMPLETE_RULE,
            "source_rule_scope": "original residual response family of each normalized side-four host",
            "formal_extension_scope": "apply the intrinsic rule to every response in each restoration menu",
        },
        "menus": rows,
        "aggregate": {
            "restoration_menus": 4,
            "safe_backgrounds_per_menu": 32,
            "menu_background_cases": 128,
            "selected_identity_agreement_cases": selected_agreement,
            "next_gap_agreement_cases": gap_agreement,
            "minimizer_face_agreement_cases": face_agreement,
            "minimizer_face_disagreement_cases": 128 - face_agreement,
            "complete_unique_minimizer_cases": unique_complete,
            "complete_tie_break_dependent_cases": tie_break_cases,
            "directly_source_authorized_cases": source_authorized,
            "formal_extension_only_cases": 128 - source_authorized,
            "restored_menus": 3,
            "restored_menu_cases": 96,
            "restored_tie_break_dependent_cases": 64,
            "restored_selector_import_fields_per_menu": len(RESTORED_IMPORT_FIELDS),
            "restored_selector_import_fields_populated": 0,
            "restored_selector_rules_imported": 0,
            "scheduler_source_documents_audited": 2,
            "scheduler_tie_break_rules_found": 0,
        },
        "source_boundary": {
            "blocked_normalized_selector_compatible": 1,
            "formal_intrinsic_extension_matches_complete_selected_identity_all_cases": 1,
            "formal_intrinsic_extension_matches_complete_next_gap_all_cases": 1,
            "formal_intrinsic_extension_matches_complete_minimizer_face_all_cases": 0,
            "restore_both_face_disagreement_cases": 24,
            "restore_02_selector_requires_tie_break": 1,
            "restore_20_selector_requires_tie_break": 0,
            "restore_both_selector_requires_tie_break": 1,
            "installed_scheduler_specifies_lexicographic_tie_break": 0,
            "face_congruence_substitute_proved": 0,
            "restored_selector_rule_source_authorized": 0,
            "physical_selector_rule_import_allowed": 0,
        },
        "restored_selector_import_contract": {
            "fields": list(RESTORED_IMPORT_FIELDS),
            "field_count": len(RESTORED_IMPORT_FIELDS),
            "acceptance_rule": (
                "each restored menu requires a physical occurrence and legal menu state, "
                "a source-defined response family and score semantics, and either a source "
                "tie-break rule or complete child/payment congruence on its entire minimizer face"
            ),
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "legal_restoration_operation_proved": 0,
            "source_scheduler_tie_break_proved": 0,
            "operation_congruence_proved": 0,
            "payment_congruence_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(root: Path, value: dict[str, Any]) -> None:
    require(value == compile_manifest(root), "manifest differs from deterministic compiler")


def mutation_audit(root: Path, expected: dict[str, Any]) -> int:
    mutations = []

    def add(mutator):
        item = copy.deepcopy(expected)
        mutator(item)
        mutations.append(item)

    add(lambda x: x["aggregate"].__setitem__("selected_identity_agreement_cases", 127))
    add(lambda x: x["aggregate"].__setitem__("minimizer_face_agreement_cases", 128))
    add(lambda x: x["aggregate"].__setitem__("complete_tie_break_dependent_cases", 32))
    add(lambda x: x["aggregate"].__setitem__("directly_source_authorized_cases", 128))
    add(lambda x: x["source_boundary"].__setitem__("restored_selector_rule_source_authorized", 1))
    add(lambda x: x["source_boundary"].__setitem__("installed_scheduler_specifies_lexicographic_tie_break", 1))
    add(lambda x: x["source_boundary"].__setitem__("face_congruence_substitute_proved", 1))
    add(lambda x: x["source_boundary"].__setitem__("physical_selector_rule_import_allowed", 1))
    add(lambda x: x["menus"][1].__setitem__("complete_tie_break_dependent_cases", 0))
    add(lambda x: x["menus"][2].__setitem__("source_rule_directly_authorized_cases", 32))
    add(lambda x: x["menus"][3].__setitem__("minimizer_face_disagreement_cases", 0))
    add(lambda x: x["menus"][3]["intrinsic_minimizer_face"].remove("2301"))
    add(lambda x: x["restored_selector_import_contract"]["fields"].pop())
    add(lambda x: x["honesty"].__setitem__("source_scheduler_tie_break_proved", 1))
    add(lambda x: x["honesty"].__setitem__("all_n_proved_by_checker", 1))

    rejected = 0
    for item in mutations:
        try:
            validate_manifest(root, item)
        except AuditError:
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    manifest = compile_manifest(args.root)
    mutation_audit(args.root, manifest)
    if args.check:
        validate_manifest(args.root, json.loads(args.check.read_text()))
    if args.write:
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    if not args.check and not args.write:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
