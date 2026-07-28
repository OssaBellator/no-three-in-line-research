from fractions import Fraction
from random import Random

def simple_cycles(n, edges):
    edge = {(u, v): g for u, v, g in edges}
    out = [[] for _ in range(n)]
    for u, v, _ in edges:
        out[u].append(v)
    seen = set()
    cycles = []
    for start in range(n):
        stack = [(start, [start])]
        while stack:
            u, path = stack.pop()
            for v in out[u]:
                if v == start and len(path) >= 1:
                    cyc = path[:]
                    rots = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
                    key = min(rots)
                    if key not in seen:
                        seen.add(key)
                        prod = Fraction(1, 1)
                        for i in range(len(cyc)):
                            prod *= edge[(cyc[i], cyc[(i + 1) % len(cyc)])]
                        cycles.append((key, prod))
                elif v not in path and len(path) < n:
                    stack.append((v, path + [v]))
    return cycles

def max_path_potential(n, edges):
    out = [[] for _ in range(n)]
    for u, v, g in edges:
        out[u].append((v, g))
    q = [Fraction(1, 1) for _ in range(n)]
    for start in range(n):
        stack = [(start, frozenset([start]), Fraction(1, 1))]
        best = Fraction(1, 1)
        while stack:
            u, used, prod = stack.pop()
            if prod > best:
                best = prod
            for v, g in out[u]:
                if v not in used:
                    stack.append((v, used | {v}, prod * g))
        q[start] = best
    return q

def main() -> None:
    rng = Random(2026072811)
    systems = 6000
    edges_total = 0
    cycle_checks = 0
    certified = 0
    amplifying = 0
    transfer_checks = 0

    gains = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
             Fraction(1, 1), Fraction(3, 2), Fraction(2, 1)]
    for _ in range(systems):
        n = rng.randint(2, 6)
        edges = []
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < 0.28:
                    edges.append((u, v, rng.choice(gains)))
        edges_total += len(edges)
        cycles = simple_cycles(n, edges)
        cycle_checks += len(cycles)
        bad = [c for c in cycles if c[1] > 1]
        if bad:
            amplifying += 1
            assert max(p for _, p in bad) > 1
            continue

        certified += 1
        q = max_path_potential(n, edges)
        for u, v, g in edges:
            assert q[u] >= g * q[v]

        for _ in range(rng.randint(1, 12)):
            if not edges:
                break
            u, v, g = rng.choice(edges)
            mass = rng.randint(1, 20)
            child = Fraction(rng.randint(0, g.numerator * mass), g.denominator)
            assert child <= g * mass
            assert q[v] * child <= q[u] * mass
            transfer_checks += 1

    print("BDA gain-cycle duality audit")
    print(f"  systems: {systems}")
    print(f"  gain edges: {edges_total}")
    print(f"  simple directed cycles checked: {cycle_checks}")
    print(f"  certified nonamplifying systems: {certified}")
    print(f"  amplifying-cycle systems: {amplifying}")
    print(f"  weighted transfer checks: {transfer_checks}")

if __name__ == "__main__":
    main()
