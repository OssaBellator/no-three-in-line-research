#!/usr/bin/env python3
"""Verify PX106-PX107: quartic near-resolution and packing barrier."""
from __future__ import annotations

Permutation = tuple[int, ...]
Block = frozenset[int]


def roots_minus_one(p: int) -> tuple[int, ...]:
    return tuple(value for value in range(p) if value * value % p == p - 1)


def affine_map(p: int, slope: int, translation: int) -> Permutation:
    return tuple((slope * x + translation) % p for x in range(p))


def is_strong(mapping: Permutation) -> bool:
    p = len(mapping)
    return (
        len(set(mapping)) == p
        and len({(x - mapping[x]) % p for x in range(p)}) == p
        and len({(x + mapping[x]) % p for x in range(p)}) == p
    )


def square_blocks(p: int, slope: int) -> set[Block]:
    blocks: set[Block] = set()
    vertices = (0, 1, (-slope) % p, (1 - slope) % p)
    for a in range(p):
        for r in range(1, p):
            blocks.add(frozenset((a + r * value) % p for value in vertices))
    return blocks


def quartic_cosets(p: int, slope: int) -> tuple[Block, ...]:
    group = {1, slope, p - 1, (-slope) % p}
    unseen = set(range(1, p))
    result: list[Block] = []
    while unseen:
        value = min(unseen)
        coset = frozenset(value * element % p for element in group)
        result.append(coset)
        unseen -= coset
    return tuple(result)


def packed_mapping(
    p: int,
    slope: int,
    translation: int,
    centre: int,
    selected_cosets: set[int],
) -> Permutation:
    cosets = quartic_cosets(p, slope)
    coset_index = {
        value: index for index, coset in enumerate(cosets) for value in coset
    }
    result = []
    for x in range(p):
        if x == centre:
            result.append((slope * x + translation) % p)
            continue
        index = coset_index[(x - centre) % p]
        local_slope = -slope if index in selected_cosets else slope
        result.append(
            (local_slope * (x - centre) + slope * centre + translation) % p
        )
    return tuple(result)


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    blocks = square_blocks(p, slope)
    cosets = quartic_cosets(p, slope)
    assert len(cosets) == (p - 1) // 4

    all_classes: list[set[Block]] = []
    for centre in range(p):
        parallel_class = {
            frozenset((centre + value) % p for value in coset)
            for coset in cosets
        }
        assert len(parallel_class) == (p - 1) // 4
        assert set().union(*parallel_class) == set(range(p)) - {centre}
        assert sum(len(block) for block in parallel_class) == p - 1
        assert parallel_class <= blocks
        all_classes.append(parallel_class)

    assert set().union(*all_classes) == blocks
    assert sum(len(parallel_class) for parallel_class in all_classes) == len(blocks)
    assert all(
        first.isdisjoint(second)
        for index, first in enumerate(all_classes)
        for second in all_classes[index + 1 :]
    )

    translation = 3 % p
    for centre in (0, 1, p // 2):
        count = len(cosets)
        seen: set[Permutation] = set()
        for bits in range(1 << count):
            chosen = {index for index in range(count) if bits & (1 << index)}
            mapping = packed_mapping(p, slope, translation, centre, chosen)
            assert is_strong(mapping)
            seen.add(mapping)
        assert len(seen) == 1 << count

        all_flipped = packed_mapping(
            p, slope, translation, centre, set(range(count))
        )
        expected = tuple(
            (-slope * x + translation + 2 * slope * centre) % p
            for x in range(p)
        )
        assert all_flipped == expected

    root = affine_map(p, slope, translation)
    decoded: dict[tuple[int, int], Block] = {}
    for centre in range(p):
        for coset in cosets:
            block = frozenset((centre + value) % p for value in coset)
            for x in block:
                y = (-slope * x + translation + 2 * slope * centre) % p
                key = (x, y)
                assert y != root[x]
                assert key not in decoded
                decoded[key] = block
    assert len(decoded) == p * (p - 1)
    assert all(
        (x, y) in decoded
        for x in range(p)
        for y in range(p)
        if y != root[x]
    )

    block_count = p * (p - 1) // 4
    labelled_triples = 2 * p * block_count * 4
    near_matching_size = (p - 1) // 4
    lower_probability = (4 * near_matching_size) / labelled_triples
    assert lower_probability == 1 / (2 * p * p)
    spread_constant = lower_probability * p * (p - 1) * (p - 2)

    print(
        f"p={p}: classes={p}, blocks={len(blocks)}, cube=2^{len(cosets)}, "
        f"packing_K3_lower={spread_constant:.6f}"
    )


def main() -> None:
    for p in (5, 13, 17, 29):
        verify_prime(p)
    print("quartic near-resolution and packing barrier verified")


if __name__ == "__main__":
    main()
