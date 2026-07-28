#!/usr/bin/env python3
"""Exact documentary T15 interface-row exhaustiveness frontier.

The row census is derived from T04. T07 supplies semantic claims, T13 global-state identity,
T14 component weights, and T11/T12 the final nonrecurrent exits. Passing checks identity,
integer arithmetic, exact support and coverage only; ``all_n_proved_by_checker`` is always zero.
"""
from __future__ import annotations
import json, math, sys
from collections import Counter
from pathlib import Path
from typing import Any
import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as targets
import check_prime_power_auxiliary_semantics_frontier_v2 as t12
import check_prime_power_block_interface_population_frontier as t04
import check_prime_power_canonical_raw_host_catalogue as cat
import check_prime_power_component_scale_frontier as t14
import check_prime_power_fate_transition_state_frontier as t07
import check_prime_power_obligation_artifact_registry as obligations
import check_prime_power_recurrent_block_closure_frontier as t11
import check_prime_power_state_equivalence_frontier as t13

class T15Error(ValueError): pass
def req(x: bool, m: str)->None:
    if not x: raise T15Error(m)
def text(x: Any, p: str)->str:
    req(isinstance(x,str) and bool(x),f"{p}: nonempty string required"); return x
def idlist(x: Any, allowed:set[str], p:str, empty:bool=False)->list[str]:
    req(isinstance(x,list) and all(isinstance(v,str) and v for v in x),f"{p}: bad list")
    req(x==sorted(x) and len(x)==len(set(x)) and set(x)<=allowed,f"{p}: exact sorted support required")
    req(empty or bool(x),f"{p}: nonempty support required"); return list(x)

def exits(t11x:dict[str,Any],t12x:dict[str,Any],links:dict[tuple[str,str],str])->list[dict[str,Any]]:
    common={r["block_id"]:r for r in t11x["recurrent_block_common_weight_records"]}; elim={r["block_id"]:r for r in t12x["block_auxiliary_eliminations"]}; out=[]
    for b in sorted(common):
        if b not in elim: continue
        c,e=common[b],elim[b]; cert=e["acyclic_auxiliary_elimination_certificate"]
        roles={r["id"]:r["role"] for r in c["common_state_records"]}; recurrent=set(c["common_weight_certificate"]["scc_state_ids"]); aux={r["auxiliary_state_id"] for r in cert["auxiliary_expansions"]}; final=set()
        for row in cert["eliminated_row_records"]:
            parent=row["parent_state_id"]
            for target,m in row["selected_child_vector"]:
                req(target in roles and type(m) is int and m>0,f"block {b}: malformed eliminated target")
                if roles[target]=="recurrent": req(target in recurrent,f"block {b}: external recurrent target"); continue
                req(roles[target]!="auxiliary" and (b,parent) in links and (b,target) in links,f"block {b}: unresolved final exit")
                final.add((parent,target)); core={"block_id":b,"parent_local_state_id":parent,"parent_global_state_id":links[(b,parent)],"target_local_state_id":target,"target_global_state_id":links[(b,target)],"target_role":roles[target],"multiplicity":m,"row_elimination_sha256":row["row_elimination_sha256"],"block_auxiliary_elimination_sha256":e["block_auxiliary_elimination_sha256"]}
                r={"exit_subject_id":f"exit::{cat.canonical_digest(core)[:32]}",**core}; r["interface_exit_subject_sha256"]=cat.canonical_digest(r); out.append(r)
        for parent,target in c["nonrecurrent_exit_edge_records"]:
            req(target in aux if roles[target]=="auxiliary" else (parent,target) in final,f"block {b}: T11 exit not represented after T12")
    out.sort(key=lambda r:(r["parent_global_state_id"],r["target_global_state_id"],r["block_id"],r["row_elimination_sha256"]))
    req(len({r["exit_subject_id"] for r in out})==len(out),"duplicate exit subject"); return out

def exact_certificate(c:dict[str,Any])->dict[str,Any]:
    t14c,t12c=c.get("component_scale_frontier_certificate"),c.get("auxiliary_semantics_frontier_certificate"); req(isinstance(t14c,dict) and isinstance(t12c,dict),"T14/T12 certificates required")
    for k in ("interface_component_multiplier_records","interface_row_records","interface_row_semantic_certificates","interface_exit_coverage_records","interface_row_artifacts"): req(isinstance(c.get(k),list),f"{k}: list required")
    t14.validate_certificate(t14c); t14x=t14.exact_certificate(t14c); t12.validate_certificate(t12c); t12x=t12.exact_certificate(t12c)
    t11c,t13c=t14c["recurrent_block_closure_frontier_certificate"],t14c["state_equivalence_frontier_certificate"]
    req(t12c["recurrent_block_closure_frontier_certificate"]["certificate_sha256"]==t11c["certificate_sha256"],"T12/T14 use different T11 roots")
    t11.validate_certificate(t11c); t11x=t11.exact_certificate(t11c); t13.validate_certificate(t13c); t13x=t13.exact_certificate(t13c)
    t07c=t13c["fate_transition_state_frontier_certificate"]; t07.validate_certificate(t07c); t07x=t07.exact_certificate(t07c)
    t04c=t07c["block_interface_population_frontier_certificate"]; t04.validate_certificate(t04c); t04x=t04.exact_certificate(t04c)
    registry=t04c["atomic_target_artifact_registry_certificate"]; targets.validate_certificate(registry); targetx=targets.exact_certificate(registry); atomc=registry["current_frontier_execution_certificate"]["atomic_frontier_execution_certificate"]; atomic.validate_certificate(atomc); atomx=atomic.exact_certificate(atomc)
    rule=t04c["slot_candidate_population_frontier_certificate"]["rule_exhaustiveness_frontier_certificate"]; source=rule["source_truth_frontier_execution_certificate"]["source_statement_truth_registry_certificate"]
    obligc=source["obligation_artifact_registry_certificate"]; obligations.validate_certificate(obligc); obligx=obligations.exact_certificate(obligc); closurex=closure.exact_certificate(obligc["all_n_implication_closure_certificate"])
    units=[u for u in t04x["expected_block_interface_population_units"] if u["unit_kind"]=="interface-row"]
    payload={r["unit_id"]:r for r in t04x["block_interface_population_payloads"]}; t04art={r["unit_id"]:r["artifact_id"] for r in t04x["block_interface_population_artifacts"]}
    slotsem={r["slot_id"]:r for r in t07x["slot_fate_transition_state_semantic_certificates"]}; slotart={r["slot_id"]:r["artifact_id"] for r in t07x["slot_fate_transition_state_artifacts"]}
    globals_={r["global_state_id"]:r for r in t13x["global_state_records"]}; classart={r["global_state_id"]:r["artifact_id"] for r in t13x["state_equivalence_class_artifacts"]}; links={(r["block_id"],r["local_state_id"]):r["global_state_id"] for r in t13x["local_to_global_state_links"]}
    weights={r["global_state_id"]:r for r in t14x["global_component_weight_records"]}; arithmetic=t14x["component_scale_arithmetic_records"]; t14art={r["component_id"]:r["artifact_id"] for r in t14x["component_scale_artifacts"]}
    rawm=c["interface_component_multiplier_records"]; req(len(rawm)==len(arithmetic),"exact component multiplier count required"); mult=[]
    for i,(raw,a) in enumerate(zip(rawm,arithmetic)):
        cid=a["component_id"]; req(raw.get("component_id")==cid and raw.get("scale_component_arithmetic_sha256")==a["scale_component_arithmetic_sha256"],f"multiplier {i}: component mismatch")
        v=raw.get("interface_multiplier"); req(type(v) is int and v>0,f"multiplier {cid}: positive integer required")
        r={"component_id":cid,"scale_component_arithmetic_sha256":a["scale_component_arithmetic_sha256"],"interface_multiplier":v,"scale_statement":text(raw.get("scale_statement"),"scale_statement"),"evidence":text(raw.get("evidence"),"evidence")}; r["interface_component_multiplier_sha256"]=cat.canonical_digest(r); mult.append(r)
    req(rawm==mult and math.gcd(*(r["interface_multiplier"] for r in mult))==1,"component multiplier bank must be canonical and primitive")
    multby={r["component_id"]:r["interface_multiplier"] for r in mult}; final={g:multby[w["component_id"]]*w["component_weight"] for g,w in weights.items()}; msha=cat.canonical_digest(mult)
    raws=c.get("interface_component_scale_artifact"); scale=None
    if raws is not None:
        support=sorted(t14art.values())
        req(raws.get("artifact_kind")=="global-interface-component-scale-proof" and raws.get("interface_component_multiplier_records_sha256")==msha and raws.get("support_t14_component_artifact_ids")==support,"bad interface scale artifact")
        scale={"artifact_id":text(raws.get("artifact_id"),"scale artifact ID"),"artifact_kind":"global-interface-component-scale-proof","interface_component_multiplier_records_sha256":msha,"proof_locator":text(raws.get("proof_locator"),"scale locator"),"proof_digest":text(raws.get("proof_digest"),"scale digest"),"proof_statement":text(raws.get("proof_statement"),"scale statement"),"support_t14_component_artifact_ids":support,"evidence":text(raws.get("evidence"),"scale evidence")}; scale["interface_component_scale_artifact_sha256"]=cat.canonical_digest(scale)
    rawrec=c["interface_row_records"]; req(len(rawrec)==len(units),"exact T04 interface row count required"); records=[]
    for i,(raw,u) in enumerate(zip(rawrec,units)):
        b=u["parent_bindings"][0]; p=payload.get(u["unit_id"]); expected={"unit_id":u["unit_id"],"row_id":u["object_id"],"row_kind":u["row_kind"],"unit_identity_sha256":u["unit_identity_sha256"],"parent_global_state_id":b["parent_global_state_id"],"operation_slot_id":b["operation_slot_id"],"t04_population_payload_sha256":None if p is None else p["block_interface_population_payload_sha256"]}
        req(all(raw.get(k)==v for k,v in expected.items()),f"interface row {i}: T04 identity mismatch"); status=raw.get("status"); note=text(raw.get("note"),"row note"); req(status in {"open","proved"},"bad row status")
        loc,dig=raw.get("verification_locator"),raw.get("verification_digest"); req((loc is None and dig is None) if status=="open" else (p is not None and loc==f"interface-row-registry://{u['object_id']}" and isinstance(dig,str) and bool(dig)),"bad row verification fields")
        core={**expected,"status":status,"verification_locator":loc,"note":note}; r={**core,"verification_digest":dig,"interface_row_record_core_sha256":cat.canonical_digest(core)}; r["interface_row_record_sha256"]=cat.canonical_digest(r); records.append(r)
    req(rawrec==records and [r["row_id"] for r in records]==[u["object_id"] for u in units],"noncanonical interface row bank")
    semgroup={r["row_id"]:[] for r in records}
    for s in c["interface_row_semantic_certificates"]: req(s.get("row_id") in semgroup,"unknown row semantic"); semgroup[s["row_id"]].append(s)
    sems=[]
    for u,r in zip(units,records):
        rid=r["row_id"]
        if r["status"]=="open": req(not semgroup[rid],f"open row {rid} has semantics"); continue
        req(len(semgroup[rid])==1 and u["unit_id"] in payload,f"row {rid}: one semantic certificate required"); raw=semgroup[rid][0]; b=u["parent_bindings"][0]; slot,parent=b["operation_slot_id"],b["parent_global_state_id"]
        req(slot in slotsem and slot in slotart and parent in globals_ and parent in classart and parent in weights,f"row {rid}: exact semantic ancestry missing")
        claims_state={x["claim_id"] for x in slotsem[slot]["state_claims"]}; claims_trans={x["claim_id"] for x in slotsem[slot]["transition_claims"]}; pdata=payload[u["unit_id"]]["population_data"]
        fixed=raw.get("fixed_offset"); req(type(fixed) is int,"fixed_offset integer required"); targets_out=[]
        for j,t in enumerate(raw.get("target_semantics",[])):
            g,m=t.get("global_state_id"),t.get("multiplicity"); req(g in globals_ and g in classart and g in weights and globals_[g]["role"]!="auxiliary" and type(m) is int and m>0,f"row {rid} target {j}: invalid")
            x={"global_state_id":g,"multiplicity":m,"global_state_record_sha256":globals_[g]["global_state_record_sha256"],"t13_class_artifact_id":classart[g],"component_id":weights[g]["component_id"],"component_weight":weights[g]["component_weight"],"final_global_weight":final[g],"support_state_claim_ids":idlist(t.get("support_state_claim_ids"),claims_state,"target state support"),"support_transition_claim_ids":idlist(t.get("support_transition_claim_ids"),claims_trans,"target transition support"),"target_statement":text(t.get("target_statement"),"target statement"),"evidence":text(t.get("evidence"),"target evidence")}; x["interface_target_semantic_sha256"]=cat.canonical_digest(x); targets_out.append(x)
        req(raw.get("target_semantics")==targets_out and targets_out==sorted(targets_out,key=lambda x:x["global_state_id"]),f"row {rid}: noncanonical targets")
        load=fixed+sum(x["multiplicity"]*x["final_global_weight"] for x in targets_out); margin=final[parent]-load; req(margin>=0,f"row {rid}: negative margin")
        digests={"t04_target_states_sha256":cat.canonical_digest(pdata["target_states"]),"t04_route_data_sha256":cat.canonical_digest(pdata["route_data"]),"t04_transition_data_sha256":cat.canonical_digest(pdata["transition_data"]),"t04_source_clause_binding_sha256":cat.canonical_digest(pdata["source_clause_binding"])}
        req(all(raw.get(k)==v for k,v in digests.items()),f"row {rid}: T04 payload digest mismatch")
        x={"unit_id":u["unit_id"],"row_id":rid,"row_kind":u["row_kind"],"unit_identity_sha256":u["unit_identity_sha256"],"t04_population_payload_sha256":payload[u["unit_id"]]["block_interface_population_payload_sha256"],"operation_slot_id":slot,"t07_semantic_artifact_id":slotart[slot],"parent_global_state_id":parent,"parent_global_state_record_sha256":globals_[parent]["global_state_record_sha256"],"parent_t13_class_artifact_id":classart[parent],"parent_component_id":weights[parent]["component_id"],"parent_component_weight":weights[parent]["component_weight"],"parent_final_global_weight":final[parent],"parent_state_claim_ids":idlist(raw.get("parent_state_claim_ids"),claims_state,"parent state support"),"parent_transition_claim_ids":idlist(raw.get("parent_transition_claim_ids"),claims_trans,"parent transition support"),**digests,"fixed_offset":fixed,"target_semantics":targets_out,"target_weight":load-fixed,"row_load":load,"margin":margin,"classification":"strict" if margin>0 else "critical-unranked","row_statement":text(raw.get("row_statement"),"row statement"),"evidence":text(raw.get("evidence"),"row evidence")}; x["interface_row_semantic_certificate_sha256"]=cat.canonical_digest(x); sems.append(x)
    req(c["interface_row_semantic_certificates"]==sems,"noncanonical semantic bank"); semby={s["row_id"]:s for s in sems}
    ex=exits(t11x,t12x,links); rawcov=c["interface_exit_coverage_records"]; req(len(rawcov)==len(ex),"exact exit coverage count required"); cov=[]
    for i,(raw,s) in enumerate(zip(rawcov,ex)):
        req(raw.get("exit_subject_id")==s["exit_subject_id"] and raw.get("interface_exit_subject_sha256")==s["interface_exit_subject_sha256"],f"coverage {i}: subject mismatch"); kind,row,terminal=raw.get("disposition_kind"),raw.get("row_id"),raw.get("terminal_id")
        req(kind in {"interface-row","terminal-sink"},"bad exit disposition")
        if kind=="interface-row":
            req(row in semby and terminal is None,"exit row disposition requires proved row"); ts={x["global_state_id"]:x for x in semby[row]["target_semantics"]}; req(semby[row]["parent_global_state_id"]==s["parent_global_state_id"] and s["target_global_state_id"] in ts and ts[s["target_global_state_id"]]["multiplicity"]>=s["multiplicity"],"interface row does not cover exit")
        else: req(row is None and isinstance(terminal,str) and terminal and globals_[s["target_global_state_id"]]["role"]=="sink","terminal disposition only for sink")
        x={"exit_subject_id":s["exit_subject_id"],"interface_exit_subject_sha256":s["interface_exit_subject_sha256"],"disposition_kind":kind,"row_id":row,"terminal_id":terminal,"coverage_statement":text(raw.get("coverage_statement"),"coverage statement"),"evidence":text(raw.get("evidence"),"coverage evidence")}; x["interface_exit_coverage_sha256"]=cat.canonical_digest(x); cov.append(x)
    req(rawcov==cov,"noncanonical exit coverage bank")
    artgroup={r["row_id"]:[] for r in records}
    for a in c["interface_row_artifacts"]: req(a.get("row_id") in artgroup,"unknown row artifact"); artgroup[a["row_id"]].append(a)
    t12art={a["block_id"]:a["artifact_id"] for a in t12x["auxiliary_semantics_artifacts"]}; arts=[]; bundles=[]
    for u,r in zip(units,records):
        rid=r["row_id"]
        if r["status"]=="open": req(not artgroup[rid],f"open row {rid} has artifact"); continue
        req(len(artgroup[rid])==1 and scale is not None and u["unit_id"] in t04art,f"row {rid}: proof prerequisites missing"); raw=artgroup[rid][0]; sem=semby[rid]; rowcov=[x for x in cov if x["row_id"]==rid]
        comps=sorted({sem["parent_component_id"],*(x["component_id"] for x in sem["target_semantics"])}); classes=sorted({sem["parent_t13_class_artifact_id"],*(x["t13_class_artifact_id"] for x in sem["target_semantics"])}); blocks=sorted({s["block_id"] for s,x in zip(ex,cov) if x["row_id"]==rid})
        supports={"support_t04_population_artifact_ids":[t04art[u["unit_id"]]],"support_t07_semantic_artifact_ids":[slotart[u["parent_bindings"][0]["operation_slot_id"]]],"support_t12_auxiliary_artifact_ids":sorted(t12art[b] for b in blocks),"support_t13_class_artifact_ids":classes,"support_t14_component_artifact_ids":sorted(t14art[x] for x in comps),"support_interface_component_scale_artifact_ids":[scale["artifact_id"]]}
        req(raw.get("artifact_kind")=="interface-row-semantic-proof" and raw.get("interface_row_semantic_certificate_sha256")==sem["interface_row_semantic_certificate_sha256"] and raw.get("interface_exit_coverages_sha256")==cat.canonical_digest(rowcov),f"row {rid}: artifact binding mismatch")
        req(all(raw.get(k)==v and raw.get("artifact_id") not in v for k,v in supports.items()),f"row {rid}: exact artifact support required")
        x={"row_id":rid,"artifact_id":text(raw.get("artifact_id"),"artifact ID"),"artifact_kind":"interface-row-semantic-proof","interface_row_semantic_certificate_sha256":sem["interface_row_semantic_certificate_sha256"],"interface_exit_coverages_sha256":cat.canonical_digest(rowcov),"proof_locator":text(raw.get("proof_locator"),"proof locator"),"proof_digest":text(raw.get("proof_digest"),"proof digest"),"proof_statement":text(raw.get("proof_statement"),"proof statement"),**supports,"evidence":text(raw.get("evidence"),"artifact evidence")}; x["interface_row_artifact_sha256"]=cat.canonical_digest(x); arts.append(x)
        b={"row_id":rid,"interface_row_record_core_sha256":r["interface_row_record_core_sha256"],"interface_row_semantic_certificate_sha256":sem["interface_row_semantic_certificate_sha256"],"interface_exit_coverages_sha256":cat.canonical_digest(rowcov),"interface_row_artifact_sha256":x["interface_row_artifact_sha256"]}; b["interface_row_proof_bundle_sha256"]=cat.canonical_digest(b); req(r["verification_digest"]==b["interface_row_proof_bundle_sha256"],f"row {rid}: verification digest mismatch"); bundles.append(b)
    req(c["interface_row_artifacts"]==arts and len({a["artifact_id"] for a in arts})==len(arts),"noncanonical artifact bank")
    counts=Counter(r["status"] for r in records); ready=int(all((t04x["claims"]["t04_block_interface_population_ready"],t07x["claims"]["fate_transition_state_semantics_ready"],t11x["claims"]["t11_recurrent_block_closure_ready"],t12x["claims"]["t12_auxiliary_semantics_ready"],t13x["claims"]["t13_state_equivalence_ready"],t14x["claims"]["t14_component_scales_ready"])) and scale is not None and counts["proved"]==len(records) and len(arts)==len(records) and len(cov)==len(ex))
    bank={"t04_interface_units_sha256":cat.canonical_digest(units),"t07_state_semantics_proof_bank_sha256":t07x["claims"]["state_semantics_proof_bank_sha256"],"t07_transition_proof_bank_sha256":t07x["claims"]["transition_proof_bank_sha256"],"t11_recurrent_block_closure_proof_bank_sha256":t11x["claims"]["t11_recurrent_block_closure_proof_bank_sha256"],"t12_auxiliary_semantics_proof_bank_sha256":t12x["claims"]["auxiliary_semantics_proof_bank_sha256"],"t13_state_equivalence_proof_bank_sha256":t13x["claims"]["state_equivalence_frontier_proof_bank_sha256"],"t14_component_scale_proof_bank_sha256":t14x["claims"]["component_scale_frontier_proof_bank_sha256"],"interface_component_multiplier_records_sha256":cat.canonical_digest(mult),"interface_component_scale_artifact_sha256":None if scale is None else scale["interface_component_scale_artifact_sha256"],"interface_row_records_sha256":cat.canonical_digest(records),"interface_row_semantic_certificates_sha256":cat.canonical_digest(sems),"interface_exit_subjects_sha256":cat.canonical_digest(ex),"interface_exit_coverage_records_sha256":cat.canonical_digest(cov),"interface_row_artifacts_sha256":cat.canonical_digest(arts),"interface_row_proof_bundles_sha256":cat.canonical_digest(bundles)}; bank["interface_exhaustiveness_frontier_proof_bank_sha256"]=cat.canonical_digest(bank)
    close={r["obligation_id"]:r for r in closurex["obligation_closure_records"]}; req(int(close["INTERFACE_RETURN_ROWS_EXHAUSTIVE"]["closed"])==ready,"T15 obligation closure mismatch")
    oa=[a for a in obligx["proof_artifacts"] if a["obligation_id"]=="INTERFACE_RETURN_ROWS_EXHAUSTIVE"]; req(len(oa)==(1 if ready else 0),"T15 obligation artifact presence mismatch")
    if ready:
        support=sorted(a["artifact_id"] for a in obligx["proof_artifacts"] if a["obligation_id"] in {"FATE_TRANSITION_STATE_SEMANTICS","AUXILIARY_EXPANSIONS_SEMANTIC","COMPONENT_SCALE_SEMANTIC"}); a=oa[0]
        req(a["artifact_kind"]=="interface-exhaustiveness-proof" and a["locator"]=="interface-exhaustiveness-frontier://INTERFACE_RETURN_ROWS_EXHAUSTIVE" and a["digest"]==bank["interface_exhaustiveness_frontier_proof_bank_sha256"] and a["support_artifact_ids"]==support,"T15 obligation artifact mismatch")
    results={r["target_id"]:r for r in atomx["target_result_records"]}; req(int(results["T15_INTERFACE_EXHAUSTIVENESS"]["effective_target_complete"])==ready,"T15 target mismatch")
    ta={a["target_id"]:a for a in targetx["atomic_target_artifacts"]}.get("T15_INTERFACE_EXHAUSTIVENESS")
    if ready: req(ta is not None and ta["artifact_kind"]=="interface-exhaustiveness-proof" and ta["proof_locator"]=="interface-exhaustiveness-frontier://T15_INTERFACE_EXHAUSTIVENESS" and ta["proof_digest"]==bank["interface_exhaustiveness_frontier_proof_bank_sha256"],"T15 target artifact mismatch")
    else: req(ta is None,"open T15 target has artifact")
    claims={"expected_interface_rows":len(units),"open_interface_rows":counts["open"],"proved_interface_rows":counts["proved"],"strict_interface_rows":sum(s["classification"]=="strict" for s in sems),"critical_unranked_interface_rows":sum(s["classification"]=="critical-unranked" for s in sems),"final_exit_subjects":len(ex),"minimum_interface_margin":min((s["margin"] for s in sems),default=None),"t15_interface_exhaustiveness_ready":ready,"exact_t04_interface_row_census":1,"exact_t07_row_semantic_support":1,"exact_t13_endpoint_identity":1,"exact_t14_component_weights":1,"exact_t11_t12_final_exit_coverage":1,"critical_rows_deferred_to_t16_rank":1,"noncircular_t15_bank_binding":1,"all_n_proved_by_checker":0,"open_interface_row_ids":[r["row_id"] for r in records if r["status"]=="open"],"interface_exhaustiveness_frontier_proof_bank_sha256":bank["interface_exhaustiveness_frontier_proof_bank_sha256"]}
    return {"interface_component_multiplier_records":mult,"interface_component_scale_artifact":scale,"interface_row_records":records,"interface_row_semantic_certificates":sems,"interface_exit_subjects":ex,"interface_exit_coverage_records":cov,"interface_row_artifacts":arts,"interface_row_proof_bundles":bundles,"interface_exhaustiveness_frontier_proof_bank":bank,"claims":claims}

def validate_certificate(c:Any)->dict[str,Any]:
    req(isinstance(c,dict) and c.get("version")==1,"version 1 certificate required"); exact=exact_certificate(c)
    for k,v in exact.items(): req(c.get(k)==v,f"{k}: incorrect")
    req(c.get("certificate_sha256")==cat.canonical_digest({k:v for k,v in c.items() if k!="certificate_sha256"}),"certificate_sha256: incorrect")
    q=exact["claims"]; return {"rows":q["expected_interface_rows"],"proved":q["proved_interface_rows"],"exits":q["final_exit_subjects"],"critical":q["critical_unranked_interface_rows"],"ready":q["t15_interface_exhaustiveness_ready"],"all_n":0}

def main()->None:
    if len(sys.argv)!=2: raise SystemExit("usage: check_prime_power_interface_exhaustiveness_frontier.py certificate.json")
    print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))
if __name__=="__main__": main()
