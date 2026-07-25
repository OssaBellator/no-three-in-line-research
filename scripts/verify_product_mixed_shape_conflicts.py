#!/usr/bin/env python3
"""Verify PX164--PX166 anchored secants, stars, and row buckets."""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

Edge = tuple[int, int, int, int]
Shape = tuple[int, int, int]


def edge(prime: int, row: int, column: int) -> Edge:
    return row, column, (row - column) % prime, (row + column) % prime


def compatible(prime: int, shape: Shape) -> bool:
    slope, row_ratio, image_ratio = shape
    if slope in (0, 1, prime - 1):
        return False
    if row_ratio in (0, 1) or image_ratio in (0, 1):
        return False
    return all(
        value % prime != 0
        for value in (
            row_ratio - slope * image_ratio,
            row_ratio - 1 - slope * (image_ratio - 1),
            row_ratio + slope * image_ratio,
            row_ratio - 1 + slope * (image_ratio - 1),
        )
    )


def occurrence(
    prime: int,
    shape: Shape,
    base_row: int,
    step: int,
    base_image: int,
) -> tuple[Edge, Edge, Edge]:
    slope, row_ratio, image_ratio = shape
    return (
        edge(prime, base_row, base_image),
        edge(
            prime,
            (base_row + step) % prime,
            (base_image + slope * step) % prime,
        ),
        edge(
            prime,
            (base_row + row_ratio * step) % prime,
            (base_image + image_ratio * slope * step) % prime,
        ),
    )


def is_matching(items: tuple[Edge, ...]) -> bool:
    return all(
        len({item[part] for item in items}) == len(items)
        for part in range(4)
    )


def balanced_buckets(prime: int, bucket_count: int) -> dict[int, int]:
    return {
        row: min(bucket_count - 1, row * bucket_count // prime)
        for row in range(prime)
    }


def verify_anchor_secants(prime: int) -> None:
    anchor = edge(prime, 0, 0)
    for slope in range(prime):
        if slope in (0, 1, prime - 1):
            continue
        for role in (0, 1):
            partners = []
            for step in range(1, prime):
                if role == 0:
                    partner = edge(prime, step, slope * step % prime)
                else:
                    partner = edge(prime, -step % prime, -slope * step % prime)
                assert is_matching((anchor, partner))
                partners.append(partner)
            assert len(partners) == prime - 1
            assert len(set(partners)) == prime - 1


def verify_shape(prime: int, shape: Shape) -> None:
    occurrences = []
    for base_row in range(prime):
        for step in range(1, prime):
            for base_image in range(prime):
                item = occurrence(prime, shape, base_row, step, base_image)
                assert is_matching(item)
                occurrences.append(item)

    # For a fixed shape and centre role, a leaf edge has link degree at most two.
    for centre_role in range(3):
        links: dict[Edge, Counter[Edge]] = defaultdict(Counter)
        for item in occurrences:
            centre = item[centre_role]
            leaves = [item[index] for index in range(3) if index != centre_role]
            links[centre][leaves[0]] += 1
            links[centre][leaves[1]] += 1
        assert max(
            value
            for leaf_counts in links.values()
            for value in leaf_counts.values()
        ) <= 2

    bucket_count = 2
    bucket_of = balanced_buckets(prime, bucket_count)
    bucket_sizes = Counter(bucket_of.values())

    for old_size in (1, 2):
        for old_roles in combinations(range(3), old_size):
            distinguished = old_roles[0]
            new_roles = [role for role in range(3) if role not in old_roles]
            totals = Counter()
            row_counts = Counter()
            pair_counts = Counter()
            for item in occurrences:
                bucket = bucket_of[item[distinguished][0]]
                totals[bucket] += 1
                for role in new_roles:
                    row_counts[(bucket, role, item[role][0])] += 1
                if len(new_roles) == 2:
                    first, second = new_roles
                    pair_counts[
                        (bucket, item[first][0], item[second][0])
                    ] += 1

            for bucket, size in bucket_sizes.items():
                assert totals[bucket] == size * prime * (prime - 1)
            assert max(row_counts.values(), default=0) <= max(bucket_sizes.values()) * prime
            assert max(pair_counts.values(), default=0) <= prime


def main() -> None:
    for prime in (7, 11):
        verify_anchor_secants(prime)
        shapes = [
            (slope, row_ratio, image_ratio)
            for slope in range(prime)
            for row_ratio in range(prime)
            for image_ratio in range(prime)
            if compatible(prime, (slope, row_ratio, image_ratio))
        ]
        for shape in shapes:
            verify_shape(prime, shape)
        print(f"p={prime}: verified {len(shapes)} compatible mixed-shape tables")
    print("PX164--PX166 mixed shape framework verified")


if __name__ == "__main__":
    main()
