#!/usr/bin/env python3
"""Validate scoped weight feasibility for the side-four blocker sample."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path
from typing import Any

class BlockerSampleWeightError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise BlockerSampleWeightError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ROUTING_PATH="data/prime_power_side_four_blocker_sample_credit_routing_contract.json"
WEIGHT_PATH="data/prime_power_side_four_blocker_sample_weight_feasibility_contract.json"
ROUTING_CHECKER_PATH="scripts/check_prime_power_side_four_blocker_sample_credit_routing.py"
EXPECTED_ROUTING_SHA256="4b8da717b59a47d8c5f1d4db1308e934c26390804611b0906c81c30cce136aa5"
EXPECTED_WEIGHT_SHA256="f879314c3ab11b96e3fc09df0c5f540cde441055c6af00f631c4cbbee4deafb5"
RESIDUAL_NAMES={
"parent_state_key","parent_global_weight_binding","w_return_00_rank1_global_binding",
"w_return_11_rank1_global_binding","w_return_11_rank2_global_binding",
"w_return_33_rank3_global_binding","selector_coefficient_and_child_binding",
"collision_coefficient_and_child_binding","interface_coefficient_and_child_binding",
"global_recurrent_block_compatibility"}

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise BlockerSampleWeightError("unable to locate repository root")

def load_module(path: Path)->Any:
    require(path.is_file(),"routing checker missing")
    spec=importlib.util.spec_from_file_location("blocker_sample_routing",path)
    require(spec is not None and spec.loader is not None,"routing checker import")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def fraction(value: list[int])->Fraction:
    require(isinstance(value,list) and len(value)==2 and all(isinstance(x,int) for x in value) and value[1]>0,"rational encoding")
    return Fraction(value[0],value[1])

def validate(root: Path,contract: dict[str,Any])->None:
    routing_checker=load_module(root/ROUTING_CHECKER_PATH)
    routing=json.loads((root/ROUTING_PATH).read_text(encoding="utf-8"))
    routing_checker.validate(root,routing)
    require(routing_checker.EXPECTED_ROUTING_SHA256==EXPECTED_ROUTING_SHA256,"routing checker binding")
    require(contract["routing_contract_sha256"]==EXPECTED_ROUTING_SHA256,"routing binding")
    require(digest(contract)==EXPECTED_WEIGHT_SHA256,"weight digest")
    require(contract["scope"]=={
        "host_id":"s4-75b04c45c1c8eac2",
        "row_scope":"blocker-sample-return-only-local-feasibility",
        "global_recurrent_state_occurrence":"unproved",
        "global_weight_compatibility":"unproved"},"scope")
    terms=routing["weighted_return_expression"]["terms"]
    require(contract["return_row"]["terms"]==terms,"return terms")
    witness=contract["explicit_local_witness"];weights=witness["child_weights"]
    require(set(weights)=={symbol for symbol,_ in terms} and all(isinstance(x,int) and x>0 for x in weights.values()),"positive child weights")
    parent=witness["parent_weight"];require(isinstance(parent,int) and parent>0,"positive parent")
    total=sum(coef*weights[symbol] for symbol,coef in terms)
    require(total==witness["weighted_child_total"]==5,"weighted total")
    require(parent-total==witness["strict_slack"]==5 and total<parent,"strict local row")
    normalized={symbol:fraction(value) for symbol,value in witness["normalized_child_weights"].items()}
    require(fraction(witness["normalized_parent_weight"])==1,"normalized parent")
    require(normalized=={symbol:Fraction(weights[symbol],parent) for symbol in weights},"normalized children")
    normalized_total=sum(coef*normalized[symbol] for symbol,coef in terms)
    require(normalized_total==fraction(witness["normalized_weighted_child_total"])==Fraction(1,2),"normalized total")
    require(1-normalized_total==fraction(witness["normalized_strict_slack"])==Fraction(1,2),"normalized slack")
    accounting=contract["category_accounting"]
    require(accounting["return"]=="locally-weighted-under-explicit-witness","return accounting")
    require(accounting["line"]=="certificate-source-only-no-second-offspring-charge","line accounting")
    require(accounting["geometric"]=="rank-three-certificate-source-only-no-second-offspring-charge","geometric accounting")
    require(all(accounting[key]=="unresolved-not-zero" for key in ("selector","collision","interface")),"remaining categories")
    residual=contract["residual_bindings"]
    require(len(residual)==10 and {item["name"] for item in residual}==RESIDUAL_NAMES,"residual bindings")
    require(all(item["status"]=="unresolved" for item in residual),"residual honesty")
    require(contract["aggregate"]=={
        "return_child_classes":4,"return_coefficient_mass":5,"local_parent_weight":10,
        "local_weighted_child_total":5,"local_strict_slack":5,
        "unresolved_global_weight_bindings":5,"unresolved_compulsory_categories":3,
        "residual_binding_records":10},"aggregate")
    require(contract["honesty"]=={
        "blocker_sample_return_only_weight_feasibility_proved":1,
        "blocker_sample_return_only_local_witness_complete":1,
        "blocker_sample_global_weight_bindings_complete":0,
        "blocker_sample_full_compulsory_row_complete":0,
        "blocker_sample_weighted_row_strict":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},"honesty")

def mutation_audit(root: Path,contract: dict[str,Any])->int:
    mutations=[
        lambda x:x["return_row"]["terms"].pop(),
        lambda x:x["explicit_local_witness"].update(parent_weight=5),
        lambda x:x["explicit_local_witness"]["child_weights"].update(w_return_33_rank3=0),
        lambda x:x["explicit_local_witness"].update(weighted_child_total=4),
        lambda x:x["explicit_local_witness"].update(strict_slack=6),
        lambda x:x["explicit_local_witness"]["normalized_child_weights"].update(w_return_11_rank2=[1,5]),
        lambda x:x["category_accounting"].update(geometric="offspring-charge"),
        lambda x:x["category_accounting"].update(collision="zero"),
        lambda x:x["residual_bindings"].pop(),
        lambda x:x["residual_bindings"][0].update(status="resolved"),
        lambda x:x["honesty"].update(blocker_sample_weighted_row_strict=1),
        lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(contract);mutate(bad)
        try:validate(root,bad)
        except BlockerSampleWeightError:rejected+=1
    require(rejected==len(mutations),"weight corruption accepted")
    return rejected

def main()->None:
    root=repository_root();contract=json.loads((root/WEIGHT_PATH).read_text(encoding="utf-8"))
    validate(root,contract)
    print(json.dumps({
        "checker":"prime-power-side-four-blocker-sample-weight-feasibility",
        "routing_contract_sha256":EXPECTED_ROUTING_SHA256,
        "weight_contract_sha256":EXPECTED_WEIGHT_SHA256,
        "local_parent_weight":10,"local_weighted_child_total":5,"local_strict_slack":5,
        "residual_binding_record_count":10,"rejected_corruptions":mutation_audit(root,contract),
        "blocker_sample_return_only_weight_feasibility_proved":1,
        "blocker_sample_return_only_local_witness_complete":1,
        "blocker_sample_global_weight_bindings_complete":0,
        "blocker_sample_full_compulsory_row_complete":0,
        "blocker_sample_weighted_row_strict":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__":main()
