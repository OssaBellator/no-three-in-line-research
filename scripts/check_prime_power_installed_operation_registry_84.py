#!/usr/bin/env python3
"""Extend the installed operation registry through CMR551."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry84Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry84Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "7d63fde340856c7e51900eefe4e2cbacc464690e6cc11298f5d3ec6d42a30806"
BASE_OPERATION_KIND_COUNT = 66
BASE_CONTRACT_COUNT = 18
BASE_OWNER_CHANGING_KIND_COUNT = 34
NEW_CONTRACT_SHA256 = "35bfc31201b5fffb46b37e9c36ffd4c1e9e01c6d1ccdb2b592818b9dc8bdcc80"

NEW_ENTRIES = [
    {
        "operation_kind": "persistent-blocker-trace-contact",
        "source_theorems": ["CMR524", "CMR525", "CMR526"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "trace contact enters persistent-cross signature scheduler",
    },
    {
        "operation_kind": "persistent-blocker-maximum-absorption",
        "source_theorems": ["CMR522", "CMR524"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "maximum-allowed blocker is absorbed into the forbidden matching",
    },
    {
        "operation_kind": "persistent-blocker-two-endpoint-deficiency",
        "source_theorems": ["CMR523", "CMR524", "CMR525"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "two endpoint partners enter cross-pair scheduler",
    },
    {
        "operation_kind": "persistent-cross-pair-cylinder",
        "source_theorems": ["CMR527", "CMR528", "CMR531"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "injective pair type determines a disjoint line-clean cylinder",
    },
    {
        "operation_kind": "persistent-cross-pair-recurrence",
        "source_theorems": ["CMR529", "CMR533", "CMR534"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "recurrent paid pair enters joint-absence scheduler",
    },
    {
        "operation_kind": "persistent-cross-two-arm-bank",
        "source_theorems": ["CMR530", "CMR534"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "matching in partner support graph yields disjoint pair cylinders",
    },
    {
        "operation_kind": "persistent-cross-one-arm-line-star",
        "source_theorems": ["CMR530", "CMR534"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "one fixed cross arm enters line-star scheduler",
    },
    {
        "operation_kind": "persistent-cross-weighted-selector",
        "source_theorems": ["CMR531", "CMR534"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "fixed paid pair enters weighted selector scheduler",
    },
    {
        "operation_kind": "persistent-cross-trace-token-signature",
        "source_theorems": ["CMR526", "CMR532", "CMR534"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "trace witnesses consume finite line and token signatures",
    },
    {
        "operation_kind": "persistent-cross-joint-absence-payment",
        "source_theorems": ["CMR533", "CMR538", "CMR539"],
        "owner_effect": "restoration-owner-change",
        "payment_class": "edge-reintroduction",
        "continuation": "multi-edge absent-to-present transitions pay restoration ledger",
    },
    {
        "operation_kind": "cross-envelope-epoch-assignment",
        "source_theorems": ["CMR535"],
        "owner_effect": "envelope-owner-change",
        "payment_class": "envelope-depth-descent",
        "continuation": "strict envelope change decreases the canonical depth",
    },
    {
        "operation_kind": "cross-signature-finite-stock",
        "source_theorems": ["CMR536", "CMR537", "CMR540"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "epoch-labelled pair and trace signatures have finite stock",
    },
    {
        "operation_kind": "cross-signature-joint-persistence",
        "source_theorems": ["CMR538", "CMR539", "CMR540"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "jointly absent signature enters fixed-selector scheduler",
    },
    {
        "operation_kind": "refined-trace-fixed-selector",
        "source_theorems": ["CMR541", "CMR542", "CMR543", "CMR544", "CMR545"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "refined rooted trace fixes one line-clean selector scheduler",
    },
    {
        "operation_kind": "fixed-selector-unavailable-stock",
        "source_theorems": ["CMR546", "CMR547", "CMR551"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "large unavailable inventory consumes finite residual edge stock",
    },
    {
        "operation_kind": "fixed-selector-collateral-polarization",
        "source_theorems": ["CMR546", "CMR548", "CMR549"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "rank-zero and rank-one collateral atoms have finite stocks",
    },
    {
        "operation_kind": "fixed-selector-rank-zero-target-recurrence",
        "source_theorems": ["CMR549", "CMR550", "CMR551"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "fixed residual target atom enters target-load scheduler",
    },
    {
        "operation_kind": "fixed-selector-rank-one-secant-recurrence",
        "source_theorems": ["CMR549", "CMR550", "CMR551"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "fixed paid-endpoint secant enters line-energy scheduler",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-84/v1",
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
EXPECTED_CONTRACT_DIGEST = "515aaa29fac034eb7f1f119040b60164a3de4ae128363e87a6b48d3f3962fbdd"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 18, "eighteen persistent-cross operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {
        "same-owner", "restoration-owner-change", "envelope-owner-change"
    }
    allowed_payments = {
        "owner-witness-stock", "scheduler-dispatch",
        "edge-reintroduction", "envelope-depth-descent"
    }
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
        require(owner in allowed_owners, f"{path}: owner effect")
        require(payment in allowed_payments, f"{path}: payment class")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: scheduler continuation missing")
        if payment == "edge-reintroduction":
            require(owner == "restoration-owner-change", f"{path}: reintroduction owner")
        if payment == "envelope-depth-descent":
            require(owner == "envelope-owner-change", f"{path}: envelope owner")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 84, "84 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 84,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 84 - owner_changes,
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
        lambda entries: entries[0].update(continuation="terminal"),
        lambda entries: entries[9].update(owner_effect="same-owner"),
        lambda entries: entries[10].update(owner_effect="same-owner"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutator in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutator(bad)
        try:
            validate(bad)
        except Registry84Error:
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
        "installed_transition_kind_bank_84_exhaustive": 1,
        "persistent_cross_selector_operations_registered": 1,
        "installed_payment_assignment_84_complete": 1,
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
