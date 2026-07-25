#!/usr/bin/env python3
from itertools import product


def cyclic(n, edges):
    indeg = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    todo = [i for i in range(n) if indeg[i] == 0]
    count = 0
    while todo:
        u = todo.pop()
        count += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                todo.append(v)
    return count != n


def topological_order(n, edges):
    indeg = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    todo = [i for i in range(n) if indeg[i] == 0]
    order = []
    while todo:
        u = todo.pop()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                todo.append(v)
    assert len(order) == n
    return order


def check(n, base, hist):
    if cyclic(n, hist):
        return
    order = topological_order(n, hist)
    for i in range(n):
        for j in range(i + 1, n):
            assert (order[j], order[i]) in base
    delta = max(
        [0]
        + [sum((i, j) in base for j in range(n)) for i in range(n)]
        + [sum((i, j) in base for i in range(n)) for j in range(n)]
    )
    assert n <= delta + 1


def main():
    for n in range(1, 5):
        cells = [(i, j) for i in range(n) for j in range(n) if i != j]
        for bits in product((0, 1), repeat=len(cells)):
            base = {edge for edge, bit in zip(cells, bits) if bit == 0}
            hist = set(cells) - base
            check(n, base, hist)
    print("PX315--PX318 composite history-cycle verifier: PASS")


if __name__ == "__main__":
    main()
