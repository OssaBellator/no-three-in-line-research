#!/usr/bin/env python3
"""Execute recurrent cover, budget, census and auxiliary-elimination ancestry for CMR1630--CMR1701."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class RecurrentCoverBudgetCensusError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise RecurrentCoverBudgetCensusError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SOURCE_FILES = ['docs/307-prime-power-return-assignment-superlevel-covers.md', 'docs/308-prime-power-line-clean-universal-budget-floors.md', 'docs/309-prime-power-selector-capacity-gap-compiler.md', 'docs/310-prime-power-fixed-interface-symmetry-normalization.md', 'docs/311-prime-power-normalized-thin-response-census.md', 'docs/312-prime-power-return-class-support-covers.md', 'docs/313-prime-power-line-clean-profile-capacity-compiler.md', 'docs/314-prime-power-normalized-thin-rank-three-census.md', 'docs/315-prime-power-subcritical-auxiliary-block-elimination.md']
VERIFIER_FILES = ['scripts/verify_prime_power_return_assignment_superlevel_covers.py', 'scripts/verify_prime_power_line_clean_universal_budget_floors.py', 'scripts/verify_prime_power_selector_capacity_gap_compiler.py', 'scripts/verify_prime_power_fixed_interface_symmetry_normalization.py', 'scripts/verify_prime_power_normalized_thin_response_census.py', 'scripts/verify_prime_power_return_class_support_covers.py', 'scripts/verify_prime_power_line_clean_profile_capacity_compiler.py', 'scripts/verify_prime_power_normalized_thin_rank_three_census.py', 'scripts/verify_prime_power_subcritical_auxiliary_block_elimination.py']
CONTRACT = {'schema': 'prime-power-recurrent-cover-budget-census-ancestry/v1', 'source_range': ['CMR1630', 'CMR1701'], 'source_files': ['docs/307-prime-power-return-assignment-superlevel-covers.md', 'docs/308-prime-power-line-clean-universal-budget-floors.md', 'docs/309-prime-power-selector-capacity-gap-compiler.md', 'docs/310-prime-power-fixed-interface-symmetry-normalization.md', 'docs/311-prime-power-normalized-thin-response-census.md', 'docs/312-prime-power-return-class-support-covers.md', 'docs/313-prime-power-line-clean-profile-capacity-compiler.md', 'docs/314-prime-power-normalized-thin-rank-three-census.md', 'docs/315-prime-power-subcritical-auxiliary-block-elimination.md'], 'verifier_files': ['scripts/verify_prime_power_return_assignment_superlevel_covers.py', 'scripts/verify_prime_power_line_clean_universal_budget_floors.py', 'scripts/verify_prime_power_selector_capacity_gap_compiler.py', 'scripts/verify_prime_power_fixed_interface_symmetry_normalization.py', 'scripts/verify_prime_power_normalized_thin_response_census.py', 'scripts/verify_prime_power_return_class_support_covers.py', 'scripts/verify_prime_power_line_clean_profile_capacity_compiler.py', 'scripts/verify_prime_power_normalized_thin_rank_three_census.py', 'scripts/verify_prime_power_subcritical_auxiliary_block_elimination.py'], 'checked_layers': ['return-selector superlevel matching and vertex-cover certificates', 'universal side-four line-clean budget floors and automatic ranges', 'selector class-capacity gap compilation and restoration caps', 'fixed-interface symmetry normalization with equivariant label retention', 'exact normalized thin response and rank-three prescription censuses through side five', 'geometric class-support cover compilation into shared assignment duals', 'line-clean profile-capacity compilation with overflow localization', 'exact nonnegative auxiliary-block resolvent elimination and rational/integer lifting'], 'honesty_flags': {'return_assignment_cover_globally_strict': 0, 'line_clean_universal_budgets_cover_all_classes': 0, 'selector_capacity_gaps_close_all_classes': 0, 'normalized_thin_geometric_offspring_certified': 0, 'auxiliary_effective_core_subcritical': 0, 'same_owner_diagonal_blocks_subcritical': 0, 'global_target_collateral_inequality_proved': 0, 'global_transition_kind_bank_exhaustive': 0, 'global_termination_proved': 0, 'actual_global_parent_rule_complete': 0, 'all_n_proved_by_checker': 0}}
EXPECTED_CONTRACT_SHA256 = "d04df054a47094437e1428567b2d5f244b67eff42070ee5adc1566cafdfce7b2"

def repository_root(start: Path | None = None) -> Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise RecurrentCoverBudgetCensusError("unable to locate repository root")

def environment() -> dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

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
    require(fixture.get("source_file_count")==9,"fixture source count")
    require(fixture.get("verifier_file_count")==9,"fixture verifier count")
    require(fixture.get("return_assignment_superlevel_covers_exact")==1,"fixture superlevel")
    require(fixture.get("line_clean_universal_budget_floors_exact")==1,"fixture floors")
    require(fixture.get("selector_capacity_gap_compiler_exact")==1,"fixture selector gap")
    require(fixture.get("fixed_interface_symmetry_normalization_exact")==1,"fixture symmetry")
    require(fixture.get("normalized_thin_response_census_exact")==1,"fixture thin response")
    require(fixture.get("return_class_support_covers_exact")==1,"fixture support covers")
    require(fixture.get("line_clean_profile_capacity_compiler_exact")==1,"fixture profile compiler")
    require(fixture.get("normalized_thin_rank_three_census_exact")==1,"fixture rank three")
    require(fixture.get("subcritical_auxiliary_block_elimination_exact")==1,"fixture auxiliary")
    require(fixture.get("return_assignment_cover_globally_strict")==0,"fixture cover honesty")
    require(fixture.get("normalized_thin_geometric_offspring_certified")==0,"fixture thin honesty")
    require(fixture.get("auxiliary_effective_core_subcritical")==0,"fixture effective honesty")
    require(fixture.get("all_n_proved_by_checker")==0,"fixture all-n honesty")

def mutation_audit() -> int:
    fixture={
        "source_file_count":9,"verifier_file_count":9,
        "return_assignment_superlevel_covers_exact":1,
        "line_clean_universal_budget_floors_exact":1,
        "selector_capacity_gap_compiler_exact":1,
        "fixed_interface_symmetry_normalization_exact":1,
        "normalized_thin_response_census_exact":1,
        "return_class_support_covers_exact":1,
        "line_clean_profile_capacity_compiler_exact":1,
        "normalized_thin_rank_three_census_exact":1,
        "subcritical_auxiliary_block_elimination_exact":1,
        "return_assignment_cover_globally_strict":0,
        "normalized_thin_geometric_offspring_certified":0,
        "auxiliary_effective_core_subcritical":0,
        "all_n_proved_by_checker":0,
    }
    mutations=[
        lambda item:item.update(source_file_count=8),
        lambda item:item.update(verifier_file_count=8),
        lambda item:item.update(return_assignment_superlevel_covers_exact=0),
        lambda item:item.update(line_clean_universal_budget_floors_exact=0),
        lambda item:item.update(selector_capacity_gap_compiler_exact=0),
        lambda item:item.update(fixed_interface_symmetry_normalization_exact=0),
        lambda item:item.update(normalized_thin_response_census_exact=0),
        lambda item:item.update(return_class_support_covers_exact=0),
        lambda item:item.update(line_clean_profile_capacity_compiler_exact=0),
        lambda item:item.update(normalized_thin_rank_three_census_exact=0),
        lambda item:item.update(subcritical_auxiliary_block_elimination_exact=0),
        lambda item:item.update(return_assignment_cover_globally_strict=1),
        lambda item:item.update(normalized_thin_geometric_offspring_certified=1),
        lambda item:item.update(auxiliary_effective_core_subcritical=1),
        lambda item:item.update(all_n_proved_by_checker=1),
        lambda item:item.clear(),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except RecurrentCoverBudgetCensusError: rejected+=1
    require(rejected==len(mutations),"recurrent cover/budget corruption accepted")
    return rejected

def main() -> None:
    contract_hash=digest(CONTRACT)
    require(contract_hash==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({
        "checker":"prime-power-recurrent-cover-budget-census-ancestry",
        "contract_sha256":contract_hash,
        "source_file_count":len(SOURCE_FILES),
        "verifier_file_count":len(VERIFIER_FILES),
        "verifier_reports":reports,
        "rejected_corruptions":mutation_audit(),
        "return_assignment_superlevel_covers_exact":1,
        "line_clean_universal_budget_floors_exact":1,
        "selector_capacity_gap_compiler_exact":1,
        "fixed_interface_symmetry_normalization_exact":1,
        "normalized_thin_response_census_exact":1,
        "return_class_support_covers_exact":1,
        "line_clean_profile_capacity_compiler_exact":1,
        "normalized_thin_rank_three_census_exact":1,
        "subcritical_auxiliary_block_elimination_exact":1,
        "recurrent_cover_budget_census_ancestry_proved":1,
        "return_assignment_cover_globally_strict":0,
        "line_clean_universal_budgets_cover_all_classes":0,
        "selector_capacity_gaps_close_all_classes":0,
        "normalized_thin_geometric_offspring_certified":0,
        "auxiliary_effective_core_subcritical":0,
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
