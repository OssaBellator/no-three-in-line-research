#!/usr/bin/env python3
"""Validate scoped weight feasibility and residual bindings for the side-four sample."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from fractions import Fraction
from pathlib import Path
from typing import Any

class SampleWeightFeasibilityError(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise SampleWeightFeasibilityError(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SAMPLE_PATH="data/prime_power_side_four_actual_background_sample_batch.json"
ROUTING_PATH="data/prime_power_side_four_sample_credit_routing_contract.json"
WEIGHT_PATH="data/prime_power_side_four_sample_weight_feasibility_contract.json"
ROUTING_CHECKER_PATH="scripts/check_prime_power_side_four_sample_credit_routing.py"
EXPECTED_ROUTING_SHA256="f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5"
EXPECTED_WEIGHT_SHA256="d85580884ba95d368350ee1230890e4b54b86c33466c55fb20cb837de46b7316"
RESIDUAL_NAMES={
"parent_state_key","parent_global_weight_binding",
"w_return_00_rank1_global_binding","w_return_22_rank1_global_binding",
"w_return_22_rank2_global_binding","selector_coefficient_and_child_binding",
"collision_coefficient_and_child_binding","interface_coefficient_and_child_binding",
"global_recurrent_block_compatibility"}

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise SampleWeightFeasibilityError("unable to locate repository root")

def load_module(path: Path)->Any:
    require(path.is_file(),"routing checker missing")
    spec=importlib.util.spec_from_file_location("side_four_sample_routing",path)
    require(spec is not None and spec.loader is not None,"routing checker import")
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def fraction(value: list[int])->Fraction:
    require(isinstance(value,list) and len(value)==2 and all(isinstance(x,int) for x in value) and value[1]>0,"rational encoding")
    return Fraction(value[0],value[1])

def validate(root: Path, contract: dict[str,Any])->None:
    routing_checker=load_module(root/ROUTING_CHECKER_PATH)
    sample=json.loads((root/SAMPLE_PATH).read_text(encoding="utf-8"))
    routing=json.loads((root/ROUTING_PATH).read_text(encoding="utf-8"))
    routing_checker.validate(sample,routing)
    require(routing_checker.EXPECTED_ROUTING_SHA256==EXPECTED_ROUTING_SHA256,"routing checker binding")
    require(contract.get("routing_contract_sha256")==EXPECTED_ROUTING_SHA256,"routing contract binding")
    require(digest(contract)==EXPECTED_WEIGHT_SHA256,"weight contract digest")
    require(contract["scope"]=={
        "host_id":"s4-fc915f89dec31fec",
        "row_scope":"sample-return-only-local-feasibility",
        "global_recurrent_state_occurrence":"unproved",
        "global_weight_compatibility":"unproved"},"scope")
    terms=routing["weighted_return_expression"]["terms"]
    require(contract["return_row"]["terms"]==terms,"return term binding")
    witness=contract["explicit_local_witness"]; weights=witness["child_weights"]
    require(set(weights)=={symbol for symbol,_ in terms} and all(isinstance(x,int) and x>0 for x in weights.values()),"positive child weights")
    parent=witness["parent_weight"]; require(isinstance(parent,int) and parent>0,"positive parent weight")
    total=sum(coefficient*weights[symbol] for symbol,coefficient in terms)
    require(total==witness["weighted_child_total"]==4,"weighted child total")
    require(parent-total==witness["strict_slack"]==4 and total<parent,"strict local row")
    normalized={symbol:fraction(value) for symbol,value in witness["normalized_child_weights"].items()}
    require(fraction(witness["normalized_parent_weight"])==1,"normalized parent")
    require(normalized=={symbol:Fraction(weights[symbol],parent) for symbol in weights},"normalized children")
    normalized_total=sum(coefficient*normalized[symbol] for symbol,coefficient in terms)
    require(normalized_total==fraction(witness["normalized_weighted_child_total"])==Fraction(1,2),"normalized total")
    require(1-normalized_total==fraction(witness["normalized_strict_slack"])==Fraction(1,2),"normalized slack")
    accounting=contract["category_accounting"]
    require(accounting["return"]=="locally-weighted-under-explicit-witness","return accounting")
    require(accounting["line"]=="certificate-source-only-no-second-offspring-charge","line accounting")
    require(accounting["geometric"]=="known-zero-for-selected-response","geometric accounting")
    require(all(accounting[key]=="unresolved-not-zero" for key in ("selector","collision","interface")),"unresolved categories")
    residual=contract["residual_bindings"]
    require(len(residual)==9 and {item["name"] for item in residual}==RESIDUAL_NAMES,"residual bindings")
    require(all(item["status"]=="unresolved" for item in residual),"residual honesty")
    require(contract["aggregate"]=={
        "return_child_classes":3,"return_coefficient_mass":4,
        "local_parent_weight":8,"local_weighted_child_total":4,"local_strict_slack":4,
        "unresolved_global_weight_bindings":4,"unresolved_compulsory_categories":3,
        "residual_binding_records":9},"aggregate")
    require(contract["honesty"]=={
        "sample_return_only_weight_feasibility_proved":1,
        "sample_return_only_local_witness_complete":1,
        "sample_global_weight_bindings_complete":0,
        "sample_full_compulsory_row_complete":0,
        "sample_weighted_row_strict":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},"honesty")

def mutation_audit(root: Path, contract: dict[str,Any])->int:
    mutations=[
        lambda x:x["return_row"]["terms"].pop(),
        lambda x:x["explicit_local_witness"].update(parent_weight=4),
        lambda x:x["explicit_local_witness"]["child_weights"].update(w_return_22_rank2=0),
        lambda x:x["explicit_local_witness"].update(weighted_child_total=3),
        lambda x:x["explicit_local_witness"].update(strict_slack=5),
        lambda x:x["explicit_local_witness"]["normalized_child_weights"].update(w_return_22_rank2=[1,4]),
        lambda x:x["category_accounting"].update(selector="zero"),
        lambda x:x["category_accounting"].update(line="offspring-charge"),
        lambda x:x["residual_bindings"].pop(),
        lambda x:x["residual_bindings"][0].update(status="resolved"),
        lambda x:x["honesty"].update(sample_weighted_row_strict=1),
        lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(contract); mutate(bad)
        try: validate(root,bad)
        except SampleWeightFeasibilityError: rejected+=1
    require(rejected==len(mutations),"weight feasibility corruption accepted")
    return rejected

def main()->None:
    root=repository_root(); contract=json.loads((root/WEIGHT_PATH).read_text(encoding="utf-8"))
    validate(root,contract)
    print(json.dumps({
        "checker":"prime-power-side-four-sample-weight-feasibility",
        "routing_contract_sha256":EXPECTED_ROUTING_SHA256,
        "weight_contract_sha256":EXPECTED_WEIGHT_SHA256,
        "local_parent_weight":8,"local_weighted_child_total":4,"local_strict_slack":4,
        "residual_binding_record_count":9,"rejected_corruptions":mutation_audit(root,contract),
        "sample_return_only_weight_feasibility_proved":1,
        "sample_return_only_local_witness_complete":1,
        "sample_global_weight_bindings_complete":0,
        "sample_full_compulsory_row_complete":0,
        "sample_weighted_row_strict":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__": main()
