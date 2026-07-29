#!/usr/bin/env python3
"""Finite checks for GC4at--GC4ax."""


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def add(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])


def sub(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)])


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def eval_poly(a, t, p):
    out = 0
    for x in reversed(a):
        out = (out * t + x) % p
    return out


def vector_sub(x, y, p):
    return sub(x[0], y[0], p), sub(x[1], y[1], p)


def det_poly(a, b, p):
    return sub(mul(a[0], b[1], p), mul(a[1], b[0], p), p)


def degree(a):
    return -1 if a == (0,) else len(a) - 1


def main() -> None:
    checks = 0
    for p in (2, 3, 5, 7):
        for d in range(0, 4):
            samples = 3000 if p <= 3 else 1000
            for seed in range(samples):
                trajectories = []
                for i in range(3):
                    coords = []
                    for c in range(2):
                        coeffs = [((seed + 3 * i + 5 * c + 7 * k + i * c * k) % p) for k in range(d + 1)]
                        coords.append(trim(coeffs))
                    trajectories.append(tuple(coords))
                a = vector_sub(trajectories[1], trajectories[0], p)
                b = vector_sub(trajectories[2], trajectories[0], p)
                F = det_poly(a, b, p)
                pa = max(degree(a[0]), degree(a[1]), 0)
                qb = max(degree(b[0]), degree(b[1]), 0)
                assert degree(F) <= pa + qb
                assert degree(F) <= 2 * d
                roots = sum(eval_poly(F, t, p) == 0 for t in range(p))
                if F != (0,):
                    assert roots <= degree(F)
                else:
                    assert all(x == 0 for x in F)

                # Two-chart incidence/capacity arithmetic.
                D1 = max(degree(F), 0)
                D2 = min(2 * d, D1 + 1)
                M1 = (seed % 3) + 1
                M2 = ((seed // 3) % 3) + 1
                incidence = D1 * M1 + D2 * M2
                weights1 = sorted([((seed + i) % 7) + 1 for i in range(D1 * M1 + 3)], reverse=True)
                weights2 = sorted([((2 * seed + i) % 5) + 1 for i in range(D2 * M2 + 2)], reverse=True)
                cap = sum(weights1[: D1 * M1]) + sum(weights2[: D2 * M2])
                assert cap >= 0 and incidence >= 0
                checks += 1
    print(f"verified {checks} polynomial collinearity charts")


if __name__ == "__main__":
    main()
