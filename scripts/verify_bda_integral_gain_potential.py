#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from math import gcd, lcm
import random

rng=random.Random(20260729); S=defaultdict(int)
for _ in range(6000):
    n=rng.randint(2,7)
    P=[rng.randint(1,20) for _ in range(n)]
    g=0
    for x in P: g=gcd(g,x)
    P=[x//g for x in P]
    scale=rng.randint(1,12)
    q=[Fraction(x,scale) for x in P]
    L=1
    for x in q: L=lcm(L,x.denominator)
    Q=[int(L*x) for x in q]
    h=0
    for x in Q: h=gcd(h,x)
    Q=[x//h for x in Q]
    assert all(Q[i]*P[0]==P[i]*Q[0] for i in range(n))
    S['systems']+=1; S['vertices']+=n; S['integer_weight_units']+=sum(Q)
    for _ in range(rng.randint(n,3*n)):
        u,v=rng.randrange(n),rng.randrange(n)
        damping=Fraction(rng.randint(1,8),8)
        gain=damping*q[u]/q[v]
        assert Q[v]*gain<=Q[u]
        mass=rng.randint(1,20)
        out=(gain.numerator*mass)//gain.denominator
        assert Q[v]*out<=Q[u]*mass
        S['edges']+=1; S['transfers']+=1
    if rng.random()<.25:
        u,v=rng.randrange(n),rng.randrange(n)
        bad=Fraction(9,8)*q[u]/q[v]
        assert Q[v]*bad>Q[u]
        S['violations']+=1
    J=rng.randint(1,10); budget=sum(Q)*rng.randint(1,5)
    assert (budget//J)*J<=budget
print(dict(S))
