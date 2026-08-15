#!/usr/bin/env python3
"""Audit whether installed construction sources define the first-host transition domain."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

HOST = "s4-75b04c45c1c8eac2"
STATE_ORDER = ("00", "01", "10", "11")
STATES = {
    "00": {"menu": "blocked", "restored": [], "deleted": ["02", "20"], "selected": "3012"},
    "01": {"menu": "restore_20", "restored": ["20"], "deleted": ["02"], "selected": "3201"},
    "10": {"menu": "restore_02", "restored": ["02"], "deleted": ["20"], "selected": "2031"},
    "11": {"menu": "restore_both", "restored": ["02", "20"], "deleted": [], "selected": "2031"},
}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))
EDGE_FIELDS = [
    "physical_occurrence_id",
    "persistent_owner_token",
    "source_state_ref",
    "target_state_ref",
    "operation_kind",
    "operation_registry_entry_ref",
    "operation_trace_ref",
    "changed_cell",
    "action",
    "legality_proof_ref",
    "intermediate_state_refs",
    "realization_status",
]
UPSTREAM = [
    {
        "role": "installed_operation_kind_registry",
        "document": "docs/555-prime-power-installed-operation-registry-1166.md",
        "document_blob_sha": "fd5971338a71449bc03e759ceb350977001fe4d4",
        "checker": "scripts/check_prime_power_installed_operation_registry_1166.py",
        "checker_blob_sha": "de2316006b502bc0e8059dd2c7a0aa27990c326c",
        "required_markers": [
            "operation kinds = 1166",
            "Installed-bank exhaustiveness applies only to the declared 1166-kind registry",
        ],
        "first_host_state_records": 0,
        "first_host_edge_records": 0,
        "boundary": "operation-kind and payment-class registry, not an occurrence-level legality table",
    },
    {
        "role": "protected_interface_execution",
        "document": "docs/490-prime-power-protected-interface-execution-ancestry.md",
        "document_blob_sha": "e57bc9a66dff826b3bb8e643d3a53e0a38b0cdae",
        "checker": "scripts/check_prime_power_protected_interface_execution_ancestry.py",
        "required_markers": [
            "side-five protected matching",
            "global_transition_kind_bank_exhaustive = 0",
        ],
        "first_host_state_records": 0,
        "first_host_edge_records": 0,
        "boundary": "side-five protected-interface fixture and factorization theorem",
    },
    {
        "role": "target_anchor_lineage",
        "document": "docs/500-prime-power-target-anchor-lineage-ancestry.md",
        "document_blob_sha": "3ae68197b8dbf8f89cda64e845fd38323d0a3201",
        "checker": "scripts/check_prime_power_target_anchor_lineage_ancestry.py",
        "required_markers": [
            "side-three ordered saturated anchors",
            "4,608 restoration subsets",
            "global_transition_kind_bank_exhaustive = 0",
        ],
        "first_host_state_records": 0,
        "first_host_edge_records": 0,
        "boundary": "fixture restoration and bulk redeletion, not first-host restoration legality",
    },
    {
        "role": "inherited_coordinate_diagonal_block",
        "document": "docs/527-prime-power-inherited-coordinate-diagonal-block-ancestry.md",
        "document_blob_sha": "49d472aa0c5917d32f5f10738aace7e95a96801b",
        "checker": "scripts/check_prime_power_inherited_coordinate_diagonal_block_ancestry.py",
        "required_markers": [
            "same_owner_diagonal_blocks_subcritical = 0",
            "actual_global_parent_rule_complete = 0",
        ],
        "first_host_state_records": 0,
        "first_host_edge_records": 0,
        "boundary": "owner-DAG and quotient contract with same-owner strictness still open",
    },
    {
        "role": "owner_fate_lineage_kernel",
        "document": "docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md",
        "document_blob_sha": "ec44cff041306268b4ed8677b1ab17915cc99a0d",
        "checker": "scripts/check_prime_power_owner_fate_lineage_kernel_ancestry.py",
        "required_markers": [
            "owner_fate_rows_populated_all_recurrent_states = 0",
            "raw_fibre_backgrounds_cover_all_provenance = 0",
        ],
        "first_host_state_records": 0,
        "first_host_edge_records": 0,
        "boundary": "lossless row-key contract and raw-lineage schema with incomplete recurrent population",
    },
]


class DomainAuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise DomainAuditError(message)


def repository_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise DomainAuditError("repository root not found")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def directed_edges() -> list[tuple[str, str]]:
    return sorted(list(UNDIRECTED) + [(target, source) for source, target in UNDIRECTED])


def changed_cell(source: str, target: str) -> str:
    return "02" if source[0] != target[0] else "20"


def action(source: str, target: str) -> str:
    index = 0 if changed_cell(source, target) == "02" else 1
    return "restore" if source[index] == "0" and target[index] == "1" else "delete"


def compile_manifest(root: Path) -> dict:
    for interface in UPSTREAM:
        document = (root / interface["document"]).read_text(encoding="utf-8")
        checker = root / interface["checker"]
        require(checker.is_file(), f"missing checker {interface['checker']}")
        require(HOST not in document, f"first-host record leaked into {interface['document']}")
        for marker in interface["required_markers"]:
            require(marker in document, f"missing marker {marker!r}")

    coverage = load_json(root / "data/exact_recurrent_first_host_physical_source_coverage.json")
    route_gate = load_json(root / "data/exact_recurrent_first_host_closure_route_source_gate.json")
    admission = load_json(root / "data/exact_recurrent_first_host_route_cover_admission.json")

    require(coverage["aggregate"]["source_backed_physical_fields"] == 0, "physical source fields changed")
    require(
        next(row for row in coverage["field_coverage"] if row["field"] == "legal_operations")[
            "physical_populated"
        ]
        == 0,
        "legal operations unexpectedly populated",
    )
    require(route_gate["aggregate"]["physical_legal_edges"] == 0, "route gate legal edges changed")
    require(route_gate["aggregate"]["persistent_owner_tokens"] == 0, "route gate owner tokens changed")
    require(
        route_gate["aggregate"]["source_admissible_edge_route_pairs"] == 0,
        "route gate admissibility changed",
    )
    require(admission["aggregate"]["current_route_closed_edges"] == 0, "closed edge set changed")
    require(admission["aggregate"]["current_complete_covers"] == 0, "complete cover state changed")

    state_rows = [
        {
            "state": state,
            **STATES[state],
            "physical_state_ref": None,
            "physical_state_realized": 0,
        }
        for state in STATE_ORDER
    ]
    edge_rows = []
    for source, target in directed_edges():
        edge_rows.append(
            {
                "edge": f"{source}->{target}",
                "source_state": source,
                "target_state": target,
                "changed_cell": changed_cell(source, target),
                "action": action(source, target),
                "selector_changing": int(STATES[source]["selected"] != STATES[target]["selected"]),
                "candidate_symbolic_edge": 1,
                "operation_kind_mapped": 0,
                "physical_legal_transition": 0,
                "persistent_owner_token": 0,
                "operation_trace_populated": 0,
                "promotion_fields": {field: None for field in EDGE_FIELDS},
            }
        )

    return {
        "schema": "exact-recurrent-first-host-transition-domain-source-audit/v1",
        "scope": {
            "host_id": HOST,
            "deletions": ["02", "20"],
            "symbolic_state_bits": ["r02", "r20"],
        },
        "upstream_interfaces": copy.deepcopy(UPSTREAM),
        "states": state_rows,
        "edges": edge_rows,
        "promotion_contract": {
            "required_edge_fields": EDGE_FIELDS,
            "field_count": len(EDGE_FIELDS),
            "state_realization_precondition": (
                "both endpoint states must have source-backed physical occurrence records"
            ),
            "simultaneous_state_precondition": (
                "any edge incident to state 11 additionally requires a source-backed "
                "realization of the restore-both endpoint"
            ),
        },
        "source_join": {
            "physical_source_coverage": (
                "data/exact_recurrent_first_host_physical_source_coverage.json"
            ),
            "closure_route_source_gate": (
                "data/exact_recurrent_first_host_closure_route_source_gate.json"
            ),
            "route_cover_admission": (
                "data/exact_recurrent_first_host_route_cover_admission.json"
            ),
            "source_backed_legal_operations": 0,
            "source_backed_physical_fields": 0,
            "source_admissible_edge_route_pairs": 0,
            "route_closed_edges": 0,
            "complete_scalar_covers": 0,
        },
        "aggregate": {
            "upstream_interfaces_audited": len(UPSTREAM),
            "installed_operation_kinds": 1166,
            "symbolic_menu_states": len(STATE_ORDER),
            "physical_menu_states": 0,
            "symbolic_directed_edges": len(edge_rows),
            "physical_directed_edges": 0,
            "exact_edge_operation_kind_mappings": 0,
            "exact_edge_legality_proofs": 0,
            "exact_edge_owner_tokens": 0,
            "exact_edge_operation_traces": 0,
            "required_promotion_fields_per_edge": len(EDGE_FIELDS),
            "source_reduced_edge_domain": 0,
        },
        "conclusion": {
            "installed_registry_is_occurrence_legality_table": 0,
            "fixture_restoration_promotes_first_host_edges": 0,
            "simultaneous_restoration_state_physically_realized": 0,
            "physical_transition_domain_known": 0,
            "route_cover_admission_can_be_applied_to_physical_mask": 0,
            "transition_domain_source_audit_complete": 1,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict, root: Path) -> None:
    require(manifest == compile_manifest(root), "manifest mismatch")


def mutation_audit(manifest: dict, root: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(physical_menu_states=1),
        lambda item: item["aggregate"].update(physical_directed_edges=1),
        lambda item: item["aggregate"].update(exact_edge_operation_kind_mappings=1),
        lambda item: item["aggregate"].update(exact_edge_legality_proofs=1),
        lambda item: item["aggregate"].update(source_reduced_edge_domain=1),
        lambda item: item["states"][3].update(physical_state_realized=1),
        lambda item: item["edges"][0].update(operation_kind_mapped=1),
        lambda item: item["edges"][0].update(physical_legal_transition=1),
        lambda item: item["edges"][0]["promotion_fields"].update(operation_kind="restore-edge"),
        lambda item: item["source_join"].update(source_backed_legal_operations=1),
        lambda item: item["source_join"].update(route_closed_edges=1),
        lambda item: item["conclusion"].update(fixture_restoration_promotes_first_host_edges=1),
        lambda item: item["conclusion"].update(physical_transition_domain_known=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, root)
        except DomainAuditError:
            rejected += 1
    require(rejected == len(mutations), "mutation accepted")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    root = repository_root()
    manifest = compile_manifest(root)
    validate(manifest, root)
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.check:
        validate(load_json(args.check), root)
    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-transition-domain-source-audit",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest, root),
                **manifest["conclusion"],
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
