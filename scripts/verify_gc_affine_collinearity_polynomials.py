#!/usr/bin/env python3
"""Finite checks for GC4ap--GC4as."""

from itertools import product


def det(a, b, p):
    return (a[0] * b[1] - a[1] * b[0]) % p


def sub(a, b, p):
    return ((a[0] - b[0]) % p, (a[1] - b[1]) % p)


def add_scaled(x, u, t, p):
    return ((x[0] + t * u[0]) % p, (x[1] + t * u[1]) % p)


def main():
    checks = 0
    for p in (2, 3, 5, 7):
        pts = list(product(range(p), repeat=2))
        # Exhaust all affine families for p<=3; deterministic samples for larger fields.
        data = product(pts, repeat=6) if p <= 3 else (
            (pts[i % len(pts)], pts[(2*i+1) % len(pts)], pts[(3*i+2) % len(pts)],
             pts[(5*i+1) % len(pts)], pts[(7*i+3) % len(pts)], pts[(11*i+4) % len(pts)])
            for i in range(20000)
        )
        for x1, x2, x3, u1, u2, u3 in data:
            a0 = sub(x2, x1, p)
            a1 = sub(u2, u1, p)
            b0 = sub(x3, x1, p)
            b1 = sub(u3, u1, p)
            c0 = det(a0, b0, p)
            c1 = (det(a1, b0, p) + det(a0, b1, p)) % p
            c2 = det(a1, b1, p)
            roots = []
            for t in range(p):
                X1 = add_scaled(x1, u1, t, p)
                X2 = add_scaled(x2, u2, t, p)
                X3 = add_scaled(x3, u3, t, p)
                direct = det(sub(X2, X1, p), sub(X3, X1, p), p)
                poly = (c0 + c1 * t + c2 * t * t) % p
                assert direct == poly
                if direct == 0:
                    roots.append(t)
            zero_polynomial = c0 == c1 == c2 == 0
            if zero_polynomial:
                assert len(roots) == p
            else:
                assert len(roots) <= 2
                # For fields larger than the degree, vanishing everywhere forces zero coefficients.
                if p > 2:
                    assert len(roots) < p
            checks += 1
    print(f"verified {checks} affine collinearity families")


if __name__ == "__main__":
    main()
