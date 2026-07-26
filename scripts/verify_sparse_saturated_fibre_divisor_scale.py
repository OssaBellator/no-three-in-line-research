#!/usr/bin/env python3
"""Finite checks for SAS5bi--SAS5bm."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt, sqrt
from random import Random


def divisors(value: int) -> list[int]:
    out = []
    for d in range(1, isqrt(value) + 1):
        if value % d == 0:
            out.append(d)
            if d * d != value:
                out.append(value // d)
    return sorted(out)


def valid_records(n: int, x: int, z: int, epsilon: int):
    difference = z - x
    D = abs(difference)
    records = []
    for g in divisors(D):
        a0 = difference // (epsilon * g)
        assert a0 != 0
        for b0 in range(-(n - 1), n):
            if b0 == 0 or b0 == a0 or gcd(abs(a0), abs(b0)) != 1:
                continue
            companion = x + epsilon * g * b0
            if not (0 <= companion < n):
                continue
            if companion in {x, z}:
                continue
            records.append((g, a0, b0, companion))
    return records


def exhaustive_arithmetic_checks(counts: Counter[str]) -> None:
    for n in range(4, 15):
        for x in range(n):
            for z in range(n):
                if z == x:
                    continue
                for epsilon in (-1, 1):
                    records = valid_records(n, x, z, epsilon)
                    D = abs(z - x)
                    for g, a0, b0, companion in records:
                        assert D % g == 0
                        assert z == x + a0 * epsilon * g
                        assert companion == x + b0 * epsilon * g
                        assert gcd(abs(a0), abs(b0)) == 1
                        assert (companion - x) % g == 0
                    counts["fixed-defect systems"] += 1
                    counts["primitive records"] += len(records)


def weighted_scale_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        n = rng.randint(5, 40)
        x, z = rng.sample(range(n), 2)
        epsilon = rng.choice((-1, 1))
        records = valid_records(n, x, z, epsilon)
        if not records:
            continue
        chosen = rng.sample(records, rng.randint(1, min(len(records), 18)))
        weighted = [(record, Fraction(rng.randint(1, 20), rng.randint(1, 5))) for record in chosen]
        by_scale = defaultdict(Fraction)
        companions = defaultdict(set)
        for (g, _a0, _b0, companion), weight in weighted:
            by_scale[g] += weight
            companions[g].add(companion)
        total = sum((weight for _record, weight in weighted), Fraction(0))
        tau = len(divisors(abs(z - x)))
        best_g, best_weight = max(by_scale.items(), key=lambda item: item[1])
        assert best_weight >= total / tau
        assert float(best_weight) + 1e-12 >= float(total) / (2 * sqrt(abs(z - x)))

        # Test both the safe-donor and saturated-scale alternatives.
        y = rng.randrange(n)
        scale_companions = companions[best_g]
        all_columns = set(range(n))
        possible_donors = list(all_columns - {z})
        donor_count = rng.randint(1, min(len(possible_donors), 10))
        donor_set = set(rng.sample(possible_donors, donor_count))
        safe = donor_set - {x, y} - scale_companions
        if safe:
            donor = min(safe)
            assert donor not in scale_companions
            for g, _a0, _b0, companion in (record for record, _weight in weighted if record[0] == best_g):
                assert g == best_g
                assert donor not in {x, z, companion}
            counts["safe scale repairs"] += 1
        else:
            retained = donor_set - {x, y}
            assert retained <= scale_companions
            difference = z - x
            a0 = difference // (epsilon * best_g)
            for donor in retained:
                assert (donor - x) % best_g == 0
                b0 = (donor - x) // (epsilon * best_g)
                assert gcd(abs(a0), abs(b0)) == 1
            d = len(donor_set)
            slots = 1 + (n - 1) // best_g
            assert d - 2 <= slots
            if d >= 4:
                assert best_g <= (n - 1) // (d - 3)
            counts["random saturated scales"] += 1
        counts["weighted scale systems"] += 1


def explicit_saturation_checks(counts: Counter[str]) -> None:
    rng = Random(811)
    for _ in range(30000):
        n = rng.randint(6, 50)
        x, z = rng.sample(range(n), 2)
        epsilon = rng.choice((-1, 1))
        records = valid_records(n, x, z, epsilon)
        if not records:
            continue
        by_scale = defaultdict(list)
        for record in records:
            by_scale[record[0]].append(record)
        g = rng.choice(list(by_scale))
        scale_records = by_scale[g]
        companions = sorted({record[3] for record in scale_records})
        if not companions:
            continue
        y = rng.randrange(n)
        donor_core = set(rng.sample(companions, rng.randint(1, min(len(companions), 8))))
        donor_set = set(donor_core)
        if rng.randrange(2) == 0:
            donor_set.add(x)
        if rng.randrange(2) == 0:
            donor_set.add(y)
        retained = donor_set - {x, y}
        assert retained <= set(companions)
        a0 = (z - x) // (epsilon * g)
        for donor in retained:
            assert donor % g == x % g
            b0 = (donor - x) // (epsilon * g)
            assert gcd(abs(a0), abs(b0)) == 1
        d = len(donor_set)
        assert d - 2 <= 1 + (n - 1) // g
        if d >= 4:
            assert g <= (n - 1) // (d - 3)
        counts["explicit saturated scales"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_arithmetic_checks(counts)
    weighted_scale_checks(counts)
    explicit_saturation_checks(counts)
    print("SAS5bi--SAS5bm saturated-fibre divisor-scale audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
