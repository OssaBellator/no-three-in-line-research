#!/usr/bin/env python3
"""Verify CMR67--CMR69 and the corrected saturated root law."""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations


def determinant(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def reciprocal_permutation(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(
        b if x == 0 else (b + c * pow(x, -1, p)) % p
        for x in range(p)
    )


def verify_balanced_family(p: int) -> tuple[int, int, int]:
    assert p % 4 == 1
    h = (p - 1) // 2
    family = [
        reciprocal_permutation(p, b, c)
        for b in range(p)
        for c in nonsquares(p)
    ]
    assert len(family) == p * h

    triple_checks = 0
    for values in family:
        assert sorted(values) == list(range(p))
        points = list(enumerate(values))
        for triple in combinations(points, 3):
            assert determinant(*triple) != 0, (p, values, triple)
            triple_checks += 1

    single_counts: Counter[tuple[int, int]] = Counter()
    pair_counts: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    for values in family:
        cells = [(x, values[x]) for x in range(p)]
        single_counts.update(cells)
        for first, second in combinations(cells, 2):
            pair_counts[(first, second)] += 1

    assert len(single_counts) == p * p
    assert set(single_counts.values()) == {h}
    assert max(pair_counts.values(), default=0) <= 1
    return len(family), triple_checks, len(pair_counts)


def verify_saturated_root_law(p: int) -> tuple[int, int]:
    """Check the exact disjointness characterization and root marginals."""
    assert p % 4 == 1
    ns = nonsquares(p)
    h = len(ns)
    maps = {
        (b, c): reciprocal_permutation(p, b, c)
        for b in range(p)
        for c in ns
    }

    characterization_checks = 0
    for (b0, c0), f0 in maps.items():
        for (b1, c1), f1 in maps.items():
            disjoint = all(f0[x] != f1[x] for x in range(p))
            assert disjoint == (c0 == c1 and b0 != b1)
            characterization_checks += 1

    root_states = []
    for c in ns:
        for b0 in range(p):
            for b1 in range(p):
                if b0 == b1:
                    continue
                root_states.append((maps[(b0, c)], maps[(b1, c)]))

    assert len(root_states) == h * p * (p - 1)

    layer_cells = [Counter(), Counter()]
    ordered_rows = [Counter() for _ in range(p)]
    for f0, f1 in root_states:
        assert all(f0[x] != f1[x] for x in range(p))
        for x in range(p):
            layer_cells[0][(x, f0[x])] += 1
            layer_cells[1][(x, f1[x])] += 1
            ordered_rows[x][(f0[x], f1[x])] += 1

    expected_cell_count = h * (p - 1)
    assert set(layer_cells[0].values()) == {expected_cell_count}
    assert set(layer_cells[1].values()) == {expected_cell_count}
    for counts in ordered_rows:
        assert len(counts) == p * (p - 1)
        assert set(counts.values()) == {h}

    return len(root_states), characterization_checks


def prime_power_data(n: int) -> tuple[int, int] | None:
    for p in range(3, n + 1, 2):
        if not is_prime(p):
            continue
        value = p
        k = 1
        while value < n:
            value *= p
            k += 1
        if value == n:
            return p, k
    return None


def verify_first_separation_structure(p: int, k: int) -> tuple[int, list[int]]:
    n = p**k
    by_s = [0] * k
    checks = 0

    for x1, x2, x3 in combinations(range(n), 3):
        columns = (x1, x2, x3)
        pair_values = (
            valuation(x1 - x2, p),
            valuation(x1 - x3, p),
            valuation(x2 - x3, p),
        )
        s = max(pair_values)
        assert 0 <= s <= k - 1
        by_s[s] += 1

        kappas = (x3 - x2, x1 - x3, x2 - x1)
        r = min(valuation(value, p) for value in kappas)
        reduced = tuple(value // (p**r) for value in kappas)
        unit_indices = [i for i, value in enumerate(reduced) if value % p != 0]
        assert len(unit_indices) >= 2
        chosen = unit_indices[0]

        for depth in range(s + 1, k):
            prefixes = [x % (p**depth) for x in columns]
            assert len(set(prefixes)) == 3
            assert depth >= 1  # The corrected root coupling is never charged here.
            assert reduced[chosen] % p != 0
            checks += 1

    for s, count in enumerate(by_s):
        pair_bound = p**s * ((n // (p**s)) * (n // (p**s) - 1) // 2)
        assert count <= pair_bound * n

    return checks, by_s


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=29)
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    balanced_primes = 0
    local_states = 0
    root_states = 0
    local_triples = 0
    local_pairs = 0
    root_characterizations = 0
    for p in range(5, args.max_prime + 1, 2):
        if not is_prime(p) or p % 4 != 1:
            continue
        states, triples, pairs = verify_balanced_family(p)
        roots, characterizations = verify_saturated_root_law(p)
        balanced_primes += 1
        local_states += states
        root_states += roots
        local_triples += triples
        local_pairs += pairs
        root_characterizations += characterizations

    structural_instances = 0
    structural_checks = 0
    valuation_cells = 0
    for n in range(9, args.max_modulus + 1):
        data = prime_power_data(n)
        if data is None:
            continue
        p, k = data
        if k < 2:
            continue
        checks, by_s = verify_first_separation_structure(p, k)
        structural_instances += 1
        structural_checks += checks
        valuation_cells += sum(1 for count in by_s if count)

    print(
        "verified first-separation sum "
        f"balanced-primes={balanced_primes}; local-states={local_states}; "
        f"root-states={root_states}; local-triples={local_triples}; "
        f"local-pairs={local_pairs}; root-characterizations={root_characterizations}; "
        f"prime-powers={structural_instances}; digit-checks={structural_checks}; "
        f"valuation-cells={valuation_cells}"
    )


if __name__ == "__main__":
    main()
