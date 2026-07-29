#!/usr/bin/env python3
"""Finite checks for GC2mt--GC2mw."""
from collections import Counter, defaultdict, deque
import random

def run(seed=97,cases=2500):
 r=random.Random(seed); s=Counter()
 for _ in range(cases):
  m,b,c,x=r.randint(1,8),r.randint(0,8),r.randint(0,6),r.randint(0,4); U=[f'u{i}' for i in range(m)]; A=U+[f'a{i}' for i in range(b)]; B=[f'b{i}' for i in range(b)]; R=A+[f'c{i}' for i in range(c)]; T=B+[f'd{i}' for i in range(c)]+[f'z{i}' for i in range(m+x)]; M={(f'a{i}',f'b{i}') for i in range(b)}|{(f'c{i}',f'd{i}') for i in range(c)}; E=set(M)
  for a in A:
   for t in B:
    if r.random()<.45:E.add((a,t))
  mt={t:a for a,t in M}; sr,st,q=set(U),set(),deque(U)
  while q:
   y=q.popleft()
   if y in R:
    for a,t in E:
     if a==y and (a,t) not in M and t not in st:st.add(t);q.append(t)
   elif y in mt and mt[y] not in sr:sr.add(mt[y]);q.append(mt[y])
  assert {t for a,t in E if a in sr}==st and len(sr)-len(st)==m
  Z=[t for t in T if t not in {v for u,v in M}];assert len(Z)>=m and set(Z).isdisjoint(st) and all((a,t) not in E for a in U for t in Z)
  qn=r.randint(1,6); L=[(a,t,r.randrange(max(1,m*len(Z)//3)),r.randrange(qn)) for a in U for t in Z]; C=Counter(p for a,t,w,p in L);p=max(C,key=C.get);F=[e for e in L if e[3]==p];assert len(F)*qn>=m*len(Z)
  a,t,w,p=F[0];assert len(M|{(a,t)})==len(M)+1;r.shuffle(F);ur,ut,N=set(),set(),[]
  for e in F:
   a,t,w,p=e
   if a not in ur and t not in ut:ur.add(a);ut.add(t);N.append(e)
  by=defaultdict(list)
  for e in N:by[e[2]].append(e)
  mu=r.randint(1,4);Q=max(by.values(),key=len) if by and max(map(len,by.values()))>=mu+1 else [v[0] for v in by.values()];add={(a,t) for a,t,w,p in Q};assert len(M|add)==len(M)+len(add);s['systems']+=1;s['free_pairs']+=m*len(Z);s['predicate_pairs']+=len(F);s['repair_gain']+=len(add)
 print(dict(s))
if __name__=='__main__':run()
