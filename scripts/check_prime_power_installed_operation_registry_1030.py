#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1829."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry1030Error(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise Registry1030Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="240be08e0fe0e6e061d55a245cd544880b8612f9575099faa011e10d47ec77c6"
BASE_OPERATION_KIND_COUNT=974
BASE_CONTRACT_COUNT=39
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="f03ab61fabb4ad8727f239a31474466f3074f2397762a63fd4255c683176e3eb"

RAW=r"""residual-matching-collinearity-counterexample|CMR1774|same-owner|owner-witness-stock|record an explicit residual matching permutation that destroys Euclidean collinearity
trivial-residual-geometric-stabilizer|CMR1775|same-owner|owner-witness-stock|record the identity as the only residual geometric stabilizer fixing zero and one
matching-geometric-invariant-separation|CMR1776|same-owner|local-family-equivalence|replace matching-only invariants by separate matching and geometric coordinates
exact-geometric-state-signature|CMR1777|same-owner|local-family-equivalence|replace a normalized state by its full deletion prescription provenance and line-incidence signature
honest-geometric-fibre-expansion|CMR1778|same-owner|local-family-equivalence|replace one matching orbit by exact geometric fibres verified or componentwise upper-fibre rows
geometric-fibre-certificate-lifting|CMR1779|same-owner|certificate-gluing|glue strict exact-orbit or upper-fibre certificates back to every geometric state
finite-geometric-census-compiler|CMR1780|same-owner|table-enumeration|enumerate exact geometric fibres denominators multiplicities owners and labelled rows
geometric-fibre-correction-endpoint|CMR1781|same-owner|finite-base-dispatch|record the corrected geometric thin-table frontier beyond matching normalization
exact-line-energy-prescription-coefficients|CMR1782|same-owner|local-family-equivalence|replace line-energy offspring by exact rank-one rank-two and rank-three prescription coefficients
exact-line-energy-response-expectation|CMR1783|same-owner|local-family-equivalence|replace one response-law line energy by exact prescription marginal sums
corrected-line-energy-marginal-upper-row|CMR1784|same-owner|spectral-certificate|certificate-dominate corrected genuinely new offspring by the exact marginal line-energy row
rank-one-line-energy-assignment|CMR1785|same-owner|spectral-certificate|certificate-bind the rank-one geometric term by one ordinary assignment dual
rank-two-three-marginal-rows|CMR1786|same-owner|spectral-certificate|certificate-bind exact or coarse rank-two and rank-three prescription marginals
charged-geometric-coefficient-alternative|CMR1787|same-owner|spectral-certificate|certificate-dominate geometric coefficients by pair-only and background-triple charge coefficients
exact-line-energy-rook-numerator|CMR1788|same-owner|table-enumeration|enumerate the exact integer line-energy numerator from contracted rook counts
hybrid-line-energy-strict-response|CMR1789|same-owner|scheduler-dispatch|scheduler selects a strict response when combined marginal bounds lie below destroyed load
rank-prescription-peeling-identity|CMR1790|same-owner|local-family-equivalence|replace every rank prescription sum by its exact distinguished-edge peeling identity
rank-two-nested-assignment|CMR1791|same-owner|spectral-certificate|certificate-bind compatible pair scores by contracted inner and outer assignments
rank-three-nested-assignment|CMR1792|same-owner|spectral-certificate|certificate-bind compatible triple scores by three nested contracted assignments
nested-rational-dual-cascade|CMR1793|same-owner|certificate-gluing|glue inner middle and outer rational assignment dual objectives
nested-strict-integer-certificate|CMR1794|same-owner|spectral-certificate|certificate-clear nested rank-one-two-three objectives to one strict integer inequality
nested-line-energy-specialization|CMR1795|same-owner|spectral-certificate|certificate-bind exact geometric line energy by peeled outer edge scores
class-supported-nested-cover-cascade|CMR1796|same-owner|certificate-gluing|glue class-supported covers at every contracted assignment level
nested-assignment-line-energy-endpoint|CMR1797|same-owner|finite-base-dispatch|record exact marginal and nested-assignment certificate alternatives
raw-geometric-fibre-expansion|CMR1798|same-owner|local-family-equivalence|replace each canonical matching host by its coordinate-labelled raw geometric fibre
exact-geometric-orbit-size-distribution|CMR1799|same-owner|table-enumeration|enumerate side-four and side-five matching-orbit fibre sizes
coordinate-labelled-geometric-host-census|CMR1800|same-owner|table-enumeration|enumerate the exact seven-hundred-forty raw geometric hosts
geometric-fibre-denominator-reuse|CMR1801|same-owner|local-family-equivalence|replace repeated matching denominators by orbit-shared counts while retaining geometric numerators
response-line-occupancy-triple-cap|CMR1802|same-owner|spectral-certificate|certificate-bind response triple counts by maximum host line occupancy
background-rank-two-line-load-cap|CMR1803|same-owner|spectral-certificate|certificate-bind rank-two geometric energy by the maximum compatible background line load
coarse-geometric-fibre-certificate|CMR1804|same-owner|spectral-certificate|certificate-bind every response by rank-one assignment background load and host triple caps
geometric-fibre-host-census-endpoint|CMR1805|same-owner|finite-base-dispatch|record the exact seven-hundred-forty-host geometric certificate worklist
response-triple-value-census|CMR1806|same-owner|table-enumeration|enumerate exact response triple values over every raw side-four and side-five host
hostwise-rank-three-maximum-census|CMR1807|same-owner|table-enumeration|enumerate the maximum response triple count in every raw host
triple-free-geometric-host-stock|CMR1808|same-owner|finite-base-dispatch|record the exact side-four hosts with identically zero rank-three row
side-four-rank-three-numerator-table|CMR1809|same-owner|table-enumeration|enumerate sharp side-four denominator-specific rank-three numerators
side-five-rank-three-numerator-table|CMR1810|same-owner|table-enumeration|enumerate sharp side-five denominator-specific rank-three numerators
uniform-rank-three-fibre-caps|CMR1811|same-owner|spectral-certificate|certificate-bind side-four and side-five rank-three expectations by sharp uniform inequalities
aggregate-rank-three-fibre-census|CMR1812|same-owner|table-enumeration|enumerate aggregate response and response-triple occurrence totals
rank-three-geometric-fibre-endpoint|CMR1813|same-owner|finite-base-dispatch|record the complete background-independent rank-three fibre table
line-occupancy-assignment-optimum|CMR1814|same-owner|table-enumeration|enumerate each line occupancy capacity by a zero-one assignment optimum
linewise-monotone-energy-cap|CMR1815|same-owner|spectral-certificate|certificate-dominate one line energy by its host occupancy capacity
complete-line-capacity-row|CMR1816|same-owner|spectral-certificate|certificate-bind complete geometric response energy by the line-occupancy table
rank-one-line-trace-dual-sum|CMR1817|same-owner|certificate-gluing|glue weighted line-indicator assignment duals into one rank-one dual
rank-two-line-occupancy-certificate|CMR1818|same-owner|spectral-certificate|certificate-bind rank-two energy by background loads and line occupancy capacities
rank-three-line-occupancy-certificate|CMR1819|same-owner|spectral-certificate|certificate-bind response triples by cubic line occupancy capacities
deterministic-line-capacity-strict-response|CMR1820|same-owner|scheduler-dispatch|scheduler selects a strict response when the complete line-capacity total is below destroyed load
line-occupancy-capacity-endpoint|CMR1821|same-owner|finite-base-dispatch|record the finite background-line occupancy certificate compiler
peeled-geometric-outer-score|CMR1822|same-owner|local-family-equivalence|replace all geometric ranks by one peeled outer edge score
combined-return-selector-geometric-score|CMR1823|same-owner|local-family-equivalence|replace return selector and geometric collateral by one common outer edge score
unified-outer-assignment-certificate|CMR1824|same-owner|spectral-certificate|certificate-bind the complete coupled response by one outer assignment
unified-class-supported-cover-compiler|CMR1825|same-owner|certificate-gluing|glue return selector and geometric class covers into one feasible outer dual
unified-outer-strict-integer-certificate|CMR1826|same-owner|spectral-certificate|certificate-clear the complete outer score to one strict integer inequality
unified-line-clean-strict-response|CMR1827|same-owner|scheduler-dispatch|scheduler selects a strict line-clean response from a unified outer dual below destroyed load
unified-recurrent-row-certificate|CMR1828|same-owner|spectral-certificate|certificate-bind a normalized recurrent row below one before auxiliary elimination
unified-outer-assignment-endpoint|CMR1829|same-owner|finite-base-dispatch|record the exact unified outer response-score certificate surface"""

def parse(line: str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-1030/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed geometric fibre marginal nested occupancy and unified outer assignment operations through CMR1829","honesty_flags":{"geometric_fibre_rows_complete_all_provenance":0,"rank_one_two_geometric_fibre_rows_subcritical":0,"unified_outer_assignment_globally_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="c93c2c8d69260ecc2c2c4b0709af26c16a9c054b2ec7f85f4cea83a36dcb8084"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"spectral-certificate","local-family-equivalence","finite-base-dispatch","scheduler-dispatch","owner-witness-stock","table-enumeration","certificate-gluing"}

def validate(entries: list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==56,"fifty-six operations required")
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
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==1030,"1030 installed kinds required"); require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":974,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":1030,"bound_contract_count":40,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":1030-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[15].update(continuation="select"),lambda x:x[10].update(continuation="estimate"),lambda x:x[6].update(continuation="compile"),lambda x:x[0].update(continuation="counterexample"),lambda x:x[5].update(continuation="lift"),lambda x:x[0].update(owner_effect="factor-child-owner-change"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry1030Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_1030_exhaustive":1,"geometric_fibre_outer_assignment_operations_registered":1,"installed_payment_assignment_1030_complete":1,"geometric_fibre_rows_complete_all_provenance":0,"rank_one_two_geometric_fibre_rows_subcritical":0,"unified_outer_assignment_globally_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
