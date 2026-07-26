#!/usr/bin/env python3
"""Exhaustive finite check for the twelve swap words in SAS5j."""

from __future__ import annotations

from itertools import combinations, permutations, product

Word = tuple[str, int] | tuple[str, int, int]


def classify(scope: tuple[int, int, int], x: int, y: int) -> Word | None:
    positions = {column: index for index, column in enumerate(scope)}
    x_position = positions.get(x)
    y_position = positions.get(y)
    if x_position is None and y_position is None:
        return None
    if x_position is not None and y_position is None:
        return ("X", x_position)
    if y_position is not None and x_position is None:
        return ("Y", y_position)
    assert x_position is not None and y_position is not None
    return ("XY", x_position, y_position)


def mismatch_count(
    colouring: tuple[int, ...],
    scope: tuple[int, int, int],
    required: tuple[int, int, int],
) -> int:
    return sum(colouring[column] != required[index] for index, column in enumerate(scope))


def verify() -> None:
    columns = range(5)
    labels = range(3)
    seen_destroyed: set[Word] = set()
    seen_repaired: set[Word] = set()
    checked_records = 0

    for colouring in product(labels, repeat=5):
        for x, y in combinations(columns, 2):
            a = colouring[x]
            b = colouring[y]
            if a == b:
                continue
            swapped = list(colouring)
            swapped[x], swapped[y] = swapped[y], swapped[x]
            swapped_tuple = tuple(swapped)

            for scope in permutations(columns, 3):
                for required in product(labels, repeat=3):
                    before = mismatch_count(colouring, scope, required) == 0
                    after = mismatch_count(swapped_tuple, scope, required) == 0
                    if before == after:
                        continue

                    word = classify(scope, x, y)
                    assert word is not None
                    checked_records += 1

                    if before and not after:
                        seen_destroyed.add(word)
                        assert mismatch_count(colouring, scope, required) == 0
                        if word[0] == "X":
                            assert required[word[1]] == a
                        elif word[0] == "Y":
                            assert required[word[1]] == b
                        else:
                            assert required[word[1]] == a
                            assert required[word[2]] == b

                    if after and not before:
                        seen_repaired.add(word)
                        if word[0] == "X":
                            assert required[word[1]] == b
                            assert mismatch_count(colouring, scope, required) == 1
                        elif word[0] == "Y":
                            assert required[word[1]] == a
                            assert mismatch_count(colouring, scope, required) == 1
                        else:
                            assert required[word[1]] == b
                            assert required[word[2]] == a
                            assert mismatch_count(colouring, scope, required) == 2

    expected: set[Word] = {
        *(('X', index) for index in range(3)),
        *(('Y', index) for index in range(3)),
        *(('XY', left, right) for left in range(3) for right in range(3) if left != right),
    }
    assert seen_destroyed == expected
    assert seen_repaired == expected
    print(
        f"verified {checked_records} changed constraint records; "
        "all 12 destruction and 12 repair words occur"
    )


if __name__ == "__main__":
    verify()
