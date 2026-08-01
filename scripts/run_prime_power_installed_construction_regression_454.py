#!/usr/bin/env python3
"""Run the installed 454-kind construction checker stack."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path
from typing import Any
class ConstructionRegression454Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise ConstructionRegression454Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
BASE_CHAINED_MANIFEST_SHA256='0a4e90217d3caaa06bb57f8458939e7cce2f9c68bd05ccddea2ea1c3149321bd'
BASE_MANIFEST_COUNT=49
MANIFEST_EXTENSION=[
 ('scripts/check_prime_power_selected_scheduler_terminal_wall_ancestry.py','f10e632f119fdd56a830ddeb8b9d15d18769f59e703d0dad7a59f243a7c8246c','selected_scheduler_terminal_wall_ancestry_proved'),
 ('scripts/check_prime_power_installed_operation_registry_454.py','63034b7d3af319de121a26ea863309808de0e3b06f0359448be9afed3e73f40f','installed_transition_kind_bank_454_exhaustive'),
]
EXPECTED_CHAINED_MANIFEST_SHA256='b5766866f7d04d687fcb56cf32d1f107be34c28fc34be1eae8b75039c269edbe'
def repository_root(start:Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/'STATUS.md').is_file() and (candidate/'scripts').is_dir(): return candidate
    raise ConstructionRegression454Error('unable to locate repository root')
def load_module(path:Path,name:str)->Any:
    require(path.is_file(),f'{path.name}: missing')
    spec=importlib.util.spec_from_file_location(name,path); require(spec is not None and spec.loader is not None,f'{path.name}: import spec')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module
def load_base_manifest(root:Path)->list[tuple[str,str,str]]:
    runner=load_module(root/'scripts/run_prime_power_installed_construction_regression_392.py','installed_regression_392')
    require(runner.EXPECTED_CHAINED_MANIFEST_SHA256==BASE_CHAINED_MANIFEST_SHA256,'base 392-kind chained seal')
    manifest=[*runner.load_base_manifest(root),*runner.MANIFEST_EXTENSION]; runner.validate_manifest(manifest)
    require(len(manifest)==BASE_MANIFEST_COUNT,'base forty-nine-checker count'); return manifest
def validate_manifest(manifest:list[tuple[str,str,str]])->None:
    require(digest({'base_chained_manifest_sha256':BASE_CHAINED_MANIFEST_SHA256,'extension':MANIFEST_EXTENSION})==EXPECTED_CHAINED_MANIFEST_SHA256,'chained manifest digest mismatch')
    require(len(manifest)==BASE_MANIFEST_COUNT+len(MANIFEST_EXTENSION),'fifty-one-checker manifest required')
    paths=set(); flags=set()
    for index,item in enumerate(manifest):
        require(isinstance(item,tuple) and len(item)==3,f'manifest[{index}]: tuple required')
        path,contract,flag=item
        require(path.startswith('scripts/check_prime_power_') and path.endswith('.py'),f'manifest[{index}]: checker path')
        require(path not in paths,f'manifest[{index}]: duplicate path'); paths.add(path)
        require(len(contract)==64 and all(char in '0123456789abcdef' for char in contract),f'manifest[{index}]: contract')
        require(flag and flag not in flags,f'manifest[{index}]: flag'); flags.add(flag)
def environment()->dict[str,str]:
    result=dict(os.environ); result.update({'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'}); return result
def contract_from(report:dict[str,Any])->Any:
    return report.get('contract_sha256',report.get('contract_digest'))
def audit(root:Path,item:tuple[str,str,str],execute:bool)->dict[str,Any]:
    path,contract,flag=item; checker=root/path
    require(checker.is_file(),f'{path}: checker missing'); compile(checker.read_text(encoding='utf-8'),str(checker),'exec')
    if not execute: return {'path':path,'contract':contract,'expected_flag':flag}
    completed=subprocess.run([sys.executable,str(checker)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f'{path} failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}')
    try: report=json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc: raise ConstructionRegression454Error(f'{path}: invalid JSON report') from exc
    require(isinstance(report,dict),f'{path}: JSON object required')
    require(contract_from(report)==contract,f'{path}: contract mismatch')
    require(report.get(flag)==1,f'{path}: expected {flag}=1')
    require(report.get('all_n_proved_by_checker')==0,f'{path}: honesty flag')
    return {'path':path,'contract':contract,'expected_flag':flag,'all_n_proved_by_checker':0}
def main()->None:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--static-only',action='store_true'); args=parser.parse_args()
    root=repository_root(); manifest=[*load_base_manifest(root),*MANIFEST_EXTENSION]; validate_manifest(manifest)
    results=[audit(root,item,execute=not args.static_only) for item in manifest]
    print(json.dumps({'checker':'prime-power-installed-construction-regression-454','base_chained_manifest_sha256':BASE_CHAINED_MANIFEST_SHA256,
      'manifest_extension':MANIFEST_EXTENSION,'chained_manifest_sha256':EXPECTED_CHAINED_MANIFEST_SHA256,
      'installed_checker_count':len(manifest),'executed_checker_count':0 if args.static_only else len(manifest),
      'static_only':int(args.static_only),'results':results,'installed_transition_regression_454_complete':1,
      'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
      'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0},sort_keys=True))
if __name__=='__main__': main()
