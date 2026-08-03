#!/usr/bin/env python3
"""Audit source imports capable of discharging the first-host selector-face worklist."""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
WORKLIST_PATH = Path("data/exact_recurrent_first_host_selector_face_congruence_worklist.json")
ANCESTRY_DOC = Path("docs/554-prime-power-owner-fate-lineage-kernel-ancestry.md")
REGISTRY_DOC = Path("docs/555-prime-power-installed-operation-registry-1166.md")

COMPONENTS = (
    "common_owner",
    "operation",
    "child_row",
    "payment",
    "closure_route",
)
SIGNATURE_EVIDENCE_FIELDS = (
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
PARAMETRIC_EVIDENCE_FIELDS = (
    "physical_occurrence_domain_ref",
    "legal_menu_state_domain_ref",
    "signature_domain_completeness_ref",
    "common_owner_schema_ref",
    "operation_congruence_ref",
    "child_row_congruence_ref",
    "payment_congruence_ref",
    "closure_route_congruence_ref",
    "theorem_ref",
    "realization_status",
)
SOURCE_SPECS = (
    {
        "source_id": "owner-fate-lineage-kernel-ancestry",
        "path": ANCESTRY_DOC,
        "components": ("common_owner", "child_row", "payment"),
        "markers": (
            "Every recurrent child coefficient has one exact compression key containing structural owner",
            "A compulsory weighted assignment certificate contains every declared return",
            "Ties retain an exact minimizer face and selector switches require an explicit threshold crossing.",
            "owner_fate_rows_populated_all_recurrent_states = 0",
        ),
    },
    {
        "source_id": "installed-operation-registry-1166",
        "path": REGISTRY_DOC,
        "components": ("common_owner", "operation", "payment", "closure_route"),
        "markers": (
            "Every entry has a literal nonempty CMR1894--CMR1965 source list and nonempty continuation rule.",
            "All 72 operations preserve structural owner.",
            "Nineteen local-family equivalences bind lossless class compression",
            "Installed-bank exhaustiveness applies only to the declared 1166-kind registry.",
        ),
    },
)
RESPONSE_LABELS = ("2031", "2301", "2310", "3201")


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


def all_empty(record: dict[str, Any], fields: tuple[str, ...]) -> bool:
    return set(record) == set(fields) and all(record[field] is None for field in fields)


def compile_manifest(root: Path) -> dict[str, Any]:
    worklist = load_json(root, WORKLIST_PATH)
    require(
        worklist.get("schema")
        == "exact-recurrent-first-host-selector-face-congruence-worklist/v1",
        "worklist schema",
    )
    require(worklist.get("host_id") == HOST_ID, "worklist host")
    aggregate = worklist.get("aggregate", {})
    require(aggregate.get("signature_pair_obligations") == 32, "32 obligations")
    require(aggregate.get("menu_parametric_pair_theorem_domains") == 4, "four menu domains")
    require(aggregate.get("cross_menu_pair_theorem_types") == 3, "three pair types")
    require(aggregate.get("total_signature_evidence_slots") == 288, "288 signature slots")
    require(aggregate.get("populated_signature_evidence_slots") == 0, "empty signature slots")
    require(aggregate.get("accepted_signature_obligations") == 0, "zero accepted obligations")
    boundary = worklist.get("source_boundary", {})
    require(boundary.get("selector_tie_break_substitution_allowed") == 0, "tie boundary")
    require(boundary.get("operation_signature_physically_complete") == 0, "signature boundary")

    source_rows = []
    union_components: set[str] = set()
    all_source_text = ""
    for spec in SOURCE_SPECS:
        text = (root / spec["path"]).read_text(encoding="utf-8")
        for marker in spec["markers"]:
            require(marker in text, f"source marker: {spec['source_id']}: {marker}")
        labels = [label for label in RESPONSE_LABELS if label in text]
        require(not labels, f"unexpected first-host response label in {spec['source_id']}")
        union_components.update(spec["components"])
        all_source_text += "\n" + text
        source_rows.append(
            {
                "source_id": spec["source_id"],
                "path": str(spec["path"]),
                "abstract_components": list(spec["components"]),
                "abstract_component_count": len(spec["components"]),
                "first_host_response_labels_found": labels,
                "occurrence_faithful_pair_join_found": 0,
            }
        )
    require(union_components == set(COMPONENTS), "abstract component union")
    require(all(label not in all_source_text for label in RESPONSE_LABELS), "response labels absent")

    signature_records = []
    pair_to_menus: dict[tuple[str, str], set[str]] = {}
    signature_slots = 0
    for cell in worklist.get("cells", []):
        menu = cell["menu"]
        signature = cell["operation_signature"]
        count = cell["background_count"]
        for obligation in cell["basis_obligations"]:
            pair = obligation["response_pair"]
            evidence = obligation["evidence"]
            require(all_empty(evidence, SIGNATURE_EVIDENCE_FIELDS), "signature evidence contract")
            require(obligation.get("evidence_fields_populated") == 0, "signature populated")
            require(obligation.get("congruence_accepted") == 0, "signature accepted")
            structural = {
                "menu": menu,
                "operation_signature": signature,
                "response_pair": pair,
                "background_count": count,
            }
            signature_records.append(
                {
                    "record_id": stable_id("fc-sig", structural),
                    **structural,
                    "evidence": evidence,
                    "source_import_accepted": 0,
                }
            )
            signature_slots += len(SIGNATURE_EVIDENCE_FIELDS)
            pair_to_menus.setdefault(tuple(pair), set()).add(menu)
    require(len(signature_records) == 32, "signature record count")
    require(signature_slots == 288, "signature slot count")

    menu_records = []
    for row in worklist.get("menu_parametric_domains", []):
        structural = {
            "menu": row["menu"],
            "response_pair": row["response_pair"],
            "signature_classes": row["signature_classes"],
            "background_cases": row["background_cases"],
        }
        menu_records.append(
            {
                "record_id": stable_id("fc-menu", structural),
                **structural,
                "evidence": {field: None for field in PARAMETRIC_EVIDENCE_FIELDS},
                "source_import_accepted": 0,
            }
        )
    require(len(menu_records) == 4, "menu record count")

    pair_census = {
        tuple(row["response_pair"]): row
        for row in worklist.get("pair_type_census", [])
    }
    require(set(pair_census) == set(pair_to_menus), "pair census domain")
    cross_records = []
    for pair in sorted(pair_census):
        row = pair_census[pair]
        structural = {
            "response_pair": list(pair),
            "menus": sorted(pair_to_menus[pair]),
            "signature_obligations": row["signature_obligations"],
            "raw_background_comparisons": row["raw_background_comparisons"],
        }
        cross_records.append(
            {
                "record_id": stable_id("fc-cross", structural),
                **structural,
                "evidence": {field: None for field in PARAMETRIC_EVIDENCE_FIELDS},
                "source_import_accepted": 0,
            }
        )
    require(len(cross_records) == 3, "cross record count")
    require(
        next(row for row in cross_records if row["response_pair"] == ["2031", "2310"])["menus"]
        == ["restore_02", "restore_both"],
        "cross-menu pair domain",
    )

    source_subsets = []
    for mask in range(1, 1 << len(source_rows)):
        chosen = [source_rows[index] for index in range(len(source_rows)) if mask >> index & 1]
        covered = sorted(
            set().union(*(set(row["abstract_components"]) for row in chosen))
        )
        if covered == sorted(COMPONENTS):
            source_subsets.append([row["source_id"] for row in chosen])
    minimum_abstract_cover = min(map(len, source_subsets))
    require(minimum_abstract_cover == 2, "minimum abstract source cover")
    require(source_subsets == [[row["source_id"] for row in source_rows]], "unique source cover")

    menu_slots = len(menu_records) * len(PARAMETRIC_EVIDENCE_FIELDS)
    cross_slots = len(cross_records) * len(PARAMETRIC_EVIDENCE_FIELDS)
    return {
        "schema": "exact-recurrent-first-host-selector-face-source-import-gate/v1",
        "host_id": HOST_ID,
        "sources": {
            "face_congruence_worklist": str(WORKLIST_PATH),
            "audited_abstract_sources": source_rows,
            "required_abstract_components": list(COMPONENTS),
            "minimum_abstract_source_cover_size": minimum_abstract_cover,
            "minimum_abstract_source_covers": source_subsets,
        },
        "acceptance_modes": {
            "signature_specific": {
                "records": signature_records,
                "record_count": len(signature_records),
                "evidence_fields": list(SIGNATURE_EVIDENCE_FIELDS),
                "evidence_fields_per_record": len(SIGNATURE_EVIDENCE_FIELDS),
                "evidence_slots": signature_slots,
                "accepted_records": 0,
                "mode_accepted": 0,
            },
            "menu_parametric": {
                "records": menu_records,
                "record_count": len(menu_records),
                "evidence_fields": list(PARAMETRIC_EVIDENCE_FIELDS),
                "evidence_fields_per_record": len(PARAMETRIC_EVIDENCE_FIELDS),
                "evidence_slots": menu_slots,
                "accepted_records": 0,
                "mode_accepted": 0,
            },
            "cross_menu_parametric": {
                "records": cross_records,
                "record_count": len(cross_records),
                "evidence_fields": list(PARAMETRIC_EVIDENCE_FIELDS),
                "evidence_fields_per_record": len(PARAMETRIC_EVIDENCE_FIELDS),
                "evidence_slots": cross_slots,
                "accepted_records": 0,
                "mode_accepted": 0,
            },
        },
        "aggregate": {
            "source_documents_audited": len(source_rows),
            "abstract_components_required": len(COMPONENTS),
            "abstract_components_covered_by_union": len(union_components),
            "minimum_abstract_source_cover_size": minimum_abstract_cover,
            "first_host_response_labels_found_in_sources": 0,
            "occurrence_faithful_pair_joins_found": 0,
            "acceptance_modes": 3,
            "accepted_modes": 0,
            "signature_specific_records": len(signature_records),
            "signature_specific_evidence_slots": signature_slots,
            "menu_parametric_records": len(menu_records),
            "menu_parametric_evidence_slots": menu_slots,
            "cross_menu_parametric_records": len(cross_records),
            "cross_menu_parametric_evidence_slots": cross_slots,
            "populated_evidence_slots_all_modes": 0,
            "accepted_import_records_all_modes": 0,
        },
        "source_boundary": {
            "abstract_schema_component_union_complete": 1,
            "single_abstract_source_complete": 0,
            "abstract_source_cover_occurrence_faithful": 0,
            "response_pair_specific_source_theorem_found": 0,
            "signature_specific_import_available": 0,
            "menu_parametric_import_available": 0,
            "cross_menu_import_available": 0,
            "face_congruence_source_import_accepted": 0,
            "selector_tie_break_substitution_allowed": 0,
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
    candidates = []

    def add(mutator) -> None:
        item = copy.deepcopy(expected)
        mutator(item)
        candidates.append(item)

    add(lambda x: x["aggregate"].__setitem__("abstract_components_covered_by_union", 4))
    add(lambda x: x["aggregate"].__setitem__("minimum_abstract_source_cover_size", 1))
    add(lambda x: x["aggregate"].__setitem__("first_host_response_labels_found_in_sources", 1))
    add(lambda x: x["aggregate"].__setitem__("occurrence_faithful_pair_joins_found", 1))
    add(lambda x: x["aggregate"].__setitem__("accepted_modes", 1))
    add(lambda x: x["aggregate"].__setitem__("signature_specific_records", 31))
    add(lambda x: x["aggregate"].__setitem__("menu_parametric_records", 3))
    add(lambda x: x["aggregate"].__setitem__("cross_menu_parametric_records", 2))
    add(lambda x: x["aggregate"].__setitem__("populated_evidence_slots_all_modes", 1))
    add(lambda x: x["acceptance_modes"]["signature_specific"]["records"][0].__setitem__("source_import_accepted", 1))
    add(lambda x: x["acceptance_modes"]["menu_parametric"]["records"][0]["evidence"].__setitem__("theorem_ref", "fixture"))
    add(lambda x: x["acceptance_modes"]["cross_menu_parametric"]["records"][1]["menus"].pop())
    add(lambda x: x["sources"]["audited_abstract_sources"][0]["abstract_components"].append("closure_route"))
    add(lambda x: x["source_boundary"].__setitem__("single_abstract_source_complete", 1))
    add(lambda x: x["source_boundary"].__setitem__("face_congruence_source_import_accepted", 1))
    add(lambda x: x["source_boundary"].__setitem__("selector_tie_break_substitution_allowed", 1))
    add(lambda x: x["honesty"].__setitem__("payment_congruence_proved", 1))
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
    mutation_audit(args.root, manifest)
    if args.check:
        validate_manifest(args.root, json.loads(args.check.read_text(encoding="utf-8")))
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.check and not args.write:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
