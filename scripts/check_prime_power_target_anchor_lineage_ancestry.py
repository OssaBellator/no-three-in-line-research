#!/usr/bin/env python3
"""Check target reserve, return ancestry, anchor normalization and edge lineage."""
from __future__ import annotations

import copy
import json
from typing import Any

from target_anchor_common import TargetAnchorError, digest, require
from target_anchor_target import (
    labelled_target_pair_audit,
    neutralized_temporal_audit,
    pair_neutralization_audit,
    return_forest_audit,
    target_line_reserve_audit,
)
from target_anchor_anchor import (
    active_context_audit,
    anchor_batch_audit,
    anchor_restoration_audit,
    physical_edge_lineage_audit,
)

CONTRACT = {
    "schema": "prime-power-target-anchor-lineage-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(748, 830)],
    "fixture_scales": {
        "line_board_min": 6,
        "line_board_max": 10,
        "neutralization_board": 8,
        "labelled_pair_host": 3,
        "anchor_state_side": 3,
        "return_forest_generations": 6,
    },
    "required_flags": [
        "recurrent_target_line_reserve_exact",
        "protected_line_pair_neutralization_exact",
        "neutralized_pair_temporal_ledger_exact",
        "recurrent_labelled_target_pair_ancestry_proved",
        "global_return_ancestry_forest_exact",
        "anchor_state_batch_rejection_exact",
        "anchor_batch_restoration_ledger_exact",
        "stored_anchor_bulk_redeletion_exact",
        "private_batch_normalization_exact",
        "active_context_absorption_exact",
        "physical_edge_lineage_exact",
        "target_anchor_lineage_ancestry_proved",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "2f846aa50012d196dffc90511de0c254782b1a5696b1cb25ee1cf1b73a990359"


def validate_contract(contract: dict[str, Any]) -> None:
    require(contract.get("schema") == "prime-power-target-anchor-lineage-ancestry/v1",
            "schema")
    require(contract.get("source_theorems") == [f"CMR{i}" for i in range(748, 830)],
            "complete CMR748--829 ancestry")
    scales = contract.get("fixture_scales")
    require(isinstance(scales, dict) and len(scales) == 6
            and all(isinstance(value, int) and value >= 3 for value in scales.values()),
            "fixture scales")
    flags = contract.get("required_flags")
    require(isinstance(flags, list) and len(flags) == 12 and len(set(flags)) == 12,
            "flags")
    honesty = contract.get("honesty_flags")
    require(isinstance(honesty, dict) and honesty and all(value == 0 for value in honesty.values()),
            "honesty")


def mutation_audit() -> int:
    mutations = [
        lambda contract: contract.update(schema="anonymous"),
        lambda contract: contract["source_theorems"].pop(),
        lambda contract: contract["source_theorems"].append("CMR829"),
        lambda contract: contract["fixture_scales"].update(line_board_min=2),
        lambda contract: contract["fixture_scales"].update(anchor_state_side="3"),
        lambda contract: contract["required_flags"].pop(),
        lambda contract: contract["required_flags"].append(contract["required_flags"][0]),
        lambda contract: contract["honesty_flags"].update(global_termination_proved=1),
        lambda contract: contract.pop("fixture_scales"),
        lambda contract: contract.pop("honesty_flags"),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(CONTRACT)
        mutate(bad)
        try:
            validate_contract(bad)
        except (TargetAnchorError, AttributeError, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    validate_contract(copy.deepcopy(CONTRACT))
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest")
    report = {
        "contract_digest": contract_digest,
        "target_line_reserve": target_line_reserve_audit(),
        "pair_neutralization": pair_neutralization_audit(),
        "neutralized_temporal": neutralized_temporal_audit(),
        "labelled_target_pair": labelled_target_pair_audit(),
        "return_forest": return_forest_audit(),
        "anchor_batch": anchor_batch_audit(),
        "anchor_restoration": anchor_restoration_audit(),
        "active_context": active_context_audit(),
        "physical_edge_lineage": physical_edge_lineage_audit(),
        "rejected_corruptions": mutation_audit(),
        "recurrent_target_line_reserve_exact": 1,
        "protected_line_pair_neutralization_exact": 1,
        "neutralized_pair_temporal_ledger_exact": 1,
        "recurrent_labelled_target_pair_ancestry_proved": 1,
        "global_return_ancestry_forest_exact": 1,
        "anchor_state_batch_rejection_exact": 1,
        "anchor_batch_restoration_ledger_exact": 1,
        "stored_anchor_bulk_redeletion_exact": 1,
        "private_batch_normalization_exact": 1,
        "active_context_absorption_exact": 1,
        "physical_edge_lineage_exact": 1,
        "target_anchor_lineage_ancestry_proved": 1,
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
