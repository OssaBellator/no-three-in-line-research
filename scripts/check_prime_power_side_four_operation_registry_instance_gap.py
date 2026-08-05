#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

class RegistryInstanceGapError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise RegistryInstanceGapError(message)

def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file(): return candidate
    raise RegistryInstanceGapError("repository root not found")

def main() -> None:
    repo = root()
    contract = json.loads((repo / "data/prime_power_side_four_operation_registry_instance_gap_contract.json").read_text())
    require(digest(contract) == "983be0d89991979213c6bd4ddad8b10de04a77f40386c20cd8553068749cae3f", "contract digest")
    registry = (repo / contract["registry_checker"]).read_text()
    for field in contract["registry_fields"]:
        require(field in registry, f"registry field missing: {field}")
    for field in contract["required_population_fields"]:
        require(field not in contract["registry_fields"], f"population field incorrectly registered: {field}")
    require(contract["parent_additional_field"] not in contract["registry_fields"], "parent provenance incorrectly registered")
    require(contract["installed_operation_kind_count"] == 1166, "operation count")
    require(contract["new_owner_fate_operation_kind_count"] == 72, "new operation count")
    require(contract["instance_population_fields_present"] == 0, "instance fields must remain absent")
    honesty = contract["honesty"]
    require(honesty["registry_instance_gap_checked"] == 1, "gap flag")
    for key in ("first_manifest_record_populated", "binding_input_population_complete", "global_binding_constructed", "global_binding_incompatibility_proved", "all_n_proved_by_checker"):
        require(honesty[key] == 0, f"honesty flag {key}")
    print(json.dumps({"checker":"prime-power-side-four-operation-registry-instance-gap","contract_sha256":digest(contract),**honesty}, sort_keys=True))

if __name__ == "__main__": main()
