#!/usr/bin/env python3
"""Execute geometric-fibre and unified outer-assignment ancestry for CMR1774--CMR1829."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class GeometricFibreOuterAssignmentError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise GeometricFibreOuterAssignmentError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SOURCE_FILES=["docs/325-prime-power-geometric-orbit-fibre-correction.md","docs/326-prime-power-line-energy-marginal-rook-compiler.md","docs/327-prime-power-nested-assignment-line-energy-certificates.md","docs/328-prime-power-geometric-fibre-host-census-and-line-caps.md","docs/329-prime-power-exact-rank-three-geometric-fibre-census.md","docs/330-prime-power-line-occupancy-capacity-certificate.md","docs/331-prime-power-unified-outer-assignment-response-score.md"]
VERIFIER_FILES=["scripts/verify_prime_power_geometric_orbit_fibre_correction.py","scripts/verify_prime_power_line_energy_marginal_rook_compiler.py","scripts/verify_prime_power_nested_assignment_line_energy.py","scripts/verify_prime_power_geometric_fibre_host_census.py","scripts/verify_prime_power_exact_rank_three_geometric_fibre_census.py","scripts/verify_prime_power_line_occupancy_capacity.py","scripts/verify_prime_power_unified_outer_assignment_response.py"]
CONTRACT={"schema":"prime-power-geometric-fibre-outer-assignment-ancestry/v1","source_range":["CMR1774","CMR1829"],"source_files":SOURCE_FILES,"verifier_files":VERIFIER_FILES,"checked_layers":["geometric orbit-fibre correction and honest fibre upper quotients","exact marginal and nested-assignment line-energy certificates","coordinate-labelled side-four/five host and rank-three censuses","line-occupancy assignment capacities for all geometric ranks","unified outer return-selector-geometric assignment scores"],"honesty_flags":{"geometric_fibre_rows_complete_all_provenance":0,"rank_one_two_geometric_fibre_rows_subcritical":0,"unified_outer_assignment_globally_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_SHA256="f03ab61fabb4ad8727f239a31474466f3074f2397762a63fd4255c683176e3eb"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise GeometricFibreOuterAssignmentError("unable to locate repository root")

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def execute_verifier(root: Path,relative_path: str)->dict[str,Any]:
    path=root/relative_path; require(path.is_file(),f"{relative_path}: missing verifier"); compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip(); require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any])->None:
    require(fixture.get("source_file_count")==7,"fixture source count"); require(fixture.get("verifier_file_count")==7,"fixture verifier count")
    for key in ("geometric_orbit_fibre_correction_exact","line_energy_marginal_rook_exact","nested_assignment_line_energy_exact","geometric_fibre_host_census_exact","rank_three_geometric_fibre_census_exact","line_occupancy_capacity_exact","unified_outer_assignment_exact"): require(fixture.get(key)==1,f"fixture {key}")
    for key in ("geometric_fibre_rows_complete_all_provenance","unified_outer_assignment_globally_strict","all_labelled_recurrent_blocks_subcritical","all_n_proved_by_checker"): require(fixture.get(key)==0,f"fixture honesty {key}")

def mutation_audit()->int:
    fixture={"source_file_count":7,"verifier_file_count":7,"geometric_orbit_fibre_correction_exact":1,"line_energy_marginal_rook_exact":1,"nested_assignment_line_energy_exact":1,"geometric_fibre_host_census_exact":1,"rank_three_geometric_fibre_census_exact":1,"line_occupancy_capacity_exact":1,"unified_outer_assignment_exact":1,"geometric_fibre_rows_complete_all_provenance":0,"unified_outer_assignment_globally_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"all_n_proved_by_checker":0}
    mutations=[lambda x:x.update(source_file_count=6),lambda x:x.update(verifier_file_count=6)]
    mutations += [lambda x,key=key:x.update({key:0}) for key in ("geometric_orbit_fibre_correction_exact","line_energy_marginal_rook_exact","nested_assignment_line_energy_exact","geometric_fibre_host_census_exact","rank_three_geometric_fibre_census_exact","line_occupancy_capacity_exact","unified_outer_assignment_exact")]
    mutations += [lambda x,key=key:x.update({key:1}) for key in ("geometric_fibre_rows_complete_all_provenance","unified_outer_assignment_globally_strict","all_labelled_recurrent_blocks_subcritical","all_n_proved_by_checker")]
    mutations.append(lambda x:x.clear()); rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except GeometricFibreOuterAssignmentError: rejected+=1
    require(rejected==len(mutations),"geometric fibre corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({"checker":"prime-power-geometric-fibre-outer-assignment-ancestry","contract_sha256":contract,"source_file_count":len(SOURCE_FILES),"verifier_file_count":len(VERIFIER_FILES),"verifier_reports":reports,"rejected_corruptions":mutation_audit(),"geometric_orbit_fibre_correction_exact":1,"line_energy_marginal_rook_exact":1,"nested_assignment_line_energy_exact":1,"geometric_fibre_host_census_exact":1,"rank_three_geometric_fibre_census_exact":1,"line_occupancy_capacity_exact":1,"unified_outer_assignment_exact":1,"geometric_fibre_outer_assignment_ancestry_proved":1,"geometric_fibre_rows_complete_all_provenance":0,"rank_one_two_geometric_fibre_rows_subcritical":0,"unified_outer_assignment_globally_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
