#!/usr/bin/env python3
"""Extend the installed operation registry through CMR853."""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


class Registry239Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Registry239Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


BASE_REGISTRY_SHA256 = "d6a7fb4f646af70b6dd685729a1b2cd1a5b53553bebd132640e72cd4d9eba612"
BASE_OPERATION_KIND_COUNT = 221
BASE_CONTRACT_COUNT = 24
BASE_OWNER_CHANGING_KIND_COUNT = 75
NEW_CONTRACT_SHA256 = "d59d5eb82d388c12ba4551c377054d8bdce91b7d10098ebc32c78c56025727cc"
NEW_ENTRIES = [
    {
        "operation_kind": "complete-state-single-edge-child",
        "source_theorems": ["CMR830", "CMR831", "CMR832"],
        "owner_effect": "host-owner-change",
        "payment_class": "local-family-restriction",
        "continuation": "one rejected-state edge defines one viable deletion child",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "complete-state-viable-child-union",
        "source_theorems": ["CMR831", "CMR832"],
        "owner_effect": "same-owner",
        "payment_class": "branch-cover-dispatch",
        "continuation": "viable single-edge children exactly cover every alternative state",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "complete-state-branch-depth-stock",
        "source_theorems": ["CMR833"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "distinct branch deletions consume finite labelled edge stock",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "improving-witness-preserving-child-path",
        "source_theorems": ["CMR834"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "one improving witness determines a surviving viable child path",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "aggressive-batch-subbranch-containment",
        "source_theorems": ["CMR835"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "aggressive entering-batch child lies inside every constituent edge child",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "complete-state-terminal-leaf-dispatch",
        "source_theorems": ["CMR836", "CMR837"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "terminal viable leaf enters improvement contraction or owner-change scheduler",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "state-family-essential-core-extraction",
        "source_theorems": ["CMR838", "CMR839"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "common state-family core determines exact viable child edges",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "state-family-complete-core-contraction",
        "source_theorems": ["CMR840", "CMR841"],
        "owner_effect": "factor-child-owner-change",
        "payment_class": "strict-factor-contraction",
        "continuation": "complete compatible core contracts to a core-free residual family",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "core-width-conservation",
        "source_theorems": ["CMR842"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "core rank and viable child count conserve state cardinality",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "deterministic-zero-one-child",
        "source_theorems": ["CMR843"],
        "owner_effect": "same-owner",
        "payment_class": "branch-cover-dispatch",
        "continuation": "zero and one residual edge give singleton or deterministic child",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "branch-core-rank-budget",
        "source_theorems": ["CMR844", "CMR845"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "contracted core ranks telescope along every branch",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "distinguishing-transversal-extraction",
        "source_theorems": ["CMR846"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "minimum state identifier equals an alternative-support transversal",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "distinguishing-compressed-child-cover",
        "source_theorems": ["CMR847"],
        "owner_effect": "same-owner",
        "payment_class": "branch-cover-dispatch",
        "continuation": "minimum distinguishing edge set gives exact compressed child cover",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "distinguishing-low-rank-richness",
        "source_theorems": ["CMR848"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "high distinguishing rank enters low-rank exchange scheduler",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "distinguishing-product-additivity",
        "source_theorems": ["CMR849"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "exact product factors add distinguishing width",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "matching-exchange-cycle-decomposition",
        "source_theorems": ["CMR850"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "alternative matching states correspond to directed exchange cycles",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "exchange-feedback-vertex-width",
        "source_theorems": ["CMR851"],
        "owner_effect": "same-owner",
        "payment_class": "scheduler-dispatch",
        "continuation": "matching branch width enters feedback-vertex scheduler",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
    {
        "operation_kind": "exchange-essential-cycle-characterization",
        "source_theorems": ["CMR852", "CMR853"],
        "owner_effect": "same-owner",
        "payment_class": "owner-witness-stock",
        "continuation": "essential edges are exactly vertices outside exchange-cycle support",
        "contract_sha256": NEW_CONTRACT_SHA256,
    },
]

CONTRACT = {
    "schema": "prime-power-installed-operation-registry-239/v1",
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
EXPECTED_CONTRACT_DIGEST = "42dda9f4be17e18a2fd82e94f540e14a93c9f2605790dc52366e17150992405e"


def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 18, "eighteen complete-branch operations required")
    kinds: set[str] = set()
    owner_changes = BASE_OWNER_CHANGING_KIND_COUNT
    payments: dict[str, int] = {}
    allowed_owners = {"same-owner", "host-owner-change", "factor-child-owner-change"}
    allowed_payments = {
        "owner-witness-stock", "scheduler-dispatch", "branch-cover-dispatch",
        "local-family-restriction", "strict-factor-contraction",
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
            require(owner == "host-owner-change" and "child" in continuation,
                    f"{path}: branch child owner")
        if payment == "strict-factor-contraction":
            require(owner == "factor-child-owner-change", f"{path}: factor owner")
        if payment == "branch-cover-dispatch":
            require(owner == "same-owner" and ("cover" in continuation or "child" in continuation),
                    f"{path}: branch cover continuation")
        owner_changes += owner != "same-owner"
        payments[payment] = payments.get(payment, 0) + 1
    require(BASE_OPERATION_KIND_COUNT + len(kinds) == 239, "239 installed kinds required")
    return {
        "base_operation_kind_count": BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count": len(kinds),
        "installed_operation_kind_count": 239,
        "bound_contract_count": BASE_CONTRACT_COUNT + 1,
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": 239 - owner_changes,
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
        lambda entries: entries[0].update(owner_effect="same-owner"),
        lambda entries: entries[7].update(owner_effect="same-owner"),
        lambda entries: entries[1].update(owner_effect="host-owner-change"),
        lambda entries: entries.pop(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(NEW_ENTRIES)
        mutate(bad)
        try:
            validate(bad)
        except Registry239Error:
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
        "installed_transition_kind_bank_239_exhaustive": 1,
        "complete_branch_operations_registered": 1,
        "installed_payment_assignment_239_complete": 1,
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
