#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1581."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry782Error(RuntimeError): pass
def require(ok: bool, message: str) -> None:
    if not ok: raise Registry782Error(message)
def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="a56bf0f4f45277106f5489ddc5f490a0ff068771e41a21d8d66e8c0b65120e73"
BASE_OPERATION_KIND_COUNT=714
BASE_CONTRACT_COUNT=35
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="0a1620bf756ec529255be95c072a8435d870762644908a5000418d084948aec4"

RAW=r"""hall-cut-matching-capacity-excess|CMR1510,CMR1511|same-owner|owner-witness-stock|record the exact Hall-cut excess beyond partial-matching capacity
arbitrary-partial-matching-deletion-survival|CMR1512|same-owner|scheduler-dispatch|scheduler preserves a perfect response after deleting any allowed partial matching
nonaxis-line-trace-deletion|CMR1513|same-owner|local-family-equivalence|replace one complete nonaxis response trace by an allowed partial-matching deletion
target-safe-line-clean-response|CMR1514|same-owner|scheduler-dispatch|scheduler selects a response avoiding the opposite layer target edge and full line trace
exact-line-local-collateral-elimination|CMR1515|same-owner|spectral-certificate|certificate-bind the complete line-local collateral row to zero
loaded-owner-line-clean-dispatch|CMR1516|same-owner|scheduler-dispatch|scheduler removes one loaded owner and all allowed response partners on its line
same-line-self-loop-removal-certificate|CMR1517|same-owner|spectral-certificate|certificate-remove the mandatory same-owner same-line self-loop from the recurrent quotient
fixed-central-pair-trace-stock|CMR1518|same-owner|history-budget|bound fixed-central pair and trace signature stocks inside one envelope epoch
repeated-token-persistent-edge-threshold|CMR1519|same-owner|history-budget|bound heavy token episodes or record one persistent labelled edge
return-or-long-absence-run|CMR1520|same-owner|history-budget|route persistent-edge recurrence to exact return payment or one long absence run
persistent-edge-absorption-pair-trace-dispatch|CMR1521|same-owner|scheduler-dispatch|scheduler absorbs the persistent edge or dispatches to pair or trace majority
persistent-paid-pair-selector-row|CMR1522|same-owner|owner-witness-stock|record one jointly persistent paid-pair selector and its deterministic surcharge
persistent-trace-incidence-row|CMR1523|same-owner|owner-witness-stock|record one fixed trace-line or row-column incidence signature
repeated-token-master-dispatch|CMR1524|same-owner|scheduler-dispatch|scheduler dispatches heavy token recurrence to stock return absorption selector or trace
atomic-recurrent-token-quotient|CMR1525|same-owner|local-family-equivalence|replace broad repeated-token recurrence by return selector and trace atomic rows
forbidden-board-inclusion-exclusion-count|CMR1526|same-owner|finite-base-dispatch|bind forbidden-board perfect-matching counts by exact rook inclusion-exclusion
degree-two-rook-component-factorization|CMR1527|same-owner|local-family-equivalence|replace the opposite-plus-trace board by independent path and even-cycle components
path-cycle-rook-polynomial-recurrence|CMR1528|same-owner|finite-base-dispatch|bind every path and even-cycle component to its exact rook polynomial recurrence
target-edge-rook-deletion-contraction|CMR1529|same-owner|local-family-equivalence|replace the target-augmented board by one exact deletion-contraction identity
exact-line-clean-response-count|CMR1530|same-owner|finite-base-dispatch|bind every line-clean response family to one positive exact rook count
exact-line-clean-prescription-probability|CMR1531|same-owner|spectral-certificate|certificate-bind each rank-at-most-three prescription to an exact rook completion ratio
finite-line-clean-rook-signature|CMR1532|same-owner|owner-witness-stock|record the finite path-cycle target-survival signature of one prescription
exact-off-line-collateral-row|CMR1533|same-owner|spectral-certificate|certificate-bind off-line collateral to an exact rational rook-signature dot product
two-matching-width-rectangle-bound|CMR1534|same-owner|owner-witness-stock|record the forbidden rectangle bound from two matching widths and one target edge
line-clean-capacitated-hall-certificate|CMR1535|same-owner|spectral-certificate|certificate-bind every line-clean cut to the d-minus-three factor demand
spanning-line-clean-regular-core|CMR1536|same-owner|finite-base-dispatch|bind every line-clean host to a spanning d-minus-three regular core
uniform-line-clean-permanent-denominator|CMR1537|same-owner|spectral-certificate|certificate-bind every line-clean response count to the uniform permanent denominator
uniform-line-clean-prescription-bound|CMR1538|same-owner|spectral-certificate|certificate-dominate rank-one through rank-three line-clean prescriptions uniformly
uniform-off-line-collateral-envelope|CMR1539|same-owner|spectral-certificate|certificate-dominate the exact off-line rook row by the uniform rank envelope
restricted-host-line-clean-improvement|CMR1540|same-owner|scheduler-dispatch|scheduler selects a feasible strict line-clean response under the explicit host penalty
uniform-line-clean-coefficient-endpoint|CMR1541|same-owner|finite-base-dispatch|record the d-over-d-minus-three coefficient as the universal line-clean fallback
target-disjoint-trace-classification|CMR1542|same-owner|local-family-equivalence|replace target compatibility by the exact endpoint-disjoint trace condition
derangement-extension-completion|CMR1543|same-owner|scheduler-dispatch|scheduler extends a target-disjoint trace except for the singleton opposite-edge remainder
exact-strong-factor-dichotomy|CMR1544|same-owner|finite-base-dispatch|record the exact d-minus-two versus d-minus-three regular-factor class
sharpened-line-clean-permanent|CMR1545|same-owner|spectral-certificate|certificate-bind each factor class to its sharpened permanent denominator
sharpened-line-clean-probability|CMR1546|same-owner|spectral-certificate|certificate-dominate prescription probabilities by the exact binary factor coefficient
binary-line-clean-collateral-certificate|CMR1547|same-owner|spectral-certificate|certificate-bind strong or weak line-clean collateral and restricted-host penalties
geometric-strong-trace-classification|CMR1548|same-owner|owner-witness-stock|record geometric trace sizes that force the strong factor class
binary-factor-signature-row|CMR1549|same-owner|local-family-equivalence|replace one line-clean row by its exact strong or weak factor signature
singleton-deficient-cut-capacity|CMR1550|same-owner|owner-witness-stock|record the unique deficient cut and optimal singleton capacity upper bound
singleton-capacitated-hall-certificate|CMR1551|same-owner|spectral-certificate|certificate-bind every singleton-host cut to the optimal fractional factor demand
singleton-fractional-factor-flow|CMR1552|same-owner|finite-base-dispatch|bind the singleton host to an exact denominator-bounded fractional factor flow
singleton-permanent-denominator|CMR1553|same-owner|spectral-certificate|certificate-bind the singleton response count to its intermediate permanent denominator
singleton-prescription-collateral-bound|CMR1554|same-owner|spectral-certificate|certificate-dominate singleton prescription and off-line collateral rows
singleton-restricted-host-improvement|CMR1555|same-owner|scheduler-dispatch|scheduler selects a feasible strict singleton line-clean response
ternary-line-clean-coefficient-classification|CMR1556,CMR1557|same-owner|local-family-equivalence|replace every line-clean row by strong singleton or endpoint-overlap coefficient class
optimal-paid-pair-selector-threshold|CMR1558|same-owner|spectral-certificate|certificate-bind the least integer threshold forcing subunit selector execution
candidate-free-bounded-restoration|CMR1559|same-owner|scheduler-dispatch|scheduler executes a subunit selector with zero candidate offspring and bounded restoration
first-restoration-label-resource|CMR1560|same-owner|history-budget|bound first restoration labels by one finite monotone physical-edge stock
subunit-selector-return-row|CMR1561|same-owner|spectral-certificate|certificate-bind the recurrent selector row to repeated return only
return-selector-two-row-spectral|CMR1562|same-owner|spectral-certificate|certificate-reduce the return-selector block to alpha plus beta times T below one
return-selector-integer-certificate|CMR1563|same-owner|spectral-certificate|certificate-clear the two-row return-selector inequality to strict integers
uniform-gap-selector-cap|CMR1564,CMR1565|same-owner|spectral-certificate|certificate-bind every uniformly subunit selector class to one explicit return cap
trace-centre-stock|CMR1566|same-owner|history-budget|bound rooted trace centres by the finite side-squared envelope stock
trace-centre-batching|CMR1567|same-owner|history-budget|route excess trace recurrence to one fixed rooted centre
rooted-trace-line-identification|CMR1568|same-owner|owner-witness-stock|record the unique nonaxis real line determined by the rooted centre and witness
root-target-trace-disjointness|CMR1569|same-owner|local-family-equivalence|replace rooted trace execution by a target-disjoint complete line deletion
rooted-trace-coefficient-classification|CMR1570|same-owner|finite-base-dispatch|record each rooted trace as strong or singleton and never endpoint-overlap
rooted-trace-execution-row|CMR1571|same-owner|spectral-certificate|certificate-bind rooted trace execution to its exact line-clean coefficient row
master-trace-dispatch|CMR1572,CMR1573|same-owner|scheduler-dispatch|scheduler dispatches trace recurrence to finite centre stock or one exact rooted line-clean row
source-target-exchange-bijection|CMR1574|same-owner|local-family-equivalence|replace leaving and entering matching edges by exact source and target exchange bijections
alternating-cycle-exchange-signature|CMR1575|same-owner|owner-witness-stock|record the alternating-cycle length of each returned-edge exchange pair
recreated-credit-entering-owner|CMR1576|same-owner|owner-witness-stock|record the unique absolute last-entering owner of every recreated credit
returned-predecessor-transport|CMR1577|same-owner|local-family-equivalence|transport each recreated credit from its entering owner to the same-source returned predecessor
exact-classwise-return-kernel|CMR1578|same-owner|spectral-certificate|certificate-bind every recreated credit class to the exact returned-edge kernel identity
local-owner-bound-return-kernel|CMR1579|same-owner|spectral-certificate|certificate-dominate returned-edge kernel entries by paired entering-owner bounds
coarse-return-upper-quotient|CMR1580|same-owner|spectral-certificate|certificate-bind exact exchange kernels to finite host-uniform rational upper quotients
return-selector-coupling|CMR1581|same-owner|spectral-certificate|certificate-couple the return quotient to the selector cap through one strict two-row inequality"""

def parse(line: str) -> dict[str, Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={
    "schema":"prime-power-installed-operation-registry-782/v1",
    "base_registry_sha256":BASE_REGISTRY_SHA256,
    "base_operation_kind_count":BASE_OPERATION_KIND_COUNT,
    "base_contract_count":BASE_CONTRACT_COUNT,
    "base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,
    "new_contract_sha256":NEW_CONTRACT_SHA256,
    "new_entries":NEW_ENTRIES,
    "scope":"installed line-clean repeated-token restoration trace and return-kernel operations through CMR1581",
    "honesty_flags":{
        "line_clean_recurrent_rows_subcritical":0,
        "return_selector_block_subcritical":0,
        "critical_selector_candidate_regime_closed":0,
        "trace_without_root_target_execution_closed":0,
        "same_owner_diagonal_blocks_subcritical":0,
        "global_target_collateral_inequality_proved":0,
        "global_transition_kind_bank_exhaustive":0,
        "global_termination_proved":0,
        "actual_global_parent_rule_complete":0,
        "all_n_proved_by_checker":0,
    },
}
EXPECTED_CONTRACT_DIGEST="b15c91825d0859a979f3953139554c2e2c81a1f68ea31d0b7d35a57437f0b946"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"owner-witness-stock","history-budget","spectral-certificate","finite-base-dispatch","local-family-equivalence","scheduler-dispatch"}

def validate(entries: list[dict[str, Any]]) -> dict[str, Any]:
    require(len(entries)==68,"sixty-eight operations required")
    kinds=set(); owners=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for index,item in enumerate(entries):
        path=f"entry[{index}]"; kind=item.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: operation kind"); kinds.add(kind)
        require(item.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=item.get("source_theorems")
        require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: sources")
        owner=item.get("owner_effect"); payment=item.get("payment_class"); continuation=item.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner"); require(payment in ALLOWED_PAYMENTS,f"{path}: payment")
        require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler")
        if payment=="spectral-certificate": require("certificate" in continuation or "bind" in continuation,f"{path}: certificate")
        if payment=="finite-base-dispatch": require("record" in continuation or "bind" in continuation,f"{path}: finite base")
        if payment=="owner-witness-stock": require("record" in continuation,f"{path}: witness stock")
        if payment=="history-budget": require("bound" in continuation or "route" in continuation or "record" in continuation,f"{path}: history")
        owners += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==782,"782 installed kinds required")
    require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":714,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":782,"bound_contract_count":36,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":782-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit() -> int:
    mutations=[
        lambda value:value.append(copy.deepcopy(value[0])),
        lambda value:value[0].update(operation_kind=value[1]["operation_kind"]),
        lambda value:value[0].update(contract_sha256="0"*64),
        lambda value:value[0].update(source_theorems=[]),
        lambda value:value[0].update(owner_effect="anonymous"),
        lambda value:value[0].update(payment_class="free"),
        lambda value:value[0].update(continuation=""),
        lambda value:value[1].update(continuation="select a response"),
        lambda value:value[4].update(continuation="estimate a row"),
        lambda value:value[15].update(continuation="compute"),
        lambda value:value[0].update(continuation="witness"),
        lambda value:value[7].update(continuation="episode"),
        lambda value:value[0].update(owner_effect="factor-child-owner-change"),
        lambda value:value.pop(),
        lambda value:value.clear(),
    ]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry782Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted")
    return rejected

def main() -> None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_782_exhaustive":1,"line_clean_return_core_operations_registered":1,"installed_payment_assignment_782_complete":1,"line_clean_recurrent_rows_subcritical":0,"return_selector_block_subcritical":0,"critical_selector_candidate_regime_closed":0,"trace_without_root_target_execution_closed":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_restoration_operations_proved":0,"all_returned_edge_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()