#!/usr/bin/env python3
"""Execute superlevel, budget, thin-census and auxiliary ancestry for CMR1630--CMR1701."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class SuperlevelBudgetThinAuxiliaryError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise SuperlevelBudgetThinAuxiliaryError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SOURCE_FILES=[
"docs/307-prime-power-return-assignment-superlevel-covers.md",
"docs/308-prime-power-line-clean-universal-budget-floors.md",
"docs/309-prime-power-selector-capacity-gap-compiler.md",
"docs/310-prime-power-fixed-interface-symmetry-normalization.md",
"docs/311-prime-power-normalized-thin-response-census.md",
"docs/312-prime-power-return-class-support-covers.md",
"docs/313-prime-power-line-clean-profile-capacity-compiler.md",
"docs/314-prime-power-normalized-thin-rank-three-census.md",
"docs/315-prime-power-subcritical-auxiliary-block-elimination.md",
]
VERIFIER_FILES=[
"scripts/verify_prime_power_return_assignment_superlevel_covers.py",
"scripts/verify_prime_power_line_clean_universal_budget_floors.py",
"scripts/verify_prime_power_selector_capacity_gap_compiler.py",
"scripts/verify_prime_power_fixed_interface_symmetry_normalization.py",
"scripts/verify_prime_power_normalized_thin_response_census.py",
"scripts/verify_prime_power_return_class_support_covers.py",
"scripts/verify_prime_power_line_clean_profile_capacity_compiler.py",
"scripts/verify_prime_power_normalized_thin_rank_three_census.py",
"scripts/verify_prime_power_subcritical_auxiliary_block_elimination.py",
]
CONTRACT={
"schema":"prime-power-superlevel-budget-thin-auxiliary-ancestry/v1",
"source_range":["CMR1630","CMR1701"],
"source_files":SOURCE_FILES,
"verifier_files":VERIFIER_FILES,
"checked_layers":[
"combined return-selector superlevel matching and vertex-cover certificates",
"universal line-clean budget floors and exact selector-capacity gaps",
"fixed-interface symmetry normalization and exact thin response census through side five",
"class-supported return covers and line-clean profile-capacity overflow localization",
"normalized rank-three thin census and exact auxiliary-block resolvent elimination",
],
"honesty_flags":{
"return_superlevel_cover_globally_strict":0,
"universal_line_clean_budgets_close_all_classes":0,
"selector_capacity_classes_closed":0,
"normalized_thin_geometric_rows_subcritical":0,
"auxiliary_effective_core_subcritical":0,
"same_owner_diagonal_blocks_subcritical":0,
"global_target_collateral_inequality_proved":0,
"global_transition_kind_bank_exhaustive":0,
"global_termination_proved":0,
"actual_global_parent_rule_complete":0,
"all_n_proved_by_checker":0,
}}
EXPECTED_CONTRACT_SHA256="e155ea311c24a9f04e1a603877190d1e60f9928a4607546635a9198344e53ad0"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise SuperlevelBudgetThinAuxiliaryError("unable to locate repository root")

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def execute_verifier(root: Path, relative_path: str)->dict[str,Any]:
    path=root/relative_path
    require(path.is_file(),f"{relative_path}: missing verifier")
    compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip(); require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any])->None:
    require(fixture.get("source_file_count")==9,"fixture source count")
    require(fixture.get("verifier_file_count")==9,"fixture verifier count")
    for key in (
        "return_superlevel_covers_exact","universal_line_clean_budget_floors_exact",
        "selector_capacity_gap_exact","fixed_interface_symmetry_normalization_exact",
        "normalized_thin_response_census_exact","return_class_support_covers_exact",
        "line_clean_profile_capacity_exact","normalized_thin_rank_three_census_exact",
        "auxiliary_block_elimination_exact",
    ): require(fixture.get(key)==1,f"fixture {key}")
    for key in (
        "return_superlevel_cover_globally_strict","normalized_thin_geometric_rows_subcritical",
        "auxiliary_effective_core_subcritical","all_n_proved_by_checker",
    ): require(fixture.get(key)==0,f"fixture honesty {key}")

def mutation_audit()->int:
    fixture={"source_file_count":9,"verifier_file_count":9,
    "return_superlevel_covers_exact":1,"universal_line_clean_budget_floors_exact":1,
    "selector_capacity_gap_exact":1,"fixed_interface_symmetry_normalization_exact":1,
    "normalized_thin_response_census_exact":1,"return_class_support_covers_exact":1,
    "line_clean_profile_capacity_exact":1,"normalized_thin_rank_three_census_exact":1,
    "auxiliary_block_elimination_exact":1,"return_superlevel_cover_globally_strict":0,
    "normalized_thin_geometric_rows_subcritical":0,"auxiliary_effective_core_subcritical":0,
    "all_n_proved_by_checker":0}
    mutations=[lambda x:x.update(source_file_count=8),lambda x:x.update(verifier_file_count=8)]
    mutations += [lambda x,key=key:x.update({key:0}) for key in (
        "return_superlevel_covers_exact","universal_line_clean_budget_floors_exact","selector_capacity_gap_exact",
        "fixed_interface_symmetry_normalization_exact","normalized_thin_response_census_exact",
        "return_class_support_covers_exact","line_clean_profile_capacity_exact",
        "normalized_thin_rank_three_census_exact","auxiliary_block_elimination_exact")]
    mutations += [lambda x,key=key:x.update({key:1}) for key in (
        "return_superlevel_cover_globally_strict","normalized_thin_geometric_rows_subcritical",
        "auxiliary_effective_core_subcritical","all_n_proved_by_checker")]
    mutations.append(lambda x:x.clear())
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except SuperlevelBudgetThinAuxiliaryError: rejected+=1
    require(rejected==len(mutations),"superlevel/budget corruption accepted")
    return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({
    "checker":"prime-power-superlevel-budget-thin-auxiliary-ancestry",
    "contract_sha256":contract,"source_file_count":len(SOURCE_FILES),"verifier_file_count":len(VERIFIER_FILES),
    "verifier_reports":reports,"rejected_corruptions":mutation_audit(),
    "return_superlevel_covers_exact":1,"universal_line_clean_budget_floors_exact":1,
    "selector_capacity_gap_exact":1,"fixed_interface_symmetry_normalization_exact":1,
    "normalized_thin_response_census_exact":1,"return_class_support_covers_exact":1,
    "line_clean_profile_capacity_exact":1,"normalized_thin_rank_three_census_exact":1,
    "auxiliary_block_elimination_exact":1,"superlevel_budget_thin_auxiliary_ancestry_proved":1,
    "return_superlevel_cover_globally_strict":0,"universal_line_clean_budgets_close_all_classes":0,
    "selector_capacity_classes_closed":0,"normalized_thin_geometric_rows_subcritical":0,
    "auxiliary_effective_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,
    "global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,
    "global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0,
    },sort_keys=True))

if __name__=="__main__": main()
