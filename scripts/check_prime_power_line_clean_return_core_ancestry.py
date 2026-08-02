#!/usr/bin/env python3
"""Execute line-clean, repeated-token and return-kernel ancestry for CMR1510--CMR1581."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


class LineCleanReturnCoreError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise LineCleanReturnCoreError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SOURCE_FILES = ['docs/292-prime-power-extension-free-partial-matching-line-clean.md', 'docs/293-prime-power-repeated-token-atomic-compression.md', 'docs/294-prime-power-extension-free-line-clean-rook-rows.md', 'docs/295-prime-power-line-clean-uniform-permanent-envelope.md', 'docs/296-prime-power-line-clean-factor-signature-sharpening.md', 'docs/297-prime-power-line-clean-singleton-fractional-factor.md', 'docs/298-prime-power-paid-pair-selector-return-splice.md', 'docs/299-prime-power-trace-centre-line-clean-splice.md', 'docs/300-prime-power-returned-edge-exchange-kernel.md']
VERIFIER_FILES = ['scripts/verify_prime_power_extension_free_partial_matching_line_clean.py', 'scripts/verify_prime_power_repeated_token_atomic_compression.py', 'scripts/verify_prime_power_extension_free_line_clean_rook_rows.py', 'scripts/verify_prime_power_line_clean_uniform_permanent.py', 'scripts/verify_prime_power_line_clean_factor_sharpening.py', 'scripts/verify_prime_power_line_clean_singleton_fractional.py', 'scripts/verify_prime_power_paid_pair_selector_return_splice.py', 'scripts/verify_prime_power_trace_centre_line_clean_splice.py', 'scripts/verify_prime_power_return_exchange_kernel.py']
CONTRACT = {'schema': 'prime-power-line-clean-return-core-ancestry/v1', 'source_range': ['CMR1510', 'CMR1581'], 'source_files': ['docs/292-prime-power-extension-free-partial-matching-line-clean.md', 'docs/293-prime-power-repeated-token-atomic-compression.md', 'docs/294-prime-power-extension-free-line-clean-rook-rows.md', 'docs/295-prime-power-line-clean-uniform-permanent-envelope.md', 'docs/296-prime-power-line-clean-factor-signature-sharpening.md', 'docs/297-prime-power-line-clean-singleton-fractional-factor.md', 'docs/298-prime-power-paid-pair-selector-return-splice.md', 'docs/299-prime-power-trace-centre-line-clean-splice.md', 'docs/300-prime-power-returned-edge-exchange-kernel.md'], 'verifier_files': ['scripts/verify_prime_power_extension_free_partial_matching_line_clean.py', 'scripts/verify_prime_power_repeated_token_atomic_compression.py', 'scripts/verify_prime_power_extension_free_line_clean_rook_rows.py', 'scripts/verify_prime_power_line_clean_uniform_permanent.py', 'scripts/verify_prime_power_line_clean_factor_sharpening.py', 'scripts/verify_prime_power_line_clean_singleton_fractional.py', 'scripts/verify_prime_power_paid_pair_selector_return_splice.py', 'scripts/verify_prime_power_trace_centre_line_clean_splice.py', 'scripts/verify_prime_power_return_exchange_kernel.py'], 'checked_layers': ['arbitrary partial-matching deletion and exact target-safe nonaxis line cleaning', 'repeated-token compression to return, paid-pair selector and trace atomic rows', 'degree-two component rook polynomials and exact line-clean prescription ratios', 'uniform spanning-factor permanent envelopes and ternary line-clean coefficient classes', 'subunit paid-pair selector restoration caps and exact two-row return coupling', 'rooted trace-centre batching and strong-or-singleton line-clean execution', 'returned-edge exchange bijections, exact recreated-credit transport and coarse return quotients'], 'honesty_flags': {'line_clean_recurrent_rows_subcritical': 0, 'return_selector_block_subcritical': 0, 'critical_selector_candidate_regime_closed': 0, 'trace_without_root_target_execution_closed': 0, 'same_owner_diagonal_blocks_subcritical': 0, 'global_target_collateral_inequality_proved': 0, 'global_transition_kind_bank_exhaustive': 0, 'global_termination_proved': 0, 'actual_global_parent_rule_complete': 0, 'all_n_proved_by_checker': 0}}
EXPECTED_CONTRACT_SHA256 = "0a1620bf756ec529255be95c072a8435d870762644908a5000418d084948aec4"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise LineCleanReturnCoreError("unable to locate repository root")


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
    require(fixture.get("source_file_count") == 9, "fixture source count")
    require(fixture.get("verifier_file_count") == 9, "fixture verifier count")
    require(fixture.get("partial_matching_line_clean_exact") == 1, "fixture line clean")
    require(fixture.get("repeated_token_atomic_compression_exact") == 1, "fixture token compression")
    require(fixture.get("line_clean_rook_rows_exact") == 1, "fixture rook rows")
    require(fixture.get("ternary_line_clean_coefficients_exact") == 1, "fixture coefficients")
    require(fixture.get("subunit_selector_return_splice_exact") == 1, "fixture selector splice")
    require(fixture.get("rooted_trace_line_clean_splice_exact") == 1, "fixture trace splice")
    require(fixture.get("return_exchange_kernel_exact") == 1, "fixture return kernel")
    require(fixture.get("line_clean_recurrent_rows_subcritical") == 0, "fixture line-clean honesty")
    require(fixture.get("return_selector_block_subcritical") == 0, "fixture return honesty")
    require(fixture.get("all_n_proved_by_checker") == 0, "fixture all-n honesty")


def mutation_audit() -> int:
    fixture = {
        "source_file_count": 9,
        "verifier_file_count": 9,
        "partial_matching_line_clean_exact": 1,
        "repeated_token_atomic_compression_exact": 1,
        "line_clean_rook_rows_exact": 1,
        "ternary_line_clean_coefficients_exact": 1,
        "subunit_selector_return_splice_exact": 1,
        "rooted_trace_line_clean_splice_exact": 1,
        "return_exchange_kernel_exact": 1,
        "line_clean_recurrent_rows_subcritical": 0,
        "return_selector_block_subcritical": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(source_file_count=8),
        lambda item: item.update(verifier_file_count=8),
        lambda item: item.update(partial_matching_line_clean_exact=0),
        lambda item: item.update(repeated_token_atomic_compression_exact=0),
        lambda item: item.update(line_clean_rook_rows_exact=0),
        lambda item: item.update(ternary_line_clean_coefficients_exact=0),
        lambda item: item.update(subunit_selector_return_splice_exact=0),
        lambda item: item.update(rooted_trace_line_clean_splice_exact=0),
        lambda item: item.update(return_exchange_kernel_exact=0),
        lambda item: item.update(line_clean_recurrent_rows_subcritical=1),
        lambda item: item.update(return_selector_block_subcritical=1),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try:
            validate_fixture(bad)
        except LineCleanReturnCoreError:
            rejected += 1
    require(rejected == len(mutations), "line-clean/return corruption accepted")
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    root = repository_root()
    for source in SOURCE_FILES:
        require((root / source).is_file(), f"{source}: missing source")
    reports = [execute_verifier(root, path) for path in VERIFIER_FILES]
    print(
        json.dumps(
            {
                "checker": "prime-power-line-clean-return-core-ancestry",
                "contract_sha256": contract,
                "source_file_count": len(SOURCE_FILES),
                "verifier_file_count": len(VERIFIER_FILES),
                "verifier_reports": reports,
                "rejected_corruptions": mutation_audit(),
                "partial_matching_line_clean_exact": 1,
                "repeated_token_atomic_compression_exact": 1,
                "line_clean_rook_rows_exact": 1,
                "ternary_line_clean_coefficients_exact": 1,
                "subunit_selector_return_splice_exact": 1,
                "rooted_trace_line_clean_splice_exact": 1,
                "return_exchange_kernel_exact": 1,
                "line_clean_return_core_ancestry_proved": 1,
                "line_clean_recurrent_rows_subcritical": 0,
                "return_selector_block_subcritical": 0,
                "critical_selector_candidate_regime_closed": 0,
                "trace_without_root_target_execution_closed": 0,
                "same_owner_diagonal_blocks_subcritical": 0,
                "global_target_collateral_inequality_proved": 0,
                "all_owner_operations_proved": 0,
                "all_scheduler_operations_proved": 0,
                "all_restoration_operations_proved": 0,
                "all_returned_edge_operations_proved": 0,
                "all_construction_ancestry_proved": 0,
                "global_transition_kind_bank_exhaustive": 0,
                "global_termination_proved": 0,
                "actual_global_parent_rule_complete": 0,
                "all_n_proved_by_checker": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
