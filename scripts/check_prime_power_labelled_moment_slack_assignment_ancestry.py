#!/usr/bin/env python3
"""Execute labelled moment, slack and assignment ancestry for CMR1830--CMR1893."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class LabelledMomentSlackAssignmentError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise LabelledMomentSlackAssignmentError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SOURCE_FILES=["docs/332-prime-power-geometric-fibre-occupancy-moment-census.md","docs/333-prime-power-label-weighted-unified-assignment-lp.md","docs/334-prime-power-diagonal-parity-line-occupancy-census.md","docs/335-prime-power-geometric-fibre-moment-pareto-envelopes.md","docs/336-prime-power-labelled-assignment-certificate-manifest.md","docs/337-prime-power-rank-three-fibre-slack-classification.md","docs/338-prime-power-exact-response-averaged-line-moment-census.md","docs/339-prime-power-rank-three-slack-line-budget-allocation.md"]
VERIFIER_FILES=["scripts/verify_prime_power_geometric_fibre_occupancy_moments.py","scripts/verify_prime_power_label_weighted_unified_assignment_lp.py","scripts/verify_prime_power_diagonal_parity_line_occupancy.py","scripts/verify_prime_power_geometric_fibre_moment_pareto_envelopes.py","scripts/check_label_weighted_assignment_certificate.py","scripts/verify_prime_power_rank_three_fibre_slack_classification.py","scripts/verify_prime_power_exact_response_averaged_line_moments.py","scripts/verify_prime_power_rank_three_slack_line_budget_allocation.py"]
CONTRACT={"schema":"prime-power-labelled-moment-slack-assignment-ancestry/v1","source_range":["CMR1830","CMR1893"],"source_files":SOURCE_FILES,"verifier_files":VERIFIER_FILES,"checked_layers":["exact occupancy moment census and diagonal parity full-line capacities","label-weighted unified nested assignment LP and executable certificate manifest","moment Pareto envelopes and exact rank-three host slack classification","response-averaged line moments and rank-three residual line-budget allocation"],"honesty_flags":{"labelled_assignment_manifest_populated_all_recurrent_states":0,"rank_three_slack_allocates_all_geometric_rows":0,"actual_background_height_profiles_certified":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_SHA256="fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise LabelledMomentSlackAssignmentError("unable to locate repository root")

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def execute_verifier(root: Path,relative_path: str)->dict[str,Any]:
    path=root/relative_path; require(path.is_file(),f"{relative_path}: missing verifier"); compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip(); require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any])->None:
    require(fixture.get("source_file_count")==8,"fixture source count"); require(fixture.get("verifier_file_count")==8,"fixture verifier count")
    for key in ("occupancy_moment_census_exact","label_weighted_assignment_lp_exact","diagonal_parity_line_occupancy_exact","moment_pareto_envelopes_exact","labelled_assignment_manifest_checker_exact","rank_three_fibre_slack_exact","response_averaged_line_moments_exact","rank_three_slack_line_budget_exact"): require(fixture.get(key)==1,f"fixture {key}")
    for key in ("labelled_assignment_manifest_populated_all_recurrent_states","rank_three_slack_allocates_all_geometric_rows","actual_background_height_profiles_certified","complete_labelled_recurrent_lp_strict","all_n_proved_by_checker"): require(fixture.get(key)==0,f"fixture honesty {key}")

def mutation_audit()->int:
    fixture={"source_file_count":8,"verifier_file_count":8,"occupancy_moment_census_exact":1,"label_weighted_assignment_lp_exact":1,"diagonal_parity_line_occupancy_exact":1,"moment_pareto_envelopes_exact":1,"labelled_assignment_manifest_checker_exact":1,"rank_three_fibre_slack_exact":1,"response_averaged_line_moments_exact":1,"rank_three_slack_line_budget_exact":1,"labelled_assignment_manifest_populated_all_recurrent_states":0,"rank_three_slack_allocates_all_geometric_rows":0,"actual_background_height_profiles_certified":0,"complete_labelled_recurrent_lp_strict":0,"all_n_proved_by_checker":0}
    mutations=[lambda x:x.update(source_file_count=7),lambda x:x.update(verifier_file_count=7)]
    mutations += [lambda x,key=key:x.update({key:0}) for key in ("occupancy_moment_census_exact","label_weighted_assignment_lp_exact","diagonal_parity_line_occupancy_exact","moment_pareto_envelopes_exact","labelled_assignment_manifest_checker_exact","rank_three_fibre_slack_exact","response_averaged_line_moments_exact","rank_three_slack_line_budget_exact")]
    mutations += [lambda x,key=key:x.update({key:1}) for key in ("labelled_assignment_manifest_populated_all_recurrent_states","rank_three_slack_allocates_all_geometric_rows","actual_background_height_profiles_certified","complete_labelled_recurrent_lp_strict","all_n_proved_by_checker")]
    mutations.append(lambda x:x.clear()); rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except LabelledMomentSlackAssignmentError: rejected+=1
    require(rejected==len(mutations),"labelled moment corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({"checker":"prime-power-labelled-moment-slack-assignment-ancestry","contract_sha256":contract,"source_file_count":len(SOURCE_FILES),"verifier_file_count":len(VERIFIER_FILES),"verifier_reports":reports,"rejected_corruptions":mutation_audit(),"occupancy_moment_census_exact":1,"label_weighted_assignment_lp_exact":1,"diagonal_parity_line_occupancy_exact":1,"moment_pareto_envelopes_exact":1,"labelled_assignment_manifest_checker_exact":1,"rank_three_fibre_slack_exact":1,"response_averaged_line_moments_exact":1,"rank_three_slack_line_budget_exact":1,"labelled_moment_slack_assignment_ancestry_proved":1,"labelled_assignment_manifest_populated_all_recurrent_states":0,"rank_three_slack_allocates_all_geometric_rows":0,"actual_background_height_profiles_certified":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
