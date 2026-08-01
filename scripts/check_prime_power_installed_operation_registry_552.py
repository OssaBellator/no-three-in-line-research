#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1317."""
from __future__ import annotations
import copy
import hashlib
import json
from typing import Any

class Registry552Error(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise Registry552Error(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

BASE_REGISTRY_SHA256 = "5b2a0a8ec909513c5d3b166767ace7f00724fa90cf5a79f32590b4d984df3f4a"
BASE_OPERATION_KIND_COUNT = 525
BASE_CONTRACT_COUNT = 31
BASE_OWNER_CHANGING_KIND_COUNT = 154
NEW_CONTRACT_SHA256 = "caa854d1cac17e5d4680558a9829b01a5d19b86a811e2baae47170d4839f3114"

def e(kind, sources, owner, payment, continuation):
    return {"operation_kind": kind, "source_theorems": sources, "owner_effect": owner, "payment_class": payment, "continuation": continuation, "contract_sha256": NEW_CONTRACT_SHA256}

NEW_ENTRIES = [
 e("side-three-full-grid-state-classification",["CMR1278","CMR1279"],"same-owner","finite-base-dispatch","dispatch the exact six physical side-three full-grid states by potential and target type"),
 e("side-three-full-grid-clean-target-response",["CMR1280","CMR1281"],"same-owner","scheduler-dispatch","scheduler replaces every dirty full-grid side-three target by its unique clean response"),
 e("side-three-restricted-singleton-wall",["CMR1282"],"factor-child-owner-change","strict-child-descent","continue an unavailable singleton response through its one-edge deficiency wall"),
 e("side-three-zero-offspring-terminal-block",["CMR1283","CMR1284","CMR1285"],"same-owner","spectral-certificate","bind the verified affine full-grid terminal block to the exact zero offspring matrix"),
 e("side-four-full-grid-state-stock",["CMR1286"],"same-owner","finite-base-dispatch","dispatch the complete side-four full-grid state and potential census"),
 e("side-four-full-grid-target-response-search",["CMR1287","CMR1288"],"same-owner","scheduler-dispatch","scheduler selects a strictly lower full-grid response for every dirty side-four state"),
 e("side-four-deterministic-potential-descent",["CMR1289","CMR1291","CMR1292"],"same-owner","history-budget","bound the canonical full-grid response path by the integer potential and live-credit stock"),
 e("side-four-lowering-host-expansion",["CMR1290","CMR1293"],"host-owner-change","local-family-restriction","restrict a full-coordinate lowering expansion to improvement or added minimum-core contraction"),
 e("side-five-full-grid-state-stock",["CMR1294"],"same-owner","finite-base-dispatch","dispatch the complete side-five full-grid state and potential census"),
 e("side-five-degree-three-response-bank-stock",["CMR1295"],"same-owner","owner-witness-stock","record the exact twelve-or-thirteen response matching stock of each side-five bank"),
 e("side-five-extension-target-table",["CMR1296"],"same-owner","finite-base-dispatch","bind every fixed-opposite target cell to its complete side-five response minimum"),
 e("side-five-full-grid-strict-response",["CMR1297","CMR1298"],"same-owner","scheduler-dispatch","scheduler selects a strictly lower full-grid response for every dirty side-five state"),
 e("side-five-lowering-host-expansion",["CMR1299","CMR1301"],"host-owner-change","local-family-restriction","restrict a full-coordinate side-five lowering expansion to improvement or contraction"),
 e("side-five-finite-descent-budget",["CMR1300"],"same-owner","history-budget","bound accepted potential decreases and labelled-edge contractions on the side-five root owner"),
 e("regular-edge-containing-one-factor",["CMR1302"],"same-owner","local-family-equivalence","extend every edge of a regular bipartite response complement to one perfect matching"),
 e("extension-free-response-union",["CMR1303"],"same-owner","local-family-equivalence","replace the union over forbidden extensions by all responses avoiding the opposite matching and target cell"),
 e("canonical-post-response-extension-recovery",["CMR1304"],"same-owner","scheduler-dispatch","scheduler recovers the first compatible forbidden extension after selecting an extension-free response"),
 e("extension-free-target-minimum",["CMR1305","CMR1306"],"same-owner","finite-base-dispatch","optimize directly over target-omitting responses while preserving exact target destruction"),
 e("extension-free-restricted-lowering-expansion",["CMR1307"],"host-owner-change","local-family-restriction","restrict a missing extension-free minimizer through a lowering expansion or contraction"),
 e("extension-free-versus-fixed-bank-scope",["CMR1308","CMR1309"],"same-owner","scheduler-dispatch","scheduler uses the response union for ambient optimization and one fixed bank for blockage walls"),
 e("side-six-full-grid-state-stock",["CMR1310"],"same-owner","finite-base-dispatch","dispatch the complete side-six ordered physical and potential census"),
 e("side-six-extension-free-response-table",["CMR1311"],"same-owner","finite-base-dispatch","bind all fixed-opposite nonopposite cells to side-six extension-free response minima"),
 e("side-six-immediate-response-trichotomy",["CMR1312"],"same-owner","scheduler-dispatch","scheduler separates immediate strict improvements from equal-potential one-layer traps"),
 e("side-six-equal-response-escape-graph",["CMR1313"],"same-owner","history-budget","route equal-potential traps to exits within two steps when the reverse escape graph permits"),
 e("side-six-closed-one-layer-trap-core",["CMR1314"],"same-owner","owner-witness-stock","record the exact feeder and directed two-cycle structure of the closed one-layer trap class"),
 e("side-six-clean-joint-escape",["CMR1315"],"same-owner","scheduler-dispatch","scheduler replaces every closed one-layer trap by the recorded clean two-layer response"),
 e("side-six-clean-lowering-expansion",["CMR1316","CMR1317"],"host-owner-change","local-family-restriction","restrict the clean joint response through a lowering expansion or added-core contraction"),
]

CONTRACT = {"schema":"prime-power-installed-operation-registry-552/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"full standard grids and verified translate/common-scale affine copies","honesty_flags":{"scattered_residual_finite_grid_policy_proved":0,"one_layer_fixed_target_policy_globally_sufficient":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST = "77670b377285d73441fd7c19cdd83a115ce658ef263098f45c73a633f352d232"
ALLOWED_OWNERS={"same-owner","host-owner-change","factor-child-owner-change"}
ALLOWED_PAYMENTS={"finite-base-dispatch","scheduler-dispatch","strict-child-descent","spectral-certificate","history-budget","local-family-restriction","owner-witness-stock","local-family-equivalence"}

def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries)==27,"twenty-seven operations required")
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for index,entry in enumerate(entries):
        path=f"entry[{index}]"; kind=entry.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: unique kind"); kinds.add(kind)
        require(entry.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=entry.get("source_theorems"); require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: source ancestry")
        owner=entry.get("owner_effect"); payment=entry.get("payment_class"); continuation=entry.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner"); require(payment in ALLOWED_PAYMENTS,f"{path}: payment"); require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler continuation")
        if payment=="local-family-restriction": require(owner=="host-owner-change" and "restrict" in continuation,f"{path}: host restriction")
        if payment=="strict-child-descent": require(owner=="factor-child-owner-change" and "continue" in continuation,f"{path}: child descent")
        if payment=="finite-base-dispatch": require("dispatch" in continuation or "bind" in continuation or "optimize" in continuation,f"{path}: finite base")
        owner_changes += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==552,"552 kinds required"); require(owner_changes==159,"159 owner-changing kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":552,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owner_changes,"same_owner_operation_kinds":552-owner_changes,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit() -> int:
    mutations=[lambda entries:entries.append(copy.deepcopy(entries[0])),lambda entries:entries[0].update(operation_kind=entries[1]["operation_kind"]),lambda entries:entries[0].update(contract_sha256="0"*64),lambda entries:entries[0].update(source_theorems=[]),lambda entries:entries[0].update(owner_effect="anonymous"),lambda entries:entries[0].update(payment_class="free"),lambda entries:entries[0].update(continuation=""),lambda entries:entries[1].update(continuation="replace"),lambda entries:entries[2].update(owner_effect="same-owner"),lambda entries:entries[7].update(owner_effect="same-owner"),lambda entries:entries[18].update(owner_effect="same-owner"),lambda entries:entries.pop()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry552Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main() -> None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_552_exhaustive":1,"finite_grid_response_operations_registered":1,"installed_payment_assignment_552_complete":1,"scattered_residual_finite_grid_policy_proved":0,"one_layer_fixed_target_policy_globally_sufficient":0,"global_target_collateral_inequality_proved":0,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
