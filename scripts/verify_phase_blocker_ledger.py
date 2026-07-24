#!/usr/bin/env python3
"""Verify OP4k state-qualified rank-three blocker accounting."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import ceil
from typing import Hashable

try:
    from scripts.verify_phase_geometric_labels import Point, channel
    from scripts.verify_phase_paid_edge_density import divisor_cap
    from scripts.verify_phase_rank_three_router import (
        RankThreeFactor,
        canonical_route,
        all_real_factors,
        greedy_point_matching,
        make_factors,
    )
except ModuleNotFoundError:
    from verify_phase_geometric_labels import Point, channel
    from verify_phase_paid_edge_density import divisor_cap
    from verify_phase_rank_three_router import (
        RankThreeFactor,
        canonical_route,
        all_real_factors,
        greedy_point_matching,
        make_factors,
    )


Weight = Fraction
Signature = tuple[object, ...]
Token = tuple[Hashable, str, Signature]


@dataclass(frozen=True)
class LedgerResult:
    status: str
    tokens: frozenset[Token]
    represented: frozenset[Signature]
    new_tokens: frozenset[Token]
    recurrent_signature: Signature | None
    recurrent_factors: tuple[int, ...]
    recurrent_weight: Weight
    old_count: int
    divisor_cap: int
    total_weight: Weight


def blocker_signature(factor: RankThreeFactor, prime: int) -> Signature:
    route = canonical_route(factor, prime)
    return (route.profile, route.signature)


def route_blocker_ledger(
    factors: tuple[RankThreeFactor, ...],
    prime: int,
    snapshot: Hashable,
    ledger: frozenset[Token],
    factor_cap: Weight,
) -> LedgerResult:
    """Apply the OP4k growth/recurrent gate to one matching."""

    assert factors
    assert factor_cap > 0
    assert all(
        left.support_scope.isdisjoint(right.support_scope)
        for left, right in combinations(factors, 2)
    )
    assert all(
        set(left.points).isdisjoint(right.points)
        for left, right in combinations(factors, 2)
    )

    cap = divisor_cap(prime)
    buckets: dict[Signature, list[RankThreeFactor]] = defaultdict(list)
    for factor in factors:
        buckets[blocker_signature(factor, prime)].append(factor)

    for bucket in buckets.values():
        assert len(bucket) <= cap

    old_signatures = {
        signature
        for state, role, signature in ledger
        if state == snapshot and role == "rank3"
    }
    represented = frozenset(buckets)
    new_tokens = frozenset(
        (snapshot, "rank3", signature)
        for signature in represented - old_signatures
    )
    total_weight = sum(
        (factor.weight for factor in factors),
        Fraction(),
    )
    heaviest = max(
        factors,
        key=lambda factor: (factor.weight, factor.source_factor),
    )

    common = {
        "represented": represented,
        "old_count": len(old_signatures),
        "divisor_cap": cap,
        "total_weight": total_weight,
    }
    if heaviest.weight > factor_cap:
        return LedgerResult(
            status="heavy_rank_three_factor",
            tokens=ledger,
            new_tokens=frozenset(),
            recurrent_signature=None,
            recurrent_factors=(heaviest.source_factor,),
            recurrent_weight=heaviest.weight,
            **common,
        )

    if new_tokens:
        minimum_new = max(
            1,
            ceil(len(factors) / cap) - len(old_signatures),
        )
        assert len(new_tokens) >= minimum_new
        return LedgerResult(
            status="blocker_ledger_growth",
            tokens=ledger | new_tokens,
            new_tokens=new_tokens,
            recurrent_signature=None,
            recurrent_factors=(),
            recurrent_weight=Fraction(),
            **common,
        )

    assert old_signatures
    recurrent_signature, recurrent_bucket = max(
        buckets.items(),
        key=lambda item: (
            sum(
                (factor.weight for factor in item[1]),
                Fraction(),
            ),
            len(item[1]),
            repr(item[0]),
        ),
    )
    recurrent_weight = sum(
        (factor.weight for factor in recurrent_bucket),
        Fraction(),
    )
    assert recurrent_weight * len(old_signatures) >= total_weight
    assert len(recurrent_bucket) <= cap
    assert total_weight <= factor_cap * cap * len(old_signatures)
    return LedgerResult(
        status="current_recurrent_blocker_fibre",
        tokens=ledger,
        new_tokens=frozenset(),
        recurrent_signature=recurrent_signature,
        recurrent_factors=tuple(
            factor.source_factor for factor in recurrent_bucket
        ),
        recurrent_weight=recurrent_weight,
        **common,
    )


def verify_abstract_bounds(cap: int) -> int:
    """Exhaust fibre occupancies and every old-record subset."""

    cases = 0
    signatures = tuple(range(4))
    for width in range(1, len(signatures) + 1):
        active = signatures[:width]
        for occupancies in product(range(1, cap + 1), repeat=width):
            factor_count = sum(occupancies)
            assert width >= ceil(factor_count / cap)
            for old_width in range(len(signatures) + 1):
                old = set(signatures[:old_width])
                new = set(active) - old
                if new:
                    assert len(new) >= max(
                        1,
                        ceil(factor_count / cap) - len(old),
                    )
                else:
                    assert old
                    assert max(occupancies) >= ceil(
                        factor_count / len(old)
                    )
                cases += 1
    return cases


def verify_combined_descent() -> int:
    cases = 0
    for capacity in range(7):
        for potential in range(6):
            for ledger_size in range(capacity + 1):
                rank = (
                    (capacity + 1) * potential
                    + capacity
                    - ledger_size
                )
                if ledger_size < capacity:
                    growth_rank = (
                        (capacity + 1) * potential
                        + capacity
                        - (ledger_size + 1)
                    )
                    assert growth_rank < rank
                if potential > 0:
                    for reset_size in range(capacity + 1):
                        descent_rank = (
                            (capacity + 1) * (potential - 1)
                            + capacity
                            - reset_size
                        )
                        assert descent_rank < rank
                cases += 1
    return cases


def matching_by_profile(
    triples: tuple[tuple[Point, Point, Point], ...],
    prime: int,
) -> tuple[tuple[Point, Point, Point], ...]:
    buckets: dict[tuple[int, ...], list[tuple[Point, Point, Point]]] = (
        defaultdict(list)
    )
    for triple in triples:
        profile = tuple(sorted(channel(point, prime) for point in triple))
        buckets[profile].append(triple)
    return max(
        (
            greedy_point_matching(tuple(bucket))
            for bucket in buckets.values()
        ),
        key=len,
    )


def verify_real_outputs(prime: int) -> int:
    triples = all_real_factors(prime)
    matching = matching_by_profile(triples, prime)
    assert len(matching) >= 3
    factors = make_factors(matching)
    snapshot = ("phase", 0)
    empty: frozenset[Token] = frozenset()

    growth = route_blocker_ledger(
        factors,
        prime,
        snapshot,
        empty,
        Fraction(1),
    )
    assert growth.status == "blocker_ledger_growth"
    assert len(growth.new_tokens) >= ceil(
        len(factors) / growth.divisor_cap
    )

    recurrent = route_blocker_ledger(
        factors,
        prime,
        snapshot,
        growth.tokens,
        Fraction(1),
    )
    assert recurrent.status == "current_recurrent_blocker_fibre"
    assert recurrent.recurrent_signature is not None
    assert recurrent.recurrent_factors
    assert (
        recurrent.recurrent_weight * recurrent.old_count
        >= recurrent.total_weight
    )

    other_snapshot = route_blocker_ledger(
        factors,
        prime,
        ("phase", 1),
        growth.tokens,
        Fraction(1),
    )
    assert other_snapshot.status == "blocker_ledger_growth"
    assert other_snapshot.new_tokens.isdisjoint(growth.new_tokens)

    first_heavy = (Fraction(3),) + tuple(
        Fraction(1) for _ in factors[1:]
    )
    heavy = route_blocker_ledger(
        make_factors(matching, first_heavy),
        prime,
        snapshot,
        growth.tokens,
        Fraction(1),
    )
    assert heavy.status == "heavy_rank_three_factor"
    assert heavy.recurrent_weight == 3

    zero_one_weights = tuple(
        Fraction(index % 2) for index in range(len(factors))
    )
    zero_weight = route_blocker_ledger(
        make_factors(matching, zero_one_weights),
        prime,
        snapshot,
        growth.tokens,
        Fraction(1),
    )
    assert zero_weight.status == "current_recurrent_blocker_fibre"
    assert zero_weight.recurrent_weight * zero_weight.old_count >= (
        zero_weight.total_weight
    )

    same_payload = next(iter(growth.represented))
    fan_token = (snapshot, "fan", same_payload)
    rank_three_token = (snapshot, "rank3", same_payload)
    assert fan_token != rank_three_token
    assert rank_three_token in growth.tokens
    assert fan_token not in growth.tokens

    return 6


def main() -> None:
    prime = 11
    cap = divisor_cap(prime)
    abstract_cases = verify_abstract_bounds(cap)
    descent_cases = verify_combined_descent()
    outputs = verify_real_outputs(prime)
    print(
        "phase blocker ledger verified:",
        f"{abstract_cases} abstract ledger cases,",
        f"{descent_cases} combined descent states,",
        f"{outputs} real matching outputs,",
        f"divisor cap {cap}",
    )


if __name__ == "__main__":
    main()
