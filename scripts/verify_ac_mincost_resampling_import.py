#!/usr/bin/env python3
"""Verify AC5ac--AC5af on finite Hall flows and event inventories."""
from fractions import Fraction
from itertools import product


def verify():
    checks = 0
    loads = []
    vals = [Fraction(0), Fraction(1, 2), Fraction(1)]
    for q in product(vals, repeat=3):
        if sum(q) == 2:
            loads.append(q)
    event_sets = [
        ({0}, {1}),
        ({0, 1}, {1, 2}),
        ({0}, {0, 2}, {2}),
    ]
    A = 2
    t = 3
    for q in loads:
        for cur in event_sets:
            for high in event_sets:
                mcur = [sum(b in C for C in cur) for b in range(3)]
                mhigh = [sum(b in C for C in high) for b in range(3)]
                gamma_cur = sum(Fraction(sum(q[b] for b in C), A) for C in cur)
                gamma_high = sum(Fraction(sum(q[b] for b in C), A) for C in high)
                rhs_cur = Fraction(sum(mcur[b] * q[b] for b in range(3)), A)
                rhs_high = Fraction(sum(mhigh[b] * q[b] for b in range(3)), A)
                assert gamma_cur == rhs_cur
                assert gamma_high == rhs_high
                cost = sum((mcur[b] + t * mhigh[b]) * q[b] for b in range(3))
                assert Fraction(cost, A) == gamma_cur + t * gamma_high
                if cost < t * A:
                    assert gamma_cur + t * gamma_high < t
                mpath = [mcur[b] + t * (2 * mhigh[b]) for b in range(3)]
                path_cost = sum(mpath[b] * q[b] for b in range(3))
                assert Fraction(path_cost, A) == gamma_cur + 2 * t * gamma_high
                checks += 1
    return checks


def main():
    print(f"AC min-cost resampling import: verified {verify()} flow/inventory combinations")


if __name__ == '__main__':
    main()
