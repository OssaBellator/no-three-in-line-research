#!/usr/bin/env python3
"""Exhaust RI5y--RI5z on small paid/collateral systems."""

from fractions import Fraction
from itertools import product


def prescription_words(component_count):
    # None means unprescribed; 0 and 1 prescribe current and target.
    words = []
    for word in product((None, 0, 1), repeat=component_count):
        rank = sum(value is not None for value in word)
        if 1 <= rank <= 3 and any(value == 1 for value in word):
            words.append(word)
    return words


def occurs(word, bits):
    return all(
        required is None or required == bits[index]
        for index, required in enumerate(word)
    )


def verify_margin_systems(maximum_components=4, maximum_weight=2):
    margin_checks = 0
    probability_checks = 0

    for component_count in range(1, maximum_components + 1):
        words = prescription_words(component_count)

        for paid in product(
            range(maximum_weight + 1), repeat=component_count
        ):
            for rank_one in product(
                range(maximum_weight + 1), repeat=component_count
            ):
                favorable = tuple(
                    index
                    for index in range(component_count)
                    if paid[index] > rank_one[index]
                )
                frozen = set(range(component_count)) - set(favorable)
                positive_margin = sum(
                    paid[index] - rank_one[index]
                    for index in favorable
                )
                total_paid = sum(paid)
                total_rank_one = sum(rank_one)

                assert positive_margin >= max(
                    0, total_paid - total_rank_one
                )

                toggle_states = []
                for favorable_bits in product((0, 1), repeat=len(favorable)):
                    bits = [0] * component_count
                    for offset, index in enumerate(favorable):
                        bits[index] = favorable_bits[offset]
                    toggle_states.append(tuple(bits))

                expected_paid = sum(
                    Fraction(
                        sum(
                            paid[index]
                            for index in favorable
                            if bits[index]
                        ),
                        len(toggle_states),
                    )
                    for bits in toggle_states
                )
                expected_rank_one = sum(
                    Fraction(
                        sum(
                            rank_one[index]
                            for index in favorable
                            if bits[index]
                        ),
                        len(toggle_states),
                    )
                    for bits in toggle_states
                )
                assert expected_paid - expected_rank_one == Fraction(
                    positive_margin, 2
                )
                margin_checks += 1

                for word in words:
                    original_rank = sum(
                        value is not None for value in word
                    )
                    if original_rank == 1:
                        continue

                    if any(word[index] == 1 for index in frozen):
                        expected_probability = Fraction(0, 1)
                    else:
                        filtered_rank = sum(
                            word[index] is not None
                            for index in favorable
                        )
                        assert 1 <= filtered_rank <= 3
                        expected_probability = Fraction(
                            1, 2**filtered_rank
                        )

                    actual_probability = Fraction(
                        sum(occurs(word, bits) for bits in toggle_states),
                        len(toggle_states),
                    )
                    assert actual_probability == expected_probability
                    probability_checks += 1

    return margin_checks, probability_checks


def verify_failure_router(maximum_value=4):
    checks = 0
    for positive_margin in range(1, 2 * maximum_value + 1):
        half_margin = Fraction(positive_margin, 2)
        for fixed in range(maximum_value + 1):
            if half_margin <= fixed:
                continue
            for terms in product(range(maximum_value + 1), repeat=4):
                if sum(terms) < half_margin - fixed:
                    continue
                assert max(terms) >= (half_margin - fixed) / 4
                checks += 1
    return checks


def verify():
    margins, probabilities = verify_margin_systems()
    routers = verify_failure_router()
    return margins, probabilities, routers


def main():
    margins, probabilities, routers = verify()
    print(
        "RI rank-one margin bank: verified "
        f"{margins} margin systems, {probabilities} prescription "
        f"probabilities, and {routers} failure routers"
    )


if __name__ == "__main__":
    main()
