#!/usr/bin/env python3
"""Verify OP4j rank-three matching to product-carry dispersion."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb

try:
    from scripts.verify_phase_geometric_labels import (
        CarryStarRoute,
        FactorCertificate,
        Point,
        channel,
        classify_factor,
        determinant,
    )
    from scripts.verify_phase_paid_edge_density import divisor_cap
except ModuleNotFoundError:
    from verify_phase_geometric_labels import (  # type: ignore[no-redef]
        CarryStarRoute,
        FactorCertificate,
        Point,
        channel,
        classify_factor,
        determinant,
    )
    from verify_phase_paid_edge_density import (  # type: ignore[no-redef]
        divisor_cap,
    )


Weight = Fraction


@dataclass(frozen=True)
class RankThreeFactor:
    source_factor: int
    points: tuple[Point, Point, Point]
    support_scope: frozenset[int]
    weight: Weight = Fraction(1)


@dataclass(frozen=True)
class RankThreeRoute:
    source_factor: int
    profile: tuple[object, ...]
    signature: tuple[object, ...]
    endpoints: tuple[Point, Point]
    anchor: Point
    certificate: FactorCertificate


def canonical_route(
    factor: RankThreeFactor,
    prime: int,
) -> RankThreeRoute:
    assert len(factor.support_scope) == 3
    assert factor.weight >= 0
    assert determinant(*factor.points) == 0
    certificate = classify_factor(prime, factor.points)
    channels = certificate.channels
    multiplicities = {
        value: channels.count(value)
        for value in set(channels)
    }

    if certificate.kind == "two_channel_rational":
        repeated = next(
            value
            for value, count in multiplicities.items()
            if count == 2
        )
        singleton = next(
            value
            for value, count in multiplicities.items()
            if count == 1
        )
        route = next(
            item
            for item in certificate.carry_routes
            if channel(item.anchor, prime) == singleton
        )
        assert route.signature[0][0] == repeated
        assert route.signature[1][0] == repeated
        carry_left = route.signature[0][1]
        carry_right = route.signature[1][1]
        profile: tuple[object, ...] = (
            "two_plus_one",
            repeated,
            singleton,
        )
        signature: tuple[object, ...] = (
            repeated,
            min(carry_left, carry_right),
            max(carry_left, carry_right),
        )
    else:
        assert certificate.kind == "three_channel_carry"
        ordered = tuple(
            sorted(
                (
                    channel(point, prime),
                    point,
                )
                for point in factor.points
            )
        )
        anchor_channel, anchor = ordered[0]
        endpoint_data = ordered[1:]
        endpoints = tuple(item[1] for item in endpoint_data)
        route = next(
            item
            for item in certificate.carry_routes
            if item.anchor == anchor
        )
        endpoint_carries = {
            point: (channel_value, carry)
            for (channel_value, carry), point in zip(
                route.signature,
                route.endpoints,
            )
        }
        profile = (
            "three_channel",
            *(item[0] for item in ordered),
        )
        signature = (
            endpoint_data[0][0],
            endpoint_carries[endpoint_data[0][1]][1],
            endpoint_data[1][0],
            endpoint_carries[endpoint_data[1][1]][1],
        )
        route = CarryStarRoute(
            anchor=anchor,
            endpoints=endpoints,
            signature=(
                endpoint_carries[endpoints[0]],
                endpoint_carries[endpoints[1]],
            ),
            cross_levels=None,
        )
        assert profile[1] == anchor_channel

    assert set(route.endpoints).isdisjoint({route.anchor})
    assert set(route.endpoints) | {route.anchor} == set(factor.points)
    return RankThreeRoute(
        source_factor=factor.source_factor,
        profile=profile,
        signature=signature,
        endpoints=route.endpoints,
        anchor=route.anchor,
        certificate=certificate,
    )


def profile_capacity(channel_count: int) -> int:
    assert channel_count >= 2
    return (
        channel_count * (channel_count - 1)
        + comb(channel_count, 3)
    )


def grouped(routes: tuple[RankThreeRoute, ...], key):
    buckets: dict[object, list[RankThreeRoute]] = defaultdict(list)
    for route in routes:
        buckets[key(route)].append(route)
    return {
        item: tuple(bucket)
        for item, bucket in buckets.items()
    }


def route_rank_three_matching(
    factors: tuple[RankThreeFactor, ...],
    prime: int,
    active_channels: frozenset[int],
    factor_cap: Weight,
) -> dict[str, object]:
    """Route a switch-disjoint rank-three matching arithmetically."""

    assert factors
    assert factor_cap > 0
    assert len(active_channels) >= 2
    assert all(
        len(factor.support_scope) == 3
        for factor in factors
    )
    assert all(
        left.support_scope.isdisjoint(right.support_scope)
        for left, right in combinations(factors, 2)
    )
    assert all(
        set(left.points).isdisjoint(right.points)
        for left, right in combinations(factors, 2)
    )
    assert all(
        channel(point, prime) in active_channels
        for factor in factors
        for point in factor.points
    )

    routes = tuple(canonical_route(factor, prime) for factor in factors)
    route_by_factor = {
        route.source_factor: route
        for route in routes
    }
    assert len(route_by_factor) == len(factors)
    factor_by_id = {
        factor.source_factor: factor
        for factor in factors
    }
    assert len(factor_by_id) == len(factors)

    profile_groups = grouped(routes, lambda route: route.profile)
    finite_profile_cap = profile_capacity(len(active_channels))
    assert len(profile_groups) <= finite_profile_cap

    count_profile, count_routes = max(
        profile_groups.items(),
        key=lambda item: (len(item[1]), repr(item[0])),
    )
    assert len(count_routes) * finite_profile_cap >= len(factors)
    count_signatures = grouped(
        count_routes,
        lambda route: route.signature,
    )

    cap = divisor_cap(prime)
    for bucket in count_signatures.values():
        endpoints = [
            point
            for route in bucket
            for point in route.endpoints
        ]
        assert len(endpoints) == len(set(endpoints))
        assert len(bucket) <= cap
    assert len(count_signatures) * cap >= len(count_routes)

    total_weight = sum(
        (factor.weight for factor in factors),
        Fraction(),
    )
    weight_profile, weight_routes = max(
        profile_groups.items(),
        key=lambda item: (
            sum(
                (
                    factor_by_id[route.source_factor].weight
                    for route in item[1]
                ),
                Fraction(),
            ),
            repr(item[0]),
        ),
    )
    profile_weight = sum(
        (
            factor_by_id[route.source_factor].weight
            for route in weight_routes
        ),
        Fraction(),
    )
    assert profile_weight * finite_profile_cap >= total_weight

    selected_factor_data = max(
        factors,
        key=lambda factor: (
            factor.weight,
            factor.source_factor,
        ),
    )
    selected_factor_weight = selected_factor_data.weight
    common = {
        "factor_count": len(factors),
        "total_weight": total_weight,
        "active_channel_count": len(active_channels),
        "profile_capacity": finite_profile_cap,
        "represented_profile_count": len(profile_groups),
        "count_profile": count_profile,
        "count_profile_size": len(count_routes),
        "count_signature_count": len(count_signatures),
        "weight_profile": weight_profile,
        "weight_profile_weight": profile_weight,
        "divisor_cap": cap,
    }
    if selected_factor_weight > factor_cap:
        return {
            "status": "heavy_rank_three_factor",
            **common,
            "source_factor": selected_factor_data.source_factor,
            "source_factor_weight": selected_factor_weight,
            "factor_cap": factor_cap,
        }

    signature_groups = grouped(
        weight_routes,
        lambda route: route.signature,
    )
    signature_loads: dict[object, Weight] = {}
    for signature, bucket in signature_groups.items():
        endpoints = [
            point
            for route in bucket
            for point in route.endpoints
        ]
        assert len(endpoints) == len(set(endpoints))
        assert len(bucket) <= cap
        load = sum(
            (
                factor_by_id[route.source_factor].weight
                for route in bucket
            ),
            Fraction(),
        )
        assert load <= factor_cap * cap
        signature_loads[signature] = load
    assert (
        len(signature_groups)
        * factor_cap
        * cap
        >= profile_weight
    )
    return {
        "status": "rank_three_carry_growth",
        **common,
        "factor_cap": factor_cap,
        "signature_count": len(signature_groups),
        "signature_loads": signature_loads,
    }


def all_real_factors(
    prime: int,
) -> tuple[tuple[Point, Point, Point], ...]:
    points = tuple(
        (x, y)
        for x in range(1, prime)
        for y in range(1, prime)
    )
    return tuple(
        triple
        for triple in combinations(points, 3)
        if determinant(*triple) == 0
        and len({channel(point, prime) for point in triple}) >= 2
    )


def greedy_point_matching(
    triples: tuple[tuple[Point, Point, Point], ...],
) -> tuple[tuple[Point, Point, Point], ...]:
    selected: list[tuple[Point, Point, Point]] = []
    used: set[Point] = set()
    for triple in triples:
        if set(triple).isdisjoint(used):
            selected.append(triple)
            used.update(triple)
    return tuple(selected)


def make_factors(
    triples: tuple[tuple[Point, Point, Point], ...],
    weights: tuple[Weight, ...] | None = None,
) -> tuple[RankThreeFactor, ...]:
    if weights is None:
        weights = tuple(Fraction(1) for _ in triples)
    assert len(weights) == len(triples)
    return tuple(
        RankThreeFactor(
            source_factor=index,
            points=triple,
            support_scope=frozenset(
                (3 * index, 3 * index + 1, 3 * index + 2)
            ),
            weight=weight,
        )
        for index, (triple, weight) in enumerate(zip(triples, weights))
    )


def verify_route_records(
    triples: tuple[tuple[Point, Point, Point], ...],
    prime: int,
) -> int:
    profile_signature_factors: dict[
        tuple[object, ...],
        list[RankThreeRoute],
    ] = defaultdict(list)
    for index, triple in enumerate(triples):
        factor = RankThreeFactor(
            source_factor=index,
            points=triple,
            support_scope=frozenset((0, 1, 2)),
        )
        route = canonical_route(factor, prime)
        profile_signature_factors[
            route.profile + route.signature
        ].append(route)
        assert set(route.endpoints) | {route.anchor} == set(triple)

    cap = divisor_cap(prime)
    for routes in profile_signature_factors.values():
        endpoint_set = {
            point
            for route in routes
            for point in route.endpoints
        }
        assert endpoint_set
        # A fixed signature uses at most two product-carry levels,
        # each of size at most the divisor cap.  Hence any
        # endpoint-disjoint subfamily has at most cap pairs.
        assert len(endpoint_set) <= 2 * cap
    return len(profile_signature_factors)


def verify_matching_outputs(
    triples: tuple[tuple[Point, Point, Point], ...],
    prime: int,
) -> int:
    by_profile: dict[
        tuple[int, ...],
        list[tuple[Point, Point, Point]],
    ] = defaultdict(list)
    for triple in triples:
        by_profile[
            tuple(sorted(channel(point, prime) for point in triple))
        ].append(triple)

    three_profile = max(
        (
            (profile, tuple(bucket))
            for profile, bucket in by_profile.items()
            if len(set(profile)) == 3
        ),
        key=lambda item: len(
            greedy_point_matching(item[1])
        ),
    )
    three_matching = greedy_point_matching(three_profile[1])
    assert len(three_matching) >= 3
    three_factors = make_factors(three_matching)
    three_result = route_rank_three_matching(
        three_factors,
        prime,
        frozenset(three_profile[0]),
        Fraction(1),
    )
    assert three_result["status"] == "rank_three_carry_growth"

    two_profile = max(
        (
            (profile, tuple(bucket))
            for profile, bucket in by_profile.items()
            if len(set(profile)) == 2
        ),
        key=lambda item: len(
            greedy_point_matching(item[1])
        ),
    )
    two_matching = greedy_point_matching(two_profile[1])
    assert len(two_matching) >= 2
    two_factors = make_factors(two_matching)
    two_result = route_rank_three_matching(
        two_factors,
        prime,
        frozenset(two_profile[0]),
        Fraction(1),
    )
    assert two_result["status"] == "rank_three_carry_growth"

    heavy_weights = (
        Fraction(5),
    ) + tuple(Fraction(1) for _ in three_matching[1:])
    heavy = route_rank_three_matching(
        make_factors(three_matching, heavy_weights),
        prime,
        frozenset(three_profile[0]),
        Fraction(1),
    )
    assert heavy["status"] == "heavy_rank_three_factor"
    assert heavy["source_factor_weight"] == 5

    available = tuple(
        triple
        for triple in two_matching
        if all(
            point not in {
                used_point
                for selected in three_matching[:2]
                for used_point in selected
            }
            for point in triple
        )
    )
    mixed_triples = three_matching[:2] + available[:2]
    if len(mixed_triples) >= 3:
        active = frozenset(
            channel(point, prime)
            for triple in mixed_triples
            for point in triple
        )
        mixed = route_rank_three_matching(
            make_factors(mixed_triples),
            prime,
            active,
            Fraction(1),
        )
        assert mixed["represented_profile_count"] >= 2
    return 4


def main() -> None:
    prime = 11
    triples = all_real_factors(prime)
    route_classes = verify_route_records(triples, prime)
    routed_outputs = verify_matching_outputs(triples, prime)
    print(
        "phase rank-three router verified:",
        f"{len(triples)} real factors,",
        f"{route_classes} profile-signature classes,",
        f"{routed_outputs} matching outputs",
    )


if __name__ == "__main__":
    main()
