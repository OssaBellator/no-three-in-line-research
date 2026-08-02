#!/usr/bin/env python3
"""Execute recurrent certificate-assembly ancestry for CMR1582--CMR1629."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class RecurrentCertificateAssemblyError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise RecurrentCertificateAssemblyError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SOURCE_FILES = [
    "docs/301-prime-power-return-selector-assignment-scalarization.md",
    "docs/302-prime-power-line-clean-integer-credit-budgets.md",
    "docs/303-prime-power-critical-selector-profile-localization.md",
    "docs/304-prime-field-root-channel-support-splice.md",
    "docs/305-prime-power-fixed-interface-thin-exact-table.md",
    "docs/306-prime-power-label-preserving-crt-certificate-assembly.md",
]
VERIFIER_FILES = [
    "scripts/verify_prime_power_return_selector_assignment.py",
    "scripts/verify_prime_power_line_clean_integer_budgets.py",
    "scripts/verify_prime_power_critical_selector_localization.py",
    "scripts/verify_prime_field_root_channel_support_splice.py",
    "scripts/verify_prime_power_fixed_interface_thin_table.py",
    "scripts/verify_prime_power_label_preserving_crt_assembly.py",
]
CONTRACT = {
    "schema": "prime-power-recurrent-certificate-assembly-ancestry/v1",
    "source_range": ["CMR1582", "CMR1629"],
    "source_files": SOURCE_FILES,
    "verifier_files": VERIFIER_FILES,
    "checked_layers": [
        "shared return-selector assignment scalarization and strict rational/integer dual certificates",
        "strong, singleton and endpoint-overlap line-clean integer credit budgets and slacks",
        "critical selector gap localization to finite rank/profile/geometric classes",
        "prime-field root-channel compression to singleton supports, return or exact fixed-interface atoms",
        "exact rational fixed-interface rows and finite thin-side certificate compilation",
        "label-preserving CRT SCC reduction and constructive rational/integer certificate gluing",
    ],
    "honesty_flags": {
        "return_selector_assignment_dual_globally_strict": 0,
        "line_clean_integer_slacks_globally_positive": 0,
        "critical_selector_classes_closed": 0,
        "fixed_interface_thin_table_subcritical": 0,
        "labelled_crt_recurrent_blocks_subcritical": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "195b9f8ce43391860ea28b7b0d882250fc0f13222b16e67f432c786cc2d80285"

def repository_root(start: Path | None = None) -> Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise RecurrentCertificateAssemblyError("unable to locate repository root")

def environment() -> dict[str,str]:
    result=dict(os.environ)
    result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"})
    return result

def execute_verifier(root: Path, relative_path: str) -> dict[str,Any]:
    path=root/relative_path
    require(path.is_file(),f"{relative_path}: missing verifier")
    compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip()
    require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any]) -> None:
    require(fixture.get("source_file_count")==6,"fixture source count")
    require(fixture.get("verifier_file_count")==6,"fixture verifier count")
    require(fixture.get("return_selector_assignment_exact")==1,"fixture assignment")
    require(fixture.get("line_clean_integer_budgets_exact")==1,"fixture budgets")
    require(fixture.get("critical_selector_localization_exact")==1,"fixture localization")
    require(fixture.get("prime_field_root_support_splice_exact")==1,"fixture root support")
    require(fixture.get("fixed_interface_thin_table_exact")==1,"fixture thin table")
    require(fixture.get("label_preserving_crt_assembly_exact")==1,"fixture CRT")
    require(fixture.get("return_selector_assignment_dual_globally_strict")==0,"fixture assignment honesty")
    require(fixture.get("labelled_crt_recurrent_blocks_subcritical")==0,"fixture CRT honesty")
    require(fixture.get("all_n_proved_by_checker")==0,"fixture all-n honesty")

def mutation_audit() -> int:
    fixture={
        "source_file_count":6,
        "verifier_file_count":6,
        "return_selector_assignment_exact":1,
        "line_clean_integer_budgets_exact":1,
        "critical_selector_localization_exact":1,
        "prime_field_root_support_splice_exact":1,
        "fixed_interface_thin_table_exact":1,
        "label_preserving_crt_assembly_exact":1,
        "return_selector_assignment_dual_globally_strict":0,
        "labelled_crt_recurrent_blocks_subcritical":0,
        "all_n_proved_by_checker":0,
    }
    mutations=[
        lambda item:item.update(source_file_count=5),
        lambda item:item.update(verifier_file_count=5),
        lambda item:item.update(return_selector_assignment_exact=0),
        lambda item:item.update(line_clean_integer_budgets_exact=0),
        lambda item:item.update(critical_selector_localization_exact=0),
        lambda item:item.update(prime_field_root_support_splice_exact=0),
        lambda item:item.update(fixed_interface_thin_table_exact=0),
        lambda item:item.update(label_preserving_crt_assembly_exact=0),
        lambda item:item.update(return_selector_assignment_dual_globally_strict=1),
        lambda item:item.update(labelled_crt_recurrent_blocks_subcritical=1),
        lambda item:item.update(all_n_proved_by_checker=1),
        lambda item:item.clear(),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except RecurrentCertificateAssemblyError: rejected+=1
    require(rejected==len(mutations),"recurrent-certificate corruption accepted")
    return rejected

def main() -> None:
    contract=digest(CONTRACT)
    require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({
        "checker":"prime-power-recurrent-certificate-assembly-ancestry",
        "contract_sha256":contract,
        "source_file_count":len(SOURCE_FILES),
        "verifier_file_count":len(VERIFIER_FILES),
        "verifier_reports":reports,
        "rejected_corruptions":mutation_audit(),
        "return_selector_assignment_exact":1,
        "line_clean_integer_budgets_exact":1,
        "critical_selector_localization_exact":1,
        "prime_field_root_support_splice_exact":1,
        "fixed_interface_thin_table_exact":1,
        "label_preserving_crt_assembly_exact":1,
        "recurrent_certificate_assembly_ancestry_proved":1,
        "return_selector_assignment_dual_globally_strict":0,
        "line_clean_integer_slacks_globally_positive":0,
        "critical_selector_classes_closed":0,
        "fixed_interface_thin_table_subcritical":0,
        "labelled_crt_recurrent_blocks_subcritical":0,
        "same_owner_diagonal_blocks_subcritical":0,
        "global_target_collateral_inequality_proved":0,
        "all_owner_operations_proved":0,
        "all_scheduler_operations_proved":0,
        "all_restoration_operations_proved":0,
        "all_returned_edge_operations_proved":0,
        "all_envelope_operations_proved":0,
        "all_construction_ancestry_proved":0,
        "global_transition_kind_bank_exhaustive":0,
        "global_termination_proved":0,
        "actual_global_parent_rule_complete":0,
        "all_n_proved_by_checker":0,
    },sort_keys=True))

if __name__=="__main__": main()
