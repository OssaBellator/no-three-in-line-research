#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
R=[14,15,23,18,4,25,7,17,29,13,9,2,20,28,1,12,19,24,26,5,3,30,27,11,22,6,21,16,8,10]
B=[5,10,24,9,8,15,28,20,25,1,6,4,23,29,30,18,7,19,2,11,26,13,21,3,14,27,12,22,17,16]
def col(a,b,c):return (b[1]-a[1])*(c[2]-a[2])==(b[2]-a[2])*(c[1]-a[1])
def triples(r,b):
 p=[('r',i+1,y) for i,y in enumerate(r)]+[('b',i+1,y) for i,y in enumerate(b)]
 return {tuple(sorted(t)) for t in combinations(p,3) if col(*t)}
base=triples(R,B);assert len(base)==4
pd=Counter();dd=Counter();best=[];legal=0;mn=999
for layer,arr,other in [('r',R,B),('b',B,R)]:
 for i,j in combinations(range(30),2):
  if arr[j]==other[i] or arr[i]==other[j]:continue
  legal+=1;n=arr.copy();n[i],n[j]=n[j],n[i];t=triples(n,B) if layer=='r' else triples(R,n);p=len(t);d=len(base-t);c=len(t-base);pd[p]+=1;dd[d]+=1
  if p<mn:mn=p;best=[(layer,i+1,j+1,d,c)]
  elif p==mn:best.append((layer,i+1,j+1,d,c))
assert legal==810 and mn==6
assert pd==Counter({12:127,13:113,14:108,11:101,15:81,10:72,16:69,9:38,17:36,8:19,18:18,7:9,19:8,20:4,6:3,22:2,23:1,21:1})
assert dd==Counter({0:542,1:221,2:43,3:4})
assert sorted(best)==[('b',19,24,0,2),('r',5,7,1,3),('r',19,26,0,2)]
print('AC p31 four-triple core audit');print('triples: 4');print('legal_immediate_switches: 810');print('improving_switches: 0');print('least_potential: 6')
