#!/usr/bin/env python3
"""Check the side-four joint global state/weight binding attempt."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

EXPECTED_CONTRACT_SHA256 = "787039d4458fe2e5ee1400e76815cee6dc8b4425d04436453083a91ce7d9f077"

class BindingAttemptError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise BindingAttemptError(message)

def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()

def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise BindingAttemptError("repository root not found")

def main() -> None:
    repo = root()
    contract = json.loads((repo / "data/prime_power_side_four_joint_global_binding_attempt_contract.json").read_text())
    require(canonical_digest(contract) == EXPECTED_CONTRACT_SHA256, "contract digest")
    joint = json.loads((repo / contract["inputs"]["joint_contract"]).read_text())
    owner_source = (repo / contract["inputs"]["owner_fate_checker"]).read_text()

    require(joint["aggregate"]["sample_rows"] == 2, "two sample rows")
    require(joint["aggregate"]["exact_child_classes"] == 7, "seven exact child classes")
    require(len(joint["class_bindings"]) == 7, "seven class bindings")
    require(len({row["class_id"] for row in joint["class_bindings"]}) == 7, "distinct exact classes")
    require(len(joint["explicit_joint_local_witness"]["parent_weights"]) == 2, "two local parent weights")
    require(len(joint["explicit_joint_local_witness"]["child_weights"]) == 7, "seven local child weights")
    require(all(row["status"] == "unresolved" for row in joint["residual_bindings"]), "joint residuals remain unresolved")

    for literal in (
        '"owner_fate_rows_populated_all_recurrent_states":0',
        '"compulsory_weighted_certificates_complete":0',
        '"actual_global_parent_rule_complete":0',
    ):
        require(literal in owner_source, f"missing ancestry honesty literal {literal}")

    attempt = contract["attempt"]
    require(attempt["parent_state_keys_requested"] == 2, "parent request count")
    require(attempt["exact_child_classes_requested"] == 7, "child request count")
    require(attempt["global_weight_bindings_requested"] == 9, "weight request count")
    require(attempt["result"] == "underdetermined", "attempt result")
    require(contract["honesty"] == {
        "all_n_proved_by_checker": 0,
        "checked_global_binding_attempt_complete": 1,
        "global_binding_constructed": 0,
        "global_binding_incompatibility_proved": 0,
        "joint_sample_global_recurrent_compatibility_proved": 0,
        "joint_sample_global_weight_bindings_complete": 0,
    }, "honesty block")

    print(json.dumps({
        "checker": "prime-power-side-four-joint-global-binding-attempt",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        "sample_rows": 2,
        "exact_child_classes": 7,
        "requested_global_weight_bindings": 9,
        "binding_attempt_result": "underdetermined",
        **contract["honesty"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
