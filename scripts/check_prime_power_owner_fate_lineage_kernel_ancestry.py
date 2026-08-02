#!/usr/bin/env python3
"""Execute owner/fate, lineage and line-kernel ancestry for CMR1894--CMR1965."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class OwnerFateLineageKernelError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise OwnerFateLineageKernelError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SOURCE_FILES=["docs/340-prime-power-owner-fate-collision-class-compression.md","docs/341-prime-power-compulsory-weighted-assignment-certificates.md","docs/342-prime-power-slack-preconditioned-assignment-manifest.md","docs/343-prime-power-complete-line-energy-kernel.md","docs/344-prime-power-background-increment-line-energy-kernel.md","docs/345-prime-power-line-energy-selector-stability.md","docs/346-prime-power-background-normalized-line-energy-kernel.md","docs/347-prime-power-raw-fibre-background-lineage.md","docs/348-prime-power-rank-three-zero-response-blockers.md"]
VERIFIER_FILES=["scripts/verify_prime_power_owner_fate_class_compression.py","scripts/verify_prime_power_compulsory_weighted_assignment.py","scripts/verify_prime_power_slack_preconditioned_manifest.py","scripts/verify_prime_power_complete_line_energy_kernel.py","scripts/verify_prime_power_background_increment_kernel.py","scripts/verify_prime_power_line_energy_selector_stability.py","scripts/verify_prime_power_background_normalized_kernel.py","scripts/verify_prime_power_raw_fibre_background_lineage.py","scripts/verify_prime_power_rank_three_zero_response_blockers.py"]
CONTRACT={"schema":"prime-power-owner-fate-lineage-kernel-ancestry/v1","source_range":["CMR1894","CMR1965"],"source_files":SOURCE_FILES,"verifier_files":VERIFIER_FILES,"checked_layers":["exact owner fate collision class compression and compulsory weighted assignment certificates","slack-preconditioned executable manifests and complete line-energy kernels","background increment selector stability and background-normalized kernel identities","raw geometric fibre background lineage and exact rank-three zero-response blockers"],"honesty_flags":{"owner_fate_rows_populated_all_recurrent_states":0,"compulsory_weighted_certificates_complete":0,"raw_fibre_backgrounds_cover_all_provenance":0,"rank_three_zero_blockers_globally_resolved":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_SHA256="a81184108c06638fe3b44754b80c0fe271d8a92d7b78db6befb681890dd810eb"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise OwnerFateLineageKernelError("unable to locate repository root")

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def execute_verifier(root: Path,relative_path: str)->dict[str,Any]:
    path=root/relative_path; require(path.is_file(),f"{relative_path}: missing verifier"); compile(path.read_text(encoding="utf-8"),str(path),"exec")
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output=completed.stdout.strip(); require(output.startswith("verified "),f"{relative_path}: missing verified report")
    return {"path":relative_path,"stdout_sha256":hashlib.sha256(output.encode()).hexdigest(),"stdout":output}

def validate_fixture(fixture: dict[str,Any])->None:
    require(fixture.get("source_file_count")==9,"fixture source count"); require(fixture.get("verifier_file_count")==9,"fixture verifier count")
    for key in ("owner_fate_class_compression_exact","compulsory_weighted_assignment_exact","slack_preconditioned_manifest_exact","complete_line_energy_kernel_exact","background_increment_kernel_exact","selector_stability_exact","background_normalized_kernel_exact","raw_fibre_background_lineage_exact","rank_three_zero_response_blockers_exact"): require(fixture.get(key)==1,f"fixture {key}")
    for key in ("owner_fate_rows_populated_all_recurrent_states","compulsory_weighted_certificates_complete","raw_fibre_backgrounds_cover_all_provenance","rank_three_zero_blockers_globally_resolved","all_n_proved_by_checker"): require(fixture.get(key)==0,f"fixture honesty {key}")

def mutation_audit()->int:
    fixture={"source_file_count":9,"verifier_file_count":9,"owner_fate_class_compression_exact":1,"compulsory_weighted_assignment_exact":1,"slack_preconditioned_manifest_exact":1,"complete_line_energy_kernel_exact":1,"background_increment_kernel_exact":1,"selector_stability_exact":1,"background_normalized_kernel_exact":1,"raw_fibre_background_lineage_exact":1,"rank_three_zero_response_blockers_exact":1,"owner_fate_rows_populated_all_recurrent_states":0,"compulsory_weighted_certificates_complete":0,"raw_fibre_backgrounds_cover_all_provenance":0,"rank_three_zero_blockers_globally_resolved":0,"all_n_proved_by_checker":0}
    mutations=[lambda x:x.update(source_file_count=8),lambda x:x.update(verifier_file_count=8)]
    mutations += [lambda x,key=key:x.update({key:0}) for key in ("owner_fate_class_compression_exact","compulsory_weighted_assignment_exact","slack_preconditioned_manifest_exact","complete_line_energy_kernel_exact","background_increment_kernel_exact","selector_stability_exact","background_normalized_kernel_exact","raw_fibre_background_lineage_exact","rank_three_zero_response_blockers_exact")]
    mutations += [lambda x,key=key:x.update({key:1}) for key in ("owner_fate_rows_populated_all_recurrent_states","compulsory_weighted_certificates_complete","raw_fibre_backgrounds_cover_all_provenance","rank_three_zero_blockers_globally_resolved","all_n_proved_by_checker")]
    mutations.append(lambda x:x.clear()); rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except OwnerFateLineageKernelError: rejected+=1
    require(rejected==len(mutations),"owner/fate kernel corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,"contract digest mismatch")
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f"{source}: missing source")
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({"checker":"prime-power-owner-fate-lineage-kernel-ancestry","contract_sha256":contract,"source_file_count":len(SOURCE_FILES),"verifier_file_count":len(VERIFIER_FILES),"verifier_reports":reports,"rejected_corruptions":mutation_audit(),"owner_fate_class_compression_exact":1,"compulsory_weighted_assignment_exact":1,"slack_preconditioned_manifest_exact":1,"complete_line_energy_kernel_exact":1,"background_increment_kernel_exact":1,"selector_stability_exact":1,"background_normalized_kernel_exact":1,"raw_fibre_background_lineage_exact":1,"rank_three_zero_response_blockers_exact":1,"owner_fate_lineage_kernel_ancestry_proved":1,"owner_fate_rows_populated_all_recurrent_states":0,"compulsory_weighted_certificates_complete":0,"raw_fibre_backgrounds_cover_all_provenance":0,"rank_three_zero_blockers_globally_resolved":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
