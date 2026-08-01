#!/usr/bin/env python3
"""Extend the installed operation registry through CMR690."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any

from product_factor_child_registry_entries_a import ENTRIES_A
from product_factor_child_registry_entries_b import ENTRIES_B


class Registry188Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry188Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "931588a34f8817674a8e819aecf2e5aa79c2809a04b8e20c6520e95b2bf423f3"
BASE_OPERATION_KIND_COUNT = 138
BASE_CONTRACT_COUNT = 22
BASE_OWNER_CHANGING_KIND_COUNT = 42
NEW_CONTRACT_SHA256 = "0ce977177196fbffe8c8ffc446346dde64347999b299307f96ca74d4586e4e12"

NEW_ENTRIES = [*ENTRIES_A, *ENTRIES_B]

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-188/v1",
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
EXPECTED_CONTRACT_DIGEST = "f70e412fffd0e8e1c0987fe3b274d138b382a8624867c6e2f0b3ebc0193a034e"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 50, "fifty product/factor/child operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {
        "same-owner", "host-owner-change", "factor-child-owner-change",
        "routing-owner-change", "restoration-owner-change",
    }
    allowed_payments = {
        "owner-witness-stock", "scheduler-dispatch", "local-family-restriction",
        "strict-factor-contraction", "factor-product-dispatch", "edge-reintroduction",
        "routing-change-churn", "labelled-interface-payment", "strict-child-descent",
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
        if payment == "local-family-restriction":
            require(owner == "host-owner-change" and "edge" in continuation,
                    f"{path}: local restriction owner")
        if payment in {"strict-factor-contraction", "strict-child-descent", "factor-product-dispatch"}:
            require(owner == "factor-child-owner-change", f"{path}: factor owner")
        if payment == "routing-change-churn":
            require(owner == "routing-owner-change", f"{path}: routing owner")
        if payment == "edge-reintroduction":
            require(owner == "restoration-owner-change", f"{path}: restoration owner")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 188, "188 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 188,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 188 - owner_changes,
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
        lambda entries: entries[4].update(owner_effect="same-owner"),
        lambda entries: entries[6].update(owner_effect="same-owner"),
        lambda entries: entries[14].update(owner_effect="same-owner"),
        lambda entries: entries[23].update(owner_effect="same-owner"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry188Error:
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
        "installed_transition_kind_bank_188_exhaustive": 1,
        "product_factor_child_operations_registered": 1,
        "installed_payment_assignment_188_complete": 1,
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
