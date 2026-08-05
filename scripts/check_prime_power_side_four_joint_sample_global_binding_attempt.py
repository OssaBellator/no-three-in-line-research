#!/usr/bin/env python3
"""Audit whether the joint side-four sample classes bind to the installed global recurrence."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


class JointSampleGlobalBindingAuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise JointSampleGlobalBindingAuditError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


JOINT_PATH = "data/prime_power_side_four_joint_sample_weight_compatibility_contract.json"
AUDIT_PATH = "data/prime_power_side_four_joint_sample_global_binding_attempt_contract.json"
RUNNER_PATH = "scripts/run_prime_power_installed_construction_regression_1166.py"
ANCESTRY_PATH = "scripts/check_prime_power_labelled_moment_slack_assignment_ancestry.py"
VALIDATOR_PATH = "scripts/check_label_weighted_assignment_certificate.py"
REGISTRY_PATH = "scripts/check_prime_power_installed_operation_registry_1166.py"

EXPECTED_JOINT_SHA256 = "1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5"
EXPECTED_AUDIT_SHA256 = "2cafda35faf9e888828cbe531e0274fea3f82b79275adece31e745b1248cf85d"
EXPECTED_RUNNER_MANIFEST_SHA256 = "e0f69a5665fd4adf4cf88a8cccb861f84133a5dbde435e9f996640159e24988d"
EXPECTED_ANCESTRY_SHA256 = "fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f"
EXPECTED_REGISTRY_SHA256 = "383afc9477f5b52cf60f500c55f51005e4a3020dc34051a04437bdaf503a619b"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise JointSampleGlobalBindingAuditError("unable to locate repository root")


def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: missing")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(root: Path, audit: dict[str, Any]) -> None:
    joint = json.loads((root / JOINT_PATH).read_text(encoding="utf-8"))
    require(digest(joint) == EXPECTED_JOINT_SHA256, "joint sample contract digest")
    require(digest(audit) == EXPECTED_AUDIT_SHA256, "binding audit contract digest")
    require(audit["joint_sample_contract_sha256"] == EXPECTED_JOINT_SHA256, "joint binding")

    runner = load_module(root / RUNNER_PATH, "installed_runner_1166_binding_audit")
    require(
        runner.EXPECTED_CHAINED_MANIFEST_SHA256 == EXPECTED_RUNNER_MANIFEST_SHA256,
        "canonical runner manifest",
    )
    require(
        runner.BASE_MANIFEST_COUNT + len(runner.MANIFEST_EXTENSION) == 77,
        "canonical checker count",
    )
    require(
        audit["canonical_runner"]
        == {
            "path": RUNNER_PATH,
            "manifest_sha256": EXPECTED_RUNNER_MANIFEST_SHA256,
            "installed_checker_count": 77,
        },
        "runner audit record",
    )

    ancestry = load_module(root / ANCESTRY_PATH, "labelled_ancestry_binding_audit")
    require(ancestry.EXPECTED_CONTRACT_SHA256 == EXPECTED_ANCESTRY_SHA256, "ancestry contract")
    ancestry_honesty = ancestry.CONTRACT["honesty_flags"]
    require(ancestry_honesty["labelled_assignment_manifest_populated_all_recurrent_states"] == 0, "all-state manifest honesty")
    require(ancestry_honesty["complete_labelled_recurrent_lp_strict"] == 0, "global LP honesty")
    require(
        audit["labelled_assignment_ancestry"]
        == {
            "path": ANCESTRY_PATH,
            "contract_sha256": EXPECTED_ANCESTRY_SHA256,
            "all_state_manifest_populated": 0,
            "complete_labelled_lp_strict": 0,
        },
        "ancestry audit record",
    )

    validator = load_module(root / VALIDATOR_PATH, "labelled_validator_binding_audit")
    example = validator.build_example_manifest()
    summary = validator.validate_manifest(example)
    require(summary["states"] == 1 and example["states"] == [{"id": "S", "weight": 7}], "built-in example mode")
    validator_source = (root / VALIDATOR_PATH).read_text(encoding="utf-8")
    require("manifest = build_example_manifest()" in validator_source, "default validator example")
    require("[manifest.json]" in validator_source, "external manifest mode")
    require(
        audit["certificate_validator"]
        == {
            "path": VALIDATOR_PATH,
            "mode_without_argument": "built-in-example",
            "external_manifest_required_for_global_binding": 1,
        },
        "validator audit record",
    )

    registry = load_module(root / REGISTRY_PATH, "registry_1166_binding_audit")
    require(registry.EXPECTED_CONTRACT_DIGEST == EXPECTED_REGISTRY_SHA256, "registry contract")
    census = registry.validate(copy.deepcopy(registry.NEW_ENTRIES))
    require(census["installed_operation_kind_count"] == 1166, "operation-kind count")
    require(registry.CONTRACT["honesty_flags"]["owner_fate_rows_populated_all_recurrent_states"] == 0, "registry row honesty")
    require(
        audit["operation_registry"]
        == {
            "path": REGISTRY_PATH,
            "contract_sha256": EXPECTED_REGISTRY_SHA256,
            "operation_kinds": 1166,
            "state_weight_manifest": 0,
        },
        "registry audit record",
    )

    attempts = audit["binding_attempts"]
    require(len(attempts) == 9, "nine binding attempts")
    require(sum(item["scope"] == "parent" for item in attempts) == 2, "two parent attempts")
    require(sum(item["scope"] == "child" for item in attempts) == 7, "seven child attempts")
    require(
        all(item["status"] == "not-bound-by-installed-canonical-stack" for item in attempts),
        "binding status",
    )
    exact_classes = {item["class_id"] for item in joint["class_bindings"]}
    attempted_classes = {item["class_id"] for item in attempts if item["scope"] == "child"}
    require(attempted_classes == exact_classes, "complete exact child-class audit")

    require(
        audit["audit_conclusion"]
        == {
            "outcome": "residual-not-incompatible",
            "reason": "the installed canonical stack supplies exact validators and operation schemas but no populated all-state recurrent manifest mapping these two parents and seven exact child classes to global weights",
            "mathematical_incompatibility_proved": 0,
            "global_binding_succeeded": 0,
        },
        "audit conclusion",
    )
    require(len(audit["remaining_obligations"]) == 6, "remaining obligation count")
    require(
        audit["aggregate"]
        == {
            "binding_attempts": 9,
            "parent_binding_attempts": 2,
            "child_binding_attempts": 7,
            "remaining_obligations": 6,
        },
        "audit aggregate",
    )
    require(
        audit["honesty"]
        == {
            "joint_sample_global_binding_audit_complete": 1,
            "joint_sample_global_weight_bindings_complete": 0,
            "joint_sample_global_incompatibility_proved": 0,
            "joint_sample_global_recurrent_compatibility_proved": 0,
            "joint_sample_full_compulsory_rows_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
        "audit honesty",
    )


def mutation_audit(root: Path, audit: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(binding_attempts=8),
        lambda item: item["binding_attempts"].pop(),
        lambda item: item["binding_attempts"][0].update(status="bound"),
        lambda item: item["binding_attempts"][2].update(class_id="projected-alias"),
        lambda item: item["canonical_runner"].update(installed_checker_count=76),
        lambda item: item["labelled_assignment_ancestry"].update(all_state_manifest_populated=1),
        lambda item: item["certificate_validator"].update(mode_without_argument="global-manifest"),
        lambda item: item["operation_registry"].update(state_weight_manifest=1),
        lambda item: item["audit_conclusion"].update(outcome="incompatible"),
        lambda item: item["audit_conclusion"].update(mathematical_incompatibility_proved=1),
        lambda item: item["audit_conclusion"].update(global_binding_succeeded=1),
        lambda item: item["remaining_obligations"].pop(),
        lambda item: item["honesty"].update(joint_sample_global_weight_bindings_complete=1),
        lambda item: item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(audit)
        mutate(bad)
        try:
            validate(root, bad)
        except JointSampleGlobalBindingAuditError:
            rejected += 1
    require(rejected == len(mutations), "binding-audit corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    audit = json.loads((root / AUDIT_PATH).read_text(encoding="utf-8"))
    validate(root, audit)
    print(json.dumps({
        "checker": "prime-power-side-four-joint-sample-global-binding-attempt",
        "contract_sha256": EXPECTED_AUDIT_SHA256,
        "binding_attempt_count": 9,
        "parent_binding_attempt_count": 2,
        "child_binding_attempt_count": 7,
        "remaining_obligation_count": 6,
        "rejected_corruptions": mutation_audit(root, audit),
        "binding_outcome": "residual-not-incompatible",
        "joint_sample_global_binding_audit_complete": 1,
        "joint_sample_global_weight_bindings_complete": 0,
        "joint_sample_global_incompatibility_proved": 0,
        "joint_sample_global_recurrent_compatibility_proved": 0,
        "joint_sample_full_compulsory_rows_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
