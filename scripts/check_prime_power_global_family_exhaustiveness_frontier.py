#!/usr/bin/env python3
"""Exact documentary T19 global-family exhaustiveness frontier.

T02 supplies the expected global-parent applications and T18 supplies the final row family.  Every row
is rebound to its exact T04 case/clause/slot ancestry.  No independently supplied global integer family
or legacy global-family skeleton certificate is accepted as proof of T19.  This checks finite identity,
coverage and typed support only and always reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json, sys
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as targets
import check_prime_power_block_interface_population_frontier as t04
import check_prime_power_canonical_raw_host_catalogue as cat
import check_prime_power_obligation_artifact_registry as obligations
import check_prime_power_row_theorem_frontier as t18
import check_prime_power_rule_exhaustiveness_frontier as t02


class T19Error(ValueError): pass

def req(value: bool, message: str) -> None:
    if not value: raise T19Error(message)

def text(value: Any, path: str) -> str:
    req(isinstance(value, str) and bool(value), f"{path}: nonempty string required"); return value

def ids(value: Any, expected: list[str], path: str) -> list[str]:
    req(isinstance(value, list) and value == expected, f"{path}: exact list required")
    req(value == sorted(value) and len(value) == len(set(value)), f"{path}: sorted/unique required")
    req(all(isinstance(item, str) and item for item in value), f"{path}: bad ID"); return list(value)


@contextmanager
def corrected_roots():
    """Expose the corrected T02+T18 proof root and remove the legacy T19 certificate support."""
    definition = atomic.TARGETS["T19_GLOBAL_FAMILY"]
    old_proof, old_research = definition["proof_dependency_target_ids"], definition["research_dependency_target_ids"]
    old_special = targets.special_certificate_support
    definition["proof_dependency_target_ids"] = ("T02_RULE_EXHAUSTIVENESS", "T18_ROW_THEOREMS")
    definition["research_dependency_target_ids"] = ("T18_ROW_THEOREMS",)
    def special(target_id: str, surfaces: dict[str, Any]) -> list[str]:
        return [] if target_id == "T19_GLOBAL_FAMILY" else old_special(target_id, surfaces)
    targets.special_certificate_support = special
    try: yield
    finally:
        definition["proof_dependency_target_ids"], definition["research_dependency_target_ids"] = old_proof, old_research
        targets.special_certificate_support = old_special


def applications(t02x: dict[str, Any]) -> list[dict[str, Any]]:
    return [r for r in t02x["rule_exhaustiveness_records"] if r["record_kind"] == "global-parent-application"]


def row_ancestry(subject: dict[str, Any], theorem: dict[str, Any], theorem_artifact: str | None,
                 application: dict[str, Any], application_artifact: str | None, unit: dict[str, Any],
                 payload: dict[str, Any] | None, population_artifact: str | None) -> dict[str, Any]:
    parent, identity = subject["parent_global_state_id"], application["identity"]
    binding = [b for b in unit["parent_bindings"] if b["parent_global_state_id"] == parent]
    req(len(binding) == 1, f"row {subject['final_row_id']}: exact T04 parent binding required"); binding = binding[0]
    req(subject["selected_slot_id"] == identity["operation_slot_id"], f"row {subject['final_row_id']}: T02/T18 slot mismatch")
    for key in ("source_case_id", "source_clause_id", "operation_slot_id"):
        req(binding[key] == identity[key], f"row {subject['final_row_id']}: T02/T04 {key} mismatch")
    expected_kind = "recurrent-block" if subject["source_kind"] == "recurrent" else "interface-row"
    req(unit["unit_kind"] == expected_kind, f"row {subject['final_row_id']}: wrong T04 unit kind")
    req(unit["object_id"] == (subject["block_id"] if subject["source_kind"] == "recurrent" else subject["row_id"]),
        f"row {subject['final_row_id']}: T04 object mismatch")
    out = {
        "final_row_id": subject["final_row_id"], "final_row_subject_sha256": subject["final_row_subject_sha256"],
        "source_kind": subject["source_kind"], "row_id": subject["row_id"], "block_id": subject["block_id"],
        "parent_global_state_id": parent, "source_case_id": identity["source_case_id"],
        "source_clause_id": identity["source_clause_id"], "operation_slot_id": identity["operation_slot_id"],
        "t02_application_record_id": application["record_id"],
        "t02_application_record_sha256": application["rule_exhaustiveness_record_sha256"],
        "t02_application_artifact_id": application_artifact, "t04_unit_id": unit["unit_id"],
        "t04_unit_identity_sha256": unit["unit_identity_sha256"],
        "t04_parent_binding_sha256": binding["parent_binding_sha256"],
        "t04_population_payload_sha256": None if payload is None else payload["block_interface_population_payload_sha256"],
        "t04_population_artifact_id": population_artifact,
        "t18_row_theorem_record_sha256": theorem["final_row_theorem_record_sha256"],
        "t18_row_theorem_status": theorem["status"], "t18_row_theorem_artifact_id": theorem_artifact,
    }
    out["global_family_row_ancestry_sha256"] = cat.canonical_digest(out); return out


def status(raw: dict[str, Any], application: dict[str, Any], rows: list[dict[str, Any]], path: str) -> dict[str, Any]:
    identity, parent = application["identity"], application["identity"]["parent_global_state_id"]
    core = {
        "coverage_id": f"global-family-coverage::{parent}", "parent_global_state_id": parent,
        "t02_application_record_id": application["record_id"],
        "t02_application_record_sha256": application["rule_exhaustiveness_record_sha256"],
        "source_case_id": identity["source_case_id"], "source_clause_id": identity["source_clause_id"],
        "operation_slot_id": identity["operation_slot_id"],
        "expected_final_row_ids": [r["final_row_id"] for r in rows],
        "row_ancestry_records_sha256": cat.canonical_digest(rows), "status": raw.get("status"),
        "verification_locator": raw.get("verification_locator"), "note": text(raw.get("note"), f"{path}.note"),
    }
    for key, value in core.items(): req(raw.get(key) == value, f"{path}.{key}: mismatch")
    req(core["status"] in {"open", "proved"}, f"{path}.status: open/proved required")
    digest = raw.get("verification_digest")
    if core["status"] == "open": req(core["verification_locator"] is None and digest is None, f"{path}: open verification")
    else: req(core["verification_locator"] == f"global-family-coverage-registry://{parent}" and isinstance(digest, str) and digest,
              f"{path}: canonical proved verification required")
    out = {**core, "verification_digest": digest, "global_family_coverage_record_core_sha256": cat.canonical_digest(core)}
    out["global_family_coverage_record_sha256"] = cat.canonical_digest(out); return out


def semantic(raw: dict[str, Any], record: dict[str, Any], application: dict[str, Any], rows: list[dict[str, Any]], path: str) -> dict[str, Any]:
    parent = record["parent_global_state_id"]
    req(raw.get("coverage_id") == record["coverage_id"] and raw.get("parent_global_state_id") == parent,
        f"{path}: identity mismatch")
    req(application["status"] == "proved" and bool(rows), f"{path}: proved application and nonempty rows required")
    req(all(r["t18_row_theorem_status"] == "proved" and r["t02_application_artifact_id"]
            and r["t04_population_artifact_id"] and r["t18_row_theorem_artifact_id"] for r in rows),
        f"{path}: complete proved row ancestry required")
    req(raw.get("row_ancestry_records") == rows, f"{path}: exact row ancestry required")
    out = {
        "coverage_id": record["coverage_id"], "parent_global_state_id": parent,
        "source_case_id": record["source_case_id"], "source_clause_id": record["source_clause_id"],
        "operation_slot_id": record["operation_slot_id"],
        "t02_application_record_sha256": application["rule_exhaustiveness_record_sha256"],
        "row_ancestry_records": rows, "row_ancestry_records_sha256": cat.canonical_digest(rows),
        "application_exhaustiveness_statement": text(raw.get("application_exhaustiveness_statement"), f"{path}.application statement"),
        "row_alternative_exhaustiveness_statement": text(raw.get("row_alternative_exhaustiveness_statement"), f"{path}.row statement"),
        "source_clause_interpretation": text(raw.get("source_clause_interpretation"), f"{path}.clause interpretation"),
        "evidence": text(raw.get("evidence"), f"{path}.evidence"),
    }
    out["global_family_coverage_semantic_sha256"] = cat.canonical_digest(out); return out


def artifact(raw: dict[str, Any], record: dict[str, Any], sem: dict[str, Any], app_artifact: str,
             rows: list[dict[str, Any]], path: str) -> dict[str, Any]:
    t04s = sorted({r["t04_population_artifact_id"] for r in rows}); t18s = sorted({r["t18_row_theorem_artifact_id"] for r in rows})
    req(None not in t04s and None not in t18s, f"{path}: null proved support")
    req(raw.get("coverage_id") == record["coverage_id"] and raw.get("artifact_kind") == "global-family-parent-coverage-proof",
        f"{path}: identity/kind mismatch")
    req(raw.get("global_family_coverage_semantic_sha256") == sem["global_family_coverage_semantic_sha256"], f"{path}: semantic mismatch")
    ids(raw.get("support_t02_application_artifact_ids"), [app_artifact], f"{path}.T02 support")
    ids(raw.get("support_t04_population_artifact_ids"), t04s, f"{path}.T04 support")
    ids(raw.get("support_t18_row_theorem_artifact_ids"), t18s, f"{path}.T18 support")
    out = {
        "coverage_id": record["coverage_id"], "artifact_id": text(raw.get("artifact_id"), f"{path}.artifact ID"),
        "artifact_kind": "global-family-parent-coverage-proof",
        "global_family_coverage_semantic_sha256": sem["global_family_coverage_semantic_sha256"],
        "proof_locator": text(raw.get("proof_locator"), f"{path}.locator"),
        "proof_digest": text(raw.get("proof_digest"), f"{path}.digest"),
        "proof_statement": text(raw.get("proof_statement"), f"{path}.statement"),
        "support_t02_application_artifact_ids": [app_artifact], "support_t04_population_artifact_ids": t04s,
        "support_t18_row_theorem_artifact_ids": t18s, "evidence": text(raw.get("evidence"), f"{path}.evidence"),
    }
    req(out["artifact_id"] not in [app_artifact, *t04s, *t18s], f"{path}: self support")
    out["global_family_coverage_artifact_sha256"] = cat.canonical_digest(out); return out


def _exact(c: dict[str, Any]) -> dict[str, Any]:
    t18c = c.get("row_theorem_frontier_certificate"); req(isinstance(t18c, dict), "T18 certificate required")
    for key in ("global_family_coverage_records", "global_family_coverage_semantic_certificates",
                "global_family_coverage_artifacts", "global_family_coverage_proof_bundles"):
        req(isinstance(c.get(key), list), f"{key}: list required")
    t18.validate_certificate(t18c); t18x = t18.exact_certificate(t18c)
    t17c=t18c["state_predicate_frontier_certificate"]; t16c=t17c["global_rank_frontier_certificate"]
    t15c=t16c["interface_exhaustiveness_frontier_certificate"]; t14c=t15c["component_scale_frontier_certificate"]
    t13c=t14c["state_equivalence_frontier_certificate"]; t07c=t13c["fate_transition_state_frontier_certificate"]
    t04c=t07c["block_interface_population_frontier_certificate"]; t04.validate_certificate(t04c); t04x=t04.exact_certificate(t04c)
    t02c=t04c["slot_candidate_population_frontier_certificate"]["rule_exhaustiveness_frontier_certificate"]
    t02.validate_certificate(t02c); t02x=t02.exact_certificate(t02c)
    registry=t04c["atomic_target_artifact_registry_certificate"]; targets.validate_certificate(registry); targetx=targets.exact_certificate(registry)
    atomc=registry["current_frontier_execution_certificate"]["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomc); atomx=atomic.exact_certificate(atomc)
    source=t02c["source_truth_frontier_execution_certificate"]["source_statement_truth_registry_certificate"]
    obligc=source["obligation_artifact_registry_certificate"]; obligations.validate_certificate(obligc); obligx=obligations.exact_certificate(obligc)
    closurex=closure.exact_certificate(obligc["all_n_implication_closure_certificate"])

    apps=applications(t02x); appby={a["identity"]["parent_global_state_id"]:a for a in apps}; req(len(appby)==len(apps),"duplicate T02 parent")
    t02art={a["record_id"]:a["artifact_id"] for a in t02x["rule_exhaustiveness_artifacts"]}
    units=t04x["expected_block_interface_population_units"]
    blocks={u["object_id"]:u for u in units if u["unit_kind"]=="recurrent-block"}; interfaces={u["object_id"]:u for u in units if u["unit_kind"]=="interface-row"}
    payload={p["unit_id"]:p for p in t04x["block_interface_population_payloads"]}; t04art={a["unit_id"]:a["artifact_id"] for a in t04x["block_interface_population_artifacts"]}
    theorem={r["final_row_id"]:r for r in t18x["final_row_theorem_records"]}; t18art={a["final_row_id"]:a["artifact_id"] for a in t18x["global_row_theorem_artifacts"]}
    byparent={p:[] for p in appby}; rows=[]
    for subject in t18x["final_row_subjects"]:
        fid,parent=subject["final_row_id"],subject["parent_global_state_id"]; req(parent in appby and fid in theorem,f"row {fid}: missing T02/T18 ancestry")
        unit=blocks.get(subject["block_id"]) if subject["source_kind"]=="recurrent" else interfaces.get(subject["row_id"]); req(unit is not None,f"row {fid}: T04 unit missing")
        r=row_ancestry(subject,theorem[fid],t18art.get(fid),appby[parent],t02art.get(appby[parent]["record_id"]),unit,payload.get(unit["unit_id"]),t04art.get(unit["unit_id"]))
        byparent[parent].append(r); rows.append(r)
    for group in byparent.values(): group.sort(key=lambda r:r["final_row_id"])
    rows.sort(key=lambda r:r["final_row_id"]); req(len({r["final_row_id"] for r in rows})==len(rows),"duplicate final row")

    rawrec=c["global_family_coverage_records"]; req(len(rawrec)==len(apps) and [r.get("parent_global_state_id") for r in rawrec]==[a["identity"]["parent_global_state_id"] for a in apps],"exact T02 parent order required")
    records=[status(raw,a,byparent[a["identity"]["parent_global_state_id"]],f"coverage[{i}]") for i,(raw,a) in enumerate(zip(rawrec,apps))]
    req(rawrec==records,"noncanonical T19 records"); recby={r["parent_global_state_id"]:r for r in records}
    semgroup={p:[] for p in appby}
    for raw in c["global_family_coverage_semantic_certificates"]: req(raw.get("parent_global_state_id") in semgroup,"unknown T19 semantic parent"); semgroup[raw["parent_global_state_id"]].append(raw)
    sems=[]; semby={}
    for a in apps:
        p=a["identity"]["parent_global_state_id"]; rec=recby[p]; group=semgroup[p]
        if rec["status"]=="open": req(not group,f"parent {p}: open semantics"); continue
        req(len(group)==1,f"parent {p}: one semantic required"); s=semantic(group[0],rec,a,byparent[p],f"semantic[{p}]"); sems.append(s); semby[p]=s
    req(c["global_family_coverage_semantic_certificates"]==sems,"noncanonical T19 semantics")
    artgroup={p:[] for p in appby}
    for raw in c["global_family_coverage_artifacts"]:
        p=raw.get("coverage_id","").removeprefix("global-family-coverage::"); req(p in artgroup,"unknown T19 artifact parent"); artgroup[p].append(raw)
    arts=[]; bundles=[]
    for a in apps:
        p=a["identity"]["parent_global_state_id"]; rec=recby[p]; group=artgroup[p]
        if rec["status"]=="open": req(not group,f"parent {p}: open artifact"); continue
        req(len(group)==1 and a["record_id"] in t02art,f"parent {p}: one artifact and T02 support required")
        ar=artifact(group[0],rec,semby[p],t02art[a["record_id"]],byparent[p],f"artifact[{p}]"); arts.append(ar)
        b={"coverage_id":rec["coverage_id"],"global_family_coverage_record_core_sha256":rec["global_family_coverage_record_core_sha256"],
           "global_family_coverage_semantic_sha256":semby[p]["global_family_coverage_semantic_sha256"],
           "global_family_coverage_artifact_sha256":ar["global_family_coverage_artifact_sha256"],
           "support_t02_application_artifact_ids":ar["support_t02_application_artifact_ids"],
           "support_t04_population_artifact_ids":ar["support_t04_population_artifact_ids"],
           "support_t18_row_theorem_artifact_ids":ar["support_t18_row_theorem_artifact_ids"]}
        b["global_family_coverage_proof_bundle_sha256"]=cat.canonical_digest(b); req(rec["verification_digest"]==b["global_family_coverage_proof_bundle_sha256"],f"parent {p}: verification mismatch"); bundles.append(b)
    req(c["global_family_coverage_artifacts"]==arts and c["global_family_coverage_proof_bundles"]==bundles,"noncanonical T19 artifacts/bundles")
    req(len({a["artifact_id"] for a in arts})==len(arts),"duplicate T19 artifact ID")

    counts=Counter(r["status"] for r in records); t02ready=int(t02x["claims"]["rule_exhaustiveness_ready"]); t18ready=int(t18x["claims"]["t18_row_theorems_ready"])
    ready=int(t02ready and t18ready and counts["proved"]==len(records) and len(sems)==len(records)==len(arts)
              and all(byparent.values()) and len(rows)==len(t18x["final_row_subjects"]))
    bank={"t02_rule_exhaustiveness_proof_bundle_sha256":t02x["claims"]["rule_exhaustiveness_proof_bundle_sha256"],
          "t04_expected_units_sha256":cat.canonical_digest(units),"t04_population_payloads_sha256":cat.canonical_digest(t04x["block_interface_population_payloads"]),
          "t18_row_theorem_frontier_proof_bank_sha256":t18x["claims"]["row_theorem_frontier_proof_bank_sha256"],
          "t02_global_parent_applications_sha256":cat.canonical_digest(apps),"global_family_row_ancestry_records_sha256":cat.canonical_digest(rows),
          "global_family_coverage_records_sha256":cat.canonical_digest(records),"global_family_coverage_semantic_certificates_sha256":cat.canonical_digest(sems),
          "global_family_coverage_artifacts_sha256":cat.canonical_digest(arts),"global_family_coverage_proof_bundles_sha256":cat.canonical_digest(bundles)}
    bank["global_family_exhaustiveness_frontier_proof_bank_sha256"]=cat.canonical_digest(bank)
    closed={r["obligation_id"]:r for r in closurex["obligation_closure_records"]}; req(int(closed["EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE"]["closed"])==ready,"T19 obligation closure mismatch")
    o=[a for a in obligx["proof_artifacts"] if a["obligation_id"]=="EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE"]; req(len(o)==(1 if ready else 0),"T19 obligation artifact presence mismatch")
    if ready:
        oa=o[0]; dep=set(closure.OBLIGATION_DEPENDENCIES["EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE"]); support=sorted(a["artifact_id"] for a in obligx["proof_artifacts"] if a["obligation_id"] in dep)
        req(oa["artifact_kind"]=="global-family-exhaustiveness-proof" and oa["locator"]=="global-family-exhaustiveness-frontier://EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE"
            and oa["digest"]==bank["global_family_exhaustiveness_frontier_proof_bank_sha256"] and oa["support_artifact_ids"]==support,"T19 obligation artifact mismatch")
    results={r["target_id"]:r for r in atomx["target_result_records"]}; req(int(results["T19_GLOBAL_FAMILY"]["effective_target_complete"])==ready,"T19 target completion mismatch")
    target={a["target_id"]:a for a in targetx["atomic_target_artifacts"]}.get("T19_GLOBAL_FAMILY")
    if ready: req(target is not None and target["artifact_kind"]=="global-family-proof" and target["proof_locator"]=="global-family-exhaustiveness-frontier://T19_GLOBAL_FAMILY" and target["proof_digest"]==bank["global_family_exhaustiveness_frontier_proof_bank_sha256"],"T19 target artifact mismatch")
    else: req(target is None,"open T19 target has artifact")
    claims={"expected_global_parent_applications":len(apps),"derived_final_rows":len(rows),"recurrent_final_rows":sum(r["source_kind"]=="recurrent" for r in rows),
            "interface_final_rows":sum(r["source_kind"]=="interface" for r in rows),"open_global_family_coverages":counts["open"],"proved_global_family_coverages":counts["proved"],
            "t02_rule_exhaustiveness_ready":t02ready,"t18_row_theorems_ready":t18ready,"t19_global_family_exhaustiveness_ready":ready,
            "exact_t02_application_census":1,"exact_t18_final_row_census":1,"exact_t04_source_clause_ancestry":1,"exact_parent_slot_row_partition":1,
            "legacy_parallel_global_family_excluded":1,"corrected_t02_t18_target_root":1,"noncircular_t19_bank_binding":1,"all_n_proved_by_checker":0,
            "open_parent_global_state_ids":[r["parent_global_state_id"] for r in records if r["status"]=="open"],
            "global_family_row_ancestry_records_sha256":cat.canonical_digest(rows),"global_family_exhaustiveness_frontier_proof_bank_sha256":bank["global_family_exhaustiveness_frontier_proof_bank_sha256"]}
    return {"global_family_row_ancestry_records":rows,"global_family_coverage_records":records,"global_family_coverage_semantic_certificates":sems,
            "global_family_coverage_artifacts":arts,"global_family_coverage_proof_bundles":bundles,
            "global_family_exhaustiveness_frontier_proof_bank":bank,"claims":claims}


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    with corrected_roots(): return _exact(certificate)

def validate_certificate(certificate: Any) -> dict[str, Any]:
    req(isinstance(certificate,dict) and certificate.get("version")==1,"version 1 certificate required"); exact=exact_certificate(certificate)
    for key,value in exact.items(): req(certificate.get(key)==value,f"{key}: incorrect")
    payload={k:v for k,v in certificate.items() if k!="certificate_sha256"}; req(certificate.get("certificate_sha256")==cat.canonical_digest(payload),"certificate digest incorrect")
    c=exact["claims"]; return {"parents":c["expected_global_parent_applications"],"rows":c["derived_final_rows"],"proved":c["proved_global_family_coverages"],"ready":c["t19_global_family_exhaustiveness_ready"],"all_n":0}

def build_certificate(t18_certificate:dict[str,Any],records:list[dict[str,Any]],semantics:list[dict[str,Any]],artifacts:list[dict[str,Any]])->dict[str,Any]:
    c={"version":1,"row_theorem_frontier_certificate":t18_certificate,"global_family_coverage_records":records,
       "global_family_coverage_semantic_certificates":semantics,"global_family_coverage_artifacts":artifacts,"global_family_coverage_proof_bundles":[]}
    c.update(exact_certificate(c)); c["certificate_sha256"]=cat.canonical_digest(c); return c

def main()->None:
    if len(sys.argv)!=2: raise SystemExit("usage: check_prime_power_global_family_exhaustiveness_frontier.py certificate.json")
    print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))

if __name__=="__main__": main()
