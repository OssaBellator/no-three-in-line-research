#!/usr/bin/env python3
"""Verify the full-selector block-map normal form and universal 2 x 3 closure."""
from __future__ import annotations

from itertools import combinations, permutations, product

Permutation = tuple[int, ...]
Point = tuple[int, int]
FactorPair = tuple[Permutation, Permutation]
ORIENTATION = "cf"
CANONICAL_INNER: FactorPair = ((0, 2, 1), (1, 0, 2))
CANONICAL_SELECTED: tuple[Point, ...] = (
    (0, 1), (0, 3), (1, 1), (1, 5), (2, 3), (2, 5),
    (3, 0), (3, 2), (4, 0), (4, 4), (5, 2), (5, 4),
)
CANONICAL_LAYERS: FactorPair = (
    (1, 5, 3, 0, 4, 2),
    (3, 1, 5, 2, 0, 4),
)


def compose(first: Permutation, second: Permutation) -> Permutation:
    """Return first after second."""
    return tuple(first[second[index]] for index in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def identity(n: int) -> Permutation:
    return tuple(range(n))


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    for first in permutations(range(n)):
        for second in permutations(range(n)):
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = [(x, first[x]) for x in range(n)]
            points.extend((x, second[x]) for x in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def apply_power(permutation: Permutation, exponent: int) -> Permutation:
    return identity(len(permutation)) if exponent == 0 else permutation


def block_maps(
    tau: FactorPair,
    row_maps: tuple[Permutation, Permutation],
    column_maps: tuple[Permutation, Permutation],
) -> tuple[tuple[tuple[Permutation, Permutation], ...], ...]:
    result = []
    for i in (0, 1):
        row = []
        for j in (0, 1):
            row.append(
                tuple(
                    compose(column_maps[j], compose(tau[s], inverse(row_maps[i])))
                    for s in (0, 1)
                )
            )
        result.append(tuple(row))
    return tuple(result)  # type: ignore[return-value]


def normal_parameters(
    tau: FactorPair,
    row_maps: tuple[Permutation, Permutation],
    column_maps: tuple[Permutation, Permutation],
) -> tuple[Permutation, Permutation, Permutation, Permutation]:
    alpha_0, alpha_1 = row_maps
    beta_0, beta_1 = column_maps
    tau_0, tau_1 = tau
    t = compose(beta_0, compose(tau_0, inverse(alpha_0)))
    p = compose(alpha_0, inverse(alpha_1))
    q = compose(beta_1, inverse(beta_0))
    h = compose(alpha_0, compose(inverse(tau_0), compose(tau_1, inverse(alpha_0))))
    return t, p, q, h


def normal_block_maps(
    t: Permutation,
    p: Permutation,
    q: Permutation,
    h: Permutation,
) -> tuple[tuple[tuple[Permutation, Permutation], ...], ...]:
    result = []
    for i in (0, 1):
        row = []
        for j in (0, 1):
            row.append(
                tuple(
                    compose(
                        apply_power(q, j),
                        compose(t, compose(apply_power(h, s), apply_power(p, i))),
                    )
                    for s in (0, 1)
                )
            )
        result.append(tuple(row))
    return tuple(result)  # type: ignore[return-value]


def host_from_block_maps(
    maps: tuple[tuple[tuple[Permutation, Permutation], ...], ...],
    orientation: str,
) -> tuple[Point, ...]:
    n = len(maps[0][0][0])
    cells = set()
    for i, j, s, u in product((0, 1), (0, 1), (0, 1), range(n)):
        v = maps[i][j][s][u]
        x = n * i + u if orientation[0] == "c" else 2 * u + i
        y = n * j + v if orientation[1] == "c" else 2 * v + j
        cells.add((x, y))
    assert len(cells) == 8 * n
    return tuple(sorted(cells))


def verify_degree_two(host: tuple[Point, ...], selected: tuple[Point, ...]) -> None:
    side = len(selected) // 2
    assert set(selected).issubset(host)
    assert len(selected) == 2 * side
    assert all(sum(x == row for x, _ in selected) == 2 for row in range(side))
    assert all(sum(y == column for _, y in selected) == 2 for column in range(side))
    assert is_no_three(selected)


def cycle_type(permutation: Permutation) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def verify_normal_form() -> None:
    all_permutations = tuple(permutations(range(3)))
    checked = 0
    for tau_0, tau_1, alpha_0, alpha_1, beta_0, beta_1 in product(
        all_permutations, repeat=6
    ):
        tau = (tau_0, tau_1)
        row_maps = (alpha_0, alpha_1)
        column_maps = (beta_0, beta_1)
        direct = block_maps(tau, row_maps, column_maps)
        normal = normal_block_maps(*normal_parameters(tau, row_maps, column_maps))
        assert direct == normal
        checked += 1
    assert checked == 6**6
    print(f"full-host normal form: checked {checked} side-three map tuples")


def verify_side_three_closure() -> None:
    identity_three = identity(3)
    canonical_maps = block_maps(
        CANONICAL_INNER,
        (identity_three, identity_three),
        (identity_three, identity_three),
    )
    canonical_host = host_from_block_maps(canonical_maps, ORIENTATION)
    verify_degree_two(canonical_host, CANONICAL_SELECTED)

    target_t = CANONICAL_INNER[0]
    target_h = compose(inverse(CANONICAL_INNER[0]), CANONICAL_INNER[1])
    assert cycle_type(target_h) == (3,)

    factors = valid_factor_pairs(3)
    assert len(factors) == 4
    for tau_0, tau_1 in factors:
        relative = compose(inverse(tau_0), tau_1)
        assert cycle_type(relative) == (3,)
        gamma = next(
            candidate
            for candidate in permutations(range(3))
            if compose(candidate, compose(relative, inverse(candidate))) == target_h
        )
        beta = compose(target_t, compose(gamma, inverse(tau_0)))
        transported_maps = block_maps(
            (tau_0, tau_1),
            (gamma, gamma),
            (beta, beta),
        )
        transported_host = host_from_block_maps(transported_maps, ORIENTATION)
        assert transported_host == canonical_host
        verify_degree_two(transported_host, CANONICAL_SELECTED)

    assert is_no_three(
        tuple(
            (x, CANONICAL_LAYERS[layer][x])
            for layer in (0, 1)
            for x in range(6)
        )
    )
    print("universal 2 x 3 -> 6 full-selector closure verified for all four ordered factors")
    print(f"side-six layers: {CANONICAL_LAYERS}")


def main() -> None:
    verify_normal_form()
    verify_side_three_closure()


if __name__ == "__main__":
    main()
