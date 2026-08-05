#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Any

class SourceCoverageError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise SourceCoverageError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def repository_root() -> Path:
    current = Path(__file__).resolve().parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir(): return candidate
    raise SourceCoverageError("unable to locate repository root")

def main() -> None:
    root = repository_root()
    path = root / "data/prime_power_side_four_joint_binding_source_coverage_contract.json"
    contract = json.loads(path.read_text(encoding="utf-8"))
    require(contract.get("schema") == "prime-power-side-four-joint-binding-source-coverage/v1", "schema")
    sources = contract.get("candidate_installed_sources")
    require(isinstance(sources, list) and len(sources) == 9, "nine candidate sources")
    required = ("provides_exact_recurrent_state_key", "provides_installed_weight", "provides_transition_occurrence_provenance", "provides_parent_rule_provenance")
    qualifying = 0
    for index, source in enumerate(sources):
        require((root / source["path"]).is_file(), f"candidate[{index}] missing")
        require(source.get("provides_format_or_local_structure") is True, f"candidate[{index}] local structure")
        require(all(source.get(key) is False for key in required), f"candidate[{index}] unsupported population claim")
        qualifying += int(all(source.get(key) is True for key in required))
    boundary = contract.get("installed_boundary", {})
    require((root / boundary.get("checker", "")).is_file(), "installed boundary checker")
    for key in ("owner_fate_rows_populated_all_recurrent_states", "compulsory_weighted_certificates_complete", "actual_global_parent_rule_complete"):
        require(boundary.get(key) == 0, f"boundary honesty {key}")
    result = contract.get("coverage_result", {})
    require(result.get("candidate_source_count") == 9, "candidate count")
    require(result.get("qualifying_population_source_count") == qualifying == 0, "qualifying count")
    require(result.get("first_manifest_record_populated") is False, "population honesty")
    require(result.get("source_coverage_audit_complete") is True, "audit complete")
    for key in ("binding_input_population_complete", "global_binding_constructed", "global_binding_incompatibility_proved"):
        require(result.get(key) is False, f"honesty {key}")
    require(result.get("all_n_proved_by_checker") == 0, "all-n honesty")
    print(json.dumps({"checker":"prime-power-side-four-joint-binding-source-coverage","contract_sha256":digest(contract),**result}, sort_keys=True))

if __name__ == "__main__": main()
