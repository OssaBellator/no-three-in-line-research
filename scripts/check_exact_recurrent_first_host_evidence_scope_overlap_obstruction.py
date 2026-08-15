#!/usr/bin/env python3
"""Audit scoped evidence slots versus unsafe lexical field-name collapse."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from pathlib import Path
from typing import Any

HOST = "s4-75b04c45c1c8eac2"
HYBRID_PATH = Path("data/exact_recurrent_first_host_hybrid_source_certificate_antichain.json")
ROUTE_PATH = Path("data/exact_recurrent_first_host_closure_route_source_gate.json")
STATES = ("00","01","10","11")
SELECTED = {"00":"3012","01":"3201","10":"2031","11":"2031"}
UNDIRECTED = (("00","01"),("00","10"),("01","11"),("10","11"))
FAMILIES = {
    "restore_02": ("00->10","01->11"),
    "delete_02": ("10->00","11->01"),
    "restore_20": ("00->01","10->11"),
    "delete_20": ("01->00","11->10"),
}
STATE_FIELDS = (
    "physical_occurrence_domain_ref","state_definition_ref",
    "state_impossibility_theorem_ref","domain_completeness_ref",
    "incident_edge_exclusion_ref","realization_status",
)
FAMILY_FIELDS = (
    "shared_theorem_ref","both_context_values_proved","shared_owner_schema_ref",
    "shared_operation_schema_ref","shared_route_schema_ref",
    "child_payment_compatibility_ref","realization_status",
)
ROUTE_ORDER = (
    "physical_exclusion","decorated_outer_reset",
    "finite_unrestorable_capacity","terminal_or_improving_output",
    "bounded_strict_potential",
)

class AuditError(RuntimeError): pass
def req(ok: bool, msg: str) -> None:
    if not ok: raise AuditError(msg)
def load(root: Path, path: Path) -> dict[str, Any]:
    value=json.loads((root/path).read_text())
    req(isinstance(value,dict),str(path)); return value

def edges() -> tuple[str,...]:
    out=set()
    for a,b in UNDIRECTED:
        out.add(f"{a}->{b}"); out.add(f"{b}->{a}")
    return tuple(sorted(out))

def state_edges(state: str) -> set[str]:
    return {e for e in edges() if e.startswith(state+"->") or e.endswith("->"+state)}

def label_covers() -> set[frozenset[str]]:
    changing={e for e in edges() if SELECTED[e[:2]] != SELECTED[e[4:]]}
    out=set()
    for order in itertools.permutations(sorted(set(SELECTED.values()))):
        rank={x:i for i,x in enumerate(order)}
        paid={e for e in changing if rank[SELECTED[e[:2]]] > rank[SELECTED[e[4:]]]}
        out.add(frozenset(changing-paid))
    req(len(out)==6,"label cover count")
    return out

def menu_covers() -> set[frozenset[str]]:
    out=set()
    for order in itertools.permutations(STATES):
        rank={x:i for i,x in enumerate(order)}
        external=set()
        for a,b in UNDIRECTED:
            paid=(a,b) if rank[a]>rank[b] else (b,a)
            external.add(f"{paid[1]}->{paid[0]}")
        out.add(frozenset(external))
    req(len(out)==14,"menu cover count")
    return out

def cert_edges() -> dict[str,set[str]]:
    out={f"state:{s}":state_edges(s) for s in STATES}
    out.update({f"family:{f}":set(es) for f,es in FAMILIES.items()})
    out.update({f"edge:{e}":{e} for e in edges()})
    return out

def minimal_sets(covers: set[frozenset[str]]) -> list[frozenset[str]]:
    ce=cert_edges(); names=tuple(ce); feasible=[]
    for size in range(len(names)+1):
        for combo in itertools.combinations(names,size):
            closed=set()
            for c in combo: closed |= ce[c]
            if any(k<=closed for k in covers):
                feasible.append(frozenset(combo))
    return sorted([s for s in feasible if not any(t<s for t in feasible)],
                  key=lambda s:(len(s),sorted(s)))

def route_fields(route_gate: dict[str,Any]) -> dict[str,tuple[str,...]]:
    out={}
    for row in route_gate.get("route_contracts",[]):
        route=row["route"]
        fields=tuple(row["base_physical_fields"]+row["route_specific_fields"])
        req(len(fields)==len(set(fields)),f"duplicate fields inside {route}")
        out[route]=fields
    req(set(out)==set(ROUTE_ORDER),"route classes")
    req({k:len(v) for k,v in out.items()}=={
        "physical_exclusion":5,"decorated_outer_reset":8,
        "finite_unrestorable_capacity":9,"terminal_or_improving_output":10,
        "bounded_strict_potential":11},"route slot counts")
    return out

def fields(cert: str, route: str, edge_fields: dict[str,tuple[str,...]]) -> tuple[str,...]:
    if cert.startswith("state:"): return STATE_FIELDS
    if cert.startswith("family:"): return FAMILY_FIELDS
    return edge_fields[route]

def summarize(patterns: list[frozenset[str]], route: str,
              edge_fields: dict[str,tuple[str,...]]) -> dict[str,Any]:
    dist={}; records=[]; repeated=0
    for p in patterns:
        raw=sum(len(fields(c,route,edge_fields)) for c in p)
        union=set()
        for c in p: union.update(fields(c,route,edge_fields))
        lexical=len(union); saving=raw-lexical
        if saving: repeated += 1
        key=f"{raw}|{lexical}|{saving}"
        dist[key]=dist.get(key,0)+1
        records.append({"certificates":sorted(p),"scoped_slots":raw,
                        "lexical_union_fields":lexical,
                        "unsafe_lexical_savings":saving})
    payload=json.dumps(records,sort_keys=True,separators=(",",":"))
    return {
        "pattern_count":len(patterns),
        "patterns_with_repeated_field_names":repeated,
        "minimum_scoped_slots":min(r["scoped_slots"] for r in records),
        "minimum_lexical_union_fields":min(r["lexical_union_fields"] for r in records),
        "maximum_unsafe_lexical_savings":max(r["unsafe_lexical_savings"] for r in records),
        "scoped_lexical_savings_distribution":dict(sorted(dist.items())),
        "registry_digest":hashlib.sha256(payload.encode()).hexdigest(),
    }

def compile_manifest(root: Path) -> dict[str,Any]:
    hybrid=load(root,HYBRID_PATH); route_gate=load(root,ROUTE_PATH)
    req(hybrid.get("schema")=="exact-recurrent-first-host-hybrid-source-certificate-antichain/v1","hybrid schema")
    req(hybrid.get("host_id")==HOST,"hybrid host")
    req(hybrid.get("certificate_universe",{}).get("certificate_subsets")==65536,"hybrid subset census")
    req(hybrid.get("aggregate",{}).get("minimal_label_patterns")==51,"hybrid label antichain")
    req(hybrid.get("aggregate",{}).get("minimal_menu_patterns")==100,"hybrid menu antichain")
    req(hybrid.get("aggregate",{}).get("current_accepted_state_certificates")==0,"state source")
    req(hybrid.get("aggregate",{}).get("current_accepted_family_certificates")==0,"family source")
    req(hybrid.get("aggregate",{}).get("current_accepted_individual_edge_certificates")==0,"edge source")
    req(route_gate.get("schema")=="exact-recurrent-first-host-closure-route-source-gate/v1","route schema")
    req(route_gate.get("scope",{}).get("host_id")==HOST,"route host")
    req(route_gate.get("aggregate",{}).get("source_admissible_edge_route_pairs")==0,"route source")

    edge_fields=route_fields(route_gate)
    label=minimal_sets(label_covers()); menu=minimal_sets(menu_covers())
    req(len(label)==51 and len(menu)==100,"antichain reconstruction")
    req({len(x) for x in label}=={2,3},"label sizes")
    req({len(x) for x in menu}=={2,3,4},"menu sizes")

    overlap={}
    for route in ROUTE_ORDER:
        ef=edge_fields[route]
        overlap[route]={
            "state_family":sorted(set(STATE_FIELDS)&set(FAMILY_FIELDS)),
            "state_edge":sorted(set(STATE_FIELDS)&set(ef)),
            "family_edge":sorted(set(FAMILY_FIELDS)&set(ef)),
            "state_state_same_names":len(STATE_FIELDS),
            "family_family_same_names":len(FAMILY_FIELDS),
            "edge_edge_same_names":len(ef),
        }
        req(overlap[route]["state_family"]==["realization_status"],"state/family overlap")
        req(overlap[route]["state_edge"]==["realization_status"],f"state/edge overlap {route}")
        req(overlap[route]["family_edge"]==["realization_status"],f"family/edge overlap {route}")

    route_summaries={}
    for route in ROUTE_ORDER:
        route_summaries[route]={
            "edge_fields":list(edge_fields[route]),
            "edge_evidence_slots":len(edge_fields[route]),
            "label":summarize(label,route,edge_fields),
            "menu":summarize(menu,route,edge_fields),
        }
    req(route_summaries["physical_exclusion"]["label"]["minimum_scoped_slots"]==11,"label floor")
    req(route_summaries["physical_exclusion"]["menu"]["minimum_scoped_slots"]==12,"menu floor")
    req(route_summaries["physical_exclusion"]["label"]["minimum_lexical_union_fields"]==5,"label lexical floor")
    req(route_summaries["physical_exclusion"]["menu"]["minimum_lexical_union_fields"]==5,"menu lexical floor")
    for route in ROUTE_ORDER[1:]:
        req(route_summaries[route]["label"]["minimum_scoped_slots"]==12,f"{route} label floor")
        req(route_summaries[route]["menu"]["minimum_scoped_slots"]==12,f"{route} menu floor")
        req(route_summaries[route]["label"]["minimum_lexical_union_fields"]==6,f"{route} label lexical")
        req(route_summaries[route]["menu"]["minimum_lexical_union_fields"]==6,f"{route} menu lexical")

    return {
        "schema":"exact-recurrent-first-host-evidence-scope-overlap-obstruction/v1",
        "host_id":HOST,
        "sources":{"hybrid_source_certificate_antichain":str(HYBRID_PATH),
                   "closure_route_source_gate":str(ROUTE_PATH)},
        "contract_field_sets":{"state_impossibility":list(STATE_FIELDS),
                               "action_family":list(FAMILY_FIELDS),
                               "individual_edge_routes":{r:list(edge_fields[r]) for r in ROUTE_ORDER}},
        "lexical_overlap_matrix":overlap,
        "route_class_summaries":route_summaries,
        "scope_rule":{
            "field_slots_are_certificate_instance_scoped":1,
            "identical_field_names_do_not_authorize_slot_deduplication":1,
            "one_source_reference_may_populate_multiple_slots_only_with_uniformity_theorem":1,
            "cross_class_field_equivalence_requires_explicit_bridge":1,
            "lexical_union_counts_are_unsafe_lower_bounds":1,
        },
        "sharing_gate":{
            "required_fields":["certificate_instance_domain_ref","field_equivalence_map",
                "uniformity_theorem_ref","scope_preservation_ref","local_obligation_preservation_ref",
                "realization_status"],
            "accepted_sharing_theorems":0,
            "populated_fields":0,
        },
        "aggregate":{
            "label_antichain_patterns":51,"menu_antichain_patterns":100,
            "route_classes":5,"accepted_sharing_theorems":0,
            "current_minimum_safe_label_slots":11,
            "current_minimum_safe_menu_slots":12,
            "unsafe_physical_exclusion_label_lexical_floor":5,
            "unsafe_physical_exclusion_menu_lexical_floor":5,
        },
        "honesty":{"physical_occurrence_coverage_proved":0,
            "physical_transition_legality_proved":0,"persistent_owner_identity_proved":0,
            "recurrent_child_rows_populated":0,"strict_lyapunov_certificate_proved":0,
            "global_termination_proved":0,"all_n_proved_by_checker":0},
    }

def validate(root: Path, value: dict[str,Any]) -> None:
    req(value==compile_manifest(root),"deterministic manifest")

def mutation(root: Path, expected: dict[str,Any]) -> int:
    edits=[]
    def add(fn): x=copy.deepcopy(expected); fn(x); edits.append(x)
    add(lambda x:x["aggregate"].__setitem__("label_antichain_patterns",50))
    add(lambda x:x["aggregate"].__setitem__("menu_antichain_patterns",99))
    add(lambda x:x["aggregate"].__setitem__("current_minimum_safe_label_slots",10))
    add(lambda x:x["aggregate"].__setitem__("current_minimum_safe_menu_slots",11))
    add(lambda x:x["aggregate"].__setitem__("unsafe_physical_exclusion_label_lexical_floor",6))
    add(lambda x:x["sharing_gate"].__setitem__("accepted_sharing_theorems",1))
    add(lambda x:x["sharing_gate"].__setitem__("populated_fields",1))
    add(lambda x:x["scope_rule"].__setitem__("identical_field_names_do_not_authorize_slot_deduplication",0))
    add(lambda x:x["scope_rule"].__setitem__("cross_class_field_equivalence_requires_explicit_bridge",0))
    add(lambda x:x["lexical_overlap_matrix"]["physical_exclusion"].__setitem__("state_edge",[]))
    add(lambda x:x["route_class_summaries"]["physical_exclusion"]["label"].__setitem__("minimum_scoped_slots",10))
    add(lambda x:x["route_class_summaries"]["physical_exclusion"]["label"].__setitem__("minimum_lexical_union_fields",6))
    add(lambda x:x["route_class_summaries"]["physical_exclusion"]["menu"].__setitem__("maximum_unsafe_lexical_savings",14))
    add(lambda x:x["route_class_summaries"]["decorated_outer_reset"]["label"].__setitem__("minimum_scoped_slots",11))
    add(lambda x:x["route_class_summaries"]["finite_unrestorable_capacity"].__setitem__("edge_evidence_slots",8))
    add(lambda x:x["route_class_summaries"]["terminal_or_improving_output"]["menu"].__setitem__("pattern_count",99))
    add(lambda x:x["route_class_summaries"]["bounded_strict_potential"]["label"].__setitem__("registry_digest","0"*64))
    add(lambda x:x["honesty"].__setitem__("all_n_proved_by_checker",1))
    rejected=0
    for value in edits:
        try: validate(root,value)
        except AuditError: rejected += 1
    req(rejected==18,"mutation rejection count")
    return rejected

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=".")
    ap.add_argument("--check")
    ap.add_argument("--write")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args(); root=Path(args.root)
    expected=compile_manifest(root)
    if args.write:
        (root/args.write).write_text(json.dumps(expected,sort_keys=True,separators=(",",":"))+"\n")
    if args.check:
        validate(root,json.loads((root/args.check).read_text()))
    if args.self_test:
        mutation(root,expected)
    print(json.dumps({"schema":expected["schema"],
        "label_patterns":51,"menu_patterns":100,
        "minimum_safe_label_slots":11,"minimum_safe_menu_slots":12,
        "accepted_sharing_theorems":0,
        "all_n_proved_by_checker":0},sort_keys=True))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
