#!/usr/bin/env python3
"""Finite audit for AC3qp--AC3qt.

Checks terminal-yield and strict path-product weights on acyclic capacity-source
networks, one-step and history inequalities, the combined amplification bound,
and SCC condensation/cyclic-core classification.
"""

from __future__ import annotations

import random
from collections import defaultdict, deque
from itertools import product

SEED = 20260726
RNG = random.Random(SEED)


def weights(rho: list[list[int]], beta: list[int]) -> tuple[list[int], list[int]]:
    """rho is upper triangular: edge i->j only for i<j."""
    n = len(rho)
    y = [0] * n
    w = [0] * n
    for i in range(n - 1, -1, -1):
        y[i] = beta[i] + sum(rho[i][j] * y[j] for j in range(i + 1, n))
        w[i] = 1 + beta[i] + sum(rho[i][j] * w[j] for j in range(i + 1, n))
    return y, w


def exhaustive_dags() -> int:
    checked = 0
    for n in range(1, 4):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        for vals in product(range(3), repeat=len(pairs) + n):
            rho = [[0] * n for _ in range(n)]
            for (i, j), value in zip(pairs, vals[: len(pairs)]):
                rho[i][j] = value
            beta = list(vals[len(pairs) :])
            y, w = weights(rho, beta)
            for i in range(n):
                assert y[i] == beta[i] + sum(rho[i][j] * y[j] for j in range(i + 1, n))
                assert w[i] == 1 + beta[i] + sum(
                    rho[i][j] * w[j] for j in range(i + 1, n)
                )
                assert w[i] >= 1
            checked += 1
    return checked


def random_transition_checks(trials: int = 100_000) -> int:
    accepted = 0
    for _ in range(trials):
        n = RNG.randint(1, 8)
        rho = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                rho[i][j] = RNG.randint(0, 3)
        beta = [RNG.randint(0, 3) for _ in range(n)]
        y, w = weights(rho, beta)
        s = [RNG.randint(0, 12) for _ in range(n)]
        B = RNG.randint(0, 20)
        d = [RNG.randint(0, value) for value in s]
        incoming = [sum(rho[i][j] * d[i] for i in range(j)) for j in range(n)]
        r = [RNG.randint(0, cap) for cap in incoming]
        g_cap = sum(beta[i] * d[i] for i in range(n))
        G = RNG.randint(0, g_cap)
        D = RNG.randint(0, B)
        s2 = [s[i] - d[i] + r[i] for i in range(n)]
        B2 = B - D + G

        Y = sum(y[i] * s[i] for i in range(n))
        Y2 = sum(y[i] * s2[i] for i in range(n))
        assert Y2 - Y <= -G

        psi = B + sum(w[i] * s[i] for i in range(n))
        psi2 = B2 + sum(w[i] * s2[i] for i in range(n))
        assert psi2 - psi <= -D - sum(d)
        if D + sum(d) > 0:
            accepted += 1
            assert psi2 < psi
    return accepted


def history_checks(histories: int = 40_000) -> tuple[int, int]:
    total_steps = 0
    total_created = 0
    for _ in range(histories):
        n = RNG.randint(1, 7)
        rho = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                rho[i][j] = RNG.randint(0, 2)
        beta = [RNG.randint(0, 3) for _ in range(n)]
        y, w = weights(rho, beta)
        s = [RNG.randint(0, 10) for _ in range(n)]
        B = RNG.randint(0, 18)
        Y0 = sum(y[i] * s[i] for i in range(n))
        psi0 = B + sum(w[i] * s[i] for i in range(n))
        gross_G = 0
        gross_spend = 0
        steps = 0
        for _step in range(200):
            available = [i for i, value in enumerate(s) if value > 0]
            if not available and B == 0:
                break
            d = [0] * n
            if available and (B == 0 or RNG.random() < 0.8):
                i = RNG.choice(available)
                d[i] = RNG.randint(1, s[i])
            D = RNG.randint(0, min(B, 2))
            if D + sum(d) == 0:
                continue
            incoming = [sum(rho[i][j] * d[i] for i in range(j)) for j in range(n)]
            r = [RNG.randint(0, cap) for cap in incoming]
            G = RNG.randint(0, sum(beta[i] * d[i] for i in range(n)))
            s = [s[i] - d[i] + r[i] for i in range(n)]
            B = B - D + G
            gross_G += G
            gross_spend += D + sum(d)
            steps += 1
        assert gross_G <= Y0
        assert gross_spend <= psi0
        assert steps <= psi0
        total_steps += steps
        total_created += gross_G
    return total_steps, total_created


def combined_checks(trials: int = 80_000) -> int:
    checked = 0
    for _ in range(trials):
        B0 = RNG.randint(0, 30)
        S0 = RNG.randint(0, B0)
        Y0 = RNG.randint(0, 30)
        L = RNG.randint(0, 20)
        G = RNG.randint(0, Y0)
        D = RNG.randint(0, 20)
        A_max = L + (B0 - S0) + G - D
        if A_max < 0:
            continue
        A = RNG.randint(0, A_max)
        ST = S0 + A - L
        BT = B0 + G - D
        assert 0 <= ST <= BT
        assert A + D <= L + (B0 - S0) + Y0
        checked += 1
    return checked


def tarjan_scc(adj: list[list[int]]) -> list[list[int]]:
    n = len(adj)
    index = 0
    stack: list[int] = []
    on_stack = [False] * n
    indices = [-1] * n
    low = [0] * n
    out: list[list[int]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True
        for w in adj[v]:
            if indices[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == v:
                    break
            out.append(comp)

    for v in range(n):
        if indices[v] < 0:
            visit(v)
    return out


def scc_checks(trials: int = 30_000) -> tuple[int, int]:
    cyclic = 0
    multi = 0
    for _ in range(trials):
        n = RNG.randint(1, 10)
        rates = [[0] * n for _ in range(n)]
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if RNG.random() < 0.18:
                    rates[i][j] = RNG.randint(1, 3)
                    adj[i].append(j)
        comps = tarjan_scc(adj)
        cid = {}
        for k, comp in enumerate(comps):
            for v in comp:
                cid[v] = k
        cond = [set() for _ in comps]
        indeg = [0] * len(comps)
        for i in range(n):
            for j in adj[i]:
                if cid[i] != cid[j] and cid[j] not in cond[cid[i]]:
                    cond[cid[i]].add(cid[j])
                    indeg[cid[j]] += 1
        queue = deque(i for i, deg in enumerate(indeg) if deg == 0)
        seen = 0
        while queue:
            u = queue.popleft()
            seen += 1
            for v in cond[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        assert seen == len(comps)

        for comp in comps:
            is_cyclic = len(comp) > 1 or any(rates[v][v] > 0 for v in comp)
            if not is_cyclic:
                continue
            cyclic += 1
            g = {v: sum(rates[v][u] for u in comp) for v in comp}
            assert all(value >= 1 for value in g.values())
            if all(value == 1 for value in g.values()):
                for v in comp:
                    positives = [u for u in comp if rates[v][u] > 0]
                    assert len(positives) == 1 and rates[v][positives[0]] == 1
            else:
                multi += 1
                assert any(value >= 2 for value in g.values())
    return cyclic, multi


def main() -> None:
    dags = exhaustive_dags()
    accepted = random_transition_checks()
    steps, created = history_checks()
    combined = combined_checks()
    cyclic, multi = scc_checks()
    print(
        "PASS AC ranked capacity-source audit:",
        f"{dags} exhaustive DAGs;",
        f"{accepted} strict random transitions;",
        f"{steps} history transitions;",
        f"{created} gross capacity units;",
        f"{combined} combined feasible systems;",
        f"{cyclic} cyclic SCCs ({multi} multi-output).",
    )


if __name__ == "__main__":
    main()
