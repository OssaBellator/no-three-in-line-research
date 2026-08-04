#!/usr/bin/env python3
"""Validate the symbolic-line refinement of the side-four dependency map."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from pathlib import Path
from typing import Any

class LineDependencyRefinementError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise LineDependencyRefinementError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

DEPENDENCY_CHECKER_PATH = "scripts/check_prime_power_side_four_compulsory_coefficient_dependency_map.py"
DEPENDENCY_CONTRACT_PATH = "data/prime_power_side_four_compulsory_coefficient_dependency_contract.json"
LINE_CHECKER_PATH = "scripts/check_prime_power_side_four_symbolic_line_kernel_context.py"
LINE_CONTRACT_PATH = "data/prime_power_side_four_symbolic_line_kernel_context_contract.json"
REFINEMENT_PATH = "data/prime_power_side_four_coefficient_dependency_line_refinement.json"
EXPECTED_DEPENDENCY_CONTRACT_SHA256 = "47c765be4b4a79f826dba2ac23fb2d7a69f0d64ba23bb94d1cb1d608178fbacc"
EXPECTED_DEPENDENCY_RECORD_SHA256 = "4cd91e195393ea226474c3c33f80ac63fcdd9c4b8b0bf95b810f54d0c490d401"
EXPECTED_LINE_CONTRACT_SHA256 = "0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e"
EXPECTED_REFINEMENT_SHA256 = "b836ada7de6f0af399bd1999b5f2cc533eb02b4ccd7b4c9308fce57924f2728b"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise LineDependencyRefinementError("unable to locate repository root")

def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: checker missing")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def expected_refinement() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-coefficient-dependency-line-refinement/v1",
        "base_dependency_contract_sha256": EXPECTED_DEPENDENCY_CONTRACT_SHA256,
        "base_dependency_record_sha256": EXPECTED_DEPENDENCY_RECORD_SHA256,
        "symbolic_line_contract_sha256": EXPECTED_LINE_CONTRACT_SHA256,
        "refinement": {
            "category": "line",
            "newly_available_input": "line_coefficient_rule",
            "rule": "K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)",
            "refined_records": 86,
            "known_input_occurrence_delta": 86,
            "missing_input_occurrence_delta": -86,
            "remaining_line_missing_inputs": ["background_height_profile", "line_owner_labels"],
        },
        "aggregate": {
            "records": 516,
            "coefficient_known_records": 86,
            "coefficient_unresolved_records": 430,
            "known_input_occurrences": 774,
            "missing_input_occurrences": 1376,
            "partially_grounded_records": 430,
            "coefficient_known_binding_unresolved_records": 86,
            "line_category": {
                "records": 86,
                "known_coefficients": 0,
                "unresolved_coefficients": 86,
                "known_input_occurrences": 172,
                "missing_input_occurrences": 172,
                "dependency_status": "partially-grounded",
            },
        },
        "honesty": {
            "line_dependency_refinement_complete_for_normalized_block": 1,
            "actual_background_height_profiles_complete": 0,
            "line_owner_labels_complete": 0,
            "numeric_rank_one_rank_two_line_coefficients_complete": 0,
            "unresolved_coefficients_populated": 0,
            "global_child_provenance_complete": 0,
            "child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def validate(root: Path, refinement: dict[str, Any]) -> None:
    dependency = load_module(root / DEPENDENCY_CHECKER_PATH, "side_four_dependency_checker")
    line = load_module(root / LINE_CHECKER_PATH, "side_four_line_checker")
    require(dependency.EXPECTED_DEPENDENCY_CONTRACT_SHA256 == EXPECTED_DEPENDENCY_CONTRACT_SHA256, "dependency contract binding")
    require(dependency.EXPECTED_DEPENDENCY_RECORD_SHA256 == EXPECTED_DEPENDENCY_RECORD_SHA256, "dependency record binding")
    require(line.EXPECTED_CONTRACT_SHA256 == EXPECTED_LINE_CONTRACT_SHA256, "symbolic line contract binding")
    dependency_contract = json.loads((root / DEPENDENCY_CONTRACT_PATH).read_text(encoding="utf-8"))
    line_contract = json.loads((root / LINE_CONTRACT_PATH).read_text(encoding="utf-8"))
    records = dependency.validate(root, dependency_contract)
    line.validate(root, line_contract)
    require(refinement == expected_refinement(), "line refinement differs from canonical schema")
    require(digest(refinement) == EXPECTED_REFINEMENT_SHA256, "line refinement digest mismatch")
    line_records = [record for record in records if record["category"] == "line"]
    require(len(line_records) == 86, "base line record count")
    require(all("line_coefficient_rule" in record["missing_inputs"] for record in line_records), "base line rule must be missing")
    require(all("selected_response_line_signature" in record["known_inputs"] for record in line_records), "base line signature must be known")
    base_known = sum(len(record["known_inputs"]) for record in records)
    base_missing = sum(len(record["missing_inputs"]) for record in records)
    require((base_known, base_missing) == (688, 1462), "base dependency occurrence census")
    require(base_known + 86 == refinement["aggregate"]["known_input_occurrences"], "refined known occurrence total")
    require(base_missing - 86 == refinement["aggregate"]["missing_input_occurrences"], "refined missing occurrence total")

def mutation_audit(root: Path, refinement: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(known_input_occurrences=773),
        lambda item: item["aggregate"].update(missing_input_occurrences=1375),
        lambda item: item["refinement"].update(refined_records=85),
        lambda item: item["refinement"].update(known_input_occurrence_delta=85),
        lambda item: item["refinement"].update(missing_input_occurrence_delta=-85),
        lambda item: item["refinement"].update(rule="rank three only"),
        lambda item: item["refinement"]["remaining_line_missing_inputs"].pop(),
        lambda item: item.update(symbolic_line_contract_sha256="0" * 64),
        lambda item: item["honesty"].update(actual_background_height_profiles_complete=1),
        lambda item: item["honesty"].update(numeric_rank_one_rank_two_line_coefficients_complete=1),
        lambda item: item["honesty"].update(unresolved_coefficients_populated=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(refinement)
        mutate(bad)
        try:
            validate(root, bad)
        except LineDependencyRefinementError:
            rejected += 1
    require(rejected == len(mutations), "line refinement corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    refinement = json.loads((root / REFINEMENT_PATH).read_text(encoding="utf-8"))
    validate(root, refinement)
    print(json.dumps({
        "checker": "prime-power-side-four-coefficient-dependency-line-refinement",
        "base_dependency_contract_sha256": EXPECTED_DEPENDENCY_CONTRACT_SHA256,
        "base_dependency_record_sha256": EXPECTED_DEPENDENCY_RECORD_SHA256,
        "symbolic_line_contract_sha256": EXPECTED_LINE_CONTRACT_SHA256,
        "line_refinement_sha256": EXPECTED_REFINEMENT_SHA256,
        "refined_record_count": 86,
        "known_input_occurrence_count": 774,
        "missing_input_occurrence_count": 1376,
        "rejected_corruptions": mutation_audit(root, refinement),
        "side_four_coefficient_dependency_line_refinement_complete": 1,
        "line_dependency_refinement_complete_for_normalized_block": 1,
        "actual_background_height_profiles_complete": 0,
        "line_owner_labels_complete": 0,
        "numeric_rank_one_rank_two_line_coefficients_complete": 0,
        "unresolved_coefficients_populated": 0,
        "global_child_provenance_complete": 0,
        "child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
