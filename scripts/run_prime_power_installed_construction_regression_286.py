#!/usr/bin/env python3
"""Run the installed 286-kind construction checker stack."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class ConstructionRegression286Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise ConstructionRegression286Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

BASE_CHAINED_MANIFEST_SHA256="fdad5ad0e23bd87f4b3f00d736ef70435b6d117e6822b4dc79f5a24557cea315"
BASE_MANIFEST_COUNT=43
MANIFEST_EXTENSION=[
 ("scripts/check_prime_power_scc_branch_minimum_face_ancestry.py","3ec89baac0450290c3dbe3a340af76aaea95bf7f4c84342a9aac8f7c31862498","scc_branch_minimum_face_ancestry_proved"),
 ("scripts/check_prime_power_installed_operation_registry_286.py","46f989ec87e87fb4a4bff9302bb5ca00a396d7e84861f9df6f0cab58bb6e38dc","installed_transition_kind_bank_286_exhaustive"),
]
EXPECTED_CHAINED_MANIFEST_SHA256="3b206d44e2c243f0d32e91b4cc15381afc9f8b2251af980c88ce6c221fdf1beb"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for c in (current,*current.parents):
        if (c/'STATUS.md').is_file() and (c/'scripts').is_dir(): return c
    raise ConstructionRegression286Error('unable to locate repository root')

def load_module(path:Path,name:str)->Any:
    require(path.is_file(),f'{path.name}: missing')
    spec=importlib.util.spec_from_file_location(name,path); require(spec is not None and spec.loader is not None,f'{path.name}: import spec')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def load_base_manifest(root:Path)->list[tuple[str,str,str]]:
    runner=load_module(root/'scripts/run_prime_power_installed_construction_regression_239.py','installed_regression_239')
    require(runner.EXPECTED_CHAINED_MANIFEST_SHA256==BASE_CHAINED_MANIFEST_SHA256,'base 239-kind chained seal')
    manifest=[*runner.load_base_manifest(root),*runner.MANIFEST_EXTENSION]
    runner.validate_manifest(manifest)
    require(len(manifest)==BASE_MANIFEST_COUNT,'base forty-three-checker count')
    return manifest

def validate_manifest(manifest:list[tuple[str,str,str]])->None:
    require(digest({'base_chained_manifest_sha256':BASE_CHAINED_MANIFEST_SHA256,'extension':MANIFEST_EXTENSION})==EXPECTED_CHAINED_MANIFEST_SHA256,'chained manifest digest mismatch')
    require(len(manifest)==BASE_MANIFEST_COUNT+len(MANIFEST_EXTENSION),'forty-five-checker manifest required')
    paths=set(); flags=set()
    for i,item in enumerate(manifest):
        require(isinstance(item,tuple) and len(item)==3,f'manifest[{i}]: tuple required')
        path,contract,flag=item
        require(path.startswith('scripts/check_prime_power_') and path.endswith('.py'),f'manifest[{i}]: checker path')
        require(path not in paths,f'manifest[{i}]: duplicate path'); paths.add(path)
        require(len(contract)==64 and all(ch in '0123456789abcdef' for ch in contract),f'manifest[{i}]: contract')
        require(flag and flag not in flags,f'manifest[{i}]: flag'); flags.add(flag)

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
    except json.JSONDecodeError as exc: raise ConstructionRegression286Error(f'{path}: invalid JSON report') from exc
    require(isinstance(report,dict),f'{path}: JSON object required')
    require(contract_from(report)==contract,f'{path}: contract mismatch')
    require(report.get(flag)==1,f'{path}: expected {flag}=1')
    require(report.get('all_n_proved_by_checker')==0,f'{path}: honesty flag')
    return {'path':path,'contract':contract,'expected_flag':flag,'all_n_proved_by_checker':0}

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--static-only',action='store_true'); args=parser.parse_args()
    root=repository_root(); manifest=[*load_base_manifest(root),*MANIFEST_EXTENSION]; validate_manifest(manifest)
    results=[audit(root,item,execute=not args.static_only) for item in manifest]
    print(json.dumps({'checker':'prime-power-installed-construction-regression-286','base_chained_manifest_sha256':BASE_CHAINED_MANIFEST_SHA256,
                      'manifest_extension':MANIFEST_EXTENSION,'chained_manifest_sha256':EXPECTED_CHAINED_MANIFEST_SHA256,
                      'installed_checker_count':len(manifest),'executed_checker_count':0 if args.static_only else len(manifest),
                      'static_only':int(args.static_only),'results':results,'installed_transition_regression_286_complete':1,
                      'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
                      'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0},sort_keys=True))
if __name__=='__main__':main()
