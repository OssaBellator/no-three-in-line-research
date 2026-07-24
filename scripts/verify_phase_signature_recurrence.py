#!/usr/bin/env python3
"""Verify OP3k--OP4c signature recurrence and protected-bank completion."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import ceil


Signature = int
Support = frozenset[int]
Literal = tuple[int, int]
Clause = tuple[Literal, ...]
Check = dict[int, int]
Correction = dict[int, int]


def exposure_ledger(
    events: tuple[frozenset[Signature], ...],
    gains: tuple[int, ...],
) -> tuple[
    Counter[Signature],
    dict[Signature, Fraction],
    tuple[int, ...],
    tuple[int, ...],
]:
    """Return degrees, split gain, fresh events, and wholly recurrent events."""

    assert len(events) == len(gains)
    degree: Counter[Signature] = Counter()
    load: dict[Signature, Fraction] = defaultdict(Fraction)
    seen: set[Signature] = set()
    fresh: list[int] = []
    recurrent: list[int] = []

    for index, (signatures, gain) in enumerate(zip(events, gains)):
        assert signatures
        assert gain > 0
        if signatures - seen:
            fresh.append(index)
        else:
            recurrent.append(index)
        share = Fraction(gain, len(signatures))
        for signature in signatures:
            degree[signature] += 1
            load[signature] += share
        seen.update(signatures)

    assert sum(load.values(), Fraction()) == sum(gains)
    assert len(fresh) <= len(seen)
    return degree, dict(load), tuple(fresh), tuple(recurrent)


def verify_exposure_ledger() -> int:
    checked = 0
    for universe_size in range(1, 4):
        universe = tuple(range(universe_size))
        nonempty = tuple(
            frozenset(choice)
            for size in range(1, universe_size + 1)
            for choice in combinations(universe, size)
        )
        for round_count in range(1, 5):
            for events in product(nonempty, repeat=round_count):
                gains = tuple(index + 1 for index in range(round_count))
                degree, load, fresh, recurrent = exposure_ledger(
                    events,
                    gains,
                )
                union = set().union(*events)
                incidence_count = sum(map(len, events))
                assert set(degree) == union
                assert max(load.values()) >= Fraction(sum(gains), len(union))
                assert len(fresh) <= len(union)

                seen: set[int] = set()
                for index, signatures in enumerate(events):
                    if index in recurrent:
                        assert signatures <= seen
                    seen.update(signatures)

                for capacity in range(1, round_count + 1):
                    if max(degree.values()) <= capacity:
                        assert len(union) >= ceil(
                            incidence_count / capacity
                        )
                checked += 1
    return checked


def verify_snapshot_ledger() -> int:
    checked = 0
    signature_sets = (
        frozenset({0}),
        frozenset({1}),
        frozenset({0, 1}),
    )
    for state_count in range(1, 4):
        events = tuple(
            (state, signatures)
            for state in range(state_count)
            for signatures in signature_sets
        )
        for trace_length in range(1, 5):
            for trace in product(events, repeat=trace_length):
                ledger: set[tuple[int, int]] = set()
                growth_rounds = 0
                for state, signatures in trace:
                    tokens = {
                        (state, signature)
                        for signature in signatures
                    }
                    if tokens - ledger:
                        growth_rounds += 1
                    else:
                        assert tokens <= ledger
                    ledger.update(tokens)
                assert len(ledger) <= 2 * state_count
                assert growth_rounds <= len(ledger)
                checked += 1
    return checked


def verify_token_descent() -> int:
    checked = 0
    for token_budget in range(1, 7):
        for potential in range(1, 5):
            for ledger_size in range(token_budget + 1):
                rank = (
                    (token_budget + 1) * potential
                    + token_budget
                    - ledger_size
                )
                for reset_ledger in range(token_budget + 1):
                    improved_rank = (
                        (token_budget + 1) * (potential - 1)
                        + token_budget
                        - reset_ledger
                    )
                    assert improved_rank < rank
                    checked += 1
                if ledger_size < token_budget:
                    growth_rank = (
                        (token_budget + 1) * potential
                        + token_budget
                        - (ledger_size + 1)
                    )
                    assert growth_rank == rank - 1
                    checked += 1
    return checked


def support_coloring(
    supports: tuple[Support, ...],
) -> tuple[tuple[int, ...], ...]:
    """Greedily partition a support family into disjoint color classes."""

    assert supports
    assert all(supports)
    adjacency: list[set[int]] = [set() for _ in supports]
    for left, right in combinations(range(len(supports)), 2):
        if supports[left] & supports[right]:
            adjacency[left].add(right)
            adjacency[right].add(left)

    colors: list[int] = [-1] * len(supports)
    order = sorted(
        range(len(supports)),
        key=lambda index: (-len(adjacency[index]), index),
    )
    for index in order:
        used = {
            colors[neighbor]
            for neighbor in adjacency[index]
            if colors[neighbor] >= 0
        }
        color = 0
        while color in used:
            color += 1
        colors[index] = color

    classes = tuple(
        tuple(index for index, value in enumerate(colors) if value == color)
        for color in range(max(colors) + 1)
    )
    for color_class in classes:
        for left, right in combinations(color_class, 2):
            assert supports[left].isdisjoint(supports[right])
    return classes


def paid_disjoint_class(
    supports: tuple[Support, ...],
    weights: tuple[Fraction, ...],
) -> tuple[tuple[int, ...], int, int]:
    """Extract a disjoint color class retaining the largest total weight."""

    assert len(supports) == len(weights)
    assert all(weight > 0 for weight in weights)
    classes = support_coloring(supports)
    point_load = Counter(
        point
        for support in supports
        for point in support
    )
    support_width = max(map(len, supports))
    maximum_load = max(point_load.values())
    assert len(classes) <= support_width * maximum_load

    selected = max(
        classes,
        key=lambda color_class: (
            sum((weights[index] for index in color_class), Fraction()),
            tuple(-index for index in color_class),
        ),
    )
    selected_weight = sum(
        (weights[index] for index in selected),
        Fraction(),
    )
    assert selected_weight * support_width * maximum_load >= sum(weights)
    return selected, support_width, maximum_load


def verify_paid_disjoint_extraction() -> int:
    universe = range(4)
    candidates = tuple(
        frozenset(choice)
        for size in (1, 2)
        for choice in combinations(universe, size)
    )
    checked = 0
    for family_size in range(1, 6):
        for supports in combinations(candidates, family_size):
            weights = tuple(
                Fraction(1 + (3 * index) % 5, 1 + index % 2)
                for index in range(family_size)
            )
            selected, width, maximum_load = paid_disjoint_class(
                supports,
                weights,
            )
            assert all(
                supports[left].isdisjoint(supports[right])
                for left, right in combinations(selected, 2)
            )
            assert (
                sum((weights[index] for index in selected), Fraction())
                * width
                * maximum_load
                >= sum(weights)
            )
            checked += 1

    targets = (1, 2, 1, 3, 2, 3, 1)
    repeated = max(Counter(targets).values())
    assert repeated >= ceil(len(targets) / 3)
    return checked


@dataclass(frozen=True)
class ProjectedClause:
    literals: Clause
    check_index: int
    touched: tuple[tuple[int, tuple[int, ...]], ...]


def build_protected_cnf(
    current: tuple[int, ...],
    corrections: tuple[Correction, ...],
    checks: tuple[Check, ...],
) -> tuple[ProjectedClause, ...]:
    """Project canonical forbidden checks to binary correction orientations."""

    owner: dict[int, int] = {}
    for index, correction in enumerate(corrections):
        assert correction
        for variable, target in correction.items():
            assert 0 <= variable < len(current)
            assert target != current[variable]
            assert variable not in owner
            owner[variable] = index

    projected: list[ProjectedClause] = []
    for check_index, check in enumerate(checks):
        assert check
        assert len(check) <= 3
        required: dict[int, int] = {}
        touched: dict[int, list[int]] = defaultdict(list)
        possible = True

        for variable, forbidden in check.items():
            assert 0 <= variable < len(current)
            if variable not in owner:
                if current[variable] != forbidden:
                    possible = False
                    break
                continue

            correction_index = owner[variable]
            target = corrections[correction_index][variable]
            if current[variable] == forbidden:
                orientation = 0
            elif target == forbidden:
                orientation = 1
            else:
                possible = False
                break

            if (
                correction_index in required
                and required[correction_index] != orientation
            ):
                possible = False
                break
            required[correction_index] = orientation
            touched[correction_index].append(variable)

        if not possible:
            continue

        literals = tuple(
            (correction_index, 1 - orientation)
            for correction_index, orientation in sorted(required.items())
        )
        projected.append(
            ProjectedClause(
                literals=literals,
                check_index=check_index,
                touched=tuple(
                    (index, tuple(variables))
                    for index, variables in sorted(touched.items())
                ),
            )
        )
    return tuple(projected)


def protected_state(
    current: tuple[int, ...],
    corrections: tuple[Correction, ...],
    orientation: tuple[int, ...],
) -> tuple[int, ...]:
    state = list(current)
    for enabled, correction in zip(orientation, corrections):
        if enabled:
            for variable, target in correction.items():
                state[variable] = target
    return tuple(state)


def clause_satisfied(clause: Clause, orientation: tuple[int, ...]) -> bool:
    return any(orientation[variable] == value for variable, value in clause)


def check_violated(state: tuple[int, ...], check: Check) -> bool:
    return all(state[variable] == value for variable, value in check.items())


def verify_projection_exactness() -> int:
    current = (0, 0, 0, 0)
    corrections = ({0: 1, 1: 1}, {2: 1}, {3: 1})
    checks: list[Check] = []
    for rank in range(1, 4):
        for scope in combinations(range(4), rank):
            for values in product(range(3), repeat=rank):
                checks.append(dict(zip(scope, values)))

    projected = build_protected_cnf(
        current,
        corrections,
        tuple(checks),
    )
    for check in checks:
        one_projection = build_protected_cnf(
            current,
            corrections,
            (check,),
        )
        for orientation in product((0, 1), repeat=len(corrections)):
            state = protected_state(current, corrections, orientation)
            source_clean = not check_violated(state, check)
            formula_clean = all(
                clause_satisfied(item.literals, orientation)
                for item in one_projection
            )
            assert source_clean == formula_clean

    for orientation in product((0, 1), repeat=len(corrections)):
        state = protected_state(current, corrections, orientation)
        source_clean = not any(
            check_violated(state, check)
            for check in checks
        )
        formula_clean = all(
            clause_satisfied(item.literals, orientation)
            for item in projected
        )
        assert source_clean == formula_clean

    conflicting = {0: 0, 1: 1}
    assert not build_protected_cnf(
        current,
        corrections,
        (conflicting,),
    )

    for item in projected:
        if len(item.literals) == 3:
            source = checks[item.check_index]
            assert len(source) == 3
            assert len(item.touched) == 3
            assert all(len(variables) == 1 for _, variables in item.touched)
    return len(checks)


def literal_node(literal: Literal) -> int:
    variable, value = literal
    return 2 * variable + value


def negate_node(node: int) -> int:
    return node ^ 1


def implication_path(
    adjacency: tuple[tuple[tuple[int, int], ...], ...],
    start: int,
    target: int,
    component: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    queue = deque([start])
    previous: dict[int, tuple[int, int]] = {}
    seen = {start}
    while queue:
        node = queue.popleft()
        if node == target:
            break
        for neighbor, clause_index in adjacency[node]:
            if component[neighbor] != component[start] or neighbor in seen:
                continue
            seen.add(neighbor)
            previous[neighbor] = (node, clause_index)
            queue.append(neighbor)

    assert target in seen
    nodes = [target]
    clauses: list[int] = []
    while nodes[-1] != start:
        parent, clause_index = previous[nodes[-1]]
        clauses.append(clause_index)
        nodes.append(parent)
    nodes.reverse()
    clauses.reverse()
    return tuple(nodes), tuple(clauses)


def solve_2sat(
    variable_count: int,
    clauses: tuple[Clause, ...],
) -> dict[str, object]:
    """Solve a width-two formula and retain a contradictory-chain witness."""

    assert variable_count >= 0
    assert all(len(clause) <= 2 for clause in clauses)
    for index, clause in enumerate(clauses):
        if not clause:
            return {
                "satisfiable": False,
                "empty_clause": index,
            }

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(2 * variable_count)
    ]
    reverse: list[list[int]] = [[] for _ in adjacency]

    def add_implication(
        source: int,
        target: int,
        clause_index: int,
    ) -> None:
        adjacency[source].append((target, clause_index))
        reverse[target].append(source)

    for clause_index, clause in enumerate(clauses):
        for variable, value in clause:
            assert 0 <= variable < variable_count
            assert value in (0, 1)
        if len(clause) == 1:
            node = literal_node(clause[0])
            add_implication(negate_node(node), node, clause_index)
        else:
            left = literal_node(clause[0])
            right = literal_node(clause[1])
            add_implication(
                negate_node(left),
                right,
                clause_index,
            )
            add_implication(
                negate_node(right),
                left,
                clause_index,
            )

    visited = [False] * len(adjacency)
    order: list[int] = []

    def forward(node: int) -> None:
        visited[node] = True
        for neighbor, _ in adjacency[node]:
            if not visited[neighbor]:
                forward(neighbor)
        order.append(node)

    for node in range(len(adjacency)):
        if not visited[node]:
            forward(node)

    component = [-1] * len(adjacency)

    def backward(node: int, label: int) -> None:
        component[node] = label
        for neighbor in reverse[node]:
            if component[neighbor] < 0:
                backward(neighbor, label)

    label = 0
    for node in reversed(order):
        if component[node] < 0:
            backward(node, label)
            label += 1

    frozen_component = tuple(component)
    frozen_adjacency = tuple(tuple(edges) for edges in adjacency)
    for variable in range(variable_count):
        false_node = 2 * variable
        true_node = false_node + 1
        if component[false_node] == component[true_node]:
            forward_path = implication_path(
                frozen_adjacency,
                false_node,
                true_node,
                frozen_component,
            )
            backward_path = implication_path(
                frozen_adjacency,
                true_node,
                false_node,
                frozen_component,
            )
            return {
                "satisfiable": False,
                "variable": variable,
                "false_to_true": forward_path,
                "true_to_false": backward_path,
                "adjacency": frozen_adjacency,
            }

    assignment = tuple(
        int(component[2 * variable + 1] > component[2 * variable])
        for variable in range(variable_count)
    )
    assert all(clause_satisfied(clause, assignment) for clause in clauses)
    return {
        "satisfiable": True,
        "assignment": assignment,
    }


def brute_satisfiable(
    variable_count: int,
    clauses: tuple[Clause, ...],
) -> bool:
    return any(
        all(clause_satisfied(clause, assignment) for clause in clauses)
        for assignment in product((0, 1), repeat=variable_count)
    )


def verify_2sat_solver() -> int:
    variable_count = 3
    units = tuple(
        ((variable, value),)
        for variable in range(variable_count)
        for value in (0, 1)
    )
    binaries = tuple(
        ((left, left_value), (right, right_value))
        for left, right in combinations(range(variable_count), 2)
        for left_value, right_value in product((0, 1), repeat=2)
    )
    candidates = units + binaries

    checked = 0
    for clause_count in range(5):
        for clauses in combinations_with_replacement(candidates, clause_count):
            result = solve_2sat(variable_count, clauses)
            assert result["satisfiable"] == brute_satisfiable(
                variable_count,
                clauses,
            )
            checked += 1

    source_checks = tuple(
        dict(enumerate(values))
        for values in product((0, 1), repeat=2)
    )
    projected = build_protected_cnf(
        (0, 0),
        ({0: 1}, {1: 1}),
        source_checks,
    )
    contradictory = tuple(item.literals for item in projected)
    result = solve_2sat(2, contradictory)
    assert not result["satisfiable"]
    for key in ("false_to_true", "true_to_false"):
        nodes, clause_indices = result[key]
        assert len(nodes) == len(clause_indices) + 1
        adjacency = result["adjacency"]
        for source, target, clause_index in zip(
            nodes,
            nodes[1:],
            clause_indices,
        ):
            assert (target, clause_index) in adjacency[source]
            assert (
                projected[clause_index].check_index
                < len(source_checks)
            )

    fixed_bad = build_protected_cnf(
        (0,),
        (),
        ({0: 0},),
    )
    assert tuple(item.literals for item in fixed_bad) == ((),)
    empty = solve_2sat(
        0,
        tuple(item.literals for item in fixed_bad),
    )
    assert not empty["satisfiable"]
    assert empty["empty_clause"] == 0
    return checked


def verify_rank_three_boundary() -> int:
    current = (0, 0, 0)
    corrections = ({0: 1}, {1: 1}, {2: 1})
    checks = tuple(
        dict(enumerate(values))
        for values in product((0, 1), repeat=3)
    )
    projected = build_protected_cnf(current, corrections, checks)
    clauses = tuple(item.literals for item in projected)
    assert len(clauses) == 8
    assert all(len(clause) == 3 for clause in clauses)
    assert not brute_satisfiable(3, clauses)

    for item in projected:
        assert len(item.touched) == 3
        assert all(len(variables) == 1 for _, variables in item.touched)

    satisfiable_checks = checks[:-1]
    satisfiable_projected = build_protected_cnf(
        current,
        corrections,
        satisfiable_checks,
    )
    satisfiable_clauses = tuple(
        item.literals
        for item in satisfiable_projected
    )
    assert brute_satisfiable(3, satisfiable_clauses)
    return len(projected) + len(satisfiable_projected)


def main() -> None:
    ledgers = verify_exposure_ledger()
    snapshots = verify_snapshot_ledger()
    descents = verify_token_descent()
    support_families = verify_paid_disjoint_extraction()
    checks = verify_projection_exactness()
    formulas = verify_2sat_solver()
    rank_three = verify_rank_three_boundary()
    print(
        "phase signature recurrence verified:",
        f"{ledgers} ledgers,",
        f"{snapshots} snapshot traces,",
        f"{descents} descent transitions,",
        f"{support_families} support families,",
        f"{checks} source checks,",
        f"{formulas} 2-CNF formulas,",
        f"{rank_three} rank-three clauses",
    )


if __name__ == "__main__":
    main()
