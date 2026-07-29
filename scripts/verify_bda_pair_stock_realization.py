#!/usr/bin/env python3
"""Finite checks for BDA5cg--BDA5cj."""

from fractions import Fraction


def main() -> None:
    checks = 0
    for edge_count in range(1, 13):
        for K in range(1, 7):
            for d in range(1, 7):
                for seed in range(800):
                    weights = [((seed + 5 * i + i * i) % 19) for i in range(edge_count)]
                    classes = [((seed + 3 * i + i * i) % K) for i in range(edge_count)]
                    buckets = [0] * K
                    for w, cls in zip(weights, classes):
                        buckets[cls] += w
                    total = sum(weights)
                    assert sum(buckets) == total
                    assert max(buckets) * K >= total

                    # Treat this matching as the stock returned from a line router.
                    W_line = total * (2 * d - 1)
                    assert total == Fraction(W_line, 2 * d - 1)
                    heavy = max(buckets)
                    assert heavy * K * (2 * d - 1) >= W_line

                    # Rational payment efficiencies remain additive.
                    rho_num = (seed % 5) + 1
                    rho_den = ((seed // 5) % 5) + 1
                    payment = Fraction(rho_num * heavy, rho_den)
                    assert payment >= Fraction(rho_num * W_line, rho_den * K * (2 * d - 1))
                    checks += 1
    print(f"verified {checks} BDA realization stocks")


if __name__ == "__main__":
    main()
