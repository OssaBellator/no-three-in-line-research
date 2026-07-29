#!/usr/bin/env python3
"""Finite audit for AC5fz--AC5gc."""
from __future__ import annotations
import random
from collections import Counter
SEED, EPOCHS, TRACKS = 7, 1500, 7

def compat(r,t): return r[1]==t[1] and (3*r[2]+2*t[2]+r[3]+t[3])%7 not in (0,1)
def matching(rs,ts):
    adj={r[0]:[t[0] for t in ts if compat(r,t)] for r in rs}; mt={}
    def visit(rid,seen):
        for tid in adj[rid]:
            if tid in seen: continue
            seen.add(tid)
            if tid not in mt or visit(mt[tid],seen): mt[tid]=rid; return True
        return False
    for r in rs: visit(r[0],set())
    return len(mt),{rid:tid for tid,rid in mt.items()}

def one_track(rng,track,epoch):
    while True:
        nr,nk=rng.randint(2,7),rng.randint(1,4); base=track*1_000_000+epoch*1000
        rs=[(base+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(nr)]
        ts=[(base+100+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(nr+rng.randint(1,4))]
        size,d=matching(rs,ts)
        if size==nr: break
    r0=[r for r in rs if rng.random()<.65]; t0=[t for t in ts if rng.random()<.65]
    a,c=rng.randint(0,3),rng.randint(0,3)
    dr=[(base+500+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(a)]
    dt=[(base+800+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(c)]
    rp,tp=r0+dr,t0+dt
    old={(r[0],t[0]) for r in rs for t in ts if compat(r,t)}; full={(r[0],t[0]) for r in rp for t in tp if compat(r,t)}
    keep={(r[0],t[0]) for r in r0 for t in t0 if (r[0],t[0]) in old}
    boundary=[(r,t) for r in dr for t in tp if r[1]==t[1]]+[(r,t) for r in r0 for t in dt if r[1]==t[1]]
    assert keep|{(r[0],t[0]) for r,t in boundary if compat(r,t)}==full
    lt=max(sum(t[1]==k for t in tp) for k in range(nk)); lr=max(sum(r[1]==k for r in r0) for k in range(nk))
    assert len(boundary)<=a*lt+c*lr
    ids={t[0] for t in t0}; b=sum(d.get(r[0]) not in ids for r in r0); e=len(ts)-len(t0); assert b<=e
    new_size,_=matching(rp,tp); delta=len(rp)-new_size; assert delta<=a+b
    component_deficits=[]
    for k in range(nk):
        rk=[r for r in rp if r[1]==k]; tk=[t for t in tp if t[1]==k]
        mk,_=matching(rk,tk); component_deficits.append(len(rk)-mk)
    assert sum(component_deficits)==delta
    return len(boundary),len(rp)*len(tp),a+b,delta,component_deficits

def main():
    rng=random.Random(SEED); stats=Counter(); maximum=0
    for epoch in range(EPOCHS):
        tracks=[one_track(rng,s,epoch) for s in range(TRACKS)]
        boundary=sum(x[0] for x in tracks); full=sum(x[1] for x in tracks); churn=sum(x[2] for x in tracks); deficit=sum(x[3] for x in tracks)
        components=[d for x in tracks for d in x[4]]
        assert deficit==sum(components)<=churn
        active=len(components)
        if deficit:
            assert max(components)>=(deficit+active-1)//active
        stats.update(boundary=boundary,full_pairs=full,churn=churn,deficit=deficit,deficient=deficit>0); maximum=max(maximum,deficit)
    print(f"AC macro epochs: {EPOCHS}"); print(f"key-local/full pairs: {stats['boundary']}/{stats['full_pairs']}")
    print(f"total deficit/churn: {stats['deficit']}/{stats['churn']}"); print(f"deficient epochs/max deficit: {stats['deficient']}/{maximum}")
if __name__=='__main__': main()
