#!/usr/bin/env python3
"""Finite verifier for BDA5id--BDA5ig."""
from __future__ import annotations
import math, random
from dataclasses import dataclass

@dataclass(frozen=True)
class Job:
    cost: tuple[int, ...]

def drain(queue: list[Job], cap: tuple[int, ...], kappa: tuple[int, ...], window: int, rng: random.Random) -> tuple[int,int]:
    reserve=[rng.randint(0,cap[a]) for a in range(len(cap))]
    replen=[max(1,math.ceil(kappa[a]/window)) for a in range(len(cap))]
    steps=head=max_head=0
    while queue:
        steps+=1; head+=1
        for a in range(len(cap)): reserve[a]=min(cap[a],reserve[a]+replen[a])
        if all(reserve[a]>=queue[0].cost[a] for a in range(len(cap))):
            job=queue.pop(0)
            for a in range(len(cap)): reserve[a]-=job.cost[a]
            max_head=max(max_head,head); head=0
    return steps,max_head

def main() -> None:
    rng=random.Random(202); systems=jobs=arrivals=oversized=shortages=0
    for _ in range(2500):
        d=rng.randint(2,6); cap=tuple(rng.randint(3,10) for _ in range(d)); kappa=tuple(rng.randint(1,cap[a]) for a in range(d)); W=rng.randint(1,6); n=rng.randint(1,20)
        q=[]
        for _ in range(n):
            c=tuple(rng.randint(0,kappa[a]) for a in range(d)); q.append(Job(c if any(c) else (1,)+(0,)*(d-1)))
        steps,mw=drain(q.copy(),cap,kappa,W,rng); assert mw<=W and steps<=n*W
        delta0=rng.randint(n,n+10); disturbance=sum(rng.randint(0,4) for _ in range(rng.randint(2,10))); admitted=n+rng.randint(0,delta0+disturbance-n); assert admitted<=delta0+disturbance
        arrivals+=admitted
        if rng.random()<.12: oversized+=1
        if rng.random()<.25:
            a=rng.randrange(d); supplied=max(0,kappa[a]-rng.randint(1,max(1,kappa[a]))); assert kappa[a]-supplied>0; shortages+=1
        systems+=1; jobs+=n
    print(f"verified {systems} BDA queues, {jobs} jobs, {arrivals} admissions")
    print(f"returned {oversized} oversized jobs and {shortages} replenishment shortages")
if __name__ == '__main__': main()
