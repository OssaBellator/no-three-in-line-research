#!/usr/bin/env python3
from itertools import combinations
from math import gcd

P=(4,1,3,9,8,0,2,10,5,7,6)
Q=(6,3,1,8,5,10,0,2,7,9,4)
PAIRING=(1,0,3,2,5,4,8,6,7,10,9)
SOURCE=tuple((row,P[row]) for row in range(11))+tuple((row,Q[row]) for row in range(11))
ANCHOR_PAIRS=tuple(((row,P[row]),(PAIRING[row],Q[PAIRING[row]])) for row in range(11))

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def compositions(total):
    if total==0:
        yield (); return
    for first in range(1,total+1):
        for tail in compositions(total-first):
            yield (first,)+tail

def primitive_direction(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    divisor=gcd(abs(dx),abs(dy))
    return dx//divisor,dy//divisor

assert sorted(P)==list(range(11)) and sorted(Q)==list(range(11))
assert all(P[row]!=Q[row] for row in range(11))
assert len(set(SOURCE))==22
assert all(sum(point[0]==row for point in SOURCE)==2 for row in range(11))
assert all(sum(point[1]==column for point in SOURCE)==2 for column in range(11))
assert all(not collinear(*triple) for triple in combinations(SOURCE,3))
assert len({point for pair in ANCHOR_PAIRS for point in pair})==22
assert all(a[0]!=b[0] and a[1]!=b[1] for a,b in ANCHOR_PAIRS)

def embed(lengths):
    points=list(SOURCE); labels=[None]*len(points)
    for run,(a,b) in enumerate(ANCHOR_PAIRS[:len(lengths)]):
        labels[points.index(a)]=run; labels[points.index(b)]=run
    used_rows={x for x,_ in points}; used_columns={y for _,y in points}
    for run,length in enumerate(lengths):
        anchor,other=ANCHOR_PAIRS[run]
        dx,dy=primitive_direction(anchor,other)
        inserted=0
        for magnitude in range(1,10000):
            for multiplier in (magnitude,-magnitude):
                candidate=(anchor[0]+multiplier*dx,anchor[1]+multiplier*dy)
                if candidate in points or candidate[0] in used_rows or candidate[1] in used_columns:
                    continue
                bad=False
                for first,second in combinations(range(len(points)),2):
                    if not collinear(points[first],points[second],candidate):
                        continue
                    if labels[first]==run and labels[second]==run:
                        continue
                    bad=True; break
                if bad: continue
                points.append(candidate); labels.append(run)
                used_rows.add(candidate[0]); used_columns.add(candidate[1])
                inserted+=1; break
            if inserted==length: break
        assert inserted==length
    for first,second,third in combinations(range(len(points)),3):
        if not collinear(points[first],points[second],points[third]):
            continue
        assert labels[first] is not None and labels[first]==labels[second]==labels[third]
    return points

composition_count=0; maximum_coordinate=0
for lengths in compositions(11):
    points=embed(lengths); composition_count+=1
    maximum_coordinate=max(maximum_coordinate,max(max(abs(x),abs(y)) for x,y in points))
assert composition_count==1024 and maximum_coordinate==110

print({
    "saturated_source_grid_size":11,
    "saturated_source_cells":len(SOURCE),
    "row_degree":2,
    "column_degree":2,
    "source_no_three_in_line":True,
    "disjoint_anchor_pairs":len(ANCHOR_PAIRS),
    "unary_run_compositions_checked":composition_count,
    "cross_run_collinear_triples":0,
    "maximum_coordinate":maximum_coordinate,
    "remaining_gap":"this is a finite eleven-run saturated reservoir, not an asymptotic saturated source family compatible with every prime-patching scale",
    "evidence_level":"explicit_saturated_anchor_reservoir",
    "status":"passed",
})
