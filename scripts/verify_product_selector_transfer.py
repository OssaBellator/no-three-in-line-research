#!/usr/bin/env python3
"""Verify the transfer-matrix count for abstract full-selector states."""
from __future__ import annotations

from itertools import combinations, product

State = tuple[int, int]
STATES: tuple[State, ...] = tuple(product(range(3), repeat=2))
INDEX = {state: index for index, state in enumerate(STATES)}
EXPECTED_MATRIX = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 2, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 2, 0, 1, 0, 0),
    (0, 2, 0, 2, 0, 0, 0, 0, 0),
    (0, 0, 2, 0, 6, 0, 2, 0, 0),
    (0, 0, 0, 0, 0, 2, 0, 2, 0),
    (0, 0, 1, 0, 2, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 2, 0, 2, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1),
)
EXPECTED_SINGLE_CYCLE = {
    2: 90,
    3: 546,
    4: 3_618,
    5: 25_218,
    6: 181_122,
    7: 1_323_522,
    8: 9_765_378,
}


def build_transfer_matrix() -> tuple[tuple[int, ...], ...]:
    matrix = [[0] * len(STATES) for _ in STATES]
    row_choices = tuple(combinations(range(4), 2))
    for incoming in STATES:
        for first_row in row_choices:
            for second_row in row_choices:
                current = [0, 0]
                outgoing = [0, 0]
                for choice in (first_row, second_row):
                    for target in choice:
                        if target < 2:
                            current[target] += 1
                        else:
                            outgoing[target - 2] += 1
                if all(incoming[index] + current[index] == 2 for index in range(2)):
                    matrix[INDEX[incoming]][INDEX[tuple(outgoing)]] += 1
    return tuple(tuple(row) for row in matrix)


def multiply(first: tuple[tuple[int, ...], ...], second: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    size = len(first)
    return tuple(
        tuple(
            sum(first[row][middle] * second[middle][column] for middle in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def matrix_power(matrix: tuple[tuple[int, ...], ...], exponent: int) -> tuple[tuple[int, ...], ...]:
    size = len(matrix)
    result = tuple(tuple(int(row == column) for column in range(size)) for row in range(size))
    base = matrix
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def trace(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[index][index] for index in range(len(matrix)))


def radical_trace_term(length: int) -> int:
    """Return (4+2sqrt(3))^L + (4-2sqrt(3))^L as an integer."""
    if length == 0:
        return 2
    if length == 1:
        return 8
    previous_previous = 2
    previous = 8
    for _ in range(2, length + 1):
        previous_previous, previous = previous, 8 * previous - 4 * previous_previous
    return previous


def single_cycle_count(length: int) -> int:
    return 2 + 2 * 4**length + radical_trace_term(length)


def main() -> None:
    matrix = build_transfer_matrix()
    assert matrix == EXPECTED_MATRIX

    for length, expected in EXPECTED_SINGLE_CYCLE.items():
        direct = trace(matrix_power(matrix, length))
        formula = single_cycle_count(length)
        assert direct == formula == expected, (length, direct, formula, expected)
        print(f"relative {length}-cycle: selector states={expected}")

    side_six = {
        (6,): single_cycle_count(6),
        (4, 2): single_cycle_count(4) * single_cycle_count(2),
        (3, 3): single_cycle_count(3) ** 2,
    }
    assert side_six == {
        (6,): 181_122,
        (4, 2): 325_620,
        (3, 3): 298_116,
    }
    print(f"side-six relative-type selector counts: {side_six}")


if __name__ == "__main__":
    main()
