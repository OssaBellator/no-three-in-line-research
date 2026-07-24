#!/usr/bin/env python3
"""Verify AC3s--AC3u canonical shared-token roles."""

from __future__ import annotations

from itertools import combinations, product
from math import inf


Phase = tuple[int, ...]
Mismatch = tuple[int, ...]
ExactRelation = frozenset[tuple[Phase, int]]
CompressedRelation = frozenset[tuple[Mismatch, int]]


def mismatch(phase: Phase, forbidden: Phase) -> Mismatch:
    return tuple(
        int(value != forbidden[index])
        for index, value in enumerate(phase)
    )


def exact_alphabet(sizes: tuple[int, ...]) -> tuple[Phase, ...]:
    return tuple(product(*(range(size) for size in sizes)))


def verify_seven_state_interface() -> None:
    for rank in range(1, 4):
        for sizes in product(range(1, 5), repeat=rank):
            alphabet = exact_alphabet(sizes)
            for forbidden in alphabet:
                discharge = tuple(
                    phase
                    for phase in alphabet
                    if phase != forbidden
                )
                mismatch_image = {
                    mismatch(phase, forbidden)
                    for phase in discharge
                }
                assert all(any(word) for word in mismatch_image)
                assert len(mismatch_image) <= 2**rank - 1 <= 7
                assert len(discharge) == (
                    len(alphabet) - 1
                )
                assert len(discharge) <= max(sizes) ** rank - 1

    rigid_alphabet = exact_alphabet((1, 1, 1))
    assert len(rigid_alphabet) == 1
    assert not tuple(
        phase
        for phase in rigid_alphabet
        if phase != (0, 0, 0)
    )


def lift_relation(
    relation: CompressedRelation,
    discharge: tuple[Phase, ...],
    forbidden: Phase,
) -> ExactRelation:
    return frozenset(
        (phase, private_state)
        for phase in discharge
        for private_state in range(2)
        if (
            mismatch(phase, forbidden),
            private_state,
        )
        in relation
    )


def local_cost(
    factor: int,
    word: Mismatch,
    private_state: int,
) -> int:
    code = sum(
        (index + 2) * bit
        for index, bit in enumerate(word)
    )
    return 1 + (
        5 * factor
        + 3 * code
        + 7 * private_state
    ) % 13


def fixed_cost(word: Mismatch) -> int:
    return sum(
        (index + 1) * bit
        for index, bit in enumerate(word)
    )


def verify_literal_invariant_compression() -> None:
    sizes = (3, 3)
    forbidden = (0, 0)
    discharge = tuple(
        phase
        for phase in exact_alphabet(sizes)
        if phase != forbidden
    )
    words = tuple(sorted({
        mismatch(phase, forbidden)
        for phase in discharge
    }))
    possible_pairs = tuple(product(words, range(2)))
    compressed_relations = [
        frozenset(
            pair
            for index, pair in enumerate(possible_pairs)
            if mask & (1 << index)
        )
        for mask in range(1 << len(possible_pairs))
    ]

    for compressed_family in product(compressed_relations, repeat=2):
        exact_family = tuple(
            lift_relation(relation, discharge, forbidden)
            for relation in compressed_family
        )

        exact_best = inf
        for phase in discharge:
            word = mismatch(phase, forbidden)
            for private_states in product(range(2), repeat=2):
                if all(
                    (phase, private_states[factor])
                    in exact_family[factor]
                    for factor in range(2)
                ):
                    exact_best = min(
                        exact_best,
                        fixed_cost(word)
                        + sum(
                            local_cost(
                                factor,
                                word,
                                private_states[factor],
                            )
                            for factor in range(2)
                        ),
                    )

        compressed_best = inf
        for word in words:
            for private_states in product(range(2), repeat=2):
                if all(
                    (word, private_states[factor])
                    in compressed_family[factor]
                    for factor in range(2)
                ):
                    compressed_best = min(
                        compressed_best,
                        fixed_cost(word)
                        + sum(
                            local_cost(
                                factor,
                                word,
                                private_states[factor],
                            )
                            for factor in range(2)
                        ),
                    )

        assert exact_best == compressed_best


def extension_set(
    relation: ExactRelation,
    phase: Phase,
) -> frozenset[int]:
    return frozenset(
        private_state
        for private_state in range(2)
        if (phase, private_state) in relation
    )


def relation_sensitivity_witness(
    relation: ExactRelation,
    discharge: tuple[Phase, ...],
    forbidden: Phase,
) -> tuple[Phase, Phase, int] | None:
    representatives: dict[Mismatch, Phase] = {}
    for phase in discharge:
        word = mismatch(phase, forbidden)
        if word not in representatives:
            representatives[word] = phase
            continue
        first = representatives[word]
        difference = (
            extension_set(relation, first)
            ^ extension_set(relation, phase)
        )
        if difference:
            return first, phase, next(iter(difference))
    return None


def verify_sensitivity_witnesses() -> None:
    sizes = (3, 3)
    forbidden = (0, 0)
    discharge = tuple(
        phase
        for phase in exact_alphabet(sizes)
        if phase != forbidden
    )
    possible_pairs = tuple(product(discharge, range(2)))

    for mask in range(1 << len(possible_pairs)):
        relation = frozenset(
            pair
            for index, pair in enumerate(possible_pairs)
            if mask & (1 << index)
        )
        witness = relation_sensitivity_witness(
            relation,
            discharge,
            forbidden,
        )
        invariant = all(
            extension_set(relation, left)
            == extension_set(relation, right)
            for left, right in combinations(discharge, 2)
            if mismatch(left, forbidden)
            == mismatch(right, forbidden)
        )
        assert invariant == (witness is None)
        if witness is not None:
            left, right, private_state = witness
            assert mismatch(left, forbidden) == mismatch(
                right,
                forbidden,
            )
            assert (
                ((left, private_state) in relation)
                != ((right, private_state) in relation)
            )

    full_relation = frozenset(possible_pairs)
    same_word_phases = [
        phase
        for phase in discharge
        if mismatch(phase, forbidden) == (1, 0)
    ]
    left, right = same_word_phases[:2]
    private_cost = {
        (phase, private_state): (
            9
            if phase == right and private_state == 0
            else 4
        )
        for phase, private_state in possible_pairs
    }
    assert extension_set(full_relation, left) == extension_set(
        full_relation,
        right,
    )
    assert private_cost[(left, 0)] != private_cost[(right, 0)]

    common_cost = {
        phase: (
            7
            if phase == right
            else 2
        )
        for phase in discharge
    }
    assert common_cost[left] != common_cost[right]


def verify_scope_complete_private_supports() -> None:
    token_scope = frozenset((0, 1))
    supports = tuple(
        frozenset(
            variable
            for variable in range(5)
            if mask & (1 << variable)
        )
        for mask in range(1 << 5)
    )

    for family in product(supports, repeat=3):
        private = tuple(
            support - token_scope
            for support in family
        )
        conflict_edges = {
            (left, right)
            for left, right in combinations(range(3), 2)
            if private[left] & private[right]
        }
        for mask in range(1 << 3):
            chosen = [
                index
                for index in range(3)
                if mask & (1 << index)
            ]
            independent = all(
                (left, right) not in conflict_edges
                for left, right in combinations(chosen, 2)
            )
            if not independent:
                continue
            assert all(
                not (private[left] & private[right])
                for left, right in combinations(chosen, 2)
            )


def main() -> None:
    verify_seven_state_interface()
    verify_literal_invariant_compression()
    verify_sensitivity_witnesses()
    verify_scope_complete_private_supports()
    print("AC canonical shared-token roles: verified")


if __name__ == "__main__":
    main()
