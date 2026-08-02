#!/usr/bin/env python3
"""Verify PX219--PX220 thinned joint-packet rank-three control."""
from __future__ import annotations

from itertools import combinations, permutations
from math import exp, factorial, sqrt
from random import Random


Arc = tuple[int, int]
Event = frozenset[Arc]


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def candidate_triples(
    endpoints: tuple[tuple[int, int], ...],
    indices: tuple[int, ...],
) -> tuple[frozenset[Arc], ...]:
    triples: set[frozenset[Arc]] = set()
    for row_indices in combinations(indices, 3):
        for column_indices in combinations(indices, 3):
            for image in permutations(column_indices):
                cells = frozenset(zip(row_indices, image))
                points = tuple(
                    (endpoints[row][0], endpoints[column][1])
                    for row, column in cells
                )
                if len(points) == 3 and collinear(*points):
                    triples.add(cells)
    return tuple(triples)


def random_endpoints(size: int, random: Random) -> tuple[tuple[int, int], ...]:
    rows = random.sample(range(-3 * size, 8 * size), size)
    columns = random.sample(range(20 * size, 35 * size), size)
    return tuple(zip(rows, columns))


def arithmetic_endpoints(size: int) -> tuple[tuple[int, int], ...]:
    return tuple((index, 2 * index + 1) for index in range(size))


def find_thinned_subset(
    endpoints: tuple[tuple[int, int], ...],
    random: Random,
) -> tuple[tuple[int, ...], int]:
    size = len(endpoints)
    target = max(3, int(sqrt(size) / 2))
    full = tuple(range(size))
    triples = candidate_triples(endpoints, full)
    best: tuple[int, ...] | None = None
    best_count: int | None = None
    for _ in range(800):
        chosen = tuple(
            index for index in range(size) if random.random() < size**-0.5
        )
        if len(chosen) < target:
            continue
        selected = set(chosen)
        count = sum(
            all(row in selected and column in selected for row, column in triple)
            for triple in triples
        )
        if best is None or count / len(chosen) ** 4 < best_count / len(best) ** 4:
            best = chosen
            best_count = count
    assert best is not None and best_count is not None
    return best, best_count


def restrict_packet(packet: tuple[Arc, ...], chosen: set[int]) -> tuple[Arc, ...]:
    return tuple(
        (row, column)
        for row, column in packet
        if row in chosen and column in chosen
    )


def is_partial_matching(packet: tuple[Arc, ...]) -> bool:
    return (
        len({row for row, _ in packet}) == len(packet)
        and len({column for _, column in packet}) == len(packet)
    )


def verify_thinning_and_packet_restriction() -> None:
    random = Random(219)
    for size in (9, 11, 13):
        for label, endpoints in (
            ("arithmetic", arithmetic_endpoints(size)),
            ("random", random_endpoints(size, random)),
        ):
            chosen, triple_count = find_thinned_subset(endpoints, random)
            selected = set(chosen)
            order = len(chosen)
            assert order >= max(3, int(sqrt(size) / 2))
            assert triple_count <= 3 * order**4

            identity = tuple((index, index) for index in range(size))
            shift = tuple((index, (index + 1) % size) for index in range(size))
            reversal = tuple((index, size - 1 - index) for index in range(size))
            restricted = tuple(
                restrict_packet(packet, selected)
                for packet in (identity, shift, reversal)
            )
            assert all(is_partial_matching(packet) for packet in restricted)
            assert len(restricted[0]) == order
            assert len(restricted[0]) * (len(restricted[0]) - 1) // 2 == (
                order * (order - 1) // 2
            )
            print(
                f"{label}, h={size}, s={order}: "
                f"triples={triple_count}, normalized={triple_count/order**4:.6f}"
            )
    print("packet-compatible square-root thinning verified")


def packet_events(packet: tuple[Arc, ...]) -> frozenset[Event]:
    return frozenset(
        frozenset(((first_row, second_column), (second_row, first_column)))
        for (first_row, first_column), (second_row, second_column) in combinations(
            packet, 2
        )
    )


def allowed_permutations(
    size: int,
    forbidden: frozenset[Arc],
    packets: tuple[tuple[Arc, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    events = set()
    for packet in packets:
        events.update(packet_events(packet))
    allowed = []
    for permutation in permutations(range(size)):
        chosen = frozenset((row, permutation[row]) for row in range(size))
        if chosen & forbidden:
            continue
        if any(event <= chosen for event in events):
            continue
        allowed.append(permutation)
    return tuple(allowed)


def count_selected_triples(
    permutation: tuple[int, ...],
    triples: tuple[frozenset[Arc], ...],
) -> int:
    chosen = frozenset((row, permutation[row]) for row in range(len(permutation)))
    return sum(triple <= chosen for triple in triples)


def falling_factorial(size: int, rank: int) -> int:
    return factorial(size) // factorial(size - rank)


def verify_exact_rank_three_transfer() -> None:
    size = 8
    endpoints = tuple((2 * index, index * index + 3) for index in range(size))
    triples = candidate_triples(endpoints, tuple(range(size)))
    identity = tuple((index, index) for index in range(size))
    shift = tuple((index, (index + 1) % size) for index in range(size))
    packets = (identity, shift)
    forbidden = frozenset((index, (index + 3) % size) for index in range(size))
    allowed = allowed_permutations(size, forbidden, packets)
    assert allowed

    exact_total = sum(
        count_selected_triples(permutation, triples) for permutation in allowed
    )
    exact_expectation = exact_total / len(allowed)
    spread_bound = exp(4 + 4 * len(packets)) * len(triples) / falling_factorial(
        size, 3
    )
    assert exact_expectation <= spread_bound

    identity_events = packet_events(identity)
    for permutation in allowed:
        chosen = frozenset((row, permutation[row]) for row in range(size))
        assert all(not event <= chosen for event in identity_events)

    print(
        "exact joint-release rank-three transfer verified: "
        f"family={len(allowed)}, triples={len(triples)}, "
        f"expectation={exact_expectation:.6f}"
    )


def verify_asymptotic_comparison() -> None:
    for degree in range(0, 6):
        for packet_count in range(1, 6):
            constant = exp(4 * degree + 4 * packet_count)
            for order in (128, 256, 512, 1024):
                linear = constant * order
                quadratic = order * (order - 1) / 2
                ratio = linear / quadratic
                assert abs(ratio - 2 * constant / (order - 1)) < 1e-12
    print("linear-versus-quadratic packet scale verified")


def main() -> None:
    verify_thinning_and_packet_restriction()
    verify_exact_rank_three_transfer()
    verify_asymptotic_comparison()
    print("PX219--PX220 verified")


if __name__ == "__main__":
    main()
