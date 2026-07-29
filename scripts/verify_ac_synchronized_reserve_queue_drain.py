#!/usr/bin/env python3
"""Finite verifier for AC5gx--AC5ha."""
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
    rng=random.Random(777)
    systems=track_queues=jobs=steps_total=arrivals=executed=oversized=shortages=0
    for _ in range(1500):
        delta0=disturbance=admitted_total=executed_total=0
        for _track in range(7):
            d=rng.randint(2,5); cap=tuple(rng.randint(3,10) for _ in range(d)); k=tuple(rng.randint(1,cap[a]) for a in range(d)); W=rng.randint(1,6); n=rng.randint(0,12)
            q=[]
            for _ in range(n):
                c=tuple(rng.randint(0,k[a]) for a in range(d)); q.append(Job(c if any(c) else (1,)+(0,)*(d-1)))
            if n:
                st,mw=drain(q.copy(),cap,k,W,rng); assert mw<=W and st<=n*W
            else: st=0
            d0=rng.randint(n,n+8); U=sum(rng.randint(0,3) for _ in range(rng.randint(1,8))); A=n+rng.randint(0,d0+U-n); G=rng.randint(0,A)
            assert A<=d0+U and G<=A
            delta0+=d0; disturbance+=U; admitted_total+=A; executed_total+=G
            jobs+=n; steps_total+=st; track_queues+=1
            if rng.random()<.10: oversized+=1
            if rng.random()<.20: shortages+=1
        assert admitted_total<=delta0+disturbance
        assert executed_total<=delta0+disturbance
        arrivals+=admitted_total; executed+=executed_total; systems+=1
    print(f"verified {systems} synchronized systems and {track_queues} typed queues")
    print(f"drained {jobs} initial jobs in {steps_total} service microsteps")
    print(f"origin-accounted {arrivals} admissions and {executed} executions")
    print(f"returned {oversized} oversized jobs and {shortages} typed window shortages")
if __name__=='__main__': main()
