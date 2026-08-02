#!/usr/bin/env python3
"""Execute signature, displacement, carry and resource ancestry for CMR1454--CMR1509."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class SignatureCarryResourceError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise SignatureCarryResourceError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SOURCE_FILES = [
    "docs/285-prime-power-eligible-owner-signature-fans.md",
    "docs/286-prime-power-fractional-packed-signature-fans.md",
    "docs/287-prime-power-weighted-displacement-carry-routing.md",
    "docs/288-prime-power-exact-displacement-private-path-payment.md",
    "docs/289-prime-power-transfer-resource-triangularity.md",
    "docs/290-prime-power-root-displacement-child-channels.md",
    "docs/291-prime-power-owner-disjoint-packed-loaded.md",
]
VERIFIER_FILES = [
    "scripts/verify_prime_power_eligible_owner_signature_fans.py",
    "scripts/verify_prime_power_fractional_packed_signature_fans.py",
    "scripts/verify_prime_power_weighted_displacement_carry_routing.py",
    "scripts/verify_prime_power_exact_displacement_path_tokens.py",
    "scripts/verify_prime_power_transfer_resource_triangularity.py",
    "scripts/verify_prime_power_root_displacement_child_channels.py",
    "scripts/verify_prime_power_owner_disjoint_packed_loaded.py",
]
CONTRACT = {
    "schema": "prime-power-signature-carry-resource-ancestry/v1",
    "source_range": ["CMR1454", "CMR1509"],
    "source_files": SOURCE_FILES,
    "verifier_files": VERIFIER_FILES,
    "checked_layers": [
        "eligible owner-pair filtering and finite prime-power signature fans",
        "fractional candidate-packing concentration into exact-displacement translate banks",
        "weighted prefix-cell internal, crossing and depth-zero carry routing",
        "translation path-forest extraction and private blocker/token payment",
        "monotone residual-edge and absolute-token resource triangularity",
        "depth-zero root residue channels, quotient carries and strict child normalization",
        "owner-disjoint packed versus loaded payment bookkeeping",
    ],
    "honesty_flags": {
        "uniform_signature_payment_certificate_proved": 0,
        "recurrent_root_channel_core_subcritical": 0,
        "repeated_token_reused_edge_core_subcritical": 0,
        "loaded_owner_core_subcritical": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "e1a59036d2e0bdfacab901cb75f44aaf01f3a03c3f8c2e44f1f4466326d717fc"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file(): current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir(): return candidate
    raise SignatureCarryResourceError("unable to locate repository root")

def environment() -> dict[str, str]:
    result = dict(os.environ)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return result

def execute_verifier(root: Path, relative_path: str) -> dict[str, Any]:
    path = root / relative_path
    require(path.is_file(), f"{relative_path}: missing verifier")
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
    completed = subprocess.run([sys.executable, str(path)], cwd=root, env=environment(), capture_output=True, text=True, check=False)
    require(completed.returncode == 0, f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output = completed.stdout.strip()
    require(output.startswith("verified "), f"{relative_path}: missing verified report")
    return {"path": relative_path, "stdout_sha256": hashlib.sha256(output.encode()).hexdigest(), "stdout": output}

def validate_fixture(fixture: dict[str, Any]) -> None:
    require(fixture.get("source_file_count") == 7, "fixture source count")
    require(fixture.get("verifier_file_count") == 7, "fixture verifier count")
    require(fixture.get("eligible_owner_signature_fans_exact") == 1, "fixture signatures")
    require(fixture.get("fractional_packed_signature_fans_exact") == 1, "fixture packing")
    require(fixture.get("weighted_displacement_carry_routing_exact") == 1, "fixture routing")
    require(fixture.get("private_path_payment_exact") == 1, "fixture private path")
    require(fixture.get("transfer_resource_dag_exact") == 1, "fixture transfer DAG")
    require(fixture.get("root_child_channels_exact") == 1, "fixture root channels")
    require(fixture.get("owner_disjoint_packed_loaded_exact") == 1, "fixture disjointness")
    require(fixture.get("uniform_signature_payment_certificate_proved") == 0, "fixture payment honesty")
    require(fixture.get("same_owner_diagonal_blocks_subcritical") == 0, "fixture subcritical honesty")
    require(fixture.get("all_n_proved_by_checker") == 0, "fixture all-n honesty")

def mutation_audit() -> int:
    fixture = {
        "source_file_count": 7,
        "verifier_file_count": 7,
        "eligible_owner_signature_fans_exact": 1,
        "fractional_packed_signature_fans_exact": 1,
        "weighted_displacement_carry_routing_exact": 1,
        "private_path_payment_exact": 1,
        "transfer_resource_dag_exact": 1,
        "root_child_channels_exact": 1,
        "owner_disjoint_packed_loaded_exact": 1,
        "uniform_signature_payment_certificate_proved": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(source_file_count=6),
        lambda item: item.update(verifier_file_count=6),
        lambda item: item.update(eligible_owner_signature_fans_exact=0),
        lambda item: item.update(fractional_packed_signature_fans_exact=0),
        lambda item: item.update(weighted_displacement_carry_routing_exact=0),
        lambda item: item.update(private_path_payment_exact=0),
        lambda item: item.update(transfer_resource_dag_exact=0),
        lambda item: item.update(root_child_channels_exact=0),
        lambda item: item.update(owner_disjoint_packed_loaded_exact=0),
        lambda item: item.update(uniform_signature_payment_certificate_proved=1),
        lambda item: item.update(same_owner_diagonal_blocks_subcritical=1),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try: validate_fixture(bad)
        except SignatureCarryResourceError: rejected += 1
    require(rejected == len(mutations), "signature/carry corruption accepted")
    return rejected

def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    root = repository_root()
    for source in SOURCE_FILES: require((root / source).is_file(), f"{source}: missing source")
    reports = [execute_verifier(root, path) for path in VERIFIER_FILES]
    print(json.dumps({
        "checker": "prime-power-signature-carry-resource-ancestry",
        "contract_sha256": contract,
        "source_file_count": len(SOURCE_FILES),
        "verifier_file_count": len(VERIFIER_FILES),
        "verifier_reports": reports,
        "rejected_corruptions": mutation_audit(),
        "eligible_owner_signature_fans_exact": 1,
        "fractional_packed_signature_fans_exact": 1,
        "weighted_displacement_carry_routing_exact": 1,
        "private_path_payment_exact": 1,
        "transfer_resource_dag_exact": 1,
        "root_child_channels_exact": 1,
        "owner_disjoint_packed_loaded_exact": 1,
        "signature_carry_resource_ancestry_proved": 1,
        "uniform_signature_payment_certificate_proved": 0,
        "recurrent_root_channel_core_subcritical": 0,
        "repeated_token_reused_edge_core_subcritical": 0,
        "loaded_owner_core_subcritical": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "global_target_collateral_inequality_proved": 0,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__": main()
