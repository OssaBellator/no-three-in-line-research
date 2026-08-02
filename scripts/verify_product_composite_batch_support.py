#!/usr/bin/env python3
"""Verify support sizes of atomic two-cycle composite repair batches."""
from __future__ import annotations

from collections import Counter

from verify_product_batch_repair import alternating_neighbour_masks, state_mask
from verify_product_hybrid_repair import (
    FactorPair,
    enumerate_degree_two_states,
    product_host,
    triple_potential,
)


def support_census(
    outer: FactorPair,
    inner: FactorPair,
    orientation: str,
    expected_traps: int,
    expected_supports: Counter[int],
) -> None:
    host = product_host(outer, inner, orientation)
    states = enumerate_degree_two_states(host)
    edge_index = {edge: index for index, edge in enumerate(host)}
    masks = tuple(state_mask(state, edge_index) for state in states)
    mask_to_state = {mask: index for index, mask in enumerate(masks)}
    potentials = tuple(triple_potential(state) for state in states)

    neighbours: list[tuple[int, ...]] = []
    for state in states:
        neighbours.append(
            tuple(
                mask_to_state[mask]
                for mask in alternating_neighbour_masks(host, state)
            )
        )

    traps = [
        index
        for index, value in enumerate(potentials)
        if value > 0
        and all(
            potentials[neighbour] >= value
            for neighbour in neighbours[index]
        )
    ]
    assert len(traps) == expected_traps

    supports: Counter[int] = Counter()
    for start in traps:
        candidates: list[tuple[int, int, int]] = []
        for middle in neighbours[start]:
            for endpoint in neighbours[middle]:
                if potentials[endpoint] < potentials[start]:
                    removed = (masks[start] ^ masks[endpoint]).bit_count() // 2
                    candidates.append(
                        (removed, potentials[middle], potentials[endpoint])
                    )
        assert candidates, start
        removed, _, _ = min(candidates)
        supports[removed] += 1

    assert supports == expected_supports
    print(
        f"side={len(host) // 4}, orientation={orientation}: "
        f"traps={len(traps)}, minimum composite-batch supports={dict(supports)}"
    )


def main() -> None:
    family_2 = ((0, 1), (1, 0))
    family_a = ((0, 2, 1), (1, 0, 2))
    family_b = ((1, 2, 0), (2, 0, 1))

    support_census(
        outer=family_2,
        inner=family_a,
        orientation="cf",
        expected_traps=10,
        expected_supports=Counter({4: 8, 7: 2}),
    )
    support_census(
        outer=family_a,
        inner=family_b,
        orientation="cf",
        expected_traps=24,
        expected_supports=Counter({6: 12, 7: 8, 8: 4}),
    )
    support_census(
        outer=family_b,
        inner=family_a,
        orientation="cf",
        expected_traps=24,
        expected_supports=Counter({6: 12, 7: 8, 8: 4}),
    )


if __name__ == "__main__":
    main()
