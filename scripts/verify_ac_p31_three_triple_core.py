#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
R=[14,15,9,18,8,25,29,3,4,13,19,2,23,28,1,12,7,24,6,17,11,26,30,5,22,27,20,16,21,10]
B=[18,10,24,6,14,15,23,20,25,1,9,4,7,29,30,27,28,19,2,5,3,13,21,11,8,26,12,22,17,16]
def col(a,b,c):return (b[1]-a[1])*(c[2]-a[2])==(b[2]-a[2])*(c[1]-a[1])
def triples(r,b):
 p=[('r',i+1,y) for i,y in enumerate(r)]+[('b',i+1,y) for i,y in enumerate(b)]
 return {tuple(sorted(t)) for t in combinations(p,3) if col(*t)}
base=triples(R,B);assert len(base)==3
pd=Counter();dd=Counter();best=[];legal=0;mn=999
for layer,arr,other in [('r',R,B),('b',B,R)]:
 for i,j in combinations(range(30),2):
  if arr[j]==other[i] or arr[i]==other[j]:continue
  legal+=1;n=arr.copy();n[i],n[j]=n[j],n[i];t=triples(n,B) if layer=='r' else triples(R,n);p=len(t);d=len(base-t);c=len(t-base);pd[p]+=1;dd[d]+=1
  if p<mn:mn=p;best=[(layer,i+1,j+1,d,c)]
  elif p==mn:best.append((layer,i+1,j+1,d,c))
assert legal==810 and mn==5
assert pd==Counter({12:139,13:111,11:109,10:105,14:79,9:70,15:52,8:45,16:33,7:24,17:18,6:11,18:7,5:4,19:2,20:1})
assert dd==Counter({0:583,1:216,2:11})
assert sorted(best)==[('b',3,7,0,2),('b',21,26,0,2),('r',7,17,2,4),('r',7,27,1,3)]
print('AC p31 three-triple core audit');print('triples: 3');print('legal_immediate_switches: 810');print('improving_switches: 0');print('least_potential: 5')
