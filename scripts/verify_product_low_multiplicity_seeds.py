#!/usr/bin/env python3
"""Verify PX132--PX137 low-multiplicity strong-complete seeds."""
from collections import Counter
from math import ceil

SEEDS = {
    13: (0,2,4,9,7,12,3,11,6,1,5,10,8),
    17: (0,9,4,10,7,14,16,2,6,15,11,5,8,12,1,3,13),
    19: (13,9,17,6,1,11,8,14,0,2,5,15,10,12,4,16,7,3,18),
    23: (2,6,12,14,11,21,18,20,0,4,8,10,16,9,5,1,19,17,15,13,3,22,7),
    29: (11,13,28,18,2,7,23,26,16,9,17,4,1,12,24,19,10,20,5,3,25,27,14,8,15,21,6,22,0),
    31: (0,10,22,5,14,16,9,29,6,26,17,1,18,27,19,23,3,12,2,4,8,13,15,24,20,7,30,21,25,28,11),
    37: (0,10,17,25,21,19,8,32,35,12,36,22,33,31,24,2,7,14,11,15,6,28,20,27,16,30,1,9,4,23,29,26,3,34,13,18,5),
    41: (0,14,28,5,22,39,18,29,11,37,27,7,1,19,38,10,13,16,25,34,2,30,33,17,40,23,31,15,6,9,20,4,36,12,35,26,3,21,24,8,32),
    43: (0,28,21,23,3,12,24,30,13,42,32,4,1,41,26,7,22,15,39,14,11,34,19,38,25,27,8,36,16,33,40,17,35,6,2,18,10,31,9,20,5,37,29),
    47: (0,45,36,41,12,21,7,29,13,1,40,32,5,27,18,3,35,6,17,37,14,16,31,26,4,23,43,34,30,42,11,46,10,39,44,20,9,2,24,15,19,25,38,33,8,22,28),
    53: (0,27,4,26,48,16,5,13,22,7,3,38,25,41,30,52,1,14,21,31,40,51,43,28,18,11,35,19,10,46,49,32,39,2,23,45,12,8,17,47,36,6,20,15,24,33,50,9,29,44,37,34,42),
}
EXPECTED = {
    13:(28,8),17:(28,6),19:(32,6),23:(44,8),
    29:(54,9),31:(44,6),37:(54,7),41:(64,8),
    43:(76,9),47:(82,9),53:(80,7),
}

def strong(f):
    p=len(f)
    target=list(range(p))
    return sorted(f)==target and sorted((x-f[x])%p for x in range(p))==target and sorted((x+f[x])%p for x in range(p))==target

def multiplicities(f):
    p=len(f)
    inv=[0]+[pow(x,-1,p) for x in range(1,p)]
    mu=Counter(); tau=Counter()
    for u in range(p):
        for v in range(p):
            if u==v: continue
            d=(v-u)%p; fd=(f[v]-f[u])%p
            r=fd*inv[d]%p; mu[r]+=1
            for t in range(2,p):
                w=(u+t*d)%p
                s=(f[w]-f[u])*inv[fd]%p
                tau[(r,t,s)]+=1
    return max(mu.values()),max(tau.values())

def primes(limit):
    return [n for n in range(2,limit+1) if all(n%d for d in range(2,int(n**0.5)+1))]

def main():
    for p,f in SEEDS.items():
        assert strong(f)
        assert multiplicities(f)==EXPECTED[p]
        mu,tau=EXPECTED[p]
        print(f"p={p}: mu={mu}, tau={tau}, K2={mu/p:.6f}, K3={(p-2)*tau/p:.6f}")
    for p in primes(101):
        if p<7: continue
        assert ceil(p*(p-1)/((p-3)*(p-2)))==(3 if p==7 else 2)
    print("PX132--PX137 verified")

if __name__=="__main__":
    main()
