#!/usr/bin/env python3
"""Compile the exact D3/D4 cost-dominance theorem for first-host face scalars."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path

HOST = "s4-75b04c45c1c8eac2"
FACE = Path("data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json")
ROUTE = Path("data/exact_recurrent_first_host_closure_route_source_gate.json")
DOMAIN = Path("data/exact_recurrent_first_host_transition_domain_source_audit.json")
V = ("A","B","C","D3","D4")
P = (
 ("AB","A","B","00","01",32), ("AC","A","C","00","10",32),
 ("BD3","B","D3","01","11",24), ("BD4","B","D4","01","11",8),
 ("CD3","C","D3","10","11",24), ("CD4","C","D4","10","11",8),
)
EDGES=("00->01","01->00","00->10","10->00","01->11","11->01","10->11","11->10")
FIELDS=("physical_occurrence_domain_ref","restore_both_face_partition_ref",
"d3_domain_completeness_ref","d4_domain_completeness_ref",
"split_pair_route_cost_ref","split_pair_route_admissibility_ref",
"class_sensitive_benefit_theorem_ref","realization_status")

class AuditError(RuntimeError): pass
def req(x,m):
    if not x: raise AuditError(m)
def load(root,p):
    q=root/p; req(q.is_file(),f"missing {p}")
    x=json.loads(q.read_text()); req(isinstance(x,dict),f"object {p}"); return x
def sid(payload):
    s=json.dumps(payload,sort_keys=True,separators=(",",":"))
    return "face-cover-"+hashlib.sha256(s.encode()).hexdigest()[:12]
def dirs(bits):
    return tuple((a,b) if z else (b,a) for z,(_,a,b,*_) in zip(bits,P))
def acyclic(ds):
    out={x:[] for x in V}; deg={x:0 for x in V}
    for a,b in ds: out[a].append(b); deg[b]+=1
    q=sorted(x for x in V if deg[x]==0); n=0
    while q:
        a=q.pop(0); n+=1
        for b in sorted(out[a]):
            deg[b]-=1
            if deg[b]==0: q.append(b); q.sort()
    return n==len(V)
def projectable(b): return b[2]==b[3] and b[4]==b[5]
def cid(b):
    return sid({"paid":sorted(f"{a}->{c}" for a,c in dirs(b)),
                "projectable":int(projectable(b))})
def state_edge(a,b):
    s={"A":"00","B":"01","C":"10","D3":"11","D4":"11"}
    return f"{s[a]}->{s[b]}"
def vector(bits,external=False):
    x={e:0 for e in EDGES}
    for z,(_,a,b,_,_,count) in zip(bits,P):
        u,v=(a,b) if z else (b,a)
        if external: u,v=v,u
        x[state_edge(u,v)]+=count
    return x
def convex(s,a,b):
    return all(4*s[e]==3*a[e]+b[e] for e in EDGES)

def compile(root):
    face,route,domain=load(root,FACE),load(root,ROUTE),load(root,DOMAIN)
    req(face.get("schema")=="exact-recurrent-first-host-minimizer-face-scalar-route-cover/v1","face schema")
    req(route.get("schema")=="exact-recurrent-first-host-closure-route-source-gate/v1","route schema")
    req(domain.get("schema")=="exact-recurrent-first-host-transition-domain-source-audit/v1","domain schema")
    req(face.get("host_id")==HOST and route.get("scope",{}).get("host_id")==HOST and
        domain.get("scope",{}).get("host_id")==HOST,"host")
    a=face.get("aggregate",{})
    req((a.get("acyclic_face_scalar_covers"),a.get("menu_projectable_face_covers"),
         a.get("background_sensitive_face_covers"),a.get("external_occurrence_edges_per_background"))
        ==(46,14,32,4),"face census")
    req(route.get("aggregate",{}).get("source_admissible_edge_route_pairs")==0,"route source")
    req(domain.get("aggregate",{}).get("physical_directed_edges")==0,"physical edges")
    reg=face.get("orientation_registry",{})
    all_ids,menu_ids,sens_ids=map(set,(reg.get("ids",[]),reg.get("menu_projectable_ids",[]),
                                      reg.get("background_sensitive_ids",[])))
    req((len(all_ids),len(menu_ids),len(sens_ids))==(46,14,32),"registry census")
    seen={}; records=[]; pairs={}; degree={x:0 for x in menu_ids}
    split={"changing_only":0,"neutral_only":0,"both":0}; domains={"5":0,"6":0}
    for bits in itertools.product((0,1),repeat=6):
        if not acyclic(dirs(bits)): continue
        i=cid(bits); req(i not in seen,"duplicate id"); seen[i]=bits
        if projectable(bits): continue
        d3=list(bits); d3[3]=d3[2]; d3[5]=d3[4]; d3=tuple(d3)
        d4=list(bits); d4[2]=d4[3]; d4[4]=d4[5]; d4=tuple(d4)
        req(projectable(d3) and projectable(d4) and acyclic(dirs(d3)) and acyclic(dirs(d4)),"completions")
        i3,i4=cid(d3),cid(d4); req(i3 in menu_ids and i4 in menu_ids and i3!=i4,"completion ids")
        req(convex(vector(bits),vector(d3),vector(d4)),"paid convexity")
        req(convex(vector(bits,True),vector(d3,True),vector(d4,True)),"external convexity")
        sc,sn=bits[2]!=bits[3],bits[4]!=bits[5]
        profile="both" if sc and sn else "changing_only" if sc else "neutral_only"
        n=6 if profile=="both" else 5
        split[profile]+=1; domains[str(n)]+=1
        pair=tuple(sorted((i3,i4))); pairs[pair]=pairs.get(pair,0)+1
        records.append({"sensitive_cover_id":i,"copy_d3_completion_id":i3,
                        "copy_d4_completion_id":i4,"split_profile":profile,
                        "source_route_domains_if_used":n})
    req(set(seen)==all_ids,"all ids")
    req({i for i,b in seen.items() if projectable(b)}==menu_ids,"menu ids")
    req({r["sensitive_cover_id"] for r in records}==sens_ids,"sensitive ids")
    req(split=={"changing_only":12,"neutral_only":12,"both":8},"split census")
    req(domains=={"5":24,"6":8},"domain census")
    req(len(pairs)==16 and set(pairs.values())=={2},"completion pairs")
    for x,y in pairs: degree[x]+=1; degree[y]+=1
    dd={}
    for d in degree.values(): dd[str(d)]=dd.get(str(d),0)+1
    req(dd=={"2":10,"3":4},"degree census")
    records.sort(key=lambda r:r["sensitive_cover_id"])
    pair_rows=[{"completion_ids":list(k),"sensitive_mixtures":v} for k,v in sorted(pairs.items())]
    digest=hashlib.sha256(json.dumps([records,pair_rows],sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {
      "schema":"exact-recurrent-first-host-minimizer-face-cost-dominance/v1","host_id":HOST,
      "sources":{"face_scalar_route_cover":str(FACE),"closure_route_source_gate":str(ROUTE),
                 "transition_domain_source_audit":str(DOMAIN)},
      "dominance_theorem":{"background_sensitive_covers":32,"ordered_completion_maps":32,
        "unordered_completion_pairs":16,"sensitive_mixtures_per_unordered_pair":2,
        "copy_d3_weight":"3/4","copy_d4_weight":"1/4",
        "componentwise_paid_identity":"4*S=3*C_D3+C_D4",
        "componentwise_external_identity":"4*S=3*C_D3+C_D4",
        "class_blind_linear_cost_dominated_covers":32,
        "ordinary_completion_always_no_more_expensive":1,
        "class_blind_route_feasibility_adds_new_cover":0,
        "both_ordinary_completions_feasible_when_sensitive_cover_is_class_blind_feasible":1},
      "completion_graph":{"ordinary_vertices":14,"unordered_edges":16,
                          "degree_distribution":dd,"edge_multiplicity":2},
      "source_interface":{"ordinary_menu_route_domains_per_cover":4,
        "sensitive_source_route_domain_distribution":domains,
        "advantage_evidence_fields":list(FIELDS),"advantage_evidence":{f:None for f in FIELDS},
        "populated_advantage_evidence_fields":0,
        "accepted_d3_d4_sensitive_advantage_theorems":0},
      "aggregate":{"face_scalar_covers":46,"menu_projectable_covers":14,
        "background_sensitive_covers":32,"single_family_split_covers":24,
        "both_family_split_covers":8,"sensitive_covers_requiring_five_route_domains":24,
        "sensitive_covers_requiring_six_route_domains":8,
        "minimum_external_occurrence_edges_per_background":4,
        "source_admissible_edge_route_pairs":0,"physical_directed_edges":0},
      "source_boundary":{"background_sensitive_cover_can_beat_menu_cover_under_class_blind_linear_cost":0,
        "background_sensitive_cover_adds_class_blind_route_feasibility":0,
        "strict_advantage_requires_d3_d4_sensitive_cost_or_feasibility":1,
        "score_face_split_alone_supplies_physical_cost_difference":0,
        "physical_d3_d4_partition_source_imported":0,
        "promotion_to_recurrent_closure_allowed":0},
      "registry":{"digest":digest,"sensitive_records":records,"completion_pairs":pair_rows},
      "honesty":{"physical_occurrence_coverage_proved":0,
        "physical_minimizer_face_classification_proved":0,
        "physical_transition_legality_proved":0,"persistent_owner_identity_proved":0,
        "recurrent_child_rows_populated":0,"strict_lyapunov_certificate_proved":0,
        "global_termination_proved":0,"all_n_proved_by_checker":0}}

def validate(x):
    req(x.get("schema")=="exact-recurrent-first-host-minimizer-face-cost-dominance/v1","schema")
    d=x["dominance_theorem"]; a=x["aggregate"]; s=x["source_interface"]; b=x["source_boundary"]; h=x["honesty"]
    checks=(d["background_sensitive_covers"]==32,d["unordered_completion_pairs"]==16,
      d["ordinary_completion_always_no_more_expensive"]==1,
      d["class_blind_route_feasibility_adds_new_cover"]==0,
      x["completion_graph"]["degree_distribution"]=={"2":10,"3":4},
      a["sensitive_covers_requiring_five_route_domains"]==24,
      a["sensitive_covers_requiring_six_route_domains"]==8,
      a["minimum_external_occurrence_edges_per_background"]==4,
      s["populated_advantage_evidence_fields"]==0,
      s["accepted_d3_d4_sensitive_advantage_theorems"]==0,
      b["strict_advantage_requires_d3_d4_sensitive_cost_or_feasibility"]==1,
      b["promotion_to_recurrent_closure_allowed"]==0,h["all_n_proved_by_checker"]==0)
    req(all(checks),"invariant")

def mutate_tests(x):
    paths=(("dominance_theorem","background_sensitive_covers",31),
      ("dominance_theorem","unordered_completion_pairs",15),
      ("dominance_theorem","ordinary_completion_always_no_more_expensive",0),
      ("dominance_theorem","class_blind_route_feasibility_adds_new_cover",1),
      ("completion_graph","degree_distribution",{"2":9,"3":4}),
      ("aggregate","sensitive_covers_requiring_five_route_domains",23),
      ("aggregate","sensitive_covers_requiring_six_route_domains",7),
      ("aggregate","minimum_external_occurrence_edges_per_background",3),
      ("source_interface","populated_advantage_evidence_fields",1),
      ("source_interface","accepted_d3_d4_sensitive_advantage_theorems",1),
      ("source_boundary","strict_advantage_requires_d3_d4_sensitive_cost_or_feasibility",0),
      ("source_boundary","promotion_to_recurrent_closure_allowed",1),
      ("honesty","all_n_proved_by_checker",1))
    for top,key,value in paths:
        y=copy.deepcopy(x); y[top][key]=value
        try: validate(y)
        except AuditError: continue
        raise AuditError(f"mutation survived: {top}.{key}")

def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--write",type=Path); p.add_argument("--check",type=Path); p.add_argument("--self-test",action="store_true")
    z=p.parse_args(); x=compile(z.root); validate(x)
    if z.write:
        q=z.root/z.write; q.parent.mkdir(parents=True,exist_ok=True)
        q.write_text(json.dumps(x,sort_keys=True,separators=(",",":"))+"\n")
    if z.check:
        req(x==json.loads((z.root/z.check).read_text()),"manifest mismatch")
    if z.self_test: mutate_tests(x)
    if not (z.write or z.check or z.self_test): print(json.dumps(x,indent=2,sort_keys=True))
if __name__=="__main__": main()
