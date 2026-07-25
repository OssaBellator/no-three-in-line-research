#!/usr/bin/env python3
"""Finite verifier for PX327--PX329."""

from itertools import combinations, permutations, product


def tournament_from_bits(n, bits):
    pairs = list(combinations(range(n), 2))
    arcs = set()
    for bit, (u, v) in zip(bits, pairs):
        arcs.add((u, v) if bit == 0 else (v, u))
    return arcs


def degrees(n, arcs):
    out = [0] * n
    inn = [0] * n
    for u, v in arcs:
        out[u] += 1
        inn[v] += 1
    return out, inn


def canonical(n, arcs):
    reps = []
    for p in permutations(range(n)):
        image = sorted((p[u], p[v]) for u, v in arcs)
        reps.append(tuple(image))
    return min(reps)


def exhaust():
    regular_classes = {}
    for n in range(1, 6):
        pairs = n * (n - 1) // 2
        for bits in product((0, 1), repeat=pairs):
            arcs = tournament_from_bits(n, bits)
            out, inn = degrees(n, arcs)
            assert all(out[v] + inn[v] == n - 1 for v in range(n))
            delta = max(out + inn, default=0)
            assert n <= 2 * delta + 1
            if n % 2 == 1 and all(x == (n - 1) // 2 for x in out + inn):
                regular_classes.setdefault(n, set()).add(canonical(n, arcs))

    assert len(regular_classes[3]) == 1
    assert len(regular_classes[5]) == 1


def cyclic_check():
    for n in (3, 5):
        half = (n - 1) // 2
        arcs = {
            (u, v)
            for u in range(n)
            for v in range(n)
            if u != v and (v - u) % n in range(1, half + 1)
        }
        out, inn = degrees(n, arcs)
        assert out == [half] * n
        assert inn == [half] * n


def sharp_no_extra_capacity():
    for delta in (1, 2):
        n = 2 * delta + 1
        pairs = n * (n - 1) // 2
        for bits in product((0, 1), repeat=pairs):
            arcs = tournament_from_bits(n, bits)
            out, inn = degrees(n, arcs)
            if max(out + inn) <= delta:
                assert out == [delta] * n
                assert inn == [delta] * n


if __name__ == "__main__":
    exhaust()
    cyclic_check()
    sharp_no_extra_capacity()
    print("PX327--PX329 verified")
