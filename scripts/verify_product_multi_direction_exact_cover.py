#!/usr/bin/env python3
"""Verify PX171--PX173 fixed-family simultaneous-rainbow hosts."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

Form = tuple[int, int]
Edge = tuple[int, ...]


def nonproportional(prime: int, first: Form, second: Form) -> bool:
    return (first[0] * second[1] - first[1] * second[0]) % prime != 0


def host_edge(prime: int, forms: tuple[Form, ...], x: int, y: int) -> Edge:
    return tuple((a * x + b * y) % prime for a, b in forms)


def verify_host(prime: int, forms: tuple[Form, ...]) -> None:
    assert all(form != (0, 0) for form in forms)
    assert all(
        nonproportional(prime, first, second)
        for first, second in combinations(forms, 2)
    )

    edges = [
        host_edge(prime, forms, x, y)
        for x in range(prime)
        for y in range(prime)
    ]
    assert len(set(edges)) == prime * prime

    for part in range(len(forms)):
        degrees = Counter(item[part] for item in edges)
        assert set(degrees.values()) == {prime}

    maximum_codegree = 0
    for first, second in combinations(range(len(forms)), 2):
        counts = Counter((item[first], item[second]) for item in edges)
        maximum_codegree = max(maximum_codegree, max(counts.values()))
    assert maximum_codegree == 1

    # Deleting a matching of size k removes at most (uniformity-1)k edges at
    # every remaining vertex.
    affine_matching = [
        host_edge(prime, forms, x, (2 * x + 1) % prime)
        for x in range(min(2, prime))
    ]
    assert all(
        len({item[part] for item in affine_matching}) == len(affine_matching)
        for part in range(len(forms))
    )
    deleted = [set() for _ in forms]
    for item in affine_matching:
        for part, value in enumerate(item):
            deleted[part].add(value)

    for part, value in enumerate(range(prime)):
        if value in deleted[part]:
            continue
        residual = 0
        for item in edges:
            if item[part] != value:
                continue
            if all(item[index] not in deleted[index] for index in range(len(forms))):
                residual += 1
        assert residual >= prime - (len(forms) - 1) * len(affine_matching)

    print(
        f"p={prime}: parts={len(forms)}, degree={prime}, codegree={maximum_codegree}"
    )


def verify_affine_orbit(prime: int, forms: tuple[Form, ...]) -> None:
    seed = tuple((x * x * x + 2 * x) % prime for x in range(prime))
    # This check is only the linear-form covariance identity; the seed need not
    # be a simultaneous-rainbow permutation.
    for scale in range(1, prime):
        inverse = pow(scale, -1, prime)
        for row_shift in range(prime):
            for image_shift in range(prime):
                transformed = tuple(
                    (
                        scale
                        * seed[inverse * (x - row_shift) % prime]
                        + image_shift
                    )
                    % prime
                    for x in range(prime)
                )
                for a, b in forms:
                    original_values = [
                        (a * u + b * seed[u]) % prime
                        for u in range(prime)
                    ]
                    transformed_values = [
                        (a * x + b * transformed[x]) % prime
                        for x in range(prime)
                    ]
                    expected = sorted(
                        (
                            scale * value
                            + a * row_shift
                            + b * image_shift
                        )
                        % prime
                        for value in original_values
                    )
                    assert sorted(transformed_values) == expected


def main() -> None:
    for prime in (7, 11):
        forms = (
            (1, 0),
            (0, 1),
            (1, 1),
            (1, prime - 1),
            (1, 2),
        )
        verify_host(prime, forms)
        verify_affine_orbit(prime, forms)
    print("PX171--PX173 fixed-family rainbow host verified")


if __name__ == "__main__":
    main()
