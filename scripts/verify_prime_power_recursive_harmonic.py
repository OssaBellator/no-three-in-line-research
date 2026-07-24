#!/usr/bin/env python3
"""Verify the pair law and harmonic bounds CMR38--CMR40 in small cases."""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import permutations
from math import gcd
from random import Random


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def harmonic_number(n: int) -> float:
    return sum(1.0 / j for j in range(1, n + 1))


def energy(values: tuple[int, ...]) -> float:
    total = 0.0
    n = len(values)
    for x in range(n):
        for xp in range(x + 1, n):
            dx = xp - x
            dy = abs(values[xp] - values[x])
            total += gcd(dx, dy) / max(dx, dy)
    return total


def terminal_base(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(b if x == 0 else (b + c * pow(x, -1, p)) % p for x in range(p))


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def lift_k2(
    p: int,
    base: tuple[int, ...],
    fibres: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    n = p * p
    values = [0] * n
    for low in range(p):
        for high in range(p):
            x = low + p * high
            values[x] = base[low] + p * fibres[low][high]
    return tuple(values)


def expected_difference_counts(p: int, a: int) -> Counter[int]:
    n = p * p
    t = valuation(a, p)
    m = p ** (2 - t)
    scale = p**t
    counts: Counter[int] = Counter()
    denominator = m * m * (1 - 1 / p)
    assert denominator.is_integer()
    for b in range(-(m - 1), m):
        if b and b % p:
            counts[scale * b] = m - abs(b)
    assert sum(counts.values()) == int(denominator)
    return counts


def verify_uniform_exact(p: int) -> tuple[int, float]:
    assert p == 3, "exact enumeration is intentionally restricted to p=3"
    perms = tuple(permutations(range(p)))
    n = p * p
    pair_counts = {
        (x, xp): Counter()
        for x in range(n)
        for xp in range(x + 1, n)
    }
    total_energy = 0.0
    states = 0

    for base in perms:
        for f0 in perms:
            for f1 in perms:
                for f2 in perms:
                    values = lift_k2(p, base, (f0, f1, f2))
                    assert sorted(values) == list(range(n))
                    total_energy += energy(values)
                    states += 1
                    for x in range(n):
                        for xp in range(x + 1, n):
                            pair_counts[(x, xp)][values[xp] - values[x]] += 1

    for (x, xp), observed in pair_counts.items():
        a = xp - x
        expected = expected_difference_counts(p, a)
        multiplier = states // sum(expected.values())
        assert observed == Counter({b: c * multiplier for b, c in expected.items()}), (
            x,
            xp,
            observed,
            expected,
        )

    average = total_energy / states
    h = harmonic_number(n)
    bound = 4 * n * 2 * h * (1 + h)
    assert average <= bound
    return states, average


def verify_terminal_domination(p: int) -> tuple[int, float]:
    assert p == 3
    perms = tuple(permutations(range(p)))
    base = terminal_base(p, 1, nonsquares(p)[0])
    n = p * p
    total_energy = 0.0
    states = 0
    pair_counts = {
        (x, xp): Counter()
        for x in range(n)
        for xp in range(x + 1, n)
    }

    for f0 in perms:
        for f1 in perms:
            for f2 in perms:
                values = lift_k2(p, base, (f0, f1, f2))
                total_energy += energy(values)
                states += 1
                for x in range(n):
                    for xp in range(x + 1, n):
                        pair_counts[(x, xp)][values[xp] - values[x]] += 1

    uniform_states = len(perms) * states
    for (x, xp), observed in pair_counts.items():
        expected = expected_difference_counts(p, xp - x)
        for difference, count in observed.items():
            uniform_probability = expected[difference] / sum(expected.values())
            terminal_probability = count / states
            assert terminal_probability <= 6 * uniform_probability + 1e-12

    average = total_energy / states
    h = harmonic_number(n)
    bound = 24 * n * 2 * h * (1 + h)
    assert average <= bound
    return states, average


def random_recursive_permutation(p: int, k: int, rng: Random) -> tuple[int, ...]:
    n = p**k
    base_choices = [
        terminal_base(p, b, c)
        for b in range(1, (p - 1) // 2 + 1)
        for c in nonsquares(p)
    ]
    base = rng.choice(base_choices)
    digit_maps: dict[tuple[int, int], tuple[int, ...]] = {}
    values = [0] * n

    for x in range(n):
        digits = []
        value = x
        for _ in range(k):
            digits.append(value % p)
            value //= p

        row_digits = [base[digits[0]]]
        prefix = digits[0]
        power = p
        for level in range(1, k):
            key = (level, prefix)
            if key not in digit_maps:
                items = list(range(p))
                rng.shuffle(items)
                digit_maps[key] = tuple(items)
            row_digits.append(digit_maps[key][digits[level]])
            prefix += power * digits[level]
            power *= p

        y = 0
        power = 1
        for digit in row_digits:
            y += power * digit
            power *= p
        values[x] = y

    assert sorted(values) == list(range(n))
    return tuple(values)


def verify_samples(p: int, k: int, samples: int, seed: int) -> float:
    rng = Random(seed)
    n = p**k
    total = 0.0
    for _ in range(samples):
        total += energy(random_recursive_permutation(p, k, rng))
    average = total / samples
    h = harmonic_number(n)
    assert average <= 24 * n * k * h * (1 + h)
    return average


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--seed", type=int, default=1729)
    args = parser.parse_args()

    uniform_states, uniform_average = verify_uniform_exact(3)
    terminal_states, terminal_average = verify_terminal_domination(3)
    sample_average = verify_samples(3, 3, args.samples, args.seed)

    print(
        f"verified recursive harmonic law: uniform-states={uniform_states}, "
        f"uniform-average={uniform_average:.6f}, "
        f"terminal-states={terminal_states}, terminal-average={terminal_average:.6f}, "
        f"sample-average-N27={sample_average:.6f}"
    )


if __name__ == "__main__":
    main()
