#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Any

class BindingInputManifestError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise BindingInputManifestError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

EXPECTED_CONTRACT_SHA256 = "743e049de6211b8333fcb2f85e03d9deb2204715a35d2e3a0a50423902edd870"
EXPECTED_SYMBOLS = [
    "w_zero_return_00_rank1",
    "w_zero_return_22_rank1",
    "w_zero_return_22_rank2",
    "w_blocker_return_00_rank1",
    "w_blocker_return_11_rank1",
    "w_blocker_return_11_rank2",
    "w_blocker_return_33_rank3",
]
EXPECTED_PARENT_FIELDS = [
    "exact_recurrent_state_key",
    "installed_parent_weight",
    "transition_occurrence_provenance",
    "parent_rule_provenance",
]
EXPECTED_CHILD_FIELDS = [
    "exact_recurrent_state_key",
    "installed_child_weight",
    "transition_occurrence_provenance",
]
EXPECTED_ROW_FIELDS = [
    "selector_terms", "collision_terms", "interface_terms", "local_line_terms",
    "geometric_terms", "inner_duals", "outer_dual", "positive_slack",
]

def repository_root() -> Path:
    for candidate in (Path(__file__).resolve().parent, *Path(__file__).resolve().parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise BindingInputManifestError("unable to locate repository root")

def main() -> None:
    path = repository_root() / "data/prime_power_side_four_joint_global_binding_input_manifest.json"
    contract = json.loads(path.read_text(encoding="utf-8"))
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    require(contract.get("schema") == "prime-power-side-four-joint-global-binding-input-manifest/v1", "schema")
    require(contract.get("sample_rows") == ["zero", "blocker"], "sample rows")
    parents = contract.get("required_parent_records")
    require(isinstance(parents, list) and len(parents) == 2, "two parent records required")
    require([row.get("scope") for row in parents] == ["zero", "blocker"], "parent scopes")
    for row in parents:
        require(row.get("fields") == EXPECTED_PARENT_FIELDS, f"{row.get('scope')}: parent fields")
    children = contract.get("required_child_records")
    require(isinstance(children, list) and len(children) == 7, "seven exact child records required")
    require([row.get("joint_symbol") for row in children] == EXPECTED_SYMBOLS, "exact child symbols")
    require(len({row.get("class_id") for row in children}) == 7, "exact child classes must remain distinct")
    require(contract.get("required_child_fields") == EXPECTED_CHILD_FIELDS, "child fields")
    for scope in ("zero", "blocker"):
        require(contract.get("required_row_completion_records", {}).get(scope) == EXPECTED_ROW_FIELDS, f"{scope}: complete row fields")
    population = contract.get("current_population", {})
    for key in ("parent_records_populated", "child_records_populated", "global_records_populated", "complete_rows_populated"):
        require(population.get(key) == 0, f"population honesty: {key}")
    honesty = contract.get("honesty", {})
    require(honesty.get("binding_input_manifest_complete") == 1, "manifest completion flag")
    for key in ("binding_input_population_complete", "global_binding_constructed", "global_binding_incompatibility_proved", "joint_sample_global_recurrent_compatibility_proved", "all_n_proved_by_checker"):
        require(honesty.get(key) == 0, f"honesty: {key}")
    print(json.dumps({
        "checker": "prime-power-side-four-joint-global-binding-input-manifest",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        "required_parent_record_count": 2,
        "required_child_record_count": 7,
        "required_global_record_count": 3,
        "required_complete_row_count": 2,
        **honesty,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
