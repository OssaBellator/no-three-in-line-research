#!/usr/bin/env python3
"""Extend the installed operation registry through CMR628."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry132Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise Registry132Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="043cc0dfdc5f9509de81da436df1aec8579a7803623d0ace54d6d0dd6904bfdf"
BASE_OPERATION_KIND_COUNT=117
BASE_CONTRACT_COUNT=21
BASE_OWNER_CHANGING_KIND_COUNT=40
NEW_CONTRACT_SHA256="59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f"
NEW_ENTRIES=[{'operation_kind': 'heavy-line-free-cell-absorption', 'source_theorems': ['CMR605', 'CMR606', 'CMR609'], 'owner_effect': 'same-owner', 'payment_class': 'protected-core-growth', 'continuation': 'free heavy-line cells strictly grow the protected matching', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'heavy-line-post-absorption-cap', 'source_theorems': ['CMR607', 'CMR608'], 'owner_effect': 'same-owner', 'payment_class': 'owner-witness-stock', 'continuation': 'surviving heavy-line atoms obey finite protected-core caps', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'heavy-line-large-core-dispatch', 'source_theorems': ['CMR608', 'CMR610'], 'owner_effect': 'same-owner', 'payment_class': 'scheduler-dispatch', 'continuation': 'large protected core enters interface factorization scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'secant-star-matching-vertex-wall', 'source_theorems': ['CMR611', 'CMR615', 'CMR616'], 'owner_effect': 'same-owner', 'payment_class': 'scheduler-dispatch', 'continuation': 'matching-vertex wall enters protected token scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'secant-star-compatible-arm-extraction', 'source_theorems': ['CMR611', 'CMR612'], 'owner_effect': 'same-owner', 'payment_class': 'owner-witness-stock', 'continuation': 'compatible star arms form one finite owned extraction bank', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'secant-star-bulk-absorption', 'source_theorems': ['CMR612', 'CMR613', 'CMR614'], 'owner_effect': 'same-owner', 'payment_class': 'protected-core-growth', 'continuation': 'free star arms strictly grow the protected matching', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'secant-star-large-core-dispatch', 'source_theorems': ['CMR615', 'CMR616'], 'owner_effect': 'same-owner', 'payment_class': 'scheduler-dispatch', 'continuation': 'large protected core enters interface factorization scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-core-cross-skeleton-extraction', 'source_theorems': ['CMR617', 'CMR619', 'CMR620'], 'owner_effect': 'same-owner', 'payment_class': 'owner-witness-stock', 'continuation': 'balanced protected-free interfaces have finite skeleton stock', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-core-product-factorization', 'source_theorems': ['CMR618', 'CMR622'], 'owner_effect': 'factor-child-owner-change', 'payment_class': 'strict-child-descent', 'continuation': 'fixed skeleton factors into protected and free child hosts', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-core-sparse-interface-recursion', 'source_theorems': ['CMR620', 'CMR621', 'CMR622'], 'owner_effect': 'factor-child-owner-change', 'payment_class': 'strict-child-descent', 'continuation': 'small free factor gives strict lower-dimensional recursion', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-skeleton-finite-history', 'source_theorems': ['CMR623'], 'owner_effect': 'same-owner', 'payment_class': 'owner-witness-stock', 'continuation': 'nonrecurrent sparse skeleton histories have finite stock', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-skeleton-factor-diversity', 'source_theorems': ['CMR624', 'CMR625'], 'owner_effect': 'factor-child-owner-change', 'payment_class': 'scheduler-dispatch', 'continuation': 'protected-factor diversity enters matching-state expansion scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-skeleton-cross-churn-payment', 'source_theorems': ['CMR626', 'CMR627'], 'owner_effect': 'same-owner', 'payment_class': 'owner-edge-token-stock', 'continuation': 'skeleton changes consume physical cross-edge token incidence', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-skeleton-recurrent-cross-edge', 'source_theorems': ['CMR626', 'CMR628'], 'owner_effect': 'same-owner', 'payment_class': 'scheduler-dispatch', 'continuation': 'recurrent cross edge enters return and blocker scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}, {'operation_kind': 'protected-interface-history-endpoint', 'source_theorems': ['CMR623', 'CMR624', 'CMR625', 'CMR626', 'CMR627', 'CMR628'], 'owner_effect': 'same-owner', 'payment_class': 'scheduler-dispatch', 'continuation': 'fixed interface history enters factor or churn scheduler', 'contract_sha256': '59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f'}]
CONTRACT={"schema":"prime-power-installed-operation-registry-132/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"honesty_flags":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="833bb6751b69002613c0442f3f1b4180b6c02044361017e4e1e713ec2ea9b298"

def validate(entries: list[dict[str,Any]]) -> dict[str,Any]:
    require(len(entries)==15,"fifteen protected-interface operations required")
    kinds:set[str]=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments:dict[str,int]={}
    owners={"same-owner","factor-child-owner-change"}; classes={"protected-core-growth","owner-witness-stock","scheduler-dispatch","strict-child-descent","owner-edge-token-stock"}
    for i,e in enumerate(entries):
        p=f"entry[{i}]"; kind=e.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{p}: unique kind"); kinds.add(kind)
        require(e.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{p}: contract")
        src=e.get("source_theorems"); require(isinstance(src,list) and src and all(isinstance(s,str) and s.startswith("CMR") for s in src),f"{p}: ancestry")
        owner=e.get("owner_effect"); pay=e.get("payment_class"); cont=e.get("continuation")
        require(owner in owners,f"{p}: owner"); require(pay in classes,f"{p}: payment"); require(isinstance(cont,str) and cont,f"{p}: continuation")
        if pay=="scheduler-dispatch": require("scheduler" in cont,f"{p}: scheduler continuation")
        if pay=="protected-core-growth": require("grow" in cont,f"{p}: growth continuation")
        if pay=="strict-child-descent": require(owner=="factor-child-owner-change" and ("factor" in cont or "recursion" in cont),f"{p}: child descent")
        owner_changes += owner!="same-owner"; payments[pay]=payments.get(pay,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==132,"132 installed kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":132,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":132-owner_changes,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[2].update(continuation="terminal"),lambda x:x[8].update(owner_effect="same-owner"),lambda x:x[0].update(continuation="finite"),lambda x:x.pop()]
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(NEW_ENTRIES); mut(bad)
        try: validate(bad)
        except Registry132Error: rejected+=1
    require(rejected==len(muts),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    report={"contract_digest":contract,"census":census,"installed_transition_kind_bank_132_exhaustive":1,"protected_interface_execution_operations_registered":1,"installed_payment_assignment_132_complete":1,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__": main()
