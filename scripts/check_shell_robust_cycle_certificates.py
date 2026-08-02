#!/usr/bin/env python3
from fractions import Fraction
from math import floor

THREE = Fraction(3)

def reachable_vertices(initial, edges):
    adjacency = {}
    for source, target, lower, upper in edges:
        adjacency.setdefault(source, []).append(target)
    seen = {initial}
    stack = [initial]
    while stack:
        source = stack.pop()
        for target in adjacency.get(source, ()):
            if target not in seen:
                seen.add(target)
                stack.append(target)
    return seen

def simple_cycles(initial, edges):
    reachable = reachable_vertices(initial, edges)
    adjacency = {}
    for index, (source, target, lower, upper) in enumerate(edges):
        if source in reachable and target in reachable:
            adjacency.setdefault(source, []).append((target, index))
    cycles = set()
    for start in sorted(reachable):
        path_edges = []
        used = {start}
        def visit(current):
            for target, edge_index in adjacency.get(current, ()):
                if target == start:
                    cycle = tuple(path_edges + [edge_index])
                    rotations = tuple(cycle[i:] + cycle[:i] for i in range(len(cycle)))
                    cycles.add(min(rotations))
                elif target not in used and target >= start:
                    used.add(target)
                    path_edges.append(edge_index)
                    visit(target)
                    path_edges.pop()
                    used.remove(target)
        visit(start)
    return tuple(sorted(cycles))

def cycle_bounds(cycle, edges):
    lower_burden = sum(Fraction(edges[index][2]) for index in cycle)
    upper_burden = sum(Fraction(edges[index][3]) for index in cycle)
    length = len(cycle)
    optimistic_gain = THREE * length - lower_burden
    robust_gain = THREE * length - upper_burden
    return lower_burden, upper_burden, optimistic_gain, robust_gain

def graph_certificate(initial, edges):
    cycles = simple_cycles(initial, edges)
    data = tuple((cycle, cycle_bounds(cycle, edges)) for cycle in cycles)
    robust = tuple(item for item in data if item[1][3] > 0)
    possible = tuple(item for item in data if item[1][2] > 0)
    return cycles, robust, possible

def repetitions(setup, entry_worst_saving, robust_cycle_gain):
    setup = Fraction(setup)
    entry_worst_saving = Fraction(entry_worst_saving)
    robust_cycle_gain = Fraction(robust_cycle_gain)
    assert robust_cycle_gain > 0
    return max(0, floor((setup - entry_worst_saving) / robust_cycle_gain) + 1)

ROBUST_GRAPH = (
    ("s","a",4,5),
    ("a","b",1,Fraction(3,2)),
    ("b","a",2,Fraction(5,2)),
)
cycles, robust, possible = graph_certificate("s", ROBUST_GRAPH)
assert len(cycles) == 1
assert len(robust) == 1 and len(possible) == 1
cycle, robust_bounds = robust[0]
assert robust_bounds == (Fraction(3), Fraction(4), Fraction(3), Fraction(2))
entry_worst_saving = THREE - Fraction(5)
assert entry_worst_saving == -2
assert repetitions(7, entry_worst_saving, robust_bounds[3]) == 5

AMBIGUOUS_GRAPH = (
    ("s","a",0,0),
    ("a","b",2,4),
    ("b","a",3,3),
)
cycles, robust, possible = graph_certificate("s", AMBIGUOUS_GRAPH)
assert len(cycles) == 1
assert len(robust) == 0 and len(possible) == 1
_, ambiguous_bounds = possible[0]
assert ambiguous_bounds[2] == 1 and ambiguous_bounds[3] == -1

IMPOSSIBLE_GRAPH = (
    ("s","a",0,0),
    ("a","b",3,4),
    ("b","a",3,5),
)
cycles, robust, possible = graph_certificate("s", IMPOSSIBLE_GRAPH)
assert len(cycles) == 1
assert len(robust) == 0 and len(possible) == 0

nominal_mean = Fraction(9,4)
uniform_tolerance = THREE - nominal_mean
assert uniform_tolerance == Fraction(3,4)
assert nominal_mean + Fraction(1,2) < THREE
assert nominal_mean + Fraction(3,4) == THREE

print({
    "robust_common_cycle_condition": "some reachable cycle has upper-bound mean burden below three",
    "possible_cycle_condition": "some reachable cycle has lower-bound mean burden below three",
    "impossibility_condition": "every reachable cycle has lower-bound mean burden at least three",
    "robust_example_cycle_lower_burden": "3",
    "robust_example_cycle_upper_burden": "4",
    "robust_example_worst_gain": "2",
    "robust_example_entry_worst_saving": "-2",
    "robust_example_setup": "7",
    "robust_example_repetitions": 5,
    "uniform_additive_tolerance": str(uniform_tolerance),
    "remaining_gap": "no coordinate macro repertoire supplies certified edge-burden intervals and compatibility transitions",
    "evidence_level": "exact_robust_shell_cycle_interface",
    "status": "passed",
})
