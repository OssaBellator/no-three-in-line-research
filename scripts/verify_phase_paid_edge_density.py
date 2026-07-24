#!/usr/bin/env python3
"""Verify OP4i paid quotient-edge density and repetition alternatives."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import cache

try:
    from scripts.verify_phase_geometric_labels import (
        OrientedSecantRecord,
        QuotientTransition,
        determinant,
        inverse,
        logarithm_table,
        oriented_secant_record,
        product_carry,
        quotient_transition,
    )
    from scripts.verify_phase_implication_bridge import (
        extract_implication_bicycle,
    )
    from scripts.verify_phase_signature_recurrence import solve_2sat
except ModuleNotFoundError:
    from verify_phase_geometric_labels import (  # type: ignore[no-redef]
        OrientedSecantRecord,
        QuotientTransition,
        determinant,
        inverse,
        logarithm_table,
        oriented_secant_record,
        product_carry,
        quotient_transition,
    )
    from verify_phase_implication_bridge import (  # type: ignore[no-redef]
        extract_implication_bicycle,
    )
    from verify_phase_signature_recurrence import (  # type: ignore[no-redef]
        solve_2sat,
    )


Point = tuple[int, int]
Factor = tuple[Point, Point, Point]
Weight = Fraction


@dataclass(frozen=True)
class PaidOccurrence:
    source_factor: int
    factor: Factor
    weight: Weight
    record: OrientedSecantRecord
    quotient: QuotientTransition


def divisor_count(value: int) -> int:
    assert value >= 1
    count = 0
    divisor = 1
    while divisor * divisor <= value:
        if value % divisor == 0:
            count += 1 if divisor * divisor == value else 2
        divisor += 1
    return count


@cache
def divisor_cap(prime: int) -> int:
    return max(
        divisor_count(value)
        for value in range(1, prime**2)
    )


def quotient_edge_key(
    transition: QuotientTransition,
    order: int,
) -> tuple[int, int, int, int]:
    left = transition.left % order
    right = transition.right % order
    return (
        transition.root % order,
        min(left, right),
        max(left, right),
        transition.colour % order,
    )


def channel_pair(
    occurrence: PaidOccurrence,
) -> tuple[int, int]:
    return (
        occurrence.record.endpoint_channel,
        occurrence.record.anchor_channel,
    )


def rational_orbit_key(
    occurrence: PaidOccurrence,
) -> tuple[int, int, int, int]:
    record = occurrence.record
    return (
        record.root,
        min(record.parameter, record.collision_partner),
        max(record.parameter, record.collision_partner),
        record.transition,
    )


def carry_signature(
    occurrence: PaidOccurrence,
) -> tuple[int, int]:
    prime = occurrence.record.prime
    left = product_carry(occurrence.record.endpoint, prime)[1]
    right = product_carry(occurrence.record.partner, prime)[1]
    return min(left, right), max(left, right)


def group_weight(
    occurrences: tuple[PaidOccurrence, ...],
) -> Weight:
    return sum(
        (occurrence.weight for occurrence in occurrences),
        Fraction(),
    )


def grouped(
    occurrences: tuple[PaidOccurrence, ...],
    key,
) -> dict[object, tuple[PaidOccurrence, ...]]:
    buckets: dict[object, list[PaidOccurrence]] = defaultdict(list)
    for occurrence in occurrences:
        buckets[key(occurrence)].append(occurrence)
    return {
        item: tuple(bucket)
        for item, bucket in buckets.items()
    }


def heaviest(
    groups: dict[object, tuple[PaidOccurrence, ...]],
) -> tuple[object, tuple[PaidOccurrence, ...], Weight]:
    assert groups
    key, occurrences = max(
        groups.items(),
        key=lambda item: (
            group_weight(item[1]),
            repr(item[0]),
        ),
    )
    return key, occurrences, group_weight(occurrences)


def rational_orbit_witnesses(
    occurrences: tuple[PaidOccurrence, ...],
    quotient_order: int,
    logs: dict[int, int],
) -> dict[str, object]:
    by_orbit = grouped(occurrences, rational_orbit_key)
    representatives = tuple(bucket[0] for bucket in by_orbit.values())
    first_key = quotient_edge_key(
        representatives[0].quotient,
        quotient_order,
    )
    _, left_coset, right_coset, target_coset = first_key
    witnessed_left: set[int] = set()
    witnessed_right: set[int] = set()
    witnessed_source: set[int] = set()
    target_values: set[int] = set()
    complete_left: set[int] = set()
    complete_right: set[int] = set()
    complete_source: set[int] = set()
    complete_targets: set[int] = set()
    complete_fixed_points = 0
    missing_companions: list[
        tuple[tuple[int, int, int, int], tuple[int, ...]]
    ] = []

    for orbit_key, bucket in by_orbit.items():
        occurrence = bucket[0]
        record = occurrence.record
        roots = {record.parameter, record.collision_partner}
        witnessed = {
            item.record.parameter
            for item in bucket
        }
        assert witnessed <= roots
        parameter_coset = logs[record.parameter] % quotient_order
        partner_coset = (
            logs[record.collision_partner] % quotient_order
        )
        assert {
            parameter_coset,
            partner_coset,
        } == {left_coset, right_coset}
        assert logs[record.transition] % quotient_order == target_coset
        target_values.add(record.transition)

        if left_coset != right_coset:
            for value in witnessed:
                if logs[value] % quotient_order == left_coset:
                    witnessed_left.add(value)
                else:
                    assert logs[value] % quotient_order == right_coset
                    witnessed_right.add(value)
        else:
            witnessed_source.update(witnessed)

        missing = roots - witnessed
        if missing:
            missing_companions.append(
                (orbit_key, tuple(sorted(missing)))
            )
            continue

        complete_targets.add(record.transition)
        if left_coset != right_coset:
            for value in roots:
                if logs[value] % quotient_order == left_coset:
                    complete_left.add(value)
                else:
                    complete_right.add(value)
        else:
            complete_source.update(roots)
            if len(roots) == 1:
                complete_fixed_points += 1

    orbit_count = len(representatives)
    assert len(target_values) == orbit_count
    complete_orbit_count = orbit_count - len(missing_companions)
    assert len(complete_targets) == complete_orbit_count
    if left_coset != right_coset:
        assert len(complete_left) == complete_orbit_count
        assert len(complete_right) == complete_orbit_count
        return {
            "loop": False,
            "orbit_count": orbit_count,
            "complete_orbit_count": complete_orbit_count,
            "witnessed_left_source": frozenset(witnessed_left),
            "witnessed_right_source": frozenset(witnessed_right),
            "complete_left_source": frozenset(complete_left),
            "complete_right_source": frozenset(complete_right),
            "target": frozenset(target_values),
            "complete_target": frozenset(complete_targets),
            "missing_companions": tuple(missing_companions),
        }

    assert complete_fixed_points <= 2
    assert (
        len(complete_source)
        == 2 * complete_orbit_count - complete_fixed_points
    )
    return {
        "loop": True,
        "orbit_count": orbit_count,
        "complete_orbit_count": complete_orbit_count,
        "witnessed_source": frozenset(witnessed_source),
        "complete_source": frozenset(complete_source),
        "target": frozenset(target_values),
        "complete_target": frozenset(complete_targets),
        "complete_fixed_points": complete_fixed_points,
        "missing_companions": tuple(missing_companions),
    }


def audit_paid_quotient_edge(
    occurrences: tuple[PaidOccurrence, ...],
    quotient_order: int,
    density_target: int,
    factor_cap: Weight,
    logs: dict[int, int],
) -> dict[str, object]:
    """Route paid edge weight to density, reuse, or carry growth."""

    assert occurrences
    assert quotient_order >= 1
    assert density_target >= 2
    assert factor_cap > 0
    assert all(occurrence.weight > 0 for occurrence in occurrences)
    prime = occurrences[0].record.prime
    assert all(
        occurrence.record.prime == prime
        for occurrence in occurrences
    )

    edge_keys = tuple(
        quotient_edge_key(occurrence.quotient, quotient_order)
        for occurrence in occurrences
    )
    if len(set(edge_keys)) != 1:
        first = edge_keys[0]
        mismatch = next(
            index
            for index, key in enumerate(edge_keys)
            if key != first
        )
        return {
            "status": "mixed_quotient_edge",
            "edge_index": mismatch,
            "expected": first,
            "actual": edge_keys[mismatch],
        }

    total_weight = group_weight(occurrences)
    channel_groups = grouped(occurrences, channel_pair)
    (
        selected_channel_pair,
        channel_occurrences,
        channel_weight,
    ) = heaviest(channel_groups)
    channel_count = len(channel_groups)
    assert channel_weight * channel_count >= total_weight

    orbit_groups = grouped(channel_occurrences, rational_orbit_key)
    orbit_count = len(orbit_groups)
    common = {
        "total_weight": total_weight,
        "channel_pair_count": channel_count,
        "selected_channel_pair": selected_channel_pair,
        "selected_channel_weight": channel_weight,
        "orbit_count": orbit_count,
        "quotient_edge": edge_keys[0],
    }

    if orbit_count >= density_target:
        witness_audit = rational_orbit_witnesses(
            channel_occurrences,
            quotient_order,
            logs,
        )
        subgroup_order = (prime - 1) // quotient_order
        assert subgroup_order * quotient_order == prime - 1
        status = (
            "dense_rational_edge"
            if witness_audit["complete_orbit_count"] >= density_target
            else "one_sided_orbit_growth"
        )
        return {
            "status": status,
            **common,
            "subgroup_order": subgroup_order,
            "density_target": density_target,
            "witness_audit": witness_audit,
        }

    (
        selected_orbit,
        orbit_occurrences,
        orbit_weight,
    ) = heaviest(orbit_groups)
    assert orbit_weight * orbit_count >= channel_weight
    parameter_groups = grouped(
        orbit_occurrences,
        lambda occurrence: occurrence.record.parameter,
    )
    assert len(parameter_groups) <= 2
    (
        selected_parameter,
        parameter_occurrences,
        parameter_weight,
    ) = heaviest(parameter_groups)
    assert (
        parameter_weight * len(parameter_groups)
        >= orbit_weight
    )

    factor_groups = grouped(
        parameter_occurrences,
        lambda occurrence: occurrence.source_factor,
    )
    factor_weights = {
        factor: group_weight(bucket)
        for factor, bucket in factor_groups.items()
    }
    selected_factor, selected_factor_weight = max(
        factor_weights.items(),
        key=lambda item: (item[1], item[0]),
    )
    sparse_common = {
        **common,
        "selected_orbit": selected_orbit,
        "selected_orbit_weight": orbit_weight,
        "parameter_branch_count": len(parameter_groups),
        "selected_parameter": selected_parameter,
        "selected_parameter_weight": parameter_weight,
        "distinct_factor_count": len(factor_groups),
    }
    if selected_factor_weight > factor_cap:
        return {
            "status": "heavy_source_factor",
            **sparse_common,
            "source_factor": selected_factor,
            "source_factor_weight": selected_factor_weight,
            "factor_cap": factor_cap,
        }

    carry_groups: dict[
        tuple[int, int],
        list[tuple[int, Weight, PaidOccurrence]],
    ] = defaultdict(list)
    for factor, bucket in factor_groups.items():
        factors = {occurrence.factor for occurrence in bucket}
        assert len(factors) == 1
        records = {
            (
                occurrence.record.endpoint,
                occurrence.record.partner,
                occurrence.record.anchor,
            )
            for occurrence in bucket
        }
        assert len(records) == 1
        carry_groups[carry_signature(bucket[0])].append(
            (factor, factor_weights[factor], bucket[0])
        )

    cap = divisor_cap(prime)
    carry_loads: dict[tuple[int, int], Weight] = {}
    carry_factor_counts: dict[tuple[int, int], int] = {}
    for signature, entries in carry_groups.items():
        endpoint_points = {
            entry[2].record.endpoint
            for entry in entries
        }
        assert len(endpoint_points) == len(entries)
        assert len(entries) <= 2 * cap
        load = sum((entry[1] for entry in entries), Fraction())
        assert load <= 2 * cap * factor_cap
        carry_loads[signature] = load
        carry_factor_counts[signature] = len(entries)

    signature_count = len(carry_groups)
    assert (
        signature_count * 2 * cap * factor_cap
        >= parameter_weight
    )
    return {
        "status": "product_carry_growth",
        **sparse_common,
        "factor_cap": factor_cap,
        "divisor_cap": cap,
        "signature_count": signature_count,
        "signature_loads": carry_loads,
        "signature_factor_counts": carry_factor_counts,
    }


def standard_point(prime: int, channel_value: int, x: int) -> Point:
    return x, channel_value * inverse(x, prime) % prime


def enumerate_real_occurrences(
    prime: int,
    quotient_order: int,
) -> tuple[PaidOccurrence, ...]:
    logs = logarithm_table(prime)
    factor_ids: dict[Factor, int] = {}
    occurrences: list[PaidOccurrence] = []
    seen: set[tuple[int, int, int, int]] = set()

    for endpoint_channel in range(1, prime):
        for anchor_channel in range(1, prime):
            if endpoint_channel == anchor_channel:
                continue
            root = (
                anchor_channel
                * inverse(endpoint_channel, prime)
                % prime
            )
            for x in range(1, prime):
                for z in range(1, prime):
                    denominator = (root * x - z) % prime
                    if denominator == 0:
                        continue
                    u = (
                        z
                        * (x - z)
                        * inverse(denominator, prime)
                        % prime
                    )
                    if u in (0, x):
                        continue
                    endpoint = standard_point(
                        prime,
                        endpoint_channel,
                        x,
                    )
                    partner = standard_point(
                        prime,
                        endpoint_channel,
                        u,
                    )
                    anchor = standard_point(
                        prime,
                        anchor_channel,
                        z,
                    )
                    if determinant(anchor, endpoint, partner) != 0:
                        continue
                    factor = tuple(sorted((endpoint, partner, anchor)))
                    factor_id = factor_ids.setdefault(
                        factor,
                        len(factor_ids),
                    )
                    record = oriented_secant_record(
                        prime,
                        endpoint,
                        partner,
                        anchor,
                    )
                    occurrence_key = (
                        factor_id,
                        record.parameter,
                        record.transition,
                        record.endpoint_channel,
                    )
                    if occurrence_key in seen:
                        continue
                    seen.add(occurrence_key)
                    quotient = quotient_transition(
                        factor_id,
                        0,
                        record,
                        quotient_order,
                        logs,
                    )
                    occurrences.append(
                        PaidOccurrence(
                            source_factor=factor_id,
                            factor=factor,
                            weight=Fraction(1),
                            record=record,
                            quotient=quotient,
                        )
                    )
    return tuple(occurrences)


def with_weight(
    occurrence: PaidOccurrence,
    weight: int | Fraction,
) -> PaidOccurrence:
    return PaidOccurrence(
        source_factor=occurrence.source_factor,
        factor=occurrence.factor,
        weight=Fraction(weight),
        record=occurrence.record,
        quotient=occurrence.quotient,
    )


def verify_unpaid_core_boundary() -> int:
    """A tiny contradiction need not carry the protected-bank weight."""

    core = (
        ((0, 1), (1, 1)),
        ((0, 1), (1, 0)),
        ((0, 0), (1, 1)),
        ((0, 0), (1, 0)),
    )
    checked = 0
    for variable_count in range(3, 9):
        extras = tuple(
            ((variable, 1),)
            for variable in range(2, variable_count)
        )
        clauses = core + extras
        result = solve_2sat(variable_count, clauses)
        assert not result["satisfiable"]
        bicycle = extract_implication_bicycle(result, clauses)
        used_variables = {
            node // 2
            for node in bicycle.walk_nodes[:-1]
        }
        assert used_variables <= {0, 1}
        weights = (
            Fraction(1),
            Fraction(1),
        ) + tuple(
            Fraction(10**variable)
            for variable in range(2, variable_count)
        )
        bicycle_weight = sum(
            weights[variable]
            for variable in used_variables
        )
        total_weight = sum(weights, Fraction())
        assert bicycle_weight == 2
        assert total_weight / bicycle_weight >= 50
        checked += 1
    return checked


def verify_capacity_bound(
    occurrences: tuple[PaidOccurrence, ...],
) -> int:
    prime = occurrences[0].record.prime
    cap = divisor_cap(prime)
    buckets: dict[
        tuple[object, ...],
        set[int],
    ] = defaultdict(set)
    representatives: dict[
        tuple[object, ...],
        PaidOccurrence,
    ] = {}
    for occurrence in occurrences:
        key = (
            channel_pair(occurrence),
            rational_orbit_key(occurrence),
            occurrence.record.parameter,
            carry_signature(occurrence),
        )
        buckets[key].add(occurrence.source_factor)
        representatives.setdefault(key, occurrence)

    for key, factors in buckets.items():
        assert len(factors) <= 2 * cap
        occurrence = representatives[key]
        endpoint_carry = product_carry(
            occurrence.record.endpoint,
            prime,
        )[1]
        assert endpoint_carry in key[-1]
    return len(buckets)


def verify_paid_outputs(
    occurrences: tuple[PaidOccurrence, ...],
    quotient_order: int,
) -> int:
    logs = logarithm_table(occurrences[0].record.prime)
    by_edge_channel = grouped(
        occurrences,
        lambda occurrence: (
            quotient_edge_key(occurrence.quotient, quotient_order),
            channel_pair(occurrence),
        ),
    )
    dense_bucket = next(
        bucket
        for bucket in by_edge_channel.values()
        if sum(
            {
                item.record.parameter
                for item in orbit_bucket
            }
            >= {
                orbit_bucket[0].record.parameter,
                orbit_bucket[0].record.collision_partner,
            }
            for orbit_bucket in grouped(
                bucket,
                rational_orbit_key,
            ).values()
        )
        >= 3
    )
    dense_orbits = grouped(dense_bucket, rational_orbit_key)
    complete_orbits = tuple(
        bucket
        for bucket in dense_orbits.values()
        if {
            item.record.parameter
            for item in bucket
        }
        >= {
            bucket[0].record.parameter,
            bucket[0].record.collision_partner,
        }
    )
    assert len(complete_orbits) >= 3
    dense_sample_list: list[PaidOccurrence] = []
    one_sided_sample: list[PaidOccurrence] = []
    for bucket in complete_orbits[:3]:
        by_parameter = {
            item.record.parameter: item
            for item in bucket
        }
        roots = {
            bucket[0].record.parameter,
            bucket[0].record.collision_partner,
        }
        dense_sample_list.extend(by_parameter[root] for root in roots)
        one_sided_sample.append(bucket[0])
    dense_sample = tuple(dense_sample_list)
    dense = audit_paid_quotient_edge(
        dense_sample,
        quotient_order,
        3,
        Fraction(1),
        logs,
    )
    assert dense["status"] == "dense_rational_edge"
    assert len(dense["witness_audit"]["complete_target"]) == 3

    one_sided = audit_paid_quotient_edge(
        tuple(one_sided_sample),
        quotient_order,
        3,
        Fraction(1),
        logs,
    )
    assert one_sided["status"] == "one_sided_orbit_growth"
    assert one_sided["witness_audit"]["complete_orbit_count"] < 3

    by_template = grouped(
        occurrences,
        lambda occurrence: (
            quotient_edge_key(occurrence.quotient, quotient_order),
            channel_pair(occurrence),
            rational_orbit_key(occurrence),
            occurrence.record.parameter,
        ),
    )
    carry_bucket = max(
        by_template.values(),
        key=lambda bucket: len(
            {occurrence.source_factor for occurrence in bucket}
        ),
    )
    unique_factors: dict[int, PaidOccurrence] = {}
    for occurrence in carry_bucket:
        unique_factors.setdefault(
            occurrence.source_factor,
            occurrence,
        )
    assert len(unique_factors) >= 4
    carry_sample = tuple(unique_factors.values())
    carry = audit_paid_quotient_edge(
        carry_sample,
        quotient_order,
        2,
        Fraction(1),
        logs,
    )
    assert carry["status"] == "product_carry_growth"

    heavy_occurrence = with_weight(carry_sample[0], 5)
    heavy = audit_paid_quotient_edge(
        (heavy_occurrence,),
        quotient_order,
        2,
        Fraction(1),
        logs,
    )
    assert heavy["status"] == "heavy_source_factor"
    assert heavy["source_factor_weight"] == 5

    by_edge = grouped(
        occurrences,
        lambda occurrence: quotient_edge_key(
            occurrence.quotient,
            quotient_order,
        ),
    )
    multi_channel_bucket = next(
        bucket
        for bucket in by_edge.values()
        if len(grouped(bucket, channel_pair)) >= 2
    )
    channel_buckets = list(
        grouped(multi_channel_bucket, channel_pair).values()
    )
    first = with_weight(channel_buckets[0][0], 3)
    second = with_weight(channel_buckets[1][0], 1)
    localized = audit_paid_quotient_edge(
        (first, second),
        quotient_order,
        2,
        Fraction(10),
        logs,
    )
    assert localized["selected_channel_weight"] == 3
    assert localized["channel_pair_count"] == 2

    edge_keys = list(by_edge)
    assert len(edge_keys) >= 2
    mixed = audit_paid_quotient_edge(
        (
            by_edge[edge_keys[0]][0],
            by_edge[edge_keys[1]][0],
        ),
        quotient_order,
        2,
        Fraction(1),
        logs,
    )
    assert mixed["status"] == "mixed_quotient_edge"

    loop_bucket = next(
        bucket
        for (edge, _), bucket in by_edge_channel.items()
        if edge[1] == edge[2]
        and sum(
            {
                item.record.parameter
                for item in orbit_bucket
            }
            >= {
                orbit_bucket[0].record.parameter,
                orbit_bucket[0].record.collision_partner,
            }
            for orbit_bucket in grouped(
                bucket,
                rational_orbit_key,
            ).values()
        )
        >= 2
    )
    loop_orbits = grouped(loop_bucket, rational_orbit_key)
    loop_complete = tuple(
        bucket
        for bucket in loop_orbits.values()
        if {
            item.record.parameter
            for item in bucket
        }
        >= {
            bucket[0].record.parameter,
            bucket[0].record.collision_partner,
        }
    )
    loop_sample_list: list[PaidOccurrence] = []
    for bucket in loop_complete[:2]:
        by_parameter = {
            item.record.parameter: item
            for item in bucket
        }
        roots = {
            bucket[0].record.parameter,
            bucket[0].record.collision_partner,
        }
        loop_sample_list.extend(by_parameter[root] for root in roots)
    loop_sample = tuple(loop_sample_list)
    loop = audit_paid_quotient_edge(
        loop_sample,
        quotient_order,
        2,
        Fraction(1),
        logs,
    )
    assert loop["status"] == "dense_rational_edge"
    assert loop["witness_audit"]["loop"]
    assert len(loop["witness_audit"]["complete_target"]) == 2
    return 7


def main() -> None:
    prime = 11
    quotient_order = 2
    occurrences = enumerate_real_occurrences(prime, quotient_order)
    assert occurrences
    unpaid_examples = verify_unpaid_core_boundary()
    capacity_classes = verify_capacity_bound(occurrences)
    paid_outputs = verify_paid_outputs(occurrences, quotient_order)
    print(
        "phase paid edge density verified:",
        f"{len(occurrences)} real oriented factors,",
        f"{capacity_classes} carry-capacity classes,",
        f"{unpaid_examples} unpaid-core examples,",
        f"{paid_outputs} routed paid outputs",
    )


if __name__ == "__main__":
    main()
