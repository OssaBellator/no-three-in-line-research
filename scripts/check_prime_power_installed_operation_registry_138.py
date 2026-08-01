#!/usr/bin/env python3
"""Extend the installed operation registry through CMR628."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry138Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry138Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "043cc0dfdc5f9509de81da436df1aec8579a7803623d0ace54d6d0dd6904bfdf"
BASE_OPERATION_KIND_COUNT = 117
BASE_CONTRACT_COUNT = 21
BASE_OWNER_CHANGING_KIND_COUNT = 40
NEW_CONTRACT_SHA256 = "59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f"

NEW_ENTRIES = [
    {
        "operation_kind": "protected-line-contact-extraction",
        "source_theorems": ["CMR605"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "protected line contacts are charged to one owned line certificate",
    },
    {
        "operation_kind": "protected-line-bulk-absorption",
        "source_theorems": ["CMR606", "CMR608"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "all free line cells strictly enlarge the protected matching",
    },
    {
        "operation_kind": "protected-line-residual-atom-cap",
        "source_theorems": ["CMR607"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "post-absorption line atoms are bounded by protected contact stock",
    },
    {
        "operation_kind": "protected-line-atom-destruction",
        "source_theorems": ["CMR608"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "destroyed line atoms consume the fixed owned-line profile",
    },
    {
        "operation_kind": "protected-line-growth-budget",
        "source_theorems": ["CMR609"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "monotone line absorption has finite protected matching growth",
    },
    {
        "operation_kind": "protected-line-large-core-dispatch",
        "source_theorems": ["CMR610"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "large protected core enters sparse-interface scheduler",
    },
    {
        "operation_kind": "secant-star-matching-vertex-wall",
        "source_theorems": ["CMR611", "CMR616"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "matching-vertex wall enters protected contact scheduler",
    },
    {
        "operation_kind": "secant-star-compatible-arm-bank",
        "source_theorems": ["CMR611"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "matching-compatible arm bank is fixed by the owned star certificate",
    },
    {
        "operation_kind": "secant-star-protected-touch-filter",
        "source_theorems": ["CMR612"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "protected-touching arms consume finite protected vertex stock",
    },
    {
        "operation_kind": "secant-star-bulk-absorption",
        "source_theorems": ["CMR613"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "free star arms strictly enlarge the protected matching",
    },
    {
        "operation_kind": "secant-star-growth-budget",
        "source_theorems": ["CMR614"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "monotone star absorption has finite protected matching growth",
    },
    {
        "operation_kind": "secant-star-large-core-dispatch",
        "source_theorems": ["CMR615", "CMR616"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "large protected core enters sparse-interface scheduler",
    },
    {
        "operation_kind": "protected-interface-skeleton-extraction",
        "source_theorems": ["CMR617"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "balanced cross skeleton is stored in the finite interface universe",
    },
    {
        "operation_kind": "protected-interface-product-factorization",
        "source_theorems": ["CMR618"],
        "owner_effect": "factor-child-owner-change",
        "payment_class": "factor-product-dispatch",
        "continuation": "fixed skeleton yields exact protected and free child factors",
    },
    {
        "operation_kind": "protected-interface-skeleton-stock",
        "source_theorems": ["CMR619", "CMR620"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "sparse skeletons consume the exact finite interface stock",
    },
    {
        "operation_kind": "protected-interface-large-core-dispatch",
        "source_theorems": ["CMR621", "CMR622"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "small free factor enters recursive factor scheduler",
    },
    {
        "operation_kind": "protected-skeleton-finite-history",
        "source_theorems": ["CMR623"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "nonrecurrent skeleton histories consume finite skeleton stock",
    },
    {
        "operation_kind": "protected-skeleton-factor-diversity",
        "source_theorems": ["CMR624", "CMR625"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "repeated skeleton states pay protected factor matching diversity",
    },
    {
        "operation_kind": "protected-skeleton-cross-churn",
        "source_theorems": ["CMR626"],
        "owner_effect": "routing-owner-change",
        "payment_class": "routing-change-churn",
        "continuation": "skeleton change pays physical cross-edge churn",
    },
    {
        "operation_kind": "protected-interface-token-payment",
        "source_theorems": ["CMR627"],
        "owner_effect": "same-owner",
        "payment_class": "labelled-interface-payment",
        "continuation": "cross-edge churn receives exact labelled full-token incidence",
    },
    {
        "operation_kind": "protected-skeleton-history-dispatch",
        "source_theorems": ["CMR628"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "recurrent interface enters free-factor or protected-factor scheduler",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-138/v1",
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
EXPECTED_CONTRACT_DIGEST = "1ad61f338ba3095e632b4b3e2ee28b1b0400a082d50795311c077068cf6beda3"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 21, "twenty-one protected-interface operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {"same-owner", "factor-child-owner-change", "routing-owner-change"}
    allowed_payments = {
        "owner-witness-stock", "protected-core-growth", "scheduler-dispatch",
        "factor-product-dispatch", "routing-change-churn", "labelled-interface-payment",
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
        if payment == "protected-core-growth":
            require("protected" in continuation and "growth" in continuation or "enlarge" in continuation,
                    f"{path}: growth continuation")
        if payment == "factor-product-dispatch":
            require(owner == "factor-child-owner-change", f"{path}: factor owner")
        if payment == "routing-change-churn":
            require(owner == "routing-owner-change", f"{path}: routing owner")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 138, "138 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 138,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 138 - owner_changes,
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
        lambda entries: entries[5].update(continuation="terminal"),
        lambda entries: entries[1].update(continuation="finite"),
        lambda entries: entries[13].update(owner_effect="same-owner"),
        lambda entries: entries[18].update(owner_effect="same-owner"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry138Error:
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
        "installed_transition_kind_bank_138_exhaustive": 1,
        "protected_interface_execution_operations_registered": 1,
        "installed_payment_assignment_138_complete": 1,
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
