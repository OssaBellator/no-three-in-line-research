#!/usr/bin/env python3
from functools import lru_cache
import collections, math, random

SEED=28004
SYSTEMS=2600
TYPED=False
TYPE_LABELS=('A', 'B')
FIELD_NAMES=('donor address', 'remedy address', 'height address', 'cause geometry')

def matching(adj, nt):
    @lru_cache(None)
    def dp(i, used):
        if i==len(adj): return 0
        best=dp(i+1,used)
        free=adj[i]&~used
        while free:
            bit=free&-free; free-=bit
            best=max(best,1+dp(i+1,used|bit))
        return best
    return dp(0,0)

def completion_cost(adj, nt):
    @lru_cache(None)
    def dp(i, used):
        if i==len(adj): return 0
        return min((0 if (adj[i]>>t)&1 else 1)+dp(i+1,used|(1<<t))
                   for t in range(nt) if not (used>>t)&1)
    return dp(0,0)

def audit():
    rng=random.Random(SEED); z=collections.Counter()
    for _ in range(SYSTEMS):
        z["systems"]+=1; complete=True; deficient=False
        for _ in range(rng.randint(2,4)):
            z["classes"]+=1
            ni=rng.randint(1,5); nt=ni+rng.randint(0,2)
            inc=[(rng.choice(TYPE_LABELS) if TYPED else None,
                  tuple(rng.randrange(2) for _ in range(4))) for _ in range(ni)]
            tok=[]
            for _ in range(nt):
                tc=("*" if rng.random()<.58 else rng.choice(TYPE_LABELS)) if TYPED else None
                tok.append((tc,tuple(-1 if rng.random()<.68 else rng.randrange(2) for _ in range(4))))
            adj=[]; reason={}
            for i,(typ,req) in enumerate(inc):
                mask=0
                for t,(tc,cap) in enumerate(tok):
                    bad=[]
                    if TYPED and tc not in ("*",typ): bad.append(0)
                    off=1 if TYPED else 0
                    bad += [off+j for j,(a,b) in enumerate(zip(req,cap)) if b!=-1 and a!=b]
                    if bad: reason[i,t]=min(bad)
                    else: mask|=1<<t
                adj.append(mask)
            z["incidences"]+=ni; z["tokens"]+=nt
            z["old_edges"]+=sum(x.bit_count() for x in adj)
            mm=matching(tuple(adj),nt); canon=None
            for s in range(1,1<<ni):
                z["subset_checks"]+=1; nbh=0
                for i in range(ni):
                    if (s>>i)&1: nbh|=adj[i]
                d=s.bit_count()-nbh.bit_count()
                if mm==ni: assert d<=0
                else:
                    key=(-d,s.bit_count(),s)
                    if canon is None or key<canon[0]: canon=(key,s,nbh,d)
            if mm==ni: continue
            complete=False; deficient=True; z["deficient_classes"]+=1
            _,core,nbh,delta=canon
            assert delta==ni-mm and delta>0
            p=(core-1)&core
            while p:
                z["proper_core_checks"]+=1; pn=0
                for i in range(ni):
                    if (p>>i)&1: pn|=adj[i]
                assert p.bit_count()-pn.bit_count()<delta
                p=(p-1)&core
            ids=[i for i in range(ni) if (core>>i)&1]
            assert matching(tuple(adj[i]&nbh for i in ids),nt)==nbh.bit_count()
            outside=((1<<nt)-1)&~nbh; oc=outside.bit_count()
            assert oc>=delta
            counts=collections.Counter(); by=collections.defaultdict(collections.Counter)
            for i in ids:
                for t in range(nt):
                    if (outside>>t)&1:
                        assert not (adj[i]>>t)&1
                        f=reason[i,t]; counts[f]+=1; by[i][f]+=1
            rect=core.bit_count()*oc; q=len(FIELD_NAMES)
            assert max(counts.values())>=math.ceil(rect/q)
            assert max(max(v.values()) for v in by.values())>=math.ceil(oc/q)
            assert completion_cost(tuple(adj),nt)==delta
            z["cores"]+=1; z["deficit_units"]+=delta; z["core_uses"]+=core.bit_count()
            z["neighbor_tokens"]+=nbh.bit_count(); z["outside_tokens"]+=oc
            z["missing_rectangle_pairs"]+=rect; z["heavy_field_pairs"]+=max(counts.values())
            z["mincost_checks"]+=1
            if TYPED and len({inc[i][0] for i in ids})>1: z["mixed_typed_cores"]+=1
        z["complete_systems"]+=complete; z["deficient_systems"]+=deficient
    return z

if __name__=="__main__":
    z=audit()
    keys=("systems classes incidences tokens old_edges subset_checks complete_systems "
          "deficient_systems deficient_classes cores deficit_units core_uses neighbor_tokens "
          "outside_tokens missing_rectangle_pairs heavy_field_pairs proper_core_checks mincost_checks").split()
    if TYPED: keys.append("mixed_typed_cores")
    for k in keys: print(f"{k}={z[k]}")
