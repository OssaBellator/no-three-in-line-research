#!/usr/bin/env python3
"""Deterministic audit for GC2kp--GC2kt."""
from collections import defaultdict
from importlib import import_module
from random import Random
BASE=import_module("verify_gc_cut_arc_collision_pairs")
FLOW,UNIT_PATHS,ENABLED=BASE.FLOW,BASE.unit_paths,BASE.ENABLED
SEED,SYSTEMS=2404,2000

def make_system(rng):
    nt,np,nq,nr=rng.randint(2,4),rng.randint(2,3),rng.randint(2,3),rng.randint(2,3)
    s,p0,q0,r0=0,1,1+np,1+np+nq; x0,t=r0+nr,r0+nr+nt; edges=[]
    for i in range(np): edges.append((s,p0+i,rng.randint(1,3),("sp",i)))
    for i in range(np):
        made=False
        for j in range(nq):
            if rng.random()<.7: edges.append((p0+i,q0+j,rng.randint(1,3),("pq",i,j))); made=True
        if not made:
            j=rng.randrange(nq); edges.append((p0+i,q0+j,rng.randint(1,3),("pq",i,j)))
    for j in range(nq):
        made=False
        for h in range(nr):
            if rng.random()<.7: edges.append((q0+j,r0+h,rng.randint(1,3),("qr",j,h))); made=True
        if not made:
            h=rng.randrange(nr); edges.append((q0+j,r0+h,rng.randint(1,3),("qr",j,h)))
    for h in range(nr):
        made=False
        for k in range(nt):
            if rng.random()<.7: edges.append((r0+h,x0+k,rng.randint(1,3),("rt",h,k))); made=True
        if not made:
            k=rng.randrange(nt); edges.append((r0+h,x0+k,rng.randint(1,3),("rt",h,k)))
    demand=[rng.randint(1,3) for _ in range(nt)]
    for k,d in enumerate(demand): edges.append((x0+k,t,d,("term",k)))
    return t+1,edges,s,t,demand,[0]*nt

def segment(pa,pb,key):
    a,b=pa[1],pb[1]; ia,ib=a.index(key),b.index(key); la,lb=ia,ib
    while la and lb and a[la-1]==b[lb-1]: la-=1; lb-=1
    ra,rb=ia,ib
    while ra+1<len(a) and rb+1<len(b) and a[ra+1]==b[rb+1]: ra+=1; rb+=1
    common=a[la:ra+1]; assert common==b[lb:rb+1]; source_prefix=la==lb==0
    if not source_prefix: assert a[la-1]!=b[lb-1]
    assert ra+1<len(a) and rb+1<len(b) and a[ra+1]!=b[rb+1]
    return common,source_prefix

def main():
    rng=Random(SEED); out=defaultdict(int); out["systems"]=SYSTEMS
    for _ in range(SYSTEMS):
        n,edges,s,t,demand,types=make_system(rng); count=len(demand); values={}
        for mask in range(1,1<<count):
            paid,_f,_r=FLOW(n,edges,s,t,ENABLED(demand,mask)); total=sum(demand[k] for k in range(count) if mask>>k&1)
            values[mask]=(paid,total-paid); out["subset_checks"]+=1
        bad=[m for m,(_p,g) in values.items() if g>0]
        if not bad: continue
        size=min(m.bit_count() for m in bad); core=min(m for m in bad if m.bit_count()==size)
        members=[k for k in range(count) if core>>k&1]; out["deficient"]+=1
        if len(members)==1: out["singletons"]+=1; continue
        side_a=sum(1<<k for k in members[:len(members)//2]); side_b=core^side_a
        _v,_f,reached=FLOW(n,edges,s,t,ENABLED(demand,core)); _a,fa,_=FLOW(n,edges,s,t,ENABLED(demand,side_a)); _b,fb,_=FLOW(n,edges,s,t,ENABLED(demand,side_b))
        paths_a=UNIT_PATHS(n,edges,s,t,fa); paths_b=UNIT_PATHS(n,edges,s,t,fb); caps=ENABLED(demand,core); signatures=defaultdict(int)
        for u,v,c,key in edges:
            if not reached[u] or reached[v]: continue
            pressure=fa[(u,v,key)]+fb[(u,v,key)]-caps.get(key,c)
            if pressure<=0: continue
            aa=[p for p in paths_a if key in p[1]]; bb=[p for p in paths_b if key in p[1]]; assert pressure<=min(len(aa),len(bb)); out["positive_arcs"]+=1
            for pa,pb in zip(aa[:pressure],bb[:pressure]):
                common,source_prefix=segment(pa,pb,key); out["collision_pairs"]+=1; out["segment_edges"]+=len(common); out["max_segment_length"]=max(out["max_segment_length"],len(common)); out["source_prefix" if source_prefix else "internal_merge_split"]+=1; signatures[(common,types[pa[0]],types[pb[0]])]+=1
        assert signatures; out["nontrivial"]+=1; out["concentrated_pairs"]+=max(signatures.values())
    print("GC collision-segment audit passed")
    for key,value in out.items(): print(f"{key}: {value}")

if __name__=="__main__": main()
