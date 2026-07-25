#!/usr/bin/env python3
"""Verify PX185--PX186 arithmetic low-collateral rematching."""
from __future__ import annotations

from itertools import combinations
from random import Random

Permutation = tuple[int, ...]


def extremal_permutation(prime: int) -> Permutation:
    return tuple(
        1 if value == 1 else value * pow((value - 1) % prime, -1, prime) % prime
        for value in range(prime)
    )


def orbit_map(
    base: Permutation,
    scale: int,
    row_translation: int,
    image_translation: int,
) -> Permutation:
    prime = len(base)
    inverse_scale = pow(scale, -1, prime)
    return tuple(
        (
            scale
            * base[((row - row_translation) * inverse_scale) % prime]
            + image_translation
        )
        % prime
        for row in range(prime)
    )


def determinant_mod(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
    prime: int,
) -> int:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (second[1] - first[1]) * (third[0] - first[0])
    ) % prime


def triple_count(mapping: Permutation) -> int:
    prime = len(mapping)
    points = tuple(enumerate(mapping))
    return sum(
        determinant_mod(first, second, third, prime) == 0
        for first, second, third in combinations(points, 3)
    )


def maximum_line_occupancy(mapping: Permutation) -> int:
    prime = len(mapping)
    points = tuple(enumerate(mapping))
    maximum = 2
    for first, second in combinations(points, 2):
        occupancy = sum(
            determinant_mod(first, second, third, prime) == 0
            for third in points
        )
        maximum = max(maximum, occupancy)
    return maximum


def forbidden_union(
    first: Permutation,
    second: Permutation,
) -> set[tuple[int, int]]:
    return {
        (row, first[row]) for row in range(len(first))
    } | {
        (row, second[row]) for row in range(len(second))
    }


def forbidden_hits(
    mapping: Permutation,
    forbidden: set[tuple[int, int]],
) -> tuple[int, ...]:
    return tuple(
        row for row, image in enumerate(mapping) if (row, image) in forbidden
    )


def repair_forbidden_hits(
    mapping: Permutation,
    forbidden: set[tuple[int, int]],
) -> Permutation:
    current = list(mapping)
    prime = len(current)
    while True:
        bad_rows = [
            row for row, image in enumerate(current) if (row, image) in forbidden
        ]
        if not bad_rows:
            return tuple(current)
        assert len(bad_rows) <= 2
        row = bad_rows[0]
        protected = set(bad_rows)
        helper = None
        for candidate in range(prime):
            if candidate == row or candidate in protected:
                continue
            if (row, current[candidate]) in forbidden:
                continue
            if (candidate, current[row]) in forbidden:
                continue
            helper = candidate
            break
        assert helper is not None
        current[row], current[helper] = current[helper], current[row]


def random_permutation(prime: int, random: Random) -> Permutation:
    values = list(range(prime))
    random.shuffle(values)
    return tuple(values)


def verify_prime(prime: int) -> None:
    base = extremal_permutation(prime)
    assert sorted(base) == list(range(prime))
    assert triple_count(base) == (prime - 1) // 2
    assert maximum_line_occupancy(base) == 3

    random = Random(20260725 + prime)
    for trial in range(20):
        forbidden = forbidden_union(
            random_permutation(prime, random),
            random_permutation(prime, random),
        )
        best = None
        best_hits = prime + 1
        for scale in range(1, prime):
            for row_translation in range(prime):
                for image_translation in range(prime):
                    candidate = orbit_map(
                        base, scale, row_translation, image_translation
                    )
                    hits = len(forbidden_hits(candidate, forbidden))
                    if hits < best_hits:
                        best_hits = hits
                        best = candidate
                    if best_hits == 0:
                        break
                if best_hits == 0:
                    break
            if best_hits == 0:
                break
        assert best is not None
        assert best_hits <= 2
        repaired = repair_forbidden_hits(best, forbidden)
        assert sorted(repaired) == list(range(prime))
        assert not forbidden_hits(repaired, forbidden)
        count = triple_count(repaired)
        assert count <= 16 * prime
    print(
        f"p={prime}: base triples={(prime-1)//2}, random forbidden systems passed"
    )


def verify_real_transport() -> None:
    # A real collinearity in two arithmetic progressions reduces modulo p to a
    # modular collinearity of the normalized graph.
    for prime in (7, 11, 13):
        mapping = extremal_permutation(prime)
        row_start, row_step = 3, 4
        column_start, column_step = 5, 7
        points = tuple(
            (
                row_start + row_step * row,
                column_start + column_step * mapping[row],
            )
            for row in range(prime)
        )
        real_count = 0
        for indices in combinations(range(prime), 3):
            first, second, third = (points[index] for index in indices)
            determinant = (
                (second[0] - first[0]) * (third[1] - first[1])
                - (second[1] - first[1]) * (third[0] - first[0])
            )
            if determinant == 0:
                real_count += 1
                normalized = tuple((index, mapping[index]) for index in indices)
                assert determinant_mod(*normalized, prime) == 0
        assert real_count <= triple_count(mapping)
    print("arithmetic-progression real-to-modular transport verified")


def main() -> None:
    for prime in (7, 11, 13, 17, 19):
        verify_prime(prime)
    verify_real_transport()
    print("PX185--PX186 verified")


if __name__ == "__main__":
    main()
