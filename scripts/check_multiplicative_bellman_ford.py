#!/usr/bin/env python3
from fractions import Fraction


def relax(vertices, edges, q):
    A = {v: Fraction(1) for v in vertices}
    history = [A.copy()]
    for _ in range(len(vertices)):
        B = A.copy()
        for u, v, p in edges:
            cand = A[u] * p / q
            if cand > B[v]:
                B[v] = cand
        A = B
        history.append(A.copy())
    return history


def simple_cycles(vertices, edges):
    adj = {v: [] for v in vertices}
    weight = {}
    for u, v, p in edges:
        adj[u].append(v)
        weight[(u, v)] = p

    cycles = []
    keys = set()
    for start in vertices:
        stack = [(start, [start])]
        while stack:
            u, path = stack.pop()
            for v in adj[u]:
                if v == start and len(path) >= 2:
                    cyc = path[:]
                    rots = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
                    key = min(rots)
                    if key not in keys:
                        keys.add(key)
                        prod = Fraction(1)
                        for i in range(len(cyc)):
                            prod *= weight[(cyc[i], cyc[(i + 1) % len(cyc)])]
                        cycles.append((key, prod))
                elif v not in path and len(path) < len(vertices):
                    stack.append((v, path + [v]))
    return cycles


def check_graph(vertices, edges, q, should_pass):
    hist = relax(vertices, edges, q)
    stable = hist[-1] == hist[-2]
    cycles = simple_cycles(vertices, edges)
    bad = [(c, prod) for c, prod in cycles if prod > q ** len(c)]
    assert stable == should_pass
    assert (len(bad) == 0) == should_pass
    if stable:
        a = hist[-2]
        for u, v, p in edges:
            assert p * a[u] <= q * a[v]
    return stable, bad, hist[-1]


def main():
    V = ["a", "b", "c", "d"]
    passing = [
        ("a", "b", Fraction(3, 2)),
        ("b", "a", Fraction(1, 2)),
        ("b", "c", Fraction(4, 5)),
        ("c", "a", Fraction(2, 3)),
        ("b", "d", Fraction(1, 2)),
        ("d", "b", Fraction(1, 2)),
    ]
    failing = passing + [("c", "d", Fraction(5, 4)), ("d", "c", Fraction(5, 4))]
    q = Fraction(1)

    pass_result = check_graph(V, passing, q, True)
    fail_result = check_graph(V, failing, q, False)

    print({
        "all_checks_passed": True,
        "passing_stabilized": pass_result[0],
        "passing_potential": {k: str(v) for k, v in pass_result[2].items()},
        "failing_cycles": [(list(c), str(p)) for c, p in fail_result[1]],
    })


if __name__ == "__main__":
    main()
