#!/usr/bin/env python3
"""Deterministic finite audit for BDA5hn--BDA5hq."""
from collections import defaultdict, deque
import math, random

def maximum_matching(left, edges):
    adj={u:[] for u in left}
    for u,v in edges: adj[u].append(v)
    mr={}
    def aug(u,seen):
        for v in adj[u]:
            if v in seen: continue
            seen.add(v)
            if v not in mr or aug(mr[v],seen): mr[v]=u; return True
        return False
    for u in left: aug(u,set())
    return {u:v for v,u in mr.items()},mr

def closure(edges,ml,mr,roots):
    adj=defaultdict(set)
    for u,v in edges: adj[u].add(v)
    A=set(roots); B=set(); q=deque((0,u) for u in roots)
    while q:
        side,x=q.popleft()
        if side==0:
            for v in adj[x]:
                if ml.get(x)==v: continue
                if v not in B: B.add(v); q.append((1,v))
        elif x in mr and mr[x] not in A:
            A.add(mr[x]); q.append((0,mr[x]))
    return A,B

def audit(seed):
    rng=random.Random(seed); K=rng.randint(1,4)
    L=[];R=[];kl={};kr={}
    for k in range(K):
        for i in range(rng.randint(1,7)): u=f"r{k}_{i}";L.append(u);kl[u]=k
        for j in range(rng.randint(1,7)): v=f"t{k}_{j}";R.append(v);kr[v]=k
    qpred=rng.randint(1,6); E=set(); fails={}
    for u in L:
        for v in R:
            if kl[u]!=kr[v]: continue
            p=(u,v)
            if rng.random()<.45: E.add(p)
            else:
                labs={j for j in range(qpred) if rng.random()<.35}
                fails[p]=labs or {rng.randrange(qpred)}
    ml,mr=maximum_matching(L,E); roots=[u for u in L if u not in ml]
    st=defaultdict(int); st.update(vertices=len(L)+len(R),edges=len(E),roots=len(roots))
    if not roots:return st
    H=rng.randint(1,5); cause={u:rng.randrange(H) for u in roots}; groups=defaultdict(list)
    for u in roots: groups[(cause[u],kl[u])].append(u)
    _,U=max(groups.items(),key=lambda z:(len(z[1]),str(z[0])));m=len(U);k=kl[U[0]]
    assert m>=math.ceil(len(roots)/len(groups))
    Lk=[u for u in L if kl[u]==k];Rk=[v for v in R if kr[v]==k];Ek={(u,v) for u,v in E if kl[u]==k}
    A,B=closure(Ek,ml,mr,U);assert {v for u,v in Ek if u in A}==B;assert len(A)-len(B)==m
    st['selected_roots']=m;st['closure_vertices']=len(A)+len(B)
    if len(Rk)<len(Lk):st['shortfall']=len(Lk)-len(Rk);return st
    outside=set(Rk)-B;assert len(outside)>=m;rect=[(u,v) for u in U for v in outside];assert all(p not in E for p in rect)
    cnt=defaultdict(int);per=defaultdict(lambda:defaultdict(int))
    for p in rect:lab=min(fails[p]);cnt[lab]+=1;per[p[0]][lab]+=1
    lab=max(cnt,key=cnt.get);assert cnt[lab]*qpred>=m*m;assert max(per[u][lab] for u in U)>=math.ceil(m/qpred)
    st['balanced']=1;st['rectangle_pairs']=len(rect);st['predicate_pairs']=cnt[lab];return st

def main():
    total=defaultdict(int)
    for seed in range(100017,102517):
        for k,v in audit(seed).items():total[k]+=v
    expected={'vertices':49287,'edges':44438,'roots':8219,'selected_roots':4084,'closure_vertices':9560,'shortfall':5078,'balanced':318,'rectangle_pairs':1165,'predicate_pairs':760}
    assert dict(total)==expected,(dict(total),expected)
    print('BDA5hn--BDA5hq audit passed:',expected)
if __name__=='__main__':main()
