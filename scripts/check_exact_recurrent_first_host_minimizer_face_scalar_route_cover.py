#!/usr/bin/env python3
"""Classify scalar covers on exact first-host complete minimizer faces."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path
from typing import Any

HOST = "s4-75b04c45c1c8eac2"
FACE = Path("data/exact_recurrent_first_host_restoration_selector_face.json")
BOUNDARY = Path("data/exact_recurrent_first_host_selector_boolean_boundary.json")
MENU = Path("data/exact_recurrent_first_host_menu_interaction_potential.json")
VERTICES = ("A", "B", "C", "D3", "D4")
# id,left,right,left-state,right-state,bit,selected-changing,count,class
PAIRS = (
 ("AB","A","B","00","01","r20",1,32,"all"),
 ("AC","A","C","00","10","r02",1,32,"all"),
 ("BD3","B","D3","01","11","r02",1,24,"three-way"),
 ("BD4","B","D4","01","11","r02",1,8,"four-way"),
 ("CD3","C","D3","10","11","r20",0,24,"three-way"),
 ("CD4","C","D4","10","11","r20",0,8,"four-way"),
)
STATE = {"A":"00","B":"01","C":"10","D3":"11","D4":"11"}
RESTORE = {"00->01","00->10","01->11","10->11"}

class AuditError(RuntimeError): pass
def req(ok: bool, msg: str) -> None:
    if not ok: raise AuditError(msg)
def load(root: Path, path: Path) -> dict[str, Any]:
    value=json.loads((root/path).read_text())
    req(isinstance(value,dict),str(path)); return value
def sid(payload: object) -> str:
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"))
    return "face-cover-"+hashlib.sha256(raw.encode()).hexdigest()[:12]
def dag(edges: list[tuple[str,str]]) -> bool:
    out={v:[] for v in VERTICES}; deg={v:0 for v in VERTICES}
    for a,b in edges: out[a].append(b); deg[b]+=1
    q=sorted(v for v in VERTICES if deg[v]==0); seen=0
    while q:
        v=q.pop(0); seen+=1
        for w in sorted(out[v]):
            deg[w]-=1
            if deg[w]==0: q.append(w); q.sort()
    return seen==len(VERTICES)
def sdir(edge: tuple[str,str]) -> str:
    return f"{STATE[edge[0]]}->{STATE[edge[1]]}"

def compile_manifest(root: Path) -> dict[str, Any]:
    faces,boundary,menu=load(root,FACE),load(root,BOUNDARY),load(root,MENU)
    req(faces.get("schema")=="exact-recurrent-first-host-restoration-selector-face/v1","face schema")
    req(boundary.get("schema")=="exact-recurrent-first-host-selector-boolean-boundary/v3","boundary schema")
    req(menu.get("schema")=="exact-recurrent-first-host-menu-interaction-potential/v1","menu schema")
    for source in (faces,boundary,menu): req(source.get("scope",{}).get("host_id")==HOST,"host")
    mf=faces["menus"]
    req(mf["blocked"]["minimizer_faces"]==[{"background_count":32,"face":["3012"]}],"A")
    req(mf["restore_20"]["minimizer_faces"]==[{"background_count":32,"face":["3201"]}],"B")
    req(mf["restore_02"]["minimizer_faces"]==[{"background_count":32,"face":["2031","2310"]}],"C")
    req(mf["restore_both"]["minimizer_faces"]==[
      {"background_count":8,"face":["2031","2301","2310","3201"]},
      {"background_count":24,"face":["2031","2310","3201"]}],"D")
    req(faces["aggregate"]["total_distinct_minimizer_faces"]==5,"five faces")
    req(boundary["aggregate"]["directed_single_bit_context_edges"]==8,"state edges")
    req(menu["aggregate"]["acyclic_menu_orientations"]==14,"menu covers")
    menu_sets={tuple(sorted(row["paid_menu_edges"])) for row in menu["orientations"]}
    req(len(menu_sets)==14,"menu sets")

    rows=[]; cyclic=0; profile={"menu":0,"changing":0,"neutral":0,"both":0}
    restore_dist={}; projected=set()
    for bits in itertools.product((0,1),repeat=6):
        edges=[(p[1],p[2]) if bit else (p[2],p[1]) for p,bit in zip(PAIRS,bits)]
        if not dag(edges): cyclic+=1; continue
        by={p[0]:e for p,e in zip(PAIRS,edges)}
        split_ch=(by["BD3"][0]=="B")!=(by["BD4"][0]=="B")
        split_ne=(by["CD3"][0]=="C")!=(by["CD4"][0]=="C")
        projectable=not split_ch and not split_ne
        key="menu" if projectable else "both" if split_ch and split_ne else "changing" if split_ch else "neutral"
        profile[key]+=1
        paid=sorted(f"{a}->{b}" for a,b in edges)
        if projectable:
            m=tuple(sorted(sdir(by[p]) for p in ("AB","AC","BD3","CD3")))
            req(m in menu_sets,"menu projection"); projected.add(m)
        restore_types=sum(sdir(e) in RESTORE for e in edges)
        restore_dist[str(restore_types)]=restore_dist.get(str(restore_types),0)+1
        req(sum(p[7] for p in PAIRS)==128,"occurrence total")
        req(sum(p[7] for p in PAIRS if p[6])==96,"changing total")
        req(sum(p[7] for p in PAIRS if not p[6])==32,"neutral total")
        req(sum(p[7] for p in PAIRS if p[5]=="r02")==64,"r02 total")
        req(sum(p[7] for p in PAIRS if p[5]=="r20")==64,"r20 total")
        payload={"paid":paid,"projectable":int(projectable)}
        rows.append({"id":sid(payload),"projectable":int(projectable),
                     "split_changing":int(split_ch),"split_neutral":int(split_ne),
                     "paid_restore_pair_types":restore_types,"paid":paid})
    rows.sort(key=lambda r:r["id"])
    req(len(rows)==46 and cyclic==18,"orientation census")
    req(profile=={"menu":14,"changing":12,"neutral":12,"both":8},"profile")
    req(projected==menu_sets,"all menu covers")
    req(restore_dist=={"0":1,"1":6,"2":9,"3":14,"4":9,"5":6,"6":1},"restore dist")
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()

    return {
      "schema":"exact-recurrent-first-host-minimizer-face-scalar-route-cover/v1",
      "host_id":HOST,
      "sources":{"restoration_selector_face":str(FACE),"selector_boolean_boundary":str(BOUNDARY),
                 "menu_interaction_potential":str(MENU)},
      "face_graph":{
        "graph_type":"complete-bipartite-K2,3","bipartition":[["B","C"],["A","D3","D4"]],
        "vertices":[
          {"id":"A","face":["3012"],"states":["00"],"background_count":32},
          {"id":"B","face":["3201"],"states":["01"],"background_count":32},
          {"id":"C","face":["2031","2310"],"states":["10"],"background_count":32},
          {"id":"D3","face":["2031","2310","3201"],"states":["11"],"background_count":24},
          {"id":"D4","face":["2031","2301","2310","3201"],"states":["11"],"background_count":8}],
        "pairs":[{"id":p[0],"vertices":[p[1],p[2]],"states":[p[3],p[4]],"bit":p[5],
                  "selected_changing":p[6],"background_count":p[7],"background_class":p[8]} for p in PAIRS],
        "vertex_count":5,"undirected_pair_count":6,"directed_face_edge_types":12},
      "orientation_registry":{
        "ids":[r["id"] for r in rows],"digest":digest,
        "menu_projectable_ids":[r["id"] for r in rows if r["projectable"]],
        "background_sensitive_ids":[r["id"] for r in rows if not r["projectable"]]},
      "aggregate":{
        "safe_backgrounds":32,"menu_states":4,"distinct_minimizer_faces":5,
        "face_pair_orientations":64,"acyclic_face_scalar_covers":46,
        "cyclic_incompatible_orientations":18,"menu_projectable_face_covers":14,
        "background_sensitive_face_covers":32,
        "background_sensitive_changing_family_only":12,
        "background_sensitive_neutral_family_only":12,
        "background_sensitive_both_families":8,
        "existing_menu_scalar_covers":14,"projectable_face_covers_match_menu_covers":14,
        "paid_face_pair_types_per_cover":6,"external_face_pair_types_per_cover":6,
        "paid_occurrence_edges_per_safe_domain":128,
        "external_occurrence_edges_per_safe_domain":128,
        "external_occurrence_edges_per_background":4,
        "external_selected_changing_occurrence_edges_per_safe_domain":96,
        "external_selector_neutral_occurrence_edges_per_safe_domain":32,
        "external_r02_occurrence_edges_per_safe_domain":64,
        "external_r20_occurrence_edges_per_safe_domain":64,
        "paid_restore_pair_type_distribution":restore_dist,
        "physical_face_classifications_populated":0,
        "physical_face_scalar_values_populated":0,
        "physical_face_edge_routes_populated":0},
      "source_boundary":{
        "face_scalar_avoids_lexicographic_tie_break":1,
        "face_scalar_requires_exact_physical_minimizer_face":1,
        "menu_projectable_class_adds_no_scalar_cover":1,
        "background_sensitive_class_requires_D3_D4_source_separation":1,
        "background_sensitive_class_reduces_external_occurrence_burden":0,
        "minimum_external_occurrence_edges_per_background_remains_four":1,
        "minimum_external_selected_changing_edges_per_background_remains_three":1,
        "minimum_external_selector_neutral_edges_per_background_remains_one":1,
        "promotion_to_recurrent_closure_allowed":0},
      "honesty":{"physical_occurrence_coverage_proved":0,
        "physical_minimizer_face_classification_proved":0,
        "legal_restoration_operation_proved":0,"persistent_owner_identity_proved":0,
        "recurrent_child_rows_populated":0,"strict_lyapunov_certificate_proved":0,
        "global_termination_proved":0,"all_n_proved_by_checker":0}}

def validate(root: Path, value: dict[str, Any]) -> None:
    req(value==compile_manifest(root),"deterministic manifest")
def mutation(root: Path, expected: dict[str, Any]) -> int:
    edits=[]
    def add(fn): x=copy.deepcopy(expected); fn(x); edits.append(x)
    add(lambda x:x["face_graph"].__setitem__("graph_type","cycle"))
    for key,val in (("acyclic_face_scalar_covers",45),("cyclic_incompatible_orientations",17),
                    ("menu_projectable_face_covers",13),("background_sensitive_face_covers",31),
                    ("background_sensitive_changing_family_only",11),
                    ("projectable_face_covers_match_menu_covers",13),
                    ("external_occurrence_edges_per_background",3),
                    ("external_selected_changing_occurrence_edges_per_safe_domain",95),
                    ("external_selector_neutral_occurrence_edges_per_safe_domain",31),
                    ("external_r02_occurrence_edges_per_safe_domain",63)):
        add(lambda x,k=key,v=val:x["aggregate"].__setitem__(k,v))
    add(lambda x:x["aggregate"]["paid_restore_pair_type_distribution"].__setitem__("3",13))
    add(lambda x:x["orientation_registry"]["ids"].pop())
    add(lambda x:x["orientation_registry"].__setitem__("digest","0"*64))
    add(lambda x:x["source_boundary"].__setitem__("background_sensitive_class_reduces_external_occurrence_burden",1))
    add(lambda x:x["source_boundary"].__setitem__("promotion_to_recurrent_closure_allowed",1))
    add(lambda x:x["honesty"].__setitem__("strict_lyapunov_certificate_proved",1))
    add(lambda x:x["honesty"].__setitem__("all_n_proved_by_checker",1))
    rejected=0
    for x in edits:
        try: validate(root,x)
        except AuditError: rejected+=1
    req(rejected==18,"mutation audit"); return rejected

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--write",type=Path); p.add_argument("--check",type=Path)
    p.add_argument("--mutation-audit",action="store_true"); a=p.parse_args()
    value=compile_manifest(a.root)
    if a.write:
        path=a.root/a.write; path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n")
    if a.check: validate(a.root,load(a.root,a.check))
    if a.mutation_audit: print(f"mutation rejections: {mutation(a.root,value)}")
    print(json.dumps(value["aggregate"],sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
