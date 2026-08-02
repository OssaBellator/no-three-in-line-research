#!/usr/bin/env python3
from itertools import combinations
from math import gcd

P=(9,4,7,3,0,1,12,8,11,10,2,6,5)
Q=(7,12,9,1,4,3,8,0,2,11,5,10,6)
PAIRING=(1,0,3,2,5,4,7,8,6,10,12,9,11)
N=13
SOURCE=tuple((row,P[row]) for row in range(N))+tuple((row,Q[row]) for row in range(N))
ANCHOR_PAIRS=tuple(((row,P[row]),(PAIRING[row],Q[PAIRING[row]])) for row in range(N))

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

assert sorted(P)==list(range(N)) and sorted(Q)==list(range(N))
assert all(P[row]!=Q[row] for row in range(N))
assert len(set(SOURCE))==2*N
assert all(sum(point[0]==row for point in SOURCE)==2 for row in range(N))
assert all(sum(point[1]==column for point in SOURCE)==2 for column in range(N))
assert all(not collinear(*triple) for triple in combinations(SOURCE,3))
assert len({point for pair in ANCHOR_PAIRS for point in pair})==2*N
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
        for magnitude in range(1,50000):
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
        if collinear(points[first],points[second],points[third]):
            assert labels[first] is not None and labels[first]==labels[second]==labels[third]
    return points

composition_count=0; maximum_coordinate=0
for lengths in compositions(N):
    points=embed(lengths); composition_count+=1
    maximum_coordinate=max(maximum_coordinate,max(max(abs(x),abs(y)) for x,y in points))
assert composition_count==4096 and maximum_coordinate==180

q_inverse={value:index for index,value in enumerate(Q)}
sigma=tuple(q_inverse[P[row]] for row in range(N))
components=[]; seen=set()
for row in range(N):
    if row in seen: continue
    component=[]; current=row
    while current not in seen:
        seen.add(current); component.append(current); current=sigma[current]
    components.append(tuple(component))
assert sorted(map(len,components)) == [2,2,4,5]

small_components=[component for component in components if len(component)==2]
assert len(small_components)==2
for component in small_components:
    removed_rows=set(component)
    removed_columns={P[row] for row in component} | {Q[row] for row in component}
    assert len(removed_columns)==2
    remaining=[point for point in SOURCE if point[0] not in removed_rows and point[1] not in removed_columns]
    assert len(remaining)==22
    assert all(sum(point[0]==row for point in remaining)==2 for row in set(range(N))-removed_rows)
    assert all(sum(point[1]==column for point in remaining)==2 for column in set(range(N))-removed_columns)
    assert all(not collinear(*triple) for triple in combinations(remaining,3))

component_index={row:index for index,component in enumerate(components) for row in component}
within_component_options={
    row: tuple(other for other in range(N)
               if component_index[other]==component_index[row]
               and other!=row and Q[other]!=P[row])
    for row in range(N)
}
assert any(not within_component_options[row] for component in small_components for row in component)

print({
    "saturated_source_grid_size":N,
    "saturated_source_cells":len(SOURCE),
    "row_degree":2,
    "column_degree":2,
    "source_no_three_in_line":True,
    "disjoint_anchor_pairs":len(ANCHOR_PAIRS),
    "unary_run_compositions_checked":composition_count,
    "cross_run_collinear_triples":0,
    "maximum_coordinate":maximum_coordinate,
    "incidence_component_pair_sizes":tuple(sorted(map(len,components))),
    "induced_eleven_pair_subsources":len(small_components),
    "component_respecting_anchor_pairing":False,
    "remaining_gap":"the source nests from thirteen to eleven pairs, but the anchor pairing cannot descend componentwise and no uniform all-size extension rule is known",
    "evidence_level":"explicit_thirteen_pair_saturated_anchor_reservoir_with_nesting_obstruction",
    "status":"passed",
})
