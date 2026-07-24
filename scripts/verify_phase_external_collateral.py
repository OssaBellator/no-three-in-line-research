#!/usr/bin/env python3
"""Verify OP2n and OP3d--OP3f external collateral completion."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


Literal = tuple[int, int]
Check = tuple[Literal, ...]
Assignment = tuple[int, ...]
Projection = tuple[str, Check | None]


def assignments(sizes: tuple[int, ...]) -> tuple[Assignment, ...]:
    return tuple(product(*(range(size) for size in sizes)))


def scope(check: Check) -> frozenset[int]:
    return frozenset(variable for variable, _ in check)


def violated(check: Check, assignment: Assignment) -> bool:
    return all(
        assignment[variable] == label
        for variable, label in check
    )


def potential(
    checks: tuple[Check, ...],
    weights: tuple[int, ...],
    assignment: Assignment,
) -> int:
    return sum(
        weight
        for check, weight in zip(checks, weights)
        if violated(check, assignment)
    )


def canonical_checks(
    sizes: tuple[int, ...],
    ranks: tuple[int, ...] = (2, 3),
) -> tuple[Check, ...]:
    result: list[Check] = []
    for rank in ranks:
        if rank > len(sizes):
            continue
        for variables in combinations(range(len(sizes)), rank):
            for labels in product(*(range(sizes[v]) for v in variables)):
                result.append(tuple(zip(variables, labels)))
    return tuple(result)


def project_check(
    check: Check,
    action_domains: dict[int, frozenset[int]],
    fixed: Assignment,
) -> Projection:
    residual: list[Literal] = []
    for variable, label in check:
        if variable in action_domains:
            if label not in action_domains[variable]:
                return "satisfied", None
            residual.append((variable, label))
        elif fixed[variable] != label:
            return "satisfied", None
    if not residual:
        return "forced", None
    return "retained", tuple(residual)


def action_assignment(
    fixed: Assignment,
    action_variables: tuple[int, ...],
    values: tuple[int, ...],
) -> Assignment:
    result = list(fixed)
    for variable, value in zip(action_variables, values):
        result[variable] = value
    return tuple(result)


def projected_violation(
    projection: Projection,
    assignment: Assignment,
) -> bool:
    status, residual = projection
    if status == "satisfied":
        return False
    if status == "forced":
        return True
    assert residual is not None
    return violated(residual, assignment)


def verify_action_projection() -> None:
    sizes = (3, 3, 2, 2)
    universe = canonical_checks(sizes)
    action_variables = (1, 3)

    for current in assignments(sizes):
        for target in range(sizes[0]):
            if target == current[0]:
                continue
            action_domains = {
                variable: frozenset(
                    value
                    for value in range(sizes[variable])
                    if value != current[variable]
                )
                for variable in action_variables
            }
            fixed = list(current)
            fixed[0] = target
            fixed_assignment = tuple(fixed)
            projections = tuple(
                project_check(check, action_domains, fixed_assignment)
                for check in universe
            )

            action_value_tuples = tuple(
                product(
                    *(sorted(action_domains[v]) for v in action_variables)
                )
            )
            weights = tuple(
                1 + (5 * index + target) % 11
                for index in range(len(universe))
            )
            forced_weight = sum(
                weight
                for projection, weight in zip(projections, weights)
                if projection[0] == "forced"
            )

            for values in action_value_tuples:
                full = action_assignment(
                    fixed_assignment,
                    action_variables,
                    values,
                )
                for check, projection in zip(universe, projections):
                    assert violated(check, full) == projected_violation(
                        projection,
                        full,
                    )

                residual_weight = sum(
                    weight
                    for projection, weight in zip(projections, weights)
                    if projection[0] == "retained"
                    and projected_violation(projection, full)
                )
                assert potential(universe, weights, full) == (
                    forced_weight + residual_weight
                )

            hard = tuple(
                check
                for index, check in enumerate(universe)
                if (index + target) % 7 == 0
                and not violated(check, current)
            )
            hard_projections = tuple(
                project_check(check, action_domains, fixed_assignment)
                for check in hard
            )
            hard_forced = any(
                projection[0] == "forced"
                for projection in hard_projections
            )
            for values in action_value_tuples:
                full = action_assignment(
                    fixed_assignment,
                    action_variables,
                    values,
                )
                original_legal = all(
                    not violated(check, full)
                    for check in hard
                )
                projected_legal = (
                    not hard_forced
                    and all(
                        not projected_violation(projection, full)
                        for projection in hard_projections
                    )
                )
                assert original_legal == projected_legal

            selected_blockers = (
                (
                    (0, target),
                    (1, current[1]),
                    (2, current[2]),
                ),
                (
                    (0, target),
                    (3, current[3]),
                ),
            )
            for blocker in selected_blockers:
                projection = project_check(
                    blocker,
                    action_domains,
                    fixed_assignment,
                )
                assert projection[0] == "satisfied"


def correction(
    current: Assignment,
    support: tuple[int, ...],
) -> Assignment:
    result = list(current)
    for variable in support:
        result[variable] = 1 - result[variable]
    return tuple(result)


def correction_support(
    current: Assignment,
    candidate: Assignment,
) -> frozenset[int]:
    return frozenset(
        variable
        for variable in range(len(current))
        if current[variable] != candidate[variable]
    )


def conflict_edges(
    supports: tuple[frozenset[int], ...],
    checks: tuple[Check, ...],
) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for left, right in combinations(range(len(supports)), 2):
        if supports[left] & supports[right]:
            edges.add((left, right))
            continue
        if any(
            scope(check) & supports[left]
            and scope(check) & supports[right]
            for check in checks
        ):
            edges.add((left, right))
    return edges


def independent(
    chosen: tuple[int, ...],
    edges: set[tuple[int, int]],
) -> bool:
    return all(
        (min(left, right), max(left, right)) not in edges
        for left, right in combinations(chosen, 2)
    )


def joint_assignment(
    current: Assignment,
    candidates: tuple[Assignment, ...],
    chosen: tuple[int, ...],
) -> Assignment:
    result = list(current)
    occupied: set[int] = set()
    for index in chosen:
        support = correction_support(current, candidates[index])
        assert occupied.isdisjoint(support)
        occupied.update(support)
        for variable in support:
            result[variable] = candidates[index][variable]
    return tuple(result)


def verify_scope_complete_correction_graph() -> None:
    current = (0, 0, 0, 0)
    soft = (
        ((0, 1), (1, 1)),
        ((2, 0), (3, 0)),
        ((0, 1), (2, 1), (3, 1)),
        ((1, 0), (2, 1)),
        ((0, 0), (1, 0), (3, 0)),
    )
    weights = (3, 5, 7, 11, 13)
    hard = (
        ((0, 1), (3, 1)),
        ((1, 1), (2, 1), (3, 0)),
    )
    all_checks = hard + soft

    raw_candidates = tuple(
        correction(current, support)
        for rank in (1, 2)
        for support in combinations(range(len(current)), rank)
    )
    candidates = tuple(
        candidate
        for candidate in raw_candidates
        if all(not violated(check, candidate) for check in hard)
    )
    supports = tuple(
        correction_support(current, candidate)
        for candidate in candidates
    )
    edges = conflict_edges(supports, all_checks)
    base_potential = potential(soft, weights, current)
    deltas = tuple(
        potential(soft, weights, candidate) - base_potential
        for candidate in candidates
    )

    for mask in range(1 << len(candidates)):
        chosen = tuple(
            index
            for index in range(len(candidates))
            if mask & (1 << index)
        )
        if not independent(chosen, edges):
            continue
        joint = joint_assignment(current, candidates, chosen)
        assert all(not violated(check, joint) for check in hard)
        assert potential(soft, weights, joint) - base_potential == sum(
            deltas[index] for index in chosen
        )

    # Support overlap alone misses a cross-factor interaction.
    small_current = (0, 0)
    cross_check = (((0, 1), (1, 1)),)
    cross_weights = (1,)
    left = (1, 0)
    right = (0, 1)
    joint = (1, 1)
    base = potential(cross_check, cross_weights, small_current)
    left_delta = potential(cross_check, cross_weights, left) - base
    right_delta = potential(cross_check, cross_weights, right) - base
    joint_delta = potential(cross_check, cross_weights, joint) - base
    assert left_delta == right_delta == 0
    assert joint_delta == 1
    cross_supports = (
        correction_support(small_current, left),
        correction_support(small_current, right),
    )
    assert not (cross_supports[0] & cross_supports[1])
    assert conflict_edges(cross_supports, cross_check) == {(0, 1)}


def graph_edges(
    vertex_count: int,
    mask: int,
) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for index, edge in enumerate(combinations(range(vertex_count), 2)):
        if mask & (1 << index):
            edges.add(edge)
    return edges


def maximum_independent_weight(
    vertex_count: int,
    edges: set[tuple[int, int]],
    weights: tuple[int, ...],
    allowed: frozenset[int] | None = None,
) -> int:
    if allowed is None:
        allowed = frozenset(range(vertex_count))
    best = 0
    for mask in range(1 << vertex_count):
        chosen = tuple(
            vertex
            for vertex in range(vertex_count)
            if vertex in allowed and mask & (1 << vertex)
        )
        if independent(chosen, edges):
            best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_weighted_batch_bounds() -> None:
    for vertex_count in range(1, 6):
        edge_count = vertex_count * (vertex_count - 1) // 2
        for mask in range(1 << edge_count):
            edges = graph_edges(vertex_count, mask)
            weights = tuple(
                1 + (7 * vertex + 3 * mask) % 11
                for vertex in range(vertex_count)
            )
            degrees = tuple(
                sum(vertex in edge for edge in edges)
                for vertex in range(vertex_count)
            )
            optimum = maximum_independent_weight(
                vertex_count,
                edges,
                weights,
            )
            caro_wei = sum(
                (
                    Fraction(weights[vertex], degrees[vertex] + 1)
                    for vertex in range(vertex_count)
                ),
                Fraction(0),
            )
            assert optimum >= caro_wei

            total = sum(weights)
            for threshold in range(1, vertex_count + 2):
                high = frozenset(
                    vertex
                    for vertex in range(vertex_count)
                    if degrees[vertex] >= threshold
                )
                high_weight = sum(weights[vertex] for vertex in high)
                if 2 * high_weight > total:
                    continue
                low = frozenset(range(vertex_count)) - high
                low_optimum = maximum_independent_weight(
                    vertex_count,
                    edges,
                    weights,
                    low,
                )
                assert 2 * threshold * low_optimum >= total


def main() -> None:
    verify_action_projection()
    verify_scope_complete_correction_graph()
    verify_weighted_batch_bounds()
    print("OP external collateral completion: verified")


if __name__ == "__main__":
    main()
