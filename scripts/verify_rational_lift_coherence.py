#!/usr/bin/env python3
"""Verify RI5d--RI5e physical lift coherence and its obstruction."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import ceil


Point = tuple[int, int]


def inverse(value: int, prime: int) -> int:
    assert value % prime
    return pow(value, prime - 2, prime)


def rational_map(value: int, root: int, prime: int) -> int:
    assert value % prime not in (0, root % prime)
    return (
        value
        * (1 - value)
        * inverse(root - value, prime)
    ) % prime


def collision_partner(value: int, root: int, prime: int) -> int:
    return (
        root
        * (value - 1)
        * inverse(value - root, prime)
    ) % prime


def point(channel: int, column: int, prime: int) -> Point:
    return column, channel * inverse(column, prime) % prime


def determinant(left: Point, middle: Point, right: Point) -> int:
    return (
        (middle[0] - left[0]) * (right[1] - left[1])
        - (right[0] - left[0]) * (middle[1] - left[1])
    )


def subgroup(prime: int, order: int) -> frozenset[int]:
    assert (prime - 1) % order == 0
    return frozenset(
        pow(value, (prime - 1) // order, prime)
        for value in range(1, prime)
    )


def coset(value: int, group: frozenset[int], prime: int) -> frozenset[int]:
    return frozenset(value * item % prime for item in group)


def verify_arbitrary_scales() -> tuple[int, int]:
    factor_count = 0
    quotient_count = 0
    for prime in (7, 11, 13, 17):
        for endpoint_channel in range(1, prime):
            for anchor_channel in range(1, prime):
                if endpoint_channel == anchor_channel:
                    continue
                root = (
                    anchor_channel
                    * inverse(endpoint_channel, prime)
                    % prime
                )
                for parameter in range(1, prime):
                    if parameter in (1, root):
                        continue
                    transition = rational_map(parameter, root, prime)
                    if transition == 1:
                        continue
                    for scale in range(1, prime):
                        endpoint = scale
                        partner = transition * scale % prime
                        anchor = parameter * scale % prime
                        triple = (
                            point(endpoint_channel, endpoint, prime),
                            point(endpoint_channel, partner, prime),
                            point(anchor_channel, anchor, prime),
                        )
                        assert determinant(*triple) % prime == 0
                        assert anchor * inverse(endpoint, prime) % prime == parameter
                        assert partner * inverse(endpoint, prime) % prime == transition
                        factor_count += 1

                        for order in (
                            divisor
                            for divisor in range(1, prime)
                            if (prime - 1) % divisor == 0
                        ):
                            group = subgroup(prime, order)
                            scale_coset = coset(scale, group, prime)
                            assert coset(endpoint, group, prime) == scale_coset
                            assert coset(partner, group, prime) == coset(
                                transition * scale % prime,
                                group,
                                prime,
                            )
                            assert coset(anchor, group, prime) == coset(
                                parameter * scale % prime,
                                group,
                                prime,
                            )
                            quotient_count += 1
    return factor_count, quotient_count


def verify_coset_products() -> int:
    checked = 0
    for prime in (7, 11, 13, 17, 19):
        for order in range(1, prime):
            if (prime - 1) % order:
                continue
            group = subgroup(prime, order)
            for root in range(2, prime):
                for parameter in range(1, prime):
                    if parameter in (1, root):
                        continue
                    transition = rational_map(parameter, root, prime)
                    if transition == 1:
                        continue
                    for scale in range(1, prime):
                        endpoint = scale
                        partner = transition * scale % prime
                        anchor = parameter * scale % prime
                        scale_class = coset(scale, group, prime)
                        assert coset(endpoint, group, prime) == scale_class
                        assert coset(partner, group, prime) == {
                            left * right % prime
                            for left in coset(transition, group, prime)
                            for right in scale_class
                        }
                        assert coset(anchor, group, prime) == {
                            left * right % prime
                            for left in coset(parameter, group, prime)
                            for right in scale_class
                        }
                        checked += 1
    return checked


def verify_anchor_collapse() -> int:
    checked = 0
    for prime in (7, 11, 13, 17, 19):
        for root in range(2, prime):
            parameters = tuple(
                value
                for value in range(1, prime)
                if value not in (1, root)
                and rational_map(value, root, prime) != 1
            )
            for anchor in range(1, prime):
                lifted = {
                    parameter
                    * (anchor * inverse(parameter, prime) % prime)
                    % prime
                    for parameter in parameters
                }
                assert lifted == {anchor}
                checked += len(parameters)
    return checked


def scale_audit(fibres, group, prime, weights=None):
    if weights is None:
        weights = (1,) * len(fibres)
    assert len(weights) == len(fibres)
    selected_scales = []
    selected_weights = []
    split = []
    for roots, weight in zip(fibres, weights):
        root_scale_sets = []
        for occurrences in roots.values():
            root_scale_sets.append({
                coset(item["x"], group, prime)
                for item in occurrences
            })
        common = set.intersection(*root_scale_sets)
        if not common:
            split.append(tuple(root_scale_sets))
            continue
        selected_scales.append(min(common, key=lambda item: tuple(sorted(item))))
        selected_weights.append(weight)
    counts = Counter(selected_scales)
    weight_by_scale = Counter()
    for scale, weight in zip(selected_scales, selected_weights):
        weight_by_scale[scale] += weight
    heaviest = max(counts.values(), default=0)
    if counts:
        assert heaviest >= ceil(len(selected_scales) / len(counts))
        assert (
            max(weight_by_scale.values()) * len(counts)
            >= sum(selected_weights)
        )
    return split, counts, weight_by_scale


def verify_real_fixed_edge_witness() -> tuple[int, int, int]:
    prime = 11
    endpoint_channel = 1
    anchor_channel = 5
    root = 5
    group = subgroup(prime, 5)

    # Three complete F_5 fibres on one quotient edge.  Every tuple is
    # (parameter c, base x, partner u, anchor z).
    records = (
        (4, 1, 10, 4),
        (7, 1, 10, 7),
        (6, 2, 5, 1),
        (3, 2, 5, 6),
        (9, 5, 2, 1),
        (10, 5, 2, 6),
    )
    by_fibre = defaultdict(lambda: defaultdict(list))
    anchor_load = Counter()
    quotient_edges = set()
    for parameter, endpoint, partner, anchor in records:
        transition = rational_map(parameter, root, prime)
        assert transition == partner * inverse(endpoint, prime) % prime
        assert parameter == anchor * inverse(endpoint, prime) % prime
        mate = collision_partner(parameter, root, prime)
        fibre = tuple(sorted((parameter, mate)))
        triple = (
            point(endpoint_channel, endpoint, prime),
            point(endpoint_channel, partner, prime),
            point(anchor_channel, anchor, prime),
        )
        assert determinant(*triple) == 0
        root_pair = frozenset((
            coset(parameter, group, prime),
            coset(collision_partner(parameter, root, prime), group, prime),
        ))
        quotient_edges.add((
            coset(root, group, prime),
            root_pair,
            coset(transition, group, prime),
        ))
        by_fibre[fibre][parameter].append({
            "x": endpoint,
            "z": anchor,
            "u": partner,
        })
        anchor_load[anchor] += 1

    assert set(by_fibre) == {(4, 7), (3, 6), (9, 10)}
    assert len(quotient_edges) == 1
    assert all(set(roots) == set(fibre)
               for fibre, roots in by_fibre.items())
    split, scales, scale_weights = scale_audit(
        tuple(by_fibre.values()),
        group,
        prime,
        (1, 2, 4),
    )
    assert not split
    assert len(scales) == 2
    assert max(scales.values()) == 2
    assert max(scale_weights.values()) == 5
    assert len(anchor_load) == 4 < len(records)
    assert max(anchor_load.values()) == 2

    # Force an exact split-lift certificate for one otherwise complete
    # fibre by moving one companion to the other scale coset.
    synthetic = ({
        4: ({"x": 1},),
        7: ({"x": 2},),
    },)
    split, _, _ = scale_audit(synthetic, group, prime)
    assert len(split) == 1
    return len(by_fibre), len(scales), len(anchor_load)


def main() -> None:
    factor_count, quotient_count = verify_arbitrary_scales()
    coset_count = verify_coset_products()
    collapse_count = verify_anchor_collapse()
    fibres, scales, anchors = verify_real_fixed_edge_witness()
    print(
        "rational lift coherence verified:",
        f"{factor_count} arbitrary-scale factors,",
        f"{quotient_count + coset_count} quotient lifts,",
        f"{collapse_count} collapsed anchors,",
        f"{fibres} real complete fibres on {scales} scales and {anchors} anchors",
    )


if __name__ == "__main__":
    main()
