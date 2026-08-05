#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

class CollisionSemanticObstructionError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise CollisionSemanticObstructionError(message)

def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    path = root / "data/prime_power_side_four_blocker_3210_collision_semantic_obstruction.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data.get("schema") == "prime-power-side-four-blocker-3210-collision-semantic-obstruction/v1", "schema")
    scope = data["scope"]
    require(scope["response"] == "3210", "response")
    require(scope["response_edges"] == ["03", "12", "21", "30"], "response edges")
    require(scope["collision_key"] == "02,20", "collision key")
    require(scope["deleted_edges"] == ["02", "20"], "deleted edges")
    require(set(scope["response_edges"]).isdisjoint(scope["deleted_edges"]), "response uses deleted edge")
    require(scope["target_edge"] not in scope["response_edges"], "response uses target edge")
    known = data["known_exact_facts"]
    for key in ("response_avoids_deleted_edges", "response_avoids_target_edge", "return_routing_complete", "collision_dependency_declared"):
        require(known.get(key) == 1, key)
    require(known.get("return_charge_22") == 1 and known.get("return_charge_33") == 3, "return charges")
    require(known.get("collision_category_status") == "unresolved-not-zero", "collision status")
    required = data["required_semantic_inputs"]
    names = [item["name"] for item in required]
    require(names == ["collision_event_domain", "physical_offspring_constructor", "collision_multiplicity_rule", "owner_fate_collision_key_constructor", "interface_provenance_constructor", "global_transition_occurrence_witness"], "semantic input list")
    require(all(item.get("status") == "missing" and item.get("purpose") for item in required), "missing semantic inputs")
    non_derivations = data["non_derivations"]
    require(len(non_derivations) == 5 and all(isinstance(item, str) and item for item in non_derivations), "non-derivations")
    result = data["result"]
    require(result.get("semantic_input_obstruction_complete") == 1, "obstruction completion")
    for key in ("physical_collision_offspring_enumerated", "collision_multiplicities_complete", "collision_child_keys_complete", "collision_coefficient_complete", "collision_child_weight_binding_complete", "global_transition_occurrence_complete", "collision_incompatibility_proved", "all_n_proved_by_checker"):
        require(result.get(key) == 0, key)
    print(json.dumps({"checker":"prime-power-side-four-blocker-3210-collision-semantic-obstruction","contract_sha256":digest(data),**result}, sort_keys=True))

if __name__ == "__main__": main()
