#!/usr/bin/env python3
from __future__ import annotations
import copy,hashlib,json
from typing import Any
class Registry45Error(RuntimeError):pass
def require(ok,msg):
    if not ok:raise Registry45Error(msg)
def digest(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
BASE_REGISTRY_SHA256='aa7b4d1b0d7c1e7c76b8e22e547c132db5ee848c633cfc5cb45b41a76e522144'
BASE_OPERATION_KIND_COUNT=39
BASE_CONTRACT_COUNT=14
BASE_OWNER_CHANGING_KIND_COUNT=27
NEW_CONTRACT_SHA256='7089d93aa893b506e3e9d183d29869961c5e4fc59a25547d1a0c7e5607f084be'
NEW_ENTRIES=[
{'operation_kind':'mixed-cycle-boundary-fan-extraction','source_theorems':['CMR477','CMR478','CMR479'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'theta-fan or small-return-cut scheduler required'},
{'operation_kind':'mixed-cycle-small-return-cut','source_theorems':['CMR479'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'finite cut edges meet every return route'},
{'operation_kind':'mixed-cycle-two-edge-bottleneck','source_theorems':['CMR480','CMR481'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'fixed boundary-edge pair enters geometric concentration scheduler'},
{'operation_kind':'theta-fan-cycle-flip','source_theorems':['CMR478','CMR479','CMR482'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'one zero-cost theta state enters conflict scheduler'},
{'operation_kind':'theta-fan-private-edge-payment','source_theorems':['CMR482','CMR483','CMR484','CMR485','CMR486'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'distinct private entering edges receive full-token payment'},
{'operation_kind':'theta-fan-rooted-conflict-dispatch','source_theorems':['CMR484','CMR486'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'boundary-rooted conflict enters rooted geometry scheduler'},
]
for e in NEW_ENTRIES:e['contract_sha256']=NEW_CONTRACT_SHA256
CONTRACT={'schema':'prime-power-installed-operation-registry-45/v1','base_registry_sha256':BASE_REGISTRY_SHA256,'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'base_contract_count':BASE_CONTRACT_COUNT,'new_contract_sha256':NEW_CONTRACT_SHA256,'new_entries':NEW_ENTRIES,'honesty_flags':{'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}}
EXPECTED_CONTRACT_DIGEST='414d203835f3d1677bf20e7e1a0d02872653a56608e02b2fe7ab8d0aa49da4ae'
def validate(entries):
    require(len(entries)==6,'six fan/payment entries')
    kinds=set();owner_changes=BASE_OWNER_CHANGING_KIND_COUNT;payments={}
    for i,e in enumerate(entries):
        p=f'entry[{i}]';kind=e.get('operation_kind');require(isinstance(kind,str) and kind and kind not in kinds,f'{p}: unique kind');kinds.add(kind)
        require(e.get('contract_sha256')==NEW_CONTRACT_SHA256,f'{p}: contract')
        src=e.get('source_theorems');require(isinstance(src,list) and src and all(isinstance(x,str) and x.startswith('CMR') for x in src),f'{p}: sources')
        require(e.get('owner_effect')=='same-owner',f'{p}: owner')
        pay=e.get('payment_class');cont=e.get('continuation');require(pay in {'scheduler-dispatch','owner-witness-stock'},f'{p}: payment');require(isinstance(cont,str) and cont,f'{p}: continuation')
        if pay=='scheduler-dispatch':require('scheduler' in cont,f'{p}: scheduler')
        payments[pay]=payments.get(pay,0)+1
    require(BASE_OPERATION_KIND_COUNT+len(kinds)==45,'45 kinds')
    return {'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'new_operation_kind_count':len(kinds),'installed_operation_kind_count':45,'bound_contract_count':BASE_CONTRACT_COUNT+1,'owner_changing_operation_kinds':owner_changes,'same_owner_operation_kinds':45-owner_changes,'new_payment_counts':payments,'registry_sha256':digest({'base':BASE_REGISTRY_SHA256,'new':entries})}
def mutation_audit():
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]['operation_kind']),lambda x:x[0].update(contract_sha256='0'*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect='anonymous'),lambda x:x[0].update(payment_class='free'),lambda x:x[0].update(continuation=''),lambda x:x[0].update(continuation='terminal'),lambda x:x.pop()]
    r=0
    for m in muts:
        b=copy.deepcopy(NEW_ENTRIES);m(b)
        try:validate(b)
        except Registry45Error:r+=1
    require(r==len(muts),'mutation accepted');return r
def main():
    cd=digest(CONTRACT);require(cd==EXPECTED_CONTRACT_DIGEST,'contract digest')
    c=validate(copy.deepcopy(NEW_ENTRIES));c['rejected_corruptions']=mutation_audit()
    out={'contract_digest':cd,'census':c,'installed_transition_kind_bank_45_exhaustive':1,'mixed_cycle_theta_operations_registered':1,'installed_payment_assignment_45_complete':1,'all_owner_operations_proved':0,'all_scheduler_operations_proved':0,'all_restoration_operations_proved':0,'all_construction_ancestry_proved':0,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
