#!/usr/bin/env python3
"""Finite audit for AC5hb--AC5he."""
from collections import Counter
from math import ceil
from random import Random


def run(seed=777, systems=1500):
    rng=Random(seed); out=Counter()
    for _ in range(systems):
        primitives=list(range(rng.randint(24,60)))
        jobs=[]; debt=0
        for track in range(7):
            for _j in range(rng.randint(1,12)):
                footprint=frozenset(rng.sample(primitives,rng.randint(1,min(6,len(primitives)))))
                jobs.append((debt,track,footprint)); debt+=1
        beta=max(Counter(x for _,_,f in jobs for x in f).values(),default=0)
        h_edit=rng.randint(0,min(7,len(primitives)))
        edit=set(rng.sample(primitives,h_edit))
        touched=[job for job in jobs if job[2]&edit]
        untouched=[job for job in jobs if not job[2]&edit]
        assert len(touched)<=h_edit*beta
        assert len(touched)+len(untouched)==len(jobs)

        active={j:(s,f) for j,s,f in jobs}
        retired=0
        for j,s,f in touched:
            if rng.random()<.28:
                del active[j]; retired+=1
            else:
                assert active[j][0]==s  # no track migration
        disturbance=rng.randint(0,10)
        for k in range(disturbance):
            track=rng.randrange(7)
            footprint=frozenset(rng.sample(primitives,rng.randint(1,min(5,len(primitives)))))
            active[debt+k]=(track,footprint)
        assert len(active)<=len(jobs)-retired+disturbance
        assert len(active)==len(set(active))

        head=rng.choice(jobs)
        footprint=head[2]; blocks=rng.randint(1,14)
        hits=Counter(); serviced=False
        for _block in range(blocks):
            if rng.random()<.25:
                serviced=True; break
            hits[rng.choice(tuple(footprint))]+=1
        if serviced:
            out['service_cases']+=1
        else:
            assert max(hits.values())>=ceil(blocks/len(footprint))
            out['persistent_touch_cases']+=1

        out['systems']+=1
        out['jobs']+=len(jobs)
        out['touched']+=len(touched)
        out['inspection_bound']+=h_edit*beta
        out['retired']+=retired
        out['new_debts']+=disturbance
    return out

if __name__=='__main__':
    r=run(); print('AC synchronized queue revalidation audit passed')
    for k in sorted(r): print(f'{k}: {r[k]}')
