#!/usr/bin/env python3
"""Verify PX138--PX140: strong-complete exact-cover host."""
from itertools import combinations, product

def edge(p,x,y):
    return (x,y,(x-y)%p,(x+y)%p)

def compatible(edges):
    return all(len({e[part] for e in edges})==len(edges) for part in range(4))

def affine(p,r,b):
    return tuple((r*x+b)%p for x in range(p))

def strong(f):
    p=len(f); target=set(range(p))
    return set(f)==target and {(x-f[x])%p for x in range(p)}==target and {(x+f[x])%p for x in range(p)}==target

def verify_host(p):
    all_edges=tuple(edge(p,x,y) for x,y in product(range(p),repeat=2))
    for part in range(4):
        for value in range(p):
            assert sum(e[part]==value for e in all_edges)==p
    vertices=[(part,value) for part in range(4) for value in range(p)]
    for a,b in combinations(vertices,2):
        if a[0]==b[0]: continue
        assert sum(e[a[0]]==a[1] and e[b[0]]==b[1] for e in all_edges)<=1
    allowed=[r for r in range(p) if r not in (0,1,p-1)]
    maps=[affine(p,r,b) for r in allowed for b in range(p)]
    assert len(maps)==p*(p-3) and all(strong(f) for f in maps)
    for x,y in product(range(p),repeat=2):
        assert sum(f[x]==y for f in maps)==p-3
    pairs=[]
    for e1,e2 in combinations(all_edges,2):
        if compatible((e1,e2)):
            pairs.append((e1,e2))
            assert sum(f[e1[0]]==e1[1] and f[e2[0]]==e2[1] for f in maps)==1
    for e1,e2 in pairs[:min(500,len(pairs))]:
        x1,y1=e1[:2]; x2,y2=e2[:2]
        ix=pow((x2-x1)%p,-1,p); iy=pow((y2-y1)%p,-1,p)
        for x3,y3 in product(range(p),repeat=2):
            e3=edge(p,x3,y3)
            if not compatible((e1,e2,e3)): continue
            t=(x3-x1)*ix%p; s=(y3-y1)*iy%p
            count=sum(f[x1]==y1 and f[x2]==y2 and f[x3]==y3 for f in maps)
            assert count==(1 if t==s else 0)
    for f in maps[:10]:
        matching=tuple(edge(p,x,f[x]) for x in range(p))
        for k in range(4):
            used=[{e[part] for e in matching[:k]} for part in range(4)]
            for part in range(4):
                for value in range(p):
                    if value in used[part]: continue
                    degree=sum(e[part]==value and all(e[q] not in used[q] for q in range(4)) for e in all_edges)
                    assert degree>=p-3*k
    print(f"p={p}: exact-cover host and affine laws verified")

def main():
    for p in (5,7,11): verify_host(p)
    print("PX138--PX140 verified")

if __name__=="__main__": main()
