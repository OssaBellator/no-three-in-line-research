#!/usr/bin/env python3
"""Verify OP4m routing of paid current geometric defects."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import ceil

try:
    from scripts.verify_phase_carry_fan_router import route_point_star
    from scripts.verify_phase_geometric_labels import (
        Point,
        channel,
        determinant,
    )
    from scripts.verify_phase_paid_edge_density import divisor_cap
    from scripts.verify_phase_rank_three_router import (
        RankThreeFactor,
        all_real_factors,
        canonical_route,
        greedy_point_matching,
    )
except ModuleNotFoundError:
    from verify_phase_carry_fan_router import route_point_star
    from verify_phase_geometric_labels import Point, channel, determinant
    from verify_phase_paid_edge_density import divisor_cap
    from verify_phase_rank_three_router import (
        RankThreeFactor,
        all_real_factors,
        canonical_route,
        greedy_point_matching,
    )


Weight = Fraction


@dataclass(frozen=True)
class PaidDefect:
    source_factor: int
    points: tuple[Point, Point, Point]
    payment: Weight


def point_loads(
    factors: tuple[PaidDefect, ...],
) -> dict[Point, Weight]:
    loads: dict[Point, Weight] = defaultdict(Fraction)
    for factor in factors:
        for point in factor.points:
            loads[point] += factor.payment
    return dict(loads)


def greedy_paid_matching(
    factors: tuple[PaidDefect, ...],
    loads: dict[Point, Weight],
    point_cap: Weight,
) -> tuple[PaidDefect, ...]:
    remaining = {
        factor.source_factor: factor
        for factor in factors
    }
    assert len(remaining) == len(factors)
    selected: list[PaidDefect] = []
    deleted_total = Fraction()
    while remaining:
        source_factor = min(remaining)
        chosen = remaining[source_factor]
        chosen_points = set(chosen.points)
        deleted_ids = tuple(
            factor_id
            for factor_id, factor in remaining.items()
            if not chosen_points.isdisjoint(factor.points)
        )
        deleted_weight = sum(
            (remaining[factor_id].payment for factor_id in deleted_ids),
            Fraction(),
        )
        assert deleted_weight <= sum(
            (loads[point] for point in chosen.points),
            Fraction(),
        )
        assert deleted_weight <= 3 * point_cap
        selected.append(chosen)
        deleted_total += deleted_weight
        for factor_id in deleted_ids:
            del remaining[factor_id]

    assert deleted_total == sum(
        (factor.payment for factor in factors),
        Fraction(),
    )
    assert all(
        set(left.points).isdisjoint(right.points)
        for left, right in combinations(selected, 2)
    )
    return tuple(selected)


def route_paid_defects(
    factors: tuple[PaidDefect, ...],
    prime: int,
    active_channels: frozenset[int],
    point_cap: Weight,
    factor_cap: Weight,
) -> dict[str, object]:
    assert factors
    assert point_cap > 0
    assert factor_cap > 0
    assert len(active_channels) >= 2
    assert len({factor.source_factor for factor in factors}) == len(factors)
    assert len({frozenset(factor.points) for factor in factors}) == len(
        factors
    )
    assert all(factor.payment > 0 for factor in factors)
    assert all(
        len(set(factor.points)) == 3
        and determinant(*factor.points) == 0
        for factor in factors
    )
    assert all(
        channel(point, prime) in active_channels
        for factor in factors
        for point in factor.points
    )
    assert all(
        len({channel(point, prime) for point in factor.points}) >= 2
        for factor in factors
    )

    total_payment = sum(
        (factor.payment for factor in factors),
        Fraction(),
    )
    heaviest = max(
        factors,
        key=lambda factor: (factor.payment, factor.source_factor),
    )
    common = {
        "factor_count": len(factors),
        "total_payment": total_payment,
        "point_cap": point_cap,
        "factor_cap": factor_cap,
    }
    if heaviest.payment > factor_cap:
        return {
            "status": "heavy_current_source_factor",
            **common,
            "source_factor": heaviest.source_factor,
            "source_factor_payment": heaviest.payment,
        }

    loads = point_loads(factors)
    anchor, anchor_load = max(
        loads.items(),
        key=lambda item: (item[1], item[0]),
    )
    if anchor_load > point_cap:
        star = tuple(
            factor for factor in factors if anchor in factor.points
        )
        minimum_star_size = int(point_cap // factor_cap) + 1
        assert len(star) >= minimum_star_size
        pairs = tuple(
            tuple(point for point in factor.points if point != anchor)
            for factor in star
        )
        assert all(len(pair) == 2 for pair in pairs)
        channel_of = {
            point: channel(point, prime)
            for factor in star
            for point in factor.points
        }
        signature_count = route_point_star(
            anchor,
            pairs,
            channel_of,
            len(active_channels),
            prime,
        )
        return {
            "status": "paid_current_point_star",
            **common,
            "anchor": anchor,
            "anchor_load": anchor_load,
            "star_size": len(star),
            "minimum_star_size": minimum_star_size,
            "signature_count": signature_count,
        }

    matching = greedy_paid_matching(factors, loads, point_cap)
    minimum_matching_size = ceil(total_payment / (3 * point_cap))
    assert len(matching) >= minimum_matching_size

    routes = tuple(
        canonical_route(
            RankThreeFactor(
                source_factor=factor.source_factor,
                points=factor.points,
                support_scope=frozenset(
                    (
                        3 * index,
                        3 * index + 1,
                        3 * index + 2,
                    )
                ),
                weight=factor.payment,
            ),
            prime,
        )
        for index, factor in enumerate(matching)
    )
    buckets: dict[tuple[object, ...], list[int]] = defaultdict(list)
    for route in routes:
        buckets[(route.profile, route.signature)].append(
            route.source_factor
        )
    cap = divisor_cap(prime)
    assert all(len(bucket) <= cap for bucket in buckets.values())
    minimum_signatures = ceil(minimum_matching_size / cap)
    assert len(buckets) >= minimum_signatures
    return {
        "status": "paid_current_defect_matching",
        **common,
        "matching_size": len(matching),
        "minimum_matching_size": minimum_matching_size,
        "signature_count": len(buckets),
        "minimum_signature_count": minimum_signatures,
        "divisor_cap": cap,
    }


def abstract_greedy_bound(
    triples: tuple[tuple[int, int, int], ...],
    weights: tuple[Weight, ...],
    point_cap: Weight,
) -> int:
    active = tuple(
        (triple, weight)
        for triple, weight in zip(triples, weights)
        if weight > 0
    )
    assert active
    loads = {
        point: sum(
            (weight for triple, weight in active if point in triple),
            Fraction(),
        )
        for point in range(5)
    }
    assert max(loads.values()) <= point_cap
    remaining = list(active)
    selected: list[tuple[int, int, int]] = []
    while remaining:
        chosen, _ = remaining[0]
        chosen_set = set(chosen)
        deleted = tuple(
            item
            for item in remaining
            if not chosen_set.isdisjoint(item[0])
        )
        assert sum(
            (weight for _, weight in deleted),
            Fraction(),
        ) <= 3 * point_cap
        selected.append(chosen)
        remaining = [
            item
            for item in remaining
            if chosen_set.isdisjoint(item[0])
        ]
    total = sum((weight for _, weight in active), Fraction())
    assert len(selected) >= ceil(total / (3 * point_cap))
    return len(selected)


def verify_abstract_hypergraphs() -> tuple[int, int]:
    triples = tuple(combinations(range(5), 3))
    low_load_cases = 0
    star_cases = 0
    for integer_weights in product((0, 1, 2), repeat=len(triples)):
        if not any(integer_weights):
            continue
        weights = tuple(Fraction(weight) for weight in integer_weights)
        loads = tuple(
            sum(
                (
                    weight
                    for triple, weight in zip(triples, weights)
                    if point in triple
                ),
                Fraction(),
            )
            for point in range(5)
        )
        maximum_load = max(loads)
        maximum_factor = max(weights)
        abstract_greedy_bound(triples, weights, maximum_load)
        low_load_cases += 1

        if maximum_load > maximum_factor:
            point_cap = maximum_load - Fraction(1, 2)
            anchor = loads.index(maximum_load)
            star_size = sum(
                weight > 0 and anchor in triple
                for triple, weight in zip(triples, weights)
            )
            assert star_size >= int(point_cap // maximum_factor) + 1
            star_cases += 1
    return low_load_cases, star_cases


def make_paid(
    triples: tuple[tuple[Point, Point, Point], ...],
    weights: tuple[Weight, ...] | None = None,
) -> tuple[PaidDefect, ...]:
    if weights is None:
        weights = tuple(Fraction(1) for _ in triples)
    assert len(weights) == len(triples)
    return tuple(
        PaidDefect(index, triple, weight)
        for index, (triple, weight) in enumerate(zip(triples, weights))
        if weight > 0
    )


def verify_real_outputs(prime: int) -> tuple[int, int]:
    triples = all_real_factors(prime)
    active_channels = frozenset(
        channel(point, prime)
        for triple in triples
        for point in triple
    )

    heavy_weights = (Fraction(2),) + tuple(
        Fraction(1) for _ in triples[1:20]
    )
    heavy = route_paid_defects(
        make_paid(triples[:20], heavy_weights),
        prime,
        active_channels,
        Fraction(100),
        Fraction(1),
    )
    assert heavy["status"] == "heavy_current_source_factor"

    by_anchor: dict[Point, list[tuple[Point, Point, Point]]] = defaultdict(list)
    for triple in triples:
        for point in triple:
            by_anchor[point].append(triple)
    anchor, star_list = max(
        by_anchor.items(),
        key=lambda item: (len(item[1]), item[0]),
    )
    star_triples = tuple(star_list)
    star = route_paid_defects(
        make_paid(star_triples),
        prime,
        active_channels,
        Fraction(len(star_triples)) - Fraction(1, 2),
        Fraction(1),
    )
    assert star["status"] == "paid_current_point_star"
    assert star["anchor"] == anchor

    matching_triples = greedy_point_matching(triples)
    matching = route_paid_defects(
        make_paid(matching_triples),
        prime,
        active_channels,
        Fraction(1),
        Fraction(1),
    )
    assert matching["status"] == "paid_current_defect_matching"
    assert matching["matching_size"] == len(matching_triples)

    all_paid = make_paid(triples)
    loads = point_loads(all_paid)
    low_load = route_paid_defects(
        all_paid,
        prime,
        active_channels,
        max(loads.values()),
        Fraction(1),
    )
    assert low_load["status"] == "paid_current_defect_matching"

    return len(triples), 4


def main() -> None:
    abstract_cases, star_cases = verify_abstract_hypergraphs()
    real_factors, outputs = verify_real_outputs(11)
    print(
        "phase defect router verified:",
        f"{abstract_cases} weighted 3-graphs,",
        f"{star_cases} paid stars,",
        f"{real_factors} real factors,",
        f"{outputs} geometric outputs",
    )


if __name__ == "__main__":
    main()
