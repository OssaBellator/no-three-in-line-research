#!/usr/bin/env python3
"""Validate an explicit side-four blocker-alternative actual-background sample."""
from __future__ import annotations
import copy, hashlib, json
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from typing import Any

class BlockerBackgroundSampleError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise BlockerBackgroundSampleError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SELECTED_PATH="data/prime_power_side_four_selected_response_provenance_manifest.json"
OBLIGATION_PATH="data/prime_power_side_four_actual_background_profile_obligation_contract.json"
SAMPLE_PATH="data/prime_power_side_four_blocker_actual_background_sample_batch.json"
EXPECTED_SELECTED_SHA256="0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_OBLIGATION_SHA256="e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd"
EXPECTED_RESIDUAL_ROW_SHA256="72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2"
EXPECTED_SAMPLE_SHA256="39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise BlockerBackgroundSampleError("unable to locate repository root")

def canonical_line(first: tuple[int,int],second: tuple[int,int])->tuple[int,int,int]:
    require(first!=second,"distinct points required")
    x1,y1=first;x2,y2=second
    a,b,c=y1-y2,x2-x1,x1*y2-x2*y1
    common=0
    for value in (a,b,c): common=gcd(common,abs(value))
    require(common>0,"nonzero line")
    a,b,c=a//common,b//common,c//common
    if a<0 or (a==0 and b<0) or (a==0 and b==0 and c<0): a,b,c=-a,-b,-c
    return a,b,c

def on_line(line: tuple[int,int,int],point: tuple[int,int])->bool:
    a,b,c=line;x,y=point;return a*x+b*y+c==0
def edge(point: tuple[int,int])->str: return f"{point[0]}{point[1]}"

def compile_profile(selected: dict[str,Any],sample: dict[str,Any])->dict[str,Any]:
    require(digest(selected)==EXPECTED_SELECTED_SHA256,"selected manifest digest")
    profile=sample["profile"]
    rows=[row for row in selected["hosts"] if row[0]==profile["host_id"]]
    require(len(rows)==1,"sample host coverage")
    host=rows[0]
    require(host[1]==profile["selected_response"]=="3012","selected response binding")
    require(host[3]==1 and host[5]=="B","blocker selected fate")
    require(host[6]==profile["blockers"]==["b4-8a44614df456"],"blocker binding")
    require(host[7]==profile["collision_key"]=="02,20","collision binding")
    require(profile["selected_fate"]=="blocker-alternative","sample fate")
    selector=profile["selected_response"]
    response=tuple((source,int(selector[source])) for source in range(4))
    raw_background=profile["background_points"]
    require(isinstance(raw_background,list) and len(raw_background)==2 and all(isinstance(p,list) and len(p)==2 and all(isinstance(v,int) for v in p) for p in raw_background),"two integer background points")
    background=tuple(tuple(p) for p in raw_background)
    require(len(set(background))==2 and not set(background)&set(response),"background geometry")
    require(profile["coordinate_scope"]=="integer-lattice-blocker-sample-not-global-board-claim","coordinate scope")
    require(sample["scope"]=={
        "kind":"explicit-integer-coordinate-blocker-sample",
        "global_recurrent_state_claim":0,
        "normalized_host_inference":0,
        "identity_matching_inference":0},"scope honesty")
    require(profile["background_point_provenance"]==[
        {"point":[-1,6],"label":"declared-blocker-sample-background-point-0"},
        {"point":[-2,9],"label":"declared-blocker-sample-background-point-1"}],"background provenance")

    rank_one={}
    for point in response:
        incidence=0
        for first,second in combinations(background,2):
            line=canonical_line(first,second)
            if line[0]!=0 and line[1]!=0 and on_line(line,point): incidence+=1
        rank_one[edge(point)]=incidence

    rank_two={}; line_profiles={}
    for first,second in combinations(response,2):
        line=canonical_line(first,second)
        key="|".join(sorted((edge(first),edge(second))))
        load=sum(on_line(line,p) for p in background)
        occupancy=sum(on_line(line,p) for p in response)
        rank_two[key]=load
        require(occupancy>=2,f"{key}: occupancy")
        if line not in line_profiles:
            r1=occupancy*comb(load,2);r2=comb(occupancy,2)*load;r3=comb(occupancy,3)
            line_profiles[line]={"background_load":load,"response_occupancy":occupancy,"rank_one":r1,"rank_two":r2,"rank_three":r3,"total":r1+r2+r3}
        else:
            require(line_profiles[line]["background_load"]==load and line_profiles[line]["response_occupancy"]==occupancy,f"{key}: line consistency")

    rank_three={}
    for triple in combinations(response,3):
        line=canonical_line(triple[0],triple[1])
        if on_line(line,triple[2]):
            key="|".join(sorted(edge(point) for point in triple));rank_three[key]=1

    rank_one_return={f"{source}{source}":0 for source in range(4)}
    for point in response: rank_one_return[f"{point[0]}{point[0]}"]+=rank_one[edge(point)]
    rank_two_return={f"{source}{source}":0 for source in range(4)}
    for first,second in combinations(response,2):
        owner=max(first,second);key="|".join(sorted((edge(first),edge(second))))
        rank_two_return[f"{owner[0]}{owner[0]}"]+=rank_two[key]
    rank_three_return={f"{source}{source}":0 for source in range(4)}
    for triple in combinations(response,3):
        line=canonical_line(triple[0],triple[1])
        if on_line(line,triple[2]):
            owner=max(triple);rank_three_return[f"{owner[0]}{owner[0]}"]+=1
    total_return={key:rank_one_return[key]+rank_two_return[key]+rank_three_return[key] for key in rank_one_return}
    encoded_lines={",".join(str(v) for v in line):values for line,values in sorted(line_profiles.items())}
    return {
        "rank_one_by_entering_edge":rank_one,"rank_one_total":sum(rank_one.values()),
        "rank_two_by_response_pair":rank_two,"rank_two_total":sum(rank_two.values()),
        "rank_three_by_response_triple":rank_three,"rank_three_total":sum(rank_three.values()),
        "complete_line_kernel_by_line":encoded_lines,
        "complete_line_kernel_total":sum(item["total"] for item in line_profiles.values()),
        "return_rank_one_charge_by_predecessor":rank_one_return,
        "return_rank_two_charge_by_predecessor":rank_two_return,
        "return_rank_three_charge_by_predecessor":rank_three_return,
        "return_total_charge_by_predecessor":total_return}

def validate(selected: dict[str,Any],obligation: dict[str,Any],sample: dict[str,Any])->dict[str,Any]:
    require(digest(obligation)==EXPECTED_OBLIGATION_SHA256,"obligation digest")
    require(sample["actual_background_profile_obligation_contract_sha256"]==EXPECTED_OBLIGATION_SHA256,"obligation binding")
    require(sample["compiled_residual_return_row_sha256"]==EXPECTED_RESIDUAL_ROW_SHA256,"residual return binding")
    require(sample["selected_response_manifest_sha256"]==EXPECTED_SELECTED_SHA256,"selected binding")
    require(digest(sample)==EXPECTED_SAMPLE_SHA256,"sample digest")
    compiled=compile_profile(selected,sample)
    require(sample["expected"]==compiled,"numeric profile")
    require(sample["aggregate"]=={
        "profile_records":1,"background_points":2,
        "populated_rank_one_entries":4,"positive_rank_one_entries":2,
        "populated_rank_two_entries":6,"positive_rank_two_entries":1,
        "populated_rank_three_entries":4,"positive_rank_three_entries":1,
        "populated_line_classes":4,"positive_line_classes":2,
        "numeric_non_geometric_categories":["line","return"],
        "blocker_alternative_rows":1},"aggregate")
    require(sample["honesty"]=={
        "side_four_blocker_actual_background_sample_batch_complete":1,
        "blocker_sample_line_coefficients_complete":1,
        "blocker_sample_rank_one_rank_two_rank_three_return_coefficients_complete":1,
        "actual_background_profiles_complete":0,
        "global_child_provenance_complete":0,
        "child_keys_complete":0,"child_weights_complete":0,
        "complete_weighted_rows_strict":0,"all_n_proved_by_checker":0},"honesty")
    require(sample["profile"]["line_owner_labels"]=={
        "3,1,-3":"sample-line-owner:3,1,-3",
        "1,-1,-1":"selected-rank-three-line-owner:1,-1,-1"},"line owners")
    return compiled

def mutation_audit(selected: dict[str,Any],obligation: dict[str,Any],sample: dict[str,Any])->int:
    mutations=[
        lambda x:x["profile"].update(host_id="missing"),
        lambda x:x["profile"].update(selected_response="2031"),
        lambda x:x["profile"].update(selected_fate="zero-response"),
        lambda x:x["profile"]["blockers"].clear(),
        lambda x:x["profile"]["background_points"][0].__setitem__(0,0),
        lambda x:x["scope"].update(global_recurrent_state_claim=1),
        lambda x:x["expected"].update(rank_one_total=1),
        lambda x:x["expected"].update(rank_two_total=1),
        lambda x:x["expected"].update(rank_three_total=0),
        lambda x:x["expected"].update(complete_line_kernel_total=4),
        lambda x:x["expected"]["return_total_charge_by_predecessor"].update({"33":0}),
        lambda x:x["profile"]["line_owner_labels"].pop("1,-1,-1"),
        lambda x:x["honesty"].update(actual_background_profiles_complete=1),
        lambda x:x["honesty"].update(child_weights_complete=1),
        lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(sample);mutate(bad)
        try:validate(selected,obligation,bad)
        except BlockerBackgroundSampleError:rejected+=1
    require(rejected==len(mutations),"blocker sample corruption accepted")
    return rejected

def main()->None:
    root=repository_root()
    selected=json.loads((root/SELECTED_PATH).read_text(encoding="utf-8"))
    obligation=json.loads((root/OBLIGATION_PATH).read_text(encoding="utf-8"))
    sample=json.loads((root/SAMPLE_PATH).read_text(encoding="utf-8"))
    compiled=validate(selected,obligation,sample)
    print(json.dumps({
        "checker":"prime-power-side-four-blocker-actual-background-sample",
        "sample_contract_sha256":EXPECTED_SAMPLE_SHA256,
        "host_id":sample["profile"]["host_id"],
        "rank_one_total":compiled["rank_one_total"],
        "rank_two_total":compiled["rank_two_total"],
        "rank_three_total":compiled["rank_three_total"],
        "complete_line_kernel_total":compiled["complete_line_kernel_total"],
        "return_total_charge_by_predecessor":compiled["return_total_charge_by_predecessor"],
        "rejected_corruptions":mutation_audit(selected,obligation,sample),
        "side_four_blocker_actual_background_sample_batch_complete":1,
        "blocker_sample_line_coefficients_complete":1,
        "blocker_sample_rank_one_rank_two_rank_three_return_coefficients_complete":1,
        "actual_background_profiles_complete":0,
        "global_child_provenance_complete":0,
        "child_keys_complete":0,"child_weights_complete":0,
        "complete_weighted_rows_strict":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__":main()
