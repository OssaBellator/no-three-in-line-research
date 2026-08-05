#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

class CandidateError(RuntimeError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise CandidateError(message)

def repository_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in (current.parent, *current.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise CandidateError("repository root not found")

def contract_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()

def main() -> None:
    path = repository_root() / "data/prime_power_side_four_population_record_candidate.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data.get("schema") == "prime-power-side-four-population-record-candidate/v1", "schema")
    require(data.get("allowed_record_kinds") == ["parent", "child"], "record kinds")
    parents = data.get("target_parent_record_ids", [])
    children = data.get("target_child_classes", [])
    require(parents == ["zero_parent", "blocker_parent"], "parent targets")
    require(len(children) == 7 and len(set(children)) == 7, "child targets")
    require(sum(1 for item in children if item.startswith("return:00|rank1")) == 2, "split return-00 targets")

    candidate = data.get("candidate")
    admission = data.get("admission", {})
    if candidate is None:
        require(all(value == 0 for value in admission.values()), "empty candidate admission flags")
    else:
        require(isinstance(candidate, dict), "candidate object")
        kind = candidate.get("record_kind")
        require(kind in ("parent", "child"), "candidate kind")
        require(isinstance(candidate.get("exact_recurrent_state_key"), str) and candidate["exact_recurrent_state_key"].strip(), "state key")
        require(not candidate["exact_recurrent_state_key"].startswith("w_"), "alias state key")
        weight = candidate.get("installed_weight")
        require(isinstance(weight, int) and weight > 0, "positive integer installed weight")
        require(isinstance(candidate.get("transition_occurrence_provenance"), str) and candidate["transition_occurrence_provenance"].strip(), "transition provenance")
        require(isinstance(candidate.get("normalization"), dict) and candidate["normalization"], "normalization witness")
        require(isinstance(candidate.get("recurrent_block"), dict) and candidate["recurrent_block"], "recurrent block witness")
        if kind == "parent":
            require(candidate.get("record_id") in parents, "parent target")
            require(isinstance(candidate.get("parent_rule_provenance"), str) and candidate["parent_rule_provenance"].strip(), "parent-rule provenance")
        else:
            require(candidate.get("exact_child_class") in children, "child target")
            require("parent_rule_provenance" not in candidate, "child parent-rule field")

    completion = data.get("completion", {})
    require(completion.get("candidate_envelope_complete") == 1, "candidate envelope flag")
    for flag in (
        "first_manifest_record_populated",
        "binding_input_population_complete",
        "global_binding_constructed",
        "global_binding_incompatibility_proved",
        "all_n_proved_by_checker",
    ):
        require(completion.get(flag) == 0, flag)

    report = {
        "checker": "prime-power-side-four-population-record-candidate",
        "contract_sha256": contract_digest(data),
        "candidate_present": int(candidate is not None),
        "candidate_admissible_for_population_table": int(candidate is not None),
        "candidate_envelope_complete": 1,
        "first_manifest_record_populated": 0,
        "binding_input_population_complete": 0,
        "global_binding_constructed": 0,
        "global_binding_incompatibility_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()
