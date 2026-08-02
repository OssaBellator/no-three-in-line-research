#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json
from collections import Counter
from pathlib import Path
from typing import Any

class SelectedResponseManifestError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise SelectedResponseManifestError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

LINEAGE_PATH="data/prime_power_side_four_raw_fibre_lineage_manifest.json"
MANIFEST_PATH="data/prime_power_side_four_selected_response_provenance_manifest.json"
EXPECTED_LINEAGE_SHA256="84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f"
EXPECTED_MANIFEST_SHA256="0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise SelectedResponseManifestError("unable to locate repository root")

def build_expected(lineage: dict[str,Any])->dict[str,Any]:
    hosts=[]
    for host_id,deletion,responses,dispatch,blockers in lineage["hosts"]:
        parsed=[(code.split(":",1)[0],int(code.split(":",1)[1])) for code in responses]
        minimum=min(value for _,value in parsed)
        face=sorted(response for response,value in parsed if value==minimum)
        levels=sorted({value for _,value in parsed})
        gap=levels[1]-levels[0] if len(levels)>1 else "-"
        hosts.append([host_id,face[0],",".join(face),minimum,gap,"Z" if minimum==0 else "B",blockers,deletion])
    return {
        "schema":"prime-power-side-four-selected-response-provenance-manifest/v1",
        "lineage_manifest_sha256":EXPECTED_LINEAGE_SHA256,
        "selection_rule":"minimum triple count then lexicographically least response permutation",
        "encoding":"host=[id,selector,minimizer_face,minimum_energy,next_energy_gap,fate(Z|B),blockers,collision_key]",
        "normalized_provenance":{"owner_scope":"side-four-raw-host","local_line_class":"minimum-response-energy","interface":"target-01","crt_scope":"not-applied","collision_key":"host deletion trace"},
        "aggregate":{"hosts":86,"zero_selected":75,"blocker_alternatives":11,"unique_minimum":42,"tied_minimum":44,"positive_next_energy_gap":47,"no_higher_energy_response":39,"gap_census":{"1":25,"3":9,"4":13,"none":39},"minimum_energy_census":{"0":75,"1":9,"4":2}},
        "hosts":hosts,
        "honesty":{"global_provenance_complete":0,"compulsory_coefficients_complete":0,"complete_weighted_rows_strict":0,"all_n_proved_by_checker":0},
    }

def validate(lineage: dict[str,Any],manifest: dict[str,Any])->None:
    require(digest(lineage)==EXPECTED_LINEAGE_SHA256,"lineage digest mismatch")
    expected=build_expected(lineage)
    require(manifest==expected,"selection manifest differs from deterministic selector")
    require(digest(manifest)==EXPECTED_MANIFEST_SHA256,"selection manifest digest mismatch")
    require(Counter(host[3] for host in manifest["hosts"])==Counter({0:75,1:9,4:2}),"minimum energy census")
    require(Counter(host[4] for host in manifest["hosts"])==Counter({"-":39,1:25,4:13,3:9}),"gap census")
    for host in manifest["hosts"]:
        face=host[2].split(",")
        require(host[1]==min(face),"selector tie break")
        if host[5]=="B": require(host[6] and host[3]>0,"blocker fate")
        else: require(host[3]==0,"zero fate")
    require(all(value==0 for value in manifest["honesty"].values()),"honesty")

def mutation_audit(lineage: dict[str,Any],manifest: dict[str,Any])->int:
    mutations=[
        lambda item:item["aggregate"].update(hosts=85),
        lambda item:item["aggregate"].update(unique_minimum=41),
        lambda item:item["hosts"].pop(),
        lambda item:item["hosts"][0].__setitem__(1,"9999"),
        lambda item:item["hosts"][0].__setitem__(2,"9999"),
        lambda item:item["hosts"][0].__setitem__(3,4),
        lambda item:item["hosts"][0].__setitem__(4,3),
        lambda item:item["hosts"][0].__setitem__(5,"B"),
        lambda item:item["honesty"].update(compulsory_coefficients_complete=1),
        lambda item:item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(manifest); mutate(bad)
        try: validate(lineage,bad)
        except SelectedResponseManifestError: rejected+=1
    require(rejected==len(mutations),"selection corruption accepted")
    return rejected

def main()->None:
    root=repository_root()
    lineage=json.loads((root/LINEAGE_PATH).read_text(encoding="utf-8"))
    manifest=json.loads((root/MANIFEST_PATH).read_text(encoding="utf-8"))
    validate(lineage,manifest)
    print(json.dumps({"checker":"prime-power-side-four-selected-response-provenance-manifest","lineage_manifest_sha256":EXPECTED_LINEAGE_SHA256,"selection_manifest_sha256":EXPECTED_MANIFEST_SHA256,"host_count":86,"unique_minimum_count":42,"tied_minimum_count":44,"positive_next_energy_gap_count":47,"blocker_alternative_count":11,"rejected_corruptions":mutation_audit(lineage,manifest),"side_four_selected_response_provenance_manifest_complete":1,"global_provenance_complete":0,"compulsory_coefficients_complete":0,"complete_weighted_rows_strict":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__": main()
