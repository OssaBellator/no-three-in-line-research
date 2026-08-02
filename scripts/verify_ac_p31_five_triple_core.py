#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

R=[17,25,23,18,29,15,8,28,21,13,9,4,20,27,1,12,7,19,3,5,26,30,2,11,14,6,24,16,22,10]
B=[12,10,20,9,7,25,4,2,15,1,3,26,8,23,30,16,27,24,29,11,14,18,6,5,22,28,21,13,17,19]

def col(a,b,c): return (b[1]-a[1])*(c[2]-a[2])==(b[2]-a[2])*(c[1]-a[1])
def triples(r,b):
    p=[('r',i+1,y) for i,y in enumerate(r)]+[('b',i+1,y) for i,y in enumerate(b)]
    return {tuple(sorted(t)) for t in combinations(p,3) if col(*t)}
base=triples(R,B)
assert len(base)==5
pot=Counter(); destroyed=Counter(); best=None; legal=0
for layer,arr,other in [('r',R,B),('b',B,R)]:
    for i,j in combinations(range(30),2):
        if arr[j]==other[i] or arr[i]==other[j]: continue
        legal+=1; n=arr.copy(); n[i],n[j]=n[j],n[i]
        t=triples(n,B) if layer=='r' else triples(R,n)
        pot[len(t)]+=1; destroyed[len(base-t)]+=1
        key=(len(t),-len(base-t),len(t-base),layer,i+1,j+1)
        if best is None or key<best: best=key
assert legal==812
assert pot==Counter({14:126,13:118,15:110,16:87,12:86,11:65,17:62,10:48,9:30,18:27,19:25,7:8,20:7,8:5,21:4,22:2,6:1,23:1})
assert destroyed==Counter({0:475,1:281,2:53,3:3})
assert best==(6,-3,4,'r',3,27)
print('AC p31 five-triple core audit')
print('triples: 5')
print('legal_immediate_switches: 812')
print('improving_switches: 0')
print('best_move: r:3,27')
print('best_potential: 6')
