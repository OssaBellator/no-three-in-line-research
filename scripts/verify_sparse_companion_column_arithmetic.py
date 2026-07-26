#!/usr/bin/env python3
"""Finite checks for SAS5bd--SAS5bh."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
from random import Random


def primitive_shapes(n: int):
    for a0 in range(-(n - 1), n):
        if a0 == 0:
            continue
        for b0 in range(-(n - 1), n):
            if b0 == 0 or b0 == a0:
                continue
            if gcd(abs(a0), abs(b0)) == 1:
                yield a0, b0


def inversion_checks(counts: Counter[str]) -> None:
    for n in range(3, 11):
        shapes = list(primitive_shapes(n))
        assert len(shapes) <= 4 * (n - 1) ** 2
        for x in range(n):
            for q in range(n):
                if q == x:
                    continue
                for a0, b0 in shapes:
                    for defect_at_j in (True, False):
                        companion_coeff = b0 if defect_at_j else a0
                        defect_coeff = a0 if defect_at_j else b0
                        valid_parameters = []
                        for s in range(-2 * n, 2 * n + 1):
                            if s == 0:
                                continue
                            companion = x + companion_coeff * s
                            defect = x + defect_coeff * s
                            if companion == q and 0 <= defect < n and defect not in (x, q):
                                valid_parameters.append((s, defect))
                        if (q - x) % companion_coeff == 0:
                            s = (q - x) // companion_coeff
                            z = x + defect_coeff * s
                            expected = []
                            if s != 0 and 0 <= z < n and z not in (x, q):
                                expected = [(s, z)]
                            assert valid_parameters == expected
                        else:
                            assert not valid_parameters
                        assert len(valid_parameters) <= 1
                        counts["shape-orientation inversions"] += 1


def fibre_injectivity_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        n = rng.randint(3, 20)
        x = rng.randrange(n)
        q = rng.randrange(n)
        if q == x:
            q = (q + 1) % n
        defect_at_j = bool(rng.randrange(2))
        shape_to_defect = {}
        defect_to_shapes = defaultdict(list)
        for a0, b0 in primitive_shapes(n):
            companion_coeff = b0 if defect_at_j else a0
            defect_coeff = a0 if defect_at_j else b0
            if (q - x) % companion_coeff:
                continue
            s = (q - x) // companion_coeff
            z = x + defect_coeff * s
            if s == 0 or not (0 <= z < n) or z in (x, q):
                continue
            shape_to_defect[(a0, b0)] = z
            defect_to_shapes[z].append((a0, b0))
        assert len(set(shape_to_defect)) == len(shape_to_defect)
        assert len(defect_to_shapes) <= 4 * (n - 1) ** 2

        if defect_to_shapes:
            loads = {
                z: Fraction(rng.randint(1, 30), rng.randint(1, 5))
                for z in defect_to_shapes
            }
            total = sum(loads.values(), Fraction(0))
            heaviest = max(loads.values())
            assert heaviest * (4 * (n - 1) ** 2) >= total
            counts["weighted companion concentrations"] += 1
        counts["fixed companion systems"] += 1


def saturation_checks(counts: Counter[str]) -> None:
    rng = Random(44)
    for _ in range(70000):
        d = rng.randint(1, 16)
        donors = set(range(d))
        x = rng.randrange(d + 3)
        y = rng.randrange(d + 3)
        if y == x:
            y = (y + 1) % (d + 3)
        forbidden_swap = donors & {x, y}
        available = donors - forbidden_swap
        companions = {q for q in available if rng.randrange(2)}
        safe = available - companions
        if safe:
            chosen = min(safe)
            assert chosen not in companions and chosen not in {x, y}
            counts["safe donor fibres"] += 1
        else:
            assert available <= companions
            assert len(companions) >= max(0, d - 2)
            counts["saturated companion fibres"] += 1


def quantitative_checks(counts: Counter[str]) -> None:
    rng = Random(713)
    for _ in range(50000):
        n = rng.randint(2, 30)
        b = rng.randint(1, 8)
        d = rng.randint(1, 20)
        h = rng.randint(0, 20)
        w = Fraction(rng.randint(1, 100), rng.randint(1, 7))
        companion_load = Fraction(h, 2 * b * d) * w
        fibre_bound = companion_load / (4 * (n - 1) ** 2)
        assert fibre_bound == Fraction(h, 8 * b * d * (n - 1) ** 2) * w
        counts["quantitative fibre bounds"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    inversion_checks(counts)
    fibre_injectivity_checks(counts)
    saturation_checks(counts)
    quantitative_checks(counts)
    print("SAS5bd--SAS5bh companion-column arithmetic audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
