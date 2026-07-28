#!/usr/bin/env python3
"""Finite audit for RI5bh--RI5bl."""


def inverse(value: int, prime: int) -> int:
    return pow(value, prime - 2, prime)


def main() -> None:
    ordered_pairs = secant_fibres = swap_fibres = 0

    for prime in (5, 7, 11, 13):
        for a in range(1, prime):
            fibres: dict[tuple[int, int, int, int], list[tuple[int, int]]] = {}

            for x in range(1, prime):
                for y in range(1, prime):
                    if x == y:
                        continue
                    total = (x + y) % prime
                    product = (x * y) % prime
                    normalized_slope = product * inverse(a, prime) % prime
                    key = (a, total, product, normalized_slope)
                    fibres.setdefault(key, []).append((x, y))
                    ordered_pairs += 1

            for key, lifts in fibres.items():
                secant_fibres += 1
                unordered = {frozenset(pair) for pair in lifts}
                assert len(unordered) == 1
                assert len(lifts) == 2

                x, y = lifts[0]
                assert (y, x) in lifts
                a0, total, product, normalized_slope = key
                assert normalized_slope == product * inverse(a0, prime) % prime

                for X in (x, y):
                    R = a0 * inverse(X, prime) % prime
                    assert (product * R + a0 * X - a0 * total) % prime == 0
                    assert (X * X - total * X + product) % prime == 0

                swap_fibres += 1

    assert ordered_pairs == 2712
    assert secant_fibres == 1356
    assert swap_fibres == secant_fibres
    print(
        "fixed-secant orientation audit passed:",
        f"{ordered_pairs} ordered pairs, {secant_fibres} exact secants",
    )


if __name__ == "__main__":
    main()
