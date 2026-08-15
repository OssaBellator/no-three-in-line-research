#!/usr/bin/env python3
"""Audit whether first-host action families are geometrically congruent."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

FAMILIES = {
    "restore_02": (("00", "10"), ("01", "11")),
    "delete_02": (("10", "00"), ("11", "01")),
    "restore_20": (("00", "01"), ("10", "11")),
    "delete_20": (("01", "00"), ("11", "10")),
}
STATE_MENU = {
    "00": "blocked",
    "01": "restore_20",
    "10": "restore_02",
    "11": "restore_both",
}
STATE_SELECTED = {
    "00": "3012",
    "01": "3201",
    "10": "2031",
    "11": "2031",
}
FAMILY_FIELDS = (
    "family_id",
    "edge_refs",
    "shared_theorem_ref",
    "quantified_context_bit",
    "both_context_values_proved",
    "shared_owner_schema_ref",
    "shared_operation_schema_ref",
    "shared_route_schema_ref",
    "child_payment_compatibility_ref",
    "realization_status",
)


class CongruenceError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise CongruenceError(message)


def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise CongruenceError("repository root")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def edge_code(edge: tuple[str, str]) -> str:
    return f"{edge[0]}->{edge[1]}"


def singleton_key(mapping: dict, message: str) -> str:
    require(len(mapping) == 1, message)
    return next(iter(mapping))


def state_descriptor(state: str, selector: dict) -> dict:
    menu = selector["menus"][STATE_MENU[state]]
    gap = int(singleton_key(menu["next_gap_census"], f"gap {state}"))
    selected = singleton_key(menu["selected_response_census"], f"selected {state}")
    require(selected == STATE_SELECTED[state], f"selected mismatch {state}")
    faces = [
        {
            "face": row["face"],
            "background_count": row["background_count"],
        }
        for row in menu["minimizer_faces"]
    ]
    return {
        "state": state,
        "menu": STATE_MENU[state],
        "selected": selected,
        "next_gap": gap,
        "face_profiles": faces,
        "face_background_invariant": int(len(faces) == 1),
    }


def compile_manifest(repository: Path) -> dict:
    transition = load(
        repository / "data/exact_recurrent_first_host_transition_domain_source_audit.json"
    )
    selector = load(
        repository / "data/exact_recurrent_first_host_restoration_selector_face.json"
    )
    symmetry = load(
        repository / "data/exact_recurrent_first_host_safe_signature_symmetry.json"
    )
    leverage = load(
        repository / "data/exact_recurrent_first_host_action_family_route_leverage.json"
    )

    require(transition["aggregate"]["physical_directed_edges"] == 0, "physical edges changed")
    require(selector["aggregate"]["restoration_menus"] == 4, "menu count")
    require(selector["conclusion"]["complete_transition_payment_congruence_proved"] == 0,
            "transition congruence changed")
    require(symmetry["aggregate"]["exact_geometric_stabilizer"] == 1, "stabilizer")
    require(symmetry["conclusion"]["exact_first_host_automorphism_group_trivial"] == 1,
            "automorphism")
    require(leverage["aggregate"]["directed_action_families"] == 4, "family count")
    require(leverage["aggregate"]["current_source_closed_families"] == 0, "family source changed")

    states = {state: state_descriptor(state, selector) for state in STATE_MENU}
    rows = []
    homogeneous_selector_change = 0
    homogeneous_selected_pair = 0
    homogeneous_gap_pair = 0
    homogeneous_face_pair = 0
    touches_state_11 = 0

    for name, members in FAMILIES.items():
        edge_rows = []
        for source, target in members:
            source_row = states[source]
            target_row = states[target]
            edge_rows.append({
                "edge": edge_code((source, target)),
                "source_state": source,
                "target_state": target,
                "source_selected": source_row["selected"],
                "target_selected": target_row["selected"],
                "selector_changing": int(source_row["selected"] != target_row["selected"]),
                "source_gap": source_row["next_gap"],
                "target_gap": target_row["next_gap"],
                "source_face_profiles": source_row["face_profiles"],
                "target_face_profiles": target_row["face_profiles"],
                "touches_state_11": int("11" in (source, target)),
            })
        selector_flags = {row["selector_changing"] for row in edge_rows}
        selected_pairs = {
            (row["source_selected"], row["target_selected"]) for row in edge_rows
        }
        gap_pairs = {(row["source_gap"], row["target_gap"]) for row in edge_rows}
        face_pairs = {
            json.dumps(
                [row["source_face_profiles"], row["target_face_profiles"]],
                sort_keys=True,
                separators=(",", ":"),
            )
            for row in edge_rows
        }
        family_touches_11 = int(any(row["touches_state_11"] for row in edge_rows))
        homogeneous_selector_change += len(selector_flags) == 1
        homogeneous_selected_pair += len(selected_pairs) == 1
        homogeneous_gap_pair += len(gap_pairs) == 1
        homogeneous_face_pair += len(face_pairs) == 1
        touches_state_11 += family_touches_11
        rows.append({
            "family": name,
            "changed_cell": name.split("_")[1],
            "action": name.split("_")[0],
            "other_context_bit": "r20" if name.endswith("_02") else "r02",
            "members": edge_rows,
            "homogeneous_changed_cell_action": 1,
            "homogeneous_selector_change_flag": int(len(selector_flags) == 1),
            "homogeneous_ordered_selected_pair": int(len(selected_pairs) == 1),
            "homogeneous_ordered_gap_pair": int(len(gap_pairs) == 1),
            "homogeneous_ordered_face_profile_pair": int(len(face_pairs) == 1),
            "touches_context_sensitive_state_11": family_touches_11,
            "members_related_by_exact_host_automorphism": 0,
            "context_free_operation_row_inferred": 0,
            "source_uniformity_fields": {field: None for field in FAMILY_FIELDS},
            "source_uniformity_populated": 0,
        })

    require(homogeneous_selector_change == 2, "selector flag census")
    require(homogeneous_selected_pair == 0, "selected pair census")
    require(homogeneous_gap_pair == 0, "gap pair census")
    require(homogeneous_face_pair == 0, "face pair census")
    require(touches_state_11 == 4, "state 11 census")
    require(
        sorted(row["family"] for row in rows if row["homogeneous_selector_change_flag"])
        == ["delete_02", "restore_02"],
        "selector-homogeneous families",
    )

    return {
        "schema": "exact-recurrent-first-host-action-family-congruence-obstruction/v1",
        "host_id": "s4-75b04c45c1c8eac2",
        "sources": {
            "transition_domain":
                "data/exact_recurrent_first_host_transition_domain_source_audit.json",
            "selector_faces":
                "data/exact_recurrent_first_host_restoration_selector_face.json",
            "exact_symmetry":
                "data/exact_recurrent_first_host_safe_signature_symmetry.json",
            "family_leverage":
                "data/exact_recurrent_first_host_action_family_route_leverage.json",
        },
        "states": [states[state] for state in sorted(states)],
        "families": rows,
        "uniform_family_contract": {
            "field_count": len(FAMILY_FIELDS),
            "required_fields": list(FAMILY_FIELDS),
            "acceptance_rule":
                "either provide both member edge records separately or a theorem explicitly quantified over both values of the other restoration bit",
            "symmetry_shortcut_available": 0,
            "selector_gap_shortcut_available": 0,
            "complete_face_shortcut_available": 0,
        },
        "aggregate": {
            "action_families": 4,
            "members_per_family": 2,
            "families_homogeneous_changed_cell_action": 4,
            "families_homogeneous_selector_change_flag": homogeneous_selector_change,
            "families_homogeneous_ordered_selected_pair": homogeneous_selected_pair,
            "families_homogeneous_ordered_gap_pair": homogeneous_gap_pair,
            "families_homogeneous_ordered_face_profile_pair": homogeneous_face_pair,
            "families_touching_context_sensitive_state_11": touches_state_11,
            "families_related_by_exact_host_automorphism": 0,
            "source_uniformity_fields_per_family": len(FAMILY_FIELDS),
            "source_uniformity_records_populated": 0,
        },
        "conclusion": {
            "action_family_geometry_audit_complete": 1,
            "changed_cell_action_implies_operation_congruence": 0,
            "selector_change_flag_implies_operation_congruence": 0,
            "selected_response_pair_implies_operation_congruence": 0,
            "gap_pair_implies_operation_congruence": 0,
            "complete_face_profile_implies_operation_congruence": 0,
            "exact_symmetry_identifies_family_members": 0,
            "context_parametric_source_theorem_required": 1,
            "current_uniform_family_operation_congruence_proved": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "operation_congruence_proved": 0,
            "payment_congruence_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict, repository: Path) -> None:
    require(manifest == compile_manifest(repository), "manifest mismatch")


def mutation_audit(manifest: dict, repository: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(action_families=3),
        lambda item: item["aggregate"].update(families_homogeneous_selector_change_flag=3),
        lambda item: item["aggregate"].update(families_homogeneous_ordered_selected_pair=1),
        lambda item: item["aggregate"].update(families_homogeneous_ordered_gap_pair=1),
        lambda item: item["aggregate"].update(families_homogeneous_ordered_face_profile_pair=1),
        lambda item: item["aggregate"].update(families_related_by_exact_host_automorphism=1),
        lambda item: item["families"][0].update(context_free_operation_row_inferred=1),
        lambda item: item["families"][0].update(source_uniformity_populated=1),
        lambda item: item["families"][0]["source_uniformity_fields"].update(shared_theorem_ref="x"),
        lambda item: item["uniform_family_contract"].update(symmetry_shortcut_available=1),
        lambda item: item["conclusion"].update(changed_cell_action_implies_operation_congruence=1),
        lambda item: item["conclusion"].update(current_uniform_family_operation_congruence_proved=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(operation_congruence_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, repository)
        except CongruenceError:
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    repository = root()
    manifest = compile_manifest(repository)
    validate(manifest, repository)
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.check:
        validate(load(args.check), repository)
    print(json.dumps({
        "checker": "exact-recurrent-first-host-action-family-congruence-obstruction",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest, repository),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
