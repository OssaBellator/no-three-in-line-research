#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1965."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any

class Registry1166Error(RuntimeError): pass
def require(ok: bool,message: str)->None:
    if not ok: raise Registry1166Error(message)
def digest(value: Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

BASE_REGISTRY_SHA256="a4d652ef07e5a78e53d7b674e0fc50b97e714e2797270db72fe540a26d40bbb5"
BASE_OPERATION_KIND_COUNT=1094
BASE_CONTRACT_COUNT=41
BASE_OWNER_CHANGING_KIND_COUNT=164
NEW_CONTRACT_SHA256="a81184108c06638fe3b44754b80c0fe271d8a92d7b78db6befb681890dd810eb"

RAW=r"""exact-owner-fate-class-key|CMR1894|same-owner|local-family-equivalence|replace every child credit by its exact owner fate collision line interface and provenance key
owner-fate-class-coefficient-sum|CMR1895|same-owner|local-family-equivalence|replace per-credit coefficients by exact sums inside one complete class
owner-fate-class-weighted-row|CMR1896|same-owner|spectral-certificate|certificate-bind each compressed class by its child Lyapunov weight
owner-fate-class-losslessness|CMR1897|same-owner|local-family-equivalence|replace the uncompressed labelled row by its exact class-compressed image
owner-fate-class-projection-warning|CMR1898|same-owner|owner-witness-stock|record the artificial cycle created by dropping fate or collision labels
owner-fate-class-upper-quotient|CMR1899|same-owner|spectral-certificate|certificate-bind incomplete fibres only by componentwise class maxima
owner-fate-class-integer-row|CMR1900|same-owner|spectral-certificate|certificate-clear the compressed weighted row to exact integers
owner-fate-compression-endpoint|CMR1901|same-owner|finite-base-dispatch|record the exact lossless compression schema for recurrent rows
compulsory-complete-response-table|CMR1902|same-owner|table-enumeration|enumerate every allowed response and every compulsory labelled coefficient
compulsory-coefficient-presence|CMR1903|same-owner|owner-witness-stock|record every return selector collision line interface and geometric coefficient as compulsory
compulsory-child-weight-lookup|CMR1904|same-owner|spectral-certificate|certificate-bind each compulsory coefficient to the declared positive child weight
compulsory-inner-dual-coverage|CMR1905|same-owner|certificate-gluing|glue complete rank-two and rank-three inner dual coverage
compulsory-outer-dual-coverage|CMR1906|same-owner|spectral-certificate|certificate-check every allowed outer edge against the full weighted score
compulsory-strict-row-slack|CMR1907|same-owner|spectral-certificate|certificate-check positive slack against the parent weighted budget
compulsory-certificate-corruption-audit|CMR1908|same-owner|finite-base-dispatch|record rejection of every omitted compulsory term or missing dual
compulsory-weighted-certificate-endpoint|CMR1909|same-owner|finite-base-dispatch|record the complete weighted certificate artifact
rank-three-preconditioner-row|CMR1910|same-owner|local-family-equivalence|replace the rank-three term by its exact host slack preconditioner
slack-preconditioned-lower-rank-score|CMR1911|same-owner|spectral-certificate|certificate-bind rank-one and rank-two terms after subtracting rank-three slack
slack-preconditioned-return-selector-score|CMR1912|same-owner|spectral-certificate|certificate-bind return and selector terms after rank-three preconditioning
slack-preconditioned-inner-duals|CMR1913|same-owner|certificate-gluing|glue inner duals against the preconditioned residual score
slack-preconditioned-outer-dual|CMR1914|same-owner|spectral-certificate|certificate-check the complete preconditioned outer assignment
slack-preconditioned-integer-manifest|CMR1915|same-owner|spectral-certificate|certificate-clear preconditioned rows to strict integers
slack-preconditioned-manifest-audit|CMR1916|same-owner|finite-base-dispatch|record rejection of negative duplicated or unallocated slack
slack-preconditioned-manifest-endpoint|CMR1917|same-owner|finite-base-dispatch|record the executable rank-three-preconditioned manifest
complete-line-energy-local-kernel|CMR1918|same-owner|local-family-equivalence|replace one response line contribution by its complete local kernel
complete-line-energy-rank-decomposition|CMR1919|same-owner|local-family-equivalence|replace the complete kernel by exact rank-one rank-two and rank-three parts
complete-line-energy-background-profile|CMR1920|same-owner|local-family-equivalence|replace background geometry by exact line occupancy and incidence profiles
complete-line-energy-response-profile|CMR1921|same-owner|local-family-equivalence|replace response geometry by exact line occupancy and matching-compatible profiles
complete-line-energy-kernel-expectation|CMR1922|same-owner|spectral-certificate|certificate-bind expected offspring by the exact complete kernel
complete-line-energy-integer-kernel|CMR1923|same-owner|spectral-certificate|certificate-clear complete kernel expectations to integer numerators
complete-line-energy-selector|CMR1924|same-owner|scheduler-dispatch|scheduler selects a strict response when the complete kernel lies below destroyed load
complete-line-energy-kernel-endpoint|CMR1925|same-owner|finite-base-dispatch|record the exact complete line-energy kernel interface
single-background-increment-identity|CMR1926|same-owner|local-family-equivalence|replace one added background point by its exact kernel increment
rank-one-background-increment|CMR1927|same-owner|local-family-equivalence|replace rank-one kernel change by exact new secant incidences
rank-two-background-increment|CMR1928|same-owner|local-family-equivalence|replace rank-two kernel change by exact line-load increments
rank-three-background-increment|CMR1929|same-owner|local-family-equivalence|replace rank-three kernel change by its exact unchanged response term
increment-kernel-monotonicity|CMR1930|same-owner|spectral-certificate|certificate-bind background growth by nonnegative local increments
increment-kernel-additive-telescope|CMR1931|same-owner|certificate-gluing|glue a sequence of background increments to the complete kernel difference
increment-kernel-integer-certificate|CMR1932|same-owner|spectral-certificate|certificate-clear background increments to exact integers
background-increment-kernel-endpoint|CMR1933|same-owner|finite-base-dispatch|record the exact background-growth kernel compiler
selector-score-background-perturbation|CMR1934|same-owner|local-family-equivalence|replace selector score change by the exact background increment kernel
selector-gap-stability-criterion|CMR1935|same-owner|spectral-certificate|certificate-preserve a unique selector when perturbation is below its response gap
selector-tie-stability-class|CMR1936|same-owner|owner-witness-stock|record the exact minimizer face when selector ties persist
selector-switch-threshold|CMR1937|same-owner|spectral-certificate|certificate-bind every selector switch to a quantitative increment threshold
selector-stability-episode-budget|CMR1938|same-owner|history-budget|bound selector changes by accumulated nonnegative background increments
selector-stable-response-row|CMR1939|same-owner|spectral-certificate|certificate-bind one stable selector row across a background interval
selector-instability-worklist|CMR1940|same-owner|finite-base-dispatch|record the exact unstable increment or tie classes
line-energy-selector-stability-endpoint|CMR1941|same-owner|finite-base-dispatch|record selector gap and perturbation certificate forms
background-normalized-line-profile|CMR1942|same-owner|local-family-equivalence|replace absolute background counts by normalized line-profile coordinates
background-normalized-rank-one-kernel|CMR1943|same-owner|spectral-certificate|certificate-bind normalized rank-one secant energy
background-normalized-rank-two-kernel|CMR1944|same-owner|spectral-certificate|certificate-bind normalized rank-two line-load energy
background-normalized-rank-three-kernel|CMR1945|same-owner|spectral-certificate|certificate-bind normalized rank-three response energy
normalized-kernel-scale-transfer|CMR1946|same-owner|local-family-equivalence|replace one inherited scale by its normalized kernel coordinates
normalized-kernel-assignment-row|CMR1947|same-owner|spectral-certificate|certificate-bind the normalized kernel through one response assignment
normalized-kernel-integer-certificate|CMR1948|same-owner|spectral-certificate|certificate-clear normalized kernel bounds to exact integers
background-normalized-kernel-endpoint|CMR1949|same-owner|finite-base-dispatch|record the normalized background kernel certificate surface
raw-fibre-background-identifier|CMR1950|same-owner|owner-witness-stock|record the exact raw fibre host background and target identifiers
raw-fibre-background-reconstruction|CMR1951|same-owner|local-family-equivalence|replace a lineage record by its reconstructed coordinate-labelled background
raw-fibre-lineage-injectivity|CMR1952|same-owner|owner-witness-stock|record injective linkage from raw fibre records to exact backgrounds
raw-fibre-response-linkage|CMR1953|same-owner|table-enumeration|enumerate exact allowed responses for every linked raw fibre
raw-fibre-kernel-linkage|CMR1954|same-owner|local-family-equivalence|replace abstract kernel rows by rows computed on the linked background
raw-fibre-lineage-corruption-audit|CMR1955|same-owner|finite-base-dispatch|record rejection of mismatched host target background or response lineage
raw-fibre-batch-completeness|CMR1956|same-owner|table-enumeration|enumerate the complete declared raw fibre lineage batch
raw-fibre-background-lineage-endpoint|CMR1957|same-owner|finite-base-dispatch|record the exact raw-fibre background linkage interface
rank-three-zero-response-definition|CMR1958|same-owner|local-family-equivalence|replace zero-response feasibility by exact response-triple enumeration
rank-three-zero-response-host-census|CMR1959|same-owner|table-enumeration|enumerate every side-four host admitting a zero-triple response
rank-three-zero-response-minimum-blockers|CMR1960|same-owner|table-enumeration|enumerate inclusion-minimal deletion blockers for all zero responses
rank-three-zero-response-blocker-generation|CMR1961|same-owner|local-family-equivalence|replace every zero-response-free host by containment of a canonical blocker
rank-three-zero-response-survivor-classification|CMR1962|same-owner|table-enumeration|enumerate the exact positive-response minima on blocker hosts
rank-three-zero-response-strict-dispatch|CMR1963|same-owner|scheduler-dispatch|scheduler selects a zero-response branch or its exact blocker alternative
rank-three-zero-response-blocker-audit|CMR1964|same-owner|finite-base-dispatch|record the complete blocker census and corruption rejection
rank-three-zero-response-endpoint|CMR1965|same-owner|finite-base-dispatch|record the exact side-four zero-response blocker atlas"""

def parse(line: str)->dict[str,Any]:
    kind,sources,owner,payment,continuation=line.split("|",4)
    return {"operation_kind":kind,"source_theorems":sources.split(","),"owner_effect":owner,"payment_class":payment,"continuation":continuation,"contract_sha256":NEW_CONTRACT_SHA256}

NEW_ENTRIES=[parse(line) for line in RAW.splitlines() if line]
CONTRACT={"schema":"prime-power-installed-operation-registry-1166/v1","base_registry_sha256":BASE_REGISTRY_SHA256,"base_operation_kind_count":BASE_OPERATION_KIND_COUNT,"base_contract_count":BASE_CONTRACT_COUNT,"base_owner_changing_kind_count":BASE_OWNER_CHANGING_KIND_COUNT,"new_contract_sha256":NEW_CONTRACT_SHA256,"new_entries":NEW_ENTRIES,"scope":"installed owner-fate compression compulsory certificates line kernels selector stability raw lineage and zero-response blocker operations through CMR1965","honesty_flags":{"owner_fate_rows_populated_all_recurrent_states":0,"compulsory_weighted_certificates_complete":0,"raw_fibre_backgrounds_cover_all_provenance":0,"rank_three_zero_blockers_globally_resolved":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0}}
EXPECTED_CONTRACT_DIGEST="29d41e186b0ab1be5b755f6c751a0cbb6ef6db89574e8f39f91ff1325e24be9f"
ALLOWED_OWNERS={"same-owner","factor-child-owner-change"}
ALLOWED_PAYMENTS={"spectral-certificate","local-family-equivalence","finite-base-dispatch","scheduler-dispatch","owner-witness-stock","table-enumeration","certificate-gluing","history-budget"}

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
        if payment=="table-enumeration": require("enumerate" in continuation,f"{path}: table")
        if payment=="certificate-gluing": require("glue" in continuation,f"{path}: gluing")
        if payment=="history-budget": require("bound" in continuation,f"{path}: history")
        owners += owner!="same-owner"; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==1166,"1166 installed kinds required"); require(owners==164,"164 owner-changing kinds required")
    return {"base_operation_kind_count":1094,"new_operation_kind_count":len(kinds),"installed_operation_kind_count":1166,"bound_contract_count":42,"owner_changing_operation_kinds":owners,"same_owner_operation_kinds":1166-owners,"new_payment_counts":payments,"registry_sha256":digest({"base":BASE_REGISTRY_SHA256,"new":entries})}

def mutation_audit()->int:
    mutations=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]["operation_kind"]),lambda x:x[0].update(contract_sha256="0"*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect="anonymous"),lambda x:x[0].update(payment_class="free"),lambda x:x[0].update(continuation=""),lambda x:x[30].update(continuation="select"),lambda x:x[2].update(continuation="weight"),lambda x:x[8].update(continuation="table"),lambda x:x[11].update(continuation="dual"),lambda x:x[44].update(continuation="episodes"),lambda x:x[0].update(owner_effect="factor-child-owner-change"),lambda x:x.pop(),lambda x:x.clear()]
    rejected=0
    for mutate in mutations:
        bad=copy.deepcopy(NEW_ENTRIES); mutate(bad)
        try: validate(bad)
        except Registry1166Error: rejected+=1
    require(rejected==len(mutations),"registry corruption accepted"); return rejected

def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,"contract digest mismatch")
    census=validate(copy.deepcopy(NEW_ENTRIES)); census["rejected_corruptions"]=mutation_audit()
    print(json.dumps({"contract_digest":contract,"census":census,"installed_transition_kind_bank_1166_exhaustive":1,"owner_fate_lineage_kernel_operations_registered":1,"installed_payment_assignment_1166_complete":1,"owner_fate_rows_populated_all_recurrent_states":0,"compulsory_weighted_certificates_complete":0,"raw_fibre_backgrounds_cover_all_provenance":0,"rank_three_zero_blockers_globally_resolved":0,"complete_labelled_recurrent_lp_strict":0,"all_labelled_recurrent_blocks_subcritical":0,"same_owner_diagonal_blocks_subcritical":0,"global_target_collateral_inequality_proved":0,"global_transition_kind_bank_exhaustive":0,"global_termination_proved":0,"actual_global_parent_rule_complete":0,"all_n_proved_by_checker":0},sort_keys=True))

if __name__=="__main__": main()
