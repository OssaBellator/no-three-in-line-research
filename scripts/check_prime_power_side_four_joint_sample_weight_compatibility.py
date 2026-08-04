#!/usr/bin/env python3
"""Validate exact joint weight namespace and local compatibility for two side-four samples."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

class JointSampleWeightError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise JointSampleWeightError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ZERO_WEIGHT_PATH="data/prime_power_side_four_sample_weight_feasibility_contract.json"
BLOCKER_WEIGHT_PATH="data/prime_power_side_four_blocker_sample_weight_feasibility_contract.json"
ZERO_ROUTING_PATH="data/prime_power_side_four_sample_credit_routing_contract.json"
BLOCKER_ROUTING_PATH="data/prime_power_side_four_blocker_sample_credit_routing_contract.json"
JOINT_PATH="data/prime_power_side_four_joint_sample_weight_compatibility_contract.json"
ZERO_CHECKER_PATH="scripts/check_prime_power_side_four_sample_weight_feasibility.py"
BLOCKER_CHECKER_PATH="scripts/check_prime_power_side_four_blocker_sample_weight_feasibility.py"
EXPECTED_ZERO_WEIGHT_SHA256="d85580884ba95d368350ee1230890e4b54b86c33466c55fb20cb837de46b7316"
EXPECTED_BLOCKER_WEIGHT_SHA256="f879314c3ab11b96e3fc09df0c5f540cde441055c6af00f631c4cbbee4deafb5"
EXPECTED_JOINT_SHA256="1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise JointSampleWeightError("unable to locate repository root")

def load_module(path: Path,name: str)->Any:
    require(path.is_file(),f"{name}: checker missing")
    spec=importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,f"{name}: import")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def fraction(value: list[int])->Fraction:
    require(isinstance(value,list) and len(value)==2 and all(isinstance(x,int) for x in value) and value[1]>0,"rational encoding")
    return Fraction(value[0],value[1])

def expected_bindings(zero_routing: dict[str,Any],blocker_routing: dict[str,Any])->list[dict[str,str]]:
    zero_symbols=["w_zero_return_00_rank1","w_zero_return_22_rank1","w_zero_return_22_rank2"]
    blocker_symbols=["w_blocker_return_00_rank1","w_blocker_return_11_rank1","w_blocker_return_11_rank2","w_blocker_return_33_rank3"]
    result=[]
    for scope,routing,symbols in (("zero",zero_routing,zero_symbols),("blocker",blocker_routing,blocker_symbols)):
        classes=routing["compressed_child_classes"]
        require(len(classes)==len(symbols),f"{scope}: class count")
        for item,joint_symbol in zip(classes,symbols):
            result.append({"scope":scope,"local_alias":item["weight_symbol"],"class_id":item["class_id"],"joint_symbol":joint_symbol})
    return result

def validate(root: Path,contract: dict[str,Any])->None:
    zero_checker=load_module(root/ZERO_CHECKER_PATH,"zero_weight_checker")
    blocker_checker=load_module(root/BLOCKER_CHECKER_PATH,"blocker_weight_checker")
    zero_weight=json.loads((root/ZERO_WEIGHT_PATH).read_text(encoding="utf-8"))
    blocker_weight=json.loads((root/BLOCKER_WEIGHT_PATH).read_text(encoding="utf-8"))
    zero_checker.validate(root,zero_weight);blocker_checker.validate(root,blocker_weight)
    require(zero_checker.EXPECTED_WEIGHT_SHA256==EXPECTED_ZERO_WEIGHT_SHA256,"zero weight binding")
    require(blocker_checker.EXPECTED_WEIGHT_SHA256==EXPECTED_BLOCKER_WEIGHT_SHA256,"blocker weight binding")
    require(contract["zero_weight_contract_sha256"]==EXPECTED_ZERO_WEIGHT_SHA256,"zero contract seal")
    require(contract["blocker_weight_contract_sha256"]==EXPECTED_BLOCKER_WEIGHT_SHA256,"blocker contract seal")
    require(digest(contract)==EXPECTED_JOINT_SHA256,"joint contract digest")
    zero_routing=json.loads((root/ZERO_ROUTING_PATH).read_text(encoding="utf-8"))
    blocker_routing=json.loads((root/BLOCKER_ROUTING_PATH).read_text(encoding="utf-8"))
    bindings=expected_bindings(zero_routing,blocker_routing)
    require(contract["class_bindings"]==bindings,"exact class bindings")
    require(len({item["class_id"] for item in bindings})==7,"seven exact classes")
    aliases=Counter(item["local_alias"] for item in bindings)
    require(aliases==Counter({"w_return_00_rank1":2,"w_return_22_rank1":1,"w_return_22_rank2":1,"w_return_11_rank1":1,"w_return_11_rank2":1,"w_return_33_rank3":1}),"alias census")
    require(contract["alias_audit"]=={
        "local_alias_count":6,"exact_child_class_count":7,
        "colliding_aliases":{"w_return_00_rank1":["w_zero_return_00_rank1","w_blocker_return_00_rank1"]},
        "rule":"local aliases may be reused only inside their scoped contracts; joint or global bindings use exact child classes"},"alias audit")
    joint_symbol={(item["scope"],item["local_alias"]):item["joint_symbol"] for item in bindings}
    expected_zero=[[joint_symbol[("zero",alias)],coef] for alias,coef in zero_weight["return_row"]["terms"]]
    expected_blocker=[[joint_symbol[("blocker",alias)],coef] for alias,coef in blocker_weight["return_row"]["terms"]]
    require(contract["joint_rows"]=={
        "zero":{"parent_symbol":"w_parent_zero_sample","terms":expected_zero},
        "blocker":{"parent_symbol":"w_parent_blocker_sample","terms":expected_blocker}},"joint rows")
    witness=contract["explicit_joint_local_witness"];weights=witness["child_weights"];parents=witness["parent_weights"]
    require(set(weights)=={item["joint_symbol"] for item in bindings} and all(value==1 for value in weights.values()),"joint child witness")
    require(parents=={"w_parent_zero_sample":16,"w_parent_blocker_sample":16},"joint parent witness")
    totals={row:sum(coef*weights[symbol] for symbol,coef in contract["joint_rows"][row]["terms"]) for row in ("zero","blocker")}
    require(totals==witness["weighted_totals"]=={"zero":4,"blocker":5},"joint totals")
    require({"zero":16-totals["zero"],"blocker":16-totals["blocker"]}==witness["strict_slacks"]=={"zero":12,"blocker":11},"joint slacks")
    child=fraction(witness["normalized_child_weight"]);require(child==Fraction(1,16),"normalized child")
    require(fraction(witness["normalized_weighted_totals"]["zero"])==Fraction(1,4) and fraction(witness["normalized_weighted_totals"]["blocker"])==Fraction(5,16),"normalized totals")
    require(fraction(witness["normalized_strict_slacks"]["zero"])==Fraction(3,4) and fraction(witness["normalized_strict_slacks"]["blocker"])==Fraction(11,16),"normalized slacks")
    residual=contract["residual_bindings"]
    require(len(residual)==16 and len({item["name"] for item in residual})==16 and all(item["status"]=="unresolved" for item in residual),"residual bindings")
    require(contract["aggregate"]=={
        "sample_rows":2,"exact_child_classes":7,"local_aliases":6,"colliding_aliases":1,
        "joint_parent_weights":2,"joint_child_weights":7,"zero_weighted_total":4,
        "blocker_weighted_total":5,"zero_strict_slack":12,"blocker_strict_slack":11,
        "residual_binding_records":16},"aggregate")
    require(contract["honesty"]=={
        "joint_sample_exact_weight_namespace_complete":1,
        "joint_sample_local_positive_assignment_complete":1,
        "joint_sample_return_only_rows_strict_under_local_witness":1,
        "joint_sample_global_weight_bindings_complete":0,
        "joint_sample_full_compulsory_rows_complete":0,
        "joint_sample_global_recurrent_compatibility_proved":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},"honesty")

def mutation_audit(root: Path,contract: dict[str,Any])->int:
    mutations=[
        lambda x:x["class_bindings"][3].update(joint_symbol="w_zero_return_00_rank1"),
        lambda x:x["class_bindings"][3].update(class_id=x["class_bindings"][0]["class_id"]),
        lambda x:x["alias_audit"].update(exact_child_class_count=6),
        lambda x:x["alias_audit"]["colliding_aliases"].clear(),
        lambda x:x["joint_rows"]["zero"]["terms"].pop(),
        lambda x:x["explicit_joint_local_witness"]["parent_weights"].update(w_parent_zero_sample=4),
        lambda x:x["explicit_joint_local_witness"]["child_weights"].update(w_blocker_return_33_rank3=0),
        lambda x:x["explicit_joint_local_witness"]["weighted_totals"].update(blocker=4),
        lambda x:x["explicit_joint_local_witness"]["normalized_child_weight"].__setitem__(1,8),
        lambda x:x["residual_bindings"].pop(),
        lambda x:x["residual_bindings"][0].update(status="resolved"),
        lambda x:x["honesty"].update(joint_sample_global_weight_bindings_complete=1),
        lambda x:x["honesty"].update(joint_sample_full_compulsory_rows_complete=1),
        lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(contract);mutate(bad)
        try:validate(root,bad)
        except JointSampleWeightError:rejected+=1
    require(rejected==len(mutations),"joint corruption accepted")
    return rejected

def main()->None:
    root=repository_root();contract=json.loads((root/JOINT_PATH).read_text(encoding="utf-8"))
    validate(root,contract)
    print(json.dumps({
        "checker":"prime-power-side-four-joint-sample-weight-compatibility",
        "joint_contract_sha256":EXPECTED_JOINT_SHA256,
        "exact_child_class_count":7,"colliding_alias_count":1,
        "zero_strict_slack":12,"blocker_strict_slack":11,
        "residual_binding_record_count":16,"rejected_corruptions":mutation_audit(root,contract),
        "joint_sample_exact_weight_namespace_complete":1,
        "joint_sample_local_positive_assignment_complete":1,
        "joint_sample_return_only_rows_strict_under_local_witness":1,
        "joint_sample_global_weight_bindings_complete":0,
        "joint_sample_full_compulsory_rows_complete":0,
        "joint_sample_global_recurrent_compatibility_proved":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__":main()
