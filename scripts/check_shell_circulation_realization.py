#!/usr/bin/env python3
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import floor, lcm


def active_vertices(edge_counts):
    active=set()
    for (u,v),count in edge_counts.items():
        if count:
            active.update((u,v))
    return active


def balanced(edge_counts):
    outgoing=Counter()
    incoming=Counter()
    for (u,v),count in edge_counts.items():
        outgoing[u]+=count
        incoming[v]+=count
    return all(outgoing[v]==incoming[v] for v in set(outgoing)|set(incoming))


def weakly_connected(edge_counts):
    active=active_vertices(edge_counts)
    if not active:
        return False
    adjacency=defaultdict(set)
    for (u,v),count in edge_counts.items():
        if count:
            adjacency[u].add(v)
            adjacency[v].add(u)
    start=next(iter(active))
    seen={start}
    stack=[start]
    while stack:
        vertex=stack.pop()
        for neighbour in adjacency[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return active<=seen


def euler_tour(edge_counts):
    assert balanced(edge_counts)
    assert weakly_connected(edge_counts)
    adjacency=defaultdict(list)
    for edge,count in edge_counts.items():
        adjacency[edge[0]].extend([edge[1]]*count)
    start=next(vertex for vertex in active_vertices(edge_counts) if adjacency[vertex])
    stack=[start]
    tour=[]
    while stack:
        vertex=stack[-1]
        if adjacency[vertex]:
            stack.append(adjacency[vertex].pop())
        else:
            tour.append(stack.pop())
    tour.reverse()
    traversed=Counter(zip(tour,tour[1:]))
    assert traversed==Counter({edge:count for edge,count in edge_counts.items() if count})
    return tuple(tour)


def clear_rational(flow):
    denominator=1
    for value in flow.values():
        denominator=lcm(denominator,value.denominator)
    return denominator,{edge:int(denominator*value) for edge,value in flow.items()}


def robust_gain(edge_counts, burden_vertices):
    gains=[]
    for burden in burden_vertices:
        gains.append(sum(count*(3-burden[edge]) for edge,count in edge_counts.items()))
    return min(gains)


edges=tuple((u,v) for u in range(3) for v in range(3))
checked=0
for values in product(range(3),repeat=len(edges)):
    counts={edge:value for edge,value in zip(edges,values) if value}
    if not counts or not balanced(counts) or not weakly_connected(counts):
        continue
    tour=euler_tour(counts)
    assert len(tour)==1+sum(counts.values())
    checked+=1
assert checked==1086

flow={
    (0,1):Fraction(1,2),
    (1,0):Fraction(1,2),
    (1,2):Fraction(1,3),
    (2,1):Fraction(1,3),
}
scale,integer_counts=clear_rational(flow)
assert scale==6
assert integer_counts=={(0,1):3,(1,0):3,(1,2):2,(2,1):2}
assert len(euler_tour(integer_counts))==11
burden_vertices=(
    {(0,1):2,(1,0):2,(1,2):2,(2,1):2},
    {(0,1):1,(1,0):3,(1,2):1,(2,1):3},
)
assert robust_gain(integer_counts,burden_vertices)==10

disconnected={(0,0):2,(1,1):3}
assert balanced(disconnected)
assert not weakly_connected(disconnected)
connected=dict(disconnected)
connected[(0,1)]=1
connected[(1,0)]=1
assert balanced(connected) and weakly_connected(connected)
assert len(euler_tour(connected))==8


def repetitions(setup, connector_saving, bundle_gain):
    assert bundle_gain>0
    return max(0,floor(Fraction(setup-connector_saving,bundle_gain))+1)

assert repetitions(7,-2,3)==4
assert -2+3*4>7
assert -2+3*3<=7

print({
    "small_integer_circulations_checked":checked,
    "exact_executability_condition":"balanced rational circulation with weakly connected nonzero support",
    "denominator_clearing_example_scale":scale,
    "denominator_clearing_example_edges":integer_counts,
    "example_robust_gain":10,
    "disconnected_balanced_certificate_not_directly_executable":True,
    "connector_tour_restores_execution":True,
    "connector_setup_repetition_formula":"max(0,floor((S-A_connector)/G_bundle)+1)",
    "remaining_gap":"no coordinate macro graph supplies a positive connected circulation and certified burden polytope",
    "evidence_level":"exact_rational_circulation_shell_realization_interface",
    "status":"passed",
})
