#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1453."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
class Registry656Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise Registry656Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
BASE_REGISTRY_SHA256="4c0e1714052dcd95aa941a83249a2b2fecc09c723f58d29fa8fe32933f7c27a9"
BASE_OPERATION_KIND_COUNT=608
BASE_CONTRACT_COUNT=33
BASE_OWNER_CHANGING_KIND_COUNT=161
NEW_CONTRACT_SHA256="a590a41fb713c91904106d20d5eb31e18171a0761ce35a3908a29c8b87d547db"
RAW = r"""response-induced-surviving-transversal|CMR1390|same-owner|local-family-equivalence|replace one response by its equal-weight surviving candidate transversal
surviving-transversal-collateral-bound|CMR1391|same-owner|spectral-certificate|certificate-bound response collateral by the exempt candidate weight
weighted-transversal-optimization-identity|CMR1392|same-owner|local-family-equivalence|identify minimum collateral with minimum surviving transversal exemption weight
clean-transversal-response-selection|CMR1393|same-owner|scheduler-dispatch|scheduler selects a clean response from a full surviving candidate transversal
threshold-transversal-response-selection|CMR1394|same-owner|scheduler-dispatch|scheduler selects a strict response from a subthreshold surviving transversal
failed-transversal-hall-witness|CMR1395|same-owner|owner-witness-stock|record a Hall-deficient row set for every blocked transversal deletion
transversal-minimal-blocker-unit-wall-descent|CMR1395|factor-child-owner-change|strict-child-descent|continue a failed transversal through its inclusion-minimal deficiency-one unit wall
equal-share-owner-obstruction-record|CMR1396|same-owner|finite-base-dispatch|record the side-four obstruction to universal equal fractional ownership
side-five-clean-transversal-witness|CMR1397|same-owner|finite-base-dispatch|record the exact thirteen-edge clean transversal witness
fixed-presampling-candidate-owner|CMR1399,CMR1431|same-owner|owner-witness-stock|record the least entering edge owner before the response is sampled
owner-rook-class-unconditional-row|CMR1400,CMR1432|same-owner|spectral-certificate|bind each owner load to exact rook-class candidate counts and probabilities
conditional-owner-marginal-row|CMR1401,CMR1424,CMR1433|same-owner|spectral-certificate|bind conditional owner weight by one positive edge-marginal division
inherited-owner-signature-refinement|CMR1402,CMR1434|same-owner|local-family-equivalence|refine exact owner rows by inherited height line prefix quotient or carry signatures
rook-owner-assignment-dual-certificate|CMR1403,CMR1435|same-owner|spectral-certificate|certificate-dominate exact owner weights by rational row-column potentials
rook-owner-restricted-host-penalty|CMR1404,CMR1436|same-owner|spectral-certificate|certificate-add exact unavailable-edge marginal penalties to the owner dual
exact-owner-wall-size|CMR1406|same-owner|owner-witness-stock|record the exact rectangle-minus-diagonal-minus-target blocker size
sharp-extension-free-matching-preclusion|CMR1407|same-owner|owner-witness-stock|record the n-minus-two preclusion number and two exceptional stars
small-owner-deletion-survival|CMR1408|same-owner|scheduler-dispatch|scheduler preserves a response after every subcritical owner-edge deletion set
canonical-owner-support-transversal|CMR1409,CMR1410|same-owner|scheduler-dispatch|scheduler uses fixed candidate owners as a surviving transversal when support is admissible
owner-tail-response-policy|CMR1411|same-owner|scheduler-dispatch|scheduler selects a response after maximizing admissible owner-weight concentration
fractional-rank-three-cover-rounding|CMR1412|same-owner|scheduler-dispatch|scheduler rounds a low fractional prescription cover to a surviving owner support
dual-dispersed-candidate-packing|CMR1413|same-owner|owner-witness-stock|record the dual edge-load-one fractional candidate packing
residual-forbidden-rook-number|CMR1414|same-owner|finite-base-dispatch|bind every residual forbidden board to its exact rook numbers
exact-prescription-completion-count|CMR1415|same-owner|finite-base-dispatch|bind one prescription to its inclusion-exclusion completion count
exact-rook-prescription-probability|CMR1416,CMR1418|same-owner|spectral-certificate|certificate-use the exact rook completion ratio and universal rank bounds
rook-probability-class-stock|CMR1417|same-owner|owner-witness-stock|record the finite linear-size stock of exact rook probability classes
rook-class-collateral-expectation|CMR1419|same-owner|spectral-certificate|bind exact candidate class counts to the expected collateral row
exact-unavailable-edge-marginal-row|CMR1420,CMR1421|same-owner|spectral-certificate|certificate-bind unavailable-edge use to exact extension-free marginals
owner-line-load-decomposition|CMR1422,CMR1423|same-owner|local-family-equivalence|replace each owner load by its exact line-local sum and partition every new credit once
doubly-stochastic-owner-marginal|CMR1425|same-owner|spectral-certificate|bind owner occurrence probabilities to one doubly stochastic response matrix
owner-assignment-primal-dual|CMR1426|same-owner|spectral-certificate|certificate-reduce cross-line expectation to one bipartite assignment dual
strict-owner-assignment-certificate|CMR1427|same-owner|spectral-certificate|certificate-force improvement when the owner dual lies below destroyed load
integer-owner-assignment-certificate|CMR1428,CMR1429|same-owner|spectral-certificate|certificate-clear owner dual denominators into strict integer inequalities
inherited-span-line-capacity|CMR1438|same-owner|owner-witness-stock|record primitive-height line capacity using the inherited coordinate span
harmonic-owner-line-bound|CMR1439|same-owner|spectral-certificate|certificate-bound realized owner triples by harmonic eligible-pair energy
conditional-harmonic-pair-energy|CMR1440|same-owner|spectral-certificate|bind conditional fixed and response partner harmonic energy exactly
harmonic-owner-envelope|CMR1441|same-owner|spectral-certificate|certificate-dominate conditional owner weight by the harmonic star envelope
harmonic-owner-assignment-dual|CMR1442|same-owner|spectral-certificate|certificate-couple harmonic owner envelopes through one assignment dual
dyadic-harmonic-owner-split|CMR1443|same-owner|local-family-equivalence|split conditional harmonic owner energy exactly by dyadic height band
high-height-harmonic-tail|CMR1444,CMR1445|same-owner|history-budget|bound and discard the high-height conditional owner tail
lattice-capacity-scalar-coefficient|CMR1446|same-owner|local-family-equivalence|replace quadratic line population by its exact inherited-span capacity coefficient
lattice-capacity-owner-line-bound|CMR1447|same-owner|spectral-certificate|certificate-bound realized owner triples by lattice-capacity pair weights
conditional-lattice-capacity-pair-row|CMR1448|same-owner|spectral-certificate|bind conditional capacity-weighted partner rows exactly
lattice-capacity-owner-envelope|CMR1449|same-owner|spectral-certificate|certificate-dominate conditional owner weight by the capacity envelope
capacity-harmonic-refinement|CMR1450|same-owner|local-family-equivalence|replace the harmonic owner envelope by its termwise smaller capacity refinement
exact-owner-height-cutoff|CMR1451|same-owner|owner-witness-stock|record zero capacity above half the inherited coordinate span
lattice-capacity-assignment-certificate|CMR1452|same-owner|spectral-certificate|certificate-couple capacity owner envelopes through one assignment dual
dyadic-lattice-capacity-upper-quotient|CMR1453|same-owner|spectral-certificate|certificate-bind dyadic capacity coefficients to an honest owner upper quotient"""
def parse(line:str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}
NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-656/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"correction_policy":"CMR1430--1437 co-binds the CMR1398--1405 rook-owner family","honesty_flags":{"uniform_cross_line_owner_policy_proved":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="65c91f7b242b0c8d35749aad1126a4b4af937cff346e71babe0890013660b3d2"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"owner-witness-stock","history-budget","spectral-certificate","finite-base-dispatch","local-family-equivalence","scheduler-dispatch","strict-child-descent"}
def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==48,"forty-eight operations required")
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
        if payment=="finite-base-dispatch": require("record" in continuation or "bind" in continuation,f"{path}: base")
        owners+=owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==656,"656 kinds required"); require(owners==162,"162 owner-changing kinds required")
    return {"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":656,"bound_contract_count":BASE_CONTRACT_COUNT+1,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":656-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}
def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[3].update(continuation="select"),lambda x:x[6].update(owner_effect="same-owner"),lambda x:x[14].update(payment_class="strict-child-descent"),lambda x:x[7].update(payment_class="spectral-certificate"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry656Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected
def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_656_exhaustive":1,"candidate_transversal_rook_capacity_operations_registered":1,"installed_payment_assignment_656_complete":1,"uniform_cross_line_owner_policy_proved":0,"same_owner_diagonal_blocks_subcritical":0,"independent_line_kernel_sufficient":0,"global_target_collateral_inequality_proved":0,"all_owner_operations_proved":0,"all_scheduler_operations_proved":0,"all_construction_ancestry_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))
if __name__=="__main__": main()
