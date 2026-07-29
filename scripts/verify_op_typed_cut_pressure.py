#!/usr/bin/env python3
"""Finite audit for OP4ee--OP4ei."""
from collections import deque
from random import Random
SEED, SYSTEMS, TYPED = 2105, 3200, True

def flow(n, edges, s, t, enabled):
    cap=[[0]*n for _ in range(n)]
    for u,v,c,key in edges: cap[u][v]+=enabled.get(key,c)
    res=[row[:] for row in cap]; value=0
    while True:
        parent=[-1]*n; parent[s]=s; q=deque([s])
        while q and parent[t]<0:
            u=q.popleft()
            for v in range(n):
                if parent[v]<0 and res[u][v]>0:
                    parent[v]=u; q.append(v)
                    if v==t: break
        if parent[t]<0: break
        aug=10**9; v=t
        while v!=s: u=parent[v]; aug=min(aug,res[u][v]); v=u
        v=t
        while v!=s: u=parent[v]; res[u][v]-=aug; res[v][u]+=aug; v=u
        value+=aug
    reach=[False]*n; reach[s]=True; q=deque([s])
    while q:
        u=q.popleft()
        for v in range(n):
            if not reach[v] and res[u][v]>0: reach[v]=True; q.append(v)
    used={(u,v,key):cap[u][v]-res[u][v] for u,v,_,key in edges}
    return value,used,reach

def system(rng):
    nt,np,nq=rng.randint(2,4),rng.randint(2,4),rng.randint(2,4)
    s,p0,q0,x0=0,1,1+np,1+np+nq; t=x0+nt; edges=[]
    for i in range(np): edges.append((s,p0+i,rng.randint(1,3),("sp",i)))
    for i in range(np):
        made=False
        for j in range(nq):
            if rng.random()<.65: edges.append((p0+i,q0+j,rng.randint(1,3),("pq",i,j))); made=True
        if not made: j=rng.randrange(nq); edges.append((p0+i,q0+j,rng.randint(1,3),("pq",i,j)))
    for j in range(nq):
        made=False
        for k in range(nt):
            if rng.random()<.65: edges.append((q0+j,x0+k,rng.randint(1,3),("qt",j,k))); made=True
        if not made: k=rng.randrange(nt); edges.append((q0+j,x0+k,rng.randint(1,3),("qt",j,k)))
    demand=[rng.randint(1,3) for _ in range(nt)]
    for k,d in enumerate(demand): edges.append((x0+k,t,d,("term",k)))
    return t+1,edges,s,t,demand,[rng.randrange(2) for _ in range(nt)]

def enabled(demand,mask): return {("term",k):d if mask>>k&1 else 0 for k,d in enumerate(demand)}

def main():
    rng=Random(SEED)
    out=dict(systems=SYSTEMS,subset_checks=0,deficient=0,singletons=0,nontrivial=0,cut_arcs=0,positive_arcs=0,deficit_units=0,nontrivial_deficit=0,positive_pressure=0,backward_crossings=0,typed_mixed=0)
    for _ in range(SYSTEMS):
        n,edges,s,t,demand,types=system(rng); nt=len(demand); vals={}
        for mask in range(1,1<<nt):
            value,_,_=flow(n,edges,s,t,enabled(demand,mask)); total=sum(demand[k] for k in range(nt) if mask>>k&1)
            vals[mask]=(value,total-value); out["subset_checks"]+=1
        bad=[m for m,(_,gap) in vals.items() if gap>0]
        if not bad: continue
        size=min(m.bit_count() for m in bad); core=min(m for m in bad if m.bit_count()==size)
        assert all(vals[sub][1]==0 for sub in range(1,1<<nt) if sub!=core and sub&core==sub)
        delta=vals[core][1]; out["deficient"]+=1; out["deficit_units"]+=delta
        members=[k for k in range(nt) if core>>k&1]
        if len(members)==1: out["singletons"]+=1; continue
        zero=[k for k in members if types[k]==0]; one=[k for k in members if types[k]==1]
        if zero and one: a=sum(1<<k for k in zero); out["typed_mixed"]+=1
        else: a=sum(1<<k for k in members[:len(members)//2])
        b=core^a; assert vals[a][1]==vals[b][1]==0
        out["nontrivial"]+=1; out["nontrivial_deficit"]+=delta
        _,_,reach=flow(n,edges,s,t,enabled(demand,core)); va,fa,_=flow(n,edges,s,t,enabled(demand,a)); vb,fb,_=flow(n,edges,s,t,enabled(demand,b))
        assert va+vb==sum(demand[k] for k in members)
        signed=positive=count=cuts=back=maximum=0; caps=enabled(demand,core)
        for u,v,c,key in edges:
            load=fa[(u,v,key)]+fb[(u,v,key)]; c=caps.get(key,c)
            if reach[u] and not reach[v]:
                pressure=load-c; signed+=pressure; cuts+=1
                if pressure>0: positive+=pressure; count+=1; maximum=max(maximum,pressure)
            elif not reach[u] and reach[v]: signed-=load; back+=load
        assert signed==delta and positive>=delta and count and maximum*cuts>=delta
        out["cut_arcs"]+=cuts; out["positive_arcs"]+=count; out["positive_pressure"]+=positive; out["backward_crossings"]+=back
    print("OP typed cut-pressure audit passed")
    for key,value in out.items(): print(f"{key}: {value}")

if __name__=="__main__": main()
