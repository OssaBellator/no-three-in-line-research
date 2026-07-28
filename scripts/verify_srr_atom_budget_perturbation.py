#!/usr/bin/env python3
from collections import defaultdict
import random

rng=random.Random(20260802); S=defaultdict(int)
for _ in range(7000):
    n=rng.randint(1,8)
    B=[rng.randint(0,12) for _ in range(n)]
    C=[rng.randint(0,12) for _ in range(n)]
    I=[rng.randint(0,4) for _ in range(n)]
    R=[rng.randint(0,min(4,B[i])) for i in range(n)]
    D=[rng.randint(0,4) for _ in range(n)]
    L=[rng.randint(0,min(4,C[i]+D[i])) for i in range(n)]
    B2=[B[i]+I[i]-R[i] for i in range(n)]
    C2=[C[i]+D[i]-L[i] for i in range(n)]
    psi=sum(max(0,B[i]-C[i]) for i in range(n))
    psi2=sum(max(0,B2[i]-C2[i]) for i in range(n))
    assert psi2<=psi+sum(I)+sum(L)
    for i in range(n):
        if B[i]<=C[i] and C[i]-B[i]+D[i]+R[i]>=I[i]+L[i]: assert B2[i]<=C2[i]
    S['systems']+=1; S['atoms']+=n; S['reference_burden']+=sum(B); S['reference_capacity']+=sum(C)
    S['burden_increase']+=sum(I); S['burden_removal']+=sum(R); S['capacity_deposit']+=sum(D); S['capacity_loss']+=sum(L)
    S['reference_shortfall']+=psi; S['actual_shortfall']+=psi2
    if psi2:
        a=min(i for i in range(n) if B2[i]>C2[i]); assert B2[a]-C2[a]>0
        S['overloaded_systems']+=1; S['local_witnesses']+=1
    else: S['paid_systems']+=1
print(dict(S))
