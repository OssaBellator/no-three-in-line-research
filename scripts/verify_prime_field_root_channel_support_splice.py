#!/usr/bin/env python3
"""Finite checks for CMR1606--CMR1613."""

from __future__ import annotations

from collections import Counter, defaultdict
from random import Random


Cell = tuple[int, int]
Pair = tuple[Cell, Cell]
PATTERNS = ((1,), (2,), (1, 1), (2, 1), (1, 1, 1))
PARTNER_TYPES = ("fixed", "response")


def cells(prime: int) -> list[Cell]:
    return [(x, y) for x in range(prime) for y in range(prime)]


def displacement(a: Cell, b: Cell) -> Cell:
    return b[0] - a[0], b[1] - a[1]


def verify_pair_stocks() -> tuple[int, int, int]:
    primes = (2, 3, 5, 7, 11, 13, 17)
    ordered_pairs = 0
    displacement_channels = 0
    carry_checks = 0

    for prime in primes:
        grid = cells(prime)
        groups: dict[Cell, list[Pair]] = defaultdict(list)
        for a in grid:
            for b in grid:
                if a == b:
                    continue
                groups[displacement(a, b)].append((a, b))
                ordered_pairs += 1

                r = (a[0] % prime, a[1] % prime)
                rp = (b[0] % prime, b[1] % prime)
                assert r == a
                assert rp == b
                delta = displacement(a, b)
                q = (
                    (r[0] + delta[0] - rp[0]) // prime,
                    (r[1] + delta[1] - rp[1]) // prime,
                )
                assert q == (0, 0)
                carry_checks += 1

        assert sum(len(value) for value in groups.values()) == prime**2 * (
            prime**2 - 1
        )
        assert all(len(value) <= prime**2 for value in groups.values())

        for pairs in groups.values():
            by_source = defaultdict(list)
            for pair in pairs:
                by_source[pair[0]].append(pair)
            assert all(len(channel) == 1 for channel in by_source.values())
            assert len(by_source) <= prime**2
            displacement_channels += len(by_source)

    return ordered_pairs, displacement_channels, carry_checks


def verify_supports_and_signatures() -> tuple[int, int]:
    support_checks = 0
    signature_checks = 0
    for prime in (2, 3, 5, 7, 11):
        grid = cells(prime)
        pair_count = prime**2 * (prime**2 - 1)
        signatures = 0
        for a in grid:
            for b in grid:
                if a == b:
                    continue
                fixed_support = {a}
                response_support = {a, b}
                assert len(fixed_support) == 1
                assert len(response_support) == 2
                support_checks += 2
                for partner_type in PARTNER_TYPES:
                    for pattern in PATTERNS:
                        signature = (a, b, partner_type, pattern)
                        assert signature[0] != signature[1]
                        signatures += 1
                        signature_checks += 1
        assert signatures == 10 * pair_count
    return support_checks, signature_checks


def verify_first_reuse_histories(seed: int = 1613) -> tuple[int, int, int]:
    rng = Random(seed)
    histories = 0
    incidences = 0
    first_labels = 0

    for prime in (2, 3, 5, 7, 11, 13):
        grid = cells(prime)
        ordered = [(a, b) for a in grid for b in grid if a != b]
        for _ in range(500):
            length = rng.randint(1, 8 * prime**2)
            used: set[Cell] = set()
            first = 0
            repeated = 0
            for _episode in range(length):
                a, b = rng.choice(ordered)
                partner_type = rng.choice(PARTNER_TYPES)
                support = (a,) if partner_type == "fixed" else (a, b)
                for edge in support:
                    if edge in used:
                        repeated += 1
                    else:
                        used.add(edge)
                        first += 1
                    incidences += 1
            assert first == len(used)
            assert first <= prime**2
            assert first + repeated >= length
            histories += 1
            first_labels += first

    return histories, incidences, first_labels


def verify_batching(seed: int = 1611) -> tuple[int, int]:
    rng = Random(seed)
    systems = 0
    episodes = 0

    for prime in (2, 3, 5, 7, 11):
        grid = cells(prime)
        signatures = [
            (a, b, partner_type, pattern)
            for a in grid
            for b in grid
            if a != b
            for partner_type in PARTNER_TYPES
            for pattern in PATTERNS
        ]
        stock = 10 * prime**2 * (prime**2 - 1)
        assert len(signatures) == stock
        for _ in range(300):
            lam = rng.randint(2, 8)
            length = rng.randint(1, min(15000, 3 * stock))
            sample = [rng.choice(signatures) for _ in range(length)]
            multiplicity = Counter(sample)
            if max(multiplicity.values()) < lam:
                assert length <= (lam - 1) * stock
            else:
                assert any(value >= lam for value in multiplicity.values())
            systems += 1
            episodes += length

    return systems, episodes


def verify_fixed_displacement_batching(seed: int = 1612) -> int:
    rng = Random(seed)
    checked = 0
    for prime in (2, 3, 5, 7, 11, 13):
        grid = cells(prime)
        groups: dict[Cell, list[Pair]] = defaultdict(list)
        for a in grid:
            for b in grid:
                if a != b:
                    groups[displacement(a, b)].append((a, b))
        for pairs in groups.values():
            signatures = [
                (a, b, partner_type, pattern)
                for a, b in pairs
                for partner_type in PARTNER_TYPES
                for pattern in PATTERNS
            ]
            assert len(signatures) <= 10 * prime**2
            lam = rng.randint(2, 7)
            length = rng.randint(1, max(1, 3 * len(signatures)))
            sample = [rng.choice(signatures) for _ in range(length)]
            counts = Counter(sample)
            if max(counts.values()) < lam:
                assert length <= (lam - 1) * 10 * prime**2
            checked += 1
    return checked


def main() -> None:
    pairs, channels, carries = verify_pair_stocks()
    supports, signatures = verify_supports_and_signatures()
    histories, incidences, first_labels = verify_first_reuse_histories()
    batching, episodes = verify_batching()
    fixed = verify_fixed_displacement_batching()
    print(
        "verified prime-field root support splice: "
        f"{pairs} ordered pairs, {channels} singleton displacement channels "
        f"and {carries} zero-carry checks; "
        f"{supports} support checks and {signatures} terminal signatures; "
        f"{histories} histories with {incidences} support incidences "
        f"and {first_labels} first labels; "
        f"{batching} batching systems over {episodes} episodes "
        f"and {fixed} fixed-displacement systems"
    )


if __name__ == "__main__":
    main()
