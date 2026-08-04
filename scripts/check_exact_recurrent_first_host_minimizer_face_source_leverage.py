#!/usr/bin/env python3
"""Audit source leverage of background-sensitive minimizer-face scalar covers."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path
from typing import Any

HOST="s4-75b04c45c1c8eac2"
FACE=Path("data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json")
ROUTE=Path("data/exact_recurrent_first_host_closure_route_source_gate.json")
TRANS=Path("data/exact_recurrent_first_host_transition_domain_source_audit.json")
VERTICES=("A","B","C","D3","D4")
# id,left,right,left-state,right-state,count
PAIRS=(
 ("AB","A","B","00","01",32),("AC","A","C","00","10",32),
 ("BD3","B","D3","01","11",24),("BD4","B","D4","01","11",8),
 ("CD3","C","D3","10","11",24),("CD4","C","D4","10","11",8))
STATE={"A":"00","B":"01","C":"10","D3":"11","D4":"11"}
STATE_EDGES=("00->01","01->00","00->10","10->00",
             "01->11","11->01","10->11","11->10")

class AuditError(RuntimeError): pass
def req(ok: bool,msg: str)->None:
    if not ok: raise AuditError(msg)
def load(root: Path,path: Path)->dict[str,Any]:
    value=json.loads((root/path).read_text()); req(isinstance(value,dict),str(path)); return value
def canon(value: object)->str:
    return json.dumps(value,sort_keys=True,separators=(",",":"))
def sid(payload: object)->str:
    return "face-cover-"+hashlib.sha256(canon(payload).encode()).hexdigest()[:12]
def dag(edges: tuple[tuple[str,str],...])->bool:
    out={v:[] for v in VERTICES}; deg={v:0 for v in VERTICES}
    for a,b in edges: out[a].append(b); deg[b]+=1
    q=sorted(v for v in VERTICES if deg[v]==0); seen=0
    while q:
        v=q.pop(0); seen+=1
        for w in sorted(out[v]):
            deg[w]-=1
            if deg[w]==0: q.append(w); q.sort()
    return seen==len(VERTICES)
def sdir(edge: tuple[str,str])->str:
    return f"{STATE[edge[0]]}->{STATE[edge[1]]}"

def row(bits: tuple[int,...])->dict[str,Any]:
    paid=tuple((p[1],p[2]) if b else (p[2],p[1]) for p,b in zip(PAIRS,bits))
    by={p[0]:e for p,e in zip(PAIRS,paid)}
    split_ch=(by["BD3"][0]=="B")!=(by["BD4"][0]=="B")
    split_ne=(by["CD3"][0]=="C")!=(by["CD4"][0]=="C")
    projectable=not split_ch and not split_ne
    paid_names=sorted(f"{a}->{b}" for a,b in paid)
    external=tuple((b,a) for a,b in paid)
    vector={edge:0 for edge in STATE_EDGES}
    for p,e in zip(PAIRS,external): vector[sdir(e)]+=p[5]
    return {"bits":bits,"id":sid({"paid":paid_names,"projectable":int(projectable)}),
            "paid":paid,"external":external,"projectable":projectable,
            "split_changing":split_ch,"split_neutral":split_ne,"vector":vector}

def complete(bits: tuple[int,...],kind: str)->tuple[int,...]:
    x=list(bits)
    if kind=="D3": x[3]=x[2]; x[5]=x[4]
    elif kind=="D4": x[2]=x[3]; x[4]=x[5]
    else: raise AuditError(kind)
    return tuple(x)

def units(split_count: int)->dict[str,int]:
    req(split_count in (0,1,2),"split count")
    values=4 if split_count==0 else 5
    descent=4+split_count; routes=4+split_count; classifier=int(split_count>0)
    return {"scalar_value_records":values,"paid_strict_descent_records":descent,
            "external_route_records":routes,"D3_D4_classifier_records":classifier,
            "total_differential_source_units":values+descent+routes+classifier}

def compile_manifest(root: Path)->dict[str,Any]:
    face,route,trans=load(root,FACE),load(root,ROUTE),load(root,TRANS)
    req(face.get("schema")=="exact-recurrent-first-host-minimizer-face-scalar-route-cover/v1","face schema")
    req(route.get("schema")=="exact-recurrent-first-host-closure-route-source-gate/v1","route schema")
    req(trans.get("schema")=="exact-recurrent-first-host-transition-domain-source-audit/v1","transition schema")
    req(face.get("host_id")==HOST and trans.get("scope",{}).get("host_id")==HOST,"host")
    req(face.get("face_graph",{}).get("graph_type")=="complete-bipartite-K2,3","K2,3")
    req(face.get("aggregate",{}).get("acyclic_face_scalar_covers")==46,"46 covers")
    req(face.get("aggregate",{}).get("menu_projectable_face_covers")==14,"14 projectable")
    req(face.get("aggregate",{}).get("background_sensitive_face_covers")==32,"32 sensitive")
    req(route.get("aggregate",{}).get("route_classes")==5,"route classes")
    req(route.get("aggregate",{}).get("source_admissible_edge_route_pairs")==0,"route source")
    req(trans.get("aggregate",{}).get("required_promotion_fields_per_edge")==12,"transition fields")
    req(trans.get("aggregate",{}).get("physical_directed_edges")==0,"physical edges")

    covers={}
    for bits in itertools.product((0,1),repeat=6):
        r=row(bits)
        if dag(r["paid"]): covers[bits]=r
    projectable=[r for r in covers.values() if r["projectable"]]
    sensitive=[r for r in covers.values() if not r["projectable"]]
    req((len(covers),len(projectable),len(sensitive))==(46,14,32),"reconstruction")

    registry=face.get("orientation_registry",{})
    req(set(registry.get("ids",[]))=={r["id"] for r in covers.values()},"all IDs")
    req(set(registry.get("menu_projectable_ids",[]))=={r["id"] for r in projectable},"menu IDs")
    req(set(registry.get("background_sensitive_ids",[]))=={r["id"] for r in sensitive},"sensitive IDs")

    records=[]; profile={"one_family_split":0,"both_families_split":0}
    for r in sorted(sensitive,key=lambda x:x["id"]):
        d3,d4=covers[complete(r["bits"],"D3")],covers[complete(r["bits"],"D4")]
        req(d3["projectable"] and d4["projectable"] and d3["id"]!=d4["id"],"completions")
        for edge in STATE_EDGES:
            req(4*r["vector"][edge]==3*d3["vector"][edge]+d4["vector"][edge],"convex identity")
        split=int(r["split_changing"])+int(r["split_neutral"])
        kind="one_family_split" if split==1 else "both_families_split"; profile[kind]+=1
        records.append({"background_sensitive_cover_id":r["id"],
                        "D3_completion_cover_id":d3["id"],"D4_completion_cover_id":d4["id"],
                        "convex_weights":{"D3_completion":"3/4","D4_completion":"1/4"},
                        "split_profile":kind,"source_units":units(split)})
    req(profile=={"one_family_split":24,"both_families_split":8},"split profile")
    digest=hashlib.sha256(canon(records).encode()).hexdigest()

    return {
      "schema":"exact-recurrent-first-host-minimizer-face-source-leverage/v1","host_id":HOST,
      "sources":{"minimizer_face_scalar_route_cover":str(FACE),
                 "closure_route_source_gate":str(ROUTE),
                 "transition_domain_source_audit":str(TRANS)},
      "class_blind_cost_theorem":{
        "cost_scope":"nonnegative per-occurrence external-route costs depending on the directed menu-state edge but not on whether restore-both has face D3 or D4",
        "identity":"C(O)=3/4*C(O_D3)+1/4*C(O_D4)",
        "consequence":"min(C(O_D3),C(O_D4)) <= C(O) for every background-sensitive cover O",
        "background_sensitive_covers_strictly_better_than_all_projectable_covers":0,
        "background_sensitive_covers_with_projectable_no-worse_completion":32},
      "class_sensitive_cost_theorem":{
        "cost_scope":"nonnegative external-route costs allowed to distinguish all six directed face-pair domains",
        "background_sensitive_covers_constructively_uniquely_optimal":32,
        "construction":"assign cost zero to the desired cover's external direction in each face pair and positive cost to every reverse direction",
        "physical_D3_D4_cost_or_route_asymmetry_required":1},
      "source_unit_contract":{
        "counting_rule":"differential record units only; common occurrence-domain, owner, legality, boundedness, and realization contracts are required by all modes",
        "uniformity_rule":"D3 and D4 share one descent or route record only when their directions agree and a source theorem is uniform over both face classes",
        "menu_projectable":{"covers":14,**units(0)},
        "one_family_split":{"covers":24,**units(1)},
        "both_families_split":{"covers":8,**units(2)}},
      "D3_D4_classifier_contract":{
        "field_count":8,
        "fields":["physical_occurrence_domain_ref","restore_both_state_domain_ref",
                  "safe_background_or_equivalent_signature_ref","D3_characterization_ref",
                  "D4_characterization_ref","disjointness_ref","completeness_ref",
                  "realization_status"],
        "populated_fields":0,"accepted_classifier_records":0},
      "decomposition_registry":{
        "record_count":len(records),
        "background_sensitive_cover_ids":[r["background_sensitive_cover_id"] for r in records],
        "D3_completion_cover_ids":[r["D3_completion_cover_id"] for r in records],
        "D4_completion_cover_ids":[r["D4_completion_cover_id"] for r in records],
        "digest":digest},
      "aggregate":{
        "face_scalar_covers":46,"menu_projectable_covers":14,
        "background_sensitive_covers":32,"one_family_split_covers":24,
        "both_families_split_covers":8,"D3_completion_projectable":32,
        "D4_completion_projectable":32,"exact_convex_decompositions":32,
        "class_blind_dominated_or_tied_sensitive_covers":32,
        "class_blind_strictly_advantageous_sensitive_covers":0,
        "class_sensitive_potentially_advantageous_sensitive_covers":32,
        "minimum_projectable_differential_source_units":12,
        "minimum_background_sensitive_differential_source_units":16,
        "maximum_background_sensitive_differential_source_units":18,
        "current_physical_face_classifications":0,
        "current_source_face_scalar_values":0,"current_source_face_edge_routes":0,
        "current_physical_directed_edges":0},
      "source_boundary":{
        "background_sensitive_cover_admissible_without_D3_D4_classifier":0,
        "background_sensitive_cover_preferred_by_class_blind_cost":0,
        "class_sensitive_advantage_is_physical_evidence_dependent":1,
        "route_burden_reduction_proved":0,"promotion_to_recurrent_closure_allowed":0},
      "honesty":{
        "physical_occurrence_coverage_proved":0,
        "physical_minimizer_face_classification_proved":0,
        "physical_transition_legality_proved":0,"persistent_owner_identity_proved":0,
        "recurrent_child_rows_populated":0,"strict_lyapunov_certificate_proved":0,
        "global_termination_proved":0,"all_n_proved_by_checker":0}}

def validate(root: Path,value: dict[str,Any])->None:
    req(value==compile_manifest(root),"deterministic manifest")
def mutation(root: Path,expected: dict[str,Any])->int:
    edits=[]
    def add(path: tuple[str,...],value: Any):
        x=copy.deepcopy(expected); node=x
        for key in path[:-1]: node=node[key]
        node[path[-1]]=value; edits.append(x)
    for path,value in [
      (("aggregate","face_scalar_covers"),45),
      (("aggregate","menu_projectable_covers"),13),
      (("aggregate","background_sensitive_covers"),31),
      (("aggregate","one_family_split_covers"),23),
      (("aggregate","both_families_split_covers"),7),
      (("aggregate","D3_completion_projectable"),31),
      (("aggregate","D4_completion_projectable"),31),
      (("aggregate","exact_convex_decompositions"),31),
      (("aggregate","class_blind_strictly_advantageous_sensitive_covers"),1),
      (("aggregate","minimum_background_sensitive_differential_source_units"),15),
      (("aggregate","maximum_background_sensitive_differential_source_units"),17),
      (("D3_D4_classifier_contract","field_count"),7),
      (("D3_D4_classifier_contract","populated_fields"),1),
      (("class_blind_cost_theorem","background_sensitive_covers_strictly_better_than_all_projectable_covers"),1),
      (("class_sensitive_cost_theorem","background_sensitive_covers_constructively_uniquely_optimal"),31),
      (("source_boundary","route_burden_reduction_proved"),1),
      (("source_boundary","promotion_to_recurrent_closure_allowed"),1),
      (("honesty","all_n_proved_by_checker"),1)]: add(path,value)
    rejected=0
    for x in edits:
        try: validate(root,x)
        except AuditError: rejected+=1
    req(rejected==18,"mutation audit"); return rejected

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--write",type=Path); p.add_argument("--check",type=Path)
    p.add_argument("--mutation-audit",action="store_true"); a=p.parse_args()
    value=compile_manifest(a.root)
    if a.write:
        path=a.root/a.write; path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(canon(value)+"\n")
    if a.check: validate(a.root,load(a.root,a.check))
    if a.mutation_audit: print(f"mutation rejections: {mutation(a.root,value)}")
    print(json.dumps(value["aggregate"],sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
