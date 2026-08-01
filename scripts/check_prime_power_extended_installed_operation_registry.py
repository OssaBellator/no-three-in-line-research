#!/usr/bin/env python3
"""Extend the installed transition registry with Hall-wall and rollback banks.

The checker binds the previous twenty-kind registry digest to nine newly
installed operation kinds from CMR439--CMR447 and CMR727--CMR747.  It proves
exhaustiveness only for the resulting installed twenty-nine-kind bank.
"""
from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from typing import Any


class ExtendedRegistryError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ExtendedRegistryError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


BASE_REGISTRY_SHA256 = "2e92c974075217ac510e37d72dcc4f77fbb4f5bb529d56a727eadbc7dcb70da3"
BASE_OPERATION_KINDS = [
    "single-edge-deletion",
    "required-edge-conditioning",
    "forced-set-contraction",
    "first-missing-deletion",
    "first-missing-conditioned-contraction",
    "routing-skeleton-change",
    "fixed-routing-child-product-split",
    "mixed-clean-strict-child-handoff",
    "mixed-atom-nonessential-edge-deletion",
    "forced-certificate-edge-deletion",
    "forced-certificate-selected-skeleton-churn",
    "forced-certificate-factor-essentiality-loss-restoration",
    "returned-target-edge-restoration",
    "returned-target-edge-redeletion",
    "essential-target-contraction",
    "target-handoff-internal",
    "target-handoff-envelope-expansion",
    "recurrent-target-entering-edge-deletion",
    "closure-envelope-internal-rematch",
    "closure-envelope-strict-expansion",
]
BASE_CONTRACTS = {
    "context-transition": "ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d",
    "routing-change": "b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360",
    "routing-history": "b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259",
    "factor-product": "bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae",
    "mixed-deletion": "b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429",
    "forced-certificate": "dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253",
    "returned-target": "04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382",
    "target-handoff": "a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b",
    "recurrent-target": "a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0",
    "closure-envelope": "50b7720e03295dbde2557ab1d3a11dfc99a8f6d4a9528391555bc4e3adbf91c1",
}
NEW_CONTRACTS = {
    "essential-unit-wall": "97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5",
    "sparse-rollback": "35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267",
}
ALLOWED_OWNER_EFFECTS = {
    "same-owner",
    "host-owner-change",
    "factor-child-owner-change",
    "restoration-owner-change",
    "contraction-owner-change",
}
ALLOWED_PAYMENT_CLASSES = {
    "owner-witness-stock",
    "strict-child-descent",
    "host-edge-deletion",
    "scheduler-dispatch",
    "edge-reintroduction",
    "factor-contraction",
}


def new_registry_entries() -> list[dict[str, Any]]:
    wall = "essential-unit-wall"
    rollback = "sparse-rollback"
    return [
        {
            "operation_kind": "essential-return-unit-wall-extraction",
            "contract": wall,
            "contract_sha256": NEW_CONTRACTS[wall],
            "source_theorems": ["CMR727", "CMR728", "CMR729", "CMR730", "CMR731", "CMR733"],
            "owner_effect": "same-owner",
            "payment_class": "owner-witness-stock",
            "continuation": "canonical unit wall or finite/recurrent wall signature",
        },
        {
            "operation_kind": "essential-unit-wall-factor-split",
            "contract": wall,
            "contract_sha256": NEW_CONTRACTS[wall],
            "source_theorems": ["CMR734", "CMR735", "CMR736", "CMR738"],
            "owner_effect": "factor-child-owner-change",
            "payment_class": "strict-child-descent",
            "continuation": "two exact factors with total side one below parent",
        },
        {
            "operation_kind": "unit-wall-local-edge-deletion",
            "contract": wall,
            "contract_sha256": NEW_CONTRACTS[wall],
            "source_theorems": ["CMR737", "CMR738", "CMR739", "CMR740"],
            "owner_effect": "host-owner-change",
            "payment_class": "host-edge-deletion",
            "continuation": "target inactive and no new prescription activated",
        },
        {
            "operation_kind": "unit-wall-forced-target-dispatch",
            "contract": wall,
            "contract_sha256": NEW_CONTRACTS[wall],
            "source_theorems": ["CMR739", "CMR740", "CMR703"],
            "owner_effect": "same-owner",
            "payment_class": "scheduler-dispatch",
            "continuation": "target scheduler converts forced certificate to a destruction bank",
        },
        {
            "operation_kind": "unit-wall-factor-tree-split",
            "contract": wall,
            "contract_sha256": NEW_CONTRACTS[wall],
            "source_theorems": ["CMR741", "CMR742", "CMR743", "CMR744", "CMR745", "CMR746", "CMR747"],
            "owner_effect": "factor-child-owner-change",
            "payment_class": "strict-child-descent",
            "continuation": "factor-side mass decreases exactly by one",
        },
        {
            "operation_kind": "minimum-rollback-restoration",
            "contract": rollback,
            "contract_sha256": NEW_CONTRACTS[rollback],
            "source_theorems": ["CMR439", "CMR440"],
            "owner_effect": "restoration-owner-change",
            "payment_class": "edge-reintroduction",
            "continuation": "minimum restored footprint creates an avoiding matching",
        },
        {
            "operation_kind": "cheap-rollback-certificate-escape",
            "contract": rollback,
            "contract_sha256": NEW_CONTRACTS[rollback],
            "source_theorems": ["CMR441", "CMR442", "CMR444", "CMR445"],
            "owner_effect": "restoration-owner-change",
            "payment_class": "edge-reintroduction",
            "continuation": "restored-edge token payment followed by target scheduler",
        },
        {
            "operation_kind": "rollback-forced-core-contraction",
            "contract": rollback,
            "contract_sha256": NEW_CONTRACTS[rollback],
            "source_theorems": ["CMR440", "CMR441"],
            "owner_effect": "contraction-owner-change",
            "payment_class": "factor-contraction",
            "continuation": "minimum restored matching core contracts to a strict residual host",
        },
        {
            "operation_kind": "rollback-recreated-conflict-support",
            "contract": rollback,
            "contract_sha256": NEW_CONTRACTS[rollback],
            "source_theorems": ["CMR443", "CMR446", "CMR447"],
            "owner_effect": "same-owner",
            "payment_class": "owner-witness-stock",
            "continuation": "every recreated conflict is assigned to a restored edge",
        },
    ]


def validate_new_entries(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries) == 9, "nine new entries required")
    kinds: set[str] = set(BASE_OPERATION_KINDS)
    owner_changes = 17
    payment_counts: dict[str, int] = {}
    for i, entry in enumerate(entries):
        path = f"entry[{i}]"
        kind = entry.get("operation_kind")
        require(isinstance(kind, str) and kind not in kinds, f"{path}: duplicate or invalid kind")
        kinds.add(kind)
        contract = entry.get("contract")
        require(contract in NEW_CONTRACTS, f"{path}: unknown contract")
        require(entry.get("contract_sha256") == NEW_CONTRACTS[contract], f"{path}: contract mismatch")
        sources = entry.get("source_theorems")
        require(
            isinstance(sources, list)
            and sources
            and all(isinstance(source, str) and source.startswith("CMR") for source in sources),
            f"{path}: theorem ancestry required",
        )
        owner = entry.get("owner_effect")
        payment = entry.get("payment_class")
        continuation = entry.get("continuation")
        require(owner in ALLOWED_OWNER_EFFECTS, f"{path}: invalid owner effect")
        require(payment in ALLOWED_PAYMENT_CLASSES, f"{path}: invalid payment")
        require(isinstance(continuation, str) and continuation, f"{path}: continuation required")
        if payment == "scheduler-dispatch":
            require("scheduler" in continuation, f"{path}: dispatch lacks scheduler")
        owner_changes += owner != "same-owner"
        payment_counts[payment] = payment_counts.get(payment, 0) + 1
    require(len(kinds) == 29, "extended installed bank must contain 29 unique kinds")
    return {
        "installed_operation_kind_count": len(kinds),
        "base_operation_kind_count": len(BASE_OPERATION_KINDS),
        "new_operation_kind_count": len(entries),
        "bound_contract_count": len(BASE_CONTRACTS) + len(NEW_CONTRACTS),
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": len(kinds) - owner_changes,
        "new_payment_counts": payment_counts,
    }


def wall_tree_bounds(d: int) -> dict[str, int]:
    require(isinstance(d, int) and d >= 1, "positive factor side required")
    return {
        "split_bound": d,
        "node_bound": 2 * d + 1,
        "leaf_bound": d + 1,
        "depth_bound": d,
        "edge_stock_bound": sum(j * j for j in range(1, d + 1)),
        "certificate_stock_bound": sum(comb(j * j, 3) for j in range(1, d + 1)),
    }


def rollback_bounds(t: int, p: int, h: int) -> dict[str, int]:
    require(t >= 1 and p >= 2 and h >= 1, "valid rollback parameters required")
    return {
        "per_edge_rollback_bound": t,
        "whole_essential_core_incidence_bound": t * t,
        "whole_core_token_incidence_bound": (p + 1) * (h - 1) * t * t,
    }


def expect_rejection(entries: list[dict[str, Any]], mutator: Any) -> None:
    bad = copy.deepcopy(entries)
    mutator(bad)
    try:
        validate_new_entries(bad)
    except ExtendedRegistryError:
        return
    raise ExtendedRegistryError("corrupted extended registry accepted")


def mutation_audit(entries: list[dict[str, Any]]) -> int:
    mutations = [
        lambda x: x.append(copy.deepcopy(x[0])),
        lambda x: x[0].update(operation_kind=BASE_OPERATION_KINDS[0]),
        lambda x: x[0].update(contract="missing"),
        lambda x: x[0].update(contract_sha256="0" * 64),
        lambda x: x[0].update(source_theorems=[]),
        lambda x: x[0].update(owner_effect="anonymous-owner"),
        lambda x: x[0].update(payment_class="free"),
        lambda x: x[3].update(continuation=""),
        lambda x: x[3].update(continuation="terminal"),
        lambda x: x.pop(),
    ]
    for mutation in mutations:
        expect_rejection(entries, mutation)
    return len(mutations)


CONTRACT = {
    "schema": "prime-power-extended-installed-operation-registry/v1",
    "base_registry_sha256": BASE_REGISTRY_SHA256,
    "base_operation_kinds": BASE_OPERATION_KINDS,
    "base_contracts": BASE_CONTRACTS,
    "new_contracts": NEW_CONTRACTS,
    "new_entries": new_registry_entries(),
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "4df61b20f4d3b2bad19a296a18e00f817ac1a20feda02b77f8486783bb561487"


def main() -> None:
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    entries = new_registry_entries()
    census = validate_new_entries(entries)
    census["wall_tree_d7"] = wall_tree_bounds(7)
    census["rollback_t8_p2_h3"] = rollback_bounds(8, 2, 3)
    census["extended_registry_sha256"] = digest(
        {"base": BASE_REGISTRY_SHA256, "new_entries": entries}
    )
    census["rejected_corruptions"] = mutation_audit(entries)
    report = {
        "contract_digest": contract_digest,
        "census": census,
        "extended_installed_transition_kind_bank_exhaustive": 1,
        "hall_wall_operations_registered": 1,
        "rollback_restoration_operations_registered": 1,
        "extended_installed_payment_assignment_complete": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_envelope_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
