#!/usr/bin/env python3
"""Verify OP4d--OP4f implication and rank-three frontier reductions."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import gcd

try:
    from scripts.verify_phase_signature_recurrence import (
        Clause,
        ProjectedClause,
        brute_satisfiable,
        build_protected_cnf,
        clause_satisfied,
        literal_node,
        negate_node,
        solve_2sat,
    )
except ModuleNotFoundError:
    from verify_phase_signature_recurrence import (  # type: ignore[no-redef]
        Clause,
        ProjectedClause,
        brute_satisfiable,
        build_protected_cnf,
        clause_satisfied,
        literal_node,
        negate_node,
        solve_2sat,
    )


@dataclass(frozen=True)
class ImplicationEdge:
    source: int
    target: int
    clause_index: int
    source_factor: int
    touched: tuple[tuple[int, tuple[int, ...]], ...]


@dataclass(frozen=True)
class ImplicationBicycle:
    variable: int
    false_to_true: tuple[int, ...]
    true_to_false: tuple[int, ...]
    walk_nodes: tuple[int, ...]
    edges: tuple[ImplicationEdge, ...]


def clause_implications(clause: Clause) -> tuple[tuple[int, int], ...]:
    assert 1 <= len(clause) <= 2
    if len(clause) == 1:
        node = literal_node(clause[0])
        return ((negate_node(node), node),)
    left = literal_node(clause[0])
    right = literal_node(clause[1])
    return (
        (negate_node(left), right),
        (negate_node(right), left),
    )


def extract_implication_bicycle(
    result: dict[str, object],
    clauses: tuple[Clause, ...],
    projected: tuple[ProjectedClause, ...] | None = None,
    source_indices: tuple[int, ...] | None = None,
) -> ImplicationBicycle:
    """Compress a nonempty-clause 2-SAT obstruction to two simple paths."""

    assert not result["satisfiable"]
    assert "empty_clause" not in result
    variable = int(result["variable"])
    forward_nodes, forward_clauses = result["false_to_true"]
    backward_nodes, backward_clauses = result["true_to_false"]
    forward_nodes = tuple(forward_nodes)
    backward_nodes = tuple(backward_nodes)
    forward_clauses = tuple(forward_clauses)
    backward_clauses = tuple(backward_clauses)

    false_node = 2 * variable
    true_node = false_node + 1
    assert forward_nodes[0] == false_node
    assert forward_nodes[-1] == true_node
    assert backward_nodes[0] == true_node
    assert backward_nodes[-1] == false_node
    assert len(set(forward_nodes)) == len(forward_nodes)
    assert len(set(backward_nodes)) == len(backward_nodes)
    assert len(forward_clauses) == len(forward_nodes) - 1
    assert len(backward_clauses) == len(backward_nodes) - 1

    walk_nodes = forward_nodes + backward_nodes[1:]
    clause_trace = forward_clauses + backward_clauses
    assert walk_nodes[0] == walk_nodes[-1]
    assert len(clause_trace) == len(walk_nodes) - 1

    variable_count = max(
        (
            variable_index
            for clause in clauses
            for variable_index, _ in clause
        ),
        default=-1,
    ) + 1
    assert len(forward_clauses) <= 2 * variable_count - 1
    assert len(backward_clauses) <= 2 * variable_count - 1

    edges: list[ImplicationEdge] = []
    for source, target, clause_index in zip(
        walk_nodes,
        walk_nodes[1:],
        clause_trace,
    ):
        assert (source, target) in clause_implications(clauses[clause_index])
        if projected is None:
            source_factor = (
                source_indices[clause_index]
                if source_indices is not None
                else clause_index
            )
            touched: tuple[tuple[int, tuple[int, ...]], ...] = ()
        else:
            source_factor = projected[clause_index].check_index
            touched = projected[clause_index].touched
        edges.append(
            ImplicationEdge(
                source=source,
                target=target,
                clause_index=clause_index,
                source_factor=source_factor,
                touched=touched,
            )
        )

    return ImplicationBicycle(
        variable=variable,
        false_to_true=forward_nodes,
        true_to_false=backward_nodes,
        walk_nodes=walk_nodes,
        edges=tuple(edges),
    )


def generated_ratio_subgroup(
    colours: tuple[int, ...],
    order: int,
) -> frozenset[int]:
    assert colours
    base = colours[0] % order
    step = order
    for colour in colours:
        step = gcd(step, (colour - base) % order)
    return frozenset(
        multiple * step % order
        for multiple in range(order // step)
    )


def additive_coset(
    representative: int,
    subgroup: frozenset[int],
    order: int,
) -> frozenset[int]:
    return frozenset(
        (representative + element) % order
        for element in subgroup
    )


def audit_rational_bicycle(
    bicycle: ImplicationBicycle,
    literal_cosets: dict[int, int],
    edge_colours: tuple[int | None, ...],
    root_colour: int,
    quotient_order: int,
    weights: tuple[Fraction, ...] | None = None,
) -> dict[str, object]:
    """Audit the RI2k quotient law and classify its colour-ratio subgroup."""

    assert quotient_order >= 1
    assert len(edge_colours) == len(bicycle.edges)
    if weights is None:
        weights = tuple(Fraction(1) for _ in bicycle.edges)
    assert len(weights) == len(bicycle.edges)
    assert all(weight >= 0 for weight in weights)

    for index, node in enumerate(bicycle.walk_nodes[:-1]):
        if node not in literal_cosets:
            return {
                "status": "unlabelled",
                "edge_index": index,
                "node": node,
                "source_factor": bicycle.edges[index].source_factor,
            }

    normalized_vertices = tuple(
        literal_cosets[node] % quotient_order
        for node in bicycle.walk_nodes
    )
    assert normalized_vertices[0] == normalized_vertices[-1]

    colours: list[int] = []
    for index, (left, right, colour) in enumerate(
        zip(
            normalized_vertices,
            normalized_vertices[1:],
            edge_colours,
        )
    ):
        if colour is None:
            return {
                "status": "unlabelled",
                "edge_index": index,
                "source_factor": bicycle.edges[index].source_factor,
            }
        normalized_colour = colour % quotient_order
        expected = (
            root_colour + normalized_colour - left
        ) % quotient_order
        if right != expected:
            return {
                "status": "invalid",
                "edge_index": index,
                "source_factor": bicycle.edges[index].source_factor,
                "expected": expected,
                "actual": right,
            }
        colours.append(normalized_colour)

    frozen_colours = tuple(colours)
    subgroup = generated_ratio_subgroup(
        frozen_colours,
        quotient_order,
    )
    base_colour = frozen_colours[0]
    even_coset = additive_coset(
        normalized_vertices[0],
        subgroup,
        quotient_order,
    )
    odd_coset = additive_coset(
        root_colour - normalized_vertices[0] + base_colour,
        subgroup,
        quotient_order,
    )
    assert set(normalized_vertices[0::2]) <= even_coset
    assert set(normalized_vertices[1::2]) <= odd_coset
    assert set(frozen_colours) <= additive_coset(
        base_colour,
        subgroup,
        quotient_order,
    )

    result: dict[str, object] = {
        "status": "certified",
        "subgroup": subgroup,
        "subgroup_order": len(subgroup),
        "even_coset": even_coset,
        "odd_coset": odd_coset,
    }

    if len(subgroup) == 1:
        assert len(set(normalized_vertices)) <= 2
        result["classification"] = "one_colour"
        return result

    if len(subgroup) != 2:
        result["classification"] = "ratio_growth"
        return result

    omega = next(element for element in subgroup if element != 0)
    assert quotient_order % 2 == 0
    assert 2 * omega % quotient_order == 0
    source_a = normalized_vertices[0]
    source_b = (
        root_colour + base_colour - source_a
    ) % quotient_order
    a_coset = additive_coset(source_a, subgroup, quotient_order)
    b_coset = additive_coset(source_b, subgroup, quotient_order)
    template_vertices = a_coset | b_coset
    assert set(normalized_vertices) <= template_vertices

    edge_classes: dict[
        tuple[int, int, int],
        Fraction,
    ] = {}
    for left, right, colour, weight in zip(
        normalized_vertices,
        normalized_vertices[1:],
        frozen_colours,
        weights,
    ):
        edge_class = (min(left, right), max(left, right), colour)
        edge_classes[edge_class] = edge_classes.get(
            edge_class,
            Fraction(),
        ) + weight

    if a_coset != b_coset:
        classification = "alternating_square"
        capacity = 4
    else:
        classification = "loop_edge_collapse"
        capacity = 3
    assert len(edge_classes) <= capacity

    total_weight = sum(weights, Fraction())
    selected_class, selected_weight = max(
        edge_classes.items(),
        key=lambda item: (item[1], item[0]),
    )
    assert selected_weight * capacity >= total_weight
    colour_load: dict[int, Fraction] = {}
    for colour, weight in zip(frozen_colours, weights):
        colour_load[colour] = colour_load.get(
            colour,
            Fraction(),
        ) + weight
    assert max(colour_load.values()) * 2 >= total_weight

    result.update(
        {
            "classification": classification,
            "omega": omega,
            "template_vertices": template_vertices,
            "edge_classes": edge_classes,
            "selected_edge_class": selected_class,
            "selected_edge_weight": selected_weight,
            "total_weight": total_weight,
        }
    )
    return result


def maximal_rank_three_matching(
    clauses: tuple[Clause, ...],
) -> tuple[int, ...]:
    selected: list[int] = []
    used: set[int] = set()
    for index, clause in enumerate(clauses):
        if len(clause) != 3:
            continue
        scope = {variable for variable, _ in clause}
        assert len(scope) == 3
        if scope.isdisjoint(used):
            selected.append(index)
            used.update(scope)
    return tuple(selected)


def simplify_clause(
    clause: Clause,
    fixed: dict[int, int],
) -> Clause | None:
    residual: list[tuple[int, int]] = []
    for variable, value in clause:
        if variable in fixed:
            if fixed[variable] == value:
                return None
        else:
            residual.append((variable, value))
    return tuple(residual)


def solve_rank_three_kernel(
    variable_count: int,
    clauses: tuple[Clause, ...],
) -> dict[str, object]:
    """Condition a maximal rank-three matching kernel and solve by 2-SAT."""

    assert all(len(clause) <= 3 for clause in clauses)
    matching = maximal_rank_three_matching(clauses)
    matching_scopes = tuple(
        frozenset(variable for variable, _ in clauses[index])
        for index in matching
    )
    assert all(
        left.isdisjoint(right)
        for left, right in combinations(matching_scopes, 2)
    )
    kernel = tuple(sorted(set().union(*matching_scopes))) if matching else ()

    for clause in clauses:
        if len(clause) == 3:
            assert any(variable in kernel for variable, _ in clause)

    obstructions: list[dict[str, object]] = []
    for values in product((0, 1), repeat=len(kernel)):
        fixed = dict(zip(kernel, values))
        residual: list[Clause] = []
        source_indices: list[int] = []
        for source_index, clause in enumerate(clauses):
            simplified = simplify_clause(clause, fixed)
            if simplified is None:
                continue
            assert len(simplified) <= 2
            residual.append(simplified)
            source_indices.append(source_index)

        frozen_residual = tuple(residual)
        result = solve_2sat(variable_count, frozen_residual)
        if result["satisfiable"]:
            assignment = list(result["assignment"])
            for variable, value in fixed.items():
                assignment[variable] = value
            frozen_assignment = tuple(assignment)
            assert all(
                clause_satisfied(clause, frozen_assignment)
                for clause in clauses
            )
            return {
                "satisfiable": True,
                "assignment": frozen_assignment,
                "matching": matching,
                "kernel": kernel,
                "conditioned_branches": len(obstructions) + 1,
            }

        obstruction: dict[str, object] = {
            "fixed": tuple(sorted(fixed.items())),
            "source_indices": tuple(source_indices),
        }
        if "empty_clause" in result:
            residual_index = int(result["empty_clause"])
            obstruction.update(
                {
                    "kind": "empty",
                    "source_clause": source_indices[residual_index],
                }
            )
        else:
            bicycle = extract_implication_bicycle(
                result,
                frozen_residual,
                source_indices=tuple(source_indices),
            )
            obstruction.update(
                {
                    "kind": "bicycle",
                    "bicycle": bicycle,
                }
            )
        obstructions.append(obstruction)

    assert len(obstructions) == 2 ** len(kernel)
    return {
        "satisfiable": False,
        "matching": matching,
        "kernel": kernel,
        "conditioned_branches": len(obstructions),
        "obstructions": tuple(obstructions),
    }


def verify_implication_bicycles() -> int:
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
    for clause_count in range(1, 5):
        for clauses in combinations_with_replacement(
            candidates,
            clause_count,
        ):
            result = solve_2sat(variable_count, clauses)
            if result["satisfiable"] or "empty_clause" in result:
                continue
            bicycle = extract_implication_bicycle(result, clauses)
            assert bicycle.walk_nodes[0] == bicycle.walk_nodes[-1]
            assert len(bicycle.edges) <= 4 * variable_count - 2
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
    clauses = tuple(item.literals for item in projected)
    result = solve_2sat(2, clauses)
    bicycle = extract_implication_bicycle(
        result,
        clauses,
        projected=projected,
    )
    assert all(
        edge.source_factor == projected[edge.clause_index].check_index
        for edge in bicycle.edges
    )
    assert all(edge.touched for edge in bicycle.edges)
    return checked + 1


def rational_test_bicycle() -> ImplicationBicycle:
    source_checks = tuple(
        dict(enumerate(values))
        for values in product((0, 1), repeat=2)
    )
    projected = build_protected_cnf(
        (0, 0),
        ({0: 1}, {1: 1}),
        source_checks,
    )
    clauses = tuple(item.literals for item in projected)
    return extract_implication_bicycle(
        solve_2sat(2, clauses),
        clauses,
        projected=projected,
    )


def colours_from_vertices(
    bicycle: ImplicationBicycle,
    literal_cosets: dict[int, int],
    root_colour: int,
    order: int,
) -> tuple[int, ...]:
    return tuple(
        (
            literal_cosets[edge.source]
            + literal_cosets[edge.target]
            - root_colour
        )
        % order
        for edge in bicycle.edges
    )


def verify_rational_gate() -> int:
    bicycle = rational_test_bicycle()
    weights = tuple(
        Fraction(index + 1)
        for index in range(len(bicycle.edges))
    )

    square_cosets = {0: 0, 1: 4, 2: 5, 3: 1}
    square_colours = colours_from_vertices(
        bicycle,
        square_cosets,
        0,
        8,
    )
    square = audit_rational_bicycle(
        bicycle,
        square_cosets,
        square_colours,
        0,
        8,
        weights,
    )
    assert square["classification"] == "alternating_square"
    assert square["subgroup_order"] == 2

    collapsed_cosets = {0: 0, 1: 4, 2: 4, 3: 0}
    collapsed_colours = colours_from_vertices(
        bicycle,
        collapsed_cosets,
        0,
        8,
    )
    collapsed = audit_rational_bicycle(
        bicycle,
        collapsed_cosets,
        collapsed_colours,
        0,
        8,
        weights,
    )
    assert collapsed["classification"] == "loop_edge_collapse"
    assert collapsed["subgroup_order"] == 2

    growth_cosets = {0: 0, 1: 1, 2: 5, 3: 2}
    growth_colours = colours_from_vertices(
        bicycle,
        growth_cosets,
        0,
        7,
    )
    growth = audit_rational_bicycle(
        bicycle,
        growth_cosets,
        growth_colours,
        0,
        7,
    )
    assert growth["classification"] == "ratio_growth"
    assert growth["subgroup_order"] == 7

    one_colour_cosets = {0: 0, 1: 0, 2: 1, 3: 1}
    one_colour_colours = colours_from_vertices(
        bicycle,
        one_colour_cosets,
        0,
        8,
    )
    one_colour = audit_rational_bicycle(
        bicycle,
        one_colour_cosets,
        one_colour_colours,
        0,
        8,
        weights,
    )
    assert one_colour["classification"] == "one_colour"

    missing_colours = tuple(
        None if index == 1 else colour
        for index, colour in enumerate(square_colours)
    )
    missing = audit_rational_bicycle(
        bicycle,
        square_cosets,
        missing_colours,
        0,
        8,
        weights,
    )
    assert missing["status"] == "unlabelled"
    assert missing["edge_index"] == 1

    invalid_colours = list(square_colours)
    invalid_colours[0] = (invalid_colours[0] + 1) % 8
    invalid = audit_rational_bicycle(
        bicycle,
        square_cosets,
        tuple(invalid_colours),
        0,
        8,
        weights,
    )
    assert invalid["status"] == "invalid"
    assert invalid["edge_index"] == 0
    return 6


def rank_three_candidates(variable_count: int) -> tuple[Clause, ...]:
    return tuple(
        tuple(zip(scope, values))
        for scope in combinations(range(variable_count), 3)
        for values in product((0, 1), repeat=3)
    )


def verify_rank_three_kernel() -> int:
    checked = 0
    triples_three = rank_three_candidates(3)
    for mask in range(1 << len(triples_three)):
        clauses = tuple(
            clause
            for index, clause in enumerate(triples_three)
            if mask & (1 << index)
        )
        result = solve_rank_three_kernel(3, clauses)
        assert result["satisfiable"] == brute_satisfiable(3, clauses)
        checked += 1

    triples_four = rank_three_candidates(4)
    units = tuple(
        ((variable, value),)
        for variable in range(4)
        for value in (0, 1)
    )
    binaries = tuple(
        ((left, left_value), (right, right_value))
        for left, right in combinations(range(4), 2)
        for left_value, right_value in product((0, 1), repeat=2)
    )
    for triple_count in range(1, 4):
        for index, selected in enumerate(
            combinations(triples_four, triple_count)
        ):
            extras: tuple[Clause, ...] = ()
            if index % 2 == 0:
                extras += (units[index % len(units)],)
            if index % 3 == 0:
                extras += (binaries[index % len(binaries)],)
            clauses = tuple(selected) + extras
            result = solve_rank_three_kernel(4, clauses)
            assert result["satisfiable"] == brute_satisfiable(4, clauses)
            checked += 1

    all_orientations = tuple(
        tuple((variable, 1 - value) for variable, value in enumerate(values))
        for values in product((0, 1), repeat=3)
    )
    impossible = solve_rank_three_kernel(3, all_orientations)
    assert not impossible["satisfiable"]
    assert impossible["conditioned_branches"] == 8
    assert all(
        obstruction["kind"] == "empty"
        for obstruction in impossible["obstructions"]
    )

    contradictory_binary = (
        ((0, 1), (1, 1)),
        ((0, 1), (1, 0)),
        ((0, 0), (1, 1)),
        ((0, 0), (1, 0)),
    )
    separate_triple = (
        (2, 1),
        (3, 1),
        (4, 1),
    )
    mixed = solve_rank_three_kernel(
        5,
        (separate_triple,) + contradictory_binary,
    )
    assert not mixed["satisfiable"]
    assert any(
        obstruction["kind"] == "bicycle"
        for obstruction in mixed["obstructions"]
    )

    disjoint = (
        ((0, 1), (1, 1), (2, 1)),
        ((3, 1), (4, 1), (5, 1)),
    )
    disjoint_result = solve_rank_three_kernel(6, disjoint)
    assert len(disjoint_result["matching"]) == 2
    matching_scopes = [
        {variable for variable, _ in disjoint[index]}
        for index in disjoint_result["matching"]
    ]
    assert matching_scopes[0].isdisjoint(matching_scopes[1])
    return checked + 3


def main() -> None:
    bicycles = verify_implication_bicycles()
    rational_cases = verify_rational_gate()
    rank_three = verify_rank_three_kernel()
    print(
        "phase implication bridge verified:",
        f"{bicycles} contradiction bicycles,",
        f"{rational_cases} rational-gate cases,",
        f"{rank_three} rank-three formulas",
    )


if __name__ == "__main__":
    main()
