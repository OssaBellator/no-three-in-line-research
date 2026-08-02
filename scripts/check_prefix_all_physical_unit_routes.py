#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import gcd

N = 13
P = (9,4,7,3,0,1,12,8,11,10,2,6,5)
Q = (7,12,9,1,4,3,8,0,2,11,5,10,6)
CID = (0,1,0,2,1,2,1,1,3,3,3,3,3)
DELETIONS = ((0,2),(3,5))
ALLOWED = tuple(
    tuple(target for target in range(N) if target != row and Q[target] != P[row])
    for row in range(N)
)


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def primitive(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    g=gcd(abs(dx),abs(dy))
    return dx//g,dy//g


def all_minimum_cross_matchings():
    result=[]
    image=[-1]*N
    def rec(row,used,crossings):
        if crossings>4:
            return
        if row==N:
            if crossings==4:
                result.append(tuple(image))
            return
        for target in ALLOWED[row]:
            if used>>target&1:
                continue
            image[row]=target
            rec(row+1,used|(1<<target),crossings+(CID[row]!=CID[target]))
    rec(0,0,0)
    return tuple(result)


def first_optimal_route(image, rows):
    index={row:i for i,row in enumerate(rows)}
    @lru_cache(None)
    def best(pos,mask):
        if pos==len(rows):
            return 0 if mask==(1<<len(rows))-1 else 99
        row=rows[pos]
        answer=99
        for target in ALLOWED[row]:
            if target not in index:
                continue
            bit=1<<index[target]
            if mask&bit:
                continue
            answer=min(answer,(target!=image[row])+best(pos+1,mask|bit))
        return answer
    assert best(0,0)==4
    route=[]
    mask=0
    for pos,row in enumerate(rows):
        goal=best(pos,mask)
        for target in ALLOWED[row]:
            if target not in index:
                continue
            bit=1<<index[target]
            if mask&bit:
                continue
            if (target!=image[row])+best(pos+1,mask|bit)==goal:
                route.append(target)
                mask|=bit
                break
    return tuple(route)


def embed_all_unit(rows, route):
    source=[]
    for row in rows:
        source.extend(((row,P[row]),(row,Q[row])))
    assert all(cross(*triple) for triple in combinations(source,3))
    rowset=set(rows)
    anchors=[]
    for row,target in zip(rows,route):
        assert target in rowset
        a,b=(row,P[row]),(target,Q[target])
        assert a[0]!=b[0] and a[1]!=b[1]
        anchors.append((a,b))
    assert len({point for pair in anchors for point in pair})==22

    points=list(source)
    labels=[-1]*len(points)
    for run,(a,b) in enumerate(anchors):
        for i,point in enumerate(points):
            if point==a or point==b:
                labels[i]=run
    occupied_rows={x for x,_ in points}
    occupied_cols={y for _,y in points}

    for run,(a,b) in enumerate(anchors):
        dx,dy=primitive(a,b)
        inserted=False
        for magnitude in range(1,50000):
            for sign in (1,-1):
                candidate=(a[0]+sign*magnitude*dx,a[1]+sign*magnitude*dy)
                if candidate[0] in occupied_rows or candidate[1] in occupied_cols or candidate in points:
                    continue
                bad=False
                for i in range(len(points)):
                    for j in range(i+1,len(points)):
                        if cross(points[i],points[j],candidate)==0:
                            if labels[i]==run and labels[j]==run:
                                continue
                            bad=True
                            break
                    if bad:
                        break
                if bad:
                    continue
                points.append(candidate)
                labels.append(run)
                occupied_rows.add(candidate[0])
                occupied_cols.add(candidate[1])
                inserted=True
                break
            if inserted:
                break
        if not inserted:
            return None

    for i,j,k in combinations(range(len(points)),3):
        if cross(points[i],points[j],points[k])==0:
            if not (labels[i]>=0 and labels[i]==labels[j]==labels[k]):
                return None
    return max(max(abs(x),abs(y)) for x,y in points)


matchings=all_minimum_cross_matchings()
assert len(matchings)==104
histograms=(Counter(),Counter())
passed=0
for image in matchings:
    for deletion_index,deletion in enumerate(DELETIONS):
        rows=tuple(row for row in range(N) if row not in deletion)
        route=first_optimal_route(image,rows)
        maximum=embed_all_unit(rows,route)
        assert maximum is not None
        histograms[deletion_index][maximum]+=1
        passed+=1

assert passed==208
print({
    "minimum_crossing_matchings":len(matchings),
    "deletion_cases":2,
    "physical_matching_deletion_cases":passed,
    "deterministic_selector":"lexicographically first optimal radius-four route",
    "composition":"eleven unit runs",
    "all_cases_pass":True,
    "maximum_coordinate_histograms":tuple(dict(sorted(hist.items())) for hist in histograms),
    "remaining_gap":"arbitrary compositions for all 104 physical matchings and an all-size recurrence remain open",
    "evidence_level":"exact_all_physical_matching_unit_route_lift",
    "status":"passed",
})
