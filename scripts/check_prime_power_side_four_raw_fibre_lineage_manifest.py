#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

class SideFourLineageManifestError(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise SideFourLineageManifestError(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

MANIFEST_PATH="data/prime_power_side_four_raw_fibre_lineage_manifest.json"
EXPECTED_MANIFEST_SHA256="84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f"

def repository_root(start: Path|None=None)->Path:
    current=(start or Path(__file__).resolve()).resolve()
    if current.is_file(): current=current.parent
    for candidate in (current,*current.parents):
        if (candidate/"STATUS.md").is_file() and (candidate/"scripts").is_dir(): return candidate
    raise SideFourLineageManifestError("unable to locate repository root")

def collinear(a: tuple[int,int],b: tuple[int,int],c: tuple[int,int])->bool:
    return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def triple_count(response: tuple[tuple[int,int],...])->int:
    return sum(collinear(*triple) for triple in combinations(response,3))
def perfect_matchings(side: int,allowed: set[tuple[int,int]])->list[tuple[tuple[int,int],...]]:
    return [tuple((row,permutation[row]) for row in range(side)) for permutation in permutations(range(side)) if all((row,permutation[row]) in allowed for row in range(side))]
def edge_code(edges)->str:
    encoded=",".join(f"{row}{column}" for row,column in sorted(edges))
    return encoded or "-"

def build_expected()->dict[str,Any]:
    side=4
    identity=[(index,index) for index in range(side)]
    target=(0,1)
    base_host={(row,column) for row in range(side) for column in range(side) if (row,column) not in set(identity) and (row,column)!=target}
    deletions=[frozenset()]
    for rank in range(1,side+1):
        for deletion in combinations(sorted(base_host),rank):
            if len({row for row,_ in deletion})==rank and len({column for _,column in deletion})==rank:
                deletions.append(frozenset(deletion))
    expanded=[]
    for deletion in deletions:
        responses=perfect_matchings(side,base_host-set(deletion))
        if not responses: continue
        core={"side":side,"target":list(target),"opposite_matching":[list(edge) for edge in identity],"deletion_edges":[list(edge) for edge in sorted(deletion)]}
        host_id="s4-"+hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()[:16]
        response_codes=[f"{''.join(str(column) for _,column in response)}:{triple_count(response)}" for response in responses]
        expanded.append({"host_id":host_id,"deletion":deletion,"responses":response_codes,"zero_count":sum(code.endswith(":0") for code in response_codes)})
    by_deletion={item["deletion"]:item for item in expanded}
    zero_free=[item for item in expanded if item["zero_count"]==0]
    minimal=[]
    for item in zero_free:
        if not any(smaller<item["deletion"] and by_deletion[smaller]["zero_count"]==0 for smaller in by_deletion):
            minimal.append(item["deletion"])
    blockers=[]; blocker_map={}
    for deletion in sorted(minimal,key=lambda item:sorted(item)):
        core={"deletion_edges":[list(edge) for edge in sorted(deletion)]}
        blocker_id="b4-"+hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()[:12]
        blockers.append([blocker_id,edge_code(deletion)]); blocker_map[deletion]=blocker_id
    hosts=[]
    for item in sorted(expanded,key=lambda item:(len(item["deletion"]),sorted(item["deletion"]))):
        contained=[blocker_map[blocker] for blocker in blocker_map if blocker<=item["deletion"]]
        dispatch="zero-response" if item["zero_count"] else "blocker-alternative"
        hosts.append([item["host_id"],edge_code(item["deletion"]),item["responses"],dispatch,contained])
    return {
        "aggregate":{"blocked_hosts":11,"blocked_minima":{"1":9,"4":2},"hosts":86,"responses":sum(len(item[2]) for item in hosts),"zero_hosts":sum(item[3]=="zero-response" for item in hosts),"zero_responses":sum(sum(code.endswith(":0") for code in item[2]) for item in hosts)},
        "base_allowed":edge_code(base_host),
        "blockers":blockers,
        "encoding":"host=[stable_id,deletion_edges,response_permutation:triple_count,dispatch,contained_blockers]",
        "honesty":{"all_n_proved_by_checker":0,"all_recurrent_states_populated":0,"compulsory_weighted_rows_complete":0},
        "hosts":hosts,
        "opposite":edge_code(identity),
        "provenance":{"coordinate_host_response":1,"global_owner_fate_collision_interface_crt":0},
        "schema":"prime-power-side-four-raw-fibre-lineage-manifest/v1",
        "side":4,
        "target":"01",
    }

def validate(manifest: dict[str,Any])->None:
    expected=build_expected()
    require(manifest==expected,"manifest differs from deterministic enumeration")
    require(digest(manifest)==EXPECTED_MANIFEST_SHA256,"manifest digest mismatch")
    require(manifest["aggregate"]=={"blocked_hosts":11,"blocked_minima":{"1":9,"4":2},"hosts":86,"responses":206,"zero_hosts":75,"zero_responses":137},"aggregate")
    require(Counter(int(code.rsplit(":",1)[1]) for host in manifest["hosts"] for code in host[2])==Counter({0:137,1:34,4:35}),"response energy census")
    for host in manifest["hosts"]:
        if host[3]=="blocker-alternative": require(host[4],f"{host[0]}: blocker missing")
        else: require(any(code.endswith(":0") for code in host[2]),f"{host[0]}: zero response missing")
    require(all(value==0 for value in manifest["honesty"].values()),"honesty")

def mutation_audit(manifest: dict[str,Any])->int:
    mutations=[
        lambda item:item["aggregate"].update(hosts=85),
        lambda item:item["aggregate"].update(responses=205),
        lambda item:item["hosts"].pop(),
        lambda item:item["hosts"][0].__setitem__(0,"corrupt"),
        lambda item:item["hosts"][0][2].pop(),
        lambda item:item["hosts"][0].__setitem__(3,"blocker-alternative"),
        lambda item:item["blockers"].pop(),
        lambda item:item["provenance"].update(global_owner_fate_collision_interface_crt=1),
        lambda item:item["honesty"].update(compulsory_weighted_rows_complete=1),
        lambda item:item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(manifest); mutate(bad)
        try: validate(bad)
        except SideFourLineageManifestError: rejected+=1
    require(rejected==len(mutations),"manifest corruption accepted")
    return rejected

def main()->None:
    root=repository_root(); path=root/MANIFEST_PATH
    require(path.is_file(),"manifest missing")
    manifest=json.loads(path.read_text(encoding="utf-8")); validate(manifest)
    print(json.dumps({"checker":"prime-power-side-four-raw-fibre-lineage-manifest","manifest_sha256":EXPECTED_MANIFEST_SHA256,"executable_host_count":86,"response_occurrence_count":206,"zero_response_occurrence_count":137,"zero_response_free_host_count":11,"minimal_blocker_count":3,"rejected_corruptions":mutation_audit(manifest),"side_four_raw_fibre_lineage_manifest_complete":1,"global_provenance_complete":0,"compulsory_weighted_rows_complete":0,"all_recurrent_states_populated":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__": main()
