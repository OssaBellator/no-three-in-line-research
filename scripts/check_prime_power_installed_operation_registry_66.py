#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry66Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry66Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "307652b1890a3382992c06ea6f860f1da513f5f7368e5142e3ce8a1183d37f50"
BASE_OPERATION_KIND_COUNT = 57
BASE_CONTRACT_COUNT = 17
BASE_OWNER_CHANGING_KIND_COUNT = 33
NEW_CONTRACT_SHA256 = "d7c2c9bef971f9cb2d4b3298ef908641fb9afb8d80ba8f381202ee100a6efcc0"

NEW_ENTRIES = [
    {
        "operation_kind": "adaptive-unavailable-matching-absorption",
        "source_theorems": ["CMR507", "CMR510", "CMR511"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "finite absorbed-edge matching stock or recurrent absorbed edge",
    },
    {
        "operation_kind": "unavailable-row-column-cover-extraction",
        "source_theorems": ["CMR508", "CMR509"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "canonical small row-column cover labels the residual inventory",
    },
    {
        "operation_kind": "heavy-unavailable-star-extraction",
        "source_theorems": ["CMR509", "CMR510", "CMR511"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "heavy row-column star enters token scheduler",
    },
    {
        "operation_kind": "unavailable-star-heavy-token",
        "source_theorems": ["CMR512", "CMR513", "CMR515", "CMR516"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "one labelled token contains a heavy unavailable edge set",
    },
    {
        "operation_kind": "unavailable-star-dispersed-token-bank",
        "source_theorems": ["CMR513", "CMR514", "CMR515", "CMR516"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "pairwise distinct labelled token witnesses consume finite stock",
    },
    {
        "operation_kind": "unavailable-token-finite-stock",
        "source_theorems": ["CMR517", "CMR518", "CMR520"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "finite labelled token-edge stock bounds nonrecurrent episodes",
    },
    {
        "operation_kind": "unavailable-token-reintroduction-payment",
        "source_theorems": ["CMR519", "CMR520"],
        "owner_effect": "restoration-owner-change",
        "payment_class": "edge-reintroduction",
        "continuation": "absent-to-present return pays the existing reintroduction ledger",
    },
    {
        "operation_kind": "unavailable-token-persistent-blocker",
        "source_theorems": ["CMR519", "CMR520"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "persistent unavailable edge enters blocker geometry scheduler",
    },
    {
        "operation_kind": "free-absorption-finite-stock",
        "source_theorems": ["CMR521"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "finite physical edge stock or recurrent absorbed-edge scheduler",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-66/v1",
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
EXPECTED_CONTRACT_DIGEST = "3644c4335cb81419903c89576ea4ae78cf1fcdb66c6ed7a959fd664542214b02"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 9, "nine unavailable/token operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    for index, entry in enumerate(entries):
        path = f"entry[{index}]"
        kind = entry.get("operation_kind")
        require(isinstance(kind, str) and kind and kind not in kinds, f"{path}: unique kind")
        kinds.add(kind)
        require(entry.get("contract_sha256") == NEW_CONTRACT_SHA256, f"{path}: contract")
        sources = entry.get("source_theorems")
        require(
            isinstance(sources, list) and sources
            and all(isinstance(source, str) and source.startswith("CMR") for source in sources),
            f"{path}: theorem ancestry",
        )
        owner = entry.get("owner_effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(owner in {"same-owner", "restoration-owner-change"}, f"{path}: owner effect")
        require(payment in {"owner-witness-stock", "scheduler-dispatch", "edge-reintroduction"},
                f"{path}: payment class")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: mandatory scheduler missing")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 66, "66 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 66,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 66 - owner_changes,
        "new_payment_counts": payments,
        "registry_sha256": digest({"base": BASE_REGISTRY_SHA256, "new": entries}),
    }


def mutation_audit() -> int:
    mutations = [
        lambda entries: entries.append(copy.deepcopy(entries[0])),
        lambda entries: entries[0].update(operation_kind=entries[1]["operation_kind"]),
        lambda entries: entries[0].update(contract_sha256="0" * 64),
        lambda entries: entries[0].update(source_theorems=[]),
        lambda entries: entries[0].update(owner_effect="anonymous"),
        lambda entries: entries[0].update(payment_class="free"),
        lambda entries: entries[0].update(continuation=""),
        lambda entries: entries[2].update(continuation="terminal"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutator in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutator(bad)
        try:
            validate(bad)
        except Registry66Error:
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
        "installed_transition_kind_bank_66_exhaustive": 1,
        "adaptive_unavailable_temporal_operations_registered": 1,
        "installed_payment_assignment_66_complete": 1,
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
