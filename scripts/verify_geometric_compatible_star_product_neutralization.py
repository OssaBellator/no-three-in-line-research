#!/usr/bin/env python3
"""Finite audit for GC2cx--GC2db."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb, prod
import random


def allowed_permutations(t: int, forbidden: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    return [
        p for p in permutations(range(t))
        if all((i, p[i]) not in forbidden for i in range(t))
    ]


def falling(t: int, r: int) -> int:
    return prod(range(t - r + 1, t + 1))


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    for system_id in range(3_000):
        k = rng.randint(1, 3)
        blocks: list[tuple[int, set[tuple[int, int]], list[tuple[int, ...]]]] = []

        for _ in range(k):
            t = rng.randint(3, 5)
            forbidden = {(i, i) for i in range(t)}
            if rng.random() < 0.7:
                shift = rng.randint(1, t - 1)
                forbidden |= {(i, (i + shift) % t) for i in range(t)}
            omega = allowed_permutations(t, forbidden)
            if not omega:
                forbidden = {(i, i) for i in range(t)}
                omega = allowed_permutations(t, forbidden)
            assert omega
            for p in omega:
                assert all(p[i] != i for i in range(t))
                stats["old_endpoint_moves"] += t
            blocks.append((t, forbidden, omega))

        certificates = []
        for _ in range(rng.randint(5, 30)):
            support_size = rng.randint(1, min(3, k))
            support = tuple(sorted(rng.sample(range(k), support_size)))
            remaining = 3
            requirements: dict[int, tuple[tuple[int, int], ...]] = {}

            for pos, block_index in enumerate(support):
                t, _forbidden, omega = blocks[block_index]
                must_leave = len(support) - pos - 1
                max_r = min(t, remaining - must_leave)
                r = rng.randint(1, max_r)
                remaining -= r
                p = rng.choice(omega)
                rows = sorted(rng.sample(range(t), r))
                requirements[block_index] = tuple((i, p[i]) for i in rows)

            weight = rng.randint(1, 9)
            exact_probability = Fraction(1)
            product_bound = Fraction(1)
            for block_index, required in requirements.items():
                t, _forbidden, omega = blocks[block_index]
                count = sum(
                    all(p[i] == j for i, j in required)
                    for p in omega
                )
                exact_probability *= Fraction(count, len(omega))
                product_bound *= Fraction(128, falling(t, len(required)))

            assert exact_probability <= product_bound
            certificates.append(
                (support, requirements, weight, exact_probability, product_bound)
            )
            stats["certificates"] += 1
            stats[f"support_{support_size}"] += 1

        exact_expectation = sum(
            Fraction(weight) * exact_probability
            for _support, _requirements, weight, exact_probability, _bound in certificates
        )
        upper_expectation = sum(
            Fraction(weight) * bound
            for _support, _requirements, weight, _probability, bound in certificates
        )
        assert exact_expectation <= upper_expectation

        if upper_expectation > 0:
            H = upper_expectation * Fraction(rng.randint(1, 100), 100)
            by_support: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
            by_size: defaultdict[int, Fraction] = defaultdict(Fraction)
            for support, _requirements, weight, _probability, bound in certificates:
                value = Fraction(weight) * bound
                by_support[support] += value
                by_size[len(support)] += value
            M_k = sum(comb(k, s) for s in range(1, min(3, k) + 1))
            assert max(by_support.values()) >= H / M_k
            assert max(by_size.values()) >= H / 3
            stats["localized_failures"] += 1

        if system_id < 500:
            product_size = prod(len(block[2]) for block in blocks)
            if product_size <= 30_000:
                fixed_collateral = rng.randint(0, 10)
                destroyed = fixed_collateral + exact_expectation + (
                    1 if rng.random() < 0.5 else -1
                )
                changes = []
                for choices in product(*[block[2] for block in blocks]):
                    new_weight = 0
                    for _support, requirements, weight, _probability, _bound in certificates:
                        present = all(
                            all(choices[block_index][i] == j for i, j in required)
                            for block_index, required in requirements.items()
                        )
                        if present:
                            new_weight += weight
                    changes.append(Fraction(fixed_collateral) - destroyed + new_weight)

                average = sum(changes, Fraction()) / len(changes)
                assert average == Fraction(fixed_collateral) - destroyed + exact_expectation
                if average < 0:
                    assert min(changes) < 0
                    stats["improving_systems"] += 1
                stats["enumerated_product_states"] += len(changes)

        stats["systems"] += 1

    print("GC compatible-star product neutralization audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
