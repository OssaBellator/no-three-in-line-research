#!/usr/bin/env python3
"""Validate exact rank-three and unresolved residual side-four return obligations."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from collections import Counter
from pathlib import Path
from typing import Any

class ResidualReturnObligationError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ResidualReturnObligationError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

RETURN_CHECKER_PATH = "scripts/check_prime_power_side_four_return_exchange_context.py"
SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
RETURN_CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
CONTRACT_PATH = "data/prime_power_side_four_residual_return_obligation_contract.json"
EXPECTED_RETURN_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_RETURN_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"
EXPECTED_CONTRACT_SHA256 = "c256cedf67c092ecb7229fd7bfda9d5b4194ce630777de6ea2011bd179e6974f"
CLASSES = (
    "rank-three-selected-response",
    "rank-one-background",
    "rank-two-background",
    "selector-token",
    "other-labelled",
)

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ResidualReturnObligationError("unable to locate repository root")

def load_return_checker(path: Path) -> Any:
    require(path.is_file(), "return checker missing")
    spec = importlib.util.spec_from_file_location("side_four_return_checker", path)
    require(spec is not None and spec.loader is not None, "return checker import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-residual-return-obligation-contract/v1",
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "credit_classes": list(CLASSES),
        "class_rules": {
            "rank-three-selected-response": "exact recreated-credit count and returned-edge charge kernel from the sealed return context",
            "rank-one-background": "unresolved until the actual background-height and line-owner profile is attached",
            "rank-two-background": "unresolved until the actual background-height and line-owner profile is attached",
            "selector-token": "unresolved until selector/token state and child routing are attached",
            "other-labelled": "unresolved catch-all prohibited from being treated as zero; must be refined before completion",
        },
        "aggregate": {
            "rows": 86,
            "return_class_slots": 430,
            "exact_rank_three_coefficients": 86,
            "exact_rank_three_total": 17,
            "exact_rank_three_positive_rows": 11,
            "exact_rank_three_zero_rows": 75,
            "exact_rank_three_kernel_entries": 13,
            "unresolved_residual_coefficient_slots": 344,
            "unresolved_return_child_keys": 430,
            "unresolved_return_child_weights": 430,
            "residual_class_slots_by_class": {
                "rank-one-background": 86,
                "rank-two-background": 86,
                "selector-token": 86,
                "other-labelled": 86,
            },
        },
        "resolution_order": [
            "attach exact background-height and line-owner profiles for rank-one and rank-two credits",
            "attach selector/token state and return child routing",
            "refine other-labelled into explicit finite credit classes",
            "bind every return class to one child key and positive weight",
            "sum the completed classes into the total return coefficient",
        ],
        "honesty": {
            "residual_return_worklist_complete_for_normalized_block": 1,
            "rank_three_return_coefficients_complete": 1,
            "residual_return_credit_classes_complete": 0,
            "complete_return_coefficient_rule_complete": 0,
            "return_child_keys_complete": 0,
            "return_child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def compile_obligations(return_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    obligations: list[dict[str, Any]] = []
    for row in return_rows:
        rank_three = row["rank_three_kernel"]["recreated_credit_count"]
        classes = []
        for credit_class in CLASSES:
            if credit_class == "rank-three-selected-response":
                classes.append({
                    "credit_class": credit_class,
                    "coefficient_status": "known",
                    "coefficient": rank_three,
                    "charge_kernel": row["rank_three_kernel"]["charges"],
                    "child_key": None,
                    "child_weight": None,
                    "resolution": "child-key-and-weight-unresolved",
                })
            else:
                classes.append({
                    "credit_class": credit_class,
                    "coefficient_status": "unresolved",
                    "coefficient": None,
                    "charge_kernel": None,
                    "child_key": None,
                    "child_weight": None,
                    "resolution": "coefficient-class-refinement-child-key-and-weight-unresolved",
                })
        obligations.append({
            "host_id": row["host_id"],
            "selected_response": row["selected_response"],
            "fate": row["fate"],
            "classes": classes,
        })
    return obligations

def validate(root: Path, contract: dict[str, Any]) -> list[dict[str, Any]]:
    checker = load_return_checker(root / RETURN_CHECKER_PATH)
    require(checker.EXPECTED_CONTRACT_SHA256 == EXPECTED_RETURN_CONTRACT_SHA256, "return contract binding")
    require(checker.EXPECTED_COMPILED_CONTEXT_ROW_SHA256 == EXPECTED_RETURN_CONTEXT_ROW_SHA256, "return row binding")
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    return_contract = json.loads((root / RETURN_CONTRACT_PATH).read_text(encoding="utf-8"))
    return_rows = checker.validate(selected, return_contract)
    require(contract == expected_contract(), "residual return contract differs from canonical schema")
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "residual return contract digest mismatch")
    obligations = compile_obligations(return_rows)
    require(len(obligations) == 86, "return obligation row count")
    statuses = Counter()
    exact_total = 0
    exact_positive = 0
    kernel_entries = 0
    for row in obligations:
        classes = row["classes"]
        require([item["credit_class"] for item in classes] == list(CLASSES), f"{row['host_id']}: class order")
        for item in classes:
            statuses[item["coefficient_status"]] += 1
            require(item["child_key"] is None and item["child_weight"] is None, f"{row['host_id']}: unresolved child binding")
            if item["credit_class"] == "rank-three-selected-response":
                require(item["coefficient_status"] == "known", f"{row['host_id']}: rank-three status")
                require(isinstance(item["coefficient"], int) and item["coefficient"] >= 0, f"{row['host_id']}: rank-three coefficient")
                require(isinstance(item["charge_kernel"], list), f"{row['host_id']}: rank-three kernel")
                require(item["resolution"] == "child-key-and-weight-unresolved", f"{row['host_id']}: rank-three resolution")
                exact_total += item["coefficient"]
                exact_positive += item["coefficient"] > 0
                kernel_entries += len(item["charge_kernel"])
            else:
                require(item["coefficient_status"] == "unresolved" and item["coefficient"] is None, f"{row['host_id']}: residual coefficient")
                require(item["charge_kernel"] is None, f"{row['host_id']}: residual kernel")
                require(item["resolution"] == "coefficient-class-refinement-child-key-and-weight-unresolved", f"{row['host_id']}: residual resolution")
    require(statuses == Counter({"unresolved": 344, "known": 86}), "return obligation status census")
    require((exact_total, exact_positive, kernel_entries) == (17, 11, 13), "rank-three return census")
    return obligations

def mutation_audit(root: Path, contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rows=85),
        lambda item: item["aggregate"].update(return_class_slots=429),
        lambda item: item["aggregate"].update(exact_rank_three_total=16),
        lambda item: item["aggregate"].update(unresolved_residual_coefficient_slots=343),
        lambda item: item["credit_classes"].pop(),
        lambda item: item["class_rules"].update({"rank-one-background": "zero"}),
        lambda item: item["class_rules"].update({"other-labelled": "ignore"}),
        lambda item: item["resolution_order"].pop(),
        lambda item: item["honesty"].update(residual_return_credit_classes_complete=1),
        lambda item: item["honesty"].update(complete_return_coefficient_rule_complete=1),
        lambda item: item["honesty"].update(return_child_keys_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(root, bad)
        except ResidualReturnObligationError:
            rejected += 1
    require(rejected == len(mutations), "residual return corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    contract = json.loads((root / CONTRACT_PATH).read_text(encoding="utf-8"))
    obligations = validate(root, contract)
    compiled_sha256 = digest(obligations)
    print(json.dumps({
        "checker": "prime-power-side-four-residual-return-obligations",
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "residual_return_contract_sha256": EXPECTED_CONTRACT_SHA256,
        "compiled_residual_return_obligation_sha256": compiled_sha256,
        "row_count": 86,
        "return_class_slot_count": 430,
        "known_rank_three_coefficient_count": 86,
        "known_rank_three_coefficient_total": 17,
        "unresolved_residual_coefficient_count": 344,
        "unresolved_return_child_key_count": 430,
        "unresolved_return_child_weight_count": 430,
        "rejected_corruptions": mutation_audit(root, contract),
        "side_four_residual_return_obligation_worklist_complete": 1,
        "rank_three_return_coefficients_complete": 1,
        "residual_return_credit_classes_complete": 0,
        "complete_return_coefficient_rule_complete": 0,
        "return_child_keys_complete": 0,
        "return_child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
