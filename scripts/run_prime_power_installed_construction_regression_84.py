#!/usr/bin/env python3
"""Run the installed eighty-four-kind construction checker stack."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


class ConstructionRegression84Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ConstructionRegression84Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


BASE_MANIFEST_SHA256 = "ecc5043ee6e9c04901e4a1814ca0446b49c3a9c115bfbfd6ab196d02ea13150a"
BASE_MANIFEST_COUNT = 28
MANIFEST_EXTENSION = [
    (
        "scripts/check_prime_power_persistent_cross_selector_ancestry.py",
        "35bfc31201b5fffb46b37e9c36ffd4c1e9e01c6d1ccdb2b592818b9dc8bdcc80",
        "persistent_blocker_absorption_deficiency_ancestry_proved",
    ),
    (
        "scripts/check_prime_power_installed_operation_registry_84.py",
        "515aaa29fac034eb7f1f119040b60164a3de4ae128363e87a6b48d3f3962fbdd",
        "installed_transition_kind_bank_84_exhaustive",
    ),
]
EXPECTED_CHAINED_MANIFEST_SHA256 = "041abca9a30cad0f0b97a440b455df2fdbeb4501bac711c681f8f2f202ae0c49"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ConstructionRegression84Error("unable to locate repository root")


def load_base_runner(root: Path) -> Any:
    path = root / "scripts/run_prime_power_installed_construction_regression_66.py"
    require(path.is_file(), "base 66-kind runner missing")
    spec = importlib.util.spec_from_file_location("installed_regression_66", path)
    require(spec is not None and spec.loader is not None, "base runner import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.EXPECTED_MANIFEST_SHA256 == BASE_MANIFEST_SHA256, "base manifest seal")
    require(len(module.CHECKER_MANIFEST) == BASE_MANIFEST_COUNT, "base manifest count")
    require(module.digest(module.CHECKER_MANIFEST) == BASE_MANIFEST_SHA256,
            "base manifest content mismatch")
    return module


def validate_manifest(manifest: list[tuple[str, str, str]]) -> None:
    require(
        digest({
            "base_manifest_sha256": BASE_MANIFEST_SHA256,
            "extension": MANIFEST_EXTENSION,
        }) == EXPECTED_CHAINED_MANIFEST_SHA256,
        "chained manifest digest mismatch",
    )
    require(len(manifest) == BASE_MANIFEST_COUNT + len(MANIFEST_EXTENSION),
            "thirty-checker manifest required")
    paths: set[str] = set()
    flags: set[str] = set()
    for index, item in enumerate(manifest):
        require(isinstance(item, tuple) and len(item) == 3,
                f"manifest[{index}]: tuple required")
        path, contract, flag = item
        require(path.startswith("scripts/check_prime_power_") and path.endswith(".py"),
                f"manifest[{index}]: checker path required")
        require(path not in paths, f"manifest[{index}]: duplicate path")
        paths.add(path)
        require(len(contract) == 64 and all(c in "0123456789abcdef" for c in contract),
                f"manifest[{index}]: lowercase SHA-256 required")
        require(flag and flag not in flags, f"manifest[{index}]: unique theorem flag required")
        flags.add(flag)


def environment() -> dict[str, str]:
    result = dict(os.environ)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return result


def contract_from(report: dict[str, Any]) -> Any:
    return report.get("contract_sha256", report.get("contract_digest"))


def audit(root: Path, item: tuple[str, str, str], execute: bool) -> dict[str, Any]:
    path, contract, flag = item
    checker = root / path
    require(checker.is_file(), f"{path}: checker missing")
    compile(checker.read_text(encoding="utf-8"), str(checker), "exec")
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
        f"{path} failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    try:
        report = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise ConstructionRegression84Error(f"{path}: invalid JSON report") from exc
    require(isinstance(report, dict), f"{path}: JSON object required")
    require(contract_from(report) == contract, f"{path}: contract mismatch")
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
    root = repository_root()
    base = load_base_runner(root)
    manifest = [*base.CHECKER_MANIFEST, *MANIFEST_EXTENSION]
    validate_manifest(manifest)
    results = [audit(root, item, execute=not args.static_only) for item in manifest]
    report = {
        "checker": "prime-power-installed-construction-regression-84",
        "base_manifest_sha256": BASE_MANIFEST_SHA256,
        "manifest_extension": MANIFEST_EXTENSION,
        "chained_manifest_sha256": EXPECTED_CHAINED_MANIFEST_SHA256,
        "installed_checker_count": len(manifest),
        "executed_checker_count": 0 if args.static_only else len(manifest),
        "static_only": int(args.static_only),
        "results": results,
        "installed_transition_regression_84_complete": 1,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
