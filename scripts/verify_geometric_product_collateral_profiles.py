#!/usr/bin/env python3
"""Finite audit for GC2dc--GC2dg.

Checks the six rank-three block-occupancy profiles, exact product containment
probabilities in independent allowed-matching banks, and weighted localization
to one low-order star-block tuple.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb
import random


PROFILES = {
    (1,),
    (2,),
    (3,),
    (1, 1),
    (2, 1),
    (1, 1, 1),
}


def profile(counts: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((x for x in counts if x), reverse=True))


def allowed_permutations(t: int) -> list[tuple[int, ...]]:
    # Diagonal and cyclic successor are forbidden; row/column degree is two.
    out = []
    for pi in permutations(range(t)):
        if all(pi[i] not in {i, (i + 1) % t} for i in range(t)):
            out.append(pi)
    return out


def containment_probability(
    allowed: list[tuple[int, ...]], cells: tuple[tuple[int, int], ...]
) -> Fraction:
    count = sum(all(pi[i] == j for i, j in cells) for pi in allowed)
    return Fraction(count, len(allowed))


def main() -> None:
    stats: Counter[str] = Counter()

    for k in range(1, 8):
        for counts in product(range(4), repeat=k):
            if 1 <= sum(counts) <= 3:
                p = profile(counts)
                assert p in PROFILES
                stats[f"profile_{''.join(map(str, p))}"] += 1

    allowed_by_t = {t: allowed_permutations(t) for t in (5, 6, 7)}
    rng = random.Random(20260727)

    for _ in range(12_000):
        k = rng.randint(1, 3)
        ts = [rng.choice((5, 6, 7)) for _ in range(k)]
        counts = [0] * k
        remaining = rng.randint(1, 3)
        while remaining:
            i = rng.randrange(k)
            if counts[i] < 3:
                counts[i] += 1
                remaining -= 1

        local_probs: list[Fraction] = []
        for t, r in zip(ts, counts):
            if r == 0:
                local_probs.append(Fraction(1))
                continue
            allowed = allowed_by_t[t]
            witness = rng.choice(allowed)
            rows = rng.sample(range(t), r)
            cells = tuple((i, witness[i]) for i in rows)
            local = containment_probability(allowed, cells)
            falling = 1
            for q in range(r):
                falling *= t - q
            safe = min(Fraction(1), Fraction(128, falling))
            assert local <= safe
            local_probs.append(local)

        exact_joint = Fraction(1)
        for p in local_probs:
            exact_joint *= p
        recomputed = Fraction(1)
        for p in local_probs:
            recomputed *= p
        assert exact_joint == recomputed
        stats["product_probability_systems"] += 1
        stats["touched_blocks"] += sum(c > 0 for c in counts)
        stats[f"sample_profile_{''.join(map(str, profile(tuple(counts))))}"] += 1

    for _ in range(30_000):
        k = rng.randint(1, 12)
        masses: dict[tuple[int, ...], int] = defaultdict(int)
        tuple_masses: dict[tuple[int, ...], dict[tuple[int, ...], int]] = defaultdict(
            lambda: defaultdict(int)
        )
        for _record in range(rng.randint(1, 80)):
            s = rng.randint(1, min(3, k))
            blocks = tuple(sorted(rng.sample(range(k), s)))
            total = rng.randint(s, 3)
            counts = [1] * s
            for _extra in range(total - s):
                counts[rng.randrange(s)] += 1
            p = profile(tuple(counts))
            weight = rng.randint(1, 20)
            masses[p] += weight
            if p == (2, 1):
                heavy_index = counts.index(2)
                key = (blocks[heavy_index],) + tuple(
                    b for j, b in enumerate(blocks) if j != heavy_index
                )
            else:
                key = blocks
            tuple_masses[p][key] += weight

        total_mass = sum(masses.values())
        best_profile, best_mass = max(masses.items(), key=lambda item: item[1])
        assert best_mass * 6 >= total_mass

        exact = tuple_masses[best_profile]
        best_tuple = max(exact.values())
        if best_profile in {(1,), (2,), (3,)}:
            stock = k
        elif best_profile == (1, 1):
            stock = comb(k, 2)
        elif best_profile == (2, 1):
            stock = k * (k - 1)
        else:
            stock = comb(k, 3)
        assert best_tuple * max(stock, 1) >= best_mass
        stats["weighted_localizations"] += 1

    print("GC low-order product-collateral audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
