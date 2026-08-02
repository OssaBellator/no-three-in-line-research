#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1893."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry1094Error(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise Registry1094Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="60172375358504d3c697b73cf45d0d7df60441a01f09a0fa46140d720852245b"
BASE_OPERATION_KIND_COUNT=1030
BASE_CONTRACT_COUNT=40
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="fcd39ea9448f1bc6cf0b12c3108d48a3edd2cb237be6c21593dd12b9c078374f"

RAW=r"""exact-host-occupancy-moment-vector|CMR1830|same-owner|table-enumeration|enumerate maximum occupancy and first three line-capacity moments for every geometric host
first-occupancy-moment-identity|CMR1831|same-owner|local-family-equivalence|replace total line occupancy by its exact host moment identity
second-occupancy-moment-identity|CMR1832|same-owner|local-family-equivalence|replace pair occupancy mass by its exact host moment identity
third-occupancy-moment-identity|CMR1833|same-owner|local-family-equivalence|replace triple occupancy mass by its exact host moment identity
symmetric-occupancy-moment-envelope|CMR1834|same-owner|spectral-certificate|certificate-bind all line capacities by the symmetric moment envelope
nonuniform-height-layer-identity|CMR1835|same-owner|spectral-certificate|certificate-bind height-layer occupancy exactly without symmetric relaxation
moment-compressed-geometric-certificate|CMR1836|same-owner|spectral-certificate|certificate-bind a geometric fibre row by its finite occupancy moment vector
occupancy-moment-census-endpoint|CMR1837|same-owner|finite-base-dispatch|record the exact moment catalogue and compressed certificate surface
labelled-recurrent-coefficient-row|CMR1838|same-owner|local-family-equivalence|replace scalar coefficients by exact child-labelled coefficient rows
lyapunov-weighted-edge-score|CMR1839|same-owner|local-family-equivalence|replace each child coefficient by its product with the child Lyapunov weight
label-weighted-response-objective|CMR1840|same-owner|spectral-certificate|certificate-bind one response law by the exact label-weighted objective
label-weighted-nested-assignment|CMR1841|same-owner|spectral-certificate|certificate-bind labelled rank-two and rank-three terms by nested assignments
label-weighted-rational-dual|CMR1842|same-owner|certificate-gluing|glue inner middle and outer labelled assignment duals
label-weighted-integer-certificate|CMR1843|same-owner|spectral-certificate|certificate-clear the labelled nested LP to strict integer inequalities
label-preserving-auxiliary-elimination|CMR1844|same-owner|certificate-gluing|glue labelled auxiliary resolvents into the weighted outer row
label-weighted-unified-lp-endpoint|CMR1845|same-owner|finite-base-dispatch|record the exact labelled unified assignment LP schema
full-line-diagonal-parity-split|CMR1846|same-owner|local-family-equivalence|replace full-line occupancy by exact diagonal parity classes
even-diagonal-occupancy-law|CMR1847|same-owner|spectral-certificate|certificate-bind even diagonal line occupancy by the parity law
odd-diagonal-occupancy-law|CMR1848|same-owner|spectral-certificate|certificate-bind odd diagonal line occupancy by the parity law
off-diagonal-line-pairing-law|CMR1849|same-owner|local-family-equivalence|replace off-diagonal occupancy by paired line contributions
diagonal-parity-moment-census|CMR1850|same-owner|table-enumeration|enumerate parity-refined line occupancy moments over every geometric host
parity-refined-line-capacity|CMR1851|same-owner|spectral-certificate|certificate-bind line energy by parity-refined occupancy capacities
parity-refined-host-certificate|CMR1852|same-owner|spectral-certificate|certificate-bind one host row by its exact diagonal parity profile
diagonal-parity-endpoint|CMR1853|same-owner|finite-base-dispatch|record the exact diagonal-parity line-capacity catalogue
geometric-moment-vector-order|CMR1854|same-owner|local-family-equivalence|replace raw host rows by the componentwise geometric moment order
moment-dominance-pruning|CMR1855|same-owner|table-enumeration|enumerate and remove every moment vector dominated componentwise
moment-pareto-frontier|CMR1856|same-owner|table-enumeration|enumerate the exact Pareto frontier of geometric fibre moments
positive-weight-moment-optimization|CMR1857|same-owner|spectral-certificate|certificate-restrict every positive weighted moment objective to the Pareto frontier
active-height-phase-decomposition|CMR1858|same-owner|local-family-equivalence|replace a continuous height-weight objective by finitely many active phases
pareto-envelope-rational-certificate|CMR1859|same-owner|spectral-certificate|certificate-bind each active moment phase by a rational supporting inequality
pareto-envelope-integer-certificate|CMR1860|same-owner|spectral-certificate|certificate-clear moment Pareto support inequalities to exact integers
moment-pareto-endpoint|CMR1861|same-owner|finite-base-dispatch|record the finite active-height Pareto envelope worklist
labelled-state-registry-manifest|CMR1862|same-owner|table-enumeration|enumerate every labelled recurrent state identifier and positive integer weight
complete-labelled-row-manifest|CMR1863|same-owner|table-enumeration|enumerate exactly one complete recurrent row for every declared state
labelled-coefficient-provenance-check|CMR1864|same-owner|owner-witness-stock|record exact edge pair triple child labels and integer coefficients
inner-dual-coverage-check|CMR1865|same-owner|certificate-gluing|glue complete rank-two and rank-three inner dual coverage to each labelled row
outer-dual-feasibility-check|CMR1866|same-owner|spectral-certificate|certificate-check every allowed outer edge against the denominator-cleared row score
strict-row-slack-check|CMR1867|same-owner|spectral-certificate|certificate-check positive slack against the parent Lyapunov budget
labelled-manifest-corruption-audit|CMR1868|same-owner|finite-base-dispatch|record rejected incomplete inconsistent or nonstrict assignment manifests
labelled-assignment-manifest-endpoint|CMR1869|same-owner|finite-base-dispatch|record the executable labelled recurrent certificate artifact
rank-three-host-slack-definition|CMR1870|same-owner|local-family-equivalence|replace the rank-three row by its exact hostwise residual slack
rank-three-zero-slack-classification|CMR1871|same-owner|table-enumeration|enumerate hosts with no residual rank-three slack
rank-three-positive-slack-classes|CMR1872|same-owner|table-enumeration|enumerate denominator and fibre classes with positive rank-three slack
rank-three-slack-lower-bounds|CMR1873|same-owner|spectral-certificate|certificate-bind each positive slack class by its exact lower bound
rank-three-slack-pareto-refinement|CMR1874|same-owner|spectral-certificate|certificate-combine rank-three slack with moment Pareto classes
rank-three-slack-residual-budget|CMR1875|same-owner|spectral-certificate|certificate-reserve exact rank-three slack for lower-rank or return-selector terms
rank-three-slack-class-worklist|CMR1876|same-owner|finite-base-dispatch|record zero-slack and positive-slack fibre worklists
rank-three-fibre-slack-endpoint|CMR1877|same-owner|finite-base-dispatch|record the exact hostwise rank-three slack catalogue
exact-response-averaged-line-first-moment|CMR1878|same-owner|local-family-equivalence|replace response-averaged line occupancy by its exact first moment
exact-response-averaged-line-second-moment|CMR1879|same-owner|local-family-equivalence|replace response-averaged line pair occupancy by its exact second moment
exact-response-averaged-line-third-moment|CMR1880|same-owner|local-family-equivalence|replace response-averaged line triple occupancy by its exact third moment
averaged-line-moment-rook-ratio|CMR1881|same-owner|spectral-certificate|certificate-bind averaged line moments by exact contracted rook ratios
background-height-averaged-moment-row|CMR1882|same-owner|spectral-certificate|certificate-bind background-dependent lower ranks by averaged line moments
averaged-moment-integer-certificate|CMR1883|same-owner|spectral-certificate|certificate-clear response-averaged line moment bounds to exact integers
averaged-line-moment-host-census|CMR1884|same-owner|table-enumeration|enumerate exact response-averaged line moments across every geometric host
response-averaged-line-endpoint|CMR1885|same-owner|finite-base-dispatch|record the exact averaged-moment certificate surface
rank-three-slack-budget-variable|CMR1886|same-owner|local-family-equivalence|replace unused rank-three capacity by an explicit residual budget variable
load-one-line-budget-table|CMR1887|same-owner|table-enumeration|enumerate exact hostwise allocation for background line load one
load-two-line-budget-table|CMR1888|same-owner|table-enumeration|enumerate exact hostwise allocation for background line load two
slack-weighted-lower-rank-capacity|CMR1889|same-owner|spectral-certificate|certificate-bind rank-one and rank-two terms by allocated rank-three slack
slack-return-selector-coupling|CMR1890|same-owner|spectral-certificate|certificate-bind return-selector terms by the residual host slack budget
hostwise-line-budget-feasibility|CMR1891|same-owner|scheduler-dispatch|scheduler selects a strict response when one hostwise slack allocation is feasible
line-budget-integer-certificate|CMR1892|same-owner|spectral-certificate|certificate-clear rank-three slack allocation to exact integer inequalities
rank-three-slack-line-budget-endpoint|CMR1893|same-owner|finite-base-dispatch|record the exact hostwise slack allocation worklist"""

def parse(line: str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-1094/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed occupancy moment labelled LP parity Pareto manifest slack and line-budget operations through CMR1893","honesty_flags":{"labelled_assignment_manifest_populated_all_recurrent_states":0,"rank_three_slack_allocates_all_geometric_rows":0,"actual_background_height_profiles_certified":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="df6134106c292aa93711dcb060e013b6c6d700cc65813ae1943af2bdc8cb260f"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"spectral-certificate","local-family-equivalence","finite-base-dispatch","scheduler-dispatch","owner-witness-stock","table-enumeration","certificate-gluing"}

def validate(entries: list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==64,"sixty-four operations required")
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
        if payment=="finite-base-dispatch": require("record" in continuation,f"{path}: finite base")
        if payment=="owner-witness-stock": require("record" in continuation,f"{path}: witness")
        if payment=="table-enumeration": require("enumerate" in continuation,f"{path}: table")
        if payment=="certificate-gluing": require("glue" in continuation,f"{path}: gluing")
        owners += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==1094,"1094 installed kinds required"); require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":1030,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":1094,"bound_contract_count":41,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":1094-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[61].update(continuation="select"),lambda x:x[4].update(continuation="moment"),lambda x:x[0].update(continuation="table"),lambda x:x[12].update(continuation="dual"),lambda x:x[32].update(continuation="provenance"),lambda x:x[0].update(owner_effect="factor-child-owner-change"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry1094Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_1094_exhaustive":1,"labelled_moment_slack_assignment_operations_registered":1,"installed_payment_assignment_1094_complete":1,"labelled_assignment_manifest_populated_all_recurrent_states":0,"rank_three_slack_allocates_all_geometric_rows":0,"actual_background_height_profiles_certified":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
