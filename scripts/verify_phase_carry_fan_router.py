#!/usr/bin/env python3
"""Verify OP1b--OP1e carry routing for phase-factor fans."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import ceil


Point = tuple[int, int]
Triple = tuple[Point, Point, Point]


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def inv(value: int, prime: int) -> int:
    return pow(value, prime - 2, prime)


def determinant(left: Point, middle: Point, right: Point) -> int:
    return (middle[0] - left[0]) * (right[1] - left[1]) - (
        middle[1] - left[1]
    ) * (right[0] - left[0])


def divisor_count(value: int) -> int:
    value = abs(value)
    assert value > 0
    result = 0
    divisor = 1
    while divisor * divisor <= value:
        if value % divisor == 0:
            result += 1 if divisor * divisor == value else 2
        divisor += 1
    return result


def hyperbola(channel: int, prime: int) -> tuple[Point, ...]:
    return tuple(
        (x, channel * inv(x, prime) % prime)
        for x in range(1, prime)
    )


def subgroup(
    generator: int,
    order: int,
    prime: int,
) -> tuple[int, ...]:
    result = tuple(
        pow(generator, exponent, prime)
        for exponent in range(order)
    )
    assert len(set(result)) == order
    assert pow(generator, order, prime) == 1
    return result


def orbit_states(
    base_channel: int,
    generator: int,
    order: int,
    coset: tuple[int, ...],
    prime: int,
) -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(
            (
                x,
                base_channel
                * inv(pow(generator, phase, prime) * x % prime, prime)
                % prime,
            )
            for x in coset
        )
        for phase in range(order)
    )


def product_carry(
    channel: int,
    point: Point,
    prime: int,
) -> int:
    numerator = point[0] * point[1] - channel
    assert numerator % prime == 0
    return numerator // prime


def cross_carry(
    anchor: Point,
    anchor_channel: int,
    endpoint: Point,
    partner: Point,
    endpoint_channel: int,
    prime: int,
) -> int:
    numerator = (
        (endpoint[0] - anchor[0])
        * (partner[1] - anchor[1])
        - (anchor_channel - endpoint_channel)
    )
    assert numerator % prime == 0
    return numerator // prime


def maximum_bipartite_matching(
    edges: tuple[tuple[Point, Point], ...],
) -> tuple[tuple[Point, Point], ...]:
    adjacency: dict[Point, list[Point]] = defaultdict(list)
    for left, right in edges:
        adjacency[left].append(right)

    right_match: dict[Point, Point] = {}

    def augment(left: Point, seen: set[Point]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in right_match or augment(
                right_match[right],
                seen,
            ):
                right_match[right] = left
                return True
        return False

    for left in adjacency:
        augment(left, set())

    return tuple(
        (left, right)
        for right, left in right_match.items()
    )


def route_point_star(
    anchor: Point,
    pairs: tuple[tuple[Point, Point], ...],
    channel_of: dict[Point, int],
    channel_count: int,
    prime: int,
) -> int:
    assert pairs
    by_type: dict[
        tuple[int, int],
        list[tuple[Point, Point]],
    ] = defaultdict(list)
    for left, right in pairs:
        left_channel = channel_of[left]
        right_channel = channel_of[right]
        if left_channel <= right_channel:
            by_type[(left_channel, right_channel)].append((left, right))
        else:
            by_type[(right_channel, left_channel)].append((right, left))

    channel_type, typed_list = max(
        by_type.items(),
        key=lambda item: (len(item[1]), item[0]),
    )
    typed = tuple(typed_list)
    left_channel, right_channel = channel_type

    if left_channel == right_channel:
        flattened = tuple(point for pair in typed for point in pair)
        assert len(flattened) == len(set(flattened))
        selected = typed
    else:
        degrees = Counter(
            point
            for pair in typed
            for point in pair
        )
        assert max(degrees.values()) <= 2
        selected = maximum_bipartite_matching(typed)
        assert 2 * len(selected) >= len(typed)

    assert (
        len(selected) * channel_count * (channel_count + 1)
        >= len(pairs)
    )

    product_cap = max(
        divisor_count(value)
        for value in range(1, prime * prime)
    )
    cross_cap = max(
        divisor_count(value)
        for value in range(1, (prime - 2) ** 2 + 1)
    )
    signature_cap = max(product_cap, cross_cap)

    if left_channel != right_channel:
        signatures = Counter(
            (
                product_carry(left_channel, left, prime),
                product_carry(right_channel, right, prime),
            )
            for left, right in selected
        )
        assert max(signatures.values()) <= product_cap
    else:
        anchor_channel = channel_of[anchor]
        assert anchor_channel != left_channel
        levels: list[int] = []
        for left, right in selected:
            forward = cross_carry(
                anchor,
                anchor_channel,
                left,
                right,
                left_channel,
                prime,
            )
            reverse = cross_carry(
                anchor,
                anchor_channel,
                right,
                left,
                left_channel,
                prime,
            )
            assert forward == reverse
            levels.append(forward)
        signatures = Counter(levels)
        for level, multiplicity in signatures.items():
            value = anchor_channel - left_channel + prime * level
            assert value != 0
            assert multiplicity <= divisor_count(value)
        assert max(signatures.values()) <= cross_cap

    assert len(signatures) * signature_cap >= len(selected)
    assert (
        len(signatures)
        * channel_count
        * (channel_count + 1)
        * signature_cap
        >= len(pairs)
    )
    return len(signatures)


def verify_instance(
    prime: int,
    generator: int,
    order: int,
    base_channel: int,
    extra_channels: tuple[int, ...],
) -> None:
    coset = subgroup(generator, order, prime)
    states = orbit_states(
        base_channel,
        generator,
        order,
        coset,
        prime,
    )
    block = set(point for state in states for point in state)
    assert all(len(state) == order for state in states)
    assert len(block) == order * order

    rows = {point[1] for point in states[0]}
    columns = {point[0] for point in states[0]}
    phase_of: dict[Point, int] = {}
    state_channels: set[int] = set()
    for phase, state in enumerate(states):
        assert {point[0] for point in state} == columns
        assert {point[1] for point in state} == rows
        channel = (
            base_channel * inv(pow(generator, phase, prime), prime)
        ) % prime
        state_channels.add(channel)
        for point in state:
            assert point not in phase_of
            phase_of[point] = phase
            assert point[0] * point[1] % prime == channel
            carry = product_carry(channel, point, prime)
            assert 0 <= carry <= prime - 2
            for scalar in range(1, prime):
                wrap_x = scalar * point[0] // prime
                wrap_y = scalar * point[1] // prime
                assert 0 <= wrap_x <= scalar - 1
                assert 0 <= wrap_y <= scalar - 1

    channels = tuple(sorted(state_channels | set(extra_channels)))
    points = tuple(
        point
        for channel in channels
        for point in hyperbola(channel, prime)
    )
    channel_of = {
        point: channel
        for channel in channels
        for point in hyperbola(channel, prime)
    }
    assert len(channel_of) == len(points)

    triples = tuple(
        triple
        for triple in combinations(points, 3)
        if determinant(*triple) == 0
    )
    rooted: list[tuple[Triple, int]] = []
    for triple in triples:
        hits = tuple(point for point in triple if point in block)
        phases = {phase_of[point] for point in hits}
        if hits and len(phases) == 1:
            rooted.append((triple, phases.pop()))

    assert rooted
    by_phase: dict[int, list[Triple]] = defaultdict(list)
    for triple, phase in rooted:
        by_phase[phase].append(triple)

    largest_phase, phase_family_list = max(
        by_phase.items(),
        key=lambda item: (len(item[1]), item[0]),
    )
    phase_family = tuple(phase_family_list)
    assert len(phase_family) * order >= len(rooted)

    for prefix_size in range(1, len(phase_family) + 1):
        family = phase_family[:prefix_size]
        incidence = Counter(
            point
            for triple in family
            for point in triple
            if point in states[largest_phase]
        )
        anchor, multiplicity = max(
            incidence.items(),
            key=lambda item: (item[1], item[0]),
        )
        assert multiplicity * order >= len(family)
        pairs = tuple(
            tuple(point for point in triple if point != anchor)
            for triple in family
            if anchor in triple
        )
        assert len(pairs) == multiplicity
        signature_count = route_point_star(
            anchor,
            pairs,
            channel_of,
            len(channels),
            prime,
        )
        signature_cap = max(
            max(
                divisor_count(value)
                for value in range(1, prime * prime)
            ),
            max(
                divisor_count(value)
                for value in range(1, (prime - 2) ** 2 + 1)
            ),
        )
        assert (
            signature_count
            * order
            * len(channels)
            * (len(channels) + 1)
            * signature_cap
            >= len(family)
        )
        if prefix_size == len(phase_family):
            assert (
                signature_count
                * order
                * order
                * len(channels)
                * (len(channels) + 1)
                * signature_cap
                >= len(rooted)
            )


def main() -> None:
    verify_instance(
        prime=13,
        generator=3,
        order=3,
        base_channel=1,
        extra_channels=(2, 5),
    )
    verify_instance(
        prime=17,
        generator=4,
        order=4,
        base_channel=1,
        extra_channels=(2, 3),
    )
    print("OP phase-factor carry routing: exhaustive regressions passed")


if __name__ == "__main__":
    main()
