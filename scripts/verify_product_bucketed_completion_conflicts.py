#!/usr/bin/env python3
"""Verify PX162--PX164 bucket building blocks for exact completion.

The asymptotic conflict-degree estimates are symbolic. This finite harness
checks the algebraic ingredients used in them: balanced bucket fibres, local
secant degree, triangle pair-codegree, and role/row fibre counts.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations


def balanced_partition(prime: int, bucket_count: int) -> tuple[int, ...]:
    return tuple(
        min(bucket_count - 1, value * bucket_count // prime)
        for value in range(prime)
    )


def compatible_shape(
    prime: int,
    slope: int,
    row_ratio: int,
    image_ratio: int,
) -> bool:
    return (
        slope not in (0, 1, prime - 1)
        and row_ratio not in (0, 1)
        and image_ratio not in (0, 1)
        and (row_ratio - slope * image_ratio) % prime != 0
        and (row_ratio - 1 - slope * (image_ratio - 1)) % prime != 0
        and (row_ratio + slope * image_ratio) % prime != 0
        and (row_ratio - 1 + slope * (image_ratio - 1)) % prime != 0
    )


def secant_occurrences(prime: int, slope: int):
    for base_row in range(prime):
        for base_image in range(prime):
            for step in range(1, prime):
                yield (
                    base_row,
                    base_image,
                    step,
                ), (
                    (base_row, base_image),
                    (
                        (base_row + step) % prime,
                        (base_image + slope * step) % prime,
                    ),
                )


def triangle_occurrences(
    prime: int,
    slope: int,
    row_ratio: int,
    image_ratio: int,
):
    for base_row in range(prime):
        for base_image in range(prime):
            for step in range(1, prime):
                yield (
                    base_row,
                    base_image,
                    step,
                ), (
                    (base_row, base_image),
                    (
                        (base_row + step) % prime,
                        (base_image + slope * step) % prime,
                    ),
                    (
                        (base_row + row_ratio * step) % prime,
                        (base_image + image_ratio * slope * step) % prime,
                    ),
                )


def verify_prime(prime: int) -> None:
    bucket_count = max(2, round(prime**0.45))
    bucket = balanced_partition(prime, bucket_count)
    fibre_sizes = Counter(bucket)
    maximum_fibre = max(fibre_sizes.values())
    assert maximum_fibre <= (prime + bucket_count - 1) // bucket_count
    assert min(fibre_sizes.values()) >= prime // bucket_count

    # A secant bucket records (step, coarse base image). For a fixed slope,
    # projected edge and bucket, the edge can occur only in the first or second
    # role, hence degree at most two.
    for slope in range(2, prime - 1):
        local_degree: Counter[
            tuple[tuple[int, int], tuple[int, int]]
        ] = Counter()
        row_fibre: Counter[tuple[int, int, tuple[int, int]]] = Counter()
        for (base_row, base_image, step), edges in secant_occurrences(
            prime, slope
        ):
            key = (step, bucket[base_image])
            for role, edge in enumerate(edges):
                local_degree[(edge, key)] += 1
                row_fibre[(role, edge[0], key)] += 1
        assert max(local_degree.values()) <= 2
        assert max(row_fibre.values()) <= maximum_fibre

    # Check one compatible triangle shape at each prime. The identities are
    # shape-independent once compatibility holds.
    chosen = None
    for slope in range(2, prime - 1):
        for row_ratio in range(2, prime):
            for image_ratio in range(2, prime):
                if compatible_shape(prime, slope, row_ratio, image_ratio):
                    chosen = (slope, row_ratio, image_ratio)
                    break
            if chosen:
                break
        if chosen:
            break
    assert chosen is not None

    slope, row_ratio, image_ratio = chosen
    pair_codegree: Counter[
        tuple[int, tuple[tuple[int, int], tuple[int, int]]]
    ] = Counter()
    total_bucket: Counter[int] = Counter()
    role_row_bucket: Counter[tuple[int, int, int]] = Counter()
    for (base_row, base_image, step), edges in triangle_occurrences(
        prime, slope, row_ratio, image_ratio
    ):
        key = bucket[base_image]
        total_bucket[key] += 1
        for role, edge in enumerate(edges):
            role_row_bucket[(role, edge[0], key)] += 1
        for first, second in combinations(edges, 2):
            pair_codegree[(key, tuple(sorted((first, second))))] += 1

    # Without fixing roles, one projected pair has at most six assignments to
    # two of the three ordered roles.
    assert max(pair_codegree.values()) <= 6
    assert max(total_bucket.values()) <= prime * (prime - 1) * maximum_fibre
    assert max(role_row_bucket.values()) <= (prime - 1) * maximum_fibre

    print(
        f"p={prime}: buckets={bucket_count}, secant local degree<=2, "
        f"triangle pair codegree<={max(pair_codegree.values())}"
    )


def verify_exponent_choices() -> None:
    # For any desired exponent eta, theta=alpha=eta/3 and a fixed L with
    # theta(L-1)>2+eta/10 give polynomial margin in every packing count.
    for eta_times_100 in (5, 10, 20, 40):
        eta = eta_times_100 / 100
        theta = eta / 3
        epsilon = eta / 20
        length = int((2 + 2 * epsilon) / theta) + 3
        assert theta * (length - 1) > 2 + 2 * epsilon
        assert theta * (length - 1) > 1 + 2 * epsilon
        assert length >= 6
    print("symbolic bucket-exponent inequalities verified")


def main() -> None:
    for prime in (7, 11, 13, 17):
        verify_prime(prime)
    verify_exponent_choices()
    print("PX162--PX164 bucketed completion ingredients verified")


if __name__ == "__main__":
    main()
