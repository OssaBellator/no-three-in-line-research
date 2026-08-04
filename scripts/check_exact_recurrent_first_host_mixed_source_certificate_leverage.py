#!/usr/bin/env python3
"""Classify mixed state-impossibility and action-family source certificates."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path
from typing import Any

HOST = "s4-75b04c45c1c8eac2"
STATE_PATH = Path("data/exact_recurrent_first_host_state_exclusion_route_leverage.json")
FAMILY_PATH = Path("data/exact_recurrent_first_host_action_family_source_import_gate.json")
ADMISSION_PATH = Path("data/exact_recurrent_first_host_route_cover_admission.json")

STATES = ("00", "01", "10", "11")
SELECTED = {"00": "3012", "01": "3201", "10": "2031", "11": "2031"}
UNDIRECTED = (("00","01"),("00","10"),("01","11"),("10","11"))
FAMILIES = {
    "restore_02": ("00->10","01->11"),
    "delete_02": ("10->00","11->01"),
    "restore_20": ("00->01","10->11"),
    "delete_20": ("01->00","11->10"),
}
STATE_EVIDENCE_FIELDS = (
    "physical_occurrence_domain_ref",
    "state_definition_ref",
    "state_impossibility_theorem_ref",
    "domain_completeness_ref",
    "incident_edge_exclusion_ref",
    "realization_status",
)
FAMILY_EVIDENCE_FIELDS = (
    "shared_theorem_ref",
    "both_context_values_proved",
    "shared_owner_schema_ref",
    "shared_operation_schema_ref",
    "shared_route_schema_ref",
    "child_payment_compatibility_ref",
    "realization_status",
)

class AuditError(RuntimeError): pass
def req(ok: bool, msg: str) -> None:
    if not ok: raise AuditError(msg)
def load(root: Path, path: Path) -> dict[str, Any]:
    value=json.loads((root/path).read_text())
    req(isinstance(value,dict),str(path)); return value

def edges() -> set[str]:
    out=set()
    for a,b in UNDIRECTED:
        out.add(f"{a}->{b}"); out.add(f"{b}->{a}")
    return out

def state_edges(state: str) -> set[str]:
    return {e for e in edges() if e.startswith(state+"->") or e.endswith("->"+state)}

def label_covers() -> set[frozenset[str]]:
    changing={(f"{a}->{b}") for a,b in [(x,y) for x,y in UNDIRECTED]+[(y,x) for x,y in UNDIRECTED]
              if SELECTED[a]!=SELECTED[b]}
    labels=tuple(sorted(set(SELECTED.values())))
    covers=set()
    for order in itertools.permutations(labels):
        rank={x:i for i,x in enumerate(order)}
        paid={e for e in changing if rank[SELECTED[e[:2]]] > rank[SELECTED[e[4:]]]}
        covers.add(frozenset(changing-paid))
    req(len(covers)==6,"label cover count")
    return covers

def menu_covers() -> set[frozenset[str]]:
    covers=set()
    for order in itertools.permutations(STATES):
        rank={x:i for i,x in enumerate(order)}
        external=set()
        for a,b in UNDIRECTED:
            paid=(a,b) if rank[a]>rank[b] else (b,a)
            external.add(f"{paid[1]}->{paid[0]}")
        covers.add(frozenset(external))
    req(len(covers)==14,"menu cover count")
    return covers

def stable_id(kind: str, certs: frozenset[str]) -> str:
    payload={"kind":kind,"certificates":sorted(certs)}
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"))
    return "mixed-cert-"+hashlib.sha256(raw.encode()).hexdigest()[:12]

def minimal_sets(feasible_sets: list[frozenset[str]]) -> list[frozenset[str]]:
    return sorted([s for s in feasible_sets if not any(t<s for t in feasible_sets)],
                  key=lambda s:(len(s),sorted(s)))

def pattern_record(kind: str, certset: frozenset[str], cert_edges: dict[str,set[str]],
                   covers: set[frozenset[str]]) -> dict[str, Any]:
    closed=set()
    for c in certset: closed |= cert_edges[c]
    state_count=sum(c.startswith("state:") for c in certset)
    family_count=sum(c.startswith("family:") for c in certset)
    return {
        "id":stable_id(kind,certset),
        "certificates":sorted(certset),
        "certificate_count":len(certset),
        "state_certificates":state_count,
        "family_certificates":family_count,
        "source_evidence_slots":state_count*len(STATE_EVIDENCE_FIELDS)+family_count*len(FAMILY_EVIDENCE_FIELDS),
        "closed_edges":sorted(closed),
        "closed_edge_count":len(closed),
        "contained_scalar_covers":sum(c<=closed for c in covers),
    }

def compile_manifest(root: Path) -> dict[str, Any]:
    state=load(root,STATE_PATH); family=load(root,FAMILY_PATH); admission=load(root,ADMISSION_PATH)
    req(state.get("schema")=="exact-recurrent-first-host-state-exclusion-route-leverage/v1","state schema")
    req(state.get("scope",{}).get("host_id")==HOST,"state host")
    req(state.get("aggregate",{}).get("state_exclusion_patterns")==16,"state census")
    req(state.get("current_source_state",{}).get("source_backed_impossible_states")==[],"state source")
    req(family.get("schema")=="exact-recurrent-first-host-action-family-source-import-gate/v2","family schema")
    req(family.get("host_id")==HOST,"family host")
    req(family.get("aggregate",{}).get("action_families")==4,"family census")
    req(family.get("aggregate",{}).get("evidence_fields_per_family")==7,"family evidence")
    req(family.get("aggregate",{}).get("source_backed_uniform_family_imports")==0,"family source")
    family_rows={r["family_id"]:r for r in family.get("families",[])}
    req(set(family_rows)==set(FAMILIES),"family ids")
    for fid, expected in FAMILIES.items():
        row=family_rows[fid]
        req(tuple(row.get("edge_refs",[]))==expected,f"{fid} edges")
        req(row.get("family_import_accepted")==0 and row.get("evidence_fields_populated")==0,f"{fid} source")
    req(admission.get("schema")=="exact-recurrent-first-host-route-cover-admission/v1","admission schema")
    req(admission.get("host_id")==HOST,"admission host")
    req(admission.get("aggregate",{}).get("current_route_closed_edges")==0,"route source")
    req(admission.get("label_scalar",{}).get("minimal_feasible_masks")==6,"label covers")
    req(admission.get("menu_scalar",{}).get("minimal_feasible_masks")==14,"menu covers")

    label=label_covers(); menu=menu_covers()
    cert_edges={f"state:{s}":state_edges(s) for s in STATES}
    cert_edges.update({f"family:{f}":set(es) for f,es in FAMILIES.items()})
    names=tuple(cert_edges)
    subset_rows=[]; label_feasible=[]; menu_feasible=[]
    label_dist={}; menu_dist={}
    for size in range(len(names)+1):
        for combo in itertools.combinations(names,size):
            certset=frozenset(combo); closed=set()
            for c in certset: closed |= cert_edges[c]
            l=any(c<=closed for c in label); m=any(c<=closed for c in menu)
            if l:
                label_feasible.append(certset); label_dist[str(size)]=label_dist.get(str(size),0)+1
            if m:
                menu_feasible.append(certset); menu_dist[str(size)]=menu_dist.get(str(size),0)+1
            subset_rows.append((certset,closed,l,m))
    req(len(subset_rows)==256,"subset count")
    req(len(label_feasible)==215 and len(menu_feasible)==205,"feasible census")
    req(label_dist=={"2":11,"3":44,"4":67,"5":56,"6":28,"7":8,"8":1},"label distribution")
    req(menu_dist=={"2":6,"3":40,"4":66,"5":56,"6":28,"7":8,"8":1},"menu distribution")

    min_label=minimal_sets(label_feasible); min_menu=minimal_sets(menu_feasible)
    label_records=[pattern_record("label",s,cert_edges,label) for s in min_label]
    menu_records=[pattern_record("menu",s,cert_edges,menu) for s in min_menu]
    req(len(label_records)==13 and len(menu_records)==14,"minimal antichain")

    def profile(records: list[dict[str,Any]]) -> dict[str,int]:
        out={}
        for r in records:
            if r["state_certificates"] and r["family_certificates"]:
                key=f"mixed_{r['state_certificates']}s_{r['family_certificates']}f"
            elif r["state_certificates"]:
                key=f"pure_state_{r['state_certificates']}"
            else:
                key=f"pure_family_{r['family_certificates']}"
            out[key]=out.get(key,0)+1
        return out
    label_profile=profile(label_records); menu_profile=profile(menu_records)
    req(label_profile=={"pure_family_2":4,"mixed_1s_1f":4,"pure_state_2":3,"mixed_2s_1f":2},"label profile")
    req(menu_profile=={"pure_family_2":4,"pure_state_2":2,"mixed_2s_1f":8},"menu profile")

    mixed_pairs=[]
    for s in STATES:
        for f in FAMILIES:
            certset=frozenset((f"state:{s}",f"family:{f}"))
            closed=cert_edges[f"state:{s}"]|cert_edges[f"family:{f}"]
            if any(c<=closed for c in label):
                mixed_pairs.append(sorted(certset))
            req(not any(c<=closed for c in menu),"mixed pair menu shortcut")
    req(mixed_pairs==[
      ["family:restore_02","state:00"],["family:delete_02","state:00"],
      ["family:restore_02","state:01"],["family:delete_02","state:01"]],"mixed pair list")

    label_slots={}; menu_slots={}
    for r in label_records: label_slots[str(r["source_evidence_slots"])]=label_slots.get(str(r["source_evidence_slots"]),0)+1
    for r in menu_records: menu_slots[str(r["source_evidence_slots"])]=menu_slots.get(str(r["source_evidence_slots"]),0)+1
    req(label_slots=={"12":3,"13":4,"14":4,"19":2},"label slots")
    req(menu_slots=={"12":2,"14":4,"19":8},"menu slots")

    registry_payload={"label":label_records,"menu":menu_records}
    digest=hashlib.sha256(json.dumps(registry_payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {
      "schema":"exact-recurrent-first-host-mixed-source-certificate-leverage/v1",
      "host_id":HOST,
      "sources":{"state_exclusion_route_leverage":str(STATE_PATH),
                 "action_family_source_import_gate":str(FAMILY_PATH),
                 "route_cover_admission":str(ADMISSION_PATH)},
      "certificate_contracts":{
        "state_impossibility":{"certificate_ids":[f"state:{s}" for s in STATES],
          "structural_fields":["state_id"],"evidence_fields":list(STATE_EVIDENCE_FIELDS),
          "evidence_fields_per_certificate":6,"accepted_certificates":0,
          "populated_evidence_fields":0},
        "action_family":{"certificate_ids":[f"family:{f}" for f in FAMILIES],
          "evidence_fields":list(FAMILY_EVIDENCE_FIELDS),
          "evidence_fields_per_certificate":7,"accepted_certificates":0,
          "populated_evidence_fields":0}},
      "subset_census":{"certificate_types":8,"certificate_subsets":256,
        "label_feasible_subsets":215,"menu_feasible_subsets":205,
        "label_feasible_size_distribution":label_dist,
        "menu_feasible_size_distribution":menu_dist},
      "minimal_antichains":{
        "label":{"patterns":label_records,"pattern_count":13,"profile":label_profile,
                 "source_evidence_slot_distribution":label_slots,
                 "minimum_certificate_count":2,"minimum_source_evidence_slots":12},
        "menu":{"patterns":menu_records,"pattern_count":14,"profile":menu_profile,
                "source_evidence_slot_distribution":menu_slots,
                "minimum_certificate_count":2,"minimum_source_evidence_slots":12}},
      "mixed_pair_boundary":{
        "state_family_pairs":16,"label_complete_pairs":4,"menu_complete_pairs":0,
        "label_complete_pair_certificates":mixed_pairs,
        "state_11_plus_one_family_label_complete":0,
        "state_11_plus_one_family_menu_complete":0,
        "every_state_family_pair_needs_at_least_one_additional_menu_edge":1},
      "aggregate":{"minimal_label_patterns":13,"minimal_menu_patterns":14,
        "minimal_label_two_certificate_patterns":11,"minimal_label_three_certificate_patterns":2,
        "minimal_menu_two_certificate_patterns":6,"minimal_menu_three_certificate_patterns":8,
        "current_accepted_state_certificates":0,"current_accepted_family_certificates":0,
        "current_complete_label_covers":0,"current_complete_menu_covers":0},
      "source_boundary":{
        "one_state_plus_one_family_can_close_label_cover":1,
        "one_state_plus_one_family_can_close_menu_cover":0,
        "mixed_certificate_shortcut_is_conditional_on_both_source_gates":1,
        "state_absence_in_current_manifest_is_not_state_impossibility":1,
        "family_structure_is_not_uniform_family_import":1,
        "promotion_to_recurrent_closure_allowed":0},
      "registry":{"digest":digest},
      "honesty":{"physical_occurrence_coverage_proved":0,
        "physical_transition_legality_proved":0,"persistent_owner_identity_proved":0,
        "recurrent_child_rows_populated":0,"strict_lyapunov_certificate_proved":0,
        "global_termination_proved":0,"all_n_proved_by_checker":0}}
def validate(root: Path, value: dict[str,Any]) -> None:
    req(value==compile_manifest(root),"deterministic manifest")
def mutation(root: Path, expected: dict[str,Any]) -> int:
    edits=[]
    def add(fn): x=copy.deepcopy(expected); fn(x); edits.append(x)
    add(lambda x:x["subset_census"].__setitem__("certificate_subsets",255))
    add(lambda x:x["subset_census"].__setitem__("label_feasible_subsets",214))
    add(lambda x:x["subset_census"].__setitem__("menu_feasible_subsets",204))
    add(lambda x:x["minimal_antichains"]["label"].__setitem__("pattern_count",12))
    add(lambda x:x["minimal_antichains"]["menu"].__setitem__("pattern_count",13))
    add(lambda x:x["mixed_pair_boundary"].__setitem__("label_complete_pairs",3))
    add(lambda x:x["mixed_pair_boundary"].__setitem__("menu_complete_pairs",1))
    add(lambda x:x["mixed_pair_boundary"].__setitem__("state_11_plus_one_family_label_complete",1))
    add(lambda x:x["aggregate"].__setitem__("minimal_label_two_certificate_patterns",10))
    add(lambda x:x["aggregate"].__setitem__("minimal_menu_three_certificate_patterns",7))
    add(lambda x:x["certificate_contracts"]["state_impossibility"].__setitem__("accepted_certificates",1))
    add(lambda x:x["certificate_contracts"]["action_family"].__setitem__("accepted_certificates",1))
    add(lambda x:x["source_boundary"].__setitem__("state_absence_in_current_manifest_is_not_state_impossibility",0))
    add(lambda x:x["source_boundary"].__setitem__("family_structure_is_not_uniform_family_import",0))
    add(lambda x:x["source_boundary"].__setitem__("promotion_to_recurrent_closure_allowed",1))
    add(lambda x:x["registry"].__setitem__("digest","0"*64))
    add(lambda x:x["honesty"].__setitem__("global_termination_proved",1))
    add(lambda x:x["honesty"].__setitem__("all_n_proved_by_checker",1))
    rejected=0
    for x in edits:
        try: validate(root,x)
        except AuditError: rejected+=1
    req(rejected==18,"mutation audit")
    return rejected
def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path("."))
    p.add_argument("--write",type=Path); p.add_argument("--check",type=Path)
    p.add_argument("--self-test",action="store_true"); a=p.parse_args()
    value=compile_manifest(a.root)
    if a.write:
        path=a.root/a.write; path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n")
    if a.check: validate(a.root,load(a.root,a.check))
    if a.self_test: print(f"mutation rejections: {mutation(a.root,value)}")
    print(json.dumps(value["aggregate"],sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
