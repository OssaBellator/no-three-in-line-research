#!/usr/bin/env python3
"""Validate the field-level source audit for the joint side-four global binding input."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


class JointGlobalBindingSourceAuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise JointGlobalBindingSourceAuditError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


ATTEMPT_PATH = "data/prime_power_side_four_joint_global_binding_attempt_contract.json"
INPUT_PATH = "data/prime_power_side_four_joint_global_binding_input_manifest.json"
AUDIT_PATH = "data/prime_power_side_four_joint_global_binding_source_audit.json"
ZERO_SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
BLOCKER_SAMPLE_PATH = "data/prime_power_side_four_blocker_actual_background_sample_batch.json"
OWNER_FATE_PATH = "scripts/check_prime_power_owner_fate_lineage_kernel_ancestry.py"
LABELLED_PATH = "scripts/check_prime_power_labelled_moment_slack_assignment_ancestry.py"

EXPECTED_ATTEMPT_SHA256 = "787039d4458fe2e5ee1400e76815cee6dc8b4425d04436453083a91ce7d9f077"
EXPECTED_INPUT_SHA256 = "743e049de6211b8333fcb2f85e03d9deb2204715a35d2e3a0a50423902edd870"
EXPECTED_AUDIT_SHA256 = "0b469d33d245962f83f03a9f8969a2b64a17e34e39cd40f37d49d2c1b1f9f2a6"
EXPECTED_ZERO_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"
EXPECTED_BLOCKER_SAMPLE_SHA256 = "39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"
EXPECTED_OWNER_FATE_SHA256 = "8f52372765f2877c48c32f417fcca27e068ac4675cc98263fd9044e30f28d828"
EXPECTED_LABELLED_SHA256 = "fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f"

MISSING_GLOBAL = "missing-installed-global-source"
LOCAL_ONLY = "available-local-only"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise JointGlobalBindingSourceAuditError("unable to locate repository root")


def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: missing")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(root: Path, audit: dict[str, Any]) -> None:
    attempt = json.loads((root / ATTEMPT_PATH).read_text(encoding="utf-8"))
    input_manifest = json.loads((root / INPUT_PATH).read_text(encoding="utf-8"))
    zero_sample = json.loads((root / ZERO_SAMPLE_PATH).read_text(encoding="utf-8"))
    blocker_sample = json.loads((root / BLOCKER_SAMPLE_PATH).read_text(encoding="utf-8"))

    require(digest(attempt) == EXPECTED_ATTEMPT_SHA256, "binding attempt digest")
    require(digest(input_manifest) == EXPECTED_INPUT_SHA256, "binding input digest")
    require(digest(zero_sample) == EXPECTED_ZERO_SAMPLE_SHA256, "zero sample digest")
    require(digest(blocker_sample) == EXPECTED_BLOCKER_SAMPLE_SHA256, "blocker sample digest")
    require(digest(audit) == EXPECTED_AUDIT_SHA256, "source audit digest")

    require(
        audit["inputs"]
        == {
            "binding_attempt_contract_sha256": EXPECTED_ATTEMPT_SHA256,
            "binding_input_manifest_sha256": EXPECTED_INPUT_SHA256,
            "owner_fate_ancestry_contract_sha256": EXPECTED_OWNER_FATE_SHA256,
            "labelled_assignment_ancestry_contract_sha256": EXPECTED_LABELLED_SHA256,
            "zero_sample_sha256": EXPECTED_ZERO_SAMPLE_SHA256,
            "blocker_sample_sha256": EXPECTED_BLOCKER_SAMPLE_SHA256,
        },
        "input bindings",
    )

    owner_fate = load_module(root / OWNER_FATE_PATH, "owner_fate_source_audit")
    labelled = load_module(root / LABELLED_PATH, "labelled_source_audit")
    require(owner_fate.EXPECTED_CONTRACT_SHA256 == EXPECTED_OWNER_FATE_SHA256, "owner/fate contract")
    require(labelled.EXPECTED_CONTRACT_SHA256 == EXPECTED_LABELLED_SHA256, "labelled contract")
    boundaries = {
        "owner_fate_rows_populated_all_recurrent_states":
            owner_fate.CONTRACT["honesty_flags"]["owner_fate_rows_populated_all_recurrent_states"],
        "compulsory_weighted_certificates_complete":
            owner_fate.CONTRACT["honesty_flags"]["compulsory_weighted_certificates_complete"],
        "actual_global_parent_rule_complete":
            owner_fate.CONTRACT["honesty_flags"]["actual_global_parent_rule_complete"],
        "labelled_assignment_manifest_populated_all_recurrent_states":
            labelled.CONTRACT["honesty_flags"]["labelled_assignment_manifest_populated_all_recurrent_states"],
        "complete_labelled_recurrent_lp_strict":
            labelled.CONTRACT["honesty_flags"]["complete_labelled_recurrent_lp_strict"],
    }
    require(boundaries == audit["source_boundaries"], "source boundary flags")
    require(all(value == 0 for value in boundaries.values()), "source boundary honesty")

    parent_fields = input_manifest["required_parent_records"][0]["fields"]
    require([item["scope"] for item in audit["parent_field_audit"]] == ["zero", "blocker"], "parent scopes")
    for item in audit["parent_field_audit"]:
        require(set(item["fields"]) == set(parent_fields), f"{item['scope']}: parent fields")
        require(all(value == MISSING_GLOBAL for value in item["fields"].values()), f"{item['scope']}: parent source status")
        require(item["complete_record"] == 0, f"{item['scope']}: parent completion")

    expected_children = {
        item["joint_symbol"]: item["class_id"]
        for item in input_manifest["required_child_records"]
    }
    require(len(audit["child_field_audit"]) == 7, "child audit count")
    for item in audit["child_field_audit"]:
        require(expected_children[item["joint_symbol"]] == item["class_id"], f"{item['joint_symbol']}: exact class")
        require(item["local_exact_class_available"] == 1, f"{item['joint_symbol']}: local class")
        require(set(item["fields"]) == set(input_manifest["required_child_fields"]), f"{item['joint_symbol']}: child fields")
        require(all(value == MISSING_GLOBAL for value in item["fields"].values()), f"{item['joint_symbol']}: child source status")
        require(item["complete_record"] == 0, f"{item['joint_symbol']}: child completion")
    require({item["joint_symbol"] for item in audit["child_field_audit"]} == set(expected_children), "child symbol coverage")

    require(
        audit["global_field_audit"]
        == {name: MISSING_GLOBAL for name in input_manifest["required_global_records"]},
        "global source audit",
    )

    require(zero_sample["honesty"]["sample_line_coefficients_complete"] == 1, "zero local line evidence")
    require(zero_sample["expected"]["rank_three_total"] == 0, "zero geometric evidence")
    require(blocker_sample["honesty"]["blocker_sample_line_coefficients_complete"] == 1, "blocker local line evidence")
    require(blocker_sample["expected"]["rank_three_total"] == 1, "blocker geometric evidence")

    for scope in ("zero", "blocker"):
        row = audit["row_field_audit"][scope]
        require(set(row) == set(input_manifest["required_row_completion_records"][scope]) | {"complete_row"}, f"{scope}: row fields")
        require(row["local_line_terms"] == LOCAL_ONLY, f"{scope}: local line status")
        require(row["geometric_terms"] == LOCAL_ONLY, f"{scope}: geometric status")
        for field in ("selector_terms", "collision_terms", "interface_terms", "inner_duals", "outer_dual", "positive_slack"):
            require(row[field] == "missing", f"{scope}:{field}: row source status")
        require(row["complete_row"] == 0, f"{scope}: row completion")

    require(
        audit["aggregate"]
        == {
            "parent_records": 2,
            "parent_field_occurrences": 8,
            "child_records": 7,
            "child_field_occurrences": 21,
            "global_records": 3,
            "row_completion_records": 2,
            "row_field_occurrences": 16,
            "total_field_occurrences": 48,
            "available_local_only_occurrences": 4,
            "missing_source_occurrences": 44,
            "complete_parent_records": 0,
            "complete_child_records": 0,
            "complete_global_records": 0,
            "complete_rows": 0,
        },
        "source audit aggregate",
    )
    require(
        audit["conclusion"]
        == {
            "first_complete_binding_record_available": 0,
            "result": "installed-source-gap",
            "next_required_source": "a populated global recurrent-state manifest with exact parent and child keys, positive installed weights, and transition-occurrence provenance",
        },
        "source audit conclusion",
    )
    require(
        audit["honesty"]
        == {
            "joint_global_binding_source_audit_complete": 1,
            "binding_input_population_complete": 0,
            "global_binding_constructed": 0,
            "global_binding_incompatibility_proved": 0,
            "joint_sample_global_recurrent_compatibility_proved": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
        "source audit honesty",
    )


def mutation_audit(root: Path, audit: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(total_field_occurrences=47),
        lambda item: item["aggregate"].update(available_local_only_occurrences=5),
        lambda item: item["parent_field_audit"][0]["fields"].update(installed_parent_weight="available"),
        lambda item: item["parent_field_audit"][0].update(complete_record=1),
        lambda item: item["child_field_audit"][0].update(class_id="projected-alias"),
        lambda item: item["child_field_audit"][0]["fields"].update(installed_child_weight="available"),
        lambda item: item["child_field_audit"][0].update(complete_record=1),
        lambda item: item["global_field_audit"].update(weight_normalization="available"),
        lambda item: item["row_field_audit"]["zero"].update(local_line_terms="missing"),
        lambda item: item["row_field_audit"]["zero"].update(selector_terms=LOCAL_ONLY),
        lambda item: item["row_field_audit"]["blocker"].update(complete_row=1),
        lambda item: item["source_boundaries"].update(actual_global_parent_rule_complete=1),
        lambda item: item["conclusion"].update(first_complete_binding_record_available=1),
        lambda item: item["honesty"].update(binding_input_population_complete=1),
        lambda item: item["honesty"].update(global_binding_constructed=1),
        lambda item: item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(audit)
        mutate(bad)
        try:
            validate(root, bad)
        except JointGlobalBindingSourceAuditError:
            rejected += 1
    require(rejected == len(mutations), "source-audit corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    audit = json.loads((root / AUDIT_PATH).read_text(encoding="utf-8"))
    validate(root, audit)
    print(json.dumps({
        "checker": "prime-power-side-four-joint-global-binding-source-audit",
        "contract_sha256": EXPECTED_AUDIT_SHA256,
        "total_field_occurrence_count": 48,
        "available_local_only_occurrence_count": 4,
        "missing_source_occurrence_count": 44,
        "complete_binding_record_count": 0,
        "rejected_corruptions": mutation_audit(root, audit),
        "source_audit_result": "installed-source-gap",
        "joint_global_binding_source_audit_complete": 1,
        "binding_input_population_complete": 0,
        "global_binding_constructed": 0,
        "global_binding_incompatibility_proved": 0,
        "joint_sample_global_recurrent_compatibility_proved": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
