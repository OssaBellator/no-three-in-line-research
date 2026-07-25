#!/usr/bin/env python3
"""Exhaust RI5aa--RI5ab on small prescription systems."""

from fractions import Fraction
from itertools import product


def prescription_words(component_count):
    words = []
    for word in product((None, 0, 1), repeat=component_count):
        rank = sum(value is not None for value in word)
        if 1 <= rank <= 3 and any(value == 1 for value in word):
            words.append(word)
    return words


def survives(word, active):
    active = set(active)
    return all(
        not (value == 1 and index not in active)
        for index, value in enumerate(word)
    )


def filtered_rank(word, active):
    active = set(active)
    return sum(
        value is not None and index in active
        for index, value in enumerate(word)
    )


def local_shadow_costs(words, weights, active):
    active = tuple(active)
    costs = {index: 0 for index in active}
    local_words = {index: set() for index in active}

    for word_index, word in enumerate(words):
        if not survives(word, active):
            continue
        if filtered_rank(word, active) != 1:
            continue
        targets = [
            index
            for index in active
            if word[index] == 1
        ]
        assert len(targets) == 1
        target = targets[0]
        costs[target] += weights[word_index]
        local_words[target].add(word_index)

    return costs, local_words


def prune(words, weights, paid, component_count):
    active = tuple(range(component_count))
    stages = []

    while True:
        costs, local_words = local_shadow_costs(words, weights, active)
        retained = tuple(
            index for index in active if paid[index] > costs[index]
        )
        removed = tuple(index for index in active if index not in retained)
        stages.append((active, costs, local_words, removed))
        if retained == active:
            return active, stages
        active = retained


def weightings(words):
    yield tuple(1 for _ in words)
    yield tuple(1 + (index % 2) for index, _ in enumerate(words))
    yield tuple(
        1 + sum(value == 1 for value in word)
        for word in words
    )


def verify(maximum_components=5, maximum_paid=3):
    system_checks = 0
    word_checks = 0
    router_checks = 0

    for component_count in range(1, maximum_components + 1):
        words = prescription_words(component_count)

        for weights in weightings(words):
            for paid in product(
                range(maximum_paid + 1), repeat=component_count
            ):
                terminal, stages = prune(
                    words, weights, paid, component_count
                )
                assert len(stages) <= component_count + 1

                # Local costs are monotone for surviving components.
                for stage_index in range(len(stages) - 1):
                    active, costs, _, _ = stages[stage_index]
                    next_active, next_costs, _, _ = stages[stage_index + 1]
                    assert set(next_active) <= set(active)
                    for index in next_active:
                        assert next_costs[index] >= costs[index]

                removed_word_sets = []
                removed_paid = 0
                removed_shadow = 0
                for active, costs, local_words, removed in stages:
                    for index in removed:
                        assert paid[index] <= costs[index]
                        removed_paid += paid[index]
                        removed_shadow += costs[index]
                        removed_word_sets.append(local_words[index])

                for left in range(len(removed_word_sets)):
                    for right in range(left + 1, len(removed_word_sets)):
                        assert not (
                            removed_word_sets[left]
                            & removed_word_sets[right]
                        )

                if not terminal:
                    assert sum(paid) == removed_paid
                    assert removed_paid <= removed_shadow
                else:
                    terminal_costs, terminal_local = local_shadow_costs(
                        words, weights, terminal
                    )
                    positive_margin = sum(
                        paid[index] - terminal_costs[index]
                        for index in terminal
                    )
                    assert positive_margin > 0

                    states = []
                    for bits_now in product((0, 1), repeat=len(terminal)):
                        bits = [0] * component_count
                        for offset, index in enumerate(terminal):
                            bits[index] = bits_now[offset]
                        states.append(tuple(bits))

                    expected_paid = sum(
                        Fraction(
                            sum(
                                paid[index]
                                for index in terminal
                                if bits[index]
                            ),
                            len(states),
                        )
                        for bits in states
                    )
                    expected_local = sum(
                        Fraction(
                            sum(
                                terminal_costs[index]
                                for index in terminal
                                if bits[index]
                            ),
                            len(states),
                        )
                        for bits in states
                    )
                    assert expected_paid - expected_local == Fraction(
                        positive_margin, 2
                    )

                    charged = set().union(
                        *terminal_local.values()
                    ) if terminal_local else set()
                    for word_index, word in enumerate(words):
                        if not survives(word, terminal):
                            continue
                        rank = filtered_rank(word, terminal)
                        if rank == 1:
                            assert word_index in charged
                        elif word_index not in charged:
                            assert 2 <= rank <= 3
                        word_checks += 1

                system_checks += 1

    # Three-way failure router.
    for margin in range(1, 9):
        half_margin = Fraction(margin, 2)
        for fixed in range(5):
            if half_margin <= fixed:
                continue
            for terms in product(range(5), repeat=3):
                if sum(terms) < half_margin - fixed:
                    continue
                assert max(terms) >= (half_margin - fixed) / 3
                router_checks += 1

    return system_checks, word_checks, router_checks


def main():
    systems, words, routers = verify()
    print(
        "RI shadow pruning: verified "
        f"{systems} systems, {words} terminal words, "
        f"and {routers} failure routers"
    )


if __name__ == "__main__":
    main()
