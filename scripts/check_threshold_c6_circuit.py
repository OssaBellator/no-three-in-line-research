#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations

SOURCE=((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))

def collinear(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def legal(p): return all(not collinear(*t) for t in combinations(tuple((r,p[r]) for r in range(4)),3))
def layer_matrix(layers):
    out=[[0]*4 for _ in range(4)]
    for p in layers:
        for r,c in enumerate(p): out[r][c]+=1
    return tuple(tuple(row) for row in out)
def distance(A,B): return sum(abs(A[r][c]-B[r][c]) for r in range(4) for c in range(4))

legal_layers=tuple(p for p in permutations(range(4)) if legal(p))
legal_matrices={layer_matrix(tuple(legal_layers[i] for i in idxs)) for idxs in combinations_with_replacement(range(len(legal_layers)),4)}
minimum=min(distance(SOURCE,M) for M in legal_matrices)
targets=tuple(sorted(M for M in legal_matrices if distance(SOURCE,M)==minimum))
assert minimum==6 and len(targets)==8

subset_counts=[]
for target in targets:
    signed=[]
    for r in range(4):
        for c in range(4):
            d=target[r][c]-SOURCE[r][c]
            if d: signed.append((r,c,d))
    assert len(signed)==6 and sum(d for _,_,d in signed)==0
    balanced=[]
    for mask in range(1<<6):
        row=[0]*4; col=[0]*4
        for i,(r,c,d) in enumerate(signed):
            if mask>>i&1: row[r]+=d; col[c]+=d
        if row==[0]*4 and col==[0]*4: balanced.append(mask)
    assert balanced==[0,(1<<6)-1]
    subset_counts.append(len(balanced))

print({
    "nearest_legal_targets":len(targets),
    "signed_support_cells":6,
    "support_graph":"alternating C6",
    "subsets_per_support":64,
    "margin_preserving_subsets_per_support":2,
    "proper_nonempty_margin_preserving_subsets":0,
    "conclusion":"every target C6 is a circuit of the row-column transportation kernel and cannot be split into visible margin-preserving sub-edits",
    "remaining_gap":"a geometric source primitive must expose all six signed changes atomically while preserving no-three legality",
    "evidence_level":"exact_threshold_c6_circuit_indivisibility",
    "status":"passed",
})
