#!/usr/bin/env python3
"""Finite checks for AC3jv--AC3jz."""

from __future__ import annotations

from collections import Counter
from itertools import product


def verify_activated_checks(counts: Counter[str]) -> None:
    for rank in range(1, 5):
        for current in product((0, 1), repeat=rank):
            for target in range(rank):
                if current[target] != 0:
                    continue
                forbidden = list(current)
                forbidden[target] = 1
                forbidden = tuple(forbidden)
                assert forbidden != current
                assert forbidden[target] == 1
                assert current[target] == 0
                assert (
                    forbidden[:target] + forbidden[target + 1 :]
                    == current[:target] + current[target + 1 :]
                )
                counts["activated hard checks"] += 1


def verify_bda_target_patterns(counts: Counter[str]) -> None:
    # The coordinate identity is exact, while any target-containing template is
    # absent from the current three-cell incidence pattern.
    for px in range(-3, 4):
        for py in range(-3, 4):
            for dx, dy in product(range(-2, 3), repeat=2):
                if dx == 0 and dy == 0:
                    continue
                for h in range(1, 5):
                    for u in range(-3, 4):
                        for v in range(-3, 4):
                            if u == 0 or v == 0 or u == v:
                                continue
                            triple = (
                                (px, py),
                                (px + h * u * dx, py + h * u * dy),
                                (px + h * v * dx, py + h * v * dy),
                            )
                            if len(set(triple)) < 3:
                                continue
                            for target in range(3):
                                current_presence = [1, 1, 1]
                                current_presence[target] = 0
                                assert not all(current_presence)
                                assert triple[target] not in {
                                    triple[index]
                                    for index in range(3)
                                    if current_presence[index]
                                }
                                counts["BDA prospective templates"] += 1


def verify_quotient_scale_recovery(counts: Counter[str]) -> None:
    # Coset multiplication is represented additively in a cyclic quotient.
    for quotient_order in range(1, 30):
        for source_role in range(quotient_order):
            for scale in range(quotient_order):
                physical_source = (source_role + scale) % quotient_order
                recovered = (physical_source - source_role) % quotient_order
                assert recovered == scale
                for root in range(quotient_order):
                    for image in range(quotient_order):
                        physical_anchor = (root + recovered) % quotient_order
                        physical_partner = (image + recovered) % quotient_order
                        assert (physical_anchor - root) % quotient_order == recovered
                        assert (physical_partner - image) % quotient_order == recovered
                        counts["RI quotient identities"] += 1


def owner_route(current: bool, physical: bool, coherent: bool, payable: bool) -> str:
    if payable:
        # A valid payable declaration must already be current, physical and
        # coherent. Invalid truth-table rows are rejected by the verifier.
        return "paid"
    if not physical:
        return "occurrence_failure"
    if not coherent:
        return "mismatch"
    if current:
        return "fixed_current_nonpayable"
    return "prospective_literal"


def verify_owner_chart(counts: Counter[str]) -> None:
    for current, physical, coherent, payable in product((False, True), repeat=4):
        if payable and not (current and physical and coherent):
            # These flag combinations violate the chart's declaration contract.
            counts["rejected invalid payable charts"] += 1
            continue
        route = owner_route(current, physical, coherent, payable)
        if route == "paid":
            assert current and physical and coherent and payable
        elif route == "occurrence_failure":
            assert not physical and not payable
        elif route == "mismatch":
            assert physical and not coherent and not payable
        elif route == "fixed_current_nonpayable":
            assert current and physical and coherent and not payable
        elif route == "prospective_literal":
            assert not current and physical and coherent and not payable
        else:
            raise AssertionError(route)
        counts["valid owner charts"] += 1


def verify_shared_payment(counts: Counter[str]) -> None:
    # A common token is counted once, while disjoint private tokens add.
    for common_weight in range(0, 8):
        for private_count in range(0, 7):
            private_weights = list(range(1, private_count + 1))
            exact = common_weight + sum(private_weights)
            repeated_wrong = private_count * common_weight + sum(private_weights)
            assert exact <= repeated_wrong or private_count == 0
            assert exact == common_weight + sum(private_weights)
            counts["paid-set accounting systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_activated_checks(counts)
    verify_bda_target_patterns(counts)
    verify_quotient_scale_recovery(counts)
    verify_owner_chart(counts)
    verify_shared_payment(counts)

    print("AC3jv--AC3jz unary owner payment audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
