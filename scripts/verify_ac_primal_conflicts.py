#!/usr/bin/env python3
"""Verify AC3v--AC3x canonical primal conflict completion."""

from __future__ import annotations

from itertools import combinations, product


Cell = tuple[int, int]
Scope = frozenset[Cell]


def independent(
    chosen: tuple[int, ...],
    edges: set[tuple[int, int]],
) -> bool:
    return all(
        (min(left, right), max(left, right)) not in edges
        for left, right in combinations(chosen, 2)
    )


def primal_edges(
    envelopes: tuple[frozenset, ...],
    factor_scopes: tuple[frozenset, ...] = (),
    constraint_scopes: tuple[frozenset, ...] = (),
    paid_sets: tuple[frozenset, ...] | None = None,
) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for left, right in combinations(range(len(envelopes)), 2):
        conflict = bool(envelopes[left] & envelopes[right])
        conflict = conflict or any(
            scope & envelopes[left] and scope & envelopes[right]
            for scope in factor_scopes
        )
        conflict = conflict or any(
            scope & envelopes[left] and scope & envelopes[right]
            for scope in constraint_scopes
        )
        if paid_sets is not None:
            conflict = conflict or bool(
                paid_sets[left] & paid_sets[right]
            )
        if conflict:
            edges.add((left, right))
    return edges


def table_value(
    table: int,
    ordered_scope: tuple[int, ...],
    state: frozenset[int],
) -> int:
    restriction = sum(
        1 << index
        for index, cell in enumerate(ordered_scope)
        if cell in state
    )
    return (table >> restriction) & 1


def verify_arbitrary_factor_identity() -> None:
    """Exhaust every Boolean factor on every scope of four cells."""

    ground = tuple(range(4))
    base = frozenset({3})
    envelopes = (
        frozenset({0}),
        frozenset({1}),
        frozenset({2}),
    )

    for rank in range(1, len(ground) + 1):
        for raw_scope in combinations(ground, rank):
            scope = frozenset(raw_scope)
            edges = primal_edges(
                envelopes,
                factor_scopes=(scope,),
            )
            for table in range(1 << (1 << rank)):
                base_value = table_value(table, raw_scope, base)
                for chosen_mask in range(1 << len(envelopes)):
                    chosen = tuple(
                        index
                        for index in range(len(envelopes))
                        if chosen_mask & (1 << index)
                    )
                    if not independent(chosen, edges):
                        continue
                    for installs in product((0, 1), repeat=len(chosen)):
                        local_states = tuple(
                            envelopes[index]
                            if installs[position]
                            else frozenset()
                            for position, index in enumerate(chosen)
                        )
                        joint = base | frozenset().union(*local_states)
                        joint_delta = (
                            table_value(table, raw_scope, joint)
                            - base_value
                        )
                        local_delta = sum(
                            table_value(
                                table,
                                raw_scope,
                                base | state,
                            )
                            - base_value
                            for state in local_states
                        )
                        assert joint_delta == local_delta


def collinear(left: Cell, middle: Cell, right: Cell) -> bool:
    return (
        (middle[0] - left[0]) * (right[1] - left[1])
        ==
        (middle[1] - left[1]) * (right[0] - left[0])
    )


def grid_triples(grid: tuple[Cell, ...]) -> tuple[Scope, ...]:
    return tuple(
        frozenset(triple)
        for triple in combinations(grid, 3)
        if collinear(*triple)
    )


def row_column_constraints(grid: tuple[Cell, ...]) -> tuple[Scope, ...]:
    return tuple(
        frozenset((left, right))
        for left, right in combinations(grid, 2)
        if left[0] == right[0] or left[1] == right[1]
    )


def legal(
    state: frozenset[Cell],
    constraints: tuple[Scope, ...],
) -> bool:
    return all(not scope <= state for scope in constraints)


def potential(
    state: frozenset[Cell],
    triples: tuple[Scope, ...],
    weights: tuple[int, ...],
) -> int:
    return sum(
        weight
        for triple, weight in zip(triples, weights)
        if triple <= state
    )


def local_states(
    base: frozenset[Cell],
    envelope: frozenset[Cell],
    constraints: tuple[Scope, ...],
) -> tuple[frozenset[Cell], ...]:
    cells = tuple(sorted(envelope))
    return tuple(
        state
        for mask in range(1 << len(cells))
        if legal(
            base
            | (
                state := frozenset(
                    cell
                    for index, cell in enumerate(cells)
                    if mask & (1 << index)
                )
            ),
            constraints,
        )
    )


def verify_grid_additivity_and_legality() -> None:
    grid = tuple(product(range(3), repeat=2))
    triples = grid_triples(grid)
    constraints = row_column_constraints(grid)
    weights = tuple(
        1 + (7 * index + 3) % 11
        for index in range(len(triples))
    )
    raw_envelopes = (
        frozenset({(0, 0)}),
        frozenset({(1, 1)}),
        frozenset({(2, 2)}),
        frozenset({(0, 1), (1, 0)}),
        frozenset({(2, 0)}),
        frozenset({(0, 2)}),
        frozenset({(1, 2), (2, 1)}),
        frozenset({(0, 0), (1, 1), (2, 2)}),
        frozenset({(0, 0), (2, 2)}),
    )
    bases = (
        frozenset(),
        frozenset({(0, 2)}),
        frozenset({(1, 1)}),
    )

    for base in bases:
        envelopes = tuple(
            envelope
            for envelope in raw_envelopes
            if not envelope & base
        )
        states = tuple(
            local_states(base, envelope, constraints)
            for envelope in envelopes
        )
        edges = primal_edges(
            envelopes,
            factor_scopes=triples,
            constraint_scopes=constraints,
        )
        base_value = potential(base, triples, weights)

        for chosen_mask in range(1 << len(envelopes)):
            chosen = tuple(
                index
                for index in range(len(envelopes))
                if chosen_mask & (1 << index)
            )
            if not independent(chosen, edges):
                continue

            profiles: list[tuple[int, tuple[int, ...]]] = []
            for selected_states in product(*(states[j] for j in chosen)):
                joint = base | frozenset().union(*selected_states)
                assert legal(joint, constraints)
                joint_delta = potential(joint, triples, weights) - base_value
                local_deltas = tuple(
                    potential(base | state, triples, weights) - base_value
                    for state in selected_states
                )
                assert joint_delta == sum(local_deltas)
                profiles.append((joint_delta, local_deltas))

            for (
                before_total,
                before_locals,
            ), (
                after_total,
                after_locals,
            ) in combinations(profiles, 2):
                assert after_total - before_total == sum(
                    after - before
                    for before, after in zip(
                        before_locals,
                        after_locals,
                    )
                )


def verify_local_constraint_completion() -> None:
    """The background may have one hole filled by each private state."""

    constraints = (
        frozenset({0, 1}),
        frozenset({2, 3}),
    )
    envelopes = constraints
    edges = primal_edges(
        envelopes,
        constraint_scopes=constraints,
    )
    assert independent((0, 1), edges)

    state_families = (
        (frozenset({0}), frozenset({1})),
        (frozenset({2}), frozenset({3})),
    )
    base: frozenset[int] = frozenset()

    def exact_one(
        state: frozenset[int],
        scope: frozenset[int],
    ) -> bool:
        return len(state & scope) == 1

    assert not all(
        exact_one(base, scope)
        for scope in constraints
    )
    for states in product(*state_families):
        for scope in constraints:
            met = tuple(
                index
                for index, envelope in enumerate(envelopes)
                if scope & envelope
            )
            assert len(met) == 1
            assert exact_one(base | states[met[0]], scope)
        joint = base | frozenset().union(*states)
        assert all(
            exact_one(joint, scope)
            for scope in constraints
        )


def verify_higher_order_projection() -> None:
    diagonal = (
        frozenset({(0, 0)}),
        frozenset({(1, 1)}),
        frozenset({(2, 2)}),
    )
    triple = frozenset({(0, 0), (1, 1), (2, 2)})
    projected = primal_edges(
        diagonal,
        factor_scopes=(triple,),
    )
    assert projected == {(0, 1), (0, 2), (1, 2)}

    envelope_only = primal_edges(diagonal)
    assert not envelope_only
    states = tuple(envelope for envelope in diagonal)
    joint = frozenset().union(*states)
    assert int(triple <= joint) == 1
    assert sum(int(triple <= state) for state in states) == 0


def weighted(
    tokens: frozenset[str],
    weights: dict[str, int],
) -> int:
    return sum(weights[token] for token in tokens)


def verify_paid_additivity() -> None:
    common = frozenset({"pi"})
    paid_sets = (
        frozenset({"a", "b"}),
        frozenset({"b", "c"}),
        frozenset({"d"}),
        frozenset({"e", "a"}),
    )
    envelopes = tuple(frozenset({index}) for index in range(4))
    edges = primal_edges(
        envelopes,
        paid_sets=paid_sets,
    )
    weights = {
        "pi": 13,
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
    }

    for chosen_mask in range(1 << len(envelopes)):
        chosen = tuple(
            index
            for index in range(len(envelopes))
            if chosen_mask & (1 << index)
        )
        if not independent(chosen, edges):
            continue
        union = common | frozenset().union(
            *(paid_sets[index] for index in chosen)
        )
        assert weighted(union, weights) == (
            weighted(common, weights)
            + sum(weighted(paid_sets[index], weights) for index in chosen)
        )

    assert weighted(paid_sets[0] | paid_sets[1], weights) < (
        weighted(paid_sets[0], weights)
        + weighted(paid_sets[1], weights)
    )


def incidence_word(
    scope: Scope,
    left: frozenset[Cell],
    right: frozenset[Cell],
    base: frozenset[Cell],
) -> tuple[str, ...]:
    assert not left & right
    assert not left & base
    assert not right & base
    word = []
    for cell in sorted(scope):
        if cell in left:
            word.append("J")
        elif cell in right:
            word.append("K")
        elif cell in base:
            word.append("B")
        else:
            word.append("O")
    return tuple(word)


def verify_structural_labels() -> None:
    cross_words = {
        word
        for word in product(("J", "K", "B", "O"), repeat=3)
        if "J" in word and "K" in word
    }
    assert len(cross_words) == 18
    assert len(cross_words) <= 4**3

    grid = tuple(product(range(3), repeat=2))
    triples = grid_triples(grid)
    base = frozenset({(0, 2)})
    envelopes = tuple(
        frozenset({cell})
        for cell in grid
        if cell not in base
    )
    observed = set()
    for left, right in combinations(range(len(envelopes)), 2):
        witnesses = tuple(
            triple
            for triple in triples
            if triple & envelopes[left] and triple & envelopes[right]
        )
        for witness in witnesses:
            word = incidence_word(
                witness,
                envelopes[left],
                envelopes[right],
                base,
            )
            assert "J" in word and "K" in word
            observed.add(word)
    assert observed <= cross_words

    diagonal = frozenset({(0, 0), (1, 1), (2, 2)})
    word = incidence_word(
        diagonal,
        frozenset({(0, 0)}),
        frozenset({(1, 1)}),
        frozenset(),
    )
    assert word == ("J", "K", "O")


def main() -> None:
    verify_arbitrary_factor_identity()
    verify_grid_additivity_and_legality()
    verify_local_constraint_completion()
    verify_higher_order_projection()
    verify_paid_additivity()
    verify_structural_labels()
    print("AC canonical primal conflicts: verified")


if __name__ == "__main__":
    main()
