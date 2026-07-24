#!/usr/bin/env python3
"""Finite checks for mixed-radix product constructions.

The script verifies three things:

* the cycle-phase product encoding is exactly two-regular in rows and columns;
* the flattened determinant satisfies the exact coarse/mixed/fine identity;
* small saturated no-three factor pairs do not, in general, compose to a
  no-three product, even after all cycle-wise phase choices are tried.

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
PhaseState = tuple[tuple[int, ...], ...]


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


def mixed_term(a: EncodedPoint, b: EncodedPoint, c: EncodedPoint) -> int:
    di_b = b.coarse[0] - a.coarse[0]
    dj_b = b.coarse[1] - a.coarse[1]
    du_b = b.fine[0] - a.fine[0]
    dv_b = b.fine[1] - a.fine[1]
    di_c = c.coarse[0] - a.coarse[0]
    dj_c = c.coarse[1] - a.coarse[1]
    du_c = c.fine[0] - a.fine[0]
    dv_c = c.fine[1] - a.fine[1]
    return di_b * dv_c + du_b * dj_c - dj_b * du_c - dv_b * di_c


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
    for bits in product((0, 1), repeat=m * cycle_count):
        yield tuple(
            tuple(bits[i * cycle_count : (i + 1) * cycle_count])
            for i in range(m)
        )


def cycle_phase_product(
    outer: FactorPair,
    inner: FactorPair,
    phases: PhaseState,
) -> tuple[list[EncodedPoint], list[EncodedPoint]]:
    """Construct the two permutation layers of the cycle-phase product."""
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
                s = r ^ phases[i][cycle_id[u]]
                j = outer[r][i]
                v = inner[s][u]
                layers[r].append(
                    EncodedPoint(
                        x=n * i + u,
                        y=n * j + v,
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


def verify_determinant_identity(
    layers: tuple[list[EncodedPoint], list[EncodedPoint]],
    fine_side: int,
) -> None:
    points = layers[0] + layers[1]
    for a, b, c in combinations(points, 3):
        coarse = determinant(a.coarse, b.coarse, c.coarse)
        fine = determinant(a.fine, b.fine, c.fine)
        mixed = mixed_term(a, b, c)
        flat = determinant(a.flat, b.flat, c.flat)
        assert flat == fine_side * fine_side * coarse + fine_side * mixed + fine

        if flat == 0:
            assert fine % fine_side == 0
            carry = fine // fine_side
            assert abs(carry) <= fine_side - 2
            assert fine_side * coarse + mixed + carry == 0


def explicit_diagonal_counterexample() -> None:
    factor: FactorPair = ((0, 1), (1, 0))
    phases: PhaseState = ((0,), (0,))
    layers = cycle_phase_product(factor, factor, phases)
    witness = ((0, 0), (1, 1), (2, 2))
    cells = {point.flat for layer in layers for point in layer}
    assert set(witness).issubset(cells)
    assert determinant(*witness) == 0
    print(f"explicit 2x2 diagonal witness: {witness}")


def check_case(
    m: int,
    n: int,
) -> tuple[int, int, tuple[Point, Point, Point] | None]:
    states = 0
    successes = 0
    first_witness: tuple[Point, Point, Point] | None = None

    for outer in valid_factor_pairs(m):
        for inner in valid_factor_pairs(n):
            cycle_count = len(transition_cycles(*inner))
            for phases in phase_states(m, cycle_count):
                states += 1
                layers = cycle_phase_product(outer, inner, phases)
                verify_saturation(layers)
                verify_determinant_identity(layers, n)
                cells = [point.flat for layer in layers for point in layer]
                witness = first_collinear(cells)
                if witness is None:
                    successes += 1
                elif first_witness is None:
                    first_witness = witness

    return states, successes, first_witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-four",
        action="store_true",
        help="also exhaust the 2x4, 3x4, 4x2, and 4x3 cases",
    )
    args = parser.parse_args()

    explicit_diagonal_counterexample()

    cases = [(2, 2), (2, 3), (3, 2), (3, 3)]
    if args.include_four:
        cases.extend([(2, 4), (3, 4), (4, 2), (4, 3)])

    for m, n in cases:
        states, successes, witness = check_case(m, n)
        print(
            f"m={m}, n={n}: outer_pairs={len(valid_factor_pairs(m))}, "
            f"inner_pairs={len(valid_factor_pairs(n))}, states={states}, "
            f"no_three_products={successes}, first_bad_triple={witness}"
        )


if __name__ == "__main__":
    main()
