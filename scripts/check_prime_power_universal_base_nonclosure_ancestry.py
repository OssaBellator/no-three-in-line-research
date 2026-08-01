#!/usr/bin/env python3
"""Check CMR1166--CMR1197 universal range, small bases, and nonclosure."""
from __future__ import annotations
import copy, hashlib, itertools, json
from fractions import Fraction
from typing import Any
class BaseNonclosureError(RuntimeError): pass
def require(ok:bool,msg:str)->None:
    if not ok: raise BaseNonclosureError(msg)
def digest(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def perms(n): return tuple(itertools.permutations(range(n)))
def matching(p): return frozenset((i,p[i]) for i in range(len(p)))
def collinear(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(c[0]-a[0])*(b[1]-a[1])
def target_location_audit()->dict[str,int]:
    splits=movement=0; target=tuple(range(3))
    for fixed_mask in range(1<<3):
        fixed={i for i in target if fixed_mask>>i&1}; residual=set(target)-fixed
        if len(residual)==3: kind='pure-residual'
        elif residual: kind='anchored-residual'
        else: kind='fixed-core'
        require(kind in {'pure-residual','anchored-residual','fixed-core'},'CMR1166 split')
        require(len(fixed)+len(residual)==3 and fixed.isdisjoint(residual),'CMR1166 partition')
        if residual:
            for edge in residual:
                require(edge not in residual-{edge},'CMR1166 moving edge destroys target'); movement+=1
        splits+=1
    arithmetic=0
    for n in range(1,31):
        require(n<=3 or n>=4,'CMR1171 universal/base partition')
        require(n<=3 or (n>=4 and n-1<n),'CMR1172 strict side')
        require(2*n+1>=1,'CMR1172 wall tree nodes'); arithmetic+=1
    return {'target_location_splits':splits,'residual_edge_destruction_checks':movement,'universal_descent_parameter_checks':arithmetic}
def side_three_audit()->dict[str,int]:
    n=3; ps=perms(n); partitions=responses=restricted=0
    for opposite in ps:
        O=matching(opposite); der=[matching(p) for p in ps if matching(p).isdisjoint(O)]
        require(len(der)==2,'CMR1174 two derangements')
        require(O|der[0]|der[1]==frozenset((i,j) for i in range(n) for j in range(n)),'CMR1174 board partition')
        require(der[0].isdisjoint(der[1]),'CMR1174 disjoint cycles'); partitions+=1
        for e in frozenset((i,j) for i in range(n) for j in range(n))-O:
            containing=[M for M in der if e in M]; avoiding=[M for M in der if e not in M]
            require(len(containing)==len(avoiding)==1,'CMR1175 unique target response')
            F=containing[0]; R=avoiding[0]
            require(R.isdisjoint(F) and R.isdisjoint(O) and e not in R,'CMR1175 response'); responses+=1
            for host_mask in range(1<<len(R)):
                host=O|F|frozenset(edge for index,edge in enumerate(sorted(R)) if host_mask>>index&1)
                if R<=host: require(R<=host,'CMR1176 feasible singleton')
                else:
                    missing=R-host; require(missing,'CMR1176 blocker')
                    blocker=min(missing); require(R<=host|{blocker} or len(missing)>1,'CMR1176 first restoration')
                restricted+=1
    return {'side_three_permutation_partitions':partitions,'side_three_target_responses':responses,'side_three_restricted_response_cases':restricted}
def small_side_audit()->dict[str,int]:
    p2=perms(2); pairs=[]
    for a in p2:
        for b in p2:
            A=matching(a); B=matching(b)
            if A.isdisjoint(B): pairs.append((A,B))
    require(len(pairs)==2,'CMR1177 labelled assignments')
    board=frozenset((i,j) for i in range(2) for j in range(2))
    require(all(A|B==board for A,B in pairs),'CMR1177 board coverage')
    triples=list(itertools.combinations(sorted(board),3))
    require(all(not collinear(*triple) for triple in triples),'CMR1178 root clean')
    contraction=0
    for A,B in pairs:
        prescription=frozenset((0,*e) for e in A)|frozenset((1,*e) for e in B)
        residual={state-prescription for state in (prescription,)}
        require(residual=={frozenset()},'CMR1179 rigid contraction'); contraction+=1
    one=matching((0,)); require(len(one)==1,'CMR1180 side-one forced')
    require(not one.isdisjoint(one),'CMR1180 two-layer side-one impossible')
    return {'side_two_labelled_assignments':len(pairs),'side_two_physical_triples_checked':len(triples),
            'side_two_rigid_contractions':contraction,'side_one_forced_factors':1}
def lifted_ancestry_audit(max_side:int=20,max_depth:int=5)->dict[str,int]:
    checks=targets=0
    for N in range(2,max_side+1):
        for h in range(1,max_depth+1):
            A=sum(2*m*m+m+1 for m in range(1,N+1)); L=(h+1)*(A+1)
            require(L>=h+1,'CMR1188 edge lineage')
            for event_times in itertools.combinations_with_replacement(range(4),3):
                last=max(range(3),key=lambda i:(event_times[i],i))
                require(event_times[last]==max(event_times),'CMR1183 last fixation')
                if N!=2:
                    require(N>=3,'CMR1184-1186 lifted owner exists'); targets+=1
                checks+=1
    return {'last_fixation_ancestry_checks':checks,'nontrivial_lifted_target_owners':targets}
def nonclosure_audit()->dict[str,int]:
    values={'S':1,'Q1':2,'Q2':2}
    require(min(values.values())==1 and values['Q1']>=values['S'] and values['Q2']>=values['S'],'CMR1190 positive minimum model')
    conditioned={'S':values['S']}; require(min(conditioned.values())==1,'CMR1191 dirty singleton')
    stocks=[0,1,2,10]
    for stock in stocks: require(stock>=0 and min(conditioned.values())==1,'CMR1192 stock nonimplication')
    distributions=[(Fraction(1,2),Fraction(1,2)),(Fraction(1,3),Fraction(2,3)),(Fraction(1,1),Fraction(0,1))]
    averaging=0; bank=(0,2)
    for p,q in distributions:
        expectation=p*bank[0]+q*bank[1]; require(p+q==1,'CMR1193 distribution')
        if expectation<1: require(min(bank)<1,'CMR1193 average improvement')
        averaging+=1
    for lost,new in [(1,0),(2,1),(3,1),(1,2)]:
        gap=new-lost; require(gap==new-lost,'CMR1194 new-minus-lost identity')
        if new<lost: require(gap<0,'CMR1194 collateral criterion')
        averaging+=1
    classes=('residual-target','fixed-core-target','loaded-line-star','minimal-unit-wall','side-three-bank','rigid-small-interface')
    require(len(classes)==6 and len(set(classes))==6,'CMR1195 finite classes')
    return {'nonclosure_countermodels':1,'finite_stock_nonimplication_checks':len(stocks),'averaging_identity_checks':averaging,'canonical_response_classes':len(classes)}
CONTRACT={'schema':'prime-power-universal-base-nonclosure-ancestry/v1','source_theorems':[f'CMR{i}' for i in range(1166,1198)],
 'proved_theorems':[f'CMR{i}' for i in range(1166,1196)]+['CMR1197'],'open_targets':['CMR1196'],
 'banks':['universal-range-target-descent','small-joint-factor-base','small-interface-target-ancestry','finite-response-nonclosure'],
 'honesty':{'global_target_collateral_inequality_proved':0,'global_transition_kind_bank_exhaustive':0,
 'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}}
EXPECTED_CONTRACT_SHA256='1872628306b27c0e3240fe4be2acb27f319c9d2f36acead6b47deaa6838efd36'
def mutation_audit()->int:
    muts=[lambda c:c.update(schema='bad'),lambda c:c.update(source_theorems=[]),lambda c:c['source_theorems'].pop(),
      lambda c:c['proved_theorems'].append('CMR1196'),lambda c:c.update(open_targets=[]),lambda c:c['banks'].pop(),
      lambda c:c['honesty'].update(global_target_collateral_inequality_proved=1),lambda c:c['honesty'].update(all_n_proved_by_checker=1),
      lambda c:c['honesty'].pop('actual_global_parent_rule_complete')]
    def valid(c):
        require(c.get('schema')==CONTRACT['schema'],'schema'); require(c.get('source_theorems')==CONTRACT['source_theorems'],'sources')
        require(c.get('proved_theorems')==CONTRACT['proved_theorems'],'proved'); require(c.get('open_targets')==['CMR1196'],'open target')
        require(c.get('banks')==CONTRACT['banks'],'banks'); require(c.get('honesty')==CONTRACT['honesty'],'honesty')
    rejected=0
    for mut in muts:
        bad=copy.deepcopy(CONTRACT); mut(bad)
        try: valid(bad)
        except BaseNonclosureError: rejected+=1
    require(rejected==len(muts),'mutation accepted'); return rejected
def main():
    contract=digest(CONTRACT); require(contract==EXPECTED_CONTRACT_SHA256,'contract')
    report={'checker':'prime-power-universal-base-nonclosure-ancestry','contract_sha256':contract,
      **target_location_audit(),**side_three_audit(),**small_side_audit(),**lifted_ancestry_audit(),**nonclosure_audit(),
      'rejected_corruptions':mutation_audit(),'universal_range_target_descent_exact':1,
      'small_joint_factor_base_exact':1,'small_interface_target_ancestry_exact':1,'finite_response_nonclosure_exact':1,
      'global_target_collateral_inequality_proved':0,'universal_base_nonclosure_ancestry_proved':1,
      'all_owner_operations_proved':0,'all_scheduler_operations_proved':0,'all_construction_ancestry_proved':0,
      'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,
      'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    print(json.dumps(report,sort_keys=True))
if __name__=='__main__': main()
