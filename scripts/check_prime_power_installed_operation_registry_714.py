#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1509."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
class Registry714Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise Registry714Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
BASE_REGISTRY_SHA256="1152af341932a040dc60c93baf4a8712964486f7d3a39fd4d4d69ec5a1162321"
BASE_OPERATION_KIND_COUNT=656
BASE_CONTRACT_COUNT=34
BASE_OWNER_CHANGING_KIND_COUNT=162
NEW_CONTRACT_SHA256="e1a59036d2e0bdfacab901cb75f44aaf01f3a03c3f8c2e44f1f4466326d717fc"
RAW = r"""eligible-response-partner-filter|CMR1454|same-owner|local-family-equivalence|replace all response partners by the exact old-or-later entering eligibility filter
eligible-owner-capacity-envelope|CMR1455|same-owner|spectral-certificate|certificate-dominate conditional owner load by the eligibility-filtered capacity envelope
owner-pair-prime-power-signature|CMR1456|same-owner|owner-witness-stock|record partner type separation depth projective direction and primitive-height band
owner-signature-class-envelope|CMR1457|same-owner|spectral-certificate|certificate-bind eligible owner capacity to finite signature-class populations
heavy-owner-signature-concentration|CMR1458|same-owner|owner-witness-stock|record one quantitatively heavy owner signature when the eligible envelope is large
simultaneous-owner-signature-realization|CMR1459|same-owner|scheduler-dispatch|scheduler selects a response realizing the ceiling of one signature expectation
projective-direction-stock|CMR1460|same-owner|owner-witness-stock|record the finite primitive-direction stock inside one projective height band
loaded-owner-line-concentration|CMR1461|same-owner|scheduler-dispatch|scheduler routes a failed owner certificate to one simultaneous loaded real-line family
fractional-signature-incidence-accounting|CMR1462|same-owner|local-family-equivalence|replace packed candidate mass by exactly twice its nonowner signature incidence mass
fractional-heavy-signature|CMR1463|same-owner|owner-witness-stock|record one signature carrying its pigeonhole share of fractional packed mass
positive-minimum-packed-signature|CMR1464|same-owner|spectral-certificate|certificate-bind positive-minimum packing mass to one quantitative signature lower bound
packed-owner-pair-unit-cap|CMR1465|same-owner|protected-reserve-payment|pay packed signature mass by unit ordered-pair and two-unit owner capacities
response-partner-edge-unit-cap|CMR1466|same-owner|protected-reserve-payment|pay response-partner signature mass by one unit on each residual partner edge
primitive-direction-packed-subclass|CMR1467|same-owner|owner-witness-stock|record one primitive direction carrying a quantitative packed subclass
exact-displacement-packed-subclass|CMR1468|same-owner|owner-witness-stock|record one signed exact displacement carrying a quantitative translate bank
packed-signature-endpoint|CMR1469|same-owner|spectral-certificate|certificate-bind every subthreshold obstruction to a dispersed exact-displacement bank
endpoint-prefix-carry-channel|CMR1470|same-owner|local-family-equivalence|replace one exact displacement by its common prefix cell and fixed next-digit offset
heavy-full-prefix-cell|CMR1471|same-owner|owner-witness-stock|record one full prefix cell carrying its weighted share of displacement mass
internal-crossing-copy-split|CMR1472|same-owner|scheduler-dispatch|scheduler chooses the heavier internal or crossing copy class
common-earlier-exit-depth|CMR1473|same-owner|history-budget|route crossing mass to one strictly earlier exit depth
internal-strict-envelope-scaling|CMR1474|factor-child-owner-change|strict-child-descent|continue internal displacement mass in a strictly smaller prime-power envelope
quantitative-carry-routing-splice|CMR1475|same-owner|spectral-certificate|certificate-bind exact-displacement mass to internal crossing or depth-zero branch bounds
absolute-prefix-token-stock|CMR1476|same-owner|token-resource-payment|pay full-prefix concentration by one finite absolute token stock
exact-displacement-carry-dispatch|CMR1477|same-owner|scheduler-dispatch|scheduler dispatches exact displacement to scaling earlier depth root scale or token reuse
translation-path-forest|CMR1478|same-owner|local-family-equivalence|replace one exact-displacement pair family by a finite translation path forest
alternating-private-pair-extraction|CMR1479|same-owner|protected-reserve-payment|pay at least half the packed mass on endpoint-disjoint translated pairs
private-residual-support-payment|CMR1480|same-owner|protected-reserve-payment|charge every neutralized private pair to one distinct residual response edge
nonroot-private-token-placement|CMR1481|same-owner|token-resource-payment|place every nonroot private pair in one exact full-prefix token cell
heavy-or-dispersed-private-token|CMR1482|same-owner|scheduler-dispatch|scheduler chooses one heavy private token or many token-disjoint witnesses
sqrt-private-token-dichotomy|CMR1483|same-owner|token-resource-payment|pay a private bank by square-root heavy-token or dispersed-token stock
routed-private-pair-payment|CMR1484|same-owner|protected-reserve-payment|bind every carry-routing branch to a quantitative endpoint-disjoint private pair bank
private-path-payment-endpoint|CMR1485|same-owner|spectral-certificate|certificate-combine carry routing and private residual support without anonymous mass
current-mask-private-reserve|CMR1486|same-owner|protected-reserve-payment|pay private mass by the existing residual mask or fresh unhit support
routed-reserve-payment|CMR1487|same-owner|protected-reserve-payment|bind every routed branch to an existing-mask or unhit-private reserve lower bound
finite-monotone-residual-edge-stock|CMR1488|same-owner|history-budget|bound fresh private-edge neutralizations by the finite monotone response-host stock
fresh-or-repeated-absolute-token|CMR1489|same-owner|token-resource-payment|pay occupied token mass by prior token stock or strictly fresh token uses
heavy-repeated-or-fresh-token|CMR1490|same-owner|scheduler-dispatch|scheduler routes a private bank to a heavy repeated token or fresh dispersed tokens
refined-transfer-state|CMR1491|same-owner|local-family-equivalence|refine owner state by envelope depth used tokens and residual mask
strict-transfer-resource-dag|CMR1491|same-owner|history-budget|order scaling depth handoff fresh tokens and fresh edges in one finite acyclic graph
transfer-resource-block-upper-triangular|CMR1492|same-owner|spectral-certificate|certificate-bind strict transfers and resource uses above recurrent core blocks
rational-transfer-certificate-gluing|CMR1492|same-owner|spectral-certificate|certificate-glue finite transfer collateral by rational backward scaling
recurrent-core-classification|CMR1493|same-owner|finite-base-dispatch|record root channels repeated tokens reused edges loaded owners and thin blocks as recurrent cores
root-residue-partner-carry|CMR1494|same-owner|local-family-equivalence|replace depth-zero displacement by one distinct partner residue and exact quotient carry
heavy-root-channel|CMR1495|same-owner|owner-witness-stock|record one root residue channel carrying its weighted share without parity loss
root-channel-private-support|CMR1496|same-owner|protected-reserve-payment|pay one root channel by endpoint-disjoint residual support and mask alternatives
root-channel-quotient-normalization|CMR1497|same-owner|local-family-equivalence|normalize one root channel injectively to quotient coordinates and exact carry
root-channel-low-rank-coupling|CMR1498|same-owner|owner-witness-stock|record anchored or cross-factor low-rank coupling patterns in one root channel
root-child-factor-normalization|CMR1499|factor-child-owner-change|strict-child-descent|continue a root channel through strict source-child normalization or later structural exit
prime-field-root-terminal|CMR1500|same-owner|finite-base-dispatch|dispatch prime-field root channels to side-one contraction fixed interface or low-rank terminal trigger
quantitative-root-channel-dispatch|CMR1501|same-owner|scheduler-dispatch|scheduler selects one heavy root child channel and its canonical child response
exact-displacement-owner-unit-cap|CMR1502|same-owner|protected-reserve-payment|pay exact-displacement mass by at most one unit on each canonical owner
loaded-owner-exclusion|CMR1503|same-owner|scheduler-dispatch|scheduler separates loaded owners from the remaining packed displacement mass
unloaded-private-pair-extraction|CMR1504|same-owner|protected-reserve-payment|pay unloaded packed mass by an owner-disjoint endpoint-private pair bank
unloaded-private-token-alternative|CMR1505|same-owner|token-resource-payment|pay unloaded nonroot mass by heavy or dispersed owner-disjoint private tokens
unloaded-root-channel|CMR1506|same-owner|scheduler-dispatch|scheduler selects an owner-disjoint heavy root channel when loaded owners are insufficient
owner-disjoint-payment-bookkeeping|CMR1507|same-owner|local-family-equivalence|add loaded-owner and private-pair payments on disjoint canonical owner support
routed-packed-loaded-alternative|CMR1508|same-owner|spectral-certificate|certificate-bind every carry branch to many loaded owners or an unloaded private payment
packed-loaded-endpoint|CMR1509|same-owner|spectral-certificate|certificate-close overlap while preserving the unresolved numerical core inequalities"""
def parse(line:str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}
NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-714/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed signature displacement carry resource root-channel and packed-loaded operations through CMR1509","honesty_flags":{"uniform_signature_payment_certificate_proved":0,"recurrent_root_channel_core_subcritical":0,"repeated_token_reused_edge_core_subcritical":0,"loaded_owner_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="675ab24a159db1d009d6c74369a70913573351c32aa9d55494e8eac3d8837895"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"owner-witness-stock","history-budget","spectral-certificate","finite-base-dispatch","local-family-equivalence","scheduler-dispatch","strict-child-descent","protected-reserve-payment","token-resource-payment"}
def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==58,"fifty-eight operations required")
    kinds=set(); owners=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for index,item in enumerate(entries):
        path=f"entry[{index}]"; kind=item.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: kind"); kinds.add(kind)
        require(item.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=item.get("source_theorems"); require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: sources")
        owner=item.get("owner_effect"); payment=item.get("payment_class"); continuation=item.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner"); require(payment in ALLOWED_PAYMENTS,f"{path}: payment"); require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler")
        if payment=="strict-child-descent": require(owner=="factor-child-owner-change" and "continue" in continuation,f"{path}: child")
        if payment=="spectral-certificate": require("certificate" in continuation or "bind" in continuation,f"{path}: certificate")
        if payment=="finite-base-dispatch": require("record" in continuation or "dispatch" in continuation,f"{path}: base")
        if payment=="protected-reserve-payment": require("pay" in continuation or "charge" in continuation or "bind" in continuation,f"{path}: reserve")
        if payment=="token-resource-payment": require("pay" in continuation or "place" in continuation,f"{path}: token")
        owners+=owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==714,"714 kinds required"); require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":714,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":714-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}
def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[5].update(continuation="select"),lambda x:x[20].update(owner_effect="same-owner"),lambda x:x[47].update(owner_effect="same-owner"),lambda x:x[12].update(payment_class="strict-child-descent"),lambda x:x[28].update(payment_class="spectral-certificate"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry714Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected
def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_714_exhaustive":1,"signature_carry_resource_operations_registered":1,"installed_payment_assignment_714_complete":1,"uniform_signature_payment_certificate_proved":0,"recurrent_root_channel_core_subcritical":0,"repeated_token_reused_edge_core_subcritical":0,"loaded_owner_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__": main()
