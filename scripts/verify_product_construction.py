#!/usr/bin/env python3
"""Exact checks and SAT search for mixed-radix product constructions.

The script verifies:

* cycle-phase products are saturated for all four radix orientations;
* the general coarse/fine determinant identity;
* an explicit 2x3 pair defeats every cycle phase and all four orientations;
* phase feasibility is exactly a width-three CNF problem;
* exhaustive counts for selected small factor sizes.

This is a finite sanity check and falsification tool, not a proof for arbitrary
side lengths.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from typing import Iterator

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]
PhaseState = tuple[tuple[tuple[int, ...], ...], ...]
Clause = tuple[int, ...]
Orientation = str

ORIENTATIONS: tuple[Orientation, ...] = ("cc", "cf", "fc", "ff")


@dataclass(frozen=True)
class EncodedPoint:
    x: int
    y: int
    coarse: Point
    fine: Point
    outer_layer: int
    inner_layer: int

    @property
    def flat(self) -> Point:
        return (self.x, self.y)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def first_collinear(points: list[Point]) -> tuple[Point, Point, Point] | None:
    for triple in combinations(points, 3):
        if determinant(*triple) == 0:
            return triple
    return None


def is_no_three(points: list[Point]) -> bool:
    return first_collinear(points) is None


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    """Return ordered two-permutation decompositions that are no-three."""
    result: list[FactorPair] = []
    all_permutations = tuple(permutations(range(n)))
    for sigma_0 in all_permutations:
        for sigma_1 in all_permutations:
            if any(sigma_0[x] == sigma_1[x] for x in range(n)):
                continue
            points = [(x, sigma_0[x]) for x in range(n)]
            points.extend((x, sigma_1[x]) for x in range(n))
            if is_no_three(points):
                result.append((sigma_0, sigma_1))
    return tuple(result)


def transition_cycles(
    tau_0: Permutation,
    tau_1: Permutation,
) -> tuple[tuple[int, ...], ...]:
    """Orbits of tau_1^{-1} tau_0 on fine-row indices."""
    n = len(tau_0)
    inverse_1 = [0] * n
    for u, value in enumerate(tau_1):
        inverse_1[value] = u
    transition = [inverse_1[tau_0[u]] for u in range(n)]

    seen = [False] * n
    cycles: list[tuple[int, ...]] = []
    for start in range(n):
        if seen[start]:
            continue
        orbit: list[int] = []
        u = start
        while not seen[u]:
            seen[u] = True
            orbit.append(u)
            u = transition[u]
        cycles.append(tuple(orbit))
    return tuple(cycles)


def phase_states(m: int, cycle_count: int) -> Iterator[PhaseState]:
    for bits in product((0, 1), repeat=2 * m * cycle_count):
        yield tuple(
            tuple(
                tuple(
                    bits[
                        (r * m + i) * cycle_count :
                        (r * m + i + 1) * cycle_count
                    ]
                )
                for i in range(m)
            )
            for r in (0, 1)
        )


def flatten_coordinate(
    coarse_digit: int,
    fine_digit: int,
    coarse_side: int,
    fine_side: int,
    mode: str,
) -> int:
    if mode == "c":
        return fine_side * coarse_digit + fine_digit
    if mode == "f":
        return coarse_side * fine_digit + coarse_digit
    raise ValueError(f"unknown radix mode {mode!r}")


def cycle_phase_product(
    outer: FactorPair,
    inner: FactorPair,
    phases: PhaseState,
    orientation: Orientation,
) -> tuple[list[EncodedPoint], list[EncodedPoint]]:
    """Construct two permutation layers in one of the four radix orientations."""
    if orientation not in ORIENTATIONS:
        raise ValueError(f"orientation must be one of {ORIENTATIONS}")

    m = len(outer[0])
    n = len(inner[0])
    cycles = transition_cycles(*inner)
    cycle_id = [0] * n
    for index, orbit in enumerate(cycles):
        for u in orbit:
            cycle_id[u] = index

    layers: tuple[list[EncodedPoint], list[EncodedPoint]] = ([], [])
    for r in (0, 1):
        for i in range(m):
            for u in range(n):
                s = phases[r][i][cycle_id[u]]
                j = outer[r][i]
                v = inner[s][u]
                layers[r].append(
                    EncodedPoint(
                        x=flatten_coordinate(i, u, m, n, orientation[0]),
                        y=flatten_coordinate(j, v, m, n, orientation[1]),
                        coarse=(i, j),
                        fine=(u, v),
                        outer_layer=r,
                        inner_layer=s,
                    )
                )
    return layers


def verify_saturation(layers: tuple[list[EncodedPoint], list[EncodedPoint]]) -> None:
    side = len(layers[0])
    assert len(layers[1]) == side
    for layer in layers:
        assert sorted(point.x for point in layer) == list(range(side))
        assert sorted(point.y for point in layer) == list(range(side))

    all_cells = [point.flat for layer in layers for point in layer]
    assert len(all_cells) == 2 * side
    assert len(set(all_cells)) == 2 * side

    row_counts = [0] * side
    column_counts = [0] * side
    for x, y in all_cells:
        row_counts[x] += 1
        column_counts[y] += 1
    assert row_counts == [2] * side
    assert column_counts == [2] * side


def orientation_coefficients(
    m: int,
    n: int,
    orientation: Orientation,
) -> tuple[int, int, int, int]:
    """Return coefficients (a_i, a_u, a_j, a_v)."""
    a_i, a_u = (n, 1) if orientation[0] == "c" else (1, m)
    a_j, a_v = (n, 1) if orientation[1] == "c" else (1, m)
    return a_i, a_u, a_j, a_v


def verify_determinant_identity(
    layers: tuple[list[EncodedPoint], list[EncodedPoint]],
    m: int,
    n: int,
    orientation: Orientation,
) -> None:
    a_i, a_u, a_j, a_v = orientation_coefficients(m, n, orientation)
    points = layers[0] + layers[1]
    for a, b, c in combinations(points, 3):
        coarse = determinant(a.coarse, b.coarse, c.coarse)
        fine = determinant(a.fine, b.fine, c.fine)

        di_b = b.coarse[0] - a.coarse[0]
        dj_b = b.coarse[1] - a.coarse[1]
        du_b = b.fine[0] - a.fine[0]
        dv_b = b.fine[1] - a.fine[1]
        di_c = c.coarse[0] - a.coarse[0]
        dj_c = c.coarse[1] - a.coarse[1]
        du_c = c.fine[0] - a.fine[0]
        dv_c = c.fine[1] - a.fine[1]

        cross_iv = di_b * dv_c - dv_b * di_c
        cross_uj = du_b * dj_c - dj_b * du_c
        flat = determinant(a.flat, b.flat, c.flat)
        expected = (
            a_i * a_j * coarse
            + a_i * a_v * cross_iv
            + a_u * a_j * cross_uj
            + a_u * a_v * fine
        )
        assert flat == expected

        if orientation == "cc" and flat == 0:
            assert fine % n == 0
            carry = fine // n
            assert abs(carry) <= n - 2
            assert n * coarse + cross_iv + cross_uj + carry == 0


def explicit_all_orientation_counterexample() -> None:
    outer: FactorPair = ((0, 1), (1, 0))
    inner: FactorPair = ((0, 2, 1), (1, 0, 2))
    failures = 0
    for orientation in ORIENTATIONS:
        for bits in product((0, 1), repeat=4):
            phases: PhaseState = (
                ((bits[0],), (bits[1],)),
                ((bits[2],), (bits[3],)),
            )
            layers = cycle_phase_product(outer, inner, phases, orientation)
            verify_saturation(layers)
            verify_determinant_identity(layers, 2, 3, orientation)
            cells = [point.flat for layer in layers for point in layer]
            assert first_collinear(cells) is not None
            failures += 1
    assert failures == 64
    print("explicit 2x3 obstruction: all 64 phase/orientation states fail")


def canonical_clauses(clauses: Iterator[Clause] | tuple[Clause, ...]) -> tuple[Clause, ...]:
    normalized = {
        tuple(sorted(clause, key=lambda literal: (abs(literal), literal)))
        for clause in clauses
    }
    return tuple(sorted(normalized, key=lambda clause: (len(clause), clause)))


def phase_cnf(
    outer: FactorPair,
    inner: FactorPair,
    orientation: Orientation,
) -> tuple[int, tuple[Clause, ...]]:
    """Build the exact width-three CNF excluding every collinear triple."""
    m = len(outer[0])
    n = len(inner[0])
    cycles = transition_cycles(*inner)
    cycle_id = [0] * n
    for index, orbit in enumerate(cycles):
        for u in orbit:
            cycle_id[u] = index

    variable_index: dict[tuple[int, int, int], int] = {}
    variable_count = 0
    for r in (0, 1):
        for i in range(m):
            for cycle in range(len(cycles)):
                variable_index[(r, i, cycle)] = variable_count
                variable_count += 1

    positions: list[tuple[int, tuple[int, int], int]] = []
    for r in (0, 1):
        for i in range(m):
            j = outer[r][i]
            for u in range(n):
                x = flatten_coordinate(i, u, m, n, orientation[0])
                y_values = tuple(
                    flatten_coordinate(j, inner[s][u], m, n, orientation[1])
                    for s in (0, 1)
                )
                variable = variable_index[(r, i, cycle_id[u])]
                positions.append((x, y_values, variable))

    clauses: set[Clause] = set()
    for indices in combinations(range(len(positions)), 3):
        variables = sorted({positions[index][2] for index in indices})
        for bits in product((0, 1), repeat=len(variables)):
            assignment = dict(zip(variables, bits))
            points = [
                (
                    positions[index][0],
                    positions[index][1][assignment[positions[index][2]]],
                )
                for index in indices
            ]
            if determinant(*points) != 0:
                continue
            clause = tuple(
                sorted(
                    (
                        variable + 1
                        if assignment[variable] == 0
                        else -(variable + 1)
                    )
                    for variable in variables
                )
            )
            clauses.add(clause)

    return variable_count, canonical_clauses(tuple(clauses))


def simplify_one(
    clauses: tuple[Clause, ...],
    variable: int,
    value: int,
) -> tuple[Clause, ...] | None:
    satisfying_literal = variable + 1 if value == 1 else -(variable + 1)
    falsified_literal = -satisfying_literal
    result: list[Clause] = []
    for clause in clauses:
        if satisfying_literal in clause:
            continue
        reduced = tuple(literal for literal in clause if literal != falsified_literal)
        if not reduced:
            return None
        result.append(reduced)
    return canonical_clauses(tuple(result))


def count_cnf_solutions(variable_count: int, clauses: tuple[Clause, ...]) -> int:
    """Count all satisfying phase assignments by exact DPLL."""

    @lru_cache(maxsize=None)
    def recurse(
        residual: tuple[Clause, ...],
        remaining: tuple[int, ...],
    ) -> int:
        remaining_set = set(remaining)

        for clause in residual:
            if len(clause) == 1:
                literal = clause[0]
                variable = abs(literal) - 1
                value = 1 if literal > 0 else 0
                reduced = simplify_one(residual, variable, value)
                if reduced is None:
                    return 0
                return recurse(reduced, tuple(sorted(remaining_set - {variable})))

        if not residual:
            return 1 << len(remaining_set)

        used = {abs(literal) - 1 for clause in residual for literal in clause}
        free_count = len(remaining_set - used)
        active = remaining_set & used
        occurrences = {
            variable: sum(
                1
                for clause in residual
                for literal in clause
                if abs(literal) - 1 == variable
            )
            for variable in active
        }
        variable = max(active, key=occurrences.get)

        subtotal = 0
        for value in (0, 1):
            reduced = simplify_one(residual, variable, value)
            if reduced is not None:
                subtotal += recurse(reduced, tuple(sorted(active - {variable})))
        return (1 << free_count) * subtotal

    return recurse(clauses, tuple(range(variable_count)))


def verify_cnf_equivalence() -> None:
    """Compare CNF counts with direct enumeration on the smallest cases."""
    for m, n in ((2, 2), (2, 3), (3, 2)):
        for outer in valid_factor_pairs(m):
            for inner in valid_factor_pairs(n):
                cycle_count = len(transition_cycles(*inner))
                for orientation in ORIENTATIONS:
                    direct = 0
                    for phases in phase_states(m, cycle_count):
                        layers = cycle_phase_product(
                            outer,
                            inner,
                            phases,
                            orientation,
                        )
                        cells = [point.flat for layer in layers for point in layer]
                        direct += int(is_no_three(cells))
                    variable_count, clauses = phase_cnf(
                        outer,
                        inner,
                        orientation,
                    )
                    assert direct == count_cnf_solutions(variable_count, clauses)
    print("CNF equivalence: direct and exact-DPLL counts agree")


def check_case(
    m: int,
    n: int,
    orientation: Orientation,
) -> tuple[int, int, int]:
    factor_instances = 0
    states = 0
    successes = 0
    for outer in valid_factor_pairs(m):
        for inner in valid_factor_pairs(n):
            variable_count, clauses = phase_cnf(outer, inner, orientation)
            factor_instances += 1
            states += 1 << variable_count
            successes += count_cnf_solutions(variable_count, clauses)
    return factor_instances, states, successes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--extended",
        action="store_true",
        help="also solve 2x4, 4x2, 3x4, 4x3, 2x5, and 5x2",
    )
    parser.add_argument(
        "--orientation",
        choices=("all",) + ORIENTATIONS,
        default="all",
        help="radix orientation: c=coarse-major and f=fine-major",
    )
    args = parser.parse_args()

    explicit_all_orientation_counterexample()
    verify_cnf_equivalence()

    cases = [(2, 2), (2, 3), (3, 2), (3, 3)]
    if args.extended:
        cases.extend([(2, 4), (4, 2), (3, 4), (4, 3), (2, 5), (5, 2)])
    orientations = ORIENTATIONS if args.orientation == "all" else (args.orientation,)

    for m, n in cases:
        for orientation in orientations:
            instances, states, successes = check_case(m, n, orientation)
            print(
                f"m={m}, n={n}, orientation={orientation}: "
                f"factor_instances={instances}, states={states}, "
                f"no_three_products={successes}"
            )


if __name__ == "__main__":
    main()
