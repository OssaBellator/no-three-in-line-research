#!/usr/bin/env python3
"""Finite checks for AC5gp--AC5gs."""
from collections import Counter, defaultdict, deque
import random

TRACKS=('AC','RI','BDA','GC','OP','SRR','SAS')

def track_case(rng,tag):
 m,b,c,x=rng.randint(1,7),rng.randint(0,7),rng.randint(0,5),rng.randint(0,3)
 U=[f'{tag}u{i}' for i in range(m)];A=U+[f'{tag}a{i}' for i in range(b)];B=[f'{tag}b{i}' for i in range(b)];R=A+[f'{tag}c{i}' for i in range(c)];T=B+[f'{tag}d{i}' for i in range(c)]+[f'{tag}z{i}' for i in range(m+x)]
 M={(f'{tag}a{i}',f'{tag}b{i}') for i in range(b)}|{(f'{tag}c{i}',f'{tag}d{i}') for i in range(c)};E=set(M)
 for a in A:
  for t in B:
   if rng.random()<.45:E.add((a,t))
 mt={t:a for a,t in M};sr,st,q=set(U),set(),deque(U)
 while q:
  y=q.popleft()
  if y in R:
   for a,t in E:
    if a==y and (a,t) not in M and t not in st:st.add(t);q.append(t)
  elif y in mt and mt[y] not in sr:sr.add(mt[y]);q.append(mt[y])
 assert {t for a,t in E if a in sr}==st and len(sr)-len(st)==m
 Z=[t for t in T if t not in {v for u,v in M}];assert len(Z)>=m and set(Z).isdisjoint(st) and all((a,t) not in E for a in U for t in Z)
 qn=rng.randint(1,6);L=[(a,t,rng.randrange(max(1,m*len(Z)//3)),rng.randrange(qn)) for a in U for t in Z];C=Counter(p for a,t,w,p in L);p=max(C,key=C.get);F=[e for e in L if e[3]==p];assert len(F)*qn>=m*len(Z)
 rng.shuffle(F);ur,ut,N=set(),set(),[]
 for e in F:
  a,t,w,p=e
  if a not in ur and t not in ut:ur.add(a);ut.add(t);N.append(e)
 by=defaultdict(list)
 for e in N:by[e[2]].append(e)
 mu=rng.randint(1,4);Q=max(by.values(),key=len) if by and max(map(len,by.values()))>=mu+1 else [v[0] for v in by.values()]
 add={(a,t) for a,t,w,p in Q};assert len(M|add)==len(M)+len(add)
 return m,len(Z),len(F),len(add)

def run(seed=113,macros=1500):
 rng=random.Random(seed);s=Counter();Delta=rng.randint(0,20);initial=Delta;sumU=sumg=0
 for j in range(macros):
  macro_gain=0
  for tag in TRACKS:
   m,z,e,g=track_case(rng,tag);s['track_systems']+=1;s['free_pairs']+=m*z;s['predicate_pairs']+=e;s['repair_gain']+=g;macro_gain+=g
  U=rng.randint(0,12);available=Delta+U;g=min(available,rng.randint(0,max(0,macro_gain)));Delta=available-g;sumU+=U;sumg+=g
  assert Delta>=0 and sumg<=initial+sumU
  s['macro_epochs']+=1;s['ledger_churn']+=U;s['ledger_gain']+=g
 print(dict(s),{'initial_deficit':initial,'final_deficit':Delta})
if __name__=='__main__':run()
