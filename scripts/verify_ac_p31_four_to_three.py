#!/usr/bin/env python3
import json
from itertools import combinations
from pathlib import Path

def col(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def potential(r,b):
 p=[(i+1,y) for i,y in enumerate(r)]+[(i+1,y) for i,y in enumerate(b)]
 return sum(col(*t) for t in combinations(p,3))
def main():
 d=json.loads(Path('data/ac-p31-four-to-three.json').read_text());r=[y for _,y in d['start_red']];b=[y for _,y in d['start_blue']]
 assert potential(r,b)==4
 for k,m in enumerate(d['moves']):
  l=m[0];i,j=map(int,m[2:].split(','));i-=1;j-=1;a=b if l=='b' else r;o=r if l=='b' else b
  assert a[j]!=o[i] and a[i]!=o[j];a[i],a[j]=a[j],a[i];assert potential(r,b)==d['potentials'][k+1]
 assert max(d['potentials'])==9 and potential(r,b)==3
 assert [[i+1,y] for i,y in enumerate(r)]==d['final_red'];assert [[i+1,y] for i,y in enumerate(b)]==d['final_blue']
 print('AC p31 four-to-three audit');print(f"moves: {len(d['moves'])}");print('maximum_potential: 9');print('final_potential: 3')
if __name__=='__main__':main()
