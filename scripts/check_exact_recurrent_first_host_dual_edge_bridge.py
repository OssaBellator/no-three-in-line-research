#!/usr/bin/env python3
"""Check the minimal dual-edge bridge for the first physical fibre."""
from __future__ import annotations
import argparse, copy, hashlib, json
from itertools import combinations, permutations
from pathlib import Path

HOST="s4-75b04c45c1c8eac2"; SIDE=4; TARGET=(0,1); DELETIONS=((0,2),(2,0))
STRICT=((-3,5),(5,-3)); PROV=("owner","fate","collision","line","interface","crt")
class AuditError(RuntimeError): pass
def require(ok,msg):
    if not ok: raise AuditError(msg)
def collinear(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def triples(p):
    pts=tuple((r,p[r]) for r in range(SIDE))
    return sum(collinear(*t) for t in combinations(pts,3))
def code(p): return "".join(map(str,p))
def response_edges():
    diagonal={(i,i) for i in range(SIDE)}
    return tuple(sorted((r,c) for r in range(SIDE) for c in range(SIDE)
                        if (r,c) not in diagonal and (r,c)!=TARGET and (r,c) not in DELETIONS))
def responses(edges):
    allowed=set(edges)
    return tuple(p for p in permutations(range(SIDE)) if all((r,p[r]) in allowed for r in range(SIDE)))
def identifier(record):
    keys=("host_id","side","target","lineage_host_edges","response_edges","deletions",
          "coordinate_domain","background","physical_source_ref","deletion_causes","provenance")
    payload={k:record[k] for k in keys}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def make_record(background):
    eligible=response_edges()
    return {"host_id":HOST,"side":SIDE,"target":list(TARGET),
            "lineage_host_edges":[list(e) for e in sorted((*eligible,TARGET))],
            "response_edges":[list(e) for e in eligible],"deletions":[list(e) for e in DELETIONS],
            "coordinate_domain":{"kind":"relative-affine-integer","bounds":None,"physical_embedding_ref":None},
            "background":[list(p) for p in background],"physical_source_ref":None,
            "deletion_causes":{"02":None,"20":None},"provenance":{k:None for k in PROV},
            "legal_operations":[],"intermediate_states":[],"child_row":None,
            "positive_weights":None,"parent_budget":None,"realization_status":"schema-completion-only"}
def validate_record(record):
    require(record["host_id"]==HOST and record["side"]==SIDE,"host")
    target=tuple(record["target"]); lineage=tuple(map(tuple,record["lineage_host_edges"])); eligible=tuple(map(tuple,record["response_edges"]))
    require(target==TARGET and target in lineage and target not in eligible,"target separation")
    require(set(eligible)<=set(lineage),"edge inclusion")
    require(len(set(lineage))==len(lineage) and len(set(eligible))==len(eligible),"edge uniqueness")
    require(all(0<=r<SIDE and 0<=c<SIDE for r,c in lineage),"edge coordinates")
    require(tuple(map(tuple,record["deletions"]))==DELETIONS,"deletions")
    require(record["coordinate_domain"]["kind"]=="relative-affine-integer","coordinate domain")
    require(len({tuple(p) for p in record["background"]})==len(record["background"]),"background uniqueness")
    require(set(record["provenance"])==set(PROV),"provenance keys")
    family=responses(eligible)
    require(tuple(map(code,family))==("3012","3210"),"response family")
    require(tuple(map(triples,family))==(1,4),"response energies")
    return family
def missing(record):
    out=[]
    if record["coordinate_domain"].get("physical_embedding_ref") is None: out.append("coordinate_domain.physical_embedding_ref")
    if record.get("physical_source_ref") is None: out.append("physical_source_ref")
    out += [f"deletion_causes.{k}" for k,v in sorted(record["deletion_causes"].items()) if v is None]
    out += [f"provenance.{k}" for k in PROV if record["provenance"].get(k) is None]
    if not record.get("legal_operations"): out.append("legal_operations")
    if not record.get("intermediate_states"): out.append("intermediate_states")
    for k in ("child_row","positive_weights","parent_budget"):
        if record.get(k) is None: out.append(k)
    if record.get("realization_status")!="physically-realized": out.append("realization_status")
    return tuple(out)
def compile_manifest():
    safe=make_record(tuple()); strict=make_record(STRICT)
    family=validate_record(safe); require(validate_record(strict)==family,"family stability")
    require(identifier(safe)!=identifier(strict),"background identifiers")
    work=missing(safe); require(work==missing(strict) and len(work)==16,"physical worklist")
    conflated=tuple(map(code,responses(tuple(map(tuple,safe["lineage_host_edges"])))))
    require(conflated==("1032","1230","3012","3210"),"conflation witness")
    completions=[]
    for name,record in (("empty-background",safe),("strict-reversal-background",strict)):
        completions.append({"name":name,"record":record,"identifier":identifier(record),
                            "missing_physical_fields":list(work),"complete":False})
    return {"schema":"exact-recurrent-first-host-dual-edge-bridge/v1",
            "scope":{"host_id":HOST,"side":SIDE,"target":list(TARGET)},
            "bridge_contract":{"lineage_host_edges_retain_target":1,"response_edges_exclude_target":1,
                "response_edges_subset_lineage_host":1,
                "response_family":[{"response":code(p),"intrinsic_triples":triples(p)} for p in family],
                "conflated_lineage_edge_response_family":list(conflated)},
            "schema_completions":completions,
            "aggregate":{"lineage_host_edges":10,"response_edges":9,"response_family_size":2,
                "conflated_response_family_size":4,"schema_completion_records":2,
                "missing_physical_fields_per_record":16},
            "conclusion":{"target_response_eligibility_convention_reconciled_by_bridge":1,
                "bridge_schema_expressive_for_safe_and_strict_completions":1,"physical_first_host_batch_complete":0},
            "honesty":{"physical_background_realizability_proved":0,"physical_background_exclusion_proved":0,
                "legal_operations_populated":0,"recurrent_child_rows_populated":0,
                "strict_lyapunov_certificate_proved":0,"all_n_proved_by_checker":0}}
def validate(manifest):
    require(manifest==compile_manifest(),"manifest differs from compiler")
    require(manifest["conclusion"]["physical_first_host_batch_complete"]==0,"physical honesty")
    require(manifest["honesty"]["all_n_proved_by_checker"]==0,"all-n honesty")
def mutation_audit(manifest):
    mutations=[lambda x:x["aggregate"].update(response_family_size=4),
               lambda x:x["bridge_contract"].update(response_edges_exclude_target=0),
               lambda x:x["bridge_contract"]["response_family"].append({"response":"1032","intrinsic_triples":0}),
               lambda x:x["schema_completions"][0]["record"]["response_edges"].append([0,1]),
               lambda x:x["schema_completions"][0].update(complete=True),
               lambda x:x["schema_completions"][0]["missing_physical_fields"].pop(),
               lambda x:x["schema_completions"].pop(),
               lambda x:x["conclusion"].update(physical_first_host_batch_complete=1),
               lambda x:x["honesty"].update(physical_background_realizability_proved=1),
               lambda x:x["honesty"].update(all_n_proved_by_checker=1)]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(manifest); mutate(bad)
        try: validate(bad)
        except (AuditError,KeyError,TypeError,ValueError): rejected+=1
    require(rejected==len(mutations),"mutation audit"); return rejected
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--write",type=Path); parser.add_argument("--check",type=Path); args=parser.parse_args()
    manifest=compile_manifest()
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True); args.write.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    if args.check: validate(json.loads(args.check.read_text(encoding="utf-8")))
    print(json.dumps({"checker":"exact-recurrent-first-host-dual-edge-bridge",**manifest["aggregate"],
                      "mutation_corruptions_rejected":mutation_audit(manifest),**manifest["conclusion"],**manifest["honesty"]},sort_keys=True))
if __name__=="__main__": main()
