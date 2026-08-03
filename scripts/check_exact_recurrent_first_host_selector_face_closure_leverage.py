#!/usr/bin/env python3
"""Classify recurrence leverage of first-host minimizer-face congruence proofs."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
WORKLIST_PATH = Path("data/exact_recurrent_first_host_selector_face_congruence_worklist.json")
SOURCE_GATE_PATH = Path("data/exact_recurrent_first_host_selector_face_source_import_gate.json")
BOOLEAN_PATH = Path("data/exact_recurrent_first_host_selector_boolean_boundary.json")
SCALAR_PATH = Path("data/exact_recurrent_first_host_scalar_route_cover.json")
PAIR_TYPES = ("2031~2301", "2031~2310", "2031~3201")
GLOBAL_QUOTIENT_FIELDS = (
    "physical_occurrence_domain_ref",
    "selected_state_domain_ref",
    "menu_state_refs",
    "common_owner_ref",
    "operation_congruence_ref",
    "child_row_congruence_ref",
    "payment_congruence_ref",
    "closure_route_congruence_ref",
    "theorem_ref",
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


def compile_manifest(root: Path) -> dict[str, Any]:
    worklist = load_json(root, WORKLIST_PATH)
    source_gate = load_json(root, SOURCE_GATE_PATH)
    boolean = load_json(root, BOOLEAN_PATH)
    scalar = load_json(root, SCALAR_PATH)

    require(
        worklist.get("schema")
        == "exact-recurrent-first-host-selector-face-congruence-worklist/v1",
        "worklist schema",
    )
    require(worklist.get("host_id") == HOST_ID, "worklist host")
    work_agg = worklist.get("aggregate", {})
    require(work_agg.get("signature_pair_obligations") == 32, "worklist obligations")
    require(work_agg.get("menu_parametric_pair_theorem_domains") == 4, "menu domains")
    require(work_agg.get("cross_menu_pair_theorem_types") == 3, "pair types")
    require(work_agg.get("accepted_signature_obligations") == 0, "worklist honesty")

    require(
        source_gate.get("schema")
        == "exact-recurrent-first-host-selector-face-source-import-gate/v1",
        "source gate schema",
    )
    require(source_gate.get("host_id") == HOST_ID, "source gate host")
    source_agg = source_gate.get("aggregate", {})
    require(source_agg.get("signature_specific_records") == 32, "source signature records")
    require(source_agg.get("menu_parametric_records") == 4, "source menu records")
    require(source_agg.get("cross_menu_parametric_records") == 3, "source cross records")
    require(source_agg.get("accepted_modes") == 0, "source accepted modes")
    require(
        source_gate.get("source_boundary", {}).get("face_congruence_source_import_accepted") == 0,
        "source gate honesty",
    )

    require(
        boolean.get("schema") == "exact-recurrent-first-host-selector-boolean-boundary/v3",
        "boolean schema",
    )
    require(boolean.get("scope", {}).get("host_id") == HOST_ID, "boolean host")
    states = {row["state"]: row["selected_response"] for row in boolean.get("menu_states", [])}
    require(
        states == {"00": "3012", "01": "3201", "10": "2031", "11": "2031"},
        "selected state map",
    )
    bool_agg = boolean.get("aggregate", {})
    require(bool_agg.get("selector_changing_single_bit_edges") == 6, "six changing")
    require(bool_agg.get("selector_neutral_single_bit_edges") == 2, "two neutral")
    require(bool_agg.get("selected_label_bidirected_pairs") == 3, "three label pairs")

    require(
        scalar.get("schema") == "exact-recurrent-first-host-scalar-route-cover/v1",
        "scalar schema",
    )
    require(scalar.get("scope", {}).get("host_id") == HOST_ID, "scalar host")
    scalar_agg = scalar.get("aggregate", {})
    require(scalar_agg.get("selected_label_scalar_compatible_route_covers") == 6, "six covers")
    require(scalar_agg.get("selected_label_paid_edges") == 3, "three paid")
    require(scalar_agg.get("selected_label_minimum_external_routes") == 3, "three external")
    require(scalar_agg.get("menu_scalar_compatible_route_covers") == 14, "fourteen menu covers")
    require(scalar_agg.get("menu_minimum_external_routes") == 4, "four menu routes")

    patterns: list[dict[str, Any]] = []
    distribution: dict[int, int] = {}
    full_patterns: list[list[str]] = []
    for mask in range(1 << len(PAIR_TYPES)):
        chosen = [PAIR_TYPES[i] for i in range(len(PAIR_TYPES)) if mask >> i & 1]
        chosen_set = set(chosen)
        restore_02 = 32 if "2031~2310" in chosen_set else 0
        restore_both_three = 24 if {"2031~2310", "2031~3201"} <= chosen_set else 0
        restore_both_four = 8 if set(PAIR_TYPES) <= chosen_set else 0
        total = restore_02 + restore_both_three + restore_both_four
        distribution[total] = distribution.get(total, 0) + 1
        full = int(total == 64)
        if full:
            full_patterns.append(chosen)
        patterns.append(
            {
                "proved_pair_types": chosen,
                "proved_pair_count": len(chosen),
                "restore_02_tied_cases_discharged": restore_02,
                "restore_both_three_way_cases_discharged": restore_both_three,
                "restore_both_four_way_cases_discharged": restore_both_four,
                "tied_menu_background_cases_discharged": total,
                "all_tied_menu_cases_discharged": full,
                "menu_local_tie_break_substitution_available": full,
                "selected_state_global_quotient_authorized": 0,
                "selected_label_graph_reduction_authorized": 0,
            }
        )

    require(distribution == {0: 4, 32: 2, 56: 1, 64: 1}, "coverage distribution")
    require(full_patterns == [list(PAIR_TYPES)], "unique full pattern")

    original_total_nonlabel = (
        scalar_agg["selected_label_minimum_external_routes"]
        + bool_agg["selector_neutral_single_bit_edges"]
    )
    require(original_total_nonlabel == 5, "original total non-label burden")

    hypothetical = {
        "additional_theorem_required": (
            "one occurrence-faithful selected-state theorem identifying selected 3201 in "
            "state 01 with selected 2031 in states 10 and 11 across their distinct legal menus"
        ),
        "quotient_selected_classes": [["3012"], ["2031", "3201"]],
        "selected_label_vertices": 2,
        "selected_label_bidirected_pairs": 1,
        "unique_directed_selected_label_edges": 2,
        "selector_changing_menu_edges": 4,
        "selector_neutral_menu_edges": 4,
        "selected_label_scalar_orders": 2,
        "maximum_changing_menu_edges_payable_by_label_descent": 2,
        "changing_menu_edges_requiring_other_route": 2,
        "total_menu_edges_requiring_non_label_route": 6,
        "change_from_current_total_non_label_route_burden": 1,
        "menu_scalar_route_covers": scalar_agg["menu_scalar_compatible_route_covers"],
        "menu_scalar_minimum_external_routes": scalar_agg["menu_minimum_external_routes"],
        "global_quotient_evidence": {field: None for field in GLOBAL_QUOTIENT_FIELDS},
        "global_quotient_evidence_fields_populated": 0,
        "global_quotient_accepted": 0,
    }

    return {
        "schema": "exact-recurrent-first-host-selector-face-closure-leverage/v1",
        "host_id": HOST_ID,
        "sources": {
            "face_congruence_worklist": str(WORKLIST_PATH),
            "face_source_import_gate": str(SOURCE_GATE_PATH),
            "selector_boolean_boundary": str(BOOLEAN_PATH),
            "scalar_route_cover": str(SCALAR_PATH),
        },
        "pair_types": list(PAIR_TYPES),
        "subset_patterns": patterns,
        "coverage_distribution": [
            {"tied_cases_discharged": count, "subset_patterns": distribution[count]}
            for count in sorted(distribution)
        ],
        "unique_complete_pair_set": list(PAIR_TYPES),
        "indispensable_pair_types": list(PAIR_TYPES),
        "sharp_leverage_chain": [
            {
                "proved_pair_types": ["2031~2310"],
                "tied_cases_discharged": 32,
                "remaining_tied_cases": 32,
            },
            {
                "proved_pair_types": ["2031~2310", "2031~3201"],
                "tied_cases_discharged": 56,
                "remaining_tied_cases": 8,
            },
            {
                "proved_pair_types": list(PAIR_TYPES),
                "tied_cases_discharged": 64,
                "remaining_tied_cases": 0,
            },
        ],
        "automatic_recurrence_consequences": {
            "face_congruence_is_menu_local": 1,
            "menu_states_remain": 4,
            "directed_menu_edges_remain": 8,
            "selected_labels_by_state_remain": states,
            "selector_changing_edges_remain": 6,
            "selector_neutral_edges_remain": 2,
            "selected_label_scalar_route_covers_remain": 6,
            "selected_label_external_changing_routes_remain": 3,
            "menu_scalar_route_covers_remain": 14,
            "menu_scalar_external_routes_remain": 4,
            "selected_state_quotient_follows_from_face_congruence": 0,
            "route_cover_reduction_follows_from_face_congruence": 0,
        },
        "hypothetical_global_selected_state_quotient": hypothetical,
        "aggregate": {
            "pair_types": len(PAIR_TYPES),
            "pair_subsets": len(patterns),
            "unique_complete_pair_sets": len(full_patterns),
            "minimum_pair_types_for_all_tied_cases": len(PAIR_TYPES),
            "tied_menu_background_cases": 64,
            "maximum_cases_discharged_without_2031_2301": 56,
            "remaining_four_way_cases_without_2031_2301": 8,
            "current_source_accepted_pair_types": 0,
            "current_source_discharged_tied_cases": 0,
            "current_source_accepted_face_modes": 0,
            "current_selected_state_global_quotients": 0,
            "global_selected_state_quotient_evidence_fields": len(GLOBAL_QUOTIENT_FIELDS),
            "global_selected_state_quotient_populated_fields": 0,
            "current_total_menu_edges_requiring_non_label_route": original_total_nonlabel,
            "hypothetical_quotient_total_menu_edges_requiring_non_label_route": 6,
            "hypothetical_quotient_route_burden_delta": 1,
        },
        "source_boundary": {
            "all_three_pair_types_needed_for_full_tie_break_substitution": 1,
            "2031_2310_needed_for_both_tied_menus": 1,
            "2031_3201_needed_for_restore_both_three_way_faces": 1,
            "2031_2301_is_final_eight_case_bottleneck": 1,
            "full_face_congruence_source_imported": 0,
            "face_congruence_implies_cross_menu_selected_state_equivalence": 0,
            "global_selected_state_quotient_source_imported": 0,
            "selector_tie_break_substitution_allowed": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "legal_restoration_operation_proved": 0,
            "persistent_owner_identity_proved": 0,
            "recurrent_child_rows_populated": 0,
            "payment_congruence_proved": 0,
            "closure_route_congruence_proved": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(root: Path, value: dict[str, Any]) -> None:
    require(value == compile_manifest(root), "manifest differs from deterministic compiler")


def mutation_audit(root: Path, expected: dict[str, Any]) -> int:
    candidates: list[dict[str, Any]] = []

    def add(mutator) -> None:
        item = copy.deepcopy(expected)
        mutator(item)
        candidates.append(item)

    add(lambda x: x["aggregate"].__setitem__("pair_subsets", 7))
    add(lambda x: x["aggregate"].__setitem__("minimum_pair_types_for_all_tied_cases", 2))
    add(lambda x: x["aggregate"].__setitem__("maximum_cases_discharged_without_2031_2301", 64))
    add(lambda x: x["aggregate"].__setitem__("current_source_discharged_tied_cases", 1))
    add(lambda x: x["coverage_distribution"][0].__setitem__("subset_patterns", 3))
    add(lambda x: x["unique_complete_pair_set"].pop())
    add(lambda x: x["subset_patterns"][2].__setitem__("tied_menu_background_cases_discharged", 31))
    add(lambda x: x["subset_patterns"][7].__setitem__("selected_label_graph_reduction_authorized", 1))
    add(lambda x: x["automatic_recurrence_consequences"].__setitem__("selected_label_scalar_route_covers_remain", 2))
    add(lambda x: x["automatic_recurrence_consequences"].__setitem__("selected_state_quotient_follows_from_face_congruence", 1))
    add(lambda x: x["hypothetical_global_selected_state_quotient"].__setitem__("selector_neutral_menu_edges", 3))
    add(lambda x: x["hypothetical_global_selected_state_quotient"].__setitem__("total_menu_edges_requiring_non_label_route", 5))
    add(lambda x: x["hypothetical_global_selected_state_quotient"]["global_quotient_evidence"].__setitem__("theorem_ref", "fixture"))
    add(lambda x: x["source_boundary"].__setitem__("full_face_congruence_source_imported", 1))
    add(lambda x: x["source_boundary"].__setitem__("face_congruence_implies_cross_menu_selected_state_equivalence", 1))
    add(lambda x: x["source_boundary"].__setitem__("promotion_to_recurrent_closure_allowed", 1))
    add(lambda x: x["honesty"].__setitem__("strict_lyapunov_certificate_proved", 1))
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
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--mutation-audit", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = compile_manifest(root)
    if args.write:
        path = args.write if args.write.is_absolute() else root / args.write
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.check:
        path = args.check if args.check.is_absolute() else root / args.check
        validate_manifest(root, json.loads(path.read_text(encoding="utf-8")))
    if args.mutation_audit:
        print(f"mutation corruptions rejected: {mutation_audit(root, manifest)}")
    if not args.write and not args.check and not args.mutation_audit:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
