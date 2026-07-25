#!/usr/bin/env python3
"""Exhaust AC3bc--AC3be weighted root-scale pairing checks."""

from fractions import Fraction
from itertools import product


def verify_pairing_identity(maximum_atoms=6):
    identity_checks = 0
    coherent_checks = 0
    imbalance_checks = 0

    values = list(product(range(3), repeat=2))
    for atom_count in range(1, maximum_atoms + 1):
        for table in product(values, repeat=atom_count):
            total = sum(left + right for left, right in table)
            if total == 0:
                continue
            paired = sum(min(left, right) for left, right in table)
            excess = sum(abs(left - right) for left, right in table)
            assert total == 2 * paired + excess
            identity_checks += 1

            if 4 * paired >= total:
                assert all(
                    min(left, right) <= left and min(left, right) <= right
                    for left, right in table
                )
                coherent_checks += 1
            else:
                assert 2 * excess > total
                positive = sum(max(0, left - right) for left, right in table)
                negative = sum(max(0, right - left) for left, right in table)
                assert positive + negative == excess
                assert 4 * max(positive, negative) > total
                imbalance_checks += 1

    return identity_checks, coherent_checks, imbalance_checks


def verify_profile_and_scale_routers(maximum_atoms=5, maximum_labels=3):
    profile_checks = 0
    scale_checks = 0

    for atom_count in range(1, maximum_atoms + 1):
        for weights in product(range(4), repeat=atom_count):
            total = sum(weights)
            if total == 0:
                continue
            for labels in product(range(maximum_labels), repeat=atom_count):
                classes = {}
                for label, weight in zip(labels, weights, strict=True):
                    classes[label] = classes.get(label, 0) + weight
                heaviest = max(classes.values())
                assert heaviest * len(classes) >= total
                profile_checks += 1

                for cap in range(1, 5):
                    if heaviest <= cap:
                        assert len(classes) * cap >= total

                for threshold in range(1, maximum_labels + 1):
                    if len(classes) <= threshold:
                        assert heaviest * threshold >= total
                    else:
                        assert len(classes) > threshold
                scale_checks += 1

    return profile_checks, scale_checks


def verify_composition(maximum_weight=64):
    composition_checks = 0

    for total in range(1, maximum_weight + 1):
        for roles in range(1, 5):
            for multiplicity in range(1, 5):
                for channel_pairs in range(1, 5):
                    for scales in range(1, 5):
                        for profiles in range(1, 5):
                            role_weight = Fraction(total, 2 * roles * multiplicity)
                            channel_weight = role_weight / channel_pairs
                            complete_weight = channel_weight / 2
                            coherent_weight = complete_weight / 4
                            decorated_weight = coherent_weight / scales / profiles
                            expected = Fraction(
                                total,
                                16
                                * roles
                                * multiplicity
                                * channel_pairs
                                * scales
                                * profiles,
                            )
                            assert decorated_weight == expected
                            imbalance_profile = complete_weight / 4 / profiles
                            expected_imbalance = Fraction(
                                total,
                                16
                                * roles
                                * multiplicity
                                * channel_pairs
                                * profiles,
                            )
                            assert imbalance_profile == expected_imbalance
                            composition_checks += 1

    return composition_checks


def main():
    identities, coherent, imbalance = verify_pairing_identity()
    profiles, scales = verify_profile_and_scale_routers()
    compositions = verify_composition()
    print(
        "AC RI scale pairing: verified "
        f"{identities} identities, {coherent} coherent pairings, "
        f"{imbalance} imbalance routers, {profiles} profile routers, "
        f"{scales} scale routers, and {compositions} compositions"
    )


if __name__ == "__main__":
    main()
