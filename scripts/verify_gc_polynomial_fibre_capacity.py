#!/usr/bin/env python3
"""Finite checks for GC4al--GC4ao."""

from itertools import product


def eval_poly(coeffs, x, p):
    out = 0
    power = 1
    for c in coeffs:
        out = (out + c * power) % p
        power = (power * x) % p
    return out


def degree(coeffs):
    for i in range(len(coeffs) - 1, -1, -1):
        if coeffs[i] != 0:
            return i
    return -1


def main():
    checks = 0
    for p in (2, 3, 5, 7):
        for maxdeg in range(0, 5):
            for coeffs in product(range(p), repeat=maxdeg + 1):
                d = degree(coeffs)
                if d < 0:
                    continue
                roots = [x for x in range(p) if eval_poly(coeffs, x, p) == 0]
                assert len(roots) <= d
                for mult in range(1, 5):
                    incidence = len(roots) * mult
                    assert incidence <= d * mult
                    weights = list(range(1, p * mult + 3))
                    weights.sort(reverse=True)
                    top = sum(weights[: d * mult])
                    chosen = sum(weights[:incidence])
                    assert chosen <= top
                    checks += 1
    print(f"verified {checks} nonzero polynomial fibre capacities")


if __name__ == "__main__":
    main()
