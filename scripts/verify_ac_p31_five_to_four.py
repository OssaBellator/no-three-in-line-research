#!/usr/bin/env python3
import json
from itertools import combinations
from pathlib import Path

def col(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def potential(r,b):
    pts=[(i+1,y) for i,y in enumerate(r)]+[(i+1,y) for i,y in enumerate(b)]
    return sum(col(*t) for t in combinations(pts,3))
def parse(m):
    layer=m[0]; i,j=map(int,m[2:].split(',')); return layer,i-1,j-1

def main():
    rec=json.loads(Path('data/ac-p31-five-to-four.json').read_text())
    r=[y for _,y in rec['start_red']]; b=[y for _,y in rec['start_blue']]
    assert potential(r,b)==rec['start_potential']==5
    assert len(rec['moves'])+1==len(rec['potentials'])
    for k,m in enumerate(rec['moves']):
        layer,i,j=parse(m); arr=b if layer=='b' else r; other=r if layer=='b' else b
        assert arr[j]!=other[i] and arr[i]!=other[j]
        arr[i],arr[j]=arr[j],arr[i]
        assert potential(r,b)==rec['potentials'][k+1]
    assert max(rec['potentials'])==rec['maximum']==10
    assert potential(r,b)==rec['final_potential']==4
    assert [[i+1,y] for i,y in enumerate(r)]==rec['final_red']
    assert [[i+1,y] for i,y in enumerate(b)]==rec['final_blue']
    assert sorted(r)==list(range(1,31)) and sorted(b)==list(range(1,31))
    assert all(r[i]!=b[i] for i in range(30))
    print('AC p31 five-to-four audit')
    print(f"moves: {len(rec['moves'])}")
    print(f"maximum_potential: {max(rec['potentials'])}")
    print(f"final_potential: {potential(r,b)}")

if __name__=='__main__': main()
