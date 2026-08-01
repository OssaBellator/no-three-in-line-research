#!/usr/bin/env python3
"""Extend the installed operation registry through CMR576."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry98Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry98Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


BASE_REGISTRY_SHA256 = "407d0fa4850effb642ec3cfc318594eaf9f6b0c7e46df4eb7370d90e09b326e1"
BASE_OPERATION_KIND_COUNT = 84
BASE_CONTRACT_COUNT = 19
BASE_OWNER_CHANGING_KIND_COUNT = 36
NEW_CONTRACT_SHA256 = "15fdb4ac2e639dd23b89dae3ce302356ee4790a2183e7768315aed8b881e6d5e"

NEW_ENTRIES = [
    {
        "operation_kind": "canonical-selector-forbidden-matching",
        "source_theorems": ["CMR552", "CMR553"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "one deterministic forbidden matching fixes the selector cylinder",
    },
    {
        "operation_kind": "canonical-selector-static-collateral",
        "source_theorems": ["CMR553", "CMR554", "CMR557"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "static collateral profile is charged once to its selector signature",
    },
    {
        "operation_kind": "canonical-selector-dynamic-availability",
        "source_theorems": ["CMR554", "CMR555", "CMR557"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "dynamic unavailable inventory enters canonical edge scheduler",
    },
    {
        "operation_kind": "canonical-selector-edge-recurrence",
        "source_theorems": ["CMR555", "CMR556", "CMR557"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "recurrent selector-edge pair enters absence-run scheduler",
    },
    {
        "operation_kind": "static-collateral-rank-polarization",
        "source_theorems": ["CMR558"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "fixed rank-zero or paid-endpoint rank-one mass is selected",
    },
    {
        "operation_kind": "static-collateral-line-decomposition",
        "source_theorems": ["CMR559", "CMR564"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "collateral atoms are assigned to exact supporting lines",
    },
    {
        "operation_kind": "static-collateral-heavy-line",
        "source_theorems": ["CMR560", "CMR561", "CMR562", "CMR567"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "heavy low-height line enters line-energy scheduler",
    },
    {
        "operation_kind": "static-collateral-secant-star",
        "source_theorems": ["CMR560", "CMR561", "CMR563", "CMR569"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "repeated-cell secant star enters star scheduler",
    },
    {
        "operation_kind": "static-collateral-disjoint-triple-bank",
        "source_theorems": ["CMR561", "CMR563"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "cell-disjoint triple bank enters deletion scheduler",
    },
    {
        "operation_kind": "static-collateral-carry-splice",
        "source_theorems": ["CMR565", "CMR566", "CMR568", "CMR570"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "height-localized lines enter prefix and carry scheduler",
    },
    {
        "operation_kind": "canonical-selector-protected-extension",
        "source_theorems": ["CMR571"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "protected partial matching has one canonical extension",
    },
    {
        "operation_kind": "canonical-selector-edge-absorption",
        "source_theorems": ["CMR572", "CMR574", "CMR575"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "absorbable recurrent edge strictly enlarges the protected matching",
    },
    {
        "operation_kind": "canonical-selector-protected-contact",
        "source_theorems": ["CMR573", "CMR574", "CMR576"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "blocked recurrent edge enters protected-contact scheduler",
    },
    {
        "operation_kind": "canonical-selector-absorption-chase",
        "source_theorems": ["CMR574", "CMR575", "CMR576"],
        "owner_effect": "same-owner",
        "payment_class": "protected-core-growth",
        "continuation": "finite protected-matching growth bounds the absorption chase",
    },
]
for entry in NEW_ENTRIES:
    entry["contract_sha256"] = NEW_CONTRACT_SHA256

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-98/v1",
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
EXPECTED_CONTRACT_DIGEST = "d42d011f37658f9614435831004fe2ef10c4ec73517cad049d7ce34f0f5dfdfa"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 14, "fourteen canonical-selector operations required")
    kinds: set[str] = set()
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
        require(entry.get("owner_effect") == "same-owner", f"{path}: owner effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(payment in {
            "owner-witness-stock", "scheduler-dispatch", "protected-core-growth"
        }, f"{path}: payment class")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: scheduler continuation")
        if payment == "protected-core-growth":
            require("protected" in continuation and (
                "enlarges" in continuation or "growth" in continuation
            ), f"{path}: growth continuation")
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 98, "98 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 98,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": BASE_OWNER_CHANGING_KIND_COUNT,
        "same_owner_operation_kinds": 98 - BASE_OWNER_CHANGING_KIND_COUNT,
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
        lambda entries: entries[11].update(continuation="finite"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry98Error:
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
        "installed_transition_kind_bank_98_exhaustive": 1,
        "canonical_selector_absorption_operations_registered": 1,
        "installed_payment_assignment_98_complete": 1,
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
