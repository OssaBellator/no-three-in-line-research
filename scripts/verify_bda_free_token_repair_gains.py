#!/usr/bin/env python3
"""Finite checks for BDA5hv--BDA5hy."""
from collections import Counter, defaultdict, deque
import random


def run(seed=89, cases=2500):
    rng, stats = random.Random(seed), Counter()
    for _ in range(cases):
        m, b, c, s = rng.randint(1, 8), rng.randint(0, 8), rng.randint(0, 6), rng.randint(0, 4)
        U=[f'u{i}' for i in range(m)]; A=U+[f'a{i}' for i in range(b)]; B=[f'b{i}' for i in range(b)]
        R=A+[f'c{i}' for i in range(c)]; T=B+[f'd{i}' for i in range(c)]+[f'z{i}' for i in range(m+s)]
        M={(f'a{i}',f'b{i}') for i in range(b)}|{(f'c{i}',f'd{i}') for i in range(c)}; E=set(M)
        for r in A:
            for t in B:
                if rng.random()<.45: E.add((r,t))
        mt={t:r for r,t in M}; sr,st,q=set(U),set(),deque(U)
        while q:
            x=q.popleft()
            if x in R:
                for r,t in E:
                    if r==x and (r,t) not in M and t not in st: st.add(t); q.append(t)
            elif x in mt and mt[x] not in sr: sr.add(mt[x]); q.append(mt[x])
        assert {t for r,t in E if r in sr}==st and len(sr)-len(st)==m
        free=[t for t in T if t not in {y for x,y in M}]
        assert len(free)>=m and set(free).isdisjoint(st) and all((r,t) not in E for r in U for t in free)
        qn=rng.randint(1,6); L=[(r,t,rng.randrange(max(1,m*len(free)//3)),rng.randrange(qn)) for r in U for t in free]
        pc=Counter(p for r,t,w,p in L); p=max(pc,key=pc.get); F=[e for e in L if e[3]==p]; assert len(F)*qn>=m*len(free)
        r,t,w,p=F[0]; assert len(M|{(r,t)})==len(M)+1
        rng.shuffle(F); ur,ut,N=set(),set(),[]
        for e in F:
            r,t,w,p=e
            if r not in ur and t not in ut: ur.add(r); ut.add(t); N.append(e)
        by=defaultdict(list)
        for e in N: by[e[2]].append(e)
        mu=rng.randint(1,4)
        Q=max(by.values(),key=len) if by and max(map(len,by.values()))>=mu+1 else [v[0] for v in by.values()]
        add={(r,t) for r,t,w,p in Q}; assert len(M|add)==len(M)+len(add)
        stats['systems']+=1; stats['free_pairs']+=m*len(free); stats['predicate_pairs']+=len(F); stats['repair_gain']+=len(add)
    print(dict(stats))

if __name__=='__main__': run()
