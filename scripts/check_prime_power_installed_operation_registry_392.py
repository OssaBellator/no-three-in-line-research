#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1093."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
from protected_surplus_registry_entries_a import ENTRIES as ENTRIES_A
from protected_surplus_registry_entries_b import ENTRIES as ENTRIES_B

class Registry392Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise Registry392Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="d9ffac41011c852e26970444cf96c34632d5d44c29eb97c335d648d2b4485f56"
BASE_OPERATION_KIND_COUNT=340
BASE_CONTRACT_COUNT=27
BASE_OWNER_CHANGING_KIND_COUNT=122
NEW_CONTRACT_SHA256="5e90f91f2c8a8679bdeb3fc78ab7b0ed71c2f8d3e09de41b8ad9fc18865bddd8"
NEW_ENTRIES=[*ENTRIES_A,*ENTRIES_B]
CONTRACT={"schema":"prime-power-installed-operation-registry-392/v1","base_registry_sha256":BASE_REGISTRY_SHA256,
          "base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,
          "base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,
          "new_entries":NEW_ENTRIES,"honesty_flags":{"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,
          "actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="5f9d0e26a11c58fd45976e1ace87c86a287d00d9d48dbc83dae421a6c2bc9785"

ALLOWED_OWNERS={"same-owner","host-owner-change","factor-child-owner-change"}
ALLOWED_PAYMENTS={"owner-witness-stock","scheduler-dispatch","support-packing","protected-core-growth",
                  "branch-cover-dispatch","history-budget","local-family-restriction","factor-product-dispatch",
                  "strict-child-descent","target-destruction-stock","strict-factor-contraction"}

def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==52,"fifty-two operations required")
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for i,x in enumerate(entries):
        path=f"entry[{i}]"; kind=x.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: unique kind"); kinds.add(kind)
        require(x.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=x.get("source_theorems")
        require(isinstance(sources,list) and sources and all(isinstance(s,str) and s.startswith("CMR") for s in sources),f"{path}: sources")
        owner=x.get("owner_effect"); payment=x.get("payment_class"); continuation=x.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner")
        require(payment in ALLOWED_PAYMENTS,f"{path}: payment")
        require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler")
        if payment=="local-family-restriction": require(owner in {"same-owner","host-owner-change"},f"{path}: restriction owner")
        if payment=="strict-factor-contraction": require(owner=="factor-child-owner-change" and "contract" in continuation,f"{path}: contraction")
        if payment=="strict-child-descent": require(owner=="factor-child-owner-change" and any(word in continuation for word in ("descend","continue","smaller")),f"{path}: descent")
        if payment=="protected-core-growth": require("protect" in continuation or "absorb" in continuation or "capacity" in continuation,f"{path}: growth continuation")
        owner_changes += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    total=BASE_OPERATION_KIND_COUNT+len(kinds); require(total==392,"392 kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),
            "installed_operation_kind_count":total,"bound_contract_count":BASE_CONTRACT_COUNT+1,
            "owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":total-owner_changes,
            "new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),
      lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),
      lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),
      lambda x:x[0].update(continuation=""),lambda x:x[2].update(continuation="route"),
      lambda x:x[8].update(payment_class="strict-factor-contraction"),lambda x:x[23].update(owner_effect="same-owner"),
      lambda x:x[40].update(owner_effect="same-owner"),lambda x:x.pop()]
    rejected=0
    for mutation in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutation(bad)
        try: validate(bad)
        except Registry392Error: rejected+=1
    require(rejected==len(mutations),"corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    report={"contract_digest":contract,"census":census,"installed_transition_kind_bank_392_exhaustive":1,
            "protected_surplus_target_packing_operations_registered":1,"installed_payment_assignment_392_complete":1,
            "all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,
            "all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,
            "global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}
    print(json.dumps(report,sort_keys=True))
if __name__=="__main__": main()
