#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import floor


def reachable_vertices(initial, edges):
    seen = {initial}
    changed = True
    while changed:
        changed = False
        for source,target,_,_ in edges:
            if source in seen and target not in seen:
                seen.add(target)
                changed = True
    return seen


def simple_cycles(initial, edges):
    reachable = reachable_vertices(initial, edges)
    adjacency = {}
    for index,(source,target,lower,upper) in enumerate(edges):
        if source in reachable and target in reachable:
            adjacency.setdefault(source,[]).append((target,index))
    cycles = set()
    for start in sorted(reachable):
        def visit(vertex,path_vertices,path_edges):
            for target,index in adjacency.get(vertex,()):
                if target == start:
                    cycle = tuple(path_edges + [index])
                    rotations = tuple(cycle[offset:]+cycle[:offset] for offset in range(len(cycle)))
                    cycles.add(min(rotations))
                elif target not in path_vertices and target >= start:
                    visit(target,path_vertices | {target},path_edges + [index])
        visit(start,{start},[])
    return tuple(sorted(cycles))


def cycle_gain(cycle, edges, use_upper):
    total = Fraction(0)
    for index in cycle:
        burden = Fraction(edges[index][3 if use_upper else 2])
        total += 3-burden
    return total


def classification(initial, edges):
    cycles = simple_cycles(initial,edges)
    possible = any(cycle_gain(cycle,edges,False) > 0 for cycle in cycles)
    robust = any(cycle_gain(cycle,edges,True) > 0 for cycle in cycles)
    return cycles,possible,robust


def positive_cycle_for_realization(initial, edges, burdens):
    cycles = simple_cycles(initial,edges)
    return any(sum(Fraction(3)-Fraction(burdens[index]) for index in cycle) > 0 for cycle in cycles)


ROBUST_EDGES = (
    (0,1,4,5),
    (1,2,1,2),
    (2,1,2,2),
)
cycles,possible,robust = classification(0,ROBUST_EDGES)
assert possible and robust
assert len(cycles) == 1
assert cycle_gain(cycles[0],ROBUST_EDGES,False) == 3
assert cycle_gain(cycles[0],ROBUST_EDGES,True) == 2
corner_results = []
for choices in product((0,1),repeat=len(ROBUST_EDGES)):
    burdens = [edge[2+choice] for edge,choice in zip(ROBUST_EDGES,choices)]
    corner_results.append(positive_cycle_for_realization(0,ROBUST_EDGES,burdens))
assert all(corner_results)

POSSIBLE_ONLY_EDGES = ((0,1,1,4),(1,0,1,4))
_,possible,robust = classification(0,POSSIBLE_ONLY_EDGES)
assert possible and not robust
corner_results = []
for choices in product((0,1),repeat=2):
    burdens = [edge[2+choice] for edge,choice in zip(POSSIBLE_ONLY_EDGES,choices)]
    corner_results.append(positive_cycle_for_realization(0,POSSIBLE_ONLY_EDGES,burdens))
assert any(corner_results) and not all(corner_results)

IMPOSSIBLE_EDGES = ((0,1,3,4),(1,0,3,5))
_,possible,robust = classification(0,IMPOSSIBLE_EDGES)
assert not possible and not robust

ENTRY_WORST_SAVING = Fraction(3-5)
ROBUST_CYCLE_GAIN = Fraction(2)
SETUP = Fraction(7)
repetitions = max(0,floor((SETUP-ENTRY_WORST_SAVING)/ROBUST_CYCLE_GAIN)+1)
assert repetitions == 5
assert ENTRY_WORST_SAVING + (repetitions-1)*ROBUST_CYCLE_GAIN <= SETUP
assert ENTRY_WORST_SAVING + repetitions*ROBUST_CYCLE_GAIN > SETUP

print({
    "edge_burden_interval": "[lower_e,upper_e]",
    "possible_all_setup_amortization": "a reachable cycle has sum_e(3-lower_e)>0",
    "robust_all_setup_amortization": "a reachable cycle has sum_e(3-upper_e)>0",
    "robust_equivalent_mean_condition": "some reachable cycle has upper-burden mean below three",
    "uncertain_region": "best-case positive cycle exists but no worst-case positive cycle exists",
    "robust_example_best_cycle_gain": 3,
    "robust_example_worst_cycle_gain": 2,
    "robust_example_setup": 7,
    "robust_example_worst_entry_saving": -2,
    "robust_example_repetitions": repetitions,
    "possible_only_example": True,
    "impossible_example": True,
    "remaining_gap": "no coordinate macro repertoire supplies certified burden intervals and compatibility edges with a robust positive cycle",
    "evidence_level": "exact_interval_cycle_robustness_interface",
    "status": "passed",
})
