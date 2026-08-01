#!/usr/bin/env python3
"""Run the installed one-hundred-thirty-two-kind construction checker stack."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class ConstructionRegression132Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise ConstructionRegression132Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

BASE_CHAINED_MANIFEST_SHA256="d259fb78a7b8a2ccbf7387c3fdd7a780b1e21f0366179c08af5ebb068cda3507"
BASE_MANIFEST_COUNT=34
MANIFEST_EXTENSION=[
 ("scripts/check_prime_power_protected_interface_execution_ancestry.py","59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f","protected_interface_execution_ancestry_proved"),
 ("scripts/check_prime_power_installed_operation_registry_132.py","833bb6751b69002613c0442f3f1b4180b6c02044361017e4e1e713ec2ea9b298","installed_transition_kind_bank_132_exhaustive"),
]
EXPECTED_CHAINED_MANIFEST_SHA256="260cc38054f3ecfede323d6057bbbecad46bb191e90410b6a4523479cc6b696d"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve(); current=current.parent if current.is_file() else current
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise ConstructionRegression132Error("unable to locate repository root")

def load_module(path:Path,name:str)->Any:
    require(path.is_file(),f"{path.name}: missing"); spec=importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,f"{path.name}: import spec")
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def load_base_manifest(root:Path)->list[tuple[str,str,str]]:
    runner=load_module(root/"scripts/run_prime_power_installed_construction_regression_117.py","installed_regression_117")
    require(runner.EXPECTED_CHAINED_MANIFEST_SHA256==BASE_CHAINED_MANIFEST_SHA256,"base 117-kind chained seal")
    manifest=[*runner.load_base_manifest(root),*runner.MANIFEST_EXTENSION]; runner.validate_manifest(manifest)
    require(len(manifest)==BASE_MANIFEST_COUNT,"base thirty-four-checker count"); return manifest

def validate_manifest(manifest:list[tuple[str,str,str]])->None:
    require(digest({"base_chained_manifest_sha256":BASE_CHAINED_MANIFEST_SHA256,"extension":MANIFEST_EXTENSION})==EXPECTED_CHAINED_MANIFEST_SHA256,"chained manifest digest mismatch")
    require(len(manifest)==36,"thirty-six-checker manifest required")
    paths:set[str]=set(); flags:set[str]=set()
    for i,item in enumerate(manifest):
        require(isinstance(item,tuple) and len(item)==3,f"manifest[{i}]: tuple")
        path,contract,flag=item; require(path.startswith("scripts/check_prime_power_") and path.endswith(".py"),f"manifest[{i}]: path")
        require(path not in paths,f"manifest[{i}]: duplicate path"); paths.add(path)
        require(len(contract)==64 and all(c in "0123456789abcdef" for c in contract),f"manifest[{i}]: contract")
        require(flag and flag not in flags,f"manifest[{i}]: flag"); flags.add(flag)

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result
def contract_from(report:dict[str,Any])->Any: return report.get("contract_sha256",report.get("contract_digest"))
def audit(root:Path,item:tuple[str,str,str],execute:bool)->dict[str,Any]:
    path,contract,flag=item; checker=root/path; require(checker.is_file(),f"{path}: missing")
    compile(checker.read_text(encoding="utf-8"),str(checker),"exec")
    if not execute: return {"path":path,"contract":contract,"expected_flag":flag}
    completed=subprocess.run([sys.executable,str(checker)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{path} failed\n{completed.stdout}\n{completed.stderr}")
    try: report=json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc: raise ConstructionRegression132Error(f"{path}: invalid JSON") from exc
    require(isinstance(report,dict),f"{path}: object"); require(contract_from(report)==contract,f"{path}: contract")
    require(report.get(flag)==1,f"{path}: flag"); require(report.get("all_n_proved_by_checker")==0,f"{path}: honesty")
    return {"path":path,"contract":contract,"expected_flag":flag,"all_n_proved_by_checker":0}

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--static-only",action="store_true"); args=parser.parse_args()
    root=repository_root(); manifest=[*load_base_manifest(root),*MANIFEST_EXTENSION]; validate_manifest(manifest)
    results=[audit(root,item,execute=not args.static_only) for item in manifest]
    report={"checker":"prime-power-installed-construction-regression-132","base_chained_manifest_sha256":BASE_CHAINED_MANIFEST_SHA256,"manifest_extension":MANIFEST_EXTENSION,"chained_manifest_sha256":EXPECTED_CHAINED_MANIFEST_SHA256,"installed_checker_count":len(manifest),"executed_checker_count":0 if args.static_only else len(manifest),"static_only":int(args.static_only),"results":results,"installed_transition_regression_132_complete":1,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__": main()
