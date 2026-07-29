#!/usr/bin/env python3
"""Finite checks for SAS5nw--SAS5nz."""
from collections import Counter
from math import ceil
from random import Random

SEED, TRIALS = 757, 2500


def independent(fps):
    left=set(range(len(fps))); out=[]
    while left:
        v=min(left); out.append(v); left-={u for u in left if fps[u]&fps[v]}
    return out


def verify():
    r=Random(SEED); systems=repairs=chosen=feasible=shortages=cost_total=0
    for _ in range(TRIALS):
        p=r.randint(4,18); h=r.randint(1,min(5,p)); beta=r.randint(1,5)
        loads=[0]*p; fps=[]
        for _ in range(r.randint(1,35)):
            avail=[x for x in range(p) if loads[x]<beta]
            if not avail: break
            fp=set(r.sample(avail,r.randint(1,min(h,len(avail)))))
            for x in fp: loads[x]+=1
            fps.append(fp)
        if not fps: continue
        assert max(Counter(x for f in fps for x in f).values())<=beta
        bound=h*(beta-1)
        assert all(sum(i!=j and bool(f&g) for j,g in enumerate(fps))<=bound for i,f in enumerate(fps))
        I=independent(fps)
        assert len(I)>=ceil(len(fps)/(bound+1))
        assert all(not(fps[i]&fps[j]) for a,i in enumerate(I) for j in I[a+1:])
        d=r.randint(1,5); costs=[[r.randint(0,4) for _ in range(d)] for _ in fps]
        C=[sum(costs[i][a] for i in I) for a in range(d)]; B=[r.randint(0,c+3) for c in C]
        if all(c<=B[a] for a,c in enumerate(C)): feasible+=1
        else:
            shortages+=1; a=next(a for a,c in enumerate(C) if c>B[a]); assert C[a]-B[a]>0
        k=max(map(sum,costs)); assert sum(C)<=k*len(I)
        systems+=1; repairs+=len(fps); chosen+=len(I); cost_total+=sum(C)
    deficit=r.randint(0,20); initial=deficit; churn=gain=ledger=0; kappa=7
    for _ in range(5000):
        u=r.randint(0,6); g=r.randint(0,deficit+u); c=r.randint(0,kappa*g)
        deficit+=u-g; churn+=u; gain+=g; ledger+=c
        assert gain<=initial+churn and ledger<=kappa*gain
    return systems,repairs,chosen,feasible,shortages,cost_total,churn,gain,ledger

if __name__=='__main__':
    print('SAS footprint-cost checks passed:', *verify())
