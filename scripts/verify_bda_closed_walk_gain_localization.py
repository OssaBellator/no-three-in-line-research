#!/usr/bin/env python3
from fractions import Fraction
import random


def simple_cycles(vertex_count, edges):
    adjacency = {v: [] for v in range(vertex_count)}
    for u, v, gain in edges:
        adjacency[u].append((v, gain))

    cycles = {}
    for start in range(vertex_count):
        stack = [(start, [start], Fraction(1))]
        while stack:
            vertex, path, product = stack.pop()
            for nxt, gain in adjacency[vertex]:
                if nxt == start:
                    if min(path) == start:
                        cycles[tuple(path)] = product * gain
                elif nxt not in path and nxt >= start:
                    stack.append((nxt, path + [nxt], product * gain))
    return list(cycles.items())


def main() -> None:
    rng = random.Random(1102)
    systems = 6_000
    cycles_checked = 0
    closed_walks = 0
    amplifying_walks = 0
    simple_cycle_witnesses = 0

    for _ in range(systems):
        vertex_count = rng.randint(2, 6)
        edges = []
        for u in range(vertex_count):
            for v in range(vertex_count):
                if u != v and rng.random() < 0.28:
                    gain = Fraction(rng.choice([1, 1, 1, 2, 3, 4]), rng.choice([1, 2, 3, 4]))
                    edges.append((u, v, gain))

        cycles = simple_cycles(vertex_count, edges)
        cycles_checked += len(cycles)
        if not cycles:
            continue

        for _ in range(rng.randint(1, 5)):
            chosen = [rng.choice(cycles) for _ in range(rng.randint(1, 4))]
            product = Fraction(1)
            for _, cycle_gain in chosen:
                product *= cycle_gain
            closed_walks += 1
            if product > 1:
                amplifying_walks += 1
                assert any(cycle_gain > 1 for _, cycle_gain in chosen)
                simple_cycle_witnesses += 1

    print(f"systems={systems}")
    print(f"simple_cycles_checked={cycles_checked}")
    print(f"closed_walks={closed_walks}")
    print(f"amplifying_closed_walks={amplifying_walks}")
    print(f"simple_cycle_witnesses={simple_cycle_witnesses}")


if __name__ == "__main__":
    main()
