#!/usr/bin/env python3
"""Execute rank-mass, multiplicity and line-energy ancestry for CMR1702--CMR1773."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class RankMassMultiplicityLineEnergyError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise RankMassMultiplicityLineEnergyError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SOURCE_FILES=[
"docs/316-prime-power-prescription-rank-mass-conservation.md",
"docs/317-prime-power-line-clean-rank-mass-large-load-closure.md",
"docs/318-prime-power-owner-support-rank-mass-capacities.md",
"docs/319-prime-power-owner-support-large-load-closure.md",
"docs/320-prime-power-geometric-prescription-multiplicity-formulas.md",
"docs/321-prime-power-packed-secant-multiplicity-bounds.md",
"docs/322-prime-power-background-triple-multiplicity-charge.md",
"docs/323-prime-power-background-potential-multiplicity-bounds.md",
"docs/324-prime-power-line-energy-profile-census.md",
]
VERIFIER_FILES=[
"scripts/verify_prime_power_prescription_rank_mass_conservation.py",
"scripts/verify_prime_power_line_clean_rank_mass_large_load.py",
"scripts/verify_prime_power_owner_support_rank_mass_capacities.py",
"scripts/verify_prime_power_owner_support_large_load_closure.py",
"scripts/verify_prime_power_geometric_prescription_multiplicity.py",
"scripts/verify_prime_power_packed_secant_multiplicity.py",
"scripts/verify_prime_power_background_triple_multiplicity_charge.py",
"scripts/verify_prime_power_background_potential_multiplicity.py",
"scripts/verify_prime_power_line_energy_profile_census.py",
]
CONTRACT={"schema":"prime-power-rank-mass-multiplicity-line-energy-ancestry/v1","source_range":["CMR1702","CMR1773"],"source_files":SOURCE_FILES,"verifier_files":VERIFIER_FILES,"checked_layers":["exact prescription rank-mass conservation and multiplicity-aware line-clean closure","owner-support matching-number capacities and small-support large-load closure","exact geometric rank-one, rank-two and rank-three prescription multiplicities","packed secant and background-triple potential multiplicity bounds","exact line-energy profile census and response-profile charge bounds"],"honesty_flags":{"all_line_clean_large_load_rows_closed":0,"all_owner_support_rows_closed":0,"geometric_multiplicity_caps_globally_sufficient":0,"triple_free_response_policy_globally_available":0,"line_energy_profile_rows_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_SHA256="681a56e37003368e62a92ae7df349488e03e03eec34c2cddf2ab39b8d6622bdd"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise RankMassMultiplicityLineEnergyError("unable to locate repository root")

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def execute_verifier(root: Path,relative_path: str)->dict[str,Any]:
    path=root/relative_path; require(path.is_file(),f"{relative_path}: missing verifier")
    compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip(); require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any])->None:
    require(fixture.get("source_file_count")==9,"fixture source count"); require(fixture.get("verifier_file_count")==9,"fixture verifier count")
    exact=("rank_mass_conservation_exact","line_clean_large_load_closure_exact","owner_support_rank_mass_exact","owner_support_large_load_closure_exact","geometric_multiplicity_formulas_exact","packed_secant_bounds_exact","background_triple_charge_exact","background_potential_bounds_exact","line_energy_profile_census_exact")
    for key in exact: require(fixture.get(key)==1,f"fixture {key}")
    for key in ("all_line_clean_large_load_rows_closed","all_owner_support_rows_closed","line_energy_profile_rows_subcritical","all_n_proved_by_checker"): require(fixture.get(key)==0,f"fixture honesty {key}")

def mutation_audit()->int:
    fixture={"source_file_count":9,"verifier_file_count":9,"rank_mass_conservation_exact":1,"line_clean_large_load_closure_exact":1,"owner_support_rank_mass_exact":1,"owner_support_large_load_closure_exact":1,"geometric_multiplicity_formulas_exact":1,"packed_secant_bounds_exact":1,"background_triple_charge_exact":1,"background_potential_bounds_exact":1,"line_energy_profile_census_exact":1,"all_line_clean_large_load_rows_closed":0,"all_owner_support_rows_closed":0,"line_energy_profile_rows_subcritical":0,"all_n_proved_by_checker":0}
    mutations=[lambda x:x.update(source_file_count=8),lambda x:x.update(verifier_file_count=8)]
    mutations += [lambda x,key=key:x.update({key:0}) for key in ("rank_mass_conservation_exact","line_clean_large_load_closure_exact","owner_support_rank_mass_exact","owner_support_large_load_closure_exact","geometric_multiplicity_formulas_exact","packed_secant_bounds_exact","background_triple_charge_exact","background_potential_bounds_exact","line_energy_profile_census_exact")]
    mutations += [lambda x,key=key:x.update({key:1}) for key in ("all_line_clean_large_load_rows_closed","all_owner_support_rows_closed","line_energy_profile_rows_subcritical","all_n_proved_by_checker")]
    mutations.append(lambda x:x.clear()); rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except RankMassMultiplicityLineEnergyError: rejected+=1
    require(rejected==len(mutations),"rank-mass corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({"checker":"prime-power-rank-mass-multiplicity-line-energy-ancestry","contract_sha256":contract,"source_file_count":len(SOURCE_FILES),"verifier_file_count":len(VERIFIER_FILES),"verifier_reports":reports,"rejected_corruptions":mutation_audit(),"rank_mass_conservation_exact":1,"line_clean_large_load_closure_exact":1,"owner_support_rank_mass_exact":1,"owner_support_large_load_closure_exact":1,"geometric_multiplicity_formulas_exact":1,"packed_secant_bounds_exact":1,"background_triple_charge_exact":1,"background_potential_bounds_exact":1,"line_energy_profile_census_exact":1,"rank_mass_multiplicity_line_energy_ancestry_proved":1,"all_line_clean_large_load_rows_closed":0,"all_owner_support_rows_closed":0,"geometric_multiplicity_caps_globally_sufficient":0,"triple_free_response_policy_globally_available":0,"line_energy_profile_rows_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
