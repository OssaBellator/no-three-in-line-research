#!/usr/bin/env python3
"""Compile the first-host action-family context-parametric source import gate."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
SCHEMA = "exact-recurrent-first-host-action-family-source-import-gate/v2"

CONGRUENCE_PATH = Path("data/exact_recurrent_first_host_action_family_congruence_obstruction.json")
TRANSITION_PATH = Path("data/exact_recurrent_first_host_transition_domain_source_audit.json")
LEVERAGE_PATH = Path("data/exact_recurrent_first_host_action_family_route_leverage.json")

FAMILIES = (
    {
        "family_id": "restore_02",
        "changed_cell": "02",
        "action": "restore",
        "edge_refs": ["00->10", "01->11"],
        "quantified_context_bit": "r20",
    },
    {
        "family_id": "delete_02",
        "changed_cell": "02",
        "action": "delete",
        "edge_refs": ["10->00", "11->01"],
        "quantified_context_bit": "r20",
    },
    {
        "family_id": "restore_20",
        "changed_cell": "20",
        "action": "restore",
        "edge_refs": ["00->01", "10->11"],
        "quantified_context_bit": "r02",
    },
    {
        "family_id": "delete_20",
        "changed_cell": "20",
        "action": "delete",
        "edge_refs": ["01->00", "11->10"],
        "quantified_context_bit": "r02",
    },
)

CONTRACT_FIELDS = (
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
STRUCTURAL_FIELDS = (
    "family_id",
    "edge_refs",
    "quantified_context_bit",
)
EVIDENCE_FIELDS = tuple(field for field in CONTRACT_FIELDS if field not in STRUCTURAL_FIELDS)

COMPONENTS = (
    "context_quantification",
    "owner_continuation",
    "operation_schema",
    "closure_route_schema",
    "child_payment_schema",
)

UPSTREAM = (
    {
        "role": "boolean_boundary_context",
        "source_branch": "research/alternating-core-chain",
        "doc_path": "docs/alternating-core-boolean-boundary-gates.md",
        "doc_blob_sha": "74b61c0f4ccfdcaba98249c06f2f37d44c53e622",
        "local_document": 0,
        "capabilities": ["context_quantification", "closure_route_schema"],
        "boundary": (
            "fixed-token Boolean boundary and route theorem; no first-host owner, "
            "operation, child row or family mapping"
        ),
    },
    {
        "role": "occurrence_lineage",
        "source_branch": "research/alternating-core-chain",
        "doc_path": "docs/alternating-core-occurrence-lineage-gates.md",
        "doc_blob_sha": "9fef497dd4b3a7689b92c0a6c5fe0d1208b8922d",
        "local_document": 0,
        "capabilities": ["owner_continuation", "closure_route_schema"],
        "boundary": (
            "declared continuation-edge identity wall; no first-host continuation "
            "relation or context-family theorem"
        ),
    },
    {
        "role": "physical_signature_quotient",
        "source_branch": "research/alternating-core-chain",
        "doc_path": "docs/alternating-core-physical-signature-lineage-quotient.md",
        "doc_blob_sha": "51df0c27bd8d079768837d1a8bf9a295939f7835",
        "local_document": 0,
        "capabilities": ["owner_continuation", "closure_route_schema"],
        "boundary": (
            "finite payment-complete signature quotient contract; no first-host "
            "signature map or family edge"
        ),
    },
    {
        "role": "installed_operation_registry",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "doc_path": "docs/555-prime-power-installed-operation-registry-1166.md",
        "doc_blob_sha": "fd5971338a71449bc03e759ceb350977001fe4d4",
        "local_document": 1,
        "required_markers": [
            "operation kinds = 1166",
            "Every entry has a literal nonempty",
            "Installed-bank exhaustiveness applies only",
        ],
        "capabilities": ["operation_schema"],
        "boundary": (
            "1166 declared operation kinds and continuation rules; not an "
            "occurrence-level edge mapping"
        ),
    },
    {
        "role": "inherited_coordinate_diagonal_block",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "doc_path": "docs/527-prime-power-inherited-coordinate-diagonal-block-ancestry.md",
        "doc_blob_sha": "49d472aa0c5917d32f5f10738aace7e95a96801b",
        "local_document": 1,
        "required_markers": [
            "Every live physical credit has one persistent last-entering structural owner",
            "same_owner_diagonal_blocks_subcritical = 0",
            "actual_global_parent_rule_complete = 0",
        ],
        "capabilities": ["owner_continuation", "child_payment_schema"],
        "boundary": (
            "owner DAG and exact-row/upper-quotient schema; same-owner blocks and "
            "global parent rule remain open"
        ),
    },
    {
        "role": "owner_fate_lineage_kernel",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "doc_path": "docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md",
        "doc_blob_sha": "ec44cff041306268b4ed8677b1ab17915cc99a0d",
        "local_document": 1,
        "required_markers": [
            "Every recurrent child coefficient has one exact compression key",
            "owner_fate_rows_populated_all_recurrent_states = 0",
            "compulsory_weighted_certificates_complete = 0",
        ],
        "capabilities": ["child_payment_schema"],
        "boundary": (
            "lossless row keys and compulsory weighted-certificate schema; recurrent "
            "rows remain unpopulated"
        ),
    },
    {
        "role": "protected_interface_execution",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "doc_path": "docs/490-prime-power-protected-interface-execution-ancestry.md",
        "doc_blob_sha": "e57bc9a66dff826b3bb8e643d3a53e0a38b0cdae",
        "local_document": 1,
        "required_markers": [
            "side-five protected matching",
            "protected_interface_execution_ancestry_proved = 1",
            "global_transition_kind_bank_exhaustive = 0",
        ],
        "capabilities": ["operation_schema"],
        "boundary": (
            "side-five execution fixture and factorization theorem; no first-host "
            "state or edge record"
        ),
    },
)

CANDIDATE_SCHEMA_ROLES = {
    "shared_owner_schema_ref": [
        "occurrence_lineage",
        "physical_signature_quotient",
        "inherited_coordinate_diagonal_block",
    ],
    "shared_operation_schema_ref": [
        "installed_operation_registry",
        "protected_interface_execution",
    ],
    "shared_route_schema_ref": [
        "boolean_boundary_context",
        "occurrence_lineage",
        "physical_signature_quotient",
    ],
    "child_payment_compatibility_ref": [
        "inherited_coordinate_diagonal_block",
        "owner_fate_lineage_kernel",
    ],
}

EXPECTED_MINIMAL_FAMILY_SETS = [
    ["delete_02", "delete_20"],
    ["delete_02", "restore_20"],
    ["restore_02", "delete_20"],
    ["restore_02", "restore_20"],
]


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


def audit_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], int]:
    congruence = load_json(root, CONGRUENCE_PATH)
    transition = load_json(root, TRANSITION_PATH)
    leverage = load_json(root, LEVERAGE_PATH)

    require(congruence.get("host_id") == HOST_ID, "congruence host")
    require(transition.get("scope", {}).get("host_id") == HOST_ID, "transition host")
    require(leverage.get("host_id") == HOST_ID, "leverage host")

    uniform = congruence.get("uniform_family_contract", {})
    require(uniform.get("field_count") == len(CONTRACT_FIELDS), "uniform field count")
    require(tuple(uniform.get("required_fields", [])) == CONTRACT_FIELDS, "uniform field order")
    require(congruence.get("aggregate", {}).get("source_uniformity_records_populated") == 0, "uniformity source state")

    edge_field_count = transition.get("promotion_contract", {}).get("field_count")
    require(edge_field_count == 12, "edge promotion field count")
    require(transition.get("aggregate", {}).get("physical_directed_edges") == 0, "physical edge state")
    require(transition.get("aggregate", {}).get("physical_menu_states") == 0, "physical state census")

    require(leverage.get("aggregate", {}).get("minimum_families_for_label_cover") == 2, "label family minimum")
    require(leverage.get("aggregate", {}).get("minimum_families_for_menu_cover") == 2, "menu family minimum")
    require(leverage.get("minimal_complete_family_sets") == EXPECTED_MINIMAL_FAMILY_SETS, "minimal family sets")

    leverage_contract = leverage.get("family_contract", {})
    congruence_rows = {row["family"]: row for row in congruence.get("families", [])}
    require(set(leverage_contract) == {row["family_id"] for row in FAMILIES}, "leverage family bank")
    require(set(congruence_rows) == set(leverage_contract), "congruence family bank")
    for family in FAMILIES:
        family_id = family["family_id"]
        require(leverage_contract[family_id]["directed_edges"] == family["edge_refs"], f"leverage edges: {family_id}")
        require(congruence_rows[family_id]["other_context_bit"] == family["quantified_context_bit"], f"context bit: {family_id}")
        require(
            [member["edge"] for member in congruence_rows[family_id]["members"]] == family["edge_refs"],
            f"congruence edges: {family_id}",
        )
    return congruence, transition, leverage, edge_field_count


def audit_upstream_sources(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source in UPSTREAM:
        row = copy.deepcopy(source)
        markers = row.pop("required_markers", [])
        if row["local_document"]:
            path = root / row["doc_path"]
            require(path.is_file(), f"missing local source: {row['doc_path']}")
            text = path.read_text()
            for marker in markers:
                require(marker in text, f"missing marker {marker!r} in {row['doc_path']}")
            row["local_markers_verified"] = 1
            row["verified_marker_count"] = len(markers)
        else:
            row["local_markers_verified"] = 0
            row["verified_marker_count"] = 0
        row["first_host_family_records"] = 0
        row["context_parametric_family_theorems"] = 0
        row["occurrence_faithful_family_join"] = 0
        rows.append(row)
    return rows


def minimum_component_cover(upstream_rows: list[dict[str, Any]]) -> tuple[int, list[list[str]]]:
    rows = []
    for size in range(1, len(upstream_rows) + 1):
        for subset in itertools.combinations(upstream_rows, size):
            covered = set().union(*(set(row["capabilities"]) for row in subset))
            if covered == set(COMPONENTS):
                rows.append(sorted(row["role"] for row in subset))
        if rows:
            return size, sorted(rows)
    raise AuditError("abstract component cover absent")


def compile_manifest(root: Path) -> dict[str, Any]:
    _, _, leverage, edge_field_count = audit_inputs(root)
    upstream_rows = audit_upstream_sources(root)

    roles = [row["role"] for row in upstream_rows]
    require(len(roles) == len(set(roles)) == 7, "upstream role census")
    require(all(set(row["capabilities"]) <= set(COMPONENTS) for row in upstream_rows), "unknown capability")

    union_capabilities = sorted(set().union(*(set(row["capabilities"]) for row in upstream_rows)))
    require(union_capabilities == sorted(COMPONENTS), "abstract component union")
    minimum_sources, minimum_covers = minimum_component_cover(upstream_rows)
    require(minimum_sources == 3, "minimum abstract source cover")
    require(len(minimum_covers) == 2, "minimum abstract cover census")

    capability_counts = {
        component: sum(component in row["capabilities"] for row in upstream_rows)
        for component in COMPONENTS
    }
    require(
        capability_counts
        == {
            "context_quantification": 1,
            "owner_continuation": 3,
            "operation_schema": 2,
            "closure_route_schema": 3,
            "child_payment_schema": 2,
        },
        "capability census",
    )

    family_rows = []
    for family in FAMILIES:
        structural = {
            "family_id": family["family_id"],
            "edge_refs": list(family["edge_refs"]),
            "quantified_context_bit": family["quantified_context_bit"],
        }
        evidence = {field: None for field in EVIDENCE_FIELDS}
        family_rows.append(
            {
                **family,
                "structural_fields": structural,
                "structural_fields_populated": len(structural),
                "evidence_fields": evidence,
                "evidence_fields_populated": 0,
                "abstract_schema_candidate_roles": CANDIDATE_SCHEMA_ROLES,
                "selected_source_backed_schema_refs": 0,
                "family_import_accepted": 0,
                "separate_member_edge_record_field_slots": 2 * edge_field_count,
            }
        )

    require(len({row["family_id"] for row in family_rows}) == 4, "family census")
    require(all(len(row["edge_refs"]) == 2 for row in family_rows), "two-edge families")
    require(all(row["structural_fields_populated"] == 3 for row in family_rows), "structural field count")
    require(all(row["evidence_fields_populated"] == 0 for row in family_rows), "evidence emptiness")

    minimal_rows = [
        {
            "families": pair,
            "family_count": 2,
            "theorem_contract_field_slots": 2 * len(CONTRACT_FIELDS),
            "structurally_prefilled_field_slots": 2 * len(STRUCTURAL_FIELDS),
            "remaining_source_evidence_field_slots": 2 * len(EVIDENCE_FIELDS),
            "separate_edge_record_field_slots": 4 * edge_field_count,
            "currently_imported_families": 0,
            "current_scalar_closure": 0,
        }
        for pair in leverage["minimal_complete_family_sets"]
    ]

    return {
        "schema": SCHEMA,
        "host_id": HOST_ID,
        "sources": {
            "family_congruence": str(CONGRUENCE_PATH),
            "transition_domain": str(TRANSITION_PATH),
            "family_leverage": str(LEVERAGE_PATH),
        },
        "contract": {
            "all_fields": list(CONTRACT_FIELDS),
            "structural_fields": list(STRUCTURAL_FIELDS),
            "evidence_fields": list(EVIDENCE_FIELDS),
            "acceptance_rule": (
                "geometry fixes family identity, both exact edge members and the other context bit; "
                "a source import is accepted only when all seven evidence fields are populated and "
                "the theorem proves both context values for the same occurrence-faithful owner lineage"
            ),
            "structural_prefill_counts_as_physical_evidence": 0,
        },
        "upstream_interfaces": upstream_rows,
        "abstract_component_analysis": {
            "components": list(COMPONENTS),
            "union_components_covered": len(union_capabilities),
            "union_component_set_complete": 1,
            "minimum_sources_to_cover_abstract_components": minimum_sources,
            "minimum_source_covers": minimum_covers,
            "capability_counts": capability_counts,
            "single_source_covers_all_components": 0,
            "abstract_union_implies_first_host_import": 0,
        },
        "families": family_rows,
        "minimal_scalar_closure_import_sets": minimal_rows,
        "aggregate": {
            "action_families": len(family_rows),
            "uniformity_fields_per_family": len(CONTRACT_FIELDS),
            "structural_fields_per_family": len(STRUCTURAL_FIELDS),
            "evidence_fields_per_family": len(EVIDENCE_FIELDS),
            "total_contract_field_slots": len(family_rows) * len(CONTRACT_FIELDS),
            "structural_fields_populated_total": len(family_rows) * len(STRUCTURAL_FIELDS),
            "source_evidence_field_slots_total": len(family_rows) * len(EVIDENCE_FIELDS),
            "evidence_fields_populated_total": 0,
            "abstract_schema_component_types": len(COMPONENTS),
            "abstract_schema_component_types_covered": len(union_capabilities),
            "upstream_interfaces_audited": len(upstream_rows),
            "external_blob_interfaces": sum(not row["local_document"] for row in upstream_rows),
            "local_marker_audited_interfaces": sum(row["local_document"] for row in upstream_rows),
            "first_host_family_theorems_found": 0,
            "source_backed_uniform_family_imports": 0,
            "minimum_uniform_family_imports_for_scalar_cover": 2,
            "minimal_scalar_closure_import_sets": len(minimal_rows),
            "theorem_contract_slots_per_minimal_scalar_cover": 2 * len(CONTRACT_FIELDS),
            "structural_slots_per_minimal_scalar_cover": 2 * len(STRUCTURAL_FIELDS),
            "remaining_evidence_slots_per_minimal_scalar_cover": 2 * len(EVIDENCE_FIELDS),
            "separate_edge_record_slots_per_minimal_scalar_cover": 4 * edge_field_count,
        },
        "conclusion": {
            "normalized_family_structure_complete": 1,
            "geometry_prefills_three_fields_per_family": 1,
            "abstract_contract_components_available_in_union": 1,
            "abstract_contract_components_joined_occurrence_faithfully": 0,
            "context_parametric_first_host_theorem_found": 0,
            "one_operation_kind_name_proves_family_uniformity": 0,
            "one_abstract_source_covers_full_family_contract": 0,
            "minimum_missing_source_evidence_slots_for_scalar_closure": 14,
            "external_abstract_theorem_counts_as_occurrence_record": 0,
            "current_uniform_family_import_allowed": 0,
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


def validate_manifest(data: dict[str, Any], root: Path) -> None:
    require(data == compile_manifest(root), "manifest differs from deterministic compiler")


def mutation_audit(expected: dict[str, Any], root: Path) -> int:
    mutants = []

    def add(mutator) -> None:
        candidate = copy.deepcopy(expected)
        mutator(candidate)
        mutants.append(candidate)

    add(lambda x: x.__setitem__("schema", "broken"))
    add(lambda x: x["aggregate"].__setitem__("evidence_fields_per_family", 6))
    add(lambda x: x["aggregate"].__setitem__("total_contract_field_slots", 39))
    add(lambda x: x["aggregate"].__setitem__("source_evidence_field_slots_total", 27))
    add(lambda x: x["aggregate"].__setitem__("remaining_evidence_slots_per_minimal_scalar_cover", 13))
    add(lambda x: x["aggregate"].__setitem__("first_host_family_theorems_found", 1))
    add(lambda x: x["conclusion"].__setitem__("current_uniform_family_import_allowed", 1))
    add(lambda x: x["conclusion"].__setitem__("abstract_contract_components_joined_occurrence_faithfully", 1))
    add(lambda x: x["honesty"].__setitem__("all_n_proved_by_checker", 1))
    add(lambda x: x["families"][0]["evidence_fields"].__setitem__("shared_theorem_ref", "invented"))
    add(lambda x: x["families"][1].__setitem__("family_import_accepted", 1))
    add(lambda x: x["families"][2]["structural_fields"].__setitem__("quantified_context_bit", "r20"))
    add(lambda x: x["families"][3]["edge_refs"].pop())
    add(lambda x: x["upstream_interfaces"][0]["capabilities"].append("operation_schema"))
    add(lambda x: x["upstream_interfaces"][3].__setitem__("doc_blob_sha", "0" * 40))
    add(lambda x: x["upstream_interfaces"][3].__setitem__("local_markers_verified", 0))
    add(lambda x: x["abstract_component_analysis"].__setitem__("minimum_sources_to_cover_abstract_components", 2))
    add(lambda x: x["minimal_scalar_closure_import_sets"][0].__setitem__("remaining_source_evidence_field_slots", 12))

    rejected = 0
    for candidate in mutants:
        try:
            validate_manifest(candidate, root)
        except AuditError:
            rejected += 1
    require(rejected == len(mutants), "mutation audit")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    manifest = compile_manifest(args.root)
    rejected = mutation_audit(manifest, args.root)

    if args.check:
        validate_manifest(json.loads(args.check.read_text()), args.root)
        print(
            "action-family source import gate: "
            f"{manifest['aggregate']['structural_fields_populated_total']}/"
            f"{manifest['aggregate']['total_contract_field_slots']} structural slots fixed, "
            f"{manifest['aggregate']['evidence_fields_populated_total']}/"
            f"{manifest['aggregate']['source_evidence_field_slots_total']} evidence slots populated, "
            f"{rejected} corruptions rejected"
        )
    if args.write:
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    if not args.check and not args.write:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
