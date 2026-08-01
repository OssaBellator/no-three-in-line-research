#!/usr/bin/env python3
from __future__ import annotations
import copy,hashlib,json
from typing import Any

class Registry39Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise Registry39Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
BASE_REGISTRY_SHA256="5fa644a7cd340834eec7aa1776b1dcdad102749878664e3259c9be5c5a9b5ae2"
BASE_OPERATION_KIND_COUNT=33
BASE_CONTRACT_COUNT=13
BASE_OWNER_CHANGING_KIND_COUNT=24
NEW_CONTRACT_SHA256="b97b2553cf5548cfc32a022172d2e011bc60952021d87178ae0e0fdc673ecc23"
NEW_ENTRIES=[
{"operation_kind":"rollback-level-skeleton-restriction","source_theorems":["CMR462","CMR463","CMR464","CMR465","CMR466"],"owner_effect":"same-owner","payment_class":"owner-witness-stock","continuation":"finite sparse skeleton followed by residual level scheduler"},
{"operation_kind":"rollback-residual-level-factorization","source_theorems":["CMR464","CMR465"],"owner_effect":"factor-child-owner-change","payment_class":"scheduler-dispatch","continuation":"independent residual level scheduler required"},
{"operation_kind":"same-level-colour-source-split","source_theorems":["CMR467","CMR468","CMR469"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"colour factor or mixed-cycle scheduler required"},
{"operation_kind":"colour-separated-level-factorization","source_theorems":["CMR470","CMR471"],"owner_effect":"factor-child-owner-change","payment_class":"scheduler-dispatch","continuation":"independent marked and unmarked factor scheduler required"},
{"operation_kind":"mixed-colour-cycle-batch-flip","source_theorems":["CMR472","CMR473","CMR474","CMR475"],"owner_effect":"same-owner","payment_class":"scheduler-dispatch","continuation":"simultaneous zero-cost cycle scheduler required"},
{"operation_kind":"mixed-cycle-sparse-tail-deletion","source_theorems":["CMR476"],"owner_effect":"factor-child-owner-change","payment_class":"strict-child-descent","continuation":"delete sparse matching-pair interface and enter colour-separated residual factors"},
]
for e in NEW_ENTRIES:e["contract_sha256"]=NEW_CONTRACT_SHA256
CONTRACT={"schema":"prime-power-installed-operation-registry-39/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"honesty_flags":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="92bea6f0961abd2c2c6799cd7171ff6c16a05e5cb37da9378ebe21545ace8437"
def validate(entries):
    require(len(entries)==6,"six level/colour entries required")
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for i,e in enumerate(entries):
        p=f"entry[{i}]"; kind=e.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{p}: unique kind")
        kinds.add(kind); require(e.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{p}: contract")
        src=e.get("source_theorems"); require(isinstance(src,list) and src and all(isinstance(x,str) and x.startswith("CMR") for x in src),f"{p}: sources")
        owner=e.get("owner_effect"); pay=e.get("payment_class"); cont=e.get("continuation")
        require(owner in {"same-owner","factor-child-owner-change"},f"{p}: owner")
        require(pay in {"owner-witness-stock","scheduler-dispatch","strict-child-descent"},f"{p}: payment")
        require(isinstance(cont,str) and cont,f"{p}: continuation")
        if pay=="scheduler-dispatch": require("scheduler" in cont,f"{p}: scheduler")
        owner_changes += owner!="same-owner"; payments[pay]=payments.get(pay,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==39,"39 kinds")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":39,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":39-owner_changes,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}
def mutation_audit():
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[1].update(continuation="terminal"),lambda x:x.pop()]
    rejected=0
    for m in muts:
        bad=copy.deepcopy(NEW_ENTRIES);m(bad)
        try:validate(bad)
        except Registry39Error:rejected+=1
    require(rejected==len(muts),"mutation accepted");return rejected
def main():
    cd=digest(CONTRACT);require(cd==EXPECTED_CONTRACT_DIGEST,"contract digest")
    census=validate(copy.deepcopy(NEW_ENTRIES));census["rejected_corruptions"]=mutation_audit()
    report={"contract_digest":cd,"census":census,"installed_transition_kind_bank_39_exhaustive":1,"rollback_level_colour_cycle_operations_registered":1,"installed_payment_assignment_39_complete":1,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__":main()
