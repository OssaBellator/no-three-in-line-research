#!/usr/bin/env python3
"""Verify AC3i--AC3j minimal Hall cores and collision routing."""

from __future__ import annotations

from itertools import product
from math import comb, isqrt


Eligibility = tuple[frozenset[int], ...]


def neighbourhood(
    eligibility: Eligibility,
    event_mask: int,
) -> frozenset[int]:
    result: set[int] = set()
    for event, tokens in enumerate(eligibility):
        if event_mask & (1 << event):
            result.update(tokens)
    return frozenset(result)


def is_minimal_deficient(eligibility: Eligibility) -> bool:
    event_count = len(eligibility)
    full_mask = (1 << event_count) - 1
    if len(neighbourhood(eligibility, full_mask)) >= event_count:
        return False
    for mask in range(1, full_mask):
        if len(neighbourhood(eligibility, mask)) < mask.bit_count():
            return False
    return True


def balanced_pairs(total: int, bins: int) -> int:
    quotient, remainder = divmod(total, bins)
    return bins * comb(quotient, 2) + remainder * quotient


def verify_balanced_pair_bound(
    maximum_bins: int = 7,
    maximum_total: int = 16,
) -> None:
    infinity = maximum_total**3
    previous = [infinity] * (maximum_total + 1)
    previous[0] = 0
    for bin_count in range(1, maximum_bins + 1):
        current = [infinity] * (maximum_total + 1)
        for total in range(maximum_total + 1):
            current[total] = min(
                previous[total - load] + comb(load, 2)
                for load in range(total + 1)
            )
            assert current[total] == balanced_pairs(total, bin_count)
        previous = current


def labelled_statistics(
    eligibility: Eligibility,
    labels: dict[tuple[int, int], int],
) -> tuple[int, list[int], dict[tuple[int, int], int]]:
    event_count = len(eligibility)
    bin_members: dict[tuple[int, int], list[int]] = {}
    for event, tokens in enumerate(eligibility):
        for token in tokens:
            key = token, labels[event, token]
            bin_members.setdefault(key, []).append(event)

    collision_mass = sum(
        comb(len(members), 2)
        for members in bin_members.values()
    )
    loads = [0] * event_count
    pair_codegrees: dict[tuple[int, int], int] = {}
    for members in bin_members.values():
        for left_index, left in enumerate(members):
            loads[left] += len(members) - 1
            for right in members[left_index + 1 :]:
                pair = min(left, right), max(left, right)
                pair_codegrees[pair] = pair_codegrees.get(pair, 0) + 1

    assert sum(loads) == 2 * collision_mass
    assert sum(pair_codegrees.values()) == collision_mass
    return collision_mass, loads, pair_codegrees


def label_assignments(
    edges: tuple[tuple[int, int], ...],
    label_count: int,
    exhaustive: bool,
) -> tuple[tuple[int, ...], ...]:
    if exhaustive:
        return tuple(product(range(label_count), repeat=len(edges)))
    return tuple(
        tuple(
            (event + shift * token + shift) % label_count
            for event, token in edges
        )
        for shift in range(1, label_count + 2)
    )


def verify_minimal_cores(maximum_events: int = 5) -> None:
    checked = 0
    for event_count in range(2, maximum_events + 1):
        token_count = event_count - 1
        token_sets = tuple(
            frozenset(
                token
                for token in range(token_count)
                if mask & (1 << token)
            )
            for mask in range(1, 1 << token_count)
        )
        for eligibility in product(token_sets, repeat=event_count):
            if not is_minimal_deficient(eligibility):
                continue
            checked += 1
            full_mask = (1 << event_count) - 1
            full_neighbourhood = neighbourhood(eligibility, full_mask)
            assert len(full_neighbourhood) == event_count - 1
            for event in range(event_count):
                without = full_mask ^ (1 << event)
                assert neighbourhood(eligibility, without) == full_neighbourhood
            assert all(
                sum(token in tokens for tokens in eligibility) >= 2
                for token in full_neighbourhood
            )

            minimum_degree = min(map(len, eligibility))
            edge_count = sum(map(len, eligibility))
            assert minimum_degree <= event_count - 1
            edges = tuple(
                (event, token)
                for event, tokens in enumerate(eligibility)
                for token in sorted(tokens)
            )
            for label_count in range(1, 4):
                assignments = label_assignments(
                    edges,
                    label_count,
                    exhaustive=event_count <= 3,
                )
                for assignment in assignments:
                    labels = dict(zip(edges, assignment))
                    collision_mass, loads, pair_codegrees = (
                        labelled_statistics(eligibility, labels)
                    )
                    lower = balanced_pairs(
                        minimum_degree * event_count,
                        label_count * (event_count - 1),
                    )
                    assert edge_count >= minimum_degree * event_count
                    assert collision_mass >= lower
                    assert max(loads) * event_count >= 2 * lower
                    assert (
                        max(pair_codegrees.values(), default=0)
                        * comb(event_count, 2)
                        >= lower
                    )
                    if minimum_degree >= label_count:
                        coarse_numerator = (
                            minimum_degree
                            * event_count
                            * (
                                minimum_degree * event_count
                                - label_count * (event_count - 1)
                            )
                        )
                        coarse_denominator = (
                            2 * label_count * (event_count - 1)
                        )
                        assert (
                            collision_mass * coarse_denominator
                            >= coarse_numerator
                        )
                    if minimum_degree >= 2 * label_count:
                        assert max(loads) > minimum_degree
    assert checked


def verify_router(
    maximum_tokens: int = 5,
    maximum_other_uses: int = 4,
) -> None:
    for label_count in range(1, 4):
        for token_count in range(1, maximum_tokens + 1):
            for labels in product(range(label_count), repeat=token_count):
                for contributions in product(
                    range(maximum_other_uses + 1),
                    repeat=token_count,
                ):
                    collision_load = sum(contributions)
                    if not collision_load:
                        continue
                    for threshold in range(1, maximum_other_uses + 1):
                        if max(contributions) > threshold:
                            continue
                        colliding_by_label = [
                            sum(
                                contribution > 0 and label == selected
                                for contribution, label in zip(
                                    contributions,
                                    labels,
                                )
                            )
                            for selected in range(label_count)
                        ]
                        assert (
                            max(colliding_by_label)
                            * threshold
                            * label_count
                            >= collision_load
                        )

                    square_root = isqrt(collision_load // label_count)
                    if square_root == 0:
                        continue
                    if max(contributions) > square_root:
                        continue
                    colliding_by_label = [
                        sum(
                            contribution > 0 and label == selected
                            for contribution, label in zip(
                                contributions,
                                labels,
                            )
                        )
                        for selected in range(label_count)
                    ]
                    assert max(colliding_by_label) >= square_root


def main() -> None:
    verify_balanced_pair_bound()
    verify_minimal_cores()
    verify_router()
    print("AC minimal Hall deficiency and collision routing: verified")


if __name__ == "__main__":
    main()
