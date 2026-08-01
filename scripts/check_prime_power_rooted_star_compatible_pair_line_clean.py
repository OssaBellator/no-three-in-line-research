#!/usr/bin/env python3
from __future__ import annotations
import hashlib,itertools,json,math
from typing import Any
EXPECTED_CONTRACT_SHA256='4492a6220f6b7622373a872b1521478089d5dd319482c8110b8cfe1e4ae9495d'
class RootPairError(ValueError):pass
def require(ok,msg):
    if not ok:raise RootPairError(msg)
def digest(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def col(a,b,c):return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def clean(points):return not any(col(*t) for t in itertools.combinations(points,3))
def derangement(n):return round(math.factorial(n)*sum((-1)**k/math.factorial(k) for k in range(n+1)))
def simple_cycles_containing(m,a):
    u,w=a;others=[v for v in range(m) if v not in {u,w}];out=[]
    for r in range(len(others)+1):
        for mid in itertools.permutations(others,r):out.append((u,w)+mid)
    return out
def flip(base,cycle):
    p=list(base)
    for i,v in enumerate(cycle):p[v]=base[cycle[(i+1)%len(cycle)]]
    return tuple(p)
def extend_partial(rows,cols,partial):
    rows=tuple(sorted(rows));cols=tuple(sorted(cols));partial=dict(partial)
    require(len(set(partial))==len(partial) and len(set(partial.values()))==len(partial),'partial matching')
    for perm in itertools.permutations(cols):
        M=dict(zip(rows,perm))
        if all(M[r]==c for r,c in partial.items()):return M
    raise RootPairError('partial cannot extend')
def cylinder(m,z1,z2):
    require(z1[0]!=z2[0] and z1[1]!=z2[1],'pair incompatible')
    rows=set(range(m))-{z1[0],z2[0]};cols=set(range(m))-{z1[1],z2[1]}
    line_cells={(r,c) for r in rows for c in cols if col(z1,z2,(r,c))}
    require(len({r for r,c in line_cells})==len(line_cells) and len({c for r,c in line_cells})==len(line_cells),'line cells not partial matching')
    F=extend_partial(rows,cols,line_cells);states=[]
    for perm in itertools.permutations(sorted(cols)):
        M=dict(zip(sorted(rows),perm))
        if all(M[r]!=F[r] for r in rows):
            pts={z1,z2}|set(M.items());states.append(tuple(sorted(pts)))
            require(all(x not in pts for x in line_cells),'line cell survived')
            require(not any(col(z1,z2,x) for x in pts-{z1,z2}),'rank-two line triple')
    require(len(states)==derangement(m-2),'derangement count')
    return states,len(line_cells)
def validate_report(r):
    require(r['contract_sha256']==EXPECTED_CONTRACT_SHA256,'contract')
    require(r['record_sha256']==digest({k:v for k,v in r.items() if k!='record_sha256'}),'seal')
    require(r['clean_base_matchings']>0 and r['rooted_star_centres']>0 and r['rooted_arms']>0,'rooted coverage')
    require(r['compatible_pair_cylinders']>0 and r['cylinder_state_occurrences']>0,'cylinder coverage')
    require(r['rooted_star_pair_cylinder_ancestry_proved']==1 and r['universal_pair_line_clean_cylinder_exact']==1,'flags')
    require(r['global_transition_kind_bank_exhaustive']==0 and r['global_termination_proved']==0 and r['all_n_proved_by_checker']==0,'honesty')
def main():
    m=5;clean_bases=centres=arms=survival_checks=arm_cylinders=arm_states=0
    for p in itertools.permutations(range(m)):
        P={(i,p[i]) for i in range(m)}
        if not clean(P):continue
        clean_bases+=1;inv={p[i]:i for i in range(m)}
        for a in itertools.product(range(m),repeat=2):
            if a in P:continue
            rooted=[]
            for x,y in itertools.combinations(sorted(P),2):
                if col(a,x,y):rooted.append((x,y))
            if not rooted:continue
            centres+=1;arms+=len(rooted);require(len(rooted)<=m//2,'star bound')
            outside=[set(xy) for xy in rooted]
            for A,B in itertools.combinations(outside,2):require(not A.intersection(B),'rooted outside pairs overlap')
            arc=(a[0],inv[a[1]]);require(arc[0]!=arc[1],'boundary cell is matching edge')
            cycles=simple_cycles_containing(m,arc)
            for x,y in rooted:
                xi=x[0];yi=y[0]
                for cyc in cycles:
                    state={(i,t) for i,t in enumerate(flip(p,cyc))};present={a,x,y}<=state
                    require(present==(xi not in cyc and yi not in cyc),'cycle-arm presence');survival_checks+=1
                z=min(x,y);states,_=cylinder(m,a,z);arm_cylinders+=1;arm_states+=len(states);other=y if z==x else x
                for state in states:
                    S=set(state);require(a in S and z in S and other not in S,'rooted arm not destroyed')
    pair_cylinders=pair_states=line_cells=0;cells=list(itertools.product(range(m),repeat=2))
    for z1,z2 in itertools.combinations(cells,2):
        if z1[0]==z2[0] or z1[1]==z2[1]:continue
        states,l=cylinder(m,z1,z2);pair_cylinders+=1;pair_states+=len(states);line_cells+=l
    arc_pairs=set()
    for r in range(2,m+1):
        for cyc in itertools.permutations(range(m),r):
            if min(cyc)!=cyc[0]:continue
            arcs_c=[(cyc[i],cyc[(i+1)%r]) for i in range(r)]
            for a,b in itertools.combinations(arcs_c,2):arc_pairs.add(tuple(sorted((a,b))))
    bottleneck_states=0
    for a,b in arc_pairs:
        require(a[0]!=b[0] and a[1]!=b[1],'cycle arcs incompatible');states,_=cylinder(m,a,b);bottleneck_states+=len(states)
    claims={'checker':'prime-power-rooted-star-compatible-pair-line-clean','contract_sha256':EXPECTED_CONTRACT_SHA256,'side':m,'clean_base_matchings':clean_bases,'rooted_star_centres':centres,'rooted_arms':arms,'rooted_cycle_arm_checks':survival_checks,'rooted_arm_cylinders':arm_cylinders,'rooted_arm_cylinder_states':arm_states,'compatible_pair_cylinders':pair_cylinders,'cylinder_state_occurrences':pair_states,'residual_line_cell_incidences':line_cells,'cycle_bottleneck_compatible_pairs':len(arc_pairs),'cycle_bottleneck_cylinder_states':bottleneck_states,'corruption_rejections':8,'rooted_star_pair_cylinder_ancestry_proved':1,'universal_pair_line_clean_cylinder_exact':1,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    claims['record_sha256']=digest(claims);validate_report(claims)
    muts=[('contract_sha256','0'*64),('rooted_star_pair_cylinder_ancestry_proved',0),('universal_pair_line_clean_cylinder_exact',0),('all_n_proved_by_checker',1),('rooted_arms',0),('compatible_pair_cylinders',0),('cylinder_state_occurrences',0),('record_sha256','f'*64)]
    rej=0
    for k,v in muts:
        bad=dict(claims);bad[k]=v
        if k!='record_sha256':bad['record_sha256']=digest({x:y for x,y in bad.items() if x!='record_sha256'})
        try:validate_report(bad)
        except RootPairError:rej+=1
    require(rej==8,'corruptions');print(json.dumps(claims,sort_keys=True))
if __name__=='__main__':main()
