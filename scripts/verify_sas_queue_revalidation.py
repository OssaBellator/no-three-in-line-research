#!/usr/bin/env python3
"""Finite audit for SAS5oe--SAS5oh."""
from collections import Counter
from math import ceil
from random import Random


def run(seed=606, systems=2500):
    rng=Random(seed); out=Counter()
    for _ in range(systems):
        p=list(range(rng.randint(16,44))); n=rng.randint(1,24)
        fs=[frozenset(rng.sample(p,rng.randint(1,min(6,len(p))))) for _ in range(n)]
        eta=max(Counter(x for f in fs for x in f).values(),default=0)
        h=rng.randint(0,min(6,len(p))); edit=set(rng.sample(p,h))
        touched=[i for i,f in enumerate(fs) if f&edit]; assert len(touched)<=h*eta
        active=set(range(n))
        for i in touched:
            if rng.randrange(3)==1: active.remove(i)
        u=rng.randint(0,6); active.update(range(n,n+u)); assert len(active)<=n+u
        total=bound=0
        for _j in range(rng.randint(1,8)):
            size=rng.randint(0,min(5,len(p))); support=set(rng.sample(p,size))
            seen=sum(bool(f&support) for f in fs); assert seen<=size*eta
            total+=seen; bound+=size*eta
        assert total<=bound
        head=fs[0]; blocks=rng.randint(1,12); hits=Counter(); serviced=False
        for _b in range(blocks):
            if rng.random()<.30: serviced=True; break
            hits[rng.choice(tuple(head))]+=1
        if serviced: out['service_cases']+=1
        else:
            assert max(hits.values())>=ceil(blocks/len(head)); out['repeated_touch_cases']+=1
        out['systems']+=1; out['jobs']+=n; out['touched']+=len(touched); out['inspection_bound']+=h*eta
    return out

if __name__=='__main__':
    r=run(); print('SAS queue revalidation audit passed')
    for k in sorted(r): print(f'{k}: {r[k]}')
