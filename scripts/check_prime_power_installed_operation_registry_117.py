#!/usr/bin/env python3
"""Extend the installed operation registry through CMR604."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry117Error(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise Registry117Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BASE_REGISTRY_SHA256 = "4732c504824406c78b9a9e92033994f30be1c744e633a5e49dcc5531497e00ae"
BASE_OPERATION_KIND_COUNT = 98
BASE_CONTRACT_COUNT = 20
BASE_OWNER_CHANGING_KIND_COUNT = 36
NEW_CONTRACT_SHA256 = "b82d83290aa95e41743fe1db9dbbf3a26c09801f40888e42cc1c8e0f0eefd0f0"
NEW_ENTRIES = [
 {"operation_kind":"disjoint-conflict-local-deletion","source_theorems":["CMR577","CMR579","CMR581"],"owner_effect":"host-owner-change","payment_class":"local-family-restriction","continuation":"matching-preserving edge deletion kills one packed conflict"},
 {"operation_kind":"disjoint-conflict-fully-forced-dispatch","source_theorems":["CMR577","CMR578","CMR581"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"fully forced packed certificate enters terminal certificate scheduler"},
 {"operation_kind":"disjoint-conflict-private-restoration-payment","source_theorems":["CMR579","CMR580","CMR581"],"owner_effect":"restoration-owner-change","payment_class":"edge-reintroduction","continuation":"recreated packed conflict pays its private restored edge"},
 {"operation_kind":"protected-contact-finite-stock","source_theorems":["CMR582","CMR583"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"blocked physical contact edges have finite protected-state stock"},
 {"operation_kind":"protected-contact-wall-extraction","source_theorems":["CMR584"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"distinct protected contacts enter row-column wall scheduler"},
 {"operation_kind":"protected-contact-heavy-token","source_theorems":["CMR585"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"one owned full-prefix token carries a heavy contact wall"},
 {"operation_kind":"protected-contact-dispersed-token-bank","source_theorems":["CMR585"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"distinct owned token cells consume finite witness stock"},
 {"operation_kind":"protected-contact-reintroduction-payment","source_theorems":["CMR586"],"owner_effect":"restoration-owner-change","payment_class":"edge-reintroduction","continuation":"recurrent protected contact pays absent-to-present returns"},
 {"operation_kind":"protected-contact-persistent-dispatch","source_theorems":["CMR586"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"persistent protected contact enters blocker scheduler"},
 {"operation_kind":"recurrent-unavailable-set-extraction","source_theorems":["CMR587","CMR592"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"uniform unavailable subset consumes finite selector-set stock"},
 {"operation_kind":"recurrent-set-aggregate-reintroduction","source_theorems":["CMR588","CMR592"],"owner_effect":"restoration-owner-change","payment_class":"edge-reintroduction","continuation":"joint unavailable set pays aggregate edge returns"},
 {"operation_kind":"recurrent-set-batch-absorption","source_theorems":["CMR589","CMR590","CMR592"],"owner_effect":"same-owner","payment_class":"protected-core-growth","continuation":"batch absorption strictly grows the protected matching"},
 {"operation_kind":"recurrent-set-small-cover-wall","source_theorems":["CMR589","CMR591","CMR592"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"small cover yields a persistent wall and token scheduler"},
 {"operation_kind":"weak-slack-near-static-dispatch","source_theorems":["CMR593","CMR594","CMR598"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"threshold-one selector enters static geometry scheduler"},
 {"operation_kind":"persistent-core-amplification","source_theorems":["CMR595","CMR596","CMR597","CMR598"],"owner_effect":"same-owner","payment_class":"protected-core-growth","continuation":"conditioned recurrence grows one jointly persistent unavailable core"},
 {"operation_kind":"owner-labelled-protected-state-stock","source_theorems":["CMR599"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"selector absorption states have finite owner-labelled stock"},
 {"operation_kind":"owner-labelled-line-stock","source_theorems":["CMR600","CMR603","CMR604"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"owned real-line certificates have finite stock"},
 {"operation_kind":"owner-labelled-token-edge-stock","source_theorems":["CMR601","CMR602","CMR604"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"owned token-edge certificates have finite stock"},
 {"operation_kind":"owner-labelled-certificate-recurrence","source_theorems":["CMR602","CMR603","CMR604"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"recurrent owned line or token certificate enters fixed-certificate scheduler"},
]
for e in NEW_ENTRIES: e["contract_sha256"] = NEW_CONTRACT_SHA256
CONTRACT={"schema":"prime-power-installed-operation-registry-117/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"honesty_flags":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="4c961b63515c0a8ac986f9ab0a11cef7ad33df3d012fbbe0ca23bcf95a2324eb"

def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==19,"nineteen protected-certificate operations required")
    kinds:set[str]=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments:dict[str,int]={}
    allowed_owners={"same-owner","host-owner-change","restoration-owner-change"}
    allowed_payments={"local-family-restriction","scheduler-dispatch","edge-reintroduction","owner-witness-stock","protected-core-growth"}
    for i,e in enumerate(entries):
        p=f"entry[{i}]"; kind=e.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{p}: unique kind"); kinds.add(kind)
        require(e.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{p}: contract")
        src=e.get("source_theorems"); require(isinstance(src,list) and src and all(isinstance(s,str) and s.startswith("CMR") for s in src),f"{p}: ancestry")
        owner=e.get("owner_effect"); pay=e.get("payment_class"); cont=e.get("continuation")
        require(owner in allowed_owners,f"{p}: owner"); require(pay in allowed_payments,f"{p}: payment"); require(isinstance(cont,str) and cont,f"{p}: continuation")
        if pay=="scheduler-dispatch": require("scheduler" in cont,f"{p}: scheduler")
        if pay=="edge-reintroduction": require(owner=="restoration-owner-change",f"{p}: restoration owner")
        if pay=="local-family-restriction": require(owner=="host-owner-change",f"{p}: host owner")
        if pay=="protected-core-growth": require("grow" in cont,f"{p}: growth continuation")
        owner_changes += owner != "same-owner"; payments[pay]=payments.get(pay,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==117,"117 installed kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":117,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":117-owner_changes,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[1].update(continuation="terminal"),lambda x:x[2].update(owner_effect="same-owner"),lambda x:x[11].update(continuation="finite"),lambda x:x.pop()]
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(NEW_ENTRIES); mut(bad)
        try: validate(bad)
        except Registry117Error: rejected+=1
    require(rejected==len(muts),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    report={"contract_digest":contract,"census":census,"installed_transition_kind_bank_117_exhaustive":1,"selector_protected_certificate_operations_registered":1,"installed_payment_assignment_117_complete":1,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__": main()
