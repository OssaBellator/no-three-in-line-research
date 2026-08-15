#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Any

EXPECTED_SHA256 = "897e31816869208ea1d1ff82920d6dabfff0d61a689fff3fc20e4eba06eca457"
TABLE = "data/prime_power_side_four_recurrent_state_population_table.json"
ALIASES = {
    "w_return_00_rank1", "w_return_22_rank1", "w_return_22_rank2",
    "w_return_11_rank1", "w_return_11_rank2", "w_return_33_rank3"
}

class PopulationTableError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise PopulationTableError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def root() -> Path:
    for candidate in (Path(__file__).resolve().parent, *Path(__file__).resolve().parents):
        if (candidate / "STATUS.md").is_file(): return candidate
    raise PopulationTableError("repository root not found")

def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def validate_record(record: dict[str, Any], required: list[str], kind: str) -> None:
    require(set(required) <= set(record), f"{kind}: missing required field")
    require(nonempty(record["record_id"]), f"{kind}: record id")
    require(nonempty(record["sample_scope"]), f"{kind}: sample scope")
    key = record["exact_recurrent_state_key"]
    require(nonempty(key) and key not in ALIASES, f"{kind}: exact recurrent state key")
    weight = record["installed_weight"]
    require(isinstance(weight, (int, float)) and not isinstance(weight, bool) and weight > 0, f"{kind}: positive installed weight")
    require(nonempty(record["transition_occurrence_provenance"]), f"{kind}: transition provenance")
    require(nonempty(record["recurrent_block_id"]), f"{kind}: recurrent block")
    require(nonempty(record["normalization_id"]), f"{kind}: normalization")
    if kind == "parent": require(nonempty(record["parent_rule_provenance"]), "parent: rule provenance")
    if kind == "child": require(nonempty(record["exact_child_class"]), "child: exact child class")

def main() -> None:
    table = json.loads((root() / TABLE).read_text())
    require(digest(table) == EXPECTED_SHA256, "population table digest mismatch")
    require(table["schema"] == "prime-power-side-four-recurrent-state-population-table/v1", "schema")
    require(table["target_parent_records"] == ["zero_parent", "blocker_parent"], "parent targets")
    children = table["target_child_classes"]
    require(len(children) == 7 and len(set(children)) == 7, "seven exact child targets")
    require(children[0] != children[3], "return-00 exact classes must remain split")
    parents = table["population"]["parents"]
    child_records = table["population"]["children"]
    for record in parents: validate_record(record, table["required_record_kinds"]["parent"], "parent")
    for record in child_records: validate_record(record, table["required_record_kinds"]["child"], "child")
    require(len({r["record_id"] for r in parents}) == len(parents), "duplicate parent record")
    require(len({r["exact_child_class"] for r in child_records}) == len(child_records), "duplicate child class")
    completion = table["completion"]
    require(completion["population_table_schema_complete"] == 1, "schema complete")
    require(completion["parent_records_populated"] == len(parents), "parent count")
    require(completion["child_records_populated"] == len(child_records), "child count")
    first = int(bool(parents or child_records))
    require(completion["first_manifest_record_populated"] == first, "first record flag")
    complete = int(len(parents) == 2 and len(child_records) == 7 and bool(table["global_records"]["normalizations"]) and bool(table["global_records"]["recurrent_blocks"]))
    require(completion["binding_input_population_complete"] == complete, "population completion flag")
    require(completion["global_binding_constructed"] == 0, "no constructed binding")
    require(completion["global_binding_incompatibility_proved"] == 0, "no incompatibility")
    require(completion["all_n_proved_by_checker"] == 0, "honesty")
    print(json.dumps({
        "checker": "prime-power-side-four-recurrent-state-population-table",
        "contract_sha256": EXPECTED_SHA256,
        "target_parent_count": 2,
        "target_child_count": 7,
        "parent_records_populated": len(parents),
        "child_records_populated": len(child_records),
        "population_table_schema_complete": 1,
        "first_manifest_record_populated": first,
        "binding_input_population_complete": complete,
        "global_binding_constructed": 0,
        "global_binding_incompatibility_proved": 0,
        "all_n_proved_by_checker": 0
    }, sort_keys=True))

if __name__ == "__main__": main()
