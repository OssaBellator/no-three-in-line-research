#!/usr/bin/env python3
"""Extend the installed operation registry through CMR592."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry110Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry110Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "4732c504824406c78b9a9e92033994f30be1c744e633a5e49dcc5531497e00ae"
BASE_OPERATION_KIND_COUNT = 98
BASE_CONTRACT_COUNT = 20
BASE_OWNER_CHANGING_KIND_COUNT = 36
NEW_CONTRACT_SHA256 = "a48ee5aa77c167c1dba3d6eab6e3a65db7397e1739323fb794df66c32d76ec5f"

NEW_ENTRIES = [
    {
        "operation_kind": "packed-conflict-nonessential-deletion",
        "source_theorems": ["CMR577", "CMR579", "CMR581"],
        "owner_effect": "host-owner-change",
        "payment_class": "edge-deletion",
        "continuation": "matching-preserving deletion removes one packed conflict edge",
    },
    {
        "operation_kind": "packed-conflict-forced-terminality",
        "source_theorems": ["CMR577", "CMR578", "CMR581"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "fully forced packed triples consume the finite essential matching core",
    },
    {
        "operation_kind": "packed-conflict-private-restoration",
        "source_theorems": ["CMR579", "CMR580", "CMR581"],
        "owner_effect": "restoration-owner-change",
        "payment_class": "edge-reintroduction",
        "continuation": "recreated packed conflict pays its private restored edge",
    },
    {
        "operation_kind": "protected-contact-finite-stock",
        "source_theorems": ["CMR582", "CMR583"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "finite physical blocked-edge stock bounds nonrecurrent contact history",
    },
    {
        "operation_kind": "protected-contact-wall-extraction",
        "source_theorems": ["CMR584"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "protected row-column wall enters contact token scheduler",
    },
    {
        "operation_kind": "protected-contact-token-splice",
        "source_theorems": ["CMR584", "CMR585"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "heavy or dispersed contact tokens consume labelled token stock",
    },
    {
        "operation_kind": "protected-contact-reintroduction",
        "source_theorems": ["CMR586"],
        "owner_effect": "restoration-owner-change",
        "payment_class": "edge-reintroduction",
        "continuation": "recurrent blocked edge pays absent-to-present restoration",
    },
    {
        "operation_kind": "recurrent-unavailable-set-extraction",
        "source_theorems": ["CMR587"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "fixed recurrent unavailable set has finite subset stock",
    },
    {
        "operation_kind": "recurrent-set-aggregate-reintroduction",
        "source_theorems": ["CMR588"],
        "owner_effect": "restoration-owner-change",
        "payment_class": "edge-reintroduction",
        "continuation": "joint-set recurrence pays aggregate edge restoration",
    },
    {
        "operation_kind": "recurrent-set-batch-absorption",
        "source_theorems": ["CMR589", "CMR590", "CMR592"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "batch absorption strictly enlarges the protected matching",
    },
    {
        "operation_kind": "recurrent-set-persistent-wall",
        "source_theorems": ["CMR589", "CMR591", "CMR592"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "simultaneously unavailable wall enters persistent token scheduler",
    },
    {
        "operation_kind": "recurrent-set-batch-growth",
        "source_theorems": ["CMR590", "CMR592"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "finite batch growth bounds protected matching enlargement",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-110/v1",
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
EXPECTED_CONTRACT_DIGEST = "2b71be7e9325fc6efdf606f59faae245e6a73047ee70deb04edf34b47e373a5f"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 12, "twelve protected batching operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {"same-owner", "host-owner-change", "restoration-owner-change"}
    allowed_payments = {
        "edge-deletion", "owner-witness-stock", "scheduler-dispatch",
        "edge-reintroduction", "protected-core-growth",
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
        if payment == "edge-deletion":
            require(owner == "host-owner-change", f"{path}: deletion owner")
        if payment == "edge-reintroduction":
            require(owner == "restoration-owner-change", f"{path}: restoration owner")
        if payment == "protected-core-growth":
            require("protected" in continuation and (
                "enlarges" in continuation or "growth" in continuation
            ), f"{path}: growth continuation")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 110, "110 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 110,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 110 - owner_changes,
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
        lambda entries: entries[4].update(continuation="terminal"),
        lambda entries: entries[0].update(owner_effect="same-owner"),
        lambda entries: entries[2].update(owner_effect="same-owner"),
        lambda entries: entries[9].update(continuation="finite"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry110Error:
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
        "installed_transition_kind_bank_110_exhaustive": 1,
        "protected_conflict_batching_operations_registered": 1,
        "installed_payment_assignment_110_complete": 1,
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
