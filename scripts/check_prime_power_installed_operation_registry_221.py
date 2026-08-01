#!/usr/bin/env python3
"""Extend the installed operation registry through CMR829."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any

from target_anchor_registry_entries_a import ENTRIES_A
from target_anchor_registry_entries_b import ENTRIES_B


class Registry221Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry221Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


BASE_REGISTRY_SHA256 = "4d4875c010c4a6eac3d51eb6492d2db39322bc1b17015dc0dc50eb10946fecfc"
BASE_OPERATION_KIND_COUNT = 188
BASE_CONTRACT_COUNT = 23
BASE_OWNER_CHANGING_KIND_COUNT = 62
NEW_CONTRACT_SHA256 = "2f846aa50012d196dffc90511de0c254782b1a5696b1cb25ee1cf1b73a990359"
NEW_ENTRIES = [*ENTRIES_A, *ENTRIES_B]

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-221/v1",
    "base_registry_sha256": BASE_REGISTRY_SHA256,
    "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
    "base_contract_count": BASE_CONTRACT_COUNT,
    "base_owner_changing_kind_count": BASE_OWNER_CHANGING_KIND_COUNT,
    "new_contract_sha256": NEW_CONTRACT_SHA256,
    "new_entries": NEW_ENTRIES,
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "939ca5627499348fb52e9153a56e0b31697c2f9f00ad8e0dcb7fba4e7bb10e4c"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 33, "thirty-three target/anchor/lineage operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {
        "same-owner", "host-owner-change", "factor-child-owner-change",
        "routing-owner-change", "restoration-owner-change",
    }
    allowed_payments = {
        "owner-witness-stock", "scheduler-dispatch", "same-envelope-dispatch",
        "state-family-restriction", "edge-reintroduction", "labelled-interface-payment",
        "host-edge-deletion", "strict-factor-contraction", "cycle-erasure",
        "private-mask-growth", "structural-lineage-stock", "routing-change-churn",
    }
    for index, entry in enumerate(entries):
        path = f"entry[{index}]"
        kind = entry.get("operation_kind")
        require(isinstance(kind, str) and kind and kind not in kinds, f"{path}: unique kind")
        kinds.add(kind)
        require(entry.get("contract_sha256") == NEW_CONTRACT_SHA256, f"{path}: contract")
        sources = entry.get("source_theorems")
        require(isinstance(sources, list) and sources
                and all(isinstance(source, str) and source.startswith("CMR") for source in sources),
                f"{path}: theorem ancestry")
        owner = entry.get("owner_effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(owner in allowed_owners, f"{path}: owner effect")
        require(payment in allowed_payments, f"{path}: payment class")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: scheduler continuation")
        if payment in {"host-edge-deletion", "state-family-restriction", "private-mask-growth"}:
            require(owner == "host-owner-change", f"{path}: host owner")
        if payment == "strict-factor-contraction":
            require(owner == "factor-child-owner-change", f"{path}: factor owner")
        if payment == "edge-reintroduction":
            require(owner == "restoration-owner-change", f"{path}: restoration owner")
        if payment == "routing-change-churn":
            require(owner == "routing-owner-change", f"{path}: routing owner")
        if payment in {"cycle-erasure", "structural-lineage-stock"}:
            require(owner == "same-owner", f"{path}: same-owner payment")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 221, "221 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 221,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 221 - owner_changes,
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
        lambda entries: entries[3].update(continuation="terminal"),
        lambda entries: entries[8].update(payment_class="free"),
        lambda entries: entries[15].update(owner_effect="same-owner"),
        lambda entries: entries[20].update(owner_effect="same-owner"),
        lambda entries: entries[27].update(owner_effect="host-owner-change"),
        lambda entries: entries[32].update(owner_effect="same-owner"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry221Error:
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
        "installed_transition_kind_bank_221_exhaustive": 1,
        "target_anchor_lineage_operations_registered": 1,
        "installed_payment_assignment_221_complete": 1,
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
