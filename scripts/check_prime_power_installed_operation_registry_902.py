#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1701."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry902Error(RuntimeError): pass
def require(ok: bool, message: str)->None:
    if not ok: raise Registry902Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="ab7be2d96abc4c31d70cbc2c13db579eb417474bdb6944a0d48bea83537cc362"
BASE_OPERATION_KIND_COUNT=830
BASE_CONTRACT_COUNT=37
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="e155ea311c24a9f04e1a603877190d1e60f9928a4607546635a9198344e53ad0"

RAW=r"""return-score-layer-decomposition|CMR1630|same-owner|local-family-equivalence|replace one edge score by its exact nested superlevel layer sum
return-superlevel-matching-bound|CMR1631|same-owner|spectral-certificate|certificate-bind the combined assignment by superlevel matching numbers
return-superlevel-konig-cover|CMR1632|same-owner|owner-witness-stock|record one minimum vertex cover for each score superlevel graph
return-superlevel-strict-certificate|CMR1633|same-owner|spectral-certificate|certificate-prove the coupled return-selector block strict from the weighted cover sum
return-superlevel-integer-certificate|CMR1634|same-owner|spectral-certificate|certificate-clear the superlevel cover inequality to strict integers
two-level-heavy-edge-envelope|CMR1635|same-owner|spectral-certificate|certificate-bind one assignment by baseline score and heavy-edge matching number
geometric-class-superlevel-specialization|CMR1636|same-owner|local-family-equivalence|replace exact edge scores by pointwise geometric class caps
return-superlevel-cover-endpoint|CMR1637|same-owner|finite-base-dispatch|record the full dual superlevel and two-level return certificate forms
permanent-ratio-monotonicity|CMR1638|same-owner|spectral-certificate|certificate-bind all side-dependent ratio minima to the smallest admissible side
strong-overlap-universal-floors|CMR1639|same-owner|spectral-certificate|certificate-bind strong and overlap ratios to universal side-four floors
singleton-universal-floor|CMR1640|same-owner|spectral-certificate|certificate-bind the singleton ratio to its universal side-four floor
universal-line-clean-integer-budgets|CMR1641|same-owner|spectral-certificate|certificate-bind all three line-clean classes to host-uniform integer budgets
universal-rank-pure-ranges|CMR1642|same-owner|finite-base-dispatch|record universal automatic ranges for pure residual ranks
universal-unavailable-edge-reserve|CMR1643|same-owner|spectral-certificate|certificate-bind restricted-host unavailability to the universal residual budget
rooted-trace-universal-specialization|CMR1644|same-owner|local-family-equivalence|replace rooted trace budgets by the strong or singleton universal classes
universal-line-clean-budget-endpoint|CMR1645|same-owner|finite-base-dispatch|record universal budgets rank ranges and unavailable reserves
selector-class-capacity-sum|CMR1646|same-owner|spectral-certificate|certificate-bind selector expectation by the summed integer class capacity
selector-capacity-restoration-cap|CMR1647|same-owner|spectral-certificate|certificate-bind positive selector slack to an exact restoration cap
critical-selector-capacity-exclusion|CMR1648|same-owner|spectral-certificate|certificate-exclude criticality whenever total class capacity is below the denominator
per-prescription-selector-capacity|CMR1649|same-owner|spectral-certificate|certificate-bind one selector class by prescription count times numerator cap
mixed-exact-residual-selector-capacity|CMR1650|same-owner|spectral-certificate|certificate-combine exact class numerators with residual capacities
capacity-gap-return-assignment-coupling|CMR1651|same-owner|spectral-certificate|certificate-couple the restoration cap to one shared return assignment or cover
refined-critical-capacity-threshold|CMR1652|same-owner|owner-witness-stock|record one class meeting the necessary critical capacity threshold
selector-capacity-gap-endpoint|CMR1653|same-owner|finite-base-dispatch|record the exact capacity slack restoration and residual worklist compiler
matching-data-relabeling-invariance|CMR1654|same-owner|local-family-equivalence|replace every relabelled matching board by its exact incidence-isomorphic board
opposite-matching-normalization|CMR1655|same-owner|local-family-equivalence|replace an arbitrary opposite matching by the identity matching
forbidden-target-normalization|CMR1656|same-owner|local-family-equivalence|replace an arbitrary disjoint target by the normalized edge zero-one
fixed-interface-residual-stabilizer|CMR1657|same-owner|owner-witness-stock|record the exact residual symmetric-group stabilizer of the normalized board
fixed-interface-canonical-orbit-code|CMR1658|same-owner|table-enumeration|enumerate canonical labelled state codes under the residual stabilizer
orbit-invariant-response-row|CMR1659|same-owner|local-family-equivalence|replace all labelled states in one orbit by one canonically indexed response row
orbit-table-certificate-lifting|CMR1660|same-owner|certificate-gluing|glue one strict orbit-table vector to all fully labelled states
symmetry-normalized-thin-table-endpoint|CMR1661|same-owner|table-enumeration|enumerate one exact rook row per canonical normalized thin orbit
normalized-thin-host-census|CMR1662|same-owner|table-enumeration|enumerate raw executable hosts and canonical deletion orbits through side five
normalized-thin-denominator-census|CMR1663|same-owner|table-enumeration|enumerate exact perfect-matching denominator distributions through side five
side-two-no-response-dispatch|CMR1664|same-owner|finite-base-dispatch|record side two as a forced structural exit before extension-free response
side-three-forced-prescription-contraction|CMR1665|same-owner|scheduler-dispatch|scheduler dispatches every executable side-three prescription to exact contraction
side-four-thin-rank-one-two-caps|CMR1666|same-owner|table-enumeration|enumerate side-four forced prescriptions and exact nonforced rank-one-two caps
side-five-thin-rank-one-two-caps|CMR1667|same-owner|table-enumeration|enumerate side-five exact nonforced rank-one-two caps
thin-rank-one-two-capacity-row|CMR1668|same-owner|spectral-certificate|certificate-bind fixed-interface class expectation by side-four-five rank caps
normalized-thin-response-endpoint|CMR1669|same-owner|finite-base-dispatch|record the complete normalized matching-level census through side five
threshold-class-union-cover|CMR1670|same-owner|owner-witness-stock|record one explicit union cover for each combined-score threshold
class-supported-return-certificate|CMR1671|same-owner|spectral-certificate|certificate-bind the combined assignment by threshold class-support covers
source-target-star-cover-specialization|CMR1672|same-owner|owner-witness-stock|record high-score source-star and target-star support covers
alternative-class-cover-optimization|CMR1673|same-owner|table-enumeration|enumerate the finite joint choices of alternative class covers
nested-cumulative-cover-weight|CMR1674|same-owner|local-family-equivalence|replace nested cover layers by one maximum weight on each support vertex
class-cover-assignment-dual|CMR1675|same-owner|spectral-certificate|certificate-bind class support weights to a feasible rational assignment dual
class-cover-integer-certificate|CMR1676|same-owner|spectral-certificate|certificate-clear class-supported vertex weights to one strict integer inequality
return-class-support-endpoint|CMR1677|same-owner|finite-base-dispatch|record the geometric class-support compiler for combined return scores
line-clean-weighted-capacity-envelope|CMR1678|same-owner|spectral-certificate|certificate-bind exact weighted line-clean count by class and availability capacities
exact-profile-capacity-certificate|CMR1679|same-owner|spectral-certificate|certificate-bind class capacities to the exact side-dependent line-clean budget
universal-profile-capacity-certificate|CMR1680|same-owner|spectral-certificate|certificate-bind class capacities to the universal line-clean budget
line-clean-overflow-class-localization|CMR1681|same-owner|owner-witness-stock|record one weighted class or availability coordinate forcing budget overflow
overflow-candidate-count-conversion|CMR1682|same-owner|owner-witness-stock|record the exact candidate-count lower bound from weighted rank overflow
unavailable-edge-overflow-conversion|CMR1683|same-owner|owner-witness-stock|record the exact unavailable-edge lower bound from budget overflow
mixed-line-clean-capacity-table|CMR1684|same-owner|spectral-certificate|certificate-combine exact enumerated classes with bounded residual capacities
line-clean-profile-capacity-endpoint|CMR1685|same-owner|finite-base-dispatch|record the exact budget pass or finite overflow-class worklist
ambient-rank-three-prescription-stock|CMR1686|same-owner|owner-witness-stock|record the exact ambient rank-three prescription stock
side-three-rank-three-contraction|CMR1687|same-owner|scheduler-dispatch|scheduler dispatches every side-three rank-three prescription to exact contraction
side-four-thin-rank-three-census|CMR1688|same-owner|table-enumeration|enumerate side-four forced and nonforced rank-three prescription probabilities
side-five-thin-rank-three-census|CMR1689|same-owner|table-enumeration|enumerate side-five rank-three prescription probabilities
complete-thin-rank-cap-table|CMR1690|same-owner|table-enumeration|enumerate the complete nonforced rank-one-two-three cap table through side five
thin-rank-capacity-expectation|CMR1691|same-owner|spectral-certificate|certificate-bind geometric class expectation by all three thin rank caps
thin-rank-integer-numerator-capacity|CMR1692|same-owner|spectral-certificate|certificate-clear thin rank probability caps to exact numerator capacities
normalized-thin-rank-three-endpoint|CMR1693|same-owner|finite-base-dispatch|record the complete matching-level thin census for ranks one through three
auxiliary-nonnegative-resolvent|CMR1694|same-owner|certificate-gluing|glue all finite auxiliary excursions through the nonnegative rational resolvent
auxiliary-effective-core-matrix|CMR1695|same-owner|local-family-equivalence|replace a subcritical full block by its effective retained core matrix
auxiliary-certificate-constructive-lift|CMR1696|same-owner|certificate-gluing|glue a strict effective-core vector back to the full auxiliary block
auxiliary-subcriticality-equivalence|CMR1697|same-owner|spectral-certificate|certificate-bind full-block subcriticality exactly to the effective core
zero-self-auxiliary-elimination|CMR1698|same-owner|local-family-equivalence|replace zero-self auxiliary rows by the exact product excursion term
auxiliary-rational-integer-certificate|CMR1699|same-owner|certificate-gluing|glue rational resolvent and core data into one strict integer certificate
block-diagonal-auxiliary-elimination|CMR1700|same-owner|certificate-gluing|glue independently certified auxiliary modules into the summed effective core
auxiliary-elimination-endpoint|CMR1701|same-owner|finite-base-dispatch|record the exact certified-auxiliary elimination protocol"""

def parse(line: str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={
"schema":"prime-power-installed-operation-registry-902/v1",
"base_registry_sha256":BASE_REGISTRY_SHA256,
"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,
"base_contract_count":BASE_CONTRACT_COUNT,
"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,
"new_contract_sha256":NEW_CONTRACT_SHA256,
"new_entries":NEW_ENTRIES,
"scope":"installed return superlevel budget normalized thin census and auxiliary elimination operations through CMR1701",
"honesty_flags":{"return_superlevel_cover_globally_strict":0,"universal_line_clean_budgets_close_all_classes":0,"selector_capacity_classes_closed":0,"normalized_thin_geometric_rows_subcritical":0,"auxiliary_effective_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="239245dca95e8a3936fd5700248af65f1534f706ac4aceccca7890c850a955ff"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"spectral-certificate","local-family-equivalence","owner-witness-stock","finite-base-dispatch","scheduler-dispatch","table-enumeration","certificate-gluing"}

def validate(entries: list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==72,"seventy-two operations required")
    kinds=set(); owners=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for index,item in enumerate(entries):
        path=f"entry[{index}]"; kind=item.get("operation_kind")
        require(isinstance(kind,str) and kind and kind not in kinds,f"{path}: kind"); kinds.add(kind)
        require(item.get("contract_sha256")==NEW_CONTRACT_SHA256,f"{path}: contract")
        sources=item.get("source_theorems"); require(isinstance(sources,list) and sources and all(isinstance(source,str) and source.startswith("CMR") for source in sources),f"{path}: sources")
        owner=item.get("owner_effect"); payment=item.get("payment_class"); continuation=item.get("continuation")
        require(owner in ALLOWED_OWNERS,f"{path}: owner"); require(payment in ALLOWED_PAYMENTS,f"{path}: payment"); require(isinstance(continuation,str) and continuation,f"{path}: continuation")
        if payment=="scheduler-dispatch": require("scheduler" in continuation,f"{path}: scheduler")
        if payment=="spectral-certificate": require("certificate" in continuation or "bind" in continuation,f"{path}: certificate")
        if payment=="owner-witness-stock": require("record" in continuation,f"{path}: witness")
        if payment=="finite-base-dispatch": require("record" in continuation,f"{path}: finite base")
        if payment=="table-enumeration": require("enumerate" in continuation,f"{path}: table")
        if payment=="certificate-gluing": require("glue" in continuation,f"{path}: gluing")
        owners += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==902,"902 installed kinds required")
    require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":830,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":902,"bound_contract_count":38,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":902-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[36].update(continuation="select"),lambda x:x[1].update(continuation="estimate"),lambda x:x[27].update(continuation="code"),lambda x:x[2].update(continuation="cover"),lambda x:x[30].update(continuation="lift"),lambda x:x[0].update(owner_effect="factor-child-owner-change"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry902Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_902_exhaustive":1,"superlevel_budget_thin_auxiliary_operations_registered":1,"installed_payment_assignment_902_complete":1,"return_superlevel_cover_globally_strict":0,"universal_line_clean_budgets_close_all_classes":0,"selector_capacity_classes_closed":0,"normalized_thin_geometric_rows_subcritical":0,"auxiliary_effective_core_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
