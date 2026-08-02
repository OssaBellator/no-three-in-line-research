#!/usr/bin/env python3
"""Execute labelled recurrent certificate ancestry for CMR1582--CMR1629."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

class LabelledRecurrentCertificateError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise LabelledRecurrentCertificateError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SOURCE_FILES = ['docs/301-prime-power-return-selector-assignment-scalarization.md', 'docs/302-prime-power-line-clean-integer-credit-budgets.md', 'docs/303-prime-power-critical-selector-profile-localization.md', 'docs/304-prime-field-root-channel-support-splice.md', 'docs/305-prime-power-fixed-interface-thin-exact-table.md', 'docs/306-prime-power-label-preserving-crt-certificate-assembly.md']
VERIFIER_FILES = ['scripts/verify_prime_power_return_selector_assignment.py', 'scripts/verify_prime_power_line_clean_integer_budgets.py', 'scripts/verify_prime_power_critical_selector_localization.py', 'scripts/verify_prime_field_root_channel_support_splice.py', 'scripts/verify_prime_power_fixed_interface_thin_table.py', 'scripts/verify_prime_power_label_preserving_crt_assembly.py']
CONTRACT = {'schema': 'prime-power-labelled-recurrent-certificate-ancestry/v1', 'source_range': ['CMR1582', 'CMR1629'], 'source_files': ['docs/301-prime-power-return-selector-assignment-scalarization.md', 'docs/302-prime-power-line-clean-integer-credit-budgets.md', 'docs/303-prime-power-critical-selector-profile-localization.md', 'docs/304-prime-field-root-channel-support-splice.md', 'docs/305-prime-power-fixed-interface-thin-exact-table.md', 'docs/306-prime-power-label-preserving-crt-certificate-assembly.md'], 'verifier_files': ['scripts/verify_prime_power_return_selector_assignment.py', 'scripts/verify_prime_power_line_clean_integer_budgets.py', 'scripts/verify_prime_power_critical_selector_localization.py', 'scripts/verify_prime_field_root_channel_support_splice.py', 'scripts/verify_prime_power_fixed_interface_thin_table.py', 'scripts/verify_prime_power_label_preserving_crt_assembly.py'], 'checked_layers': ['shared return-selector assignment scalarization and strict integer dual certificates', 'exact strong, singleton and overlap line-clean integer credit budgets', 'finite critical-selector rank/profile/geometric localization', 'prime-field root-channel singleton support and fixed-interface splice', 'finite exact fixed-interface and thin-board rational row tables', 'label-preserving SCC reduction and constructive CRT certificate gluing'], 'honesty_flags': {'return_selector_assignment_certificate_complete': 0, 'line_clean_integer_budgets_positive_all_classes': 0, 'critical_selector_classes_certified': 0, 'required_thin_tables_executed_and_certified': 0, 'all_labelled_recurrent_blocks_subcritical': 0, 'same_owner_diagonal_blocks_subcritical': 0, 'global_target_collateral_inequality_proved': 0, 'global_transition_kind_bank_exhaustive': 0, 'global_termination_proved': 0, 'actual_global_parent_rule_complete': 0, 'all_n_proved_by_checker': 0}}
EXPECTED_CONTRACT_SHA256 = "9bac28f07137a18a997239686785729530c242bae0f4ca551bdddb8974d971a6"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise LabelledRecurrentCertificateError("unable to locate repository root")

def environment() -> dict[str, str]:
    result = dict(os.environ)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return result

def execute_verifier(root: Path, relative_path: str) -> dict[str, Any]:
    path = root / relative_path
    require(path.is_file(), f"{relative_path}: missing verifier")
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
    completed = subprocess.run(
        [sys.executable, str(path)],
        cwd=root,
        env=environment(),
        capture_output=True,
        text=True,
        check=False,
    )
    require(
        completed.returncode == 0,
        f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    output = completed.stdout.strip()
    require(output.startswith("verified "), f"{relative_path}: missing verified report")
    return {
        "path": relative_path,
        "stdout_sha256": hashlib.sha256(output.encode()).hexdigest(),
        "stdout": output,
    }

def validate_fixture(fixture: dict[str, Any]) -> None:
    require(fixture.get("source_file_count") == 6, "fixture source count")
    require(fixture.get("verifier_file_count") == 6, "fixture verifier count")
    require(fixture.get("return_selector_assignment_exact") == 1, "fixture assignment")
    require(fixture.get("line_clean_integer_budgets_exact") == 1, "fixture budgets")
    require(fixture.get("critical_selector_localization_exact") == 1, "fixture localization")
    require(fixture.get("prime_field_root_support_splice_exact") == 1, "fixture root support")
    require(fixture.get("fixed_interface_thin_table_interface_exact") == 1, "fixture thin table")
    require(fixture.get("label_preserving_crt_assembly_exact") == 1, "fixture CRT")
    require(fixture.get("return_selector_assignment_certificate_complete") == 0, "fixture assignment honesty")
    require(fixture.get("required_thin_tables_executed_and_certified") == 0, "fixture thin honesty")
    require(fixture.get("all_labelled_recurrent_blocks_subcritical") == 0, "fixture labelled honesty")
    require(fixture.get("all_n_proved_by_checker") == 0, "fixture all-n honesty")

def mutation_audit() -> int:
    fixture = {
        "source_file_count": 6,
        "verifier_file_count": 6,
        "return_selector_assignment_exact": 1,
        "line_clean_integer_budgets_exact": 1,
        "critical_selector_localization_exact": 1,
        "prime_field_root_support_splice_exact": 1,
        "fixed_interface_thin_table_interface_exact": 1,
        "label_preserving_crt_assembly_exact": 1,
        "return_selector_assignment_certificate_complete": 0,
        "required_thin_tables_executed_and_certified": 0,
        "all_labelled_recurrent_blocks_subcritical": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(source_file_count=5),
        lambda item: item.update(verifier_file_count=5),
        lambda item: item.update(return_selector_assignment_exact=0),
        lambda item: item.update(line_clean_integer_budgets_exact=0),
        lambda item: item.update(critical_selector_localization_exact=0),
        lambda item: item.update(prime_field_root_support_splice_exact=0),
        lambda item: item.update(fixed_interface_thin_table_interface_exact=0),
        lambda item: item.update(label_preserving_crt_assembly_exact=0),
        lambda item: item.update(return_selector_assignment_certificate_complete=1),
        lambda item: item.update(required_thin_tables_executed_and_certified=1),
        lambda item: item.update(all_labelled_recurrent_blocks_subcritical=1),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try:
            validate_fixture(bad)
        except LabelledRecurrentCertificateError:
            rejected += 1
    require(rejected == len(mutations), "labelled recurrent certificate corruption accepted")
    return rejected

def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    root = repository_root()
    for source in SOURCE_FILES:
        require((root / source).is_file(), f"{source}: missing source")
    reports = [execute_verifier(root, path) for path in VERIFIER_FILES]
    print(json.dumps({
        "checker": "prime-power-labelled-recurrent-certificate-ancestry",
        "contract_sha256": contract,
        "source_file_count": len(SOURCE_FILES),
        "verifier_file_count": len(VERIFIER_FILES),
        "verifier_reports": reports,
        "rejected_corruptions": mutation_audit(),
        "return_selector_assignment_exact": 1,
        "line_clean_integer_budgets_exact": 1,
        "critical_selector_localization_exact": 1,
        "prime_field_root_support_splice_exact": 1,
        "fixed_interface_thin_table_interface_exact": 1,
        "label_preserving_crt_assembly_exact": 1,
        "labelled_recurrent_certificate_ancestry_proved": 1,
        "return_selector_assignment_certificate_complete": 0,
        "line_clean_integer_budgets_positive_all_classes": 0,
        "critical_selector_classes_certified": 0,
        "required_thin_tables_executed_and_certified": 0,
        "all_labelled_recurrent_blocks_subcritical": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "global_target_collateral_inequality_proved": 0,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_envelope_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
