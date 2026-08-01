#!/usr/bin/env python3
"""Seal CMR691--CMR747 coverage by the inherited owner, target and wall banks."""
from __future__ import annotations

import copy
import hashlib
import json
from math import comb, floor
from typing import Any

import check_prime_power_installed_owner_scheduler_bank as owner
import check_prime_power_target_handoff_envelope_ancestry as handoff
import check_prime_power_recurrent_target_edge_deletion_ancestry as recurrent
import check_prime_power_target_edge_return_ancestry as returned
import check_prime_power_essential_return_unit_wall_ancestry as wall
import check_prime_power_extended_installed_operation_registry as extended
import check_prime_power_installed_operation_registry_188 as registry188


class OwnerTargetWallCoverageError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise OwnerTargetWallCoverageError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


CHECKER_BINDINGS = {
    "scripts/check_prime_power_installed_owner_scheduler_bank.py": {
        "contract": "108802c0d4934c7b3d77cc972d5418a2d8b91a6cca9da78b49bc4ab58970ad26",
        "theorems": [f"CMR{i}" for i in range(691, 720)],
    },
    "scripts/check_prime_power_target_handoff_envelope_ancestry.py": {
        "contract": "a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b",
        "theorems": [f"CMR{i}" for i in range(698, 713)],
    },
    "scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py": {
        "contract": "a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0",
        "theorems": [f"CMR{i}" for i in range(713, 720)],
    },
    "scripts/check_prime_power_target_edge_return_ancestry.py": {
        "contract": "04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382",
        "theorems": [f"CMR{i}" for i in range(720, 727)],
    },
    "scripts/check_prime_power_essential_return_unit_wall_ancestry.py": {
        "contract": "97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5",
        "theorems": [f"CMR{i}" for i in range(727, 748)],
    },
    "scripts/check_prime_power_extended_installed_operation_registry.py": {
        "contract": "4df61b20f4d3b2bad19a296a18e00f817ac1a20feda02b77f8486783bb561487",
        "theorems": [f"CMR{i}" for i in range(727, 748)],
    },
}

CANONICAL_REGISTRY_CONTRACT = "f70e412fffd0e8e1c0987fe3b274d138b382a8624867c6e2f0b3ebc0193a034e"

EXPECTED_OPERATION_KINDS = {
    "target-handoff-internal",
    "target-handoff-envelope-expansion",
    "recurrent-target-entering-edge-deletion",
    "returned-target-edge-restoration",
    "returned-target-edge-redeletion",
    "essential-target-contraction",
    "essential-return-unit-wall-extraction",
    "essential-unit-wall-factor-split",
    "unit-wall-local-edge-deletion",
    "unit-wall-forced-target-dispatch",
    "unit-wall-factor-tree-split",
}

CONTRACT = {
    "schema": "prime-power-owner-target-wall-coverage/v1",
    "theorem_interval": [691, 747],
    "checker_bindings": CHECKER_BINDINGS,
    "expected_operation_kinds": sorted(EXPECTED_OPERATION_KINDS),
    "canonical_registry_contract": CANONICAL_REGISTRY_CONTRACT,
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "3038c3f03bb8485f5dd6c03efaa894a2354e675c74324bd1532c422f1c1a0feb"


def theorem_number(value: str) -> int:
    require(isinstance(value, str) and value.startswith("CMR"), "theorem id")
    return int(value[3:])


def validate_contract(contract: dict[str, Any]) -> None:
    require(contract.get("schema") == "prime-power-owner-target-wall-coverage/v1", "schema")
    require(contract.get("theorem_interval") == [691, 747], "theorem interval")
    bindings = contract.get("checker_bindings")
    require(bindings == CHECKER_BINDINGS, "bindings")
    covered = {theorem_number(t) for item in bindings.values() for t in item["theorems"]}
    require(set(range(691, 748)) <= covered, "CMR691--747 coverage gap")
    kinds = contract.get("expected_operation_kinds", [])
    require(kinds == sorted(EXPECTED_OPERATION_KINDS) and len(kinds) == len(set(kinds)),
            "operation kinds")
    require(contract.get("canonical_registry_contract") == CANONICAL_REGISTRY_CONTRACT,
            "canonical registry contract")
    honesty = contract.get("honesty_flags")
    require(isinstance(honesty, dict) and honesty and all(v == 0 for v in honesty.values()),
            "honesty")


def exact_checker_bindings() -> None:
    require(owner.EXPECTED_CONTRACT_SHA256 == CHECKER_BINDINGS[
        "scripts/check_prime_power_installed_owner_scheduler_bank.py"]["contract"], "owner contract")
    require(handoff.EXPECTED_CONTRACT_SHA256 == CHECKER_BINDINGS[
        "scripts/check_prime_power_target_handoff_envelope_ancestry.py"]["contract"], "handoff contract")
    require(recurrent.EXPECTED_CONTRACT_SHA256 == CHECKER_BINDINGS[
        "scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py"]["contract"], "recurrent contract")
    require(returned.EXPECTED_CONTRACT_SHA256 == CHECKER_BINDINGS[
        "scripts/check_prime_power_target_edge_return_ancestry.py"]["contract"], "return contract")
    require(wall.EXPECTED_CONTRACT_DIGEST == CHECKER_BINDINGS[
        "scripts/check_prime_power_essential_return_unit_wall_ancestry.py"]["contract"], "wall contract")
    require(extended.EXPECTED_CONTRACT_DIGEST == CHECKER_BINDINGS[
        "scripts/check_prime_power_extended_installed_operation_registry.py"]["contract"], "extended contract")
    require(registry188.EXPECTED_CONTRACT_DIGEST == CONTRACT["canonical_registry_contract"],
            "canonical registry contract")


def relevant_operation_entries() -> list[dict[str, Any]]:
    entries = []
    for entry in owner.installed_registry():
        numbers = {theorem_number(t) for t in entry["source_theorems"]}
        if numbers & set(range(698, 727)):
            entries.append(entry)
    for entry in extended.new_registry_entries():
        numbers = {theorem_number(t) for t in entry["source_theorems"]}
        if numbers & set(range(727, 748)):
            entries.append(entry)
    return entries


def operation_coverage_audit() -> dict[str, int]:
    entries = relevant_operation_entries()
    kinds = {entry["operation_kind"] for entry in entries}
    require(kinds == EXPECTED_OPERATION_KINDS, "existing operation coverage mismatch")
    new_kinds = {entry["operation_kind"] for entry in registry188.NEW_ENTRIES}
    require(kinds.isdisjoint(new_kinds), "CMR691--747 kind duplicated in new 188 extension")
    owner_effects = {entry["owner_effect"] for entry in entries}
    payments = {entry["payment_class"] for entry in entries}
    require({"same-owner", "host-owner-change", "factor-child-owner-change"} <= owner_effects,
            "owner effects incomplete")
    require("scheduler-dispatch" in payments, "scheduler payment absent")
    return {
        "covered_existing_operation_kinds": len(kinds),
        "duplicate_new_operation_kinds": 0,
        "owner_effect_classes": len(owner_effects),
        "payment_classes": len(payments),
    }


def owner_stock_audit() -> dict[str, int]:
    checks = 0
    for d in range(1, 9):
        for lam in range(2, 6):
            for m in range(1, d + 1):
                require(owner.host_stage_count(m) == 2 * m * m + m + 1, "CMR691")
                require(owner.routing_change_bound(m, lam) == floor((lam - 1) * m * m / 2), "CMR692")
            O = sum((2*m*m+m+1)*(1+floor((lam-1)*m*m/2)) for m in range(1,d+1))
            E = sum((2*m*m+m+1)*(1+floor((lam-1)*m*m/2))*m*m for m in range(1,d+1))
            C = sum((2*m*m+m+1)*(1+floor((lam-1)*m*m/2))*comb(m*m,3) for m in range(1,d+1))
            require(owner.owner_stage_stock(d, lam) == O, "CMR693")
            require(owner.owner_edge_stock(d, lam) == E, "CMR694")
            require(owner.owner_certificate_stock(d, lam) == C, "CMR695")
            ambient = 8
            require(owner.owner_target_pair_stock(d, lam, ambient) == 3*O*comb(ambient*ambient,3),
                    "owner target pair stock")
            checks += 1
    return {"owner_stock_parameter_profiles": checks}


def wall_tree_audit() -> dict[str, int]:
    checks = 0
    for side in range(1, 8):
        splits, nodes, leaves, depth, edge_stock, cert_stock = wall.max_tree_metrics(side)
        bounds = extended.wall_tree_bounds(side)
        require(splits <= bounds["split_bound"], "wall split")
        require(nodes <= bounds["node_bound"], "wall nodes")
        require(leaves <= bounds["leaf_bound"], "wall leaves")
        require(depth <= bounds["depth_bound"], "wall depth")
        require(edge_stock <= bounds["edge_stock_bound"], "wall edge stock")
        require(cert_stock <= bounds["certificate_stock_bound"], "wall certificate stock")
        checks += 1
    return {"unit_wall_tree_side_profiles": checks}


def mutation_audit() -> int:
    mutations = [
        lambda c: c.update(schema="anonymous"),
        lambda c: c.update(theorem_interval=[692, 747]),
        lambda c: c["checker_bindings"].pop(next(iter(c["checker_bindings"]))),
        lambda c: c["checker_bindings"][next(iter(c["checker_bindings"]))]["theorems"].clear(),
        lambda c: c["expected_operation_kinds"].pop(),
        lambda c: c["expected_operation_kinds"].append(c["expected_operation_kinds"][0]),
        lambda c: c.update(canonical_registry_contract="0"*64),
        lambda c: c["honesty_flags"].update(global_termination_proved=1),
        lambda c: c.pop("checker_bindings"),
        lambda c: c.pop("honesty_flags"),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(CONTRACT)
        mutate(bad)
        try:
            validate_contract(bad)
        except (OwnerTargetWallCoverageError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "coverage corruption accepted")
    return rejected


def main() -> None:
    validate_contract(copy.deepcopy(CONTRACT))
    exact_checker_bindings()
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest")
    report = {
        "contract_digest": contract_digest,
        "operation_coverage": operation_coverage_audit(),
        "owner_stock": owner_stock_audit(),
        "unit_wall_tree": wall_tree_audit(),
        "rejected_corruptions": mutation_audit(),
        "cmr691_747_existing_operation_coverage_exact": 1,
        "descending_path_owner_stock_revalidated": 1,
        "target_return_unit_wall_coverage_exact": 1,
        "no_duplicate_operation_registration_required": 1,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
