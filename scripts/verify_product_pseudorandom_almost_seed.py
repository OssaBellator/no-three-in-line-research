#!/usr/bin/env python3
"""Verify finite tuple-weight counts used in PX141."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb

def edge(p,x,y): return (x,y,(x-y)%p,(x+y)%p)
def compatible(es): return all(len({e[j] for e in es})==len(es) for j in range(4))

def shape(p,ordered):
    e1,e2,e3=ordered
    x1,y1=e1[:2]; x2,y2=e2[:2]; x3,y3=e3[:2]
    dx=(x2-x1)%p; dy=(y2-y1)%p
    if dx==0 or dy==0: return None
    r=dy*pow(dx,-1,p)%p
    t=(x3-x1)*pow(dx,-1,p)%p
    s=(y3-y1)*pow(dy,-1,p)%p
    return (r,t,s)

def compatible_shape(p,r,t,s):
    return r not in (0,1,p-1) and t not in (0,1) and s not in (0,1) and t!=r*s%p and (t-1)%p!=r*(s-1)%p and t!=(-r*s)%p and (t-1)%p!=(-r*(s-1))%p

def verify(p):
    edges=[edge(p,x,y) for x,y in product(range(p),repeat=2)]
    for e in edges:
        assert sum(e!=f and not compatible((e,f)) for f in edges)==4*(p-1)
    clean=[tr for tr in combinations(edges,3) if compatible(tr)]
    assert abs(len(clean)/p**3-comb(p,3))<=10*p*p
    counts=Counter(); norm1=Counter(); norm2=Counter()
    for tr in clean:
        for ordered in permutations(tr):
            sig=shape(p,ordered); counts[sig]+=1
            for e in tr: norm1[(sig,e)]+=1
            for pair in combinations(tr,2): norm2[(sig,tuple(sorted(pair)))]+=1
    for r,t,s in product(range(p),repeat=3):
        expected=p*p*(p-1) if compatible_shape(p,r,t,s) else 0
        assert counts[(r,t,s)]==expected
    assert max(norm1.values())<=6*(p-1)
    assert max(norm2.values())<=6
    print(f"p={p}: J={len(clean)}, shape totals and norms verified")

def main():
    for p in (5,7): verify(p)
    print("PX141 finite tuple-weight counts verified")

if __name__=="__main__": main()
