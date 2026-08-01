#!/usr/bin/env python3
from __future__ import annotations
import hashlib,itertools,json
from collections import deque
from typing import Any
EXPECTED_CONTRACT_SHA256='7089d93aa893b506e3e9d183d29869961c5e4fc59a25547d1a0c7e5607f084be'
class FanError(ValueError):pass
def require(ok,msg):
    if not ok: raise FanError(msg)
def digest(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sccs(n,arcs):
    adj=[[] for _ in range(n)];radj=[[] for _ in range(n)]
    for a,b in arcs:adj[a].append(b);radj[b].append(a)
    seen=[0]*n;order=[]
    def dfs(v):
        seen[v]=1
        for w in adj[v]:
            if not seen[w]:dfs(w)
        order.append(v)
    for v in range(n):
        if not seen[v]:dfs(v)
    comp=[-1]*n;comps=[]
    def rdfs(v,c):
        comp[v]=c;comps[c].append(v)
        for w in radj[v]:
            if comp[w]<0:rdfs(w,c)
    for v in reversed(order):
        if comp[v]<0:comps.append([]);rdfs(v,len(comps)-1)
    return comp,comps
def simple_paths(n,arcs,start,goal):
    adj=[[] for _ in range(n)]
    for a,b in sorted(arcs):adj[a].append(b)
    out=[]
    def dfs(v,path):
        if v==goal:out.append(tuple(path));return
        for w in adj[v]:
            if w not in path:dfs(w,path+[w])
    dfs(start,[start]);return out
def path_edges(path):return frozenset(zip(path,path[1:]))
def max_edge_disjoint(paths):
    best=[]
    for r in range(len(paths)+1):
        for idxs in itertools.combinations(range(len(paths)),r):
            used=set();ok=True
            for i in idxs:
                pe=path_edges(paths[i])
                if used.intersection(pe):ok=False;break
                used.update(pe)
            if ok and r>len(best):best=[paths[i] for i in idxs]
    return best
def min_edge_cut(arcs,paths):
    if not paths:return frozenset()
    edges=sorted(arcs)
    for r in range(len(edges)+1):
        for sub in itertools.combinations(edges,r):
            S=set(sub)
            if all(S.intersection(path_edges(p)) for p in paths):return frozenset(S)
    raise AssertionError
def shortest_path(n,arcs,start,goal):
    paths=simple_paths(n,arcs,start,goal);require(paths,'path missing');return min(paths,key=lambda p:(len(p),p))
def cycle_vertices(a,path):
    u,w=a;require(path[0]==w and path[-1]==u,'return endpoints');return (u,)+path[:-1]
def flip_state(n,cycle):
    m=list(range(n))
    for i,v in enumerate(cycle):m[v]=cycle[(i+1)%len(cycle)]
    return tuple(m)
def entering_edges(state):return frozenset((i,state[i]) for i in range(len(state)) if state[i]!=i)
def validate_report(r):
    require(r['contract_sha256']==EXPECTED_CONTRACT_SHA256,'contract')
    require(r['record_sha256']==digest({k:v for k,v in r.items() if k!='record_sha256'}),'seal')
    require(r['mixed_digraph_profiles']>0 and r['theta_fan_profiles']>0 and r['small_cut_profiles']>0,'endpoint coverage')
    require(r['theta_private_edge_incidences']>0 and r['rooted_conflict_occurrences']>0,'payment coverage')
    require(r['mixed_cycle_boundary_fan_ancestry_proved']==1,'fan flag')
    require(r['theta_fan_private_edge_payment_proved']==1,'payment flag')
    require(r['global_transition_kind_bank_exhaustive']==0 and r['global_termination_proved']==0 and r['all_n_proved_by_checker']==0,'honesty')
def main():
    n=3;vertices=range(n);all_arcs=[(i,j) for i in vertices for j in vertices if i!=j]
    profiles=mixed=theta=cutprof=0;boundary=cycles=return_paths=private_inc=rooted=nonrooted=twoedge=0;token=0
    for mask in range(1,1<<len(all_arcs)):
        arcs={a for k,a in enumerate(all_arcs) if mask>>k&1}
        comp,comps=sccs(n,arcs)
        for colors_tuple in itertools.product((0,1),repeat=n):
            if len(set(colors_tuple))<2:continue
            profiles+=1;colors=dict(enumerate(colors_tuple))
            B=sorted((a,b) for a,b in arcs if colors[a]!=colors[b] and comp[a]==comp[b])
            if not B:continue
            mixed+=1;boundary+=len(B)
            witness=[]
            for a in B:
                u,w=a;path=shortest_path(n,arcs-{a},w,u);cyc=cycle_vertices(a,path)
                require(len(set(cyc))==len(cyc) and len({colors[v] for v in cyc})>1,'witness')
                witness.append((a,cyc));cycles+=1
            distinct_by_v={v:set() for v in vertices};labels_by_v={v:[] for v in vertices}
            for a,cyc in witness:
                for v in cyc:labels_by_v[v].append(a);distinct_by_v[v].add(cyc)
            for v in vertices:
                delta=len(labels_by_v[v]);Cv=len(distinct_by_v[v])
                if delta:
                    require(Cv >= (delta+n-1)//n,'distinct cycle lower bound')
                    incid={a:sum(a in path_edges(c+(c[0],)) for c in distinct_by_v[v]) for a in B}
                    L=max(incid.values(),default=0)
                    require(L >= (2*Cv+len(B)-1)//len(B),'boundary incidence lower bound')
            for a in B:
                u,w=a;paths=simple_paths(n,arcs-{a},w,u);return_paths+=len(paths)
                packing=max_edge_disjoint(paths);cut=min_edge_cut(arcs-{a},paths)
                require(len(packing)==len(cut),'edge Menger mismatch')
                q=2
                if len(packing)>=q:
                    theta+=1;chosen=packing[:q];states=[];enter=[]
                    for p in chosen:
                        cyc=(u,)+p[:-1];st=flip_state(n,cyc);states.append(st);enter.append(entering_edges(st))
                    common=set.intersection(*(set(x) for x in enter));require(common=={a},'theta core')
                    priv=[set(x)-{a} for x in enter]
                    require(all(x for x in priv),'empty private set');require(not priv[0].intersection(priv[1]),'private overlap')
                    private_inc+=sum(len(x) for x in priv);token+=sum(len(x) for x in priv)*6
                    universe=set().union(*enter)-{a}
                    for r in range(q):
                        for F in itertools.combinations(sorted(universe),r):
                            require(any(not set(F).intersection(E) for E in enter),'small blocker hit all theta states')
                    host_edges=set((i,i) for i in vertices).union(*[set(E) for E in enter]);base=set((i,i) for i in vertices)
                    C=[frozenset(x) for x in itertools.combinations(sorted(host_edges),2) if not set(x)<=base]
                    deg={e:sum(e in c for c in C) for e in host_edges};d=max(deg.values(),default=0);nr_total=0
                    for st,E,Pr in zip(states,enter,priv):
                        state_edges=set((i,st[i]) for i in vertices);present=[c for c in C if c<=state_edges]
                        for c in present:
                            if a in c and c<=base|{a}:rooted+=1
                            else:require(c.intersection(Pr),'nonrooted conflict lacks private support');nonrooted+=1;nr_total+=1
                    require(nr_total <= d*sum(len(x) for x in priv),'aggregate private degree bound')
                else:
                    cutprof+=1;require(len(cut)<q and len(cut)>=1,'small cut size')
                    counts={b:sum(b in path_edges(p) for p in paths) for b in cut};L=len(paths);mx=max(counts.values(),default=0)
                    require(mx >= (L+len(cut)-1)//len(cut),'cut concentration');twoedge+=mx
    claims={'checker':'prime-power-mixed-cycle-boundary-theta-payment','contract_sha256':EXPECTED_CONTRACT_SHA256,'digraph_colour_profiles':profiles,'mixed_digraph_profiles':mixed,'cyclic_boundary_arcs':boundary,'canonical_witness_cycles':cycles,'return_path_incidences':return_paths,'theta_fan_profiles':theta,'small_cut_profiles':cutprof,'two_edge_bottleneck_incidences':twoedge,'theta_private_edge_incidences':private_inc,'rooted_conflict_occurrences':rooted,'nonrooted_private_conflict_occurrences':nonrooted,'sample_full_token_incidences':token,'corruption_rejections':8,'mixed_cycle_boundary_fan_ancestry_proved':1,'theta_fan_private_edge_payment_proved':1,'global_transition_kind_bank_exhaustive':0,'global_termination_proved':0,'actual_global_parent_rule_complete':0,'all_n_proved_by_checker':0}
    claims['record_sha256']=digest(claims);validate_report(claims)
    muts=[('contract_sha256','0'*64),('mixed_cycle_boundary_fan_ancestry_proved',0),('theta_fan_private_edge_payment_proved',0),('all_n_proved_by_checker',1),('mixed_digraph_profiles',0),('theta_fan_profiles',0),('rooted_conflict_occurrences',0),('record_sha256','f'*64)]
    rej=0
    for k,v in muts:
        bad=dict(claims);bad[k]=v
        if k!='record_sha256':bad['record_sha256']=digest({x:y for x,y in bad.items() if x!='record_sha256'})
        try:validate_report(bad)
        except FanError:rej+=1
    require(rej==8,'corruption rejection')
    print(json.dumps(claims,sort_keys=True))
if __name__=='__main__':main()
