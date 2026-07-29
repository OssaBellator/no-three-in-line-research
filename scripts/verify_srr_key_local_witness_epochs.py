#!/usr/bin/env python3
"""Finite audit for SRR2fm--SRR2fp."""
from __future__ import annotations
import random
from collections import Counter
SEED, CASES = 5, 2000

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
def fibres(xs,n): return {k:[x for x in xs if x[1]==k] for k in range(n)}
def main():
    rng=random.Random(SEED); stats=Counter(); accepted=trial=0
    while accepted<CASES:
        trial+=1; nr=rng.randint(2,8); nk=rng.randint(1,4)
        rs=[(i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(nr)]
        ts=[(100+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(nr+rng.randint(1,4))]
        m,d=matching(rs,ts)
        if m<nr: continue
        r0=[r for r in rs if rng.random()<.65]; t0=[t for t in ts if rng.random()<.65]
        a,c=rng.randint(0,3),rng.randint(0,3)
        dr=[(1000+10*trial+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(a)]
        dt=[(100000+10*trial+i,rng.randrange(nk),rng.randrange(9),rng.randrange(3)) for i in range(c)]
        rp,tp=r0+dr,t0+dt
        old={(r[0],t[0]) for r in rs for t in ts if compat(r,t)}; full={(r[0],t[0]) for r in rp for t in tp if compat(r,t)}
        keep={(r[0],t[0]) for r in r0 for t in t0 if (r[0],t[0]) in old}
        boundary=[(r,t) for r in dr for t in tp if r[1]==t[1]]+[(r,t) for r in r0 for t in dt if r[1]==t[1]]
        assert keep|{(r[0],t[0]) for r,t in boundary if compat(r,t)}==full
        drk,tpk,r0k,dtk=(fibres(x,nk) for x in (dr,tp,r0,dt)); exact=sum(len(drk[k])*len(tpk[k])+len(r0k[k])*len(dtk[k]) for k in range(nk)); assert exact==len(boundary)
        lt=max(len(tpk[k]) for k in range(nk)); lr=max(len(r0k[k]) for k in range(nk)); assert exact<=a*lt+c*lr
        ids={t[0] for t in t0}; b=sum(d.get(r[0]) not in ids for r in r0); e=len(ts)-len(t0); assert b<=e
        nm,_=matching(rp,tp); deficit=len(rp)-nm; assert deficit<=a+b<=a+e
        stats.update(boundary=exact,full_pairs=len(rp)*len(tp),deficient=deficit>0,deficit=deficit,churn=a+b); accepted+=1
    print(f"SRR keyed epochs: {accepted}"); print(f"key-local/full pairs: {stats['boundary']}/{stats['full_pairs']}"); print(f"deficient updates: {stats['deficient']}"); print(f"total deficit/churn: {stats['deficit']}/{stats['churn']}")
if __name__=='__main__': main()
