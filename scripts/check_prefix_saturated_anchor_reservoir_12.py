#!/usr/bin/env python3
from itertools import combinations
from math import gcd

P=(6,7,0,4,9,2,11,10,1,5,8,3)
Q=(2,9,11,7,0,4,10,8,3,6,1,5)
PAIRING=(11,9,10,8,5,6,7,4,3,2,1,0)
SOURCE=tuple((row,P[row]) for row in range(12))+tuple((row,Q[row]) for row in range(12))
ANCHOR_PAIRS=tuple(((row,P[row]),(PAIRING[row],Q[PAIRING[row]])) for row in range(12))

def collinear(a,b,c): return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
def compositions(total):
    if total==0: yield (); return
    for first in range(1,total+1):
        for tail in compositions(total-first): yield (first,)+tail
def primitive_direction(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; g=gcd(abs(dx),abs(dy)); return dx//g,dy//g

assert sorted(P)==list(range(12)) and sorted(Q)==list(range(12))
assert all(P[i]!=Q[i] for i in range(12))
assert len(set(SOURCE))==24
assert all(sum(x==r for x,_ in SOURCE)==2 for r in range(12))
assert all(sum(y==c for _,y in SOURCE)==2 for c in range(12))
assert all(not collinear(*triple) for triple in combinations(SOURCE,3))
assert len({p for pair in ANCHOR_PAIRS for p in pair})==24
assert all(a[0]!=b[0] and a[1]!=b[1] for a,b in ANCHOR_PAIRS)

def embed(lengths):
    points=list(SOURCE); labels=[None]*len(points)
    for run,(a,b) in enumerate(ANCHOR_PAIRS[:len(lengths)]):
        labels[points.index(a)]=run; labels[points.index(b)]=run
    used_rows={x for x,_ in points}; used_cols={y for _,y in points}
    for run,length in enumerate(lengths):
        a,b=ANCHOR_PAIRS[run]; dx,dy=primitive_direction(a,b); inserted=0
        for magnitude in range(1,10000):
            for multiplier in (magnitude,-magnitude):
                candidate=(a[0]+multiplier*dx,a[1]+multiplier*dy)
                if candidate in points or candidate[0] in used_rows or candidate[1] in used_cols: continue
                bad=False
                for i,j in combinations(range(len(points)),2):
                    if collinear(points[i],points[j],candidate) and not(labels[i]==run and labels[j]==run): bad=True; break
                if bad: continue
                points.append(candidate); labels.append(run); used_rows.add(candidate[0]); used_cols.add(candidate[1]); inserted+=1; break
            if inserted==length: break
        assert inserted==length
    for i,j,k in combinations(range(len(points)),3):
        if collinear(points[i],points[j],points[k]): assert labels[i] is not None and labels[i]==labels[j]==labels[k]
    return points

count=0; maximum=0
for lengths in compositions(12):
    points=embed(lengths); count+=1
    maximum=max(maximum,max(max(abs(x),abs(y)) for x,y in points))
assert count==2048 and maximum==187

print({
    "saturated_source_grid_size":12,
    "saturated_source_cells":24,
    "row_degree":2,"column_degree":2,"source_no_three_in_line":True,
    "disjoint_anchor_pairs":12,
    "unary_run_compositions_checked":count,
    "cross_run_collinear_triples":0,
    "maximum_coordinate":maximum,
    "finite_certified_pair_counts":(11,12),
    "remaining_gap":"the eleven- and twelve-pair witnesses do not yet form an infinite compatible saturated source family",
    "evidence_level":"explicit_twelve_pair_saturated_anchor_reservoir",
    "status":"passed",
})
