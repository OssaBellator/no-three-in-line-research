#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1165."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
from selected_scheduler_registry_entries_a import ENTRIES as ENTRIES_A
from selected_scheduler_registry_entries_b import ENTRIES as ENTRIES_B
class Registry454Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise Registry454Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
BASE_REGISTRY_SHA256='73991d389765adee57e8665c41533a7b6e2c71653312366d8b4ce237635bf814'
BASE_OPERATION_KIND_COUNT=392
BASE_CONTRACT_COUNT=28
BASE_OWNER_CHANGING_KIND_COUNT=130
NEW_CONTRACT_SHA256='f10e632f119fdd56a830ddeb8b9d15d18769f59e703d0dad7a59f243a7c8246c'
NEW_ENTRIES=[*ENTRIES_A,*ENTRIES_B]
CONTRACT={'schema':'prime-power-installed-operation-registry-454/v1','base_registry_sha256':BASE_REGISTRY_SHA256,
 'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'base_contract_count':BASE_CONTRACT_COUNT,
 'base_owner_changing_kind_count':BASE_OWNER_CHANGING_KIND_COUNT,'new_contract_sha256':NEW_CONTRACT_SHA256,
 'new_entries':NEW_ENTRIES,'honesty_flags':{'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
 'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}}
EXPECTED_CONTRACT_DIGEST='63034b7d3af319de121a26ea863309808de0e3b06f0359448be9afed3e73f40f'
ALLOWED_OWNERS={'same-owner','host-owner-change','factor-child-owner-change','restoration-owner-change'}
ALLOWED_PAYMENTS={'local-family-restriction','factor-product-dispatch','strict-child-descent','cycle-erasure',
 'history-budget','scheduler-dispatch','owner-witness-stock','strict-factor-contraction','strict-improvement',
 'branch-cover-dispatch','edge-reintroduction','local-family-equivalence','finite-base-dispatch'}
def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==62,'sixty-two operations required')
    kinds=set(); owner_changes=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for i,x in enumerate(entries):
        p=f'entry[{i}]'; kind=x.get('operation_kind')
        require(isinstance(kind,str) and kind and kind not in kinds,f'{p}: unique kind'); kinds.add(kind)
        require(x.get('contract_sha256')==NEW_CONTRACT_SHA256,f'{p}: contract')
        sources=x.get('source_theorems'); require(isinstance(sources,list) and sources and all(isinstance(s,str) and s.startswith('CMR') for s in sources),f'{p}: sources')
        owner=x.get('owner_effect'); payment=x.get('payment_class'); continuation=x.get('continuation')
        require(owner in ALLOWED_OWNERS,f'{p}: owner'); require(payment in ALLOWED_PAYMENTS,f'{p}: payment')
        require(isinstance(continuation,str) and continuation,f'{p}: continuation')
        if payment=='scheduler-dispatch': require('scheduler' in continuation,f'{p}: scheduler')
        if payment=='local-family-restriction': require(owner in {'same-owner','host-owner-change'} and any(w in continuation for w in ('restrict','remove','retain')),f'{p}: restriction')
        if payment=='strict-factor-contraction': require(owner=='factor-child-owner-change' and ('contract' in continuation or 'contraction' in continuation),f'{p}: contraction')
        if payment=='strict-child-descent': require(owner=='factor-child-owner-change' and any(w in continuation for w in ('continue','descent','tree')),f'{p}: descent')
        if payment=='edge-reintroduction': require(owner in {'host-owner-change','restoration-owner-change'} and any(w in continuation for w in ('return','restore','redelete')),f'{p}: reintroduction')
        if payment=='finite-base-dispatch': require('base' in continuation,f'{p}: base dispatch')
        owner_changes += owner!='same-owner'; payments[payment]=payments.get(payment,0)+1
    total=BASE_OPERATION_KIND_COUNT+len(kinds); require(total==454,'454 kinds required')
    require(owner_changes==143,'143 owner-changing kinds required')
    return {'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'new_operation_kind_count':len(kinds),
      'installed_operation_kind_count':total,'bound_contract_count':BASE_CONTRACT_COUNT+1,
      'owner_changing_operation_kinds':owner_changes,'same_owner_operation_kinds':total-owner_changes,
      'new_payment_counts':payments,'registry_sha256':digest({'base':BASE_REGISTRY_SHA256,'new':entries})}
def mutation_audit()->int:
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]['operation_kind']),
      lambda x:x[0].update(contract_sha256='0'*64),lambda x:x[0].update(source_theorems=[]),
      lambda x:x[0].update(owner_effect='anonymous'),lambda x:x[0].update(payment_class='free'),
      lambda x:x[0].update(continuation=''),lambda x:x[7].update(continuation='route'),
      lambda x:x[15].update(owner_effect='same-owner'),lambda x:x[31].update(owner_effect='same-owner'),
      lambda x:x[53].update(owner_effect='same-owner'),lambda x:x.pop()]
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(NEW_ENTRIES); mut(bad)
        try: validate(bad)
        except Registry454Error: rejected+=1
    require(rejected==len(muts),'corruption accepted'); return rejected
def main()->None:
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,'contract digest')
    census=validate(copy.deepcopy(NEW_ENTRIES)); census['rejected_corruptions']=mutation_audit()
    print(json.dumps({'contract_digest':contract,'census':census,'installed_transition_kind_bank_454_exhaustive':1,
      'selected_scheduler_terminal_wall_operations_registered':1,'installed_payment_assignment_454_complete':1,
      'all_owner_operations_proved':0,'all_scheduler_operations_proved':0,'all_restoration_operations_proved':0,
      'all_construction_ancestry_proved':0,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
      'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0},sort_keys=True))
if __name__=='__main__': main()
