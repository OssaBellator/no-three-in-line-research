#!/usr/bin/env python3
"""Finite checks for GC4ay--GC4bb."""

from itertools import product


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def sub(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)])


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def degree(a):
    return -1 if a == (0,) else len(a) - 1


def eval_poly(a, t, p):
    out = 0
    for x in reversed(a):
        out = (out * t + x) % p
    return out


def det_vec(a, b, p):
    return sub(mul(a[0], b[1], p), mul(a[1], b[0], p), p)


def check_pair(a, b, p):
    F = det_vec(a, b, p)
    if F != (0,):
        return False
    if a == ((0,), (0,)):
        return True

    s = 0 if a[0] != (0,) else 1
    other = 1 - s
    f, g = b[s], a[s]
    assert g != (0,)
    assert mul(g, b[other], p) == mul(f, a[other], p)
    assert degree(f) <= max(degree(b[0]), degree(b[1]))
    assert degree(g) <= max(degree(a[0]), degree(a[1]))
    roots = sum(eval_poly(g, t, p) == 0 for t in range(p))
    assert roots <= degree(g)
    return True


def main() -> None:
    checks = 0
    # Exhaust all degree-at-most-one vector pairs over F_2 and F_3.
    for p in (2, 3):
        polynomials = [trim(c) for c in product(range(p), repeat=2)]
        vectors = list(product(polynomials, repeat=2))
        for a in vectors:
            for b in vectors:
                if check_pair(a, b, p):
                    checks += 1

    # Deterministic higher-degree degenerate families B=lambda*A.
    for p in (2, 3, 5, 7):
        for d in range(1, 5):
            for seed in range(4000):
                a = []
                for coord in range(2):
                    a.append(trim([(seed + 3 * coord + 5 * k + coord * k) % p for k in range(d + 1)]))
                a = tuple(a)
                lam = trim([(seed + 7 * k + k * k) % p for k in range(d + 1)])
                b = (mul(lam, a[0], p), mul(lam, a[1], p))
                assert check_pair(a, b, p)
                checks += 1

    print(f"verified {checks} degenerate rational line charts")


if __name__ == "__main__":
    main()
