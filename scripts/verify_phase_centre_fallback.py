#!/usr/bin/env python3
"""Exact finite checks for OP4o current-centre descent."""

from fractions import Fraction
from itertools import combinations, product


def centre_fallback(gains, weights, indices):
    """Return a maximum-weight current centre and its certified bound."""
    indices = tuple(indices)
    assert indices
    assert len(gains) == len(weights)
    assert all(Fraction(0) < weights[i] <= gains[i] for i in indices)
    chosen = max(indices, key=lambda i: weights[i])
    total = sum((weights[i] for i in indices), Fraction(0))
    bound = total / len(indices)
    assert gains[chosen] >= weights[chosen] >= bound > 0
    return chosen, bound


def exhaustive_weighted_families():
    pairs = tuple(
        (Fraction(g), Fraction(g, divisor))
        for g in range(1, 5)
        for divisor in range(1, 4)
    )
    family_count = 0
    subfamily_count = 0
    for size in range(1, 5):
        for family in product(pairs, repeat=size):
            gains = tuple(pair[0] for pair in family)
            weights = tuple(pair[1] for pair in family)
            family_count += 1
            for subset_size in range(1, size + 1):
                for indices in combinations(range(size), subset_size):
                    chosen, bound = centre_fallback(gains, weights, indices)
                    assert gains[chosen] >= bound
                    subfamily_count += 1
    return family_count, subfamily_count


def check_signature_splits():
    checked = 0
    for size in range(1, 7):
        for gains_raw in product(range(1, 5), repeat=size):
            gains = tuple(Fraction(g) for g in gains_raw)
            for signature_count in range(1, 5):
                weights = tuple(g / signature_count for g in gains)
                chosen, bound = centre_fallback(
                    gains, weights, range(size)
                )
                assert gains[chosen] >= bound
                assert sum(weights, Fraction(0)) == (
                    sum(gains, Fraction(0)) / signature_count
                )
                checked += 1
    return checked


def check_paid_classes():
    checked = 0
    # Use 12G as the common integer scale.  The strict OP3j thresholds
    # become G_wide > 3G and G_action > G on this scale.
    for size in range(1, 7):
        for gains_raw in product(range(1, 5), repeat=size):
            gains = tuple(Fraction(g) for g in gains_raw)
            class_gain = sum(gains, Fraction(0))
            chosen, bound = centre_fallback(gains, gains, range(size))
            assert gains[chosen] >= class_gain / size == bound
            for total_scale in range(1, 13):
                total_gain = Fraction(total_scale)
                if class_gain > total_gain / 4:
                    assert gains[chosen] > total_gain / (4 * size)
                if class_gain > total_gain / 12:
                    assert gains[chosen] > total_gain / (12 * size)
                checked += 1
    return checked


def blocker_fallback(factors, gains, weights, divisor_cap):
    """Check switch-disjointness and apply OP4o to one blocker fibre."""
    assert factors
    flat = tuple(index for factor in factors for index in factor)
    assert all(len(factor) == 3 and len(set(factor)) == 3
               for factor in factors)
    assert len(set(flat)) == len(flat)
    assert len(factors) <= divisor_cap
    chosen, bound = centre_fallback(gains, weights, flat)
    total = sum((weights[i] for i in flat), Fraction(0))
    assert len(flat) == 3 * len(factors)
    assert bound == total / (3 * len(factors))
    assert bound >= total / (3 * divisor_cap)
    return chosen, bound


def check_blocker_fibres():
    checked = 0
    # Exhaust all small centre-weight patterns.  The grouping is
    # immaterial after switch-disjointness, but its exact 3b cardinality
    # and divisor-cap comparison are checked on every instance.
    for factor_count in range(1, 4):
        centre_count = 3 * factor_count
        factors = tuple(
            tuple(range(3 * j, 3 * j + 3))
            for j in range(factor_count)
        )
        for weights_raw in product(range(1, 4), repeat=centre_count):
            weights = tuple(Fraction(w) for w in weights_raw)
            gains = tuple(w + Fraction((i % 3), 2)
                          for i, w in enumerate(weights))
            blocker_fallback(factors, gains, weights, 16)
            checked += 1

    # Exercise every possible recurrent fibre size through the cap with
    # exact OP3k-style split weights.
    for factor_count in range(1, 17):
        centre_count = 3 * factor_count
        factors = tuple(
            tuple(range(3 * j, 3 * j + 3))
            for j in range(factor_count)
        )
        gains = tuple(Fraction((i % 5) + 1) for i in range(centre_count))
        weights = tuple(g / ((i % 4) + 1) for i, g in enumerate(gains))
        blocker_fallback(factors, gains, weights, 16)
        checked += 1

    # Overlap is not silently accepted as a matching fibre.
    try:
        blocker_fallback(
            ((0, 1, 2), (2, 3, 4)),
            (Fraction(1),) * 5,
            (Fraction(1),) * 5,
            16,
        )
    except AssertionError:
        pass
    else:
        raise AssertionError("overlapping blocker factors were accepted")
    return checked


def check_sharpness():
    for size in range(1, 33):
        for value in (Fraction(1, 3), Fraction(1), Fraction(7, 2)):
            gains = (value,) * size
            weights = gains
            chosen, bound = centre_fallback(gains, weights, range(size))
            assert gains[chosen] == bound == value


def main():
    family_count, subfamily_count = exhaustive_weighted_families()
    split_count = check_signature_splits()
    paid_count = check_paid_classes()
    blocker_count = check_blocker_fibres()
    check_sharpness()
    print(
        "phase centre fallback verification passed:",
        f"{family_count} weighted families,",
        f"{subfamily_count} nonempty subfamilies,",
        f"{split_count} exact split families,",
        f"{paid_count} paid-class comparisons,",
        f"{blocker_count} blocker fibres,",
        "sharp equal-weight bounds",
    )


if __name__ == "__main__":
    main()
