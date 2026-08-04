#!/usr/bin/env python3
"""Compile and validate the side-four compulsory coefficient dependency map."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from collections import Counter
from pathlib import Path
from typing import Any

class CoefficientDependencyError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise CoefficientDependencyError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

OBLIGATION_CHECKER_PATH = "scripts/check_prime_power_side_four_compulsory_row_obligation_worklist.py"
RETURN_CHECKER_PATH = "scripts/check_prime_power_side_four_return_exchange_context.py"
SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
OBLIGATION_CONTRACT_PATH = "data/prime_power_side_four_compulsory_row_obligation_worklist.json"
RETURN_CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
DEPENDENCY_CONTRACT_PATH = "data/prime_power_side_four_compulsory_coefficient_dependency_contract.json"
EXPECTED_OBLIGATION_CONTRACT_SHA256 = "62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211"
EXPECTED_OBLIGATION_ROW_SHA256 = "b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b"
EXPECTED_RETURN_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_RETURN_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"
EXPECTED_DEPENDENCY_CONTRACT_SHA256 = "47c765be4b4a79f826dba2ac23fb2d7a69f0d64ba23bb94d1cb1d608178fbacc"
EXPECTED_DEPENDENCY_RECORD_SHA256 = "4cd91e195393ea226474c3c33f80ac63fcdd9c4b8b0bf95b810f54d0c490d401"

CATEGORY_SPECS = {
    "return": {
        "required_inputs": [
            "return_exchange_class",
            "returned_edge_or_token_state",
            "return_child_key",
            "return_coefficient_rule",
        ],
        "available_context_inputs": ["return_exchange_class", "returned_edge_or_token_state"],
        "coefficient_source": "exact returned-edge exchange context and exact rank-three return subkernel; residual classes and total coefficient rule remain missing",
    },
    "selector": {
        "required_inputs": [
            "minimizer_face",
            "next_energy_gap",
            "complete_coupled_response_score",
            "selector_child_key",
            "selector_coefficient_rule",
        ],
        "available_context_inputs": ["minimizer_face", "next_energy_gap"],
        "coefficient_source": "complete coupled response score, not response-triple energy alone",
    },
    "collision": {
        "required_inputs": [
            "deletion_collision_trace",
            "child_owner",
            "child_fate",
            "child_collision_class",
            "collision_coefficient_rule",
        ],
        "available_context_inputs": ["deletion_collision_trace"],
        "coefficient_source": "owner/fate/collision child routing",
    },
    "line": {
        "required_inputs": [
            "selected_response_line_signature",
            "background_height_profile",
            "line_owner_labels",
            "line_coefficient_rule",
        ],
        "available_context_inputs": ["selected_response_line_signature"],
        "coefficient_source": "complete line-energy kernel on the actual background profile",
    },
    "interface": {
        "required_inputs": [
            "normalized_target_interface",
            "child_interface_route",
            "interface_provenance",
            "interface_coefficient_rule",
        ],
        "available_context_inputs": ["normalized_target_interface"],
        "coefficient_source": "label-preserving interface routing",
    },
    "geometric": {
        "required_inputs": ["minimum_energy", "geometric_child_key", "geometric_child_weight"],
        "available_context_inputs": ["minimum_energy"],
        "coefficient_source": "selected minimum response energy",
    },
}

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise CoefficientDependencyError("unable to locate repository root")

def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: missing checker")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def known_value(context: dict[str, Any], return_row: dict[str, Any], input_name: str) -> Any:
    mapping = {
        "return_exchange_class": "|".join(exchange[4] for exchange in return_row["exchanges"]),
        "returned_edge_or_token_state": json.dumps({
            "exchanges": [[exchange[1], exchange[2], exchange[3]] for exchange in return_row["exchanges"]],
            "rank_three_charges": return_row["rank_three_kernel"]["charges"],
        }, sort_keys=True, separators=(",", ":")),
        "minimizer_face": context["minimizer_face"],
        "next_energy_gap": context["next_energy_gap"],
        "deletion_collision_trace": context["collision_key"],
        "selected_response_line_signature": context["local_line_signature"],
        "normalized_target_interface": context["interface_label"],
        "minimum_energy": context["minimum_energy"],
    }
    require(input_name in mapping, f"{input_name}: unavailable context mapping")
    return mapping[input_name]

def compile_records(rows: list[dict[str, Any]], return_rows: list[dict[str, Any]], categories: tuple[str, ...]) -> list[dict[str, Any]]:
    return_by_host = {row["host_id"]: row for row in return_rows}
    require(len(return_by_host) == len(return_rows) == 86, "return row host coverage")
    records: list[dict[str, Any]] = []
    for row in rows:
        context = row["context"]
        require(context["host_id"] in return_by_host, f"{context['host_id']}: return context missing")
        return_row = return_by_host[context["host_id"]]
        require(return_row["selected_response"] == context["selected_response"], f"{context['host_id']}: selector/return mismatch")
        for category in categories:
            spec = CATEGORY_SPECS[category]
            known_inputs = {name: known_value(context, return_row, name) for name in spec["available_context_inputs"]}
            missing_inputs = [name for name in spec["required_inputs"] if name not in spec["available_context_inputs"]]
            coefficient_status = "known" if category == "geometric" else "unresolved"
            dependency_status = "coefficient-known-binding-unresolved" if category == "geometric" else "partially-grounded"
            records.append({
                "host_id": context["host_id"],
                "category": category,
                "coefficient_status": coefficient_status,
                "known_inputs": known_inputs,
                "missing_inputs": missing_inputs,
                "dependency_status": dependency_status,
            })
    return records

def expected_contract(categories: tuple[str, ...]) -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-compulsory-coefficient-dependency-contract/v3",
        "obligation_contract_sha256": EXPECTED_OBLIGATION_CONTRACT_SHA256,
        "compiled_obligation_row_sha256": EXPECTED_OBLIGATION_ROW_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "compiled_dependency_record_sha256": EXPECTED_DEPENDENCY_RECORD_SHA256,
        "category_order": list(categories),
        "category_specs": CATEGORY_SPECS,
        "aggregate": {
            "records": 516,
            "coefficient_known_records": 86,
            "coefficient_unresolved_records": 430,
            "child_binding_unresolved_records": 516,
            "known_input_occurrences": 688,
            "missing_input_occurrences": 1462,
            "ungrounded_records": 0,
            "partially_grounded_records": 430,
            "coefficient_known_binding_unresolved_records": 86,
            "category_census": {
                "return": {"records": 86, "known_coefficients": 0, "unresolved_coefficients": 86, "known_input_occurrences": 172, "missing_input_occurrences": 172, "dependency_status": "partially-grounded"},
                "selector": {"records": 86, "known_coefficients": 0, "unresolved_coefficients": 86, "known_input_occurrences": 172, "missing_input_occurrences": 258, "dependency_status": "partially-grounded"},
                "collision": {"records": 86, "known_coefficients": 0, "unresolved_coefficients": 86, "known_input_occurrences": 86, "missing_input_occurrences": 344, "dependency_status": "partially-grounded"},
                "line": {"records": 86, "known_coefficients": 0, "unresolved_coefficients": 86, "known_input_occurrences": 86, "missing_input_occurrences": 258, "dependency_status": "partially-grounded"},
                "interface": {"records": 86, "known_coefficients": 0, "unresolved_coefficients": 86, "known_input_occurrences": 86, "missing_input_occurrences": 258, "dependency_status": "partially-grounded"},
                "geometric": {"records": 86, "known_coefficients": 86, "unresolved_coefficients": 0, "known_input_occurrences": 86, "missing_input_occurrences": 172, "dependency_status": "coefficient-known-binding-unresolved"},
            },
            "collision_rank_census": {"0": 1, "1": 11, "2": 35, "3": 33, "4": 6},
            "selector_census": {"2031": 34, "2301": 15, "2310": 13, "3012": 9, "3201": 13, "3210": 2},
            "selector_face_census": {"unique": 42, "tied": 44},
            "positive_gap_rows": 47,
            "no_higher_energy_rows": 39,
        },
        "resolution_priority": [
            "return: enumerate residual non-rank-three credit classes and derive the total coefficient rule and child key",
            "line: attach actual background-height profile and line ownership",
            "collision: attach child owner/fate/collision routing",
            "interface: attach child interface route and provenance",
            "selector: evaluate the complete coupled score on the full minimizer face",
            "all categories: attach exact child keys and positive weights",
        ],
        "honesty": {
            "dependency_map_complete_for_normalized_block": 1,
            "unresolved_coefficients_populated": 0,
            "global_child_provenance_complete": 0,
            "child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def validate(root: Path, contract: dict[str, Any]) -> list[dict[str, Any]]:
    obligation = load_module(root / OBLIGATION_CHECKER_PATH, "side_four_obligation_checker")
    return_checker = load_module(root / RETURN_CHECKER_PATH, "side_four_return_checker")
    require(obligation.EXPECTED_CONTRACT_SHA256 == EXPECTED_OBLIGATION_CONTRACT_SHA256, "obligation contract binding")
    require(obligation.EXPECTED_COMPILED_ROW_SHA256 == EXPECTED_OBLIGATION_ROW_SHA256, "obligation row binding")
    require(return_checker.EXPECTED_CONTRACT_SHA256 == EXPECTED_RETURN_CONTRACT_SHA256, "return contract binding")
    require(return_checker.EXPECTED_COMPILED_CONTEXT_ROW_SHA256 == EXPECTED_RETURN_CONTEXT_ROW_SHA256, "return context row binding")
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    obligation_contract = json.loads((root / OBLIGATION_CONTRACT_PATH).read_text(encoding="utf-8"))
    return_contract = json.loads((root / RETURN_CONTRACT_PATH).read_text(encoding="utf-8"))
    rows = obligation.validate(selected, obligation_contract)
    return_rows = return_checker.validate(selected, return_contract)
    categories = tuple(obligation.CATEGORIES)
    require(contract == expected_contract(categories), "dependency contract differs from canonical schema")
    require(digest(contract) == EXPECTED_DEPENDENCY_CONTRACT_SHA256, "dependency contract digest mismatch")
    records = compile_records(rows, return_rows, categories)
    require(len(records) == 516, "dependency record count")
    require(digest(records) == EXPECTED_DEPENDENCY_RECORD_SHA256, "dependency record digest mismatch")
    status = Counter(record["dependency_status"] for record in records)
    require(status == Counter({"partially-grounded": 430, "coefficient-known-binding-unresolved": 86}), "dependency status census")
    coefficient = Counter(record["coefficient_status"] for record in records)
    require(coefficient == Counter({"unresolved": 430, "known": 86}), "coefficient status census")
    known_occurrences = sum(len(record["known_inputs"]) for record in records)
    missing_occurrences = sum(len(record["missing_inputs"]) for record in records)
    require((known_occurrences, missing_occurrences) == (688, 1462), "input occurrence census")
    return records

def mutation_audit(root: Path, contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(records=515),
        lambda item: item["aggregate"].update(missing_input_occurrences=1461),
        lambda item: item.update(compiled_dependency_record_sha256="0" * 64),
        lambda item: item.update(return_exchange_contract_sha256="0" * 64),
        lambda item: item["category_order"].pop(),
        lambda item: item["category_specs"]["return"]["available_context_inputs"].remove("return_exchange_class"),
        lambda item: item["category_specs"]["return"].update(coefficient_source="churn magnitude"),
        lambda item: item["category_specs"]["selector"]["available_context_inputs"].remove("next_energy_gap"),
        lambda item: item["category_specs"]["line"]["available_context_inputs"].append("background_height_profile"),
        lambda item: item["resolution_priority"].pop(),
        lambda item: item["honesty"].update(unresolved_coefficients_populated=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(root, bad)
        except CoefficientDependencyError:
            rejected += 1
    require(rejected == len(mutations), "dependency contract corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    contract = json.loads((root / DEPENDENCY_CONTRACT_PATH).read_text(encoding="utf-8"))
    records = validate(root, contract)
    print(json.dumps({
        "checker": "prime-power-side-four-compulsory-coefficient-dependency-map",
        "obligation_contract_sha256": EXPECTED_OBLIGATION_CONTRACT_SHA256,
        "compiled_obligation_row_sha256": EXPECTED_OBLIGATION_ROW_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "dependency_contract_sha256": EXPECTED_DEPENDENCY_CONTRACT_SHA256,
        "compiled_dependency_record_sha256": EXPECTED_DEPENDENCY_RECORD_SHA256,
        "dependency_record_count": len(records),
        "unresolved_coefficient_record_count": 430,
        "known_coefficient_record_count": 86,
        "known_input_occurrence_count": 688,
        "missing_input_occurrence_count": 1462,
        "partially_grounded_record_count": 430,
        "rejected_corruptions": mutation_audit(root, contract),
        "side_four_compulsory_coefficient_dependency_map_complete": 1,
        "return_exchange_context_attached": 1,
        "dependency_map_complete_for_normalized_block": 1,
        "unresolved_coefficients_populated": 0,
        "global_child_provenance_complete": 0,
        "child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
