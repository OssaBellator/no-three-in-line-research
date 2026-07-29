#!/usr/bin/env python3
"""Exact documentary T20/T21 exceptional-chamber closure frontiers.

The canonical 232 zero-selector and 20 hard-core chambers are retained.  T05 supplies exact host geometry,
T18 supplies final row theorems and T19 supplies exact parent-to-row coverage.  Closed dispositions are
sealed by chamber-specific typed artifacts; no legacy semantic-refinement row or untyped proof locator is
accepted.  This validates identity and support only and always reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json, sys
from collections import Counter, defaultdict
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as targets
import check_prime_power_canonical_raw_host_catalogue as cat
import check_prime_power_exceptional_chamber_disposition_registry as legacy
import check_prime_power_geometry_selector_frontier_v2 as t05
import check_prime_power_global_family_exhaustiveness_frontier as t19
import check_prime_power_obligation_artifact_registry as obligations
import check_prime_power_row_theorem_frontier as t18


class ChamberFrontierError(ValueError): pass

def req(value: bool, message: str)->None:
    if not value: raise ChamberFrontierError(message)

def text(value: Any, path: str)->str:
    req(isinstance(value,str) and bool(value),f"{path}: nonempty string required"); return value

def exact_ids(value: Any, expected:list[str], path:str)->list[str]:
    req(isinstance(value,list) and value==expected and value==sorted(value) and len(value)==len(set(value)),f"{path}: exact sorted support required")
    req(all(isinstance(x,str) and x for x in value),f"{path}: bad ID"); return list(value)


@contextmanager
def corrected_roots():
    saved={}; old_special=targets.special_certificate_support
    specs={
        "T20_EXCEPTIONAL_ZERO_ROWS":(("T05_GEOMETRY_SELECTORS","T18_ROW_THEOREMS","T19_GLOBAL_FAMILY"),("T19_GLOBAL_FAMILY",)),
        "T21_HARD_CORE_ROWS":(("T05_GEOMETRY_SELECTORS","T18_ROW_THEOREMS","T19_GLOBAL_FAMILY"),("T19_GLOBAL_FAMILY",)),
    }
    for target_id,(proof,research) in specs.items():
        d=atomic.TARGETS[target_id]; saved[target_id]=(d["proof_dependency_target_ids"],d["research_dependency_target_ids"])
        d["proof_dependency_target_ids"],d["research_dependency_target_ids"]=proof,research
    def special(target_id:str,surfaces:dict[str,Any])->list[str]:
        return [] if target_id in specs else old_special(target_id,surfaces)
    targets.special_certificate_support=special
    try: yield
    finally:
        for target_id,(proof,research) in saved.items():
            d=atomic.TARGETS[target_id]; d["proof_dependency_target_ids"],d["research_dependency_target_ids"]=proof,research
        targets.special_certificate_support=old_special


def exact_disposition(raw:dict[str,Any], chamber:dict[str,Any], host_geometry_ids:list[str],
                      row_by_id:dict[str,dict[str,Any]], row_artifact_by_id:dict[str,str],
                      coverage_artifact_by_parent:dict[str,str], rows_by_host:dict[str,list[str]], path:str)->dict[str,Any]:
    for key in ("chamber_id","canonical_chamber_record_sha256"):
        req(raw.get(key)==chamber[key],f"{path}.{key}: mismatch")
    status=raw.get("status"); req(status in {"open","closed"},f"{path}.status")
    proof_kind=raw.get("proof_kind"); final_row_id=raw.get("final_row_id")
    locator,digest=raw.get("verification_locator"),raw.get("verification_digest")
    if status=="open":
        req(proof_kind is None and final_row_id is None and locator is None and digest is None,f"{path}: open proof fields")
        t18ids=[]; t19ids=[]
    else:
        req(proof_kind in {"global-row-theorem","direct-chamber-proof","signature-infeasibility","host-union-proof"},f"{path}.proof_kind")
        req(isinstance(locator,str) and locator and isinstance(digest,str) and digest,f"{path}: closed verification required")
        req(host_geometry_ids,f"{path}: closed chamber requires exact T05 host geometry")
        if proof_kind=="global-row-theorem":
            req(isinstance(final_row_id,str) and final_row_id in row_by_id,f"{path}: exact T18 row required")
            row=row_by_id[final_row_id]; req(row["host_id"]==chamber["host_id"],f"{path}: row host mismatch")
            req(final_row_id in row_artifact_by_id and row["parent_global_state_id"] in coverage_artifact_by_parent,f"{path}: T18/T19 support missing")
            t18ids=[row_artifact_by_id[final_row_id]]; t19ids=[coverage_artifact_by_parent[row["parent_global_state_id"]]]
        elif proof_kind=="host-union-proof":
            req(final_row_id is None,f"{path}: host union has null final row")
            host_rows=rows_by_host.get(chamber["host_id"],[]); req(host_rows,f"{path}: host union requires exact row family")
            req(all(r in row_artifact_by_id for r in host_rows),f"{path}: host row theorem artifact missing")
            t18ids=sorted(row_artifact_by_id[r] for r in host_rows)
            t19ids=sorted({coverage_artifact_by_parent[row_by_id[r]["parent_global_state_id"]] for r in host_rows})
        else:
            req(final_row_id is None,f"{path}: direct proof has null final row"); t18ids=[]; t19ids=[]
    exact_ids(raw.get("support_t05_geometry_artifact_ids"),host_geometry_ids if status=="closed" else [],f"{path}.T05 support")
    exact_ids(raw.get("support_t18_row_theorem_artifact_ids"),t18ids,f"{path}.T18 support")
    exact_ids(raw.get("support_t19_coverage_artifact_ids"),t19ids,f"{path}.T19 support")
    out={**chamber,"status":status,"proof_kind":proof_kind,"final_row_id":final_row_id,
         "verification_locator":locator,"verification_digest":digest,
         "closure_statement":text(raw.get("closure_statement"),f"{path}.closure statement"),
         "selected_row_interpretation":text(raw.get("selected_row_interpretation"),f"{path}.selected row interpretation"),
         "support_t05_geometry_artifact_ids":host_geometry_ids if status=="closed" else [],
         "support_t18_row_theorem_artifact_ids":t18ids,"support_t19_coverage_artifact_ids":t19ids,
         "evidence":text(raw.get("evidence"),f"{path}.evidence"),"note":text(raw.get("note"),f"{path}.note")}
    out["exceptional_chamber_disposition_sha256"]=cat.canonical_digest(out); return out


def exact_artifact(raw:dict[str,Any], disposition:dict[str,Any], path:str)->dict[str,Any]:
    kind="exceptional-zero-chamber-proof" if disposition["chamber_kind"]=="zero-selector" else "hard-core-chamber-proof"
    req(raw.get("chamber_id")==disposition["chamber_id"] and raw.get("artifact_kind")==kind,f"{path}: identity/kind mismatch")
    req(raw.get("exceptional_chamber_disposition_sha256")==disposition["exceptional_chamber_disposition_sha256"],f"{path}: disposition mismatch")
    for field in ("support_t05_geometry_artifact_ids","support_t18_row_theorem_artifact_ids","support_t19_coverage_artifact_ids"):
        exact_ids(raw.get(field),disposition[field],f"{path}.{field}")
    out={"chamber_id":disposition["chamber_id"],"artifact_id":text(raw.get("artifact_id"),f"{path}.artifact ID"),"artifact_kind":kind,
         "exceptional_chamber_disposition_sha256":disposition["exceptional_chamber_disposition_sha256"],
         "proof_locator":text(raw.get("proof_locator"),f"{path}.locator"),"proof_digest":text(raw.get("proof_digest"),f"{path}.digest"),
         "proof_statement":text(raw.get("proof_statement"),f"{path}.statement"),
         "support_t05_geometry_artifact_ids":disposition["support_t05_geometry_artifact_ids"],
         "support_t18_row_theorem_artifact_ids":disposition["support_t18_row_theorem_artifact_ids"],
         "support_t19_coverage_artifact_ids":disposition["support_t19_coverage_artifact_ids"],
         "evidence":text(raw.get("evidence"),f"{path}.evidence")}
    support=[*out["support_t05_geometry_artifact_ids"],*out["support_t18_row_theorem_artifact_ids"],*out["support_t19_coverage_artifact_ids"]]
    req(out["artifact_id"] not in support,f"{path}: self support"); out["exceptional_chamber_artifact_sha256"]=cat.canonical_digest(out); return out


def _exact(c:dict[str,Any])->dict[str,Any]:
    t19c=c.get("global_family_exhaustiveness_frontier_certificate"); req(isinstance(t19c,dict),"T19 certificate required")
    for key in ("exceptional_chamber_dispositions","exceptional_chamber_artifacts","exceptional_chamber_proof_bundles"):
        req(isinstance(c.get(key),list),f"{key}: list required")
    t19.validate_certificate(t19c); t19x=t19.exact_certificate(t19c); t18c=t19c["row_theorem_frontier_certificate"]
    t18.validate_certificate(t18c); t18x=t18.exact_certificate(t18c)
    t17c=t18c["state_predicate_frontier_certificate"]; t16c=t17c["global_rank_frontier_certificate"]
    t15c=t16c["interface_exhaustiveness_frontier_certificate"]; t12c=t15c["auxiliary_semantics_frontier_certificate"]
    t11c=t12c["recurrent_block_closure_frontier_certificate"]; t10c=t11c["transition_resource_frontier_certificate"]
    t06c=t10c["candidate_policy_frontier_certificate"]; t05c=t06c["geometry_selector_frontier_certificate"]
    t05.validate_certificate(t05c); t05x=t05.exact_certificate(t05c)
    t04c=t05c["block_interface_population_frontier_certificate"]; registry=t04c["atomic_target_artifact_registry_certificate"]
    targets.validate_certificate(registry); targetx=targets.exact_certificate(registry)
    atomc=registry["current_frontier_execution_certificate"]["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomc); atomx=atomic.exact_certificate(atomc)
    source=t04c["slot_candidate_population_frontier_certificate"]["rule_exhaustiveness_frontier_certificate"]["source_truth_frontier_execution_certificate"]["source_statement_truth_registry_certificate"]
    obligc=source["obligation_artifact_registry_certificate"]; obligations.validate_certificate(obligc); obligx=obligations.exact_certificate(obligc)
    closurex=closure.exact_certificate(obligc["all_n_implication_closure_certificate"])

    host_geom:dict[str,list[str]]=defaultdict(list); host_by_slot={}
    for summary,artifact in zip(t05x["slot_geometry_summaries"],t05x["slot_geometry_selector_artifacts"]):
        host_by_slot[artifact["slot_id"]]=summary["host_id"]; host_geom[summary["host_id"]].append(artifact["artifact_id"])
    for values in host_geom.values(): values.sort()
    t18art={a["final_row_id"]:a["artifact_id"] for a in t18x["global_row_theorem_artifacts"]}
    coverage_art={a["coverage_id"].removeprefix("global-family-coverage::"):a["artifact_id"] for a in t19x["global_family_coverage_artifacts"]}
    row_by_id={}; rows_by_host:dict[str,list[str]]=defaultdict(list)
    for subject in t18x["final_row_subjects"]:
        slot=subject["selected_slot_id"]; req(slot in host_by_slot,f"row {subject['final_row_id']}: T05 host missing")
        row={**subject,"host_id":host_by_slot[slot]}; row_by_id[subject["final_row_id"]]=row; rows_by_host[row["host_id"]].append(subject["final_row_id"])
    for values in rows_by_host.values(): values.sort()

    chambers=legacy.canonical_chambers(); req((sum(x["chamber_kind"]=="zero-selector" for x in chambers),sum(x["chamber_kind"]=="hard-core" for x in chambers))==(232,20),"canonical 232+20 census drift")
    rawd=c["exceptional_chamber_dispositions"]; req(len(rawd)==len(chambers) and [x.get("chamber_id") for x in rawd]==[x["chamber_id"] for x in chambers],"exact chamber order required")
    dispositions=[exact_disposition(raw,chamber,host_geom.get(chamber["host_id"],[]),row_by_id,t18art,coverage_art,rows_by_host,f"disposition[{i}]") for i,(raw,chamber) in enumerate(zip(rawd,chambers))]
    req(rawd==dispositions,"noncanonical chamber dispositions")
    artgroup={x["chamber_id"]:[] for x in chambers}
    for raw in c["exceptional_chamber_artifacts"]: req(raw.get("chamber_id") in artgroup,"unknown chamber artifact"); artgroup[raw["chamber_id"]].append(raw)
    arts=[]; bundles=[]
    for d in dispositions:
        group=artgroup[d["chamber_id"]]
        if d["status"]=="open": req(not group,f"chamber {d['chamber_id']}: open artifact"); continue
        req(len(group)==1,f"chamber {d['chamber_id']}: one artifact required"); a=exact_artifact(group[0],d,f"artifact[{d['chamber_id']}]"); arts.append(a)
        b={"chamber_id":d["chamber_id"],"exceptional_chamber_disposition_sha256":d["exceptional_chamber_disposition_sha256"],
           "exceptional_chamber_artifact_sha256":a["exceptional_chamber_artifact_sha256"],
           "support_t05_geometry_artifact_ids":a["support_t05_geometry_artifact_ids"],
           "support_t18_row_theorem_artifact_ids":a["support_t18_row_theorem_artifact_ids"],
           "support_t19_coverage_artifact_ids":a["support_t19_coverage_artifact_ids"]}
        b["exceptional_chamber_proof_bundle_sha256"]=cat.canonical_digest(b); req(d["verification_digest"]==b["exceptional_chamber_proof_bundle_sha256"],f"chamber {d['chamber_id']}: verification mismatch"); bundles.append(b)
    req(c["exceptional_chamber_artifacts"]==arts and c["exceptional_chamber_proof_bundles"]==bundles,"noncanonical chamber artifacts/bundles")
    req(len({a["artifact_id"] for a in arts})==len(arts),"duplicate chamber artifact ID")

    bykind={kind:[d for d in dispositions if d["chamber_kind"]==kind] for kind in ("zero-selector","hard-core")}
    artby={a["chamber_id"]:a for a in arts}; t05ready=int(t05x["claims"]["geometry_selector_correct_ready"]); t19ready=int(t19x["claims"]["t19_global_family_exhaustiveness_ready"])
    zero_ready=int(t05ready and t19ready and all(d["status"]=="closed" and d["chamber_id"] in artby for d in bykind["zero-selector"]))
    hard_ready=int(t05ready and t19ready and all(d["status"]=="closed" and d["chamber_id"] in artby for d in bykind["hard-core"]))
    def bank(kind:str)->dict[str,Any]:
        ds=bykind[kind]; aa=[artby[d["chamber_id"]] for d in ds if d["chamber_id"] in artby]; bb=[b for b in bundles if b["chamber_id"] in {d["chamber_id"] for d in ds}]
        out={"chamber_kind":kind,"t05_geometry_selector_proof_bank_sha256":t05x["claims"]["geometry_selector_frontier_proof_bank_sha256"],
             "t18_row_theorem_proof_bank_sha256":t18x["claims"]["row_theorem_frontier_proof_bank_sha256"],
             "t19_global_family_proof_bank_sha256":t19x["claims"]["global_family_exhaustiveness_frontier_proof_bank_sha256"],
             "canonical_chambers_sha256":cat.canonical_digest([x for x in chambers if x["chamber_kind"]==kind]),
             "chamber_dispositions_sha256":cat.canonical_digest(ds),"chamber_artifacts_sha256":cat.canonical_digest(aa),"chamber_proof_bundles_sha256":cat.canonical_digest(bb)}
        out[f"{kind.replace('-','_')}_chamber_frontier_proof_bank_sha256"]=cat.canonical_digest(out); return out
    zero_bank,hard_bank=bank("zero-selector"),bank("hard-core")
    closed={x["obligation_id"]:x for x in closurex["obligation_closure_records"]}; all_oblig=obligx["proof_artifacts"]
    specs={"EXCEPTIONAL_ZERO_ROWS_CLOSED":(zero_ready,"exceptional-zero-row-proof","exceptional-chamber-frontier://EXCEPTIONAL_ZERO_ROWS_CLOSED",zero_bank["zero_selector_chamber_frontier_proof_bank_sha256"]),
           "HARD_CORE_ROWS_CLOSED":(hard_ready,"hard-core-row-proof","exceptional-chamber-frontier://HARD_CORE_ROWS_CLOSED",hard_bank["hard_core_chamber_frontier_proof_bank_sha256"])}
    for obligation_id,(ready,kind,locator,digest) in specs.items():
        req(int(closed[obligation_id]["closed"])==ready,f"{obligation_id}: closure mismatch"); found=[a for a in all_oblig if a["obligation_id"]==obligation_id]; req(len(found)==(1 if ready else 0),f"{obligation_id}: artifact presence")
        if ready:
            dep=set(closure.OBLIGATION_DEPENDENCIES[obligation_id]); support=sorted(a["artifact_id"] for a in all_oblig if a["obligation_id"] in dep); a=found[0]
            req(a["artifact_kind"]==kind and a["locator"]==locator and a["digest"]==digest and a["support_artifact_ids"]==support,f"{obligation_id}: artifact mismatch")
    results={r["target_id"]:r for r in atomx["target_result_records"]}; targetby={a["target_id"]:a for a in targetx["atomic_target_artifacts"]}
    target_specs={"T20_EXCEPTIONAL_ZERO_ROWS":(zero_ready,"exceptional-zero-proof","exceptional-chamber-frontier://T20_EXCEPTIONAL_ZERO_ROWS",zero_bank["zero_selector_chamber_frontier_proof_bank_sha256"]),
                  "T21_HARD_CORE_ROWS":(hard_ready,"hard-core-proof","exceptional-chamber-frontier://T21_HARD_CORE_ROWS",hard_bank["hard_core_chamber_frontier_proof_bank_sha256"])}
    for target_id,(ready,kind,locator,digest) in target_specs.items():
        req(int(results[target_id]["effective_target_complete"])==ready,f"{target_id}: completion mismatch"); a=targetby.get(target_id)
        if ready: req(a is not None and a["artifact_kind"]==kind and a["proof_locator"]==locator and a["proof_digest"]==digest,f"{target_id}: artifact mismatch")
        else: req(a is None,f"open {target_id} has artifact")
    counts=Counter((d["chamber_kind"],d["status"]) for d in dispositions)
    claims={"exceptional_chambers":len(chambers),"zero_selector_chambers":232,"hard_core_chambers":20,
            "closed_zero_selector_chambers":counts[("zero-selector","closed")],"closed_hard_core_chambers":counts[("hard-core","closed")],
            "t20_exceptional_zero_rows_ready":zero_ready,"t21_hard_core_rows_ready":hard_ready,"t05_geometry_ready":t05ready,"t19_global_family_ready":t19ready,
            "exact_canonical_chamber_census":1,"exact_t05_host_geometry_support":1,"exact_t18_t19_row_support":1,"legacy_refinement_excluded":1,
            "corrected_t19_chamber_target_roots":1,"noncircular_t20_t21_bank_binding":1,"all_n_proved_by_checker":0,
            "open_zero_chamber_ids":[d["chamber_id"] for d in bykind["zero-selector"] if d["status"]=="open"],
            "open_hard_core_chamber_ids":[d["chamber_id"] for d in bykind["hard-core"] if d["status"]=="open"],
            "zero_selector_chamber_frontier_proof_bank_sha256":zero_bank["zero_selector_chamber_frontier_proof_bank_sha256"],
            "hard_core_chamber_frontier_proof_bank_sha256":hard_bank["hard_core_chamber_frontier_proof_bank_sha256"]}
    return {"canonical_chamber_records":chambers,"exceptional_chamber_dispositions":dispositions,"exceptional_chamber_artifacts":arts,
            "exceptional_chamber_proof_bundles":bundles,"zero_selector_chamber_frontier_proof_bank":zero_bank,
            "hard_core_chamber_frontier_proof_bank":hard_bank,"claims":claims}


def exact_certificate(certificate:dict[str,Any])->dict[str,Any]:
    with corrected_roots(): return _exact(certificate)

def validate_certificate(certificate:Any)->dict[str,Any]:
    req(isinstance(certificate,dict) and certificate.get("version")==1,"version 1 certificate required"); exact=exact_certificate(certificate)
    for k,v in exact.items(): req(certificate.get(k)==v,f"{k}: incorrect")
    payload={k:v for k,v in certificate.items() if k!="certificate_sha256"}; req(certificate.get("certificate_sha256")==cat.canonical_digest(payload),"certificate digest incorrect")
    c=exact["claims"]; return {"chambers":c["exceptional_chambers"],"closed_zero":c["closed_zero_selector_chambers"],"closed_hard":c["closed_hard_core_chambers"],"t20":c["t20_exceptional_zero_rows_ready"],"t21":c["t21_hard_core_rows_ready"],"all_n":0}

def build_certificate(t19c:dict[str,Any],dispositions:list[dict[str,Any]],artifacts:list[dict[str,Any]])->dict[str,Any]:
    c={"version":1,"global_family_exhaustiveness_frontier_certificate":t19c,"exceptional_chamber_dispositions":dispositions,"exceptional_chamber_artifacts":artifacts,"exceptional_chamber_proof_bundles":[]}
    c.update(exact_certificate(c)); c["certificate_sha256"]=cat.canonical_digest(c); return c

def main()->None:
    if len(sys.argv)!=2: raise SystemExit("usage: check_prime_power_exceptional_chamber_frontier.py certificate.json")
    print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))
if __name__=="__main__": main()
