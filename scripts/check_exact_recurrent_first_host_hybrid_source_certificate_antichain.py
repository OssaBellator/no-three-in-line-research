#!/usr/bin/env python3
"""Classify state, family, and individual-edge source-certificate antichains."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path
from typing import Any

HOST = "s4-75b04c45c1c8eac2"
MIXED_PATH = Path("data/exact_recurrent_first_host_mixed_source_certificate_leverage.json")
ROUTE_PATH = Path("data/exact_recurrent_first_host_closure_route_source_gate.json")
ADMISSION_PATH = Path("data/exact_recurrent_first_host_route_cover_admission.json")
STATES = ("00", "01", "10", "11")
SELECTED = {"00":"3012", "01":"3201", "10":"2031", "11":"2031"}
UNDIRECTED = (("00","01"),("00","10"),("01","11"),("10","11"))
FAMILIES = {
    "restore_02": ("00->10","01->11"),
    "delete_02": ("10->00","11->01"),
    "restore_20": ("00->01","10->11"),
    "delete_20": ("01->00","11->10"),
}

class AuditError(RuntimeError): pass
def req(ok: bool, msg: str) -> None:
    if not ok: raise AuditError(msg)
def root() -> Path:
    here=Path(__file__).resolve()
    for candidate in (here.parent,*here.parents):
        if (candidate/"STATUS.md").is_file(): return candidate
    raise AuditError("repository root not found")
def load(repo: Path, path: Path) -> dict[str,Any]:
    value=json.loads((repo/path).read_text(encoding="utf-8"))
    req(isinstance(value,dict),str(path)); return value

def edges() -> tuple[str,...]:
    return tuple(sorted({f"{a}->{b}" for a,b in UNDIRECTED}|{f"{b}->{a}" for a,b in UNDIRECTED}))
def state_edges(state: str) -> set[str]:
    return {e for e in edges() if e.startswith(state+"->") or e.endswith("->"+state)}
def label_covers() -> set[frozenset[str]]:
    changing={e for e in edges() if SELECTED[e[:2]]!=SELECTED[e[4:]]}
    out=set()
    for order in itertools.permutations(sorted(set(SELECTED.values()))):
        rank={x:i for i,x in enumerate(order)}
        paid={e for e in changing if rank[SELECTED[e[:2]]]>rank[SELECTED[e[4:]]]}
        out.add(frozenset(changing-paid))
    req(len(out)==6,"label covers"); return out
def menu_covers() -> set[frozenset[str]]:
    out=set()
    for order in itertools.permutations(STATES):
        rank={x:i for i,x in enumerate(order)}; external=set()
        for a,b in UNDIRECTED:
            paid=(a,b) if rank[a]>rank[b] else (b,a)
            external.add(f"{paid[1]}->{paid[0]}")
        out.add(frozenset(external))
    req(len(out)==14,"menu covers"); return out

def stable_id(kind: str, certs: frozenset[str]) -> str:
    raw=json.dumps({"kind":kind,"certificates":sorted(certs)},sort_keys=True,separators=(",",":"))
    return "hybrid-cert-"+hashlib.sha256(raw.encode()).hexdigest()[:12]
def minimal_sets(feasible: list[frozenset[str]]) -> list[frozenset[str]]:
    return sorted((s for s in feasible if not any(t<s for t in feasible)),key=lambda s:(len(s),sorted(s)))
def profile_key(certs: frozenset[str]) -> str:
    s=sum(c.startswith("state:") for c in certs)
    f=sum(c.startswith("family:") for c in certs)
    e=sum(c.startswith("edge:") for c in certs)
    return f"{s}s_{f}f_{e}e"
def counts(items: list[int]) -> dict[str,int]:
    out: dict[str,int]={}
    for x in items: out[str(x)]=out.get(str(x),0)+1
    return dict(sorted(out.items(),key=lambda kv:int(kv[0])))

def compile_manifest(repo: Path) -> dict[str,Any]:
    mixed=load(repo,MIXED_PATH); route=load(repo,ROUTE_PATH); admission=load(repo,ADMISSION_PATH)
    req(mixed.get("schema")=="exact-recurrent-first-host-mixed-source-certificate-leverage/v1","mixed schema")
    req(mixed.get("host_id")==HOST,"mixed host")
    req(mixed.get("aggregate",{}).get("current_accepted_state_certificates")==0,"state source")
    req(mixed.get("aggregate",{}).get("current_accepted_family_certificates")==0,"family source")
    state_contract=mixed["certificate_contracts"]["state_impossibility"]
    family_contract=mixed["certificate_contracts"]["action_family"]
    req(state_contract["evidence_fields_per_certificate"]==6,"state field count")
    req(family_contract["evidence_fields_per_certificate"]==7,"family field count")
    req(route.get("schema")=="exact-recurrent-first-host-closure-route-source-gate/v1","route schema")
    req(route.get("scope",{}).get("host_id")==HOST,"route host")
    req(route.get("aggregate",{}).get("directed_edges")==8,"edge census")
    req(route.get("aggregate",{}).get("source_admissible_edge_route_pairs")==0,"route source")
    req(route.get("aggregate",{}).get("edges_with_route")==0,"edge source")
    req(admission.get("schema")=="exact-recurrent-first-host-route-cover-admission/v1","admission schema")
    req(admission.get("host_id")==HOST,"admission host")
    req(admission.get("aggregate",{}).get("current_route_closed_edges")==0,"admission source")

    route_costs={}
    for row in route.get("route_contracts",[]):
        route_costs[row["route"]]=len(row["base_physical_fields"])+len(row["route_specific_fields"])
    expected_costs={"physical_exclusion":5,"decorated_outer_reset":8,
                    "finite_unrestorable_capacity":9,
                    "terminal_or_improving_output":10,
                    "bounded_strict_potential":11}
    req(route_costs==expected_costs,"route evidence costs")
    edge_lower_bound=min(route_costs.values())

    label=label_covers(); menu=menu_covers()
    cert_edges={f"state:{s}":state_edges(s) for s in STATES}
    cert_edges.update({f"family:{f}":set(es) for f,es in FAMILIES.items()})
    cert_edges.update({f"edge:{e}":{e} for e in edges()})
    names=tuple(cert_edges)
    req(len(names)==16,"certificate universe")
    label_feasible=[]; menu_feasible=[]; label_dist={}; menu_dist={}
    for size in range(17):
        for combo in itertools.combinations(names,size):
            certs=frozenset(combo); closed=set()
            for c in certs: closed|=cert_edges[c]
            if any(c<=closed for c in label):
                label_feasible.append(certs); label_dist[str(size)]=label_dist.get(str(size),0)+1
            if any(c<=closed for c in menu):
                menu_feasible.append(certs); menu_dist[str(size)]=menu_dist.get(str(size),0)+1
    req(len(label_feasible)==62564,"label subset census")
    req(len(menu_feasible)==61679,"menu subset census")
    req(label_dist=={"2":19,"3":236,"4":1205,"5":3612,"6":7377,"7":11080,"8":12735,"9":11410,"10":8005,"11":4368,"12":1820,"13":560,"14":120,"15":16,"16":1},"label distribution")
    req(menu_dist=={"2":6,"3":160,"4":1028,"5":3376,"6":7170,"7":10960,"8":12690,"9":11400,"10":8004,"11":4368,"12":1820,"13":560,"14":120,"15":16,"16":1},"menu distribution")
    min_label=minimal_sets(label_feasible); min_menu=minimal_sets(menu_feasible)
    req(len(min_label)==51 and len(min_menu)==100,"antichain sizes")

    def closed(certs: frozenset[str]) -> set[str]:
        out=set()
        for c in certs: out|=cert_edges[c]
        return out
    def evidence(certs: frozenset[str], edge_cost: int=edge_lower_bound) -> int:
        return (sum(c.startswith("state:") for c in certs)*6+
                sum(c.startswith("family:") for c in certs)*7+
                sum(c.startswith("edge:") for c in certs)*edge_cost)
    def antichain_summary(kind: str, patterns: list[frozenset[str]]) -> dict[str,Any]:
        profile={}
        for p in patterns: profile[profile_key(p)]=profile.get(profile_key(p),0)+1
        ids=[stable_id(kind,p) for p in patterns]
        payload=[{"id":stable_id(kind,p),"certificates":sorted(p),
                  "closed_edges":sorted(closed(p))} for p in patterns]
        return {"pattern_count":len(patterns),
                "certificate_count_distribution":counts([len(p) for p in patterns]),
                "profile":dict(sorted(profile.items())),
                "physical_exclusion_lower_bound_slot_distribution":counts([evidence(p) for p in patterns]),
                "minimum_certificate_count":min(map(len,patterns)),
                "minimum_physical_exclusion_lower_bound_slots":min(evidence(p) for p in patterns),
                "registry_id_digest":hashlib.sha256(json.dumps(ids,separators=(",",":")).encode()).hexdigest(),
                "registry_digest":hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()}
    label_summary=antichain_summary("label",min_label); menu_summary=antichain_summary("menu",min_menu)
    req(label_summary["certificate_count_distribution"]=={"2":19,"3":32},"label minimal size")
    req(menu_summary["certificate_count_distribution"]=={"2":6,"3":80,"4":14},"menu minimal size")
    req(label_summary["profile"]=={"0s_0f_3e":6,"0s_1f_1e":4,"0s_1f_2e":6,"0s_2f_0e":4,"1s_0f_1e":4,"1s_0f_2e":8,"1s_1f_0e":4,"1s_1f_1e":8,"2s_0f_0e":3,"2s_0f_1e":2,"2s_1f_0e":2},"label profile")
    req(menu_summary["profile"]=={"0s_0f_4e":14,"0s_1f_2e":16,"0s_2f_0e":4,"1s_0f_2e":16,"1s_1f_1e":32,"2s_0f_0e":2,"2s_0f_1e":8,"2s_1f_0e":8},"menu profile")
    req(label_summary["physical_exclusion_lower_bound_slot_distribution"]=={"11":4,"12":7,"13":4,"14":4,"15":6,"16":8,"17":8,"18":8,"19":2},"label slot distribution")
    req(menu_summary["physical_exclusion_lower_bound_slot_distribution"]=={"12":2,"14":4,"16":16,"17":24,"18":32,"19":8,"20":14},"menu slot distribution")

    best_label=[p for p in min_label if evidence(p)==11]
    expected_best=[frozenset(("state:01","edge:00->10")),frozenset(("state:00","edge:01->11")),
                   frozenset(("state:01","edge:10->00")),frozenset(("state:00","edge:11->01"))]
    req(best_label==sorted(expected_best,key=lambda s:(len(s),sorted(s))),"best label patterns")
    state_edge_label=[p for p in min_label if profile_key(p)=="1s_0f_1e"]
    family_edge_label=[p for p in min_label if profile_key(p)=="0s_1f_1e"]
    req(len(state_edge_label)==4 and len(family_edge_label)==4,"macro edge pairs")
    req(not any(profile_key(p) in {"1s_0f_1e","0s_1f_1e","1s_1f_0e"} for p in min_menu),"menu two-certificate hybrid")

    route_class_minima={}
    for route_name,edge_cost in sorted(route_costs.items()):
        lmin=min(evidence(p,edge_cost) for p in min_label)
        mmin=min(evidence(p,edge_cost) for p in min_menu)
        route_class_minima[route_name]={
            "edge_evidence_slots":edge_cost,
            "minimum_label_evidence_slots":lmin,
            "label_minimizer_patterns":sum(evidence(p,edge_cost)==lmin for p in min_label),
            "minimum_menu_evidence_slots":mmin,
            "menu_minimizer_patterns":sum(evidence(p,edge_cost)==mmin for p in min_menu)}
    req(route_class_minima["physical_exclusion"]["minimum_label_evidence_slots"]==11,"physical exclusion improvement")
    req(all(row["minimum_label_evidence_slots"]==12 for name,row in route_class_minima.items() if name!="physical_exclusion"),"non-exclusion label floor")
    req(all(row["minimum_menu_evidence_slots"]==12 for row in route_class_minima.values()),"menu floor")

    return {
      "schema":"exact-recurrent-first-host-hybrid-source-certificate-antichain/v1",
      "host_id":HOST,
      "sources":{"mixed_source_certificate_leverage":str(MIXED_PATH),
                 "closure_route_source_gate":str(ROUTE_PATH),
                 "route_cover_admission":str(ADMISSION_PATH)},
      "certificate_universe":{"state_certificates":4,"action_family_certificates":4,
        "individual_edge_certificates":8,"certificate_types":16,"certificate_subsets":65536},
      "certificate_contracts":{
        "state_impossibility":{"evidence_fields_per_certificate":6,"accepted_certificates":0},
        "action_family":{"evidence_fields_per_certificate":7,"accepted_certificates":0},
        "individual_edge_route":{"route_class_evidence_slots":dict(sorted(route_costs.items())),
          "minimum_evidence_slots_per_certificate":edge_lower_bound,"accepted_certificates":0,
          "interpretation":"one exact directed edge with one fully accepted route contract"}},
      "subset_census":{"label_feasible_subsets":62564,"menu_feasible_subsets":61679,
        "label_feasible_size_distribution":label_dist,"menu_feasible_size_distribution":menu_dist},
      "minimal_antichains":{"label":label_summary,"menu":menu_summary},
      "distinguished_patterns":{
        "physical_exclusion_evidence_cheapest_label_pairs":[sorted(p) for p in best_label],
        "state_plus_edge_label_pairs":len(state_edge_label),
        "family_plus_edge_label_pairs":len(family_edge_label),
        "state_plus_edge_menu_pairs":0,"family_plus_edge_menu_pairs":0,
        "one_state_one_family_menu_pairs":0},
      "route_class_sensitivity":route_class_minima,
      "aggregate":{"minimal_label_patterns":51,"minimal_menu_patterns":100,
        "minimum_label_certificates":2,"minimum_menu_certificates":2,
        "minimum_label_evidence_slots_under_edge_physical_exclusion":11,
        "minimum_label_evidence_slots_under_nonexclusion_edge_routes":12,
        "minimum_menu_evidence_slots":12,
        "current_accepted_state_certificates":0,"current_accepted_family_certificates":0,
        "current_accepted_individual_edge_certificates":0,
        "current_complete_label_covers":0,"current_complete_menu_covers":0},
      "source_boundary":{"eleven_slot_label_bound_requires_individual_edge_physical_exclusion":1,
        "nonexclusion_individual_edge_route_beats_two_state_label_bound":0,
        "one_macro_certificate_plus_one_edge_can_close_label_cover":1,
        "one_macro_certificate_plus_one_edge_can_close_menu_cover":0,
        "individual_edge_symbol_is_not_an_accepted_route":1,
        "promotion_to_recurrent_closure_allowed":0},
      "honesty":{"physical_occurrence_coverage_proved":0,"physical_transition_legality_proved":0,
        "persistent_owner_identity_proved":0,"recurrent_child_rows_populated":0,
        "strict_lyapunov_certificate_proved":0,"global_termination_proved":0,
        "all_n_proved_by_checker":0}}

def validate(repo: Path, value: dict[str,Any]) -> None: req(value==compile_manifest(repo),"deterministic manifest")
def mutation(repo: Path, expected: dict[str,Any]) -> int:
    edits=[]
    def add(fn): x=copy.deepcopy(expected); fn(x); edits.append(x)
    add(lambda x:x["certificate_universe"].__setitem__("certificate_subsets",65535))
    add(lambda x:x["subset_census"].__setitem__("label_feasible_subsets",62563))
    add(lambda x:x["subset_census"].__setitem__("menu_feasible_subsets",61678))
    add(lambda x:x["minimal_antichains"]["label"].__setitem__("pattern_count",50))
    add(lambda x:x["minimal_antichains"]["menu"].__setitem__("pattern_count",99))
    add(lambda x:x["distinguished_patterns"].__setitem__("state_plus_edge_label_pairs",3))
    add(lambda x:x["distinguished_patterns"].__setitem__("state_plus_edge_menu_pairs",1))
    add(lambda x:x["route_class_sensitivity"]["physical_exclusion"].__setitem__("minimum_label_evidence_slots",12))
    add(lambda x:x["aggregate"].__setitem__("minimum_label_evidence_slots_under_edge_physical_exclusion",12))
    add(lambda x:x["aggregate"].__setitem__("minimum_menu_evidence_slots",11))
    add(lambda x:x["certificate_contracts"]["individual_edge_route"].__setitem__("accepted_certificates",1))
    add(lambda x:x["aggregate"].__setitem__("current_complete_label_covers",1))
    add(lambda x:x["source_boundary"].__setitem__("eleven_slot_label_bound_requires_individual_edge_physical_exclusion",0))
    add(lambda x:x["source_boundary"].__setitem__("one_macro_certificate_plus_one_edge_can_close_menu_cover",1))
    add(lambda x:x["source_boundary"].__setitem__("promotion_to_recurrent_closure_allowed",1))
    add(lambda x:x["honesty"].__setitem__("strict_lyapunov_certificate_proved",1))
    add(lambda x:x["honesty"].__setitem__("global_termination_proved",1))
    add(lambda x:x["honesty"].__setitem__("all_n_proved_by_checker",1))
    rejected=0
    for candidate in edits:
        try: validate(repo,candidate)
        except AuditError: rejected+=1
    req(rejected==len(edits),"mutation accepted"); return rejected

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--write",type=Path); parser.add_argument("--check",type=Path); parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args(); repo=root(); manifest=compile_manifest(repo); validate(repo,manifest)
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True); args.write.write_text(json.dumps(manifest,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    if args.check: validate(repo,json.loads(args.check.read_text(encoding="utf-8")))
    result={"checker":"exact-recurrent-first-host-hybrid-source-certificate-antichain",**manifest["aggregate"]}
    if args.self_test: result["mutation_corruptions_rejected"]=mutation(repo,manifest)
    print(json.dumps(result,sort_keys=True))
if __name__=="__main__": main()
