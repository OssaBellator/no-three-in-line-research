#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1629."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry830Error(RuntimeError): pass

def require(ok: bool, message: str) -> None:
    if not ok: raise Registry830Error(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="8da81442b93b56c48054370aa1f36f47e9ce5acbe9e5b99f01c5e6a8fd62f91f"
BASE_OPERATION_KIND_COUNT=782
BASE_CONTRACT_COUNT=36
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="195b9f8ce43391860ea28b7b0d882250fc0f13222b16e67f432c786cc2d80285"

RAW=r"""response-edge-doubly-stochastic-marginal|CMR1582|same-owner|local-family-equivalence|replace a rational response law by its exact doubly stochastic edge marginal
exact-return-selector-owner-expansion|CMR1583|same-owner|local-family-equivalence|replace return and selector row sums by exact conditional entering-owner expansions
scalarized-return-selector-score|CMR1584|same-owner|local-family-equivalence|replace two coupled rows by the single edge score g_ret plus T times g_sel
shared-return-selector-assignment-primal-dual|CMR1585|same-owner|spectral-certificate|certificate-dominate the scalarized row by one shared assignment primal and dual
direct-return-selector-dual-certificate|CMR1586|same-owner|spectral-certificate|certificate-prove the coupled two-row block strict from one dual objective below one
integer-return-selector-assignment-certificate|CMR1587|same-owner|spectral-certificate|certificate-clear the shared assignment dual to one strict integer system
coarse-exchange-class-assignment-quotient|CMR1588|same-owner|spectral-certificate|certificate-bind finite exchange classes to an honest assignment upper quotient
return-selector-scalarization-endpoint|CMR1589|same-owner|spectral-certificate|certificate-reduce the return-selector frontier to one combined owner-weighted assignment score
common-line-clean-weighted-count|CMR1590|same-owner|local-family-equivalence|replace rank and unavailable-edge terms by one exact integer weighted count
generic-line-clean-integer-inequality|CMR1591|same-owner|spectral-certificate|certificate-clear any rational factor coefficient to one strict integer inequality
ternary-line-clean-strict-tests|CMR1592|same-owner|spectral-certificate|certificate-bind strong singleton and overlap rows to their exact integer tests
maximal-line-clean-candidate-budget|CMR1593|same-owner|spectral-certificate|certificate-replace strict line-clean improvement by one maximal integer budget
rank-pure-line-clean-automatic-range|CMR1594|same-owner|finite-base-dispatch|record the exact maximal rank-pure automatic improvement ranges
unavailable-edge-line-clean-budget|CMR1595|same-owner|spectral-certificate|certificate-bind restricted-host unavailability to the remaining integer credit budget
line-clean-integer-slack-certificate|CMR1596|same-owner|spectral-certificate|certificate-represent line-clean improvement by one positive additive integer slack
line-clean-integer-budget-endpoint|CMR1597|same-owner|spectral-certificate|certificate-bind every ternary line-clean row to its independently checkable budget
exact-selector-class-decomposition|CMR1598|same-owner|local-family-equivalence|replace selector candidate expectation by exact residual-rank and profile class contributions
selector-gap-dichotomy|CMR1599|same-owner|scheduler-dispatch|scheduler dispatches each selector to a bounded return splice or concentrated candidate class
candidate-count-localization|CMR1600|same-owner|owner-witness-stock|record a quantitative candidate-count lower bound in one exact selector class
uniform-profile-candidate-lower-bound|CMR1601|same-owner|owner-witness-stock|record the host-uniform candidate stock forced by one concentrated profile class
integer-critical-selector-localization|CMR1602|same-owner|spectral-certificate|certificate-clear critical selector concentration to exact integer class mass
refined-geometric-selector-concentration|CMR1603|same-owner|owner-witness-stock|record one owner-height-prefix-carry subclass carrying quantitative selector mass
selector-recurrent-normal-form|CMR1604|same-owner|local-family-equivalence|replace diffuse selector recurrence by return-splice or concentrated critical classes
critical-selector-endpoint|CMR1605|same-owner|finite-base-dispatch|record the finite quantitative critical-selector class frontier
prime-field-root-singleton-channel|CMR1606|same-owner|local-family-equivalence|replace a prime-field root channel by at most one ordered translated pair
prime-field-root-pair-stock|CMR1607|same-owner|history-budget|bound the complete prime-field root-pair inventory
prime-field-support-size|CMR1608|same-owner|owner-witness-stock|record the exact one-edge or two-edge support of one prime-field root pair
first-support-label-resource|CMR1609|same-owner|history-budget|bound first prime-field support labels by one finite monotone resource stock
prime-field-terminal-signature-stock|CMR1610|same-owner|history-budget|bound exact pair partner-type and local-rank terminal signatures
prime-field-signature-batching|CMR1611|same-owner|history-budget|route excess prime-field recurrence to one exact terminal signature
prime-field-recurrent-signature-splice|CMR1612|same-owner|scheduler-dispatch|scheduler dispatches one recurring prime-field signature to resource return contraction interface or exit
prime-field-root-endpoint|CMR1613|same-owner|local-family-equivalence|replace broad prime-field root recurrence by reused support return or one exact interface atom
partial-matching-prescription-stock|CMR1614|same-owner|finite-base-dispatch|record the exact rank-one and rank-two compatible prescription stock
first-fixed-interface-signature-resource|CMR1615|same-owner|history-budget|bound first exact fixed-interface signatures by a finite monotone state stock
fixed-interface-signature-batching|CMR1616|same-owner|history-budget|route excess interface recurrence to one exact repeated prescription signature
exact-fixed-interface-rook-probability|CMR1617|same-owner|spectral-certificate|certificate-bind one repeated interface prescription to its exact rook completion ratio
exact-fixed-interface-offspring-row|CMR1618|same-owner|spectral-certificate|certificate-bind every exact interface signature to a finite rational offspring row
finite-thin-board-stock|CMR1619|same-owner|finite-base-dispatch|record the finite ambient stock of thin normalized board and prescription rows
thin-side-certificate-compiler|CMR1620|same-owner|finite-base-dispatch|bind every fixed thin cap to a finite rational row compiler and integer certificate search
fixed-interface-thin-endpoint|CMR1621|same-owner|finite-base-dispatch|record the exact finite-table endpoint for root interface and thin bases
label-preserving-exact-projection|CMR1622|same-owner|local-family-equivalence|replace interface-label forgetting by exact child aggregation and honest parent-fibre domination
labelled-transfer-scc-dag|CMR1623|same-owner|local-family-equivalence|replace the complete labelled transfer graph by its exact SCC condensation DAG
labelled-spectral-block-reduction|CMR1624|same-owner|spectral-certificate|certificate-reduce the labelled global spectral radius to recurrent SCC blocks
rational-crt-certificate-gluing|CMR1625|same-owner|spectral-certificate|certificate-glue recurrent block vectors by reverse-topological rational scaling
integer-crt-certificate-clearing|CMR1626|same-owner|spectral-certificate|certificate-clear the glued rational CRT vector and slack to strict integers
premature-label-erasure-obstruction|CMR1627|same-owner|finite-base-dispatch|record the artificial self-loop and cycle obstruction from premature label erasure
labelled-recurrent-block-schema|CMR1628|same-owner|finite-base-dispatch|record the exact return line selector support interface thin and CRT recurrent modules
label-preserving-crt-assembly-endpoint|CMR1629|same-owner|spectral-certificate|certificate-bind all strict transfers and finite interface collateral to labelled recurrent blocks"""

def parse(line: str) -> dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={
    "schema":"prime-power-installed-operation-registry-830/v1",
    "base_registry_sha256":BASE_REGISTRY_SHA256,
    "base_operation_kind_count":BASE_OPERATION_KIND_COUNT,
    "base_contract_count":BASE_CONTRACT_COUNT,
    "base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,
    "new_contract_sha256":NEW_CONTRACT_SHA256,
    "new_entries":NEW_ENTRIES,
    "scope":"installed return-selector scalarization line-clean budgets critical localization root support thin-table and labelled CRT operations through CMR1629",
    "honesty_flags":{
        "return_selector_assignment_dual_globally_strict":0,
        "line_clean_integer_slacks_globally_positive":0,
        "critical_selector_classes_closed":0,
        "fixed_interface_thin_table_subcritical":0,
        "labelled_crt_recurrent_blocks_subcritical":0,
        "same_owner_diagonal_blocks_subcritical":0,
        "global_target_collateral_inequality_proved":0,
        "global_transition_kind_bank_exhaustive":0,
        "global_termination_proved":0,
        "actual_global_parent_rule_complete":0,
        "all_n_proved_by_checker":0,
    },
}
EXPECTED_CONTRACT_DIGEST="e533e625b1f430ba72eb6c0c3a5821cbe9c0316e0d1284d65becc4f3e00c7e67"
ALLOWED_OWNERS={"same-owner"}
ALLOWED_PAYMENTS={"owner-witness-stock","history-budget","spectral-certificate","finite-base-dispatch","local-family-equivalence","scheduler-dispatch"}

def validate(entries: list[dict[str,Any]]) -> dict[str,Any]:
    require(len(entries)==48,"forty-eight operations required")
    kinds=set(); payments={}
    for index,item in enumerate(entries):
        path=f"entry[{index}]"; kind=item.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: operation kind"); kinds.add(kind)
        require(item.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=item.get("source_theorems")
        require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: sources")
        owner=item.get("owner_effect"); payment=item.get("payment_class"); continuation=item.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner")
        require(payment in ALLOWED_PAYMENTS,f"{path}: payment")
        require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler")
        if payment=="spectral-certificate": require("certificate" in continuation or "bind" in continuation,f"{path}: certificate")
        if payment=="finite-base-dispatch": require("record" in continuation or "bind" in continuation,f"{path}: finite base")
        if payment=="owner-witness-stock": require("record" in continuation,f"{path}: witness stock")
        if payment=="history-budget": require("bound" in continuation or "route" in continuation,f"{path}: history")
        payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==830,"830 installed kinds required")
    return {
        "base_operation_kind_count":BASE_OPERATION_KIND_COUNT,
        "new_operation_kind_count":len(kinds),
        "installed_operation_kind_count":830,
        "bound_contract_count":BASE_CONTRACT_COUNT+1,
        "owner_changing_operation_kinds":BASE_OWNER_CHANGING_KIND_COUNT,
        "same_owner_operation_kinds":830-BASE_OWNER_CHANGING_KIND_COUNT,
        "new_payment_counts":payments,
        "registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries}),
    }

def mutation_audit() -> int:
    mutations=[
        lambda value:value.append(copy.deepcopy(value[0])),
        lambda value:value[0].update(operation_kind=value[1]["operation_kind"]),
        lambda value:value[0].update(contract_sha256="0"*64),
        lambda value:value[0].update(source_theorems=[]),
        lambda value:value[0].update(owner_effect="factor-child-owner-change"),
        lambda value:value[0].update(payment_class="free"),
        lambda value:value[0].update(continuation=""),
        lambda value:value[17].update(continuation="select"),
        lambda value:value[3].update(continuation="estimate"),
        lambda value:value[12].update(continuation="compute"),
        lambda value:value[18].update(continuation="witness"),
        lambda value:value[25].update(continuation="episode"),
        lambda value:value.pop(),
        lambda value:value.clear(),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry830Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted")
    return rejected

def main() -> None:
    contract=digest(CONTRACT)
    require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES))
    census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({
        "contract_digest":contract,
        "census":census,
        "installed_transition_kind_bank_830_exhaustive":1,
        "recurrent_certificate_assembly_operations_registered":1,
        "installed_payment_assignment_830_complete":1,
        "return_selector_assignment_dual_globally_strict":0,
        "line_clean_integer_slacks_globally_positive":0,
        "critical_selector_classes_closed":0,
        "fixed_interface_thin_table_subcritical":0,
        "labelled_crt_recurrent_blocks_subcritical":0,
        "same_owner_diagonal_blocks_subcritical":0,
        "global_target_collateral_inequality_proved":0,
        "all_owner_operations_proved":0,
        "all_scheduler_operations_proved":0,
        "all_restoration_operations_proved":0,
        "all_returned_edge_operations_proved":0,
        "all_envelope_operations_proved":0,
        "all_construction_ancestry_proved":0,
        "global_transition_kind_bank_exhaustive":0,
        "global_termination_proved":0,
        "actual_global_parent_rule_complete":0,
        "all_n_proved_by_checker":0,
    },sort_keys=True))

if __name__=="__main__": main()
