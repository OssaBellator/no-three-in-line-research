#!/usr/bin/env python3
"""Audit source leverage of background-sensitive minimizer-face scalar covers."""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
FACE_COVER_PATH = Path("data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json")
ROUTE_GATE_PATH = Path("data/exact_recurrent_first_host_closure_route_source_gate.json")
TRANSITION_PATH = Path("data/exact_recurrent_first_host_transition_domain_source_audit.json")

VERTICES = ("A", "B", "C", "D3", "D4")
PAIRS = (
    ("AB", "A", "B", "00", "01", 32),
    ("AC", "A", "C", "00", "10", 32),
    ("BD3", "B", "D3", "01", "11", 24),
    ("BD4", "B", "D4", "01", "11", 8),
    ("CD3", "C", "D3", "10", "11", 24),
    ("CD4", "C", "D4", "10", "11", 8),
)
STATE_EDGES = (
    "00->01",
    "01->00",
    "00->10",
    "10->00",
    "01->11",
    "11->01",
    "10->11",
    "11->10",
)
STATE_BY_FACE = {"A": "00", "B": "01", "C": "10", "D3": "11", "D4": "11"}


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


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, payload: object) -> str:
    digest = hashlib.sha256(canonical_json(payload).encode()).hexdigest()[:12]
    return f"{prefix}-{digest}"


def acyclic(directions: tuple[tuple[str, str], ...]) -> bool:
    outgoing = {vertex: [] for vertex in VERTICES}
    indegree = {vertex: 0 for vertex in VERTICES}
    for source, target in directions:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = sorted(vertex for vertex in VERTICES if indegree[vertex] == 0)
    seen = 0
    while queue:
        vertex = queue.pop(0)
        seen += 1
        for target in sorted(outgoing[vertex]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
                queue.sort()
    return seen == len(VERTICES)


def state_edge(direction: tuple[str, str]) -> str:
    return f"{STATE_BY_FACE[direction[0]]}->{STATE_BY_FACE[direction[1]]}"


def orientation_record(bits: tuple[int, ...]) -> dict[str, Any]:
    paid = tuple(
        (left, right) if bit else (right, left)
        for bit, (_, left, right, _, _, _) in zip(bits, PAIRS)
    )
    by_pair = {row[0]: direction for row, direction in zip(PAIRS, paid)}
    split_changing = (by_pair["BD3"][0] == "B") != (by_pair["BD4"][0] == "B")
    split_neutral = (by_pair["CD3"][0] == "C") != (by_pair["CD4"][0] == "C")
    projectable = not split_changing and not split_neutral
    paid_face_directions = sorted(f"{source}->{target}" for source, target in paid)
    record_id = stable_id(
        "face-cover",
        {
            "paid_face_directions": paid_face_directions,
            "menu_projectable": int(projectable),
        },
    )
    external = tuple((target, source) for source, target in paid)
    occurrence_vector = {edge: 0 for edge in STATE_EDGES}
    for pair, direction in zip(PAIRS, external):
        occurrence_vector[state_edge(direction)] += pair[5]
    return {
        "bits": bits,
        "cover_id": record_id,
        "paid": paid,
        "external": external,
        "menu_projectable": projectable,
        "split_changing": split_changing,
        "split_neutral": split_neutral,
        "occurrence_vector": occurrence_vector,
    }


def complete_bits(bits: tuple[int, ...], source_class: str) -> tuple[int, ...]:
    completed = list(bits)
    if source_class == "D3":
        completed[3] = completed[2]
        completed[5] = completed[4]
    elif source_class == "D4":
        completed[2] = completed[3]
        completed[4] = completed[5]
    else:
        raise AuditError(f"unknown completion class: {source_class}")
    return tuple(completed)


def add_vectors(
    left: dict[str, int],
    right: dict[str, int],
    left_weight: int = 1,
    right_weight: int = 1,
) -> dict[str, int]:
    return {
        edge: left_weight * left[edge] + right_weight * right[edge]
        for edge in STATE_EDGES
    }


def source_units(split_count: int) -> dict[str, int]:
    require(split_count in (0, 1, 2), "split count")
    scalar_values = 4 if split_count == 0 else 5
    strict_descent = 4 + split_count
    external_routes = 4 + split_count
    classifier = 0 if split_count == 0 else 1
    return {
        "scalar_value_records": scalar_values,
        "paid_strict_descent_records": strict_descent,
        "external_route_records": external_routes,
        "D3_D4_classifier_records": classifier,
        "total_differential_source_units": (
            scalar_values + strict_descent + external_routes + classifier
        ),
    }


def compile_manifest(root: Path) -> dict[str, Any]:
    face_source = load_json(root, FACE_COVER_PATH)
    route_source = load_json(root, ROUTE_GATE_PATH)
    transition_source = load_json(root, TRANSITION_PATH)

    require(
        face_source.get("schema")
        == "exact-recurrent-first-host-minimizer-face-scalar-route-cover/v1",
        "face-cover schema",
    )
    require(
        route_source.get("schema")
        == "exact-recurrent-first-host-closure-route-source-gate/v1",
        "route-gate schema",
    )
    require(
        transition_source.get("schema")
        == "exact-recurrent-first-host-transition-domain-source-audit/v1",
        "transition schema",
    )
    require(face_source.get("host_id") == HOST_ID, "face-cover host")
    require(
        transition_source.get("scope", {}).get("host_id") == HOST_ID,
        "transition host",
    )
    require(
        face_source.get("face_graph", {}).get("graph_type")
        == "complete-bipartite-K2,3",
        "K2,3 face graph",
    )
    require(
        face_source.get("aggregate", {}).get("acyclic_face_scalar_covers") == 46,
        "46 face covers",
    )
    require(
        face_source.get("aggregate", {}).get("menu_projectable_face_covers") == 14,
        "14 projectable covers",
    )
    require(
        face_source.get("aggregate", {}).get("background_sensitive_face_covers") == 32,
        "32 background-sensitive covers",
    )
    require(
        route_source.get("aggregate", {}).get("route_classes") == 5,
        "five route classes",
    )
    require(
        route_source.get("aggregate", {}).get("source_admissible_edge_route_pairs") == 0,
        "no source route assignments",
    )
    require(
        transition_source.get("aggregate", {}).get("required_promotion_fields_per_edge") == 12,
        "twelve transition fields",
    )
    require(
        transition_source.get("aggregate", {}).get("physical_directed_edges") == 0,
        "no physical directed edges",
    )

    covers: dict[tuple[int, ...], dict[str, Any]] = {}
    for bits in itertools.product((0, 1), repeat=len(PAIRS)):
        record = orientation_record(bits)
        if acyclic(record["paid"]):
            covers[bits] = record

    require(len(covers) == 46, "reconstructed 46 covers")
    projectable = [row for row in covers.values() if row["menu_projectable"]]
    sensitive = [row for row in covers.values() if not row["menu_projectable"]]
    require(len(projectable) == 14, "reconstructed projectable count")
    require(len(sensitive) == 32, "reconstructed sensitive count")

    source_registry = face_source.get("orientation_registry", {})
    source_ids = set(source_registry.get("ids", []))
    source_projectable_ids = set(source_registry.get("menu_projectable_ids", []))
    source_sensitive_ids = set(source_registry.get("background_sensitive_ids", []))
    reconstructed_ids = {row["cover_id"] for row in covers.values()}
    reconstructed_projectable_ids = {row["cover_id"] for row in projectable}
    reconstructed_sensitive_ids = {row["cover_id"] for row in sensitive}
    require(source_ids == reconstructed_ids, "source orientation ID registry")
    require(
        source_projectable_ids == reconstructed_projectable_ids,
        "source projectable ID registry",
    )
    require(
        source_sensitive_ids == reconstructed_sensitive_ids,
        "source sensitive ID registry",
    )

    decompositions: list[dict[str, Any]] = []
    profile_count = {"one_family_split": 0, "both_families_split": 0}
    for row in sorted(sensitive, key=lambda value: value["cover_id"]):
        d3_bits = complete_bits(row["bits"], "D3")
        d4_bits = complete_bits(row["bits"], "D4")
        require(d3_bits in covers, "D3 completion acyclic")
        require(d4_bits in covers, "D4 completion acyclic")
        d3 = covers[d3_bits]
        d4 = covers[d4_bits]
        require(d3["menu_projectable"], "D3 completion projectable")
        require(d4["menu_projectable"], "D4 completion projectable")
        require(d3["cover_id"] != d4["cover_id"], "distinct completions")

        four_sensitive = {
            edge: 4 * row["occurrence_vector"][edge]
            for edge in STATE_EDGES
        }
        convex_sum = add_vectors(
            d3["occurrence_vector"],
            d4["occurrence_vector"],
            left_weight=3,
            right_weight=1,
        )
        require(four_sensitive == convex_sum, "3/4-1/4 occurrence identity")

        split_count = int(row["split_changing"]) + int(row["split_neutral"])
        profile = "one_family_split" if split_count == 1 else "both_families_split"
        profile_count[profile] += 1
        decompositions.append(
            {
                "background_sensitive_cover_id": row["cover_id"],
                "D3_completion_cover_id": d3["cover_id"],
                "D4_completion_cover_id": d4["cover_id"],
                "convex_weights": {"D3_completion": "3/4", "D4_completion": "1/4"},
                "split_profile": profile,
                "source_units": source_units(split_count),
            }
        )

    require(
        profile_count == {"one_family_split": 24, "both_families_split": 8},
        "sensitive split distribution",
    )
    require(
        all(
            row["D3_completion_cover_id"] in reconstructed_projectable_ids
            and row["D4_completion_cover_id"] in reconstructed_projectable_ids
            for row in decompositions
        ),
        "all completions source-registered projectable covers",
    )

    decomposition_digest = hashlib.sha256(
        canonical_json(decompositions).encode()
    ).hexdigest()

    return {
        "schema": "exact-recurrent-first-host-minimizer-face-source-leverage/v1",
        "host_id": HOST_ID,
        "sources": {
            "minimizer_face_scalar_route_cover": str(FACE_COVER_PATH),
            "closure_route_source_gate": str(ROUTE_GATE_PATH),
            "transition_domain_source_audit": str(TRANSITION_PATH),
        },
        "class_blind_cost_theorem": {
            "cost_scope": (
                "nonnegative per-occurrence external-route costs depending on the "
                "directed menu-state edge but not on whether restore-both has face D3 or D4"
            ),
            "identity": "C(O)=3/4*C(O_D3)+1/4*C(O_D4)",
            "consequence": (
                "min(C(O_D3),C(O_D4)) <= C(O) for every background-sensitive cover O"
            ),
            "background_sensitive_covers_strictly_better_than_all_projectable_covers": 0,
            "background_sensitive_covers_with_projectable_no-worse_completion": 32,
        },
        "class_sensitive_cost_theorem": {
            "cost_scope": (
                "nonnegative external-route costs allowed to distinguish all six "
                "directed face-pair domains"
            ),
            "background_sensitive_covers_constructively_uniquely_optimal": 32,
            "construction": (
                "assign cost zero to the desired cover's external direction in each "
                "face pair and positive cost to every reverse direction"
            ),
            "physical_D3_D4_cost_or_route_asymmetry_required": 1,
        },
        "source_unit_contract": {
            "counting_rule": (
                "differential record units only; common occurrence-domain, owner, "
                "legality, boundedness, and realization contracts are required by all modes"
            ),
            "uniformity_rule": (
                "D3 and D4 share one descent or route record only when their directions "
                "agree and a source theorem is uniform over both face classes"
            ),
            "menu_projectable": {
                "covers": 14,
                **source_units(0),
            },
            "one_family_split": {
                "covers": 24,
                **source_units(1),
            },
            "both_families_split": {
                "covers": 8,
                **source_units(2),
            },
        },
        "D3_D4_classifier_contract": {
            "field_count": 8,
            "fields": [
                "physical_occurrence_domain_ref",
                "restore_both_state_domain_ref",
                "safe_background_or_equivalent_signature_ref",
                "D3_characterization_ref",
                "D4_characterization_ref",
                "disjointness_ref",
                "completeness_ref",
                "realization_status",
            ],
            "populated_fields": 0,
            "accepted_classifier_records": 0,
        },
        "decomposition_registry": {
            "records": decompositions,
            "record_count": len(decompositions),
            "digest": decomposition_digest,
        },
        "aggregate": {
            "face_scalar_covers": 46,
            "menu_projectable_covers": 14,
            "background_sensitive_covers": 32,
            "one_family_split_covers": 24,
            "both_families_split_covers": 8,
            "D3_completion_projectable": 32,
            "D4_completion_projectable": 32,
            "exact_convex_decompositions": 32,
            "class_blind_dominated_or_tied_sensitive_covers": 32,
            "class_blind_strictly_advantageous_sensitive_covers": 0,
            "class_sensitive_potentially_advantageous_sensitive_covers": 32,
            "minimum_projectable_differential_source_units": 12,
            "minimum_background_sensitive_differential_source_units": 16,
            "maximum_background_sensitive_differential_source_units": 18,
            "current_physical_face_classifications": 0,
            "current_source_face_scalar_values": 0,
            "current_source_face_edge_routes": 0,
            "current_physical_directed_edges": 0,
        },
        "source_boundary": {
            "background_sensitive_cover_admissible_without_D3_D4_classifier": 0,
            "background_sensitive_cover_preferred_by_class_blind_cost": 0,
            "class_sensitive_advantage_is_physical_evidence_dependent": 1,
            "route_burden_reduction_proved": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "physical_minimizer_face_classification_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def compare_exact(actual: dict[str, Any], expected: dict[str, Any]) -> None:
    require(actual == expected, "manifest differs from exact compiler output")


def mutation_tests(expected: dict[str, Any]) -> int:
    mutations = [
        ("cover count", ("aggregate", "face_scalar_covers"), 45),
        ("projectable count", ("aggregate", "menu_projectable_covers"), 13),
        ("sensitive count", ("aggregate", "background_sensitive_covers"), 31),
        ("one split", ("aggregate", "one_family_split_covers"), 23),
        ("both split", ("aggregate", "both_families_split_covers"), 7),
        ("D3 completion", ("aggregate", "D3_completion_projectable"), 31),
        ("D4 completion", ("aggregate", "D4_completion_projectable"), 31),
        ("convex count", ("aggregate", "exact_convex_decompositions"), 31),
        ("class blind advantage", ("aggregate", "class_blind_strictly_advantageous_sensitive_covers"), 1),
        ("minimum units", ("aggregate", "minimum_background_sensitive_differential_source_units"), 15),
        ("maximum units", ("aggregate", "maximum_background_sensitive_differential_source_units"), 17),
        ("classifier fields", ("D3_D4_classifier_contract", "field_count"), 7),
        ("classifier population", ("D3_D4_classifier_contract", "populated_fields"), 1),
        ("class-blind conclusion", ("class_blind_cost_theorem", "background_sensitive_covers_strictly_better_than_all_projectable_covers"), 1),
        ("class-sensitive count", ("class_sensitive_cost_theorem", "background_sensitive_covers_constructively_uniquely_optimal"), 31),
        ("route reduction", ("source_boundary", "route_burden_reduction_proved"), 1),
        ("closure promotion", ("source_boundary", "promotion_to_recurrent_closure_allowed"), 1),
        ("all-n", ("honesty", "all_n_proved_by_checker"), 1),
    ]
    rejected = 0
    for _, path, replacement in mutations:
        bad = copy.deepcopy(expected)
        node: Any = bad
        for key in path[:-1]:
            node = node[key]
        node[path[-1]] = replacement
        try:
            compare_exact(bad, expected)
        except AuditError:
            rejected += 1
    require(rejected == len(mutations), "mutation rejection count")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()

    expected = compile_manifest(args.root)
    rejected = mutation_tests(expected)

    if args.check:
        actual = json.loads(args.check.read_text(encoding="utf-8"))
        require(isinstance(actual, dict), "checked manifest object")
        compare_exact(actual, expected)
    if args.write:
        args.write.write_text(canonical_json(expected) + "\n", encoding="utf-8")

    print(
        "minimizer-face source leverage: "
        f"{expected['aggregate']['background_sensitive_covers']} sensitive covers, "
        f"{expected['aggregate']['exact_convex_decompositions']} convex decompositions, "
        f"{rejected} corruptions rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
