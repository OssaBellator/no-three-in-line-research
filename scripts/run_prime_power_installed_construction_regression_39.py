#!/usr/bin/env python3
"""Run the installed thirty-nine-kind construction checker stack."""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
from typing import Any

class ConstructionRegression39Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise ConstructionRegression39Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
EXPECTED_MANIFEST_SHA256="73694657de93b3b1873f98cbf7a896dee629587641a945d3aa8ba6b76ddd3fee"
CHECKER_MANIFEST=[('scripts/check_prime_power_asymmetric_residual_host_contraction.py', 'fcc593f5812912d031ed90ab37e0fae105a35302a48b757f3fe69a7e80a0403b', 'asymmetric_residual_host_generated'), ('scripts/check_prime_power_asymmetric_context_generation.py', '8a12029b565cd8b9d51dba236f3cff782ed45ef3544fffd3ccddab8b0a32a0b9', 'asymmetric_context_family_generated'), ('scripts/check_prime_power_asymmetric_target_dispatch.py', '5e982b03f24ce4cd1230ede70563b49e3ac67976b0a84e038ae27b463e39fa83', 'local_asymmetric_candidate_response_complete'), ('scripts/check_prime_power_context_transition_registry.py', 'ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d', 'canonical_context_identity_sealed'), ('scripts/check_prime_power_routing_change_context_ancestry.py', 'b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360', 'routing_change_construction_ancestry_proved'), ('scripts/check_prime_power_routing_change_history_payment.py', 'b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259', 'routing_change_history_endpoint_exact'), ('scripts/check_prime_power_factor_child_product_ancestry.py', 'bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae', 'factor_product_construction_ancestry_proved'), ('scripts/check_prime_power_mixed_child_deletion_ancestry.py', 'b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429', 'mixed_atom_deletion_ancestry_proved'), ('scripts/check_prime_power_forced_certificate_escape_ancestry.py', 'dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253', 'forced_mixed_certificate_escape_proved'), ('scripts/check_prime_power_target_edge_return_ancestry.py', '04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382', 'returned_target_edge_ancestry_proved'), ('scripts/check_prime_power_target_handoff_envelope_ancestry.py', 'a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b', 'target_handoff_construction_ancestry_proved'), ('scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py', 'a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0', 'recurrent_target_edge_deletion_ancestry_proved'), ('scripts/check_prime_power_closure_envelope_transition_ancestry.py', '50b7720e03295dbde2557ab1d3a11dfc99a8f6d4a9528391555bc4e3adbf91c1', 'closure_branch_envelope_transition_bank_exhaustive'), ('scripts/check_prime_power_installed_owner_scheduler_bank.py', '108802c0d4934c7b3d77cc972d5418a2d8b91a6cca9da78b49bc4ab58970ad26', 'installed_transition_kind_bank_exhaustive'), ('scripts/check_prime_power_essential_return_unit_wall_ancestry.py', '97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5', 'essential_return_unit_wall_ancestry_proved'), ('scripts/check_prime_power_sparse_rollback_restoration_ancestry.py', '35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267', 'sparse_rollback_restoration_ancestry_proved'), ('scripts/check_prime_power_extended_installed_operation_registry.py', '4df61b20f4d3b2bad19a296a18e00f817ac1a20feda02b77f8486783bb561487', 'extended_installed_transition_kind_bank_exhaustive'), ('scripts/check_prime_power_rollback_optimal_face_scc_ancestry.py', '1281001711d4312dd98b8434e20dffb226b0608a893ffe5cf13f8b8e13940feb', 'rollback_minimum_cost_face_ancestry_proved'), ('scripts/check_prime_power_installed_operation_registry_33.py', '5f9d98c0b964f207fc4ac2d493b51fef5c3caaccf1464cf8bd351a477af93583', 'installed_transition_kind_bank_33_exhaustive'), ('scripts/check_prime_power_rollback_level_colour_cycle_ancestry.py', 'b97b2553cf5548cfc32a022172d2e011bc60952021d87178ae0e0fdc673ecc23', 'rollback_level_skeleton_ancestry_proved'), ('scripts/check_prime_power_installed_operation_registry_39.py', '92bea6f0961abd2c2c6799cd7171ff6c16a05e5cb37da9378ebe21545ace8437', 'installed_transition_kind_bank_39_exhaustive')]
def repository_root(start:Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/'STATUS.md').is_file() and (candidate/'scripts').is_dir(): return candidate
    raise ConstructionRegression39Error('unable to locate repository root')
def validate_manifest()->None:
    require(digest(CHECKER_MANIFEST)==EXPECTED_MANIFEST_SHA256,'twenty-one-checker manifest digest mismatch')
    paths=set();flags=set()
    for i,item in enumerate(CHECKER_MANIFEST):
        require(isinstance(item,tuple) and len(item)==3,f'manifest[{i}] tuple')
        path,contract,flag=item
        require(path.startswith('scripts/check_prime_power_') and path.endswith('.py'),f'manifest[{i}] path')
        require(path not in paths,f'manifest[{i}] duplicate path');paths.add(path)
        require(len(contract)==64 and all(c in '0123456789abcdef' for c in contract),f'manifest[{i}] contract')
        require(flag and flag not in flags,f'manifest[{i}] flag');flags.add(flag)
def environment():
    env=dict(os.environ);env.update({'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'});return env
def parse_report(stdout,path):
    text=stdout.strip();require(bool(text),f'{path}: empty stdout')
    try: report=json.loads(text)
    except json.JSONDecodeError as exc: raise ConstructionRegression39Error(f'{path}: invalid JSON: {exc}') from exc
    require(isinstance(report,dict),f'{path}: object required');return report
def contract_from(report): return report.get('contract_sha256',report.get('contract_digest'))
def audit(root,item,execute):
    path,contract,flag=item;checker=root/path
    require(checker.is_file(),f'{path}: missing');compile(checker.read_text(encoding='utf-8'),str(checker),'exec')
    if not execute:return {'path':path,'contract':contract,'expected_flag':flag}
    cp=subprocess.run([sys.executable,str(checker)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(cp.returncode==0,f'{path} failed\nstdout:\n{cp.stdout}\nstderr:\n{cp.stderr}')
    report=parse_report(cp.stdout,path);require(contract_from(report)==contract,f'{path}: contract mismatch')
    require(report.get(flag)==1,f'{path}: expected {flag}=1');require(report.get('all_n_proved_by_checker')==0,f'{path}: honesty')
    return {'path':path,'contract':contract,'expected_flag':flag,'all_n_proved_by_checker':0}
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--static-only',action='store_true');args=parser.parse_args()
    validate_manifest();root=repository_root();results=[audit(root,item,not args.static_only) for item in CHECKER_MANIFEST]
    report={'checker':'prime-power-installed-construction-regression-39','manifest_sha256':EXPECTED_MANIFEST_SHA256,'installed_checker_count':len(CHECKER_MANIFEST),'executed_checker_count':0 if args.static_only else len(CHECKER_MANIFEST),'static_only':int(args.static_only),'results':results,'installed_transition_regression_39_complete':1,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
