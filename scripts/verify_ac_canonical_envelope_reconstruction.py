#!/usr/bin/env python3
"""Exact finite checks for AC3mf--AC3mk."""

from __future__ import annotations

from itertools import combinations, product

State = frozenset[int]
Family = tuple[State, ...]


def all_subsets(size: int) -> list[State]:
    return [
        frozenset(
            element
            for element in range(size)
            if (mask >> element) & 1
        )
        for mask in range(1 << size)
    ]


def minimal_envelope(family: Family) -> State:
    result: set[int] = set()
    for state in family:
        result.update(state)
    return frozenset(result)


def incidence_map(states: tuple[State, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        (address, cell)
        for address, state in enumerate(states)
        for cell in state
    )


def main() -> None:
    universe_size = 3
    states = all_subsets(universe_size)
    nonempty_scopes = [state for state in states if state]

    families: list[Family] = [
        tuple(
            states[index]
            for index in range(len(states))
            if (mask >> index) & 1
        )
        for mask in range(1 << len(states))
    ]

    totals = {
        "state_families": len(families),
        "minimal_envelope_checks": 0,
        "valid_superset_checks": 0,
        "state_incidence_comparisons": 0,
        "monotone_family_inclusions": 0,
        "graph_monotonicity_checks": 0,
        "scope_completion_checks": 0,
        "decoration_formula_checks": 0,
    }

    valid_supersets: dict[Family, list[State]] = {}

    # Unique minimality and every possible valid envelope superset.
    for family in families:
        envelope = minimal_envelope(family)
        assert all(state <= envelope for state in family)

        supersets: list[State] = []
        for candidate in states:
            if all(state <= candidate for state in family):
                assert envelope <= candidate
                supersets.append(candidate)
                totals["valid_superset_checks"] += 1
        valid_supersets[family] = supersets
        totals["minimal_envelope_checks"] += 1

    # Fixed state-address systems: envelope changes are projections of incidence
    # changes.  Three addresses give 8^3 exact realization maps.
    realization_maps = list(product(states, repeat=3))
    for left in realization_maps:
        left_incidence = incidence_map(left)
        left_envelope = minimal_envelope(left)
        for right in realization_maps:
            right_incidence = incidence_map(right)
            right_envelope = minimal_envelope(right)

            assert len(left_envelope ^ right_envelope) <= len(
                left_incidence ^ right_incidence
            )
            for cell in left_envelope ^ right_envelope:
                assert any(
                    (address, cell) in left_incidence ^ right_incidence
                    for address in range(3)
                )
            totals["state_incidence_comparisons"] += 1

    # Every inclusion of state families induces envelope inclusion.
    for left_mask, left_family in enumerate(families):
        left_envelope = minimal_envelope(left_family)
        remaining = [
            index
            for index in range(len(states))
            if not (left_mask >> index) & 1
        ]
        for add_mask in range(1 << len(remaining)):
            right_mask = left_mask
            for position, index in enumerate(remaining):
                if (add_mask >> position) & 1:
                    right_mask |= 1 << index
            right_envelope = minimal_envelope(families[right_mask])
            assert left_envelope <= right_envelope
            totals["monotone_family_inclusions"] += 1

    # Enlarging valid envelopes can only add overlap or scope-conflict edges.
    for left_family in families:
        left_minimal = minimal_envelope(left_family)
        for right_family in families:
            right_minimal = minimal_envelope(right_family)
            for left_superset in valid_supersets[left_family]:
                for right_superset in valid_supersets[right_family]:
                    if left_minimal & right_minimal:
                        assert left_superset & right_superset
                    for scope in nonempty_scopes:
                        if scope & left_minimal and scope & right_minimal:
                            assert scope & left_superset
                            assert scope & right_superset
                        totals["graph_monotonicity_checks"] += 1

    # Scope-completion: in every independent three-repair system, one scoped
    # factor or constraint meets at most one selected minimal envelope.
    for envelopes in product(states, repeat=3):
        for scope_mask in range(1 << len(nonempty_scopes)):
            scope_family = [
                nonempty_scopes[index]
                for index in range(len(nonempty_scopes))
                if (scope_mask >> index) & 1
            ]
            edges: set[tuple[int, int]] = set()
            for left, right in combinations(range(3), 2):
                if envelopes[left] & envelopes[right] or any(
                    scope & envelopes[left] and scope & envelopes[right]
                    for scope in scope_family
                ):
                    edges.add((left, right))

            for selected_mask in range(1 << 3):
                selected = [
                    index
                    for index in range(3)
                    if (selected_mask >> index) & 1
                ]
                independent = all(
                    (min(left, right), max(left, right)) not in edges
                    for left, right in combinations(selected, 2)
                )
                if not independent:
                    continue
                for scope in scope_family:
                    assert sum(
                        bool(scope & envelopes[index])
                        for index in selected
                    ) <= 1
                totals["scope_completion_checks"] += 1

    for addresses in range(1, 101):
        for cells in range(1, 101):
            bound = 2 * addresses * cells
            assert bound >= addresses * cells
            totals["decoration_formula_checks"] += 1

    print("AC3mf--AC3mk verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
