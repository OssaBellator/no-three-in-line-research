#!/usr/bin/env python3
"""Extend the installed registry with rollback optimal-face/SCC operations."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry33Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry33Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "e655f1de7ac0a67bae16907e3bd5fae105cbaf8d7d4a2c604c76b9dae2da9d2e"
BASE_OPERATION_KIND_COUNT = 29
BASE_CONTRACT_COUNT = 12
BASE_OWNER_CHANGING_KIND_COUNT = 23
NEW_CONTRACT_SHA256 = "1281001711d4312dd98b8434e20dffb226b0608a893ffe5cf13f8b8e13940feb"
NEW_ENTRIES = [
    {
        "operation_kind": "rollback-minimum-cost-face-restriction",
        "source_theorems": ["CMR448", "CMR449", "CMR450"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "tight-host and SCC scheduler required",
    },
    {
        "operation_kind": "rollback-tight-host-restriction",
        "source_theorems": ["CMR451", "CMR452"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "optimal-allowed SCC scheduler required",
    },
    {
        "operation_kind": "rollback-optimal-scc-factor-split",
        "source_theorems": ["CMR453", "CMR454", "CMR455", "CMR456", "CMR457", "CMR458", "CMR459", "CMR460"],
        "owner_effect": "factor-child-owner-change",
        "payment_class": "scheduler-dispatch",
        "continuation": "rollback-free block, strict small block, or active-level scheduler",
    },
    {
        "operation_kind": "marked-ancestor-reset-optimal-face",
        "source_theorems": ["CMR461"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "canonical marked tight face prevents positive-cost excursions",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-33/v1",
    "base_registry_sha256": BASE_REGISTRY_SHA256,
    "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
    "base_contract_count": BASE_CONTRACT_COUNT,
    "new_contract_sha256": NEW_CONTRACT_SHA256,
    "new_entries": NEW_ENTRIES,
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "5f9d98c0b964f207fc4ac2d493b51fef5c3caaccf1464cf8bd351a477af93583"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 4, "four optimal-face entries required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payment_counts: dict[str, int] = {}
    for i, entry in enumerate(entries):
        path = f"entry[{i}]"
        kind = entry.get("operation_kind")
        require(isinstance(kind, str) and kind and kind not in kinds, f"{path}: unique kind required")
        kinds.add(kind)
        require(entry.get("contract_sha256") == NEW_CONTRACT_SHA256, f"{path}: contract mismatch")
        sources = entry.get("source_theorems")
        require(
            isinstance(sources, list) and sources
            and all(isinstance(source, str) and source.startswith("CMR") for source in sources),
            f"{path}: theorem ancestry required",
        )
        owner = entry.get("owner_effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(owner in {"same-owner", "factor-child-owner-change"}, f"{path}: owner effect")
        require(payment in {"scheduler-dispatch", "owner-witness-stock"}, f"{path}: payment")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: mandatory scheduler missing")
        owner_changes += owner != "same-owner"
        payment_counts[payment] = payment_counts.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 33, "33 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 33,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 33 - owner_changes,
        "new_payment_counts": payment_counts,
        "registry_sha256": digest({"base": BASE_REGISTRY_SHA256, "new": entries}),
    }


def mutation_audit() -> int:
    mutations = [
        lambda x: x.append(copy.deepcopy(x[0])),
        lambda x: x[0].update(operation_kind=x[1]["operation_kind"]),
        lambda x: x[0].update(contract_sha256="0" * 64),
        lambda x: x[0].update(source_theorems=[]),
        lambda x: x[0].update(owner_effect="anonymous"),
        lambda x: x[0].update(payment_class="free"),
        lambda x: x[0].update(continuation=""),
        lambda x: x[0].update(continuation="terminal"),
        lambda x: x.pop(),
    ]
    rejected = 0
    for mutator in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutator(bad)
        try:
            validate(bad)
        except Registry33Error:
            rejected += 1
    require(rejected == len(mutations), "registry corruption accepted")
    return rejected


def main() -> None:
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    census = validate(copy.deepcopy(NEW_ENTRIES))
    census["rejected_corruptions"] = mutation_audit()
    report = {
        "contract_digest": contract_digest,
        "census": census,
        "installed_transition_kind_bank_33_exhaustive": 1,
        "rollback_optimal_face_operations_registered": 1,
        "installed_payment_assignment_33_complete": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
