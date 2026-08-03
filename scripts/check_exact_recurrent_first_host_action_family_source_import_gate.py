#!/usr/bin/env python3
"""Compile the first-host action-family context-parametric source import gate."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path

HOST_ID = "s4-75b04c45c1c8eac2"

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

STRUCTURAL_FIELDS = (
    "family_id",
    "edge_refs",
    "quantified_context_bit",
)
EVIDENCE_FIELDS = (
    "shared_theorem_ref",
    "both_context_values_proved",
    "shared_owner_schema_ref",
    "shared_operation_schema_ref",
    "shared_route_schema_ref",
    "child_payment_compatibility_ref",
    "realization_status",
)
ALL_FIELDS = STRUCTURAL_FIELDS + EVIDENCE_FIELDS

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
        "doc_path": "docs/alternating-core-boolean-boundary-gates.md",
        "doc_blob_sha": "74b61c0f4ccfdcaba98249c06f2f37d44c53e622",
        "capabilities": ["context_quantification", "closure_route_schema"],
        "boundary": "fixed-token Boolean boundary and route theorem; no first-host owner, operation, child row or family mapping",
    },
    {
        "role": "occurrence_lineage",
        "doc_path": "docs/alternating-core-occurrence-lineage-gates.md",
        "doc_blob_sha": "9fef497dd4b3a7689b92c0a6c5fe0d1208b8922d",
        "capabilities": ["owner_continuation", "closure_route_schema"],
        "boundary": "declared continuation-edge identity wall; no first-host continuation relation or context-family theorem",
    },
    {
        "role": "physical_signature_quotient",
        "doc_path": "docs/alternating-core-physical-signature-lineage-quotient.md",
        "doc_blob_sha": "51df0c27bd8d079768837d1a8bf9a295939f7835",
        "capabilities": ["owner_continuation", "closure_route_schema"],
        "boundary": "finite payment-complete signature quotient contract; no first-host signature map or family edge",
    },
    {
        "role": "installed_operation_registry",
        "doc_path": "docs/555-prime-power-installed-operation-registry-1166.md",
        "doc_blob_sha": "fd5971338a71449bc03e759ceb350977001fe4d4",
        "capabilities": ["operation_schema"],
        "boundary": "1166 declared operation kinds and continuation rules; not an occurrence-level edge mapping",
    },
    {
        "role": "inherited_coordinate_diagonal_block",
        "doc_path": "docs/527-prime-power-inherited-coordinate-diagonal-block-ancestry.md",
        "doc_blob_sha": "49d472aa0c5917d32f5f10738aace7e95a96801b",
        "capabilities": ["owner_continuation", "child_payment_schema"],
        "boundary": "owner DAG and exact-row/upper-quotient schema; same-owner blocks and global parent rule remain open",
    },
    {
        "role": "owner_fate_lineage_kernel",
        "doc_path": "docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md",
        "doc_blob_sha": "ec44cff041306268b4ed8677b1ab17915cc99a0d",
        "capabilities": ["child_payment_schema"],
        "boundary": "lossless row keys and compulsory weighted-certificate schema; recurrent rows remain unpopulated",
    },
    {
        "role": "protected_interface_execution",
        "doc_path": "docs/490-prime-power-protected-interface-execution-ancestry.md",
        "doc_blob_sha": "e57bc9a66dff826b3bb8e643d3a53e0a38b0cdae",
        "capabilities": ["operation_schema"],
        "boundary": "side-five execution fixture and factorization theorem; no first-host state or edge record",
    },
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def minimum_component_cover() -> tuple[int, list[list[str]]]:
    rows = []
    for size in range(1, len(UPSTREAM) + 1):
        for subset in itertools.combinations(UPSTREAM, size):
            covered = set().union(*(set(row["capabilities"]) for row in subset))
            if covered == set(COMPONENTS):
                rows.append(sorted(row["role"] for row in subset))
        if rows:
            return size, rows
    raise AuditError("abstract component cover absent")


def compile_manifest() -> dict[str, object]:
    roles = [row["role"] for row in UPSTREAM]
    require(len(roles) == len(set(roles)) == 7, "upstream role census")
    require(all(set(row["capabilities"]) <= set(COMPONENTS) for row in UPSTREAM), "unknown capability")

    union_capabilities = sorted(set().union(*(set(row["capabilities"]) for row in UPSTREAM)))
    require(union_capabilities == sorted(COMPONENTS), "abstract component union")
    minimum_sources, minimum_covers = minimum_component_cover()
    require(minimum_sources == 3, "minimum abstract source cover")
    require(len(minimum_covers) == 2, "minimum abstract cover census")

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
                "abstract_schema_candidate_roles": {
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
                },
                "selected_source_backed_schema_refs": 0,
                "family_import_accepted": 0,
            }
        )

    require(len({row["family_id"] for row in family_rows}) == 4, "family census")
    require(all(len(row["edge_refs"]) == 2 for row in family_rows), "two-edge families")
    require(all(row["structural_fields_populated"] == 3 for row in family_rows), "structural field count")
    require(all(row["evidence_fields_populated"] == 0 for row in family_rows), "evidence emptiness")
    require(all(row["selected_source_backed_schema_refs"] == 0 for row in family_rows), "schema refs empty")

    capability_counts = {
        component: sum(component in row["capabilities"] for row in UPSTREAM)
        for component in COMPONENTS
    }
    require(capability_counts == {
        "context_quantification": 1,
        "owner_continuation": 3,
        "operation_schema": 2,
        "closure_route_schema": 3,
        "child_payment_schema": 2,
    }, "capability census")

    return {
        "schema": "exact-recurrent-first-host-action-family-source-import-gate/v1",
        "host_id": HOST_ID,
        "sources": {
            "family_congruence": "data/exact_recurrent_first_host_action_family_congruence_obstruction.json",
            "transition_domain": "data/exact_recurrent_first_host_transition_domain_source_audit.json",
            "family_leverage": "data/exact_recurrent_first_host_action_family_route_leverage.json",
        },
        "contract": {
            "all_fields": list(ALL_FIELDS),
            "structural_fields": list(STRUCTURAL_FIELDS),
            "evidence_fields": list(EVIDENCE_FIELDS),
            "acceptance_rule": (
                "geometry fixes family identity, both exact edge members and the other context bit; "
                "a source import is accepted only when all seven evidence fields are populated and "
                "the theorem proves both context values for the same occurrence-faithful owner lineage"
            ),
        },
        "upstream_interfaces": list(UPSTREAM),
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
        "aggregate": {
            "action_families": len(family_rows),
            "uniformity_fields_per_family": len(ALL_FIELDS),
            "structural_fields_per_family": len(STRUCTURAL_FIELDS),
            "evidence_fields_per_family": len(EVIDENCE_FIELDS),
            "structural_fields_populated_total": len(family_rows) * len(STRUCTURAL_FIELDS),
            "evidence_fields_populated_total": 0,
            "abstract_schema_component_types": len(COMPONENTS),
            "abstract_schema_component_types_covered": len(union_capabilities),
            "upstream_interfaces_audited": len(UPSTREAM),
            "first_host_family_theorems_found": 0,
            "source_backed_uniform_family_imports": 0,
            "minimum_uniform_family_imports_for_scalar_cover": 2,
        },
        "conclusion": {
            "normalized_family_structure_complete": 1,
            "abstract_contract_components_available_in_union": 1,
            "abstract_contract_components_joined_occurrence_faithfully": 0,
            "context_parametric_first_host_theorem_found": 0,
            "one_operation_kind_name_proves_family_uniformity": 0,
            "one_abstract_source_covers_full_family_contract": 0,
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


def validate_manifest(data: dict[str, object]) -> None:
    require(data == compile_manifest(), "manifest differs from deterministic compiler")


def mutation_audit(expected: dict[str, object]) -> int:
    mutants = []

    def add(mutator):
        candidate = copy.deepcopy(expected)
        mutator(candidate)
        mutants.append(candidate)

    add(lambda x: x["aggregate"].__setitem__("evidence_fields_per_family", 6))
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
    add(lambda x: x["abstract_component_analysis"].__setitem__("minimum_sources_to_cover_abstract_components", 2))
    add(lambda x: x["abstract_component_analysis"].__setitem__("single_source_covers_all_components", 1))
    add(lambda x: x["contract"]["evidence_fields"].pop())
    add(lambda x: x["aggregate"].__setitem__("source_backed_uniform_family_imports", 1))

    rejected = 0
    for candidate in mutants:
        try:
            validate_manifest(candidate)
        except AuditError:
            rejected += 1
    require(rejected == len(mutants), "mutation audit")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()

    manifest = compile_manifest()
    mutation_audit(manifest)

    if args.check:
        validate_manifest(json.loads(args.check.read_text()))
    if args.write:
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    if not args.check and not args.write:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
