#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1773."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry974Error(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise Registry974Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="2c9bf1cc1b551a0560753b5d5de918abaa61e2d602d2ac2ce078ff247cdccdb4"
BASE_OPERATION_KIND_COUNT=902
BASE_CONTRACT_COUNT=38
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="681a56e37003368e62a92ae7df349488e03e03eec34c2cddf2ab39b8d6622bdd"

RAW=r"""exact-rank-prescription-mass|CMR1702|same-owner|local-family-equivalence|replace every rank response family by its exact conserved binomial mass
corrected-rank-family-mass-cap|CMR1703|same-owner|spectral-certificate|certificate-bind every corrected rank family by conserved total mass
integer-rank-numerator-conservation|CMR1704|same-owner|spectral-certificate|certificate-clear rank-mass conservation to exact integer numerators
forced-prescription-mass-subtraction|CMR1705|same-owner|local-family-equivalence|replace stochastic rank mass by the exact nonforced residual after contractions
pointwise-and-rank-mass-minimum|CMR1706|same-owner|spectral-certificate|certificate-bind one class by the minimum of pointwise and conserved mass caps
side-four-five-conserved-capacity|CMR1707|same-owner|finite-base-dispatch|record exact side-four and side-five conserved rank capacities
rank-mass-integer-class-capacity|CMR1708|same-owner|spectral-certificate|certificate-bind one class by exact integer pointwise and rank-mass minima
rank-mass-capacity-endpoint|CMR1709|same-owner|finite-base-dispatch|record the combined pointwise forced and conserved rank-mass compiler
multiplicity-weighted-line-clean-expectation|CMR1710|same-owner|local-family-equivalence|replace candidate indicators by prescription multiplicity weighted expectations
multiplicity-corrected-rank-mass-bound|CMR1711|same-owner|spectral-certificate|certificate-bind off-line collateral by rank mass times multiplicity caps
forced-multiplicity-mass-subtraction|CMR1712|same-owner|spectral-certificate|certificate-remove forced prescription mass from the stochastic multiplicity row
pointwise-count-rank-mass-minimum|CMR1713|same-owner|spectral-certificate|certificate-bind each rank by the minimum of count and multiplicity-mass caps
line-clean-large-load-response|CMR1714|same-owner|scheduler-dispatch|scheduler selects a strict line-clean response above the multiplicity-corrected load threshold
line-clean-large-load-integer-certificate|CMR1715|same-owner|spectral-certificate|certificate-clear multiplicity-weighted line-clean improvement to exact integers
rooted-trace-rank-mass-specialization|CMR1716|same-owner|scheduler-dispatch|scheduler selects a strict rooted trace response above the corrected mass threshold
multiplicity-aware-line-clean-endpoint|CMR1717|same-owner|finite-base-dispatch|record exact rook budget and multiplicity-aware large-load certificate levels
response-wise-owned-submatching-cap|CMR1718|same-owner|local-family-equivalence|replace owned prescription occurrence by owner-edge count times submatching stock
owner-support-matching-capacity|CMR1719|same-owner|spectral-certificate|certificate-bind owned prescription mass by owner-support matching number
owner-support-vertex-cover-capacity|CMR1720|same-owner|spectral-certificate|certificate-bind owner-support mass by source-target cover size
fixed-owner-conditional-rank-mass|CMR1721|same-owner|spectral-certificate|certificate-bind each owner edge by conditional rank-submatching mass
weighted-owner-support-capacity|CMR1722|same-owner|spectral-certificate|certificate-bind weighted owned credits by support matching number and rank weights
return-selector-owner-score-cap|CMR1723|same-owner|spectral-certificate|certificate-bind the combined owner edge score by return-selector rank counts
owner-support-integer-numerator-capacity|CMR1724|same-owner|spectral-certificate|certificate-clear weighted owner-support capacity to integer numerators
owner-support-capacity-endpoint|CMR1725|same-owner|finite-base-dispatch|record the matching-number and vertex-cover owner-support compiler
support-local-collateral-expectation|CMR1726|same-owner|spectral-certificate|certificate-bind support-local collateral by matching number and multiplicity factors
small-owner-support-strict-response|CMR1727|same-owner|scheduler-dispatch|scheduler selects a strict response above the support-local load threshold
owner-cover-large-load-closure|CMR1728|same-owner|scheduler-dispatch|scheduler closes a large-load row from one source-target owner cover
finite-owner-support-closure|CMR1729|same-owner|scheduler-dispatch|scheduler closes a large-load row from one finite owner edge support
prime-field-reused-support-closure|CMR1730|same-owner|scheduler-dispatch|scheduler applies one-edge or two-edge reused-support thresholds
weighted-owner-support-large-load|CMR1731|same-owner|spectral-certificate|certificate-bind weighted destroyed load against support-local weighted collateral
owner-support-integer-slack-overflow|CMR1732|same-owner|owner-witness-stock|record exact support slack or one overflowing rank multiplicity class
small-owner-support-endpoint|CMR1733|same-owner|finite-base-dispatch|record strict support closure or the residual multiplicity worklist
rank-three-multiplicity-injectivity|CMR1734|same-owner|local-family-equivalence|replace every rank-three multiplicity by its zero-or-one exact value
rank-two-background-line-load|CMR1735|same-owner|local-family-equivalence|replace rank-two multiplicity by the exact background load on its determined line
rank-one-background-secant-sum|CMR1736|same-owner|local-family-equivalence|replace rank-one multiplicity by the exact background secant pair sum
uniform-secant-line-load-cap|CMR1737|same-owner|spectral-certificate|certificate-bind rank-one multiplicity by secant count and maximum line load
primitive-direction-secant-form|CMR1738|same-owner|local-family-equivalence|replace rank-one secants by exact primitive-direction line classes
geometric-line-clean-multiplicity-bound|CMR1739|same-owner|spectral-certificate|certificate-bind line-clean collateral by exact rankwise geometric multiplicities
geometric-owner-support-multiplicity-bound|CMR1740|same-owner|spectral-certificate|certificate-bind owner-supported collateral by geometric multiplicity formulas
geometric-multiplicity-endpoint|CMR1741|same-owner|finite-base-dispatch|record rank-three injective rank-two line-load and rank-one secant formulas
convex-secant-packing-maximum|CMR1742|same-owner|spectral-certificate|certificate-bind secant pair energy by the exact packed integer maximum
packed-rank-one-multiplicity|CMR1743|same-owner|spectral-certificate|certificate-bind rank-one multiplicity by background size and line-height cap
packed-secant-linear-relaxation|CMR1744|same-owner|spectral-certificate|certificate-bind packed secant multiplicity by the linear height relaxation
combined-rankwise-packed-caps|CMR1745|same-owner|local-family-equivalence|replace abstract multiplicities by packed rank-one rank-two and injective rank-three caps
packed-line-clean-large-load|CMR1746|same-owner|scheduler-dispatch|scheduler selects a strict line-clean response above the packed multiplicity threshold
packed-owner-support-large-load|CMR1747|same-owner|scheduler-dispatch|scheduler selects a strict owner-supported response above the packed threshold
packed-multiplicity-slack-overflow|CMR1748|same-owner|owner-witness-stock|record positive packed slack or one large support height secant or load obstruction
packed-secant-endpoint|CMR1749|same-owner|finite-base-dispatch|record the background-size and line-height multiplicity compiler
local-pair-triple-charge-inequality|CMR1750|same-owner|credit-charge|charge high line pair and point multiplicity to background triples with low-load residuals
rank-one-pair-triple-decomposition|CMR1751|same-owner|credit-charge|charge rank-one multiplicity to pair-only secants and triple-shadow slots
rank-two-low-slot-triple-decomposition|CMR1752|same-owner|credit-charge|charge rank-two multiplicity to two low slots and triple-shadow credits
charged-rankwise-multiplicity-cap|CMR1753|same-owner|spectral-certificate|certificate-bind rank multiplicities by pair-only and background-triple capacities
charged-line-clean-large-load|CMR1754|same-owner|scheduler-dispatch|scheduler selects a strict line-clean response above the charged multiplicity threshold
charged-owner-support-large-load|CMR1755|same-owner|scheduler-dispatch|scheduler selects a strict owner-supported response above the charged threshold
bounded-congestion-background-charge-map|CMR1756|same-owner|credit-charge|charge pairs and excess points injectively to labelled background triple slots
background-triple-charge-endpoint|CMR1757|same-owner|finite-base-dispatch|record pair-only low-slot and bounded-congestion triple charge currencies
pair-only-secant-matching|CMR1758|same-owner|local-family-equivalence|replace pair-only secants through one response point by a background matching
pair-only-secant-cardinality|CMR1759|same-owner|spectral-certificate|certificate-bind pair-only secants by half the background size
background-triple-shadow-cap|CMR1760|same-owner|spectral-certificate|certificate-bind local triple shadows by the current background triple potential
potential-only-rankwise-multiplicity|CMR1761|same-owner|spectral-certificate|certificate-bind all rank multiplicities by background size and triple potential
clean-background-multiplicity-specialization|CMR1762|same-owner|finite-base-dispatch|record triple-free background multiplicity caps
potential-only-line-clean-closure|CMR1763|same-owner|scheduler-dispatch|scheduler selects a strict line-clean response above the potential-only threshold
potential-only-owner-support-closure|CMR1764|same-owner|scheduler-dispatch|scheduler selects a strict owner-supported response above the potential threshold
background-potential-multiplicity-endpoint|CMR1765|same-owner|finite-base-dispatch|record packed-height and background-potential multiplicity compilers
linewise-binomial-rank-identity|CMR1766|same-owner|local-family-equivalence|replace one line new-triple count by exact rank-one-two-three binomial terms
global-line-energy-census|CMR1767|same-owner|local-family-equivalence|replace total geometric offspring by the exact sum of line profile energies
corrected-line-energy-upper-row|CMR1768|same-owner|spectral-certificate|certificate-dominate corrected genuinely new triples by the exact line-energy census
response-pair-triple-mass-identities|CMR1769|same-owner|local-family-equivalence|replace response pair and triple profile sums by exact global counts
linewise-background-triple-charge|CMR1770|same-owner|credit-charge|charge line-energy multiplicity to pair-only incidences low slots and line-local triple congestion
maximum-response-load-profile-bound|CMR1771|same-owner|spectral-certificate|certificate-bind line-energy offspring by pair-only incidence response load and background potential
triple-free-response-profile-bound|CMR1772|same-owner|spectral-certificate|certificate-bind triple-free response offspring by the explicit coefficient-seven bound
line-energy-profile-endpoint|CMR1773|same-owner|finite-base-dispatch|record exact profile census pair-triple identities and charged response-load bounds"""

def parse(line: str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-974/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed rank-mass large-load owner-support multiplicity charge and line-energy operations through CMR1773","honesty_flags":{"all_line_clean_large_load_rows_closed":0,"all_owner_support_rows_closed":0,"geometric_multiplicity_caps_globally_sufficient":0,"triple_free_response_policy_globally_available":0,"line_energy_profile_rows_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="5bff249b3ada147307677bb59979f034b1c2587c4cc0a8643b903dbcd6eaf96e"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"spectral-certificate","local-family-equivalence","finite-base-dispatch","scheduler-dispatch","owner-witness-stock","credit-charge"}

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
        if payment=="finite-base-dispatch": require("record" in continuation,f"{path}: finite base")
        if payment=="owner-witness-stock": require("record" in continuation,f"{path}: witness")
        if payment=="credit-charge": require("charge" in continuation,f"{path}: charge")
        owners += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==974,"974 installed kinds required"); require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":902,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":974,"bound_contract_count":39,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":974-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[12].update(continuation="select"),lambda x:x[1].update(continuation="estimate"),lambda x:x[5].update(continuation="capacity"),lambda x:x[30].update(continuation="overflow"),lambda x:x[48].update(continuation="pair"),lambda x:x[0].update(owner_effect="factor-child-owner-change"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry974Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_974_exhaustive":1,"rank_mass_multiplicity_line_energy_operations_registered":1,"installed_payment_assignment_974_complete":1,"all_line_clean_large_load_rows_closed":0,"all_owner_support_rows_closed":0,"geometric_multiplicity_caps_globally_sufficient":0,"triple_free_response_policy_globally_available":0,"line_energy_profile_rows_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
