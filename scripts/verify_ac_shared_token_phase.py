#!/usr/bin/env python3
"""Verify AC3p--AC3r shared-token phase contraction."""

from __future__ import annotations

from itertools import combinations_with_replacement, product
from math import inf


Message = frozenset[int]
Relation = frozenset[tuple[int, int]]


def all_messages(alphabet_size: int) -> list[Message]:
    return [
        frozenset(
            phase
            for phase in range(alphabet_size)
            if mask & (1 << phase)
        )
        for mask in range(1 << alphabet_size)
    ]


def message_intersection(
    messages: tuple[Message, ...],
    alphabet: Message,
) -> Message:
    result = set(alphabet)
    for message in messages:
        result.intersection_update(message)
    return frozenset(result)


def canonical_core(
    messages: tuple[Message, ...],
    alphabet: Message,
) -> tuple[int, ...]:
    target = message_intersection(messages, alphabet)
    witnesses = set()
    for phase in alphabet - target:
        witness = next(
            index
            for index, message in enumerate(messages)
            if phase not in message
        )
        witnesses.add(witness)
    return tuple(sorted(witnesses))


def verify_message_contraction() -> None:
    for alphabet_size in range(1, 5):
        alphabet = frozenset(range(alphabet_size))
        messages = all_messages(alphabet_size)
        maximum_family_size = alphabet_size + 2
        for family_size in range(maximum_family_size + 1):
            for indices in combinations_with_replacement(
                range(len(messages)),
                family_size,
            ):
                family = tuple(messages[index] for index in indices)
                target = message_intersection(family, alphabet)
                core_indices = canonical_core(family, alphabet)
                core = tuple(family[index] for index in core_indices)
                assert message_intersection(core, alphabet) == target
                assert len(core) <= alphabet_size - len(target)


def verify_phase_loss_tickets() -> None:
    for alphabet_size in range(1, 5):
        full_mask = (1 << alphabet_size) - 1
        masks = range(1 << alphabet_size)
        for sequence in product(masks, repeat=alphabet_size + 1):
            current = full_mask
            strict_losses = 0
            previous_potential = 0
            for message in sequence:
                updated = current & message
                potential = alphabet_size - updated.bit_count()
                assert potential >= previous_potential
                if updated != current:
                    strict_losses += 1
                    assert potential > previous_potential
                else:
                    assert current & ~message == 0
                current = updated
                previous_potential = potential
            assert strict_losses <= alphabet_size


def relation_message(
    relation: Relation,
    alphabet_size: int,
) -> Message:
    return frozenset(
        phase
        for phase in range(alphabet_size)
        if any(
            (phase, private_state) in relation
            for private_state in range(2)
        )
    )


def local_cost(
    factor: int,
    phase: int,
    private_state: int,
) -> int:
    return 1 + (
        5 * factor
        + 3 * phase
        + 7 * private_state
    ) % 11


def fixed_cost(phase: int) -> int:
    return (2 * phase + 1) % 5


def verify_product_cost_formula() -> None:
    alphabet_size = 3
    alphabet = frozenset(range(alphabet_size))
    possible_pairs = tuple(product(range(alphabet_size), range(2)))
    relations = [
        frozenset(
            pair
            for index, pair in enumerate(possible_pairs)
            if mask & (1 << index)
        )
        for mask in range(1 << len(possible_pairs))
    ]

    for relation_family in product(relations, repeat=3):
        messages = tuple(
            relation_message(relation, alphabet_size)
            for relation in relation_family
        )
        common_message = message_intersection(messages, alphabet)

        brute_force_best = inf
        for phase in range(alphabet_size):
            for private_states in product(range(2), repeat=3):
                if all(
                    (phase, private_states[factor])
                    in relation_family[factor]
                    for factor in range(3)
                ):
                    brute_force_best = min(
                        brute_force_best,
                        fixed_cost(phase)
                        + sum(
                            local_cost(
                                factor,
                                phase,
                                private_states[factor],
                            )
                            for factor in range(3)
                        ),
                    )

        message_best = inf
        for phase in common_message:
            private_sum = 0
            for factor, relation in enumerate(relation_family):
                private_sum += min(
                    local_cost(factor, phase, private_state)
                    for private_state in range(2)
                    if (phase, private_state) in relation
                )
            message_best = min(
                message_best,
                fixed_cost(phase) + private_sum,
            )

        assert brute_force_best == message_best
        assert (brute_force_best < inf) == bool(common_message)

        core_indices = canonical_core(messages, alphabet)
        core_messages = tuple(
            messages[index]
            for index in core_indices
        )
        assert (
            message_intersection(core_messages, alphabet)
            == common_message
        )
        assert len(core_indices) <= alphabet_size - len(common_message)

        if message_best < inf:
            for paid_weight in range(1, 18):
                if message_best < paid_weight:
                    assert paid_weight - message_best > 0
                else:
                    assert all(
                        fixed_cost(phase)
                        + sum(
                            min(
                                local_cost(
                                    factor,
                                    phase,
                                    private_state,
                                )
                                for private_state in range(2)
                                if (phase, private_state)
                                in relation_family[factor]
                            )
                            for factor in range(3)
                        )
                        >= paid_weight
                        for phase in common_message
                    )


def main() -> None:
    verify_message_contraction()
    verify_phase_loss_tickets()
    verify_product_cost_formula()
    print("AC shared-token phase contraction: verified")


if __name__ == "__main__":
    main()
