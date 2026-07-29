#!/usr/bin/env python3
"""Finite audit for RI5bm--RI5bq.

This checks finite-field line--hyperbola intersections. The Markdown note
contains the arbitrary-size proof.
"""


def primes_up_to(limit):
    primes = []
    for value in range(3, limit + 1):
        if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
            primes.append(value)
    return primes


def main():
    lines_checked = zero = one = two = 0

    for p in primes_up_to(31):
        inverse = lambda value: pow(value, p - 2, p)

        # Projective normalization: either A=1, or A=0 and B=1.
        lines = [(1, b, c) for b in range(p) for c in range(p)]
        lines.extend((0, 1, c) for c in range(p))

        for a in range(1, p):
            hyperbola = {
                (x, a * inverse(x) % p)
                for x in range(1, p)
            }

            for A, B, C in lines:
                roots = [
                    x
                    for x in range(1, p)
                    if (A * x * x - C * x + B * a) % p == 0
                ]
                quadratic_points = [
                    (x, a * inverse(x) % p)
                    for x in roots
                ]
                direct_points = [
                    point
                    for point in hyperbola
                    if (A * point[0] + B * point[1] - C) % p == 0
                ]

                assert sorted(quadratic_points) == sorted(direct_points)
                assert len(roots) <= 2

                if A and len(roots) == 2:
                    root_sum = C * inverse(A) % p
                    root_product = B * a * inverse(A) % p
                    assert (sum(roots) - root_sum) % p == 0
                    assert (roots[0] * roots[1] - root_product) % p == 0

                if len(roots) == 0:
                    zero += 1
                elif len(roots) == 1:
                    one += 1
                else:
                    two += 1
                lines_checked += 1

    print(f"{lines_checked:,} normalized line/hyperbola fibres")
    print(f"{zero:,} zero-target fibres")
    print(f"{one:,} one-target fibres")
    print(f"{two:,} two-target fibres")


if __name__ == "__main__":
    main()
