#!/usr/bin/env python3
from fractions import Fraction


def simple_cycles(vertices, edges):
    adjacency = {vertex: [] for vertex in vertices}
    for source, target, burden in edges:
        adjacency[source].append((target, Fraction(burden)))
    cycles = set()
    for start in vertices:
        def visit(current, path, burdens):
            for target, burden in adjacency[current]:
                if target == start:
                    vertex_cycle = tuple(path)
                    edge_burdens = tuple(burdens + [burden])
                    rotations = [vertex_cycle[index:] + vertex_cycle[:index] for index in range(len(vertex_cycle))]
                    canonical = min(rotations)
                    shift = rotations.index(canonical)
                    canonical_burdens = edge_burdens[shift:] + edge_burdens[:shift]
                    cycles.add((canonical, canonical_burdens))
                elif target not in path and len(path) < len(vertices):
                    visit(target, path + [target], burdens + [burden])
        visit(start, [start], [])
    return tuple(sorted(cycles))


def reachable(start, vertices, edges):
    adjacency = {vertex: [] for vertex in vertices}
    for source, target, _ in edges:
        adjacency[source].append(target)
    seen = {start}
    stack = [start]
    while stack:
        current = stack.pop()
        for target in adjacency[current]:
            if target not in seen:
                seen.add(target)
                stack.append(target)
    return seen


def cycle_records(start, vertices, edges):
    seen = reachable(start, vertices, edges)
    records = []
    for cycle, burdens in simple_cycles(vertices, edges):
        if cycle[0] not in seen:
            continue
        total_burden = sum(burdens, Fraction(0))
        length = len(burdens)
        saving = 3 * length - total_burden
        records.append({
            "cycle": cycle,
            "burdens": burdens,
            "total_burden": total_burden,
            "mean_burden": total_burden / length,
            "saving": saving,
        })
    return records

vertices = ("A", "B", "C", "D")
edges = (
    ("A", "B", 5),
    ("B", "C", 1),
    ("C", "B", 2),
    ("A", "D", 0),
    ("D", "D", 3),
)
records = cycle_records("A", vertices, edges)
positive = [record for record in records if record["saving"] > 0]
assert len(positive) == 1
best = positive[0]
assert best["cycle"] == ("B", "C")
assert best["mean_burden"] == Fraction(3, 2)
assert best["saving"] == 3

entry_saving = Fraction(-2)  # A->B has burden five.
setup = Fraction(7)
repetitions = max(0, (setup - entry_saving) // best["saving"] + 1)
assert repetitions == 4
assert entry_saving + repetitions * best["saving"] > setup
assert entry_saving + (repetitions - 1) * best["saving"] <= setup

no_gain_edges = (("A", "B", 2), ("B", "A", 4), ("B", "B", 3))
no_gain_records = cycle_records("A", ("A", "B"), no_gain_edges)
assert no_gain_records
assert all(record["saving"] <= 0 for record in no_gain_records)

# Removing nonpositive cycles from any walk cannot decrease its saving, so without
# a positive reachable cycle every walk has a simple representative of bounded
# length. Exhaust the small example to demonstrate the bounded envelope.
adjacency = {vertex: [] for vertex in ("A", "B")}
for source, target, burden in no_gain_edges:
    adjacency[source].append((target, Fraction(3 - burden)))
walk_savings = {("A",): Fraction(0)}
maximum = Fraction(0)
for _ in range(12):
    updated = {}
    for path, saving in walk_savings.items():
        for target, edge_saving in adjacency[path[-1]]:
            new_path = path + (target,)
            updated[new_path] = saving + edge_saving
            maximum = max(maximum, updated[new_path])
    walk_savings = updated
assert maximum == 1

print({
    "transition_burden": "b(e)=6*delta(e)+c(e)",
    "transition_saving": "w(e)=3-b(e)",
    "all_fixed_setups_amortizable": "a reachable directed cycle has positive total saving",
    "equivalent_cycle_mean_condition": "a reachable cycle has mean burden below three",
    "best_asymptotic_saving_rate": "maximum reachable cycle mean of w, equivalently 3 minus minimum reachable cycle mean burden",
    "example_positive_cycle": ["B", "C"],
    "example_mean_burden": "3/2",
    "example_cycle_gain": 3,
    "example_setup": 7,
    "example_entry_saving": -2,
    "example_minimum_repetitions": repetitions,
    "no_positive_cycle_example_maximum_walk_saving": maximum,
    "remaining_gap": "no coordinate-level macro transition graph with a reachable sub-three mean-burden cycle has been constructed",
    "evidence_level": "exact_shell_repertoire_cycle_mean_interface",
    "status": "passed",
})
