#!/usr/bin/env python3
"""Exhaust RI5q--RI5r on small blocker permutations."""

from itertools import combinations, permutations, product
from math import ceil, gcd


def determinant(left: tuple[int, int], right: tuple[int, int]) -> int:
    return left[0] * right[1] - left[1] * right[0]


def primitive_direction(dx: int, dy: int) -> tuple[int, int]:
    common = gcd(abs(dx), abs(dy))
    x = dx // common
    y = dy // common
    if x < 0:
        x = -x
        y = -y
    return x, y


def is_collinear(points: tuple[tuple[int, int], ...]) -> bool:
    first, second, third = points
    return determinant(
        (second[0] - first[0], second[1] - first[1]),
        (third[0] - first[0], third[1] - first[1]),
    ) == 0


def verify_geometry(maximum_size: int = 6) -> tuple[int, int, int]:
    triple_count = 0
    address_count = 0
    intersection_count = 0

    for size in range(3, maximum_size + 1):
        for blocker in permutations(range(size)):
            old_cells = {(column, blocker[column]) for column in range(size)}

            for fixed_column in range(size):
                fixed_row = blocker[fixed_column]
                corner = (fixed_column, fixed_row)
                address_owner: dict[
                    tuple[str, tuple[int, int], int], int
                ] = {}

                for auxiliary_column in range(size):
                    if auxiliary_column == fixed_column:
                        continue

                    auxiliary_row = blocker[auxiliary_column]
                    delta_column = auxiliary_column - fixed_column
                    delta_row = auxiliary_row - fixed_row
                    vertical = (fixed_column, auxiliary_row)
                    horizontal = (auxiliary_column, fixed_row)

                    new_cells = set(old_cells)
                    new_cells.remove(corner)
                    new_cells.remove((auxiliary_column, auxiliary_row))
                    new_cells.update((vertical, horizontal))

                    for columns in combinations(range(size), 3):
                        triple = tuple(
                            sorted(
                                (
                                    column,
                                    next(
                                        row
                                        for current_column, row in new_cells
                                        if current_column == column
                                    ),
                                )
                                for column in columns
                            )
                        )

                        if not is_collinear(triple):
                            continue

                        triple_cells = set(triple)
                        if triple_cells <= old_cells:
                            continue

                        local_cells = triple_cells & {vertical, horizontal}
                        if not local_cells:
                            continue

                        first, second = triple[0], triple[1]
                        direction = primitive_direction(
                            second[0] - first[0],
                            second[1] - first[1],
                        )
                        offset = determinant(
                            direction,
                            (first[0] - fixed_column, first[1] - fixed_row),
                        )
                        assert all(
                            determinant(
                                direction,
                                (column - fixed_column, row - fixed_row),
                            )
                            == offset
                            for column, row in triple
                        )

                        if local_cells == {vertical}:
                            channel = "V"
                            assert offset == direction[0] * delta_row

                            contexts = sorted(triple_cells - {vertical})
                            first_context, second_context = contexts
                            numerator = (
                                (second_context[0] - fixed_column)
                                * first_context[1]
                                - (first_context[0] - fixed_column)
                                * second_context[1]
                            )
                            denominator = (
                                second_context[0] - first_context[0]
                            )
                            assert numerator % denominator == 0
                            assert numerator // denominator == auxiliary_row
                            intersection_count += 1

                        elif local_cells == {horizontal}:
                            channel = "H"
                            assert direction[1] != 0
                            assert offset == -direction[1] * delta_column

                            contexts = sorted(triple_cells - {horizontal})
                            first_context, second_context = contexts
                            numerator = (
                                (second_context[1] - fixed_row)
                                * first_context[0]
                                - (first_context[1] - fixed_row)
                                * second_context[0]
                            )
                            denominator = (
                                second_context[1] - first_context[1]
                            )
                            assert numerator % denominator == 0
                            assert numerator // denominator == auxiliary_column
                            intersection_count += 1

                        else:
                            assert local_cells == {vertical, horizontal}
                            channel = "VH"
                            a, b = primitive_direction(delta_column, delta_row)
                            scale = delta_column // a
                            assert delta_row == scale * b
                            assert direction == (a, -b)
                            assert offset == scale * a * b

                        address = (channel, direction, offset)
                        if address in address_owner:
                            assert address_owner[address] == auxiliary_column
                        else:
                            address_owner[address] = auxiliary_column
                            address_count += 1

                        triple_count += 1

    return triple_count, address_count, intersection_count


def verify_weighted_router() -> int:
    checks = 0

    # Two offsets on the first direction and one offset on each of two more
    # directions. Exhausting small weights checks both nested pigeonholes.
    for weights in product(range(4), repeat=4):
        total = sum(weights)
        if total == 0:
            continue

        direction_weights = (
            weights[0] + weights[1],
            weights[2],
            weights[3],
        )

        for direction_threshold in (1, 2, 3):
            if max(direction_weights) <= direction_threshold:
                assert sum(weight > 0 for weight in direction_weights) >= ceil(
                    total / direction_threshold
                )
            else:
                heavy_index = next(
                    index
                    for index, weight in enumerate(direction_weights)
                    if weight > direction_threshold
                )
                heavy_weight = direction_weights[heavy_index]
                offset_weights = (
                    (weights[0], weights[1])
                    if heavy_index == 0
                    else (weights[heavy_index + 1],)
                )

                for offset_threshold in (1, 2, 3):
                    if max(offset_weights) <= offset_threshold:
                        assert sum(weight > 0 for weight in offset_weights) >= ceil(
                            heavy_weight / offset_threshold
                        )

        checks += 1

    return checks


def main() -> None:
    triples, addresses, intersections = verify_geometry()
    routers = verify_weighted_router()
    print(
        "RI crossed affine addresses verified: "
        f"{triples} variable collinear triples, "
        f"{addresses} injective affine addresses, "
        f"{intersections} context intersections, and "
        f"{routers} weighted routers"
    )


if __name__ == "__main__":
    main()
