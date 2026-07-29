#!/usr/bin/env python3
"""Deterministic finite audit for OP4gk--OP4gn."""
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

def audit(seed):
    rng=random.Random(seed);K=rng.randint(1,4);L=[];R=[];kl={};kr={}
    for k in range(K):
        for i in range(rng.randint(1,7)):u=f"r{k}_{i}";L.append(u);kl[u]=k
        for j in range(rng.randint(1,7)):v=f"t{k}_{j}";R.append(v);kr[v]=k
    q=rng.randint(1,6);E=set();fail={}
    for u in L:
        for v in R:
            if kl[u]!=kr[v]:continue
            p=(u,v)
            if rng.random()<.45:E.add(p)
            else:
                labs={j for j in range(q) if rng.random()<.35};fail[p]=labs or {rng.randrange(q)}
    ml,mr=matching(L,E);roots=[u for u in L if u not in ml];s=defaultdict(int);s.update(vertices=len(L)+len(R),edges=len(E),roots=len(roots))
    if not roots:return s
    H=rng.randint(1,5);cause={u:rng.randrange(H) for u in roots};G=defaultdict(list)
    for u in roots:G[(cause[u],kl[u])].append(u)
    _,U=max(G.items(),key=lambda z:(len(z[1]),str(z[0])));m=len(U);k=kl[U[0]];assert m>=math.ceil(len(roots)/len(G))
    Lk=[u for u in L if kl[u]==k];Rk=[v for v in R if kr[v]==k];Ek={(u,v) for u,v in E if kl[u]==k}
    A,B=closure(Ek,ml,mr,U);assert {v for u,v in Ek if u in A}==B;assert len(A)-len(B)==m
    s['selected_roots']=m;s['closure_vertices']=len(A)+len(B)
    if len(Rk)<len(Lk):s['shortfall']=len(Lk)-len(Rk);return s
    out=set(Rk)-B;assert len(out)>=m;rect=[(u,v) for u in U for v in out];assert all(p not in E for p in rect)
    cnt=defaultdict(int);per=defaultdict(lambda:defaultdict(int))
    for p in rect:lab=min(fail[p]);cnt[lab]+=1;per[p[0]][lab]+=1
    lab=max(cnt,key=cnt.get);assert cnt[lab]*q>=m*m;assert max(per[u][lab] for u in U)>=math.ceil(m/q)
    s['balanced']=1;s['rectangle_pairs']=len(rect);s['predicate_pairs']=cnt[lab];return s

def main():
    total=defaultdict(int)
    for seed in range(300017,302517):
        for k,v in audit(seed).items():total[k]+=v
    expected={'vertices':49879,'edges':44919,'roots':8283,'selected_roots':4122,'closure_vertices':9964,'shortfall':5090,'balanced':315,'rectangle_pairs':1148,'predicate_pairs':755}
    assert dict(total)==expected,(dict(total),expected)
    print('OP4gk--OP4gn audit passed:',expected)
if __name__=='__main__':main()
