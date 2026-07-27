#!/usr/bin/env python3
"""Verify SAS5gl--SAS5go by table reversal and explicit commuting swaps."""
from itertools import product, permutations


def reverse_table(t):
    x00, x10, x01, x11 = t
    return (x11, x01, x10, x00)


def swap(state, i, j):
    s = list(state)
    s[i], s[j] = s[j], s[i]
    return tuple(s)


def verify_tables():
    for t in product((0, 1), repeat=4):
        assert reverse_table(reverse_table(t)) == t
    assert reverse_table((0, 0, 0, 1)) == (1, 0, 0, 0)
    assert reverse_table((1, 0, 0, 0)) == (0, 0, 0, 1)
    return 16


def verify_states(n=6):
    checks = 0
    gamma = (0, 1)
    delta = (2, 3)
    for state in permutations(range(n)):
        g = swap(state, *gamma)
        d = swap(state, *delta)
        gd = swap(g, *delta)
        assert gd == swap(d, *gamma)
        for table in product((0, 1), repeat=4):
            old = {state: table[0], g: table[1], d: table[2], gd: table[3]}
            new_table = (old[gd], old[d], old[g], old[state])
            assert new_table == reverse_table(table)
            checks += 1
    return checks


def main():
    print(f"Sparse composed-only reversal: verified {verify_tables()} tables and {verify_states()} state-table instances")


if __name__ == '__main__':
    main()
