#!/usr/bin/env python3
"""Finite checks for AC5gt--AC5gw."""
from collections import Counter
from math import ceil
from random import Random

SEED, TRIALS, TRACKS = 761, 1500, 7


def independent(fps):
    left=set(range(len(fps))); out=[]
    while left:
        v=min(left); out.append(v); left-={u for u in left if fps[u]&fps[v]}
    return out


def verify():
    r=Random(SEED); systems=repairs=chosen=feasible=shortages=cost_total=0
    selected_by_track=[0]*TRACKS
    for _ in range(TRIALS):
        p=r.randint(7,28); h=r.randint(1,min(6,p)); beta=r.randint(1,6)
        loads=[0]*p; fps=[]; tracks=[]; costs=[]
        for _ in range(r.randint(3,50)):
            avail=[x for x in range(p) if loads[x]<beta]
            if not avail: break
            fp=set(r.sample(avail,r.randint(1,min(h,len(avail)))))
            for x in fp: loads[x]+=1
            track=r.randrange(TRACKS); vector=[0]*TRACKS; vector[track]=r.randint(0,8)
            fps.append(fp); tracks.append(track); costs.append(vector)
        if not fps: continue
        assert max(Counter(x for f in fps for x in f).values())<=beta
        bound=h*(beta-1)
        assert all(sum(i!=j and bool(f&g) for j,g in enumerate(fps))<=bound for i,f in enumerate(fps))
        I=independent(fps)
        assert len(I)>=ceil(len(fps)/(bound+1))
        assert all(not(fps[i]&fps[j]) for a,i in enumerate(I) for j in I[a+1:])
        assert all(sum(value!=0 for value in costs[i])<=1 for i in I)
        C=[sum(costs[i][a] for i in I) for a in range(TRACKS)]
        B=[r.randint(0,c+4) for c in C]
        if all(c<=B[a] for a,c in enumerate(C)): feasible+=1
        else:
            shortages+=1; a=next(a for a,c in enumerate(C) if c>B[a]); assert C[a]-B[a]>0
        systems+=1; repairs+=len(fps); chosen+=len(I); cost_total+=sum(C)
        for i in I: selected_by_track[tracks[i]]+=1
    kappa=[3,4,5,6,7,8,9]; deficit=r.randint(0,30); initial=deficit
    churn=gain=ledger=0; track_gain=[0]*TRACKS; track_cost=[0]*TRACKS
    for _ in range(5000):
        u=r.randint(0,8); available=deficit+u; g=r.randint(0,available)
        gains=[0]*TRACKS
        for _ in range(g): gains[r.randrange(TRACKS)]+=1
        for s,gs in enumerate(gains):
            cost=r.randint(0,kappa[s]*gs); track_gain[s]+=gs; track_cost[s]+=cost; ledger+=cost
        deficit=available-g; churn+=u; gain+=g
        assert gain<=initial+churn
        assert all(track_cost[s]<=kappa[s]*track_gain[s] for s in range(TRACKS))
        assert ledger<=max(kappa)*gain
    return systems,repairs,chosen,feasible,shortages,cost_total,selected_by_track,churn,gain,ledger

if __name__=='__main__':
    print('AC footprint-cost checks passed:', *verify())
