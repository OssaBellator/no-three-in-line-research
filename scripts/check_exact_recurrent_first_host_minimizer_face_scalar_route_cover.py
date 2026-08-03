#!/usr/bin/env python3
"""Classify strict scalar covers on exact first-host complete minimizer faces."""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
FACE_PATH = Path("data/exact_recurrent_first_host_restoration_selector_face.json")
BOUNDARY_PATH = Path("data/exact_recurrent_first_host_selector_boolean_boundary.json")
MENU_PATH = Path("data/exact_recurrent_first_host_menu_interaction_potential.json")

VERTICES = (
    ("A", ("3012",), ("00",), 32),
    ("B", ("3201",), ("01",), 32),
    ("C", ("2031", "2310"), ("10",), 32),
    ("D3", ("2031", "2310", "3201"), ("11",), 24),
    ("D4", ("2031", "2301", "2310", "3201"), ("11",), 8),
)
PAIRS = (
    ("AB", "A", "B", "00", "01", "r20", 1, 32, "all-safe-backgrounds"),
    ("AC", "A", "C", "00", "10", "r02", 1, 32, "all-safe-backgrounds"),
    ("BD3", "B", "D3", "01", "11", "r02", 1, 24, "restore-both-three-way"),
    ("BD4", "B", "D4", "01", "11", "r02", 1, 8, "restore-both-four-way"),
    ("CD3", "C", "D3", "10", "11", "r20", 0, 24, "restore-both-three-way"),
    ("CD4", "C", "D4", "10", "11", "r20", 0, 8, "restore-both-four-way"),
)
RESTORE_STATE_EDGES = {"00->01", "00->10", "01->11", "10->11"}


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


def stable_id(prefix: str, payload: object) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return f"{prefix}-{hashlib.sha256(canonical.encode()).hexdigest()[:12]}"


def acyclic(vertices: tuple[str, ...], directions: tuple[tuple[str, str], ...]) -> bool:
    outgoing = {vertex: [] for vertex in vertices}
    indegree = {vertex: 0 for vertex in vertices}
    for source, target in directions:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = sorted(vertex for vertex in vertices if indegree[vertex] == 0)
    seen = 0
    while queue:
        vertex = queue.pop(0)
        seen += 1
        for target in sorted(outgoing[vertex]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
                queue.sort()
    return seen == len(vertices)


def direction_for(bit: int, left: str, right: str) -> tuple[str, str]:
    return (left, right) if bit else (right, left)


def state_direction(source_face: str, target_face: str) -> str:
    state_by_face = {"A": "00", "B": "01", "C": "10", "D3": "11", "D4": "11"}
    return f"{state_by_face[source_face]}->{state_by_face[target_face]}"


def compile_manifest(root: Path) -> dict[str, Any]:
    faces = load_json(root, FACE_PATH)
    boundary = load_json(root, BOUNDARY_PATH)
    menu = load_json(root, MENU_PATH)

    require(faces.get("schema") == "exact-recurrent-first-host-restoration-selector-face/v1", "face schema")
    require(boundary.get("schema") == "exact-recurrent-first-host-selector-boolean-boundary/v3", "boundary schema")
    require(menu.get("schema") == "exact-recurrent-first-host-menu-interaction-potential/v1", "menu schema")
    require(faces.get("scope", {}).get("host_id") == HOST_ID, "face host")
    require(boundary.get("scope", {}).get("host_id") == HOST_ID, "boundary host")
    require(menu.get("scope", {}).get("host_id") == HOST_ID, "menu host")

    face_menus = faces.get("menus", {})
    require(face_menus["blocked"]["minimizer_faces"] == [{"background_count": 32, "face": ["3012"]}], "blocked face")
    require(face_menus["restore_20"]["minimizer_faces"] == [{"background_count": 32, "face": ["3201"]}], "restore20 face")
    require(face_menus["restore_02"]["minimizer_faces"] == [{"background_count": 32, "face": ["2031", "2310"]}], "restore02 face")
    require(
        face_menus["restore_both"]["minimizer_faces"]
        == [
            {"background_count": 8, "face": ["2031", "2301", "2310", "3201"]},
            {"background_count": 24, "face": ["2031", "2310", "3201"]},
        ],
        "restore-both faces",
    )
    require(faces.get("aggregate", {}).get("total_distinct_minimizer_faces") == 5, "five faces")
    require(boundary.get("aggregate", {}).get("menu_states") == 4, "four menu states")
    require(boundary.get("aggregate", {}).get("directed_single_bit_context_edges") == 8, "eight state edges")
    require(menu.get("aggregate", {}).get("acyclic_menu_orientations") == 14, "fourteen menu covers")

    menu_paid_sets = {
        tuple(sorted(row["paid_menu_edges"]))
        for row in menu.get("orientations", [])
    }
    require(len(menu_paid_sets) == 14, "menu paid-set count")

    vertices = tuple(row[0] for row in VERTICES)
    orientation_records = []
    cyclic_count = 0
    split_profile: dict[str, int] = {
        "menu_projectable": 0,
        "changing_family_only": 0,
        "neutral_family_only": 0,
        "both_restore_both_families": 0,
    }
    paid_restore_type_distribution: dict[str, int] = {}
    projected_paid_sets: set[tuple[str, ...]] = set()

    for bits in itertools.product((0, 1), repeat=len(PAIRS)):
        directions = tuple(
            direction_for(bit, row[1], row[2])
            for bit, row in zip(bits, PAIRS)
        )
        if not acyclic(vertices, directions):
            cyclic_count += 1
            continue

        by_pair = {row[0]: direction for row, direction in zip(PAIRS, directions)}
        split_changing = (by_pair["BD3"][0] == "B") != (by_pair["BD4"][0] == "B")
        split_neutral = (by_pair["CD3"][0] == "C") != (by_pair["CD4"][0] == "C")
        menu_projectable = not split_changing and not split_neutral

        if menu_projectable:
            profile = "menu_projectable"
        elif split_changing and split_neutral:
            profile = "both_restore_both_families"
        elif split_changing:
            profile = "changing_family_only"
        else:
            profile = "neutral_family_only"
        split_profile[profile] += 1

        paid_face_directions = [f"{source}->{target}" for source, target in directions]
        external_face_directions = [f"{target}->{source}" for source, target in directions]

        paid_state_edges: list[str] = []
        if menu_projectable:
            for pair_id in ("AB", "AC", "BD3", "CD3"):
                source, target = by_pair[pair_id]
                paid_state_edges.append(state_direction(source, target))
            paid_state_edges = sorted(paid_state_edges)
            projected_paid_sets.add(tuple(paid_state_edges))
            require(tuple(paid_state_edges) in menu_paid_sets, "projected menu cover")

        paid_restore_types = 0
        paid_restore_occurrences = 0
        paid_occurrences = 0
        residual_occurrences = 0
        residual_changing_occurrences = 0
        residual_neutral_occurrences = 0
        residual_r02_occurrences = 0
        residual_r20_occurrences = 0
        for row, direction in zip(PAIRS, directions):
            _, _, _, _, _, bit_name, selected_changing, background_count, _ = row
            paid_occurrences += background_count
            residual_occurrences += background_count
            paid_state = state_direction(*direction)
            if paid_state in RESTORE_STATE_EDGES:
                paid_restore_types += 1
                paid_restore_occurrences += background_count
            if selected_changing:
                residual_changing_occurrences += background_count
            else:
                residual_neutral_occurrences += background_count
            if bit_name == "r02":
                residual_r02_occurrences += background_count
            else:
                residual_r20_occurrences += background_count

        require(paid_occurrences == 128 and residual_occurrences == 128, "occurrence balance")
        require(residual_changing_occurrences == 96, "changing residual occurrence burden")
        require(residual_neutral_occurrences == 32, "neutral residual occurrence burden")
        require(residual_r02_occurrences == 64 and residual_r20_occurrences == 64, "bit residual balance")

        paid_restore_type_distribution[str(paid_restore_types)] = (
            paid_restore_type_distribution.get(str(paid_restore_types), 0) + 1
        )
        structural = {
            "paid_face_directions": sorted(paid_face_directions),
            "menu_projectable": int(menu_projectable),
        }
        orientation_records.append(
            {
                "orientation_id": stable_id("face-cover", structural),
                "paid_face_directions": sorted(paid_face_directions),
                "external_face_directions": sorted(external_face_directions),
                "menu_projectable": int(menu_projectable),
                "background_sensitive": int(not menu_projectable),
                "split_selector_changing_restore_both_family": int(split_changing),
                "split_selector_neutral_restore_both_family": int(split_neutral),
                "projected_paid_menu_edges": paid_state_edges,
                "paid_face_pair_types": 6,
                "external_face_pair_types": 6,
                "paid_occurrence_edges": paid_occurrences,
                "external_occurrence_edges": residual_occurrences,
                "external_selected_changing_occurrence_edges": residual_changing_occurrences,
                "external_selector_neutral_occurrence_edges": residual_neutral_occurrences,
                "external_r02_occurrence_edges": residual_r02_occurrences,
                "external_r20_occurrence_edges": residual_r20_occurrences,
                "paid_restore_pair_types": paid_restore_types,
                "paid_restore_occurrence_edges": paid_restore_occurrences,
            }
        )

    orientation_records.sort(key=lambda row: row["orientation_id"])
    require(len(orientation_records) == 46, "46 acyclic face orientations")
    require(cyclic_count == 18, "18 cyclic orientations")
    require(split_profile == {
        "menu_projectable": 14,
        "changing_family_only": 12,
        "neutral_family_only": 12,
        "both_restore_both_families": 8,
    }, "split profile")
    require(projected_paid_sets == menu_paid_sets, "exact menu-cover projection")
    require(paid_restore_type_distribution == {
        "0": 1, "1": 6, "2": 9, "3": 14, "4": 9, "5": 6, "6": 1
    }, "restore type distribution")

    face_vertices = [
        {
            "face_id": face_id,
            "responses": list(responses),
            "menu_states": list(states),
            "background_count": count,
        }
        for face_id, responses, states, count in VERTICES
    ]
    face_pairs = [
        {
            "pair_id": pair_id,
            "vertices": [left, right],
            "menu_state_pair": [state_left, state_right],
            "changed_bit": bit_name,
            "selected_response_changes": selected_changing,
            "background_count": count,
            "background_class": background_class,
        }
        for (
            pair_id,
            left,
            right,
            state_left,
            state_right,
            bit_name,
            selected_changing,
            count,
            background_class,
        ) in PAIRS
    ]

    return {
        "schema": "exact-recurrent-first-host-minimizer-face-scalar-route-cover/v1",
        "host_id": HOST_ID,
        "sources": {
            "restoration_selector_face": str(FACE_PATH),
            "selector_boolean_boundary": str(BOUNDARY_PATH),
            "menu_interaction_potential": str(MENU_PATH),
        },
        "face_graph": {
            "graph_type": "complete-bipartite-K2,3",
            "bipartition": [["B", "C"], ["A", "D3", "D4"]],
            "vertices": face_vertices,
            "undirected_pairs": face_pairs,
            "vertex_count": 5,
            "undirected_pair_count": 6,
            "directed_face_edge_types": 12,
        },
        "orientation_records": orientation_records,
        "aggregate": {
            "safe_backgrounds": 32,
            "menu_states": 4,
            "distinct_minimizer_faces": 5,
            "face_pair_orientations": 64,
            "acyclic_face_scalar_covers": 46,
            "cyclic_incompatible_orientations": 18,
            "menu_projectable_face_covers": 14,
            "background_sensitive_face_covers": 32,
            "background_sensitive_changing_family_only": 12,
            "background_sensitive_neutral_family_only": 12,
            "background_sensitive_both_families": 8,
            "existing_menu_scalar_covers": 14,
            "projectable_face_covers_match_menu_covers": 14,
            "paid_face_pair_types_per_cover": 6,
            "external_face_pair_types_per_cover": 6,
            "paid_occurrence_edges_per_safe_domain": 128,
            "external_occurrence_edges_per_safe_domain": 128,
            "external_occurrence_edges_per_background": 4,
            "external_selected_changing_occurrence_edges_per_safe_domain": 96,
            "external_selector_neutral_occurrence_edges_per_safe_domain": 32,
            "external_r02_occurrence_edges_per_safe_domain": 64,
            "external_r20_occurrence_edges_per_safe_domain": 64,
            "paid_restore_pair_type_distribution": paid_restore_type_distribution,
            "physical_face_classifications_populated": 0,
            "physical_face_scalar_values_populated": 0,
            "physical_face_edge_routes_populated": 0,
        },
        "source_boundary": {
            "face_scalar_avoids_lexicographic_tie_break": 1,
            "face_scalar_requires_exact_physical_minimizer_face": 1,
            "menu_projectable_class_adds_no_scalar_cover": 1,
            "background_sensitive_class_requires_D3_D4_source_separation": 1,
            "background_sensitive_class_reduces_external_occurrence_burden": 0,
            "minimum_external_occurrence_edges_per_background_remains_four": 1,
            "minimum_external_selected_changing_edges_per_background_remains_three": 1,
            "minimum_external_selector_neutral_edges_per_background_remains_one": 1,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "physical_minimizer_face_classification_proved": 0,
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

    add(lambda x: x["face_graph"].__setitem__("graph_type", "cycle"))
    add(lambda x: x["aggregate"].__setitem__("acyclic_face_scalar_covers", 45))
    add(lambda x: x["aggregate"].__setitem__("cyclic_incompatible_orientations", 17))
    add(lambda x: x["aggregate"].__setitem__("menu_projectable_face_covers", 13))
    add(lambda x: x["aggregate"].__setitem__("background_sensitive_face_covers", 31))
    add(lambda x: x["aggregate"].__setitem__("background_sensitive_changing_family_only", 11))
    add(lambda x: x["aggregate"].__setitem__("projectable_face_covers_match_menu_covers", 13))
    add(lambda x: x["aggregate"].__setitem__("external_occurrence_edges_per_background", 3))
    add(lambda x: x["aggregate"].__setitem__("external_selected_changing_occurrence_edges_per_safe_domain", 95))
    add(lambda x: x["aggregate"].__setitem__("external_selector_neutral_occurrence_edges_per_safe_domain", 31))
    add(lambda x: x["aggregate"].__setitem__("external_r02_occurrence_edges_per_safe_domain", 63))
    add(lambda x: x["aggregate"]["paid_restore_pair_type_distribution"].__setitem__("3", 13))
    add(lambda x: x["orientation_records"][0].__setitem__("menu_projectable", 1 - x["orientation_records"][0]["menu_projectable"]))
    add(lambda x: x["orientation_records"][0]["paid_face_directions"].pop())
    add(lambda x: x["source_boundary"].__setitem__("background_sensitive_class_reduces_external_occurrence_burden", 1))
    add(lambda x: x["source_boundary"].__setitem__("promotion_to_recurrent_closure_allowed", 1))
    add(lambda x: x["honesty"].__setitem__("strict_lyapunov_certificate_proved", 1))
    add(lambda x: x["honesty"].__setitem__("all_n_proved_by_checker", 1))

    rejected = 0
    for item in candidates:
        try:
            validate_manifest(root, item)
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

    value = compile_manifest(args.root)
    if args.write:
        path = args.root / args.write
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if args.check:
        stored = load_json(args.root, args.check)
        validate_manifest(args.root, stored)
    if args.mutation_audit:
        print(f"mutation rejections: {mutation_audit(args.root, value)}")
    print(json.dumps(value["aggregate"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
