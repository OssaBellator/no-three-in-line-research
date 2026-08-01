#!/usr/bin/env python3
"""Run the extended installed prime-power construction checker stack.

The manifest contains the original fourteen installed checkers plus the
essential-return unit-wall, sparse rollback, and extended registry checkers.
A passing run validates only the installed finite claims and permanent honesty
flags; it does not prove global construction exhaustiveness or termination.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


class ExtendedConstructionRegressionError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ExtendedConstructionRegressionError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


EXPECTED_MANIFEST_SHA256 = "0595bf48a3cb786cc0e9e79f7534c4c0cf2f3161b072575aaae06976e6bc194a"
CHECKER_MANIFEST = [('scripts/check_prime_power_asymmetric_residual_host_contraction.py', 'fcc593f5812912d031ed90ab37e0fae105a35302a48b757f3fe69a7e80a0403b', 'asymmetric_residual_host_generated'), ('scripts/check_prime_power_asymmetric_context_generation.py', '8a12029b565cd8b9d51dba236f3cff782ed45ef3544fffd3ccddab8b0a32a0b9', 'asymmetric_context_family_generated'), ('scripts/check_prime_power_asymmetric_target_dispatch.py', '5e982b03f24ce4cd1230ede70563b49e3ac67976b0a84e038ae27b463e39fa83', 'local_asymmetric_candidate_response_complete'), ('scripts/check_prime_power_context_transition_registry.py', 'ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d', 'canonical_context_identity_sealed'), ('scripts/check_prime_power_routing_change_context_ancestry.py', 'b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360', 'routing_change_construction_ancestry_proved'), ('scripts/check_prime_power_routing_change_history_payment.py', 'b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259', 'routing_change_history_endpoint_exact'), ('scripts/check_prime_power_factor_child_product_ancestry.py', 'bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae', 'factor_product_construction_ancestry_proved'), ('scripts/check_prime_power_mixed_child_deletion_ancestry.py', 'b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429', 'mixed_atom_deletion_ancestry_proved'), ('scripts/check_prime_power_forced_certificate_escape_ancestry.py', 'dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253', 'forced_mixed_certificate_escape_proved'), ('scripts/check_prime_power_target_edge_return_ancestry.py', '04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382', 'returned_target_edge_ancestry_proved'), ('scripts/check_prime_power_target_handoff_envelope_ancestry.py', 'a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b', 'target_handoff_construction_ancestry_proved'), ('scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py', 'a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0', 'recurrent_target_edge_deletion_ancestry_proved'), ('scripts/check_prime_power_closure_envelope_transition_ancestry.py', '50b7720e03295dbde2557ab1d3a11dfc99a8f6d4a9528391555bc4e3adbf91c1', 'closure_branch_envelope_transition_bank_exhaustive'), ('scripts/check_prime_power_installed_owner_scheduler_bank.py', '108802c0d4934c7b3d77cc972d5418a2d8b91a6cca9da78b49bc4ab58970ad26', 'installed_transition_kind_bank_exhaustive'), ('scripts/check_prime_power_essential_return_unit_wall_ancestry.py', '97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5', 'essential_return_unit_wall_ancestry_proved'), ('scripts/check_prime_power_sparse_rollback_restoration_ancestry.py', '35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267', 'sparse_rollback_restoration_ancestry_proved'), ('scripts/check_prime_power_extended_installed_operation_registry.py', '4df61b20f4d3b2bad19a296a18e00f817ac1a20feda02b77f8486783bb561487', 'extended_installed_transition_kind_bank_exhaustive')]


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ExtendedConstructionRegressionError("unable to locate repository root")


def validate_manifest() -> None:
    require(digest(CHECKER_MANIFEST) == EXPECTED_MANIFEST_SHA256,
            "extended checker manifest digest mismatch")
    paths: set[str] = set()
    flags: set[str] = set()
    for i, item in enumerate(CHECKER_MANIFEST):
        require(isinstance(item, tuple) and len(item) == 3,
                f"manifest[{i}]: exact three-field tuple required")
        path, contract, flag = item
        require(path.startswith("scripts/check_prime_power_") and path.endswith(".py"),
                f"manifest[{i}]: checker path required")
        require(path not in paths, f"manifest[{i}]: duplicate path")
        paths.add(path)
        require(len(contract) == 64 and all(c in "0123456789abcdef" for c in contract),
                f"manifest[{i}]: lowercase SHA-256 required")
        require(flag and flag not in flags, f"manifest[{i}]: unique flag required")
        flags.add(flag)


def environment() -> dict[str, str]:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return env


def parse_report(stdout: str, path: str) -> dict[str, Any]:
    text = stdout.strip()
    require(bool(text), f"{path}: no stdout")
    try:
        report = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ExtendedConstructionRegressionError(
            f"{path}: stdout is not one JSON object: {exc}\n{text}"
        ) from exc
    require(isinstance(report, dict), f"{path}: JSON object required")
    return report


def reported_contract(report: dict[str, Any]) -> Any:
    if "contract_sha256" in report:
        return report["contract_sha256"]
    return report.get("contract_digest")


def audit_checker(root: Path, item: tuple[str, str, str],
                  execute: bool) -> dict[str, Any]:
    path, contract, flag = item
    checker = root / path
    require(checker.is_file(), f"{path}: checker missing")
    source = checker.read_text(encoding="utf-8")
    compile(source, str(checker), "exec")
    if not execute:
        return {"path": path, "contract": contract, "expected_flag": flag}
    completed = subprocess.run(
        [sys.executable, str(checker)],
        cwd=root,
        env=environment(),
        capture_output=True,
        text=True,
        check=False,
    )
    require(
        completed.returncode == 0,
        f"{path}: checker failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    report = parse_report(completed.stdout, path)
    require(reported_contract(report) == contract, f"{path}: contract mismatch")
    require(report.get(flag) == 1, f"{path}: expected {flag}=1")
    require(report.get("all_n_proved_by_checker") == 0,
            f"{path}: honesty flag must remain zero")
    return {
        "path": path,
        "contract": contract,
        "expected_flag": flag,
        "all_n_proved_by_checker": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-only", action="store_true")
    args = parser.parse_args()
    validate_manifest()
    root = repository_root()
    results = [
        audit_checker(root, item, execute=not args.static_only)
        for item in CHECKER_MANIFEST
    ]
    report = {
        "checker": "prime-power-extended-installed-construction-regression",
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "installed_checker_count": len(CHECKER_MANIFEST),
        "executed_checker_count": 0 if args.static_only else len(CHECKER_MANIFEST),
        "static_only": int(args.static_only),
        "results": results,
        "extended_installed_transition_regression_complete": 1,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
