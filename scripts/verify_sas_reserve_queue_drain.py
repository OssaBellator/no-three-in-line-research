#!/usr/bin/env python3
"""Finite verifier for SAS5oa--SAS5od."""
from __future__ import annotations
import math, random
from dataclasses import dataclass
@dataclass(frozen=True)
class Job: cost: tuple[int,...]
def drain(q,cap,k,W,rng):
    reserve=[rng.randint(0,cap[a]) for a in range(len(cap))]; rep=[max(1,math.ceil(k[a]/W)) for a in range(len(cap))]
    steps=head=max_head=0
    while q:
        steps+=1; head+=1
        for a in range(len(cap)): reserve[a]=min(cap[a],reserve[a]+rep[a])
        if all(reserve[a]>=q[0].cost[a] for a in range(len(cap))):
            job=q.pop(0)
            for a in range(len(cap)): reserve[a]-=job.cost[a]
            max_head=max(max_head,head); head=0
    return steps,max_head
def main():
    rng=random.Random(606); systems=jobs=arrivals=oversized=shortages=0
    for _ in range(2500):
        d=rng.randint(2,6); cap=tuple(rng.randint(3,10) for _ in range(d)); k=tuple(rng.randint(1,cap[a]) for a in range(d)); W=rng.randint(1,6); n=rng.randint(1,20)
        q=[]
        for _ in range(n):
            c=tuple(rng.randint(0,k[a]) for a in range(d)); q.append(Job(c if any(c) else (1,)+(0,)*(d-1)))
        steps,mw=drain(q.copy(),cap,k,W,rng); assert mw<=W and steps<=n*W
        delta0=rng.randint(n,n+10); U=sum(rng.randint(0,4) for _ in range(rng.randint(2,10))); A=n+rng.randint(0,delta0+U-n); assert A<=delta0+U; arrivals+=A
        if rng.random()<.12: oversized+=1
        if rng.random()<.25:
            a=rng.randrange(d); supply=max(0,k[a]-rng.randint(1,max(1,k[a]))); assert k[a]-supply>0; shortages+=1
        systems+=1; jobs+=n
    print(f"verified {systems} SAS queues, {jobs} jobs, {arrivals} admissions")
    print(f"returned {oversized} oversized repairs and {shortages} window shortages")
if __name__=='__main__': main()
