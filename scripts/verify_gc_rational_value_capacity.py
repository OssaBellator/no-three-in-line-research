#!/usr/bin/env python3
"""Finite checks for GC4bc--GC4bf."""


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def degree(poly):
    return -1 if poly == (0,) else len(poly) - 1


def eval_poly(poly, t, p):
    out = 0
    for c in reversed(poly):
        out = (out * t + c) % p
    return out


def subtract_scaled(f, alpha, g, p):
    n = max(len(f), len(g))
    return trim([
        ((f[i] if i < len(f) else 0) - alpha * (g[i] if i < len(g) else 0)) % p
        for i in range(n)
    ])


def main() -> None:
    checks = 0
    for p in (2, 3, 5, 7):
        for d in range(0, 6):
            for seed in range(2500):
                f = trim([((seed + 3 * i + i * i) % p) for i in range(d + 1)])
                g = trim([((2 * seed + 5 * i + 1 + i * i) % p) for i in range(d + 1)])
                if g == (0,):
                    g = (1,)
                D = max(degree(f), degree(g))
                denominator_roots = sum(eval_poly(g, t, p) == 0 for t in range(p))
                assert denominator_roots <= degree(g)
                for alpha in range(p):
                    h = subtract_scaled(f, alpha, g, p)
                    valid_roots = sum(
                        eval_poly(g, t, p) != 0 and eval_poly(h, t, p) == 0
                        for t in range(p)
                    )
                    if h == (0,):
                        assert all(
                            eval_poly(f, t, p) == alpha * eval_poly(g, t, p) % p
                            for t in range(p)
                        )
                    else:
                        assert degree(h) <= D
                        assert valid_roots <= degree(h) <= D
                    checks += 1
    print(f"verified {checks} rational fixed-ratio polynomial instances")


if __name__ == "__main__":
    main()
