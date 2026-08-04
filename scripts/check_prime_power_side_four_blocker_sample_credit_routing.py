#!/usr/bin/env python3
"""Validate exact one-count routing for the populated blocker-alternative sample."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

class BlockerSampleRoutingError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise BlockerSampleRoutingError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SAMPLE_PATH="data/prime_power_side_four_blocker_actual_background_sample_batch.json"
ROUTING_PATH="data/prime_power_side_four_blocker_sample_credit_routing_contract.json"
SAMPLE_CHECKER_PATH="scripts/check_prime_power_side_four_blocker_actual_background_sample.py"
SELECTED_PATH="data/prime_power_side_four_selected_response_provenance_manifest.json"
OBLIGATION_PATH="data/prime_power_side_four_actual_background_profile_obligation_contract.json"
EXPECTED_SAMPLE_SHA256="39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"
EXPECTED_ROUTING_SHA256="4b8da717b59a47d8c5f1d4db1308e934c26390804611b0906c81c30cce136aa5"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise BlockerSampleRoutingError("unable to locate repository root")

def load_module(path: Path)->Any:
    require(path.is_file(),"blocker sample checker missing")
    spec=importlib.util.spec_from_file_location("blocker_sample_checker",path)
    require(spec is not None and spec.loader is not None,"checker import")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def child_key(*,predecessor: str,rank: int,line: tuple[int,int,int],owner: str,background_id: str)->dict[str,Any]:
    line_text=",".join(str(v) for v in line)
    local=(f"rank{rank}:{line_text}:h2:k2" if rank in {1,2} else f"rank3:{line_text}:h0:k3")
    return {
        "structural_owner":f"return:{predecessor}",
        "fate":"repeated-return",
        "collision_class":"02,20",
        "local_line_class":local,
        "interface_label":"side4-target01",
        "remaining_provenance":{
            "background_id":background_id,
            "credit_class":f"rank{rank}",
            "crt_provenance":"not-applied/blocker-sample-profile/v1",
            "entering_owner":owner,
            "source_host_fate":"blocker-alternative",
            "blockers":["b4-8a44614df456"]}}

def compile_credits(sample: dict[str,Any],checker: Any)->list[dict[str,Any]]:
    require(digest(sample)==EXPECTED_SAMPLE_SHA256,"sample digest")
    profile=sample["profile"];selector=profile["selected_response"]
    response=tuple((source,int(selector[source])) for source in range(4))
    background=tuple(tuple(point) for point in profile["background_points"])
    labels={tuple(item["point"]):f"bg{index}" for index,item in enumerate(profile["background_point_provenance"])}
    background_id=profile["background_id"];credits=[]
    for response_point in response:
        for first,second in combinations(background,2):
            line=checker.canonical_line(first,second)
            if line[0]==0 or line[1]==0 or not checker.on_line(line,response_point): continue
            owner=checker.edge(response_point);pred=f"{response_point[0]}{response_point[0]}"
            points=sorted((labels[first],labels[second]))
            credits.append({
                "credit_id":f"br1-{owner}-{points[0]}-{points[1]}","rank":1,
                "response_edges":[owner],"background_points":points,"line_equation":list(line),
                "entering_owner":owner,"returned_predecessor":pred,"coefficient":1,
                "child_key":child_key(predecessor=pred,rank=1,line=line,owner=owner,background_id=background_id),
                "weight_symbol":f"w_return_{pred}_rank1","positive_weight_required":1})
    for first,second in combinations(response,2):
        line=checker.canonical_line(first,second)
        pair=sorted((checker.edge(first),checker.edge(second)));owner_point=max(first,second)
        owner=checker.edge(owner_point);pred=f"{owner_point[0]}{owner_point[0]}"
        for point in background:
            if not checker.on_line(line,point): continue
            credits.append({
                "credit_id":f"br2-{pair[0]}-{pair[1]}-{labels[point]}","rank":2,
                "response_edges":pair,"background_points":[labels[point]],"line_equation":list(line),
                "entering_owner":owner,"returned_predecessor":pred,"coefficient":1,
                "child_key":child_key(predecessor=pred,rank=2,line=line,owner=owner,background_id=background_id),
                "weight_symbol":f"w_return_{pred}_rank2","positive_weight_required":1})
    for triple in combinations(response,3):
        line=checker.canonical_line(triple[0],triple[1])
        if not checker.on_line(line,triple[2]): continue
        edges=sorted(checker.edge(point) for point in triple);owner_point=max(triple)
        owner=checker.edge(owner_point);pred=f"{owner_point[0]}{owner_point[0]}"
        credits.append({
            "credit_id":"br3-"+"-".join(edges),"rank":3,"response_edges":edges,
            "background_points":[],"line_equation":list(line),"entering_owner":owner,
            "returned_predecessor":pred,"coefficient":1,
            "child_key":child_key(predecessor=pred,rank=3,line=line,owner=owner,background_id=background_id),
            "weight_symbol":f"w_return_{pred}_rank3","positive_weight_required":1})
    return sorted(credits,key=lambda item:item["credit_id"])

def compress(credits: list[dict[str,Any]])->list[dict[str,Any]]:
    grouped=defaultdict(int)
    for credit in credits:
        key=credit["child_key"]
        class_id=f"{key['structural_owner']}|{key['local_line_class']}|collision:{key['collision_class']}"
        grouped[(class_id,credit["weight_symbol"])]+=credit["coefficient"]
    return [{"class_id":class_id,"coefficient":coefficient,"weight_symbol":weight}
            for (class_id,weight),coefficient in sorted(grouped.items())]

def validate(root: Path,routing: dict[str,Any])->list[dict[str,Any]]:
    checker=load_module(root/SAMPLE_CHECKER_PATH)
    selected=json.loads((root/SELECTED_PATH).read_text(encoding="utf-8"))
    obligation=json.loads((root/OBLIGATION_PATH).read_text(encoding="utf-8"))
    sample=json.loads((root/SAMPLE_PATH).read_text(encoding="utf-8"))
    checker.validate(selected,obligation,sample)
    require(checker.EXPECTED_SAMPLE_SHA256==EXPECTED_SAMPLE_SHA256,"sample checker binding")
    require(routing["sample_contract_sha256"]==EXPECTED_SAMPLE_SHA256,"sample binding")
    require(digest(routing)==EXPECTED_ROUTING_SHA256,"routing digest")
    credits=compile_credits(sample,checker)
    require(routing["credits"]==credits and len(credits)==5,"exact credits")
    require(Counter(c["rank"] for c in credits)==Counter({1:2,2:2,3:1}),"rank census")
    require(Counter(c["returned_predecessor"] for c in credits)==Counter({"11":3,"00":1,"33":1}),"predecessor census")
    require(all(c["coefficient"]==1 and c["positive_weight_required"]==1 and c["weight_symbol"] for c in credits),"credit coefficients and weights")
    classes=compress(credits)
    require(routing["compressed_child_classes"]==classes and len(classes)==4,"compressed classes")
    require(routing["weighted_return_expression"]=={
        "terms":[[item["weight_symbol"],item["coefficient"]] for item in classes],
        "strict_parent_budget":None},"weighted expression")
    require(routing["accounting"]=={
        "line_category_role":"certificate-source-only",
        "return_category_role":"offspring-charge",
        "credit_counting_rule":"each blocker-sample recreated credit occurs in exactly one return child charge; line coefficients certify but do not add a second offspring term",
        "rank_three_rule":"the intrinsic selected-response triple is charged once to returned predecessor 33"},"accounting")
    require(routing["aggregate"]=={
        "credits":5,"rank_one_credits":2,"rank_two_credits":2,"rank_three_credits":1,
        "child_classes":4,"line_certificate_total":5,"return_charge_total":5,
        "returned_predecessor_census":{"00":1,"11":3,"33":1},
        "unresolved_positive_weight_symbols":4},"aggregate")
    require(routing["honesty"]=={
        "blocker_sample_credit_partition_complete":1,
        "blocker_sample_child_routing_complete":1,
        "blocker_sample_child_keys_complete_for_populated_credits":1,
        "blocker_sample_child_weights_complete":0,
        "blocker_sample_weighted_row_strict":0,
        "global_child_provenance_complete":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},"honesty")
    return credits

def mutation_audit(root: Path,routing: dict[str,Any])->int:
    mutations=[
        lambda x:x["credits"].pop(),
        lambda x:x["credits"][0].update(returned_predecessor="11"),
        lambda x:x["credits"][0].update(coefficient=2),
        lambda x:x["credits"][0]["child_key"].update(collision_class="-"),
        lambda x:x["credits"][4]["child_key"].update(local_line_class="rank2"),
        lambda x:x["credits"][4].update(weight_symbol=""),
        lambda x:x["compressed_child_classes"][3].update(coefficient=2),
        lambda x:x["weighted_return_expression"].update(strict_parent_budget=5),
        lambda x:x["accounting"].update(line_category_role="offspring-charge"),
        lambda x:x["accounting"].update(rank_three_rule="omit"),
        lambda x:x["aggregate"].update(return_charge_total=4),
        lambda x:x["honesty"].update(blocker_sample_child_weights_complete=1),
        lambda x:x["honesty"].update(blocker_sample_weighted_row_strict=1),
        lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(routing);mutate(bad)
        try:validate(root,bad)
        except BlockerSampleRoutingError:rejected+=1
    require(rejected==len(mutations),"routing corruption accepted")
    return rejected

def main()->None:
    root=repository_root();routing=json.loads((root/ROUTING_PATH).read_text(encoding="utf-8"))
    credits=validate(root,routing)
    print(json.dumps({
        "checker":"prime-power-side-four-blocker-sample-credit-routing",
        "routing_contract_sha256":EXPECTED_ROUTING_SHA256,
        "credit_count":len(credits),"child_class_count":len(routing["compressed_child_classes"]),
        "returned_predecessor_census":routing["aggregate"]["returned_predecessor_census"],
        "rejected_corruptions":mutation_audit(root,routing),
        "blocker_sample_credit_partition_complete":1,
        "blocker_sample_child_routing_complete":1,
        "blocker_sample_child_keys_complete_for_populated_credits":1,
        "blocker_sample_child_weights_complete":0,
        "blocker_sample_weighted_row_strict":0,
        "global_child_provenance_complete":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__":main()
