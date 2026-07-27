#!/usr/bin/env python3
"""Finite checks for CMR1838--CMR1845."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
from random import Random

Edge = tuple[int, int]
Matching = tuple[Edge, ...]


def lcm(first: int, second: int) -> int:
    return first // gcd(first, second) * second


def perfect_matchings(side: int, allowed: set[Edge]) -> list[Matching]:
    output: list[Matching] = []
    for permutation in permutations(range(side)):
        matching = tuple((left, permutation[left]) for left in range(side))
        if all(edge in allowed for edge in matching):
            output.append(matching)
    return output


def contract_allowed(
    allowed: set[Edge],
    prescription: tuple[Edge, ...],
) -> set[Edge]:
    used_left = {left for left, _right in prescription}
    used_right = {right for _left, right in prescription}
    return {
        edge
        for edge in allowed
        if edge[0] not in used_left and edge[1] not in used_right
    }


def assignment_max(
    side: int,
    allowed: set[Edge],
    score: dict[Edge, Fraction],
    prescription: tuple[Edge, ...] = (),
) -> Fraction:
    used_left = {left for left, _right in prescription}
    used_right = {right for _left, right in prescription}
    left_vertices = [left for left in range(side) if left not in used_left]
    right_vertices = [right for right in range(side) if right not in used_right]
    best: Fraction | None = None
    for image in permutations(right_vertices):
        matching = tuple(zip(left_vertices, image))
        if all(edge in allowed for edge in matching):
            value = sum((score.get(edge, Fraction(0)) for edge in matching), Fraction(0))
            if best is None or value > best:
                best = value
    if best is None:
        raise ValueError("contracted host has no perfect matching")
    return best


def row_max_dual(
    side: int,
    allowed: set[Edge],
    score: dict[Edge, Fraction],
    prescription: tuple[Edge, ...] = (),
) -> tuple[dict[int, Fraction], dict[int, Fraction], Fraction]:
    used_left = {left for left, _right in prescription}
    used_right = {right for _left, right in prescription}
    left_vertices = [left for left in range(side) if left not in used_left]
    right_vertices = [right for right in range(side) if right not in used_right]
    left_potential = {
        left: max(
            (
                score.get((left, right), Fraction(0))
                for right in right_vertices
                if (left, right) in allowed
            ),
            default=Fraction(0),
        )
        for left in left_vertices
    }
    right_potential = {right: Fraction(0) for right in right_vertices}
    for left in left_vertices:
        for right in right_vertices:
            if (left, right) in allowed:
                assert (
                    left_potential[left] + right_potential[right]
                    >= score.get((left, right), Fraction(0))
                )
    objective = sum(left_potential.values(), Fraction(0))
    return left_potential, right_potential, objective


def main() -> None:
    random = Random(1838)
    systems = 0
    response_checks = 0
    label_linearity_checks = 0
    nested_checks = 0
    rational_dual_checks = 0
    integer_clearings = 0

    for _ in range(600):
        side = random.randint(3, 5)
        all_edges = {(left, right) for left in range(side) for right in range(side)}
        base_permutation = list(range(side))
        random.shuffle(base_permutation)
        allowed = {(left, base_permutation[left]) for left in range(side)}
        for edge in all_edges:
            if random.random() < 0.58:
                allowed.add(edge)
        responses = perfect_matchings(side, allowed)
        assert responses

        labels = range(random.randint(2, 4))
        weights = {label: random.randint(1, 6) for label in labels}
        denominator = random.randint(50, 180)
        selector_cap = random.randint(0, 4)

        edge_coefficients: dict[tuple[int, Edge], Fraction] = {}
        pair_coefficients: dict[tuple[int, frozenset[Edge]], Fraction] = {}
        triple_coefficients: dict[tuple[int, frozenset[Edge]], Fraction] = {}

        for label in labels:
            for edge in allowed:
                return_part = Fraction(random.randint(0, 2), denominator)
                selector_part = Fraction(random.randint(0, 2), denominator)
                rank_one = Fraction(random.randint(0, 2), denominator)
                edge_coefficients[label, edge] = (
                    return_part + selector_cap * selector_part + rank_one
                )

            for pair in combinations(sorted(allowed), 2):
                if len({edge[0] for edge in pair}) < 2:
                    continue
                if len({edge[1] for edge in pair}) < 2:
                    continue
                pair_coefficients[label, frozenset(pair)] = Fraction(
                    random.randint(0, 2), denominator
                )

            for triple in combinations(sorted(allowed), 3):
                if len({edge[0] for edge in triple}) < 3:
                    continue
                if len({edge[1] for edge in triple}) < 3:
                    continue
                triple_coefficients[label, frozenset(triple)] = Fraction(
                    random.randint(0, 1), denominator
                )

        weighted_edge = {
            edge: sum(
                (
                    weights[label] * edge_coefficients[label, edge]
                    for label in labels
                ),
                Fraction(0),
            )
            for edge in allowed
        }
        weighted_pair = {
            pair: sum(
                (
                    weights[label]
                    * pair_coefficients.get((label, pair), Fraction(0))
                    for label in labels
                ),
                Fraction(0),
            )
            for pair in {pair for _label, pair in pair_coefficients}
        }
        weighted_triple = {
            triple: sum(
                (
                    weights[label]
                    * triple_coefficients.get((label, triple), Fraction(0))
                    for label in labels
                ),
                Fraction(0),
            )
            for triple in {triple for _label, triple in triple_coefficients}
        }

        j_2: dict[Edge, Fraction] = {}
        for edge in allowed:
            residual = contract_allowed(allowed, (edge,))
            score = {
                other: weighted_pair.get(frozenset((edge, other)), Fraction(0))
                for other in residual
            }
            if residual:
                try:
                    j_2[edge] = assignment_max(side, residual, score, (edge,))
                except ValueError:
                    j_2[edge] = Fraction(0)
            else:
                j_2[edge] = Fraction(0)

        j_3: dict[tuple[Edge, Edge], Fraction] = {}
        for edge in allowed:
            residual_after_edge = contract_allowed(allowed, (edge,))
            for other in residual_after_edge:
                residual = contract_allowed(allowed, (edge, other))
                score = {
                    third: weighted_triple.get(
                        frozenset((edge, other, third)), Fraction(0)
                    )
                    for third in residual
                }
                if residual:
                    try:
                        j_3[edge, other] = assignment_max(
                            side, residual, score, (edge, other)
                        )
                    except ValueError:
                        j_3[edge, other] = Fraction(0)
                else:
                    j_3[edge, other] = Fraction(0)

        h_3: dict[Edge, Fraction] = {}
        for edge in allowed:
            residual = contract_allowed(allowed, (edge,))
            score = {
                other: j_3.get((edge, other), Fraction(0))
                for other in residual
            }
            if residual:
                try:
                    h_3[edge] = assignment_max(side, residual, score, (edge,))
                except ValueError:
                    h_3[edge] = Fraction(0)
            else:
                h_3[edge] = Fraction(0)

        gamma = {
            edge: weighted_edge[edge] + j_2[edge] / 2 + h_3[edge] / 6
            for edge in allowed
        }

        for response in responses:
            labelled_total = Fraction(0)
            for label in labels:
                label_count = sum(
                    (edge_coefficients[label, edge] for edge in response),
                    Fraction(0),
                )
                label_count += sum(
                    (
                        pair_coefficients.get((label, frozenset(pair)), Fraction(0))
                        for pair in combinations(response, 2)
                    ),
                    Fraction(0),
                )
                label_count += sum(
                    (
                        triple_coefficients.get(
                            (label, frozenset(triple)), Fraction(0)
                        )
                        for triple in combinations(response, 3)
                    ),
                    Fraction(0),
                )
                labelled_total += weights[label] * label_count

            aggregated_total = sum(
                (weighted_edge[edge] for edge in response), Fraction(0)
            )
            aggregated_total += sum(
                (
                    weighted_pair.get(frozenset(pair), Fraction(0))
                    for pair in combinations(response, 2)
                ),
                Fraction(0),
            )
            aggregated_total += sum(
                (
                    weighted_triple.get(frozenset(triple), Fraction(0))
                    for triple in combinations(response, 3)
                ),
                Fraction(0),
            )
            assert labelled_total == aggregated_total
            label_linearity_checks += 1

            gamma_score = sum((gamma[edge] for edge in response), Fraction(0))
            assert aggregated_total <= gamma_score
            response_checks += 1

        outer_max = assignment_max(side, allowed, gamma)
        for response in responses:
            assert sum((gamma[edge] for edge in response), Fraction(0)) <= outer_max
            nested_checks += 1

        _left, _right, dual_objective = row_max_dual(side, allowed, gamma)
        assert outer_max <= dual_objective
        rational_dual_checks += 1

        parent_budget = dual_objective + Fraction(1, denominator)
        assert dual_objective < parent_budget

        common_denominator = 1
        for value in list(gamma.values()) + [dual_objective, parent_budget]:
            common_denominator = lcm(common_denominator, value.denominator)
        integer_objective = dual_objective * common_denominator
        integer_budget = parent_budget * common_denominator
        assert integer_objective.denominator == 1
        assert integer_budget.denominator == 1
        assert integer_objective < integer_budget
        integer_clearings += 1
        systems += 1

    print(
        "verified label-weighted unified assignment LP: "
        f"{systems} labelled systems, {response_checks} response bounds, "
        f"{label_linearity_checks} label-linearization checks, "
        f"{nested_checks} outer-assignment checks, {rational_dual_checks} "
        f"rational duals and {integer_clearings} denominator clearings"
    )


if __name__ == "__main__":
    main()
