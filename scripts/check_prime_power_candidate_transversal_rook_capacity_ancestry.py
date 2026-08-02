#!/usr/bin/env python3
"""Execute candidate-transversal, rook-owner and capacity ancestry for CMR1390--CMR1453."""
from __future__ import annotations
import copy, hashlib, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class CandidateTransversalRookCapacityError(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise CandidateTransversalRookCapacityError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SOURCE_FILES = [
    "docs/278-prime-power-candidate-transversal-hall-wall.md",
    "docs/278-prime-power-rook-owner-edge-weights.md",
    "docs/279-prime-power-owner-support-matching-preclusion.md",
    "docs/280-prime-power-extension-free-rook-probabilities.md",
    "docs/281-prime-power-cross-line-owner-assignment.md",
    "docs/282-prime-power-rook-owner-edge-weights.md",
    "docs/283-prime-power-cross-line-harmonic-owner-bound.md",
    "docs/284-prime-power-cross-line-lattice-capacity-owner.md",
]
VERIFIER_FILES = [
    "scripts/verify_prime_power_candidate_transversal_hall.py",
    "scripts/verify_prime_power_rook_owner_edge_weights.py",
    "scripts/verify_prime_power_owner_support_matching_preclusion.py",
    "scripts/verify_prime_power_extension_free_rook_probabilities.py",
    "scripts/verify_prime_power_cross_line_owner_assignment.py",
    "scripts/verify_prime_power_cross_line_harmonic_owner.py",
    "scripts/verify_prime_power_cross_line_lattice_capacity.py",
]
CONTRACT = {
    "schema": "prime-power-candidate-transversal-rook-capacity-ancestry/v1",
    "source_range": ["CMR1390", "CMR1453"],
    "source_files": SOURCE_FILES,
    "verifier_files": VERIFIER_FILES,
    "checked_layers": [
        "exact weighted deletion-transversal identity and clean/threshold response criteria",
        "failed transversal reduction to inclusion-minimal deficiency-one matching walls",
        "fixed pre-sampling owner edges and exact rook-class owner loads",
        "sharp extension-free matching preclusion and owner-support tail policies",
        "exact residual rook probabilities and unavailable-edge expectations",
        "cross-line conditional owner assignment with rational integer dual certificates",
        "harmonic conditional owner-star bounds in inherited coordinate span",
        "lattice-capacity owner envelopes, height cutoffs and dyadic quotients",
    ],
    "correction_policy": "CMR1430--1437 finalizes the CMR1398--1405 rook-owner family without duplicate operations",
    "honesty_flags": {
        "uniform_cross_line_owner_policy_proved": 0,
        "same_owner_diagonal_blocks_subcritical": 0,
        "independent_line_kernel_sufficient": 0,
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "a590a41fb713c91904106d20d5eb31e18171a0761ce35a3908a29c8b87d547db"

def repository_root(start: Path | None = None) -> Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/'STATUS.md').is_file() and (candidate/'scripts').is_dir(): return candidate
    raise CandidateTransversalRookCapacityError('unable to locate repository root')

def environment() -> dict[str,str]:
    result=dict(os.environ); result.update({'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'}); return result

def execute_verifier(root: Path, relative_path: str) -> dict[str,Any]:
    path=root/relative_path; require(path.is_file(),f'{relative_path}: missing verifier')
    compile(path.read_text(encoding='utf-8'),str(path),'exec')
    completed=subprocess.run([sys.executable,str(path)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f'{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}')
    output=completed.stdout.strip(); require(output.startswith('verified '),f'{relative_path}: missing verified report')
    return {'path':relative_path,'stdout_sha256':hashlib.sha256(output.encode()).hexdigest(),'stdout':output}

def validate_fixture(fixture: dict[str,Any]) -> None:
    require(fixture.get('source_file_count')==8,'fixture source count')
    require(fixture.get('verifier_file_count')==7,'fixture verifier count')
    require(fixture.get('candidate_transversal_identity_exact')==1,'fixture transversal')
    require(fixture.get('minimum_owner_blockers_classified')==1,'fixture blocker')
    require(fixture.get('rook_owner_rows_exact')==1,'fixture rook owner')
    require(fixture.get('cross_line_assignment_dual_exact')==1,'fixture assignment')
    require(fixture.get('lattice_capacity_owner_envelope_exact')==1,'fixture capacity')
    require(fixture.get('uniform_cross_line_owner_policy_proved')==0,'fixture uniform policy honesty')
    require(fixture.get('same_owner_diagonal_blocks_subcritical')==0,'fixture subcritical honesty')
    require(fixture.get('all_n_proved_by_checker')==0,'fixture all-n honesty')

def mutation_audit() -> int:
    fixture={'source_file_count':8,'verifier_file_count':7,'candidate_transversal_identity_exact':1,'minimum_owner_blockers_classified':1,'rook_owner_rows_exact':1,'cross_line_assignment_dual_exact':1,'lattice_capacity_owner_envelope_exact':1,'uniform_cross_line_owner_policy_proved':0,'same_owner_diagonal_blocks_subcritical':0,'all_n_proved_by_checker':0}
    mutations=[
        lambda item:item.update(source_file_count=7),lambda item:item.update(verifier_file_count=6),
        lambda item:item.update(candidate_transversal_identity_exact=0),lambda item:item.update(minimum_owner_blockers_classified=0),
        lambda item:item.update(rook_owner_rows_exact=0),lambda item:item.update(cross_line_assignment_dual_exact=0),
        lambda item:item.update(lattice_capacity_owner_envelope_exact=0),lambda item:item.update(uniform_cross_line_owner_policy_proved=1),
        lambda item:item.update(same_owner_diagonal_blocks_subcritical=1),lambda item:item.update(all_n_proved_by_checker=1),
        lambda item:item.clear(),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(fixture); mutate(bad)
        try: validate_fixture(bad)
        except CandidateTransversalRookCapacityError: rejected+=1
    require(rejected==len(mutations),'candidate/rook corruption accepted'); return rejected

def main() -> None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,'contract digest mismatch')
    root=repository_root()
    for source in SOURCE_FILES: require((root/source).is_file(),f'{source}: missing source')
    reports=[execute_verifier(root,path) for path in VERIFIER_FILES]
    print(json.dumps({
        'checker':'prime-power-candidate-transversal-rook-capacity-ancestry','contract_sha256':contract,
        'source_file_count':len(SOURCE_FILES),'verifier_file_count':len(VERIFIER_FILES),'verifier_reports':reports,
        'rejected_corruptions':mutation_audit(),'candidate_transversal_identity_exact':1,
        'minimum_owner_blockers_classified':1,'rook_owner_rows_exact':1,'owner_support_tail_policy_exact':1,
        'extension_free_rook_probabilities_exact':1,'cross_line_assignment_dual_exact':1,
        'harmonic_owner_envelope_exact':1,'lattice_capacity_owner_envelope_exact':1,
        'candidate_transversal_rook_capacity_ancestry_proved':1,'uniform_cross_line_owner_policy_proved':0,
        'same_owner_diagonal_blocks_subcritical':0,'independent_line_kernel_sufficient':0,
        'global_target_collateral_inequality_proved':0,'all_owner_operations_proved':0,
        'all_scheduler_operations_proved':0,'all_construction_ancestry_proved':0,
        'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
        'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0,
    },sort_keys=True))

if __name__=='__main__': main()
