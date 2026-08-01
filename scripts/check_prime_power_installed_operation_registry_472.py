#!/usr/bin/env python3
"""Extend the installed operation registry through CMR1197."""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
class Registry472Error(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise Registry472Error(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
BASE_REGISTRY_SHA256='9396a9ecce73ffdc9e673fcfb33b1317149acfd92c9790237f29717d0347ce35'
BASE_OPERATION_KIND_COUNT=454
BASE_CONTRACT_COUNT=29
BASE_OWNER_CHANGING_KIND_COUNT=143
NEW_CONTRACT_SHA256='1872628306b27c0e3240fe4be2acb27f319c9d2f36acead6b47deaa6838efd36'
def e(kind,sources,owner,payment,continuation):
    return {'operation_kind':kind,'source_theorems':sources,'owner_effect':owner,'payment_class':payment,
            'continuation':continuation,'contract_sha256':NEW_CONTRACT_SHA256}
NEW_ENTRIES=[
 e('universal-target-location-trichotomy',['CMR1166'],'same-owner','scheduler-dispatch','scheduler classifies a dirty target as residual anchored or fixed-core'),
 e('residual-target-degree-two-response-bank',['CMR1167'],'same-owner','scheduler-dispatch','scheduler builds the current residual full-layer target-destroying bank'),
 e('fixed-core-target-lifted-owner-response',['CMR1168'],'same-owner','scheduler-dispatch','scheduler returns a fixed target to its stored lifted owner and response bank'),
 e('universal-target-blocked-unit-wall',['CMR1169'],'factor-child-owner-change','strict-child-descent','continue a completely blocked target bank through strict unit-wall children'),
 e('universal-target-executable-currency-response',['CMR1170'],'same-owner','scheduler-dispatch','scheduler spends finite currency or accepts improvement for a feasible response'),
 e('universal-dirty-owner-nonterminal-dispatch',['CMR1171','CMR1173'],'same-owner','scheduler-dispatch','scheduler routes every dirty universal-range owner to response descent or finite base'),
 e('universal-target-strict-descent-tree',['CMR1172'],'factor-child-owner-change','strict-child-descent','continue through finite child-routing and blocker-wall descent'),
 e('side-three-singleton-target-response',['CMR1174','CMR1175'],'same-owner','scheduler-dispatch','scheduler uses the unique side-three singleton response matching'),
 e('side-three-blocked-response-unit-wall',['CMR1176'],'factor-child-owner-change','strict-child-descent','continue a blocked singleton response through its one-edge unit wall'),
 e('side-two-root-clean-base',['CMR1177','CMR1178'],'same-owner','finite-base-dispatch','dispatch the rigid clean side-two root to the finite base ledger'),
 e('side-two-rigid-interface-contraction',['CMR1179'],'factor-child-owner-change','strict-factor-contraction','contract the selected rigid side-two block into the induced interface'),
 e('side-one-forced-edge-contraction',['CMR1180'],'factor-child-owner-change','strict-factor-contraction','contract the unique one-layer side-one forced edge'),
 e('last-fixation-target-owner-selection',['CMR1182','CMR1183'],'same-owner','owner-witness-stock','select the unique backward lineage and canonical last-active target edge'),
 e('small-owner-nearest-larger-ancestor-lift',['CMR1184','CMR1185','CMR1186'],'same-owner','owner-witness-stock','lift a small fixed-interface target to its nearest side-at-least-three bank owner'),
 e('lifted-small-interface-bank-response',['CMR1187'],'same-owner','scheduler-dispatch','scheduler normalizes the lifted response through improvement loss surplus wall or exit'),
 e('lifted-target-owner-lineage-stock',['CMR1188'],'same-owner','history-budget','bound the canonical lifted owner along one physical edge lineage'),
 e('small-interface-target-endpoint',['CMR1189'],'same-owner','scheduler-dispatch','scheduler routes every dirty fixed small-interface target to its lifted bank owner'),
 e('finite-response-canonical-class-reduction',['CMR1195','CMR1197'],'same-owner','local-family-equivalence','remove duplicate routing rollback and blocker data while preserving the minimum-zero question'),
]
CONTRACT={'schema':'prime-power-installed-operation-registry-472/v1','base_registry_sha256':BASE_REGISTRY_SHA256,
 'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'base_contract_count':BASE_CONTRACT_COUNT,
 'base_owner_changing_kind_count':BASE_OWNER_CHANGING_KIND_COUNT,'new_contract_sha256':NEW_CONTRACT_SHA256,
 'new_entries':NEW_ENTRIES,'open_target':'CMR1196','honesty_flags':{'global_target_collateral_inequality_proved':0,
 'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,
 'all_n_proved_by_checker':0}}
EXPECTED_CONTRACT_DIGEST='83c69c981fbccb8ab8634a2a767032c6a44384cb30afafbf27e883738baf0232'
ALLOWED_OWNERS={'same-owner','factor-child-owner-change'}
ALLOWED_PAYMENTS={'scheduler-dispatch','strict-child-descent','finite-base-dispatch','strict-factor-contraction',
                  'owner-witness-stock','history-budget','local-family-equivalence'}
def validate(entries:list[dict[str,Any]])->dict[str,Any]:
    require(len(entries)==18,'eighteen operations required')
    kinds=set(); owners=BASE_OWNER_CHANGING_KIND_COUNT; payments={}
    for i,x in enumerate(entries):
        p=f'entry[{i}]'; kind=x.get('operation_kind')
        require(isinstance(kind,str) and kind and kind not in kinds,f'{p}: kind'); kinds.add(kind)
        require(x.get('contract_sha256')==NEW_CONTRACT_SHA256,f'{p}: contract')
        src=x.get('source_theorems'); require(isinstance(src,list) and src and all(s.startswith('CMR') for s in src),f'{p}: sources')
        owner=x.get('owner_effect'); payment=x.get('payment_class'); cont=x.get('continuation')
        require(owner in ALLOWED_OWNERS,f'{p}: owner'); require(payment in ALLOWED_PAYMENTS,f'{p}: payment')
        require(isinstance(cont,str) and cont,f'{p}: continuation')
        if payment=='scheduler-dispatch': require('scheduler' in cont,f'{p}: scheduler')
        if payment=='strict-child-descent': require(owner=='factor-child-owner-change' and 'continue' in cont,f'{p}: child descent')
        if payment=='strict-factor-contraction': require(owner=='factor-child-owner-change' and 'contract' in cont,f'{p}: contraction')
        if payment=='finite-base-dispatch': require('base' in cont,f'{p}: finite base')
        owners+=owner!='same-owner'; payments[payment]=payments.get(payment,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==472,'472 kinds required')
    require(owners==148,'148 owner-changing kinds required')
    return {'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'new_operation_kind_count':len(kinds),
      'installed_operation_kind_count':472,'bound_contract_count':BASE_CONTRACT_COUNT+1,
      'owner_changing_operation_kinds':owners,'same_owner_operation_kinds':472-owners,
      'new_payment_counts':payments,'registry_sha256':digest({'base':BASE_REGISTRY_SHA256,'new':entries})}
def mutation_audit():
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]['operation_kind']),
      lambda x:x[0].update(contract_sha256='0'*64),lambda x:x[0].update(source_theorems=[]),
      lambda x:x[0].update(owner_effect='anonymous'),lambda x:x[0].update(payment_class='free'),
      lambda x:x[0].update(continuation=''),lambda x:x[0].update(continuation='classify'),
      lambda x:x[3].update(owner_effect='same-owner'),lambda x:x[10].update(owner_effect='same-owner'),lambda x:x.pop()]
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(NEW_ENTRIES); mut(bad)
        try: validate(bad)
        except Registry472Error: rejected+=1
    require(rejected==len(muts),'corruption accepted'); return rejected
def main():
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_DIGEST,'contract')
    census=validate(copy.deepcopy(NEW_ENTRIES)); census['rejected_corruptions']=mutation_audit()
    print(json.dumps({'contract_digest':contract,'census':census,'installed_transition_kind_bank_472_exhaustive':1,
      'universal_base_operations_registered':1,'installed_payment_assignment_472_complete':1,
      'global_target_collateral_inequality_proved':0,'all_owner_operations_proved':0,'all_scheduler_operations_proved':0,
      'all_construction_ancestry_proved':0,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
      'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0},sort_keys=True))
if __name__=='__main__': main()
