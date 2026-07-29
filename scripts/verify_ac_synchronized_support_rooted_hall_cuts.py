#!/usr/bin/env python3
"""Deterministic finite audit for AC5gh--AC5gk."""
from collections import defaultdict, deque
import math, random

def matching(left,edges):
    adj={u:[] for u in left}
    for u,v in edges:adj[u].append(v)
    mr={}
    def go(u,seen):
        for v in adj[u]:
            if v in seen:continue
            seen.add(v)
            if v not in mr or go(mr[v],seen):mr[v]=u;return True
        return False
    for u in left:go(u,set())
    return {u:v for v,u in mr.items()},mr

def closure(edges,ml,mr,roots):
    adj=defaultdict(set)
    for u,v in edges:adj[u].add(v)
    A=set(roots);B=set();Q=deque((0,u) for u in roots)
    while Q:
        side,x=Q.popleft()
        if side==0:
            for v in adj[x]:
                if ml.get(x)==v:continue
                if v not in B:B.add(v);Q.append((1,v))
        elif x in mr and mr[x] not in A:A.add(mr[x]);Q.append((0,mr[x]))
    return A,B

def make_system(rng,prefix):
    K=rng.randint(1,4);L=[];R=[];kl={};kr={}
    for k in range(K):
        for i in range(rng.randint(1,7)):u=f"{prefix}r{k}_{i}";L.append(u);kl[u]=k
        for j in range(rng.randint(1,7)):v=f"{prefix}t{k}_{j}";R.append(v);kr[v]=k
    q=rng.randint(1,6);E=set();fail={}
    for u in L:
        for v in R:
            if kl[u]!=kr[v]:continue
            p=(u,v)
            if rng.random()<.45:E.add(p)
            else:
                labs={j for j in range(q) if rng.random()<.35};fail[p]=labs or {rng.randrange(q)}
    ml,mr=matching(L,E);roots=[u for u in L if u not in ml];H=rng.randint(1,5);cause={u:rng.randrange(H) for u in roots}
    return L,R,kl,kr,E,fail,q,ml,mr,roots,cause

def audit(seed):
    rng=random.Random(seed);systems=[];all_roots=[]
    for track in range(7):
        system=make_system(rng,f"s{track}_");systems.append(system)
        L,R,kl,kr,E,fail,q,ml,mr,roots,cause=system
        for u in roots:all_roots.append((track,cause[u],kl[u],u))
    stats=defaultdict(int);stats['tracks']=7;stats['deficit']=len(all_roots)
    if not all_roots:return stats
    groups=defaultdict(list)
    for track,cause,key,root in all_roots:groups[(track,cause,key)].append(root)
    triple,U=max(groups.items(),key=lambda z:(len(z[1]),str(z[0])));track,_,key=triple;m=len(U)
    assert m>=math.ceil(len(all_roots)/len(groups))
    L,R,kl,kr,E,fail,q,ml,mr,roots,cause=systems[track]
    Lk=[u for u in L if kl[u]==key];Rk=[v for v in R if kr[v]==key];Ek={(u,v) for u,v in E if kl[u]==key}
    A,B=closure(Ek,ml,mr,U);assert {v for u,v in Ek if u in A}==B;assert len(A)-len(B)==m
    stats['active_triples']=len(groups);stats['selected_roots']=m;stats['closure_vertices']=len(A)+len(B)
    if len(Rk)<len(Lk):stats['shortfall']=len(Lk)-len(Rk);return stats
    out=set(Rk)-B;assert len(out)>=m;rect=[(u,v) for u in U for v in out];assert all(p not in E for p in rect)
    cnt=defaultdict(int);per=defaultdict(lambda:defaultdict(int))
    for p in rect:lab=min(fail[p]);cnt[lab]+=1;per[p[0]][lab]+=1
    lab=max(cnt,key=cnt.get);assert cnt[lab]*q>=m*m;assert max(per[u][lab] for u in U)>=math.ceil(m/q)
    stats['balanced']=1;stats['rectangle_pairs']=len(rect);stats['predicate_pairs']=cnt[lab];return stats

def main():
    total=defaultdict(int)
    for seed in range(900000,901500):
        total['macros']+=1
        for k,v in audit(seed).items():total[k]+=v
    expected={'macros':1500,'tracks':10500,'deficit':35407,'active_triples':23190,'selected_roots':5398,'closure_vertices':9502,'shortfall':6336,'balanced':10,'rectangle_pairs':53,'predicate_pairs':35}
    assert dict(total)==expected,(dict(total),expected)
    print('AC5gh--AC5gk audit passed:',expected)
if __name__=='__main__':main()
