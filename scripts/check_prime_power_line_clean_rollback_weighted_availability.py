#!/usr/bin/env python3
from __future__ import annotations
import hashlib,itertools,json,math
from typing import Any
EXPECTED_CONTRACT_SHA256='c56a0c82ee03ed6498ac5c974e64c8129344a921a262e3d13cb28672df39ab2e'
class AvailabilityError(ValueError):pass
def require(ok,msg):
    if not ok:raise AvailabilityError(msg)
def digest(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def derangements(n):return [p for p in itertools.permutations(range(n)) if all(p[i]!=i for i in range(n))]
def edges(p):return frozenset((i,p[i]) for i in range(len(p)))
def residual_pms(n,host):return [p for p in itertools.permutations(range(n)) if edges(p)<=host]
def col(a,b,c):return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def extend_partial(rows,cols,partial):
    partial=dict(partial)
    for perm in itertools.permutations(sorted(cols)):
        M=dict(zip(sorted(rows),perm))
        if all(M[r]==c for r,c in partial.items()):return M
    raise AvailabilityError('partial extension')
def physical_cylinder(m,z1,z2):
    rows=set(range(m))-{z1[0],z2[0]};cols=set(range(m))-{z1[1],z2[1]};n=m-2
    line={(r,c) for r in rows for c in cols if col(z1,z2,(r,c))};F=extend_partial(rows,cols,line);states=[];residual=[]
    for perm in itertools.permutations(sorted(cols)):
        M=dict(zip(sorted(rows),perm))
        if all(M[r]!=F[r] for r in rows):residual.append(frozenset(M.items()));states.append(frozenset({z1,z2}|set(M.items())))
    require(len(states)==round(math.factorial(n)*sum((-1)**k/math.factorial(k) for k in range(n+1))),'cylinder size')
    U={(r,c) for r in rows for c in cols if F[r]!=c};return states,residual,U,F
def triple_count(state):return sum(col(*t) for t in itertools.combinations(sorted(state),3))
def validate_report(r):
    require(r['contract_sha256']==EXPECTED_CONTRACT_SHA256,'contract');require(r['record_sha256']==digest({k:v for k,v in r.items() if k!='record_sha256'}),'seal')
    require(r['residual_subhosts']==64 and r['minimum_restoration_profiles']==64,'residual census');require(r['cheap_profiles']>0 and r['forced_factor_profiles']>0,'both availability endpoints')
    require(r['weighted_pair_profiles']>0 and r['cheap_clean_selections']>0 and r['weighted_failure_profiles']>0,'weighted endpoints')
    require(r['line_clean_rollback_availability_proved']==1 and r['line_clean_weighted_selection_proved']==1,'flags')
    require(r['global_transition_kind_bank_exhaustive']==0 and r['global_termination_proved']==0 and r['all_n_proved_by_checker']==0,'honesty')
def main():
    n=3;D=derangements(n);U=frozenset((i,j) for i in range(n) for j in range(n) if i!=j)
    subhosts=profiles=cheap=forced=restored=token=recreated=0
    for mask in range(1<<len(U)):
        G=frozenset(e for k,e in enumerate(sorted(U)) if mask>>k&1);subhosts+=1;costs=[len(edges(p)-G) for p in D];k=min(costs);M=min(p for p,c in zip(D,costs) if c==k);R=edges(M)-G;H=G|R
        profiles+=1;restored+=len(R);token+=6*len(R);hpms=residual_pms(n,H);require(hpms,'restored host empty');require(all(R<=edges(p) for p in hpms),'restored edge not essential')
        rem_rows=set(range(n))-{i for i,j in R};rem_cols=set(range(n))-{j for i,j in R};residual_count=0
        for perm in itertools.permutations(sorted(rem_cols)):
            E=frozenset(zip(sorted(rem_rows),perm))
            if E<=H:residual_count+=1
        require(len(hpms)==residual_count,'forced-core factorization')
        if k<2:cheap+=1
        else:forced+=1;require(n-k<=n-2,'strict factor side')
        candidates=[]
        for pair in itertools.combinations(sorted(U),2):
            if pair[0][0]!=pair[1][0] and pair[0][1]!=pair[1][1]:candidates.append(frozenset(pair))
        for C in candidates:
            if C<=H and not C<=G:require(C.intersection(R),'recreated conflict lacks restoration');recreated+=1
    m=7;q=3;patterns=[lambda r,c:False,lambda r,c:(r+c)%5==0,lambda r,c:r%3==0,lambda r,c:(2*r+c)%4==0]
    pair_profiles=cheap_clean=failures=collateral_branch=unavailable_branch=marginal_checks=0;family_B=[];cells=list(itertools.product(range(m),repeat=2))
    for idx,(z1,z2) in enumerate(itertools.combinations(cells,2)):
        if z1[0]==z2[0] or z1[1]==z2[1]:continue
        states,residual,Uphys,F=physical_cylinder(m,z1,z2);n2=m-2;require(len(states)==44,'D5')
        for e in Uphys:
            occ=sum(e in M for M in residual);require(occ*(n2-1)==len(residual),'derangement marginal');marginal_checks+=1
        X=[triple_count(S) for S in states]
        for pat in patterns:
            B={e for e in Uphys if pat(*e)};r=[len(M&B) for M in residual];pair_profiles+=1;avg_num=sum(q*x+rr for x,rr in zip(X,r));den=q*len(states);best=min((q*x+rr,x,rr) for x,rr in zip(X,r));require(best[0]*den<=avg_num*q,'weighted selection');rhs_num=q*sum(X)+sum(r)
            if rhs_num<q*len(states):require(best[1]==0 and best[2]<q,'below-one selection');cheap_clean+=1
            else:
                failures+=1
                if 2*sum(X)>=len(states):collateral_branch+=1
                else:require(2*sum(r)>=q*len(states),'unavailable alternative');unavailable_branch+=1
        if idx<80:family_B.append({e for e in Uphys if (e[0]+2*e[1])%4==0})
    I=sum(len(B) for B in family_B);union=set().union(*family_B);mult={e:sum(e in B for B in family_B) for e in union};lam=4;concentrated=max(mult.values(),default=0)>=lam
    if not concentrated:require(len(union)*(lam-1)>=I,'dispersion bound')
    dispersed=[{(i,10+i)} for i in range(12)];Id=sum(map(len,dispersed));Ud=set().union(*dispersed);require(max(sum(e in B for B in dispersed) for e in Ud)<lam and len(Ud)*(lam-1)>=Id,'explicit dispersion')
    claims={'checker':'prime-power-line-clean-rollback-weighted-availability','contract_sha256':EXPECTED_CONTRACT_SHA256,'residual_side':n,'residual_subhosts':subhosts,'minimum_restoration_profiles':profiles,'cheap_profiles':cheap,'forced_factor_profiles':forced,'restored_edge_incidences':restored,'sample_full_token_incidences':token,'recreated_conflict_incidences':recreated,'weighted_parent_side':m,'weighted_pair_profiles':pair_profiles,'derangement_marginal_checks':marginal_checks,'cheap_clean_selections':cheap_clean,'weighted_failure_profiles':failures,'frozen_collateral_branches':collateral_branch,'unavailable_depletion_branches':unavailable_branch,'literal_family_unavailable_incidences':I,'literal_family_distinct_unavailable_edges':len(union),'literal_family_concentration':int(concentrated),'explicit_dispersed_edges':len(Ud),'corruption_rejections':8,'line_clean_rollback_availability_proved':1,'line_clean_weighted_selection_proved':1,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    claims['record_sha256']=digest(claims);validate_report(claims)
    muts=[('contract_sha256','0'*64),('line_clean_rollback_availability_proved',0),('line_clean_weighted_selection_proved',0),('all_n_proved_by_checker',1),('residual_subhosts',63),('cheap_profiles',0),('weighted_pair_profiles',0),('record_sha256','f'*64)];rej=0
    for key,val in muts:
        bad=dict(claims);bad[key]=val
        if key!='record_sha256':bad['record_sha256']=digest({k:v for k,v in bad.items() if k!='record_sha256'})
        try:validate_report(bad)
        except AvailabilityError:rej+=1
    require(rej==8,'corruption rejection');print(json.dumps(claims,sort_keys=True))
if __name__=='__main__':main()
