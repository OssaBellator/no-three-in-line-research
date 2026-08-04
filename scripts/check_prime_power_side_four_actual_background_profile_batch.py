#!/usr/bin/env python3
"""Validate actual-background profile records and derive all incidence counts."""
from __future__ import annotations
import copy, hashlib, json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any

class ActualBackgroundProfileError(RuntimeError): pass

def require(ok: bool,message: str)->None:
    if not ok: raise ActualBackgroundProfileError(message)

def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

SELECTED_PATH="data/prime_power_side_four_selected_response_provenance_manifest.json"
RESIDUAL_PATH="data/prime_power_side_four_residual_return_credit_worklist_contract.json"
LINE_PATH="data/prime_power_side_four_symbolic_line_kernel_context_contract.json"
BATCH_PATH="data/prime_power_side_four_actual_background_profile_batch.json"
EXPECTED_SELECTED_SHA256="0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_RESIDUAL_SHA256="606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808"
EXPECTED_LINE_SHA256="0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e"
EXPECTED_BATCH_SHA256="ace0a65dd4b6ce8dfa634a370cb531670aa824c7c83dd44f45b81f95bd57c6e4"
PROFILE_FIELDS=("profile_id","host_id","provenance_key","background_points","retained_incidence_labels","line_owner_labels","selected_response")

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise ActualBackgroundProfileError("unable to locate repository root")

def collinear(first: tuple[int,int],second: tuple[int,int],third: tuple[int,int])->bool:
    return (second[0]-first[0])*(third[1]-first[1])==(second[1]-first[1])*(third[0]-first[0])

def parse_line(value: str)->tuple[int,int,int]:
    pieces=value.split(","); require(len(pieces)==3,"canonical line encoding")
    line=tuple(int(piece) for piece in pieces)
    require(line!=(0,0,0),"nonzero line")
    return line

def line_height(background: list[tuple[int,int]],line: tuple[int,int,int])->int:
    a,b,c=line; return sum(a*x+b*y+c==0 for x,y in background)

def rank_one_pair_incidence(background: list[tuple[int,int]],entering_point: tuple[int,int])->int:
    return sum(collinear(first,second,entering_point) for first,second in combinations(background,2))

def complete_kernel(height: int,response_occupancy: int)->int:
    require(height>=0 and response_occupancy>=0,"nonnegative kernel inputs")
    return response_occupancy*comb(height,2)+comb(response_occupancy,2)*height+comb(response_occupancy,3)

def expected_batch()->dict[str,Any]:
    return {
        "schema":"prime-power-side-four-actual-background-profile-batch/v1",
        "bindings":{
            "selected_response_manifest_sha256":EXPECTED_SELECTED_SHA256,
            "residual_return_contract_sha256":EXPECTED_RESIDUAL_SHA256,
            "symbolic_line_contract_sha256":EXPECTED_LINE_SHA256,
        },
        "profile_fields":list(PROFILE_FIELDS),
        "derivation_rules":{
            "line_height":"count listed background points on the canonical coordinate line",
            "rank_one_background_pair_incidence":"count unordered listed background-point pairs collinear with the selected entering point",
            "rank_two_background_point_incidence":"line height on the exact selected-response pair line",
            "complete_line_kernel":"K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)",
            "published_counts":"all incidence counts are derived from background_points and may not be supplied independently",
        },
        "profiles":[],
        "aggregate":{
            "expected_normalized_hosts":86,
            "provided_profiles":0,
            "missing_profiles":86,
            "populated_background_points":0,
            "populated_rank_one_incidences":0,
            "populated_rank_two_incidences":0,
        },
        "honesty":{
            "actual_background_profile_schema_complete":1,
            "actual_background_profile_batch_complete":0,
            "actual_background_profiles_complete":0,
            "rank_one_return_coefficients_complete":0,
            "rank_two_return_coefficients_complete":0,
            "numeric_rank_one_rank_two_line_coefficients_complete":0,
            "global_child_provenance_complete":0,
            "complete_weighted_rows_strict":0,
            "all_n_proved_by_checker":0,
        },
    }

def validate_profile(profile: dict[str,Any],selected_by_host: dict[str,str])->dict[str,Any]:
    require(tuple(profile.keys())==PROFILE_FIELDS,"profile fields and order")
    require(isinstance(profile["profile_id"],str) and profile["profile_id"],"profile id")
    require(profile["host_id"] in selected_by_host,"profile host")
    require(profile["selected_response"]==selected_by_host[profile["host_id"]],"profile selected response")
    require(isinstance(profile["provenance_key"],str) and profile["provenance_key"],"profile provenance")
    raw_points=profile["background_points"]
    require(isinstance(raw_points,list),"background point list")
    points=[]
    for point in raw_points:
        require(isinstance(point,list) and len(point)==2 and all(isinstance(value,int) for value in point),"background point")
        points.append((point[0],point[1]))
    require(len(points)==len(set(points)),"duplicate background point")
    require(isinstance(profile["retained_incidence_labels"],list),"retained incidence labels")
    require(isinstance(profile["line_owner_labels"],dict),"line owner labels")
    return {"profile_id":profile["profile_id"],"host_id":profile["host_id"],"background_points":points}

def synthetic_derivation_audit()->dict[str,int]:
    background=[(0,0),(1,1),(2,2)]
    require(line_height(background,(1,-1,0))==3,"synthetic line height")
    require(rank_one_pair_incidence(background,(3,3))==3,"synthetic rank-one incidence")
    require(complete_kernel(3,2)==9,"synthetic complete kernel")
    require(complete_kernel(0,4)==4,"synthetic rank-three kernel")
    return {"line_height":3,"rank_one_pair_incidence":3,"rank_two_point_incidence":3,"complete_kernel_h3_k2":9,"complete_kernel_h0_k4":4}

def validate(root: Path,batch: dict[str,Any])->list[dict[str,Any]]:
    selected=json.loads((root/SELECTED_PATH).read_text(encoding="utf-8"))
    residual=json.loads((root/RESIDUAL_PATH).read_text(encoding="utf-8"))
    line=json.loads((root/LINE_PATH).read_text(encoding="utf-8"))
    require(digest(selected)==EXPECTED_SELECTED_SHA256,"selected manifest binding")
    require(digest(residual)==EXPECTED_RESIDUAL_SHA256,"residual contract binding")
    require(digest(line)==EXPECTED_LINE_SHA256,"symbolic line binding")
    require(batch==expected_batch(),"background batch differs from canonical empty schema")
    require(digest(batch)==EXPECTED_BATCH_SHA256,"background batch digest")
    selected_by_host={host[0]:host[1] for host in selected["hosts"]}
    require(len(selected_by_host)==86,"normalized host universe")
    profiles=[]; ids=set(); hosts=set()
    for profile in batch["profiles"]:
        validated=validate_profile(profile,selected_by_host)
        require(validated["profile_id"] not in ids,"duplicate profile id")
        require(validated["host_id"] not in hosts,"duplicate host profile")
        ids.add(validated["profile_id"]); hosts.add(validated["host_id"]); profiles.append(validated)
    require(len(profiles)==0,"current profile batch must remain empty until actual data is supplied")
    synthetic_derivation_audit()
    return profiles

def mutation_audit(root: Path,batch: dict[str,Any])->int:
    mutations=[
        lambda item:item["aggregate"].update(expected_normalized_hosts=85),
        lambda item:item["aggregate"].update(provided_profiles=1),
        lambda item:item["aggregate"].update(missing_profiles=85),
        lambda item:item["bindings"].update(residual_return_contract_sha256="0"*64),
        lambda item:item["profile_fields"].remove("provenance_key"),
        lambda item:item["derivation_rules"].update(line_height="supplied count"),
        lambda item:item["derivation_rules"].update(published_counts="accepted independently"),
        lambda item:item["profiles"].append({}),
        lambda item:item["honesty"].update(actual_background_profile_batch_complete=1),
        lambda item:item["honesty"].update(rank_one_return_coefficients_complete=1),
        lambda item:item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item:item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(batch); mutate(bad)
        try: validate(root,bad)
        except ActualBackgroundProfileError: rejected+=1
    require(rejected==len(mutations),"background profile corruption accepted")
    return rejected

def main()->None:
    root=repository_root(); batch=json.loads((root/BATCH_PATH).read_text(encoding="utf-8"))
    validate(root,batch); synthetic=synthetic_derivation_audit()
    print(json.dumps({
        "checker":"prime-power-side-four-actual-background-profile-batch",
        "background_profile_batch_sha256":EXPECTED_BATCH_SHA256,
        "selected_response_manifest_sha256":EXPECTED_SELECTED_SHA256,
        "residual_return_contract_sha256":EXPECTED_RESIDUAL_SHA256,
        "symbolic_line_contract_sha256":EXPECTED_LINE_SHA256,
        "expected_host_count":86,
        "provided_profile_count":0,
        "missing_profile_count":86,
        "synthetic_derivation_audit":synthetic,
        "rejected_corruptions":mutation_audit(root,batch),
        "actual_background_profile_schema_complete":1,
        "actual_background_profile_batch_complete":0,
        "actual_background_profiles_complete":0,
        "rank_one_return_coefficients_complete":0,
        "rank_two_return_coefficients_complete":0,
        "numeric_rank_one_rank_two_line_coefficients_complete":0,
        "global_child_provenance_complete":0,
        "complete_weighted_rows_strict":0,
        "all_n_proved_by_checker":0,
    },sort_keys=True))

if __name__=="__main__": main()
