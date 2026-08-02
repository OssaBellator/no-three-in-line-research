#!/usr/bin/env python3
"""Run the installed 902-kind construction checker stack."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path
from typing import Any

class ConstructionRegression902Error(RuntimeError): pass
def require(ok: bool, message: str)->None:
    if not ok: raise ConstructionRegression902Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

BASE_CHAINED_MANIFEST_SHA256="9fe8e73ea57a7386c9c90d637d02037f5d96018ab904218f08f4fbec78446583"
BASE_MANIFEST_COUNT=67
MANIFEST_EXTENSION=[
("scripts/check_prime_power_superlevel_budget_thin_auxiliary_ancestry.py","e155ea311c24a9f04e1a603877190d1e60f9928a4607546635a9198344e53ad0","superlevel_budget_thin_auxiliary_ancestry_proved"),
("scripts/check_prime_power_installed_operation_registry_902.py","239245dca95e8a3936fd5700248af65f1534f706ac4aceccca7890c850a955ff","installed_transition_kind_bank_902_exhaustive"),
]
EXPECTED_CHAINED_MANIFEST_SHA256="f8ab06f6f46e08b91b425c10e53c55779e66be9acea6bbc0017d7216130f4857"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise ConstructionRegression902Error("unable to locate repository root")

def load_module(path: Path,name: str)->Any:
    require(path.is_file(),f"{path.name}: missing")
    spec=importlib.util.spec_from_file_location(name,path); require(spec is not None and spec.loader is not None,f"{path.name}: import spec")
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def load_base_manifest(root: Path)->list[tuple[str,str,str]]:
    runner=load_module(root/"scripts/run_prime_power_installed_construction_regression_830.py","installed_regression_830")
    require(runner.EXPECTED_CHAINED_MANIFEST_SHA256==BASE_CHAINED_MANIFEST_SHA256,"base 830-kind chained seal")
    manifest=[*runner.load_base_manifest(root),*runner.MANIFEST_EXTENSION]
    runner.validate_manifest(manifest)
    require(len(manifest)==BASE_MANIFEST_COUNT,"base sixty-seven-checker count")
    return manifest

def validate_manifest(manifest: list[tuple[str,str,str]])->None:
    require(digest({"base_chained_manifest_sha256":BASE_CHAINED_MANIFEST_SHA256,"extension":MANIFEST_EXTENSION})==EXPECTED_CHAINED_MANIFEST_SHA256,"chained manifest digest mismatch")
    require(len(manifest)==BASE_MANIFEST_COUNT+len(MANIFEST_EXTENSION),"sixty-nine-checker manifest required")
    paths=set(); flags=set()
    for index,item in enumerate(manifest):
        require(isinstance(item,tuple) and len(item)==3,f"manifest[{index}]: tuple required")
        path,contract,flag=item
        require(path.startswith("scripts/check_prime_power_") and path.endswith(".py"),f"manifest[{index}]: checker path")
        require(path not in paths,f"manifest[{index}]: duplicate path"); paths.add(path)
        require(len(contract)==64 and all(character in "0123456789abcdef" for character in contract),f"manifest[{index}]: contract")
        require(flag and flag not in flags,f"manifest[{index}]: flag"); flags.add(flag)

def environment()->dict[str,str]:
    result=dict(os.environ); result.update({"PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}); return result

def contract_from(report: dict[str,Any])->Any:
    return report.get("contract_sha256",report.get("contract_digest"))

def audit(root: Path,item: tuple[str,str,str],execute: bool)->dict[str,Any]:
    path,contract,flag=item; checker=root/path
    require(checker.is_file(),f"{path}: checker missing"); compile(checker.read_text(encoding="utf-8"),str(checker),"exec")
    if not execute: return {"path":path,"contract":contract,"expected_flag":flag}
    completed=subprocess.run([sys.executable,str(checker)],cwd=root,env=environment(),capture_output=True,text=True,check=False)
    require(completed.returncode==0,f"{path} failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    try: report=json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc: raise ConstructionRegression902Error(f"{path}: invalid JSON report") from exc
    require(isinstance(report,dict),f"{path}: JSON object required")
    require(contract_from(report)==contract,f"{path}: contract mismatch")
    require(report.get(flag)==1,f"{path}: expected {flag}=1")
    require(report.get("all_n_proved_by_checker")==0,f"{path}: honesty flag")
    for honesty in ("return_superlevel_cover_globally_strict","universal_line_clean_budgets_close_all_classes","selector_capacity_classes_closed","normalized_thin_geometric_rows_subcritical","auxiliary_effective_core_subcritical","same_owner_diagonal_blocks_subcritical","global_target_collateral_inequality_proved"):
        if honesty in report: require(report.get(honesty)==0,f"{path}: {honesty} honesty")
    return {"path":path,"contract":contract,"expected_flag":flag,"all_n_proved_by_checker":0}

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--static-only",action="store_true"); args=parser.parse_args()
    root=repository_root(); manifest=[*load_base_manifest(root),*MANIFEST_EXTENSION]; validate_manifest(manifest)
    results=[audit(root,item,execute=not args.static_only) for item in manifest]
    print(json.dumps({"checker":"prime-power-installed-construction-regression-902","base_chained_manifest_sha256":BASE_CHAINED_MANIFEST_SHA256,"manifest_extension":MANIFEST_EXTENSION,"chained_manifest_sha256":EXPECTED_CHAINED_MANIFEST_SHA256,"installed_checker_count":len(manifest),"executed_checker_count":0 if args.static_only else len(manifest),"static_only":int(args.static_only),"results":results,"installed_transition_regression_902_complete":1,"return_superlevel_cover_globally_strict":0,"universal_line_clean_budgets_close_all_classes":0,"selector_capacity_classes_closed":0,"normalized_thin_geometric_rows_subcritical":0,"auxiliary_effective_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
