#!/usr/bin/env python3
"""Run the installed 221-kind construction and inherited-coverage checker stack."""
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


class ConstructionRegression221Error(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ConstructionRegression221Error(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


BASE_CHAINED_MANIFEST_SHA256 = "7ac023aecd548ee7c966e8934b149d551a57a30e5569094abd6b26cf8bd29de1"
BASE_MANIFEST_COUNT = 39
MANIFEST_EXTENSION = [
    (
        "scripts/check_prime_power_target_anchor_lineage_ancestry.py",
        "2f846aa50012d196dffc90511de0c254782b1a5696b1cb25ee1cf1b73a990359",
        "target_anchor_lineage_ancestry_proved",
    ),
    (
        "scripts/check_prime_power_installed_operation_registry_221.py",
        "939ca5627499348fb52e9153a56e0b31697c2f9f00ad8e0dcb7fba4e7bb10e4c",
        "installed_transition_kind_bank_221_exhaustive",
    ),
]
EXPECTED_CHAINED_MANIFEST_SHA256 = "5955b80f71ffdf8d2cd9ca1149d346779787521137353b4457bf35096f570f38"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ConstructionRegression221Error("unable to locate repository root")


def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path.name}: missing")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{path.name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_base_manifest(root: Path) -> list[tuple[str, str, str]]:
    runner = load_module(
        root / "scripts/run_prime_power_installed_construction_regression_188_coverage.py",
        "installed_regression_188_coverage",
    )
    require(runner.EXPECTED_CHAINED_MANIFEST_SHA256 == BASE_CHAINED_MANIFEST_SHA256,
            "base 188-coverage chained seal")
    manifest = [*runner.load_base_manifest(root), *runner.MANIFEST_EXTENSION]
    runner.validate_manifest(manifest)
    require(len(manifest) == BASE_MANIFEST_COUNT, "base thirty-nine-checker count")
    return manifest


def validate_manifest(manifest: list[tuple[str, str, str]]) -> None:
    require(
        digest({
            "base_chained_manifest_sha256": BASE_CHAINED_MANIFEST_SHA256,
            "extension": MANIFEST_EXTENSION,
        }) == EXPECTED_CHAINED_MANIFEST_SHA256,
        "chained manifest digest mismatch",
    )
    require(len(manifest) == BASE_MANIFEST_COUNT + len(MANIFEST_EXTENSION),
            "forty-one-checker manifest required")
    paths: set[str] = set()
    flags: set[str] = set()
    for index, item in enumerate(manifest):
        require(isinstance(item, tuple) and len(item) == 3,
                f"manifest[{index}]: tuple required")
        path, contract, flag = item
        require(path.startswith("scripts/check_prime_power_") and path.endswith(".py"),
                f"manifest[{index}]: checker path")
        require(path not in paths, f"manifest[{index}]: duplicate path")
        paths.add(path)
        require(len(contract) == 64 and all(char in "0123456789abcdef" for char in contract),
                f"manifest[{index}]: contract")
        require(flag and flag not in flags, f"manifest[{index}]: theorem flag")
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
        [sys.executable, str(checker)], cwd=root, env=environment(),
        capture_output=True, text=True, check=False,
    )
    require(completed.returncode == 0,
            f"{path} failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    try:
        report = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise ConstructionRegression221Error(f"{path}: invalid JSON report") from exc
    require(isinstance(report, dict), f"{path}: JSON object required")
    require(contract_from(report) == contract, f"{path}: contract mismatch")
    require(report.get(flag) == 1, f"{path}: expected {flag}=1")
    require(report.get("all_n_proved_by_checker") == 0,
            f"{path}: honesty flag must remain zero")
    return {"path": path, "contract": contract, "expected_flag": flag,
            "all_n_proved_by_checker": 0}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-only", action="store_true")
    args = parser.parse_args()
    root = repository_root()
    manifest = [*load_base_manifest(root), *MANIFEST_EXTENSION]
    validate_manifest(manifest)
    results = [audit(root, item, execute=not args.static_only) for item in manifest]
    report = {
        "checker": "prime-power-installed-construction-regression-221",
        "base_chained_manifest_sha256": BASE_CHAINED_MANIFEST_SHA256,
        "manifest_extension": MANIFEST_EXTENSION,
        "chained_manifest_sha256": EXPECTED_CHAINED_MANIFEST_SHA256,
        "installed_checker_count": len(manifest),
        "executed_checker_count": 0 if args.static_only else len(manifest),
        "static_only": int(args.static_only),
        "results": results,
        "installed_transition_regression_221_complete": 1,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
