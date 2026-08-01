#!/usr/bin/env python3
from __future__ import annotations
import copy,hashlib,json
from typing import Any
class Registry57Error(RuntimeError):pass
def require(ok,msg):
    if not ok:raise Registry57Error(msg)
def digest(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
BASE_REGISTRY_SHA256='2a5dfa1457e056259566eaf4e54034801f3a37ff57cd0548fbd0e117589b04b3'
BASE_OPERATION_KIND_COUNT=45
BASE_CONTRACT_COUNT=15
BASE_OWNER_CHANGING_KIND_COUNT=27
ROOT_CONTRACT='4492a6220f6b7622373a872b1521478089d5dd319482c8110b8cfe1e4ae9495d'
AVAIL_CONTRACT='c56a0c82ee03ed6498ac5c974e64c8129344a921a262e3d13cb28672df39ab2e'
NEW_ENTRIES=[
{'operation_kind':'boundary-rooted-secant-star-extraction','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR487','CMR488','CMR489'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'rooted secant-star geometry scheduler required'},
{'operation_kind':'rooted-cycle-arm-survival','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR488'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'exact route-arm incidence is owner-labelled'},
{'operation_kind':'rooted-arm-line-clean-cylinder','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR492','CMR493','CMR494'],'owner_effect':'restoration-owner-change','payment_class':'scheduler-dispatch','continuation':'line-clean availability scheduler required'},
{'operation_kind':'rooted-arm-equal-weight-bank','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR495'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'equal-weight cylinder selection scheduler required'},
{'operation_kind':'two-edge-bottleneck-pair-cylinder','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR490','CMR491','CMR496'],'owner_effect':'restoration-owner-change','payment_class':'scheduler-dispatch','continuation':'line-clean availability scheduler required'},
{'operation_kind':'compatible-pair-line-clean-cylinder','contract_sha256':ROOT_CONTRACT,'source_theorems':['CMR492','CMR493'],'owner_effect':'restoration-owner-change','payment_class':'scheduler-dispatch','continuation':'availability and collateral scheduler required'},
{'operation_kind':'line-clean-minimum-restoration','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR497','CMR498'],'owner_effect':'restoration-owner-change','payment_class':'edge-reintroduction','continuation':'minimum unavailable-edge footprint restored'},
{'operation_kind':'line-clean-forced-core-contraction','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR498','CMR499'],'owner_effect':'contraction-owner-change','payment_class':'strict-child-descent','continuation':'forced restoration core removed from residual factor'},
{'operation_kind':'line-clean-cheap-restoration','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR499','CMR500','CMR501'],'owner_effect':'restoration-owner-change','payment_class':'edge-reintroduction','continuation':'cheap restored-edge token and conflict payment'},
{'operation_kind':'line-clean-weighted-selection','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR502','CMR503','CMR504'],'owner_effect':'same-owner','payment_class':'scheduler-dispatch','continuation':'clean completion, collateral, or unavailable scheduler required'},
{'operation_kind':'line-clean-unavailable-edge-concentration','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR505','CMR506'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'one unavailable edge blocks many cylinders'},
{'operation_kind':'line-clean-unavailable-inventory-payment','contract_sha256':AVAIL_CONTRACT,'source_theorems':['CMR505','CMR506'],'owner_effect':'same-owner','payment_class':'owner-witness-stock','continuation':'distinct unavailable edges receive full-token payment'},
]
CONTRACT={'schema':'prime-power-installed-operation-registry-57/v1','base_registry_sha256':BASE_REGISTRY_SHA256,'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'base_contract_count':BASE_CONTRACT_COUNT,'new_contracts':[ROOT_CONTRACT,AVAIL_CONTRACT],'new_entries':NEW_ENTRIES,'honesty_flags':{'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}}
EXPECTED_CONTRACT_DIGEST='6ae7074762fef44c8213a1ef2dac22bc27d9b675e85085f36bc55b4dea0e11af'
def validate(entries):
    require(len(entries)==12,'twelve rooted/line-clean entries')
    kinds=set();owners=BASE_OWNER_CHANGING_KIND_COUNT;pays={};contracts=set()
    for i,e in enumerate(entries):
        p=f'entry[{i}]';k=e.get('operation_kind');require(isinstance(k,str) and k and k not in kinds,f'{p}: unique kind');kinds.add(k)
        c=e.get('contract_sha256');require(c in {ROOT_CONTRACT,AVAIL_CONTRACT},f'{p}: contract');contracts.add(c)
        src=e.get('source_theorems');require(isinstance(src,list) and src and all(isinstance(x,str) and x.startswith('CMR') for x in src),f'{p}: sources')
        o=e.get('owner_effect');pay=e.get('payment_class');cont=e.get('continuation');require(o in {'same-owner','restoration-owner-change','contraction-owner-change'},f'{p}: owner');require(pay in {'scheduler-dispatch','owner-witness-stock','edge-reintroduction','strict-child-descent'},f'{p}: payment');require(isinstance(cont,str) and cont,f'{p}: continuation')
        if pay=='scheduler-dispatch':require('scheduler' in cont,f'{p}: scheduler')
        owners+=o!='same-owner';pays[pay]=pays.get(pay,0)+1
    require(len(contracts)==2,'two new contracts');require(BASE_OPERATION_KIND_COUNT+len(kinds)==57,'57 kinds')
    return {'base_operation_kind_count':BASE_OPERATION_KIND_COUNT,'new_operation_kind_count':len(kinds),'installed_operation_kind_count':57,'bound_contract_count':BASE_CONTRACT_COUNT+2,'owner_changing_operation_kinds':owners,'same_owner_operation_kinds':57-owners,'new_payment_counts':pays,'registry_sha256':digest({'base':BASE_REGISTRY_SHA256,'new':entries})}
def mutation_audit():
    muts=[lambda x:x.append(copy.deepcopy(x[0])),lambda x:x[0].update(operation_kind=x[1]['operation_kind']),lambda x:x[0].update(contract_sha256='0'*64),lambda x:x[0].update(source_theorems=[]),lambda x:x[0].update(owner_effect='anonymous'),lambda x:x[0].update(payment_class='free'),lambda x:x[0].update(continuation=''),lambda x:x[0].update(continuation='terminal'),lambda x:x.pop()]
    r=0
    for m in muts:
        b=copy.deepcopy(NEW_ENTRIES);m(b)
        try:validate(b)
        except Registry57Error:r+=1
    require(r==len(muts),'mutation accepted');return r
def main():
    cd=digest(CONTRACT);require(cd==EXPECTED_CONTRACT_DIGEST,'contract digest');c=validate(copy.deepcopy(NEW_ENTRIES));c['rejected_corruptions']=mutation_audit()
    out={'contract_digest':cd,'census':c,'installed_transition_kind_bank_57_exhaustive':1,'rooted_line_clean_operations_registered':1,'installed_payment_assignment_57_complete':1,'all_owner_operations_proved':0,'all_scheduler_operations_proved':0,'all_restoration_operations_proved':0,'all_construction_ancestry_proved':0,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
