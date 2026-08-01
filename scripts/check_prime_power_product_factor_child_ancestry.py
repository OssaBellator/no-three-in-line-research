#!/usr/bin/env python3
"""Check product-rectangle, factor recursion, routing and forced-child ancestry."""
from __future__ import annotations

import copy
import json
from typing import Any

from product_factor_child_common import ProductFactorChildError, digest, require
from product_factor_child_product import (
    essential_transfer_audit, forced_escape_audit, product_rectangle_audit,
    pure_factor_recursion_audit,
)
from product_factor_child_routing import (
    factor_prefix_routing_audit, mixed_child_recursion_audit,
    multi_child_and_routing_audit,
)

CONTRACT = {
    "schema": "prime-power-product-factor-child-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(629, 691)],
    "fixture_scales": {
        "product_board_side": 5,
        "essential_host_side": 3,
        "prefix_parent_side": 8,
        "routing_factor_side": 4,
        "child_factor_side": 2,
    },
    "required_flags": [
        "product_conflict_rectangle_ancestry_proved",
        "essential_prescription_transfer_exact",
        "forced_product_certificate_escape_exact",
        "pure_factor_essential_recursion_exact",
        "factor_prefix_routing_exact",
        "multi_child_conflict_rectangles_exact",
        "routing_change_edge_support_exact",
        "mixed_child_deletion_recursion_exact",
        "forced_child_certificate_ancestry_exact",
        "product_factor_child_ancestry_proved",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "0ce977177196fbffe8c8ffc446346dde64347999b299307f96ca74d4586e4e12"


def validate_contract(contract: dict[str, Any]) -> None:
    require(contract.get("schema") == "prime-power-product-factor-child-ancestry/v1", "schema")
    sources = contract.get("source_theorems")
    require(sources == [f"CMR{i}" for i in range(629, 691)], "complete CMR629--690 ancestry")
    scales = contract.get("fixture_scales")
    require(isinstance(scales, dict) and all(isinstance(v, int) and v >= 2 for v in scales.values()),
            "fixture scales")
    flags = contract.get("required_flags")
    require(isinstance(flags, list) and len(flags) == 10 and len(set(flags)) == 10, "required flags")
    honesty = contract.get("honesty_flags")
    require(isinstance(honesty, dict) and honesty and all(v == 0 for v in honesty.values()),
            "honesty flags")


def mutation_audit() -> int:
    mutations = [
        lambda c: c.update(schema="anonymous"),
        lambda c: c["source_theorems"].pop(),
        lambda c: c["source_theorems"].append("CMR690"),
        lambda c: c["fixture_scales"].update(product_board_side=1),
        lambda c: c["fixture_scales"].update(prefix_parent_side="8"),
        lambda c: c["required_flags"].pop(),
        lambda c: c["required_flags"].append(c["required_flags"][0]),
        lambda c: c["honesty_flags"].update(global_termination_proved=1),
        lambda c: c.pop("fixture_scales"),
        lambda c: c.pop("honesty_flags"),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(CONTRACT)
        mutate(bad)
        try:
            validate_contract(bad)
        except (ProductFactorChildError, AttributeError, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "contract corruption accepted")
    return rejected


def main() -> None:
    validate_contract(copy.deepcopy(CONTRACT))
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    report = {
        "contract_digest": contract_digest,
        "product_rectangle": product_rectangle_audit(),
        "essential_transfer": essential_transfer_audit(),
        "forced_escape": forced_escape_audit(),
        "pure_factor_recursion": pure_factor_recursion_audit(),
        "factor_prefix_routing": factor_prefix_routing_audit(),
        "multi_child_and_routing": multi_child_and_routing_audit(),
        "mixed_child_recursion": mixed_child_recursion_audit(),
        "rejected_corruptions": mutation_audit(),
        "product_conflict_rectangle_ancestry_proved": 1,
        "essential_prescription_transfer_exact": 1,
        "forced_product_certificate_escape_exact": 1,
        "pure_factor_essential_recursion_exact": 1,
        "factor_prefix_routing_exact": 1,
        "multi_child_conflict_rectangles_exact": 1,
        "routing_change_edge_support_exact": 1,
        "mixed_child_deletion_recursion_exact": 1,
        "forced_child_certificate_ancestry_exact": 1,
        "product_factor_child_ancestry_proved": 1,
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
