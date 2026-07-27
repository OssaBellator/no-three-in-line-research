#!/usr/bin/env python3
"""Verify SRR2f--SRR2i on tiny switching games with exact fractions."""
from fractions import Fraction
from itertools import combinations, permutations


def solve_linear(mat, rhs):
    n = len(rhs)
    a = [list(map(Fraction, row)) + [Fraction(rhs[i])] for i, row in enumerate(mat)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        z = a[col][col]
        a[col] = [x / z for x in a[col]]
        for r in range(n):
            if r != col and a[r][col]:
                z = a[r][col]
                a[r] = [a[r][j] - z * a[col][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def game_value(payoff):
    M, C = len(payoff), len(payoff[0])
    best = None
    for s in range(1, min(M, C) + 1):
        for rows in combinations(range(M), s):
            for cols in combinations(range(C), s):
                mat = [[Fraction(1) for _ in range(s)] + [Fraction(0)]]
                rhs = [Fraction(1)]
                for c in cols:
                    mat.append([payoff[r][c] for r in rows] + [Fraction(-1)])
                    rhs.append(Fraction(0))
                sol = solve_linear(mat, rhs)
                if sol is None:
                    continue
                x, rho = sol[:-1], sol[-1]
                if any(v < 0 for v in x):
                    continue
                allpay = [sum(x[i] * payoff[rows[i]][c] for i in range(s)) for c in range(C)]
                if any(v > rho for v in allpay):
                    continue
                if best is None or rho < best:
                    best = rho
    assert best is not None
    return best


def saturating_matchings(A, B, edges):
    out = []
    for images in permutations(range(B), A):
        if all((a, images[a]) in edges for a in range(A)):
            out.append(images)
    return out


def verify():
    cases = 0
    for A in (1, 2):
        B = 3
        all_edges = [(a, b) for a in range(A) for b in range(B)]
        for mask in range(1, 1 << len(all_edges)):
            edges = {e for i, e in enumerate(all_edges) if mask >> i & 1}
            matchings = saturating_matchings(A, B, edges)
            if not matchings:
                continue
            cylinders = [{0}, {1}, {2}, {0, 1}, {1, 2}]
            payoff = []
            for m in matchings:
                row = []
                for C in cylinders:
                    load = sum(1 for b in m if b in C)
                    row.append(Fraction(B * load, A * len(C)))
                payoff.append(row)
            value = game_value(payoff)
            assert value >= 0
            assert game_value([r[:3] for r in payoff]) >= 1
            events = [{0}, {0, 1}, {1, 2}, {2}]
            for m in matchings:
                lhs = sum(Fraction(sum(1 for b in m if b in C), A) for C in events)
                multiplicity = [sum(b in C for C in events) for b in range(B)]
                rhs = Fraction(sum(multiplicity[b] for b in m), A)
                assert lhs == rhs
            cases += 1
    return cases


def main():
    print(f"SRR cylinder minimax: verified {verify()} switching games")


if __name__ == '__main__':
    main()
