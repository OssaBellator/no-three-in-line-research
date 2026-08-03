#!/usr/bin/env python3
"""Compile the first-host context-parametric action-family import gate."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any, Callable

HOST_ID = "s4-75b04c45c1c8eac2"
SCHEMA = "exact-recurrent-first-host-context-parametric-family-import/v1"

CONGRUENCE_PATH = Path("data/exact_recurrent_first_host_action_family_congruence_obstruction.json")
LEVERAGE_PATH = Path("data/exact_recurrent_first_host_action_family_route_leverage.json")

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

UPSTREAM_SCHEMAS = (
    {
        "role": "occurrence_lineage_identity_and_routes",
        "source_branch": "research/alternating-core-chain",
        "document": "docs/alternating-core-occurrence-lineage-gates.md",
        "document_blob_sha": "9fef497dd4b3a7689b92c0a6c5fe0d1208b8922d",
        "local_document": 0,
        "candidate_evidence_fields": [
            "shared_owner_schema_ref",
            "shared_route_schema_ref",
        ],
        "boundary": (
            "registered continuation edges define same-owner identity and generic "
            "closure routes, but no first-host occurrence or family theorem is supplied"
        ),
    },
    {
        "role": "physical_signature_identity_payment_quotient",
        "source_branch": "research/alternating-core-chain",
        "document": "docs/alternating-core-physical-signature-lineage-quotient.md",
        "document_blob_sha": "51df0c27bd8d079768837d1a8bf9a295939f7835",
        "local_document": 0,
        "candidate_evidence_fields": [
            "shared_owner_schema_ref",
            "shared_route_schema_ref",
            "child_payment_compatibility_ref",
        ],
        "boundary": (
            "finite payment-complete signatures and shared quotient capacities are "
            "conditional; no first-host signature map or continuation edge is populated"
        ),
    },
    {
        "role": "boolean_context_boundary_routes",
        "source_branch": "research/alternating-core-chain",
        "document": "docs/alternating-core-boolean-boundary-gates.md",
        "document_blob_sha": "74b61c0f4ccfdcaba98249c06f2f37d44c53e622",
        "local_document": 0,
        "candidate_evidence_fields": [
            "shared_route_schema_ref",
        ],
        "boundary": (
            "fixed finite predicates have exact boundary gates and generic routes, "
            "but no physical first-host token or action-family theorem is identified"
        ),
    },
    {
        "role": "installed_operation_kind_registry",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "document": "docs/555-prime-power-installed-operation-registry-1166.md",
        "document_blob_sha": "fd5971338a71449bc03e759ceb350977001fe4d4",
        "local_document": 1,
        "required_markers": [
            "operation kinds = 1166",
            "Every entry has a literal nonempty",
            "Installed-bank exhaustiveness applies only",
        ],
        "candidate_evidence_fields": [
            "shared_operation_schema_ref",
        ],
        "boundary": (
            "the finite registry supplies kinds and continuation rules, not an "
            "occurrence-level mapping of either member edge of a first-host family"
        ),
    },
    {
        "role": "protected_interface_execution",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "document": "docs/490-prime-power-protected-interface-execution-ancestry.md",
        "document_blob_sha": "e57bc9a66dff826b3bb8e643d3a53e0a38b0cdae",
        "local_document": 1,
        "required_markers": [
            "side-five protected matching",
            "protected_interface_execution_ancestry_proved = 1",
            "global_transition_kind_bank_exhaustive = 0",
        ],
        "candidate_evidence_fields": [
            "shared_operation_schema_ref",
        ],
        "boundary": (
            "the execution theorem is a side-five protected-interface fixture and "
            "does not quantify over the first-host restoration context bit"
        ),
    },
    {
        "role": "inherited_coordinate_owner_and_row_schema",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "document": "docs/527-prime-power-inherited-coordinate-diagonal-block-ancestry.md",
        "document_blob_sha": "49d472aa0c5917d32f5f10738aace7e95a96801b",
        "local_document": 1,
        "required_markers": [
            "Every live physical credit has one persistent last-entering structural owner",
            "same_owner_diagonal_blocks_subcritical = 0",
            "actual_global_parent_rule_complete = 0",
        ],
        "candidate_evidence_fields": [
            "shared_owner_schema_ref",
            "child_payment_compatibility_ref",
        ],
        "boundary": (
            "owner DAGs and exact row schemas are available conditionally, while "
            "same-owner subcriticality and the actual parent rule remain open"
        ),
    },
    {
        "role": "owner_fate_child_payment_schema",
        "source_branch": "research/exact-recurrent-lyapunov-audit",
        "document": "docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md",
        "document_blob_sha": "ec44cff041306268b4ed8677b1ab17915cc99a0d",
        "local_document": 1,
        "required_markers": [
            "Every recurrent child coefficient has one exact compression key",
            "owner_fate_rows_populated_all_recurrent_states = 0",
            "compulsory_weighted_certificates_complete = 0",
        ],
        "candidate_evidence_fields": [
            "shared_owner_schema_ref",
            "child_payment_compatibility_ref",
        ],
        "boundary": (
            "lossless child/payment schemas are proved, but recurrent rows and "
            "compulsory weighted certificates are not populated for the first host"
        ),
    },
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


def verify_local_sources(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source in UPSTREAM_SCHEMAS:
        row = copy.deepcopy(source)
        markers = row.pop("required_markers", [])
        if row["local_document"]:
            path = root / row["document"]
            require(path.is_file(), f"missing local source document: {row['document']}")
            text = path.read_text()
            for marker in markers:
                require(marker in text, f"missing source marker {marker!r} in {row['document']}")
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


def compile_manifest(root: Path) -> dict[str, Any]:
    congruence = load_json(root, CONGRUENCE_PATH)
    leverage = load_json(root, LEVERAGE_PATH)

    require(congruence.get("host_id") == HOST_ID, "congruence host")
    require(leverage.get("host_id") == HOST_ID, "leverage host")
    require(congruence.get("aggregate", {}).get("action_families") == 4, "family census")
    require(
        congruence.get("uniform_family_contract", {}).get("field_count") == len(CONTRACT_FIELDS),
        "uniform family field count",
    )
    require(
        tuple(congruence.get("uniform_family_contract", {}).get("required_fields", []))
        == CONTRACT_FIELDS,
        "uniform family field order",
    )

    family_contract = leverage.get("family_contract", {})
    require(set(family_contract) == {"restore_02", "delete_02", "restore_20", "delete_20"}, "family bank")
    congruence_rows = {row["family"]: row for row in congruence.get("families", [])}
    require(set(congruence_rows) == set(family_contract), "congruence family bank")

    source_rows = verify_local_sources(root)
    candidate_roles_by_field: dict[str, list[str]] = {field: [] for field in EVIDENCE_FIELDS}
    for source in source_rows:
        for field in source["candidate_evidence_fields"]:
            require(field in EVIDENCE_FIELDS, "candidate evidence field")
            candidate_roles_by_field[field].append(source["role"])

    family_rows: list[dict[str, Any]] = []
    for family in sorted(family_contract):
        contract = family_contract[family]
        geometry = congruence_rows[family]
        bit = contract["bit"]
        quantified_context_bit = "r20" if bit == "02" else "r02"
        structural = {
            "family_id": family,
            "edge_refs": list(contract["directed_edges"]),
            "quantified_context_bit": quantified_context_bit,
        }
        evidence = {field: None for field in EVIDENCE_FIELDS}
        require(geometry["other_context_bit"] == quantified_context_bit, f"context bit: {family}")
        require([member["edge"] for member in geometry["members"]] == structural["edge_refs"], f"edge refs: {family}")
        family_rows.append(
            {
                "family": family,
                "changed_cell": bit,
                "action": contract["action"],
                "structural_fields": structural,
                "source_evidence_fields": evidence,
                "structural_field_count": len(STRUCTURAL_FIELDS),
                "source_evidence_field_count": len(EVIDENCE_FIELDS),
                "source_evidence_populated": 0,
                "total_contract_fields_populated": len(STRUCTURAL_FIELDS),
                "context_parametric_family_imported": 0,
                "separate_member_edge_record_field_slots": 24,
                "candidate_source_roles_by_evidence_field": candidate_roles_by_field,
            }
        )

    minimal_sets = leverage.get("minimal_complete_family_sets", [])
    expected_sets = [
        ["delete_02", "delete_20"],
        ["delete_02", "restore_20"],
        ["restore_02", "delete_20"],
        ["restore_02", "restore_20"],
    ]
    require(minimal_sets == expected_sets, "minimal family sets")

    minimal_rows = [
        {
            "families": pair,
            "family_count": 2,
            "structurally_prefilled_contract_slots": 2 * len(STRUCTURAL_FIELDS),
            "remaining_source_evidence_slots": 2 * len(EVIDENCE_FIELDS),
            "separate_edge_record_field_slots": 48,
            "currently_imported_families": 0,
            "current_scalar_closure": 0,
        }
        for pair in minimal_sets
    ]

    evidence_audit = [
        {
            "field": field,
            "geometry_prefilled": 0,
            "candidate_abstract_schema_roles": candidate_roles_by_field[field],
            "candidate_abstract_schema_role_count": len(candidate_roles_by_field[field]),
            "source_populated_first_host_value": 0,
        }
        for field in EVIDENCE_FIELDS
    ]

    return {
        "schema": SCHEMA,
        "host_id": HOST_ID,
        "sources": {
            "action_family_congruence": str(CONGRUENCE_PATH),
            "action_family_leverage": str(LEVERAGE_PATH),
        },
        "aggregate": {
            "action_families": 4,
            "contract_fields_per_family": len(CONTRACT_FIELDS),
            "structural_fields_per_family": len(STRUCTURAL_FIELDS),
            "source_evidence_fields_per_family": len(EVIDENCE_FIELDS),
            "total_contract_field_slots": 4 * len(CONTRACT_FIELDS),
            "structurally_prefilled_field_slots": 4 * len(STRUCTURAL_FIELDS),
            "source_evidence_field_slots": 4 * len(EVIDENCE_FIELDS),
            "source_evidence_field_slots_populated": 0,
            "fully_imported_families": 0,
            "upstream_schema_layers_audited": len(source_rows),
            "external_blob_schema_layers": sum(not row["local_document"] for row in source_rows),
            "local_marker_audited_schema_layers": sum(row["local_document"] for row in source_rows),
            "minimal_scalar_closure_family_sets": len(minimal_sets),
            "families_per_minimal_scalar_closure": 2,
            "structural_slots_per_minimal_scalar_closure": 2 * len(STRUCTURAL_FIELDS),
            "remaining_evidence_slots_per_minimal_scalar_closure": 2 * len(EVIDENCE_FIELDS),
            "separate_edge_record_slots_per_minimal_scalar_closure": 48,
        },
        "structural_prefill": {
            "fields": list(STRUCTURAL_FIELDS),
            "derivation": (
                "family identity, its two directed member edges, and the other restoration "
                "bit are fixed by the exact action-family geometry"
            ),
            "physical_evidence_waived": 0,
        },
        "remaining_source_evidence_contract": {
            "fields": list(EVIDENCE_FIELDS),
            "field_count": len(EVIDENCE_FIELDS),
            "acceptance_rule": (
                "all seven fields must be source-backed for one occurrence-faithful theorem "
                "covering both context values; abstract schemas alone do not populate them"
            ),
        },
        "upstream_schema_audit": source_rows,
        "evidence_field_audit": evidence_audit,
        "families": family_rows,
        "minimal_scalar_closure_import_sets": minimal_rows,
        "conclusion": {
            "geometry_prefills_three_contract_fields_per_family": 1,
            "abstract_owner_operation_route_child_payment_schemas_available": 1,
            "family_specific_context_parametric_theorems_found": 0,
            "source_evidence_fields_populated": 0,
            "context_parametric_families_imported": 0,
            "one_imported_family_suffices_for_scalar_closure": 0,
            "two_cross_bit_imported_families_suffice_for_scalar_closure": 1,
            "minimum_missing_source_evidence_slots_for_scalar_closure": 14,
            "structural_prefill_counts_as_physical_proof": 0,
            "external_abstract_theorem_counts_as_occurrence_record": 0,
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


def validate_manifest(value: dict[str, Any]) -> None:
    require(value.get("schema") == SCHEMA, "schema")
    require(value.get("host_id") == HOST_ID, "host")
    aggregate = value.get("aggregate", {})
    require(aggregate.get("action_families") == 4, "aggregate families")
    require(aggregate.get("contract_fields_per_family") == 10, "contract fields")
    require(aggregate.get("structural_fields_per_family") == 3, "structural fields")
    require(aggregate.get("source_evidence_fields_per_family") == 7, "evidence fields")
    require(aggregate.get("total_contract_field_slots") == 40, "total slots")
    require(aggregate.get("structurally_prefilled_field_slots") == 12, "prefilled slots")
    require(aggregate.get("source_evidence_field_slots") == 28, "evidence slots")
    require(aggregate.get("source_evidence_field_slots_populated") == 0, "populated evidence")
    require(aggregate.get("fully_imported_families") == 0, "imported families")
    require(aggregate.get("upstream_schema_layers_audited") == 7, "source layers")
    require(aggregate.get("external_blob_schema_layers") == 3, "external layers")
    require(aggregate.get("local_marker_audited_schema_layers") == 4, "local layers")
    require(aggregate.get("minimal_scalar_closure_family_sets") == 4, "minimal sets")
    require(aggregate.get("remaining_evidence_slots_per_minimal_scalar_closure") == 14, "closure evidence")
    require(aggregate.get("separate_edge_record_slots_per_minimal_scalar_closure") == 48, "edge slots")

    source_rows = value.get("upstream_schema_audit", [])
    require(len(source_rows) == 7, "source row count")
    expected_shas = {row["role"]: row["document_blob_sha"] for row in UPSTREAM_SCHEMAS}
    require({row["role"]: row["document_blob_sha"] for row in source_rows} == expected_shas, "source blob pins")
    for row in source_rows:
        require(row.get("first_host_family_records") == 0, "source family records")
        require(row.get("context_parametric_family_theorems") == 0, "source family theorem")
        require(row.get("occurrence_faithful_family_join") == 0, "source family join")
        if row["local_document"]:
            require(row.get("local_markers_verified") == 1, "local markers")
        else:
            require(row.get("local_markers_verified") == 0, "external marker status")

    family_contract = {
        "delete_02": (["10->00", "11->01"], "r20"),
        "delete_20": (["01->00", "11->10"], "r02"),
        "restore_02": (["00->10", "01->11"], "r20"),
        "restore_20": (["00->01", "10->11"], "r02"),
    }
    families = value.get("families", [])
    require([row["family"] for row in families] == sorted(family_contract), "family order")
    for row in families:
        edges, context_bit = family_contract[row["family"]]
        structural = row["structural_fields"]
        require(structural["family_id"] == row["family"], "family id")
        require(structural["edge_refs"] == edges, "family edges")
        require(structural["quantified_context_bit"] == context_bit, "family context")
        require(set(row["source_evidence_fields"]) == set(EVIDENCE_FIELDS), "family evidence bank")
        require(all(v is None for v in row["source_evidence_fields"].values()), "family evidence values")
        require(row["structural_field_count"] == 3, "family structural count")
        require(row["source_evidence_field_count"] == 7, "family evidence count")
        require(row["source_evidence_populated"] == 0, "family evidence populated")
        require(row["total_contract_fields_populated"] == 3, "family total populated")
        require(row["context_parametric_family_imported"] == 0, "family import")
        require(row["separate_member_edge_record_field_slots"] == 24, "family separate slots")

    expected_sets = [
        ["delete_02", "delete_20"],
        ["delete_02", "restore_20"],
        ["restore_02", "delete_20"],
        ["restore_02", "restore_20"],
    ]
    minimal = value.get("minimal_scalar_closure_import_sets", [])
    require([row["families"] for row in minimal] == expected_sets, "minimal closure rows")
    for row in minimal:
        require(row["structurally_prefilled_contract_slots"] == 6, "minimal structural slots")
        require(row["remaining_source_evidence_slots"] == 14, "minimal evidence slots")
        require(row["separate_edge_record_field_slots"] == 48, "minimal edge fields")
        require(row["currently_imported_families"] == 0, "minimal imported")
        require(row["current_scalar_closure"] == 0, "minimal current closure")

    conclusion = value.get("conclusion", {})
    require(conclusion.get("geometry_prefills_three_contract_fields_per_family") == 1, "prefill conclusion")
    require(conclusion.get("family_specific_context_parametric_theorems_found") == 0, "theorem conclusion")
    require(conclusion.get("source_evidence_fields_populated") == 0, "evidence conclusion")
    require(conclusion.get("context_parametric_families_imported") == 0, "import conclusion")
    require(conclusion.get("minimum_missing_source_evidence_slots_for_scalar_closure") == 14, "minimum evidence")
    require(conclusion.get("structural_prefill_counts_as_physical_proof") == 0, "prefill honesty")
    require(conclusion.get("external_abstract_theorem_counts_as_occurrence_record") == 0, "external honesty")
    require(conclusion.get("promotion_to_recurrent_closure_allowed") == 0, "promotion")

    honesty = value.get("honesty", {})
    require(honesty and all(v == 0 for v in honesty.values()), "honesty flags")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations: list[Callable[[dict[str, Any]], None]] = [
        lambda x: x.__setitem__("schema", "broken"),
        lambda x: x["aggregate"].__setitem__("total_contract_field_slots", 39),
        lambda x: x["aggregate"].__setitem__("source_evidence_field_slots_populated", 1),
        lambda x: x["aggregate"].__setitem__("remaining_evidence_slots_per_minimal_scalar_closure", 13),
        lambda x: x["upstream_schema_audit"][0].__setitem__("document_blob_sha", "0" * 40),
        lambda x: x["upstream_schema_audit"][3].__setitem__("local_markers_verified", 0),
        lambda x: x["upstream_schema_audit"][0].__setitem__("first_host_family_records", 1),
        lambda x: x["families"][0]["structural_fields"].__setitem__("family_id", "restore_02"),
        lambda x: x["families"][0]["structural_fields"]["edge_refs"].__setitem__(0, "00->11"),
        lambda x: x["families"][0]["structural_fields"].__setitem__("quantified_context_bit", "r02"),
        lambda x: x["families"][0]["source_evidence_fields"].__setitem__("shared_theorem_ref", "unsourced"),
        lambda x: x["families"][0].__setitem__("context_parametric_family_imported", 1),
        lambda x: x["families"][0].__setitem__("total_contract_fields_populated", 4),
        lambda x: x["minimal_scalar_closure_import_sets"][0].__setitem__("remaining_source_evidence_slots", 12),
        lambda x: x["conclusion"].__setitem__("promotion_to_recurrent_closure_allowed", 1),
        lambda x: x["honesty"].__setitem__("all_n_proved_by_checker", 1),
    ]
    rejected = 0
    for mutate in mutations:
        broken = copy.deepcopy(manifest)
        mutate(broken)
        try:
            validate_manifest(broken)
        except AuditError:
            rejected += 1
    require(rejected == len(mutations), "mutation rejection census")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    manifest = compile_manifest(args.root)
    validate_manifest(manifest)
    rejected = mutation_audit(manifest)

    if args.check is not None:
        expected = json.loads(args.check.read_text())
        require(manifest == expected, "manifest mismatch")
        print(
            "context-parametric family import gate: "
            f"{manifest['aggregate']['structurally_prefilled_field_slots']} structural slots, "
            f"{manifest['aggregate']['source_evidence_field_slots_populated']}/"
            f"{manifest['aggregate']['source_evidence_field_slots']} evidence slots populated, "
            f"{rejected} corruptions rejected"
        )
    else:
        print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
