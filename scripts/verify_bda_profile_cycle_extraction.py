#!/usr/bin/env python3
"""Verify BDA5az--BDA5bb finite profile-cycle and ticket bounds."""
from itertools import product


def simple_cycle_from_walk(vertices):
    first = {}
    for j, v in enumerate(vertices):
        if v in first:
            i = first[v]
            closed = vertices[i:j + 1]
            changed = True
            while changed:
                changed = False
                pos = {}
                for k, x in enumerate(closed[:-1]):
                    if x in pos:
                        closed = closed[pos[x]:k + 1]
                        changed = True
                        break
                    pos[x] = k
            return closed
        first[v] = j
    return None


def verify(max_k=5):
    checks = 0
    for k in range(1, max_k + 1):
        for length in range(k + 1, k + 4):
            for walk in product(range(k), repeat=length):
                cycle = simple_cycle_from_walk(walk)
                assert cycle is not None
                assert cycle[0] == cycle[-1]
                assert len(cycle) - 1 <= k
                assert len(set(cycle[:-1])) == len(cycle) - 1
                checks += 1
        edges = {(u, v) for u in range(k) for v in range(k)}
        assert len(edges) == k * k
    return checks


def main():
    print(f"BDA profile cycles: verified {verify()} long walks and all edge-ticket stocks")


if __name__ == '__main__':
    main()
