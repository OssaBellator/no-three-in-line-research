#!/usr/bin/env python3
"""Deterministic adequacy audit for the BDA logical compatibility schema."""
from math import prod
from random import Random

SYSTEMS, SEED = 2500, 29002
FIELDS = ('physical_source','numerator_weight','rational_gain','damping_factor','restoration_class','epoch')
RADICES = (3,4,3,5)
EXPECTED = {'systems':2500,'capacity_obstructions':2400,'capacity_feasible':100,'omission_witnesses':2500,'lossless_separations':2500,'packed_samples':100,'total_logical_states':1838228}


def audit():
    rng=Random(SEED); out={k:0 for k in EXPECTED}; capacity=prod(RADICES)
    buckets=[[] for _ in RADICES]
    for i in range(len(FIELDS)): buckets[i%4].append(i)
    for _ in range(SYSTEMS):
        domains=[rng.randint(2,4) for _ in FIELDS]; total=prod(domains)
        out['systems']+=1; out['total_logical_states']+=total
        out['capacity_obstructions' if total>capacity else 'capacity_feasible']+=1
        f=rng.randrange(len(FIELDS)); a=[rng.randrange(d) for d in domains]; b=a.copy(); b[f]=(b[f]+1)%domains[f]
        enc=lambda x: tuple(tuple(x[i] for i in q) for q in buckets)
        omit=lambda x: tuple(x[i] for i in range(len(x)) if i!=f)
        assert enc(a)!=enc(b) and omit(a)==omit(b)
        out['omission_witnesses']+=1; out['lossless_separations']+=1
        if total<=capacity:
            idx=0; mult=1
            for value,domain in zip(a,domains): idx+=value*mult; mult*=domain
            for radix in RADICES: idx//=radix
            assert idx==0; out['packed_samples']+=1
    return out


def main():
    got=audit(); assert got==EXPECTED
    print('track=BDA logical_blocks=6 audit_coordinates=4 audit_capacity=180 binary_states=64 binary_status=encoder_required')
    print(got)


if __name__=='__main__': main()
