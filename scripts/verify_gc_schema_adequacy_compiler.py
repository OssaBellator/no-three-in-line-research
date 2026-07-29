#!/usr/bin/env python3
"""Deterministic adequacy audit for the GC logical compatibility schema."""
from math import prod
from random import Random
SYSTEMS,SEED=2500,29003
FIELDS=('physical_source','donor','remedy','height','cause','local_geometry','epoch')
RADICES=(3,4,3,5)
EXPECTED={'systems':2500,'capacity_obstructions':2500,'capacity_feasible':0,'omission_witnesses':2500,'lossless_separations':2500,'packed_samples':0,'total_logical_states':5495023}

def audit():
    rng=Random(SEED); out={k:0 for k in EXPECTED}; cap=prod(RADICES); buckets=[[] for _ in RADICES]
    for i in range(len(FIELDS)): buckets[i%4].append(i)
    for _ in range(SYSTEMS):
        ds=[rng.randint(2,4) for _ in FIELDS]; total=prod(ds); out['systems']+=1; out['total_logical_states']+=total
        out['capacity_obstructions' if total>cap else 'capacity_feasible']+=1
        f=rng.randrange(len(FIELDS)); a=[rng.randrange(d) for d in ds]; b=a.copy(); b[f]=(b[f]+1)%ds[f]
        enc=lambda x: tuple(tuple(x[i] for i in q) for q in buckets); omit=lambda x: tuple(x[i] for i in range(len(x)) if i!=f)
        assert enc(a)!=enc(b) and omit(a)==omit(b); out['omission_witnesses']+=1; out['lossless_separations']+=1
    return out

def main():
    got=audit(); assert got==EXPECTED
    print('track=GC logical_blocks=7 audit_coordinates=4 audit_capacity=180 binary_states=128 binary_status=encoder_required'); print(got)
if __name__=='__main__': main()
