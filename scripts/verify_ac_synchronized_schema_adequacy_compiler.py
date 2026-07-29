#!/usr/bin/env python3
"""Synchronized adequacy audit for the seven compatibility schemas."""
from math import prod
from random import Random

SYSTEMS,SEED=1500,29008
ORDER=('AC','RI','BDA','GC','OP','SRR','SAS')
SCHEMAS={
'AC':(('physical_source','certificate','defect','epoch','repair_class'),(3,4,3,5)),
'RI':(('repair_type','field_element_data','host_context','secant_line_address','coherence','collateral_class','epoch'),(2,4,3,5)),
'BDA':(('physical_source','numerator_weight','rational_gain','damping_factor','restoration_class','epoch'),(3,4,3,5)),
'GC':(('physical_source','donor','remedy','height','cause','local_geometry','epoch'),(3,4,3,5)),
'OP':(('repair_type','physical_source','unit_class','valuation_vector','holonomy','action_kernel','epoch'),(2,4,3,5)),
'SRR':(('candidate','witness_atom','conditioned_threshold','physical_source','tensor_cylinder','epoch'),(3,4,3,5)),
'SAS':(('repair_type','sign','boundary_profile','neutral_move','legality_class','physical_source','epoch'),(2,4,3,5)),
}
EXPECTED={'macro_systems':1500,'track_systems':10500,'logical_blocks':67500,'audit_coordinates':42000,'binary_capacity_obstructions':4500,'random_capacity_obstructions':9809,'random_capacity_feasible':691,'omission_witnesses':10500,'lossless_separations':10500,'packed_samples':691,'total_logical_states':15769493}


def audit():
    rng=Random(SEED); out={k:0 for k in EXPECTED}
    for _ in range(SYSTEMS):
        out['macro_systems']+=1
        for track in ORDER:
            fields,radices=SCHEMAS[track]; cap=prod(radices); out['track_systems']+=1; out['logical_blocks']+=len(fields); out['audit_coordinates']+=4
            if 2**len(fields)>cap: out['binary_capacity_obstructions']+=1
            ds=[rng.randint(2,4) for _ in fields]; total=prod(ds); out['total_logical_states']+=total
            out['random_capacity_obstructions' if total>cap else 'random_capacity_feasible']+=1
            f=rng.randrange(len(fields)); a=[rng.randrange(d) for d in ds]; b=a.copy(); b[f]=(b[f]+1)%ds[f]
            buckets=[[] for _ in radices]
            for i in range(len(fields)): buckets[i%4].append(i)
            enc=lambda x: tuple(tuple(x[i] for i in q) for q in buckets); omit=lambda x: tuple(x[i] for i in range(len(x)) if i!=f)
            assert enc(a)!=enc(b) and omit(a)==omit(b); out['omission_witnesses']+=1; out['lossless_separations']+=1
            if total<=cap:
                idx=0; mult=1
                for value,domain in zip(a,ds): idx+=value*mult; mult*=domain
                for radix in radices: idx//=radix
                assert idx==0; out['packed_samples']+=1
    return out


def main():
    got=audit(); assert got==EXPECTED
    bad=[t for t in ORDER if 2**len(SCHEMAS[t][0])>prod(SCHEMAS[t][1])]
    print(f'logical_blocks=45 audit_coordinates=28 binary_obstruction_tracks={",".join(bad)}')
    print(got)
if __name__=='__main__': main()
