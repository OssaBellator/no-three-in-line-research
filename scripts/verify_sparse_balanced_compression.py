#!/usr/bin/env python3
"""Verify SAS5f exact balanced-colour compression energy."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

Constraint = tuple[tuple[int, int, int], tuple[int, int, int]]


def falling(number: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= number - offset
    return result


def balanced_colourings(block_count: int, block_size: int) -> list[tuple[int, ...]]:
    total = block_count * block_size
    return [
        colouring
        for colouring in product(range(block_count), repeat=total)
        if all(colouring.count(label) == block_size for label in range(block_count))
    ]


def collinear_column_triples(
    rows: tuple[int, int, int],
    total: int,
) -> list[tuple[int, int, int]]:
    first_row, second_row, third_row = rows
    return [
        columns
        for columns in permutations(range(total), 3)
        if (
            (second_row - first_row) * (columns[2] - columns[0])
            == (third_row - first_row) * (columns[1] - columns[0])
        )
    ]


def triple_count(
    row_colours: tuple[int, ...],
    column_colours: tuple[int, ...],
) -> int:
    total = len(row_colours)
    return sum(
        all(column_colours[columns[index]] == row_colours[rows[index]]
            for index in range(3))
        for rows in combinations(range(total), 3)
        for columns in collinear_column_triples(rows, total)
    )


def profile_counts(row_colours: tuple[int, ...]) -> tuple[int, int, int]:
    total = len(row_colours)
    profile = [0, 0, 0]
    for rows in combinations(range(total), 3):
        labels = tuple(row_colours[row] for row in rows)
        multiplicities = sorted(
            (
                labels.count(label)
                for label in set(labels)
            ),
            reverse=True,
        )
        if multiplicities == [3]:
            index = 0
        elif multiplicities == [2, 1]:
            index = 1
        else:
            assert multiplicities == [1, 1, 1]
            index = 2
        profile[index] += len(collinear_column_triples(rows, total))
    return tuple(profile)


def constraints(row_colours: tuple[int, ...]) -> tuple[Constraint, ...]:
    total = len(row_colours)
    return tuple(
        (
            columns,
            tuple(row_colours[row] for row in rows),
        )
        for rows in combinations(range(total), 3)
        for columns in collinear_column_triples(rows, total)
    )


def conditional_energy(
    records: tuple[Constraint, ...],
    partial: tuple[int | None, ...],
    remaining: tuple[int, ...],
) -> Fraction:
    unassigned_total = sum(remaining)
    total = Fraction(0)
    for columns, required_labels in records:
        needed = [0] * len(remaining)
        compatible = True
        unassigned = 0
        for column, required in zip(columns, required_labels):
            assigned = partial[column]
            if assigned is None:
                needed[required] += 1
                unassigned += 1
            elif assigned != required:
                compatible = False
                break
        if not compatible:
            continue
        numerator = 1
        for label, count in enumerate(needed):
            numerator *= falling(remaining[label], count)
        total += Fraction(
            numerator,
            falling(unassigned_total, unassigned),
        )
    return total


def greedy_conditional_decoder(
    records: tuple[Constraint, ...],
    block_count: int,
    block_size: int,
) -> tuple[tuple[int, ...], tuple[Fraction, ...]]:
    total = block_count * block_size
    partial: list[int | None] = [None] * total
    remaining = [block_size] * block_count
    trace = [
        conditional_energy(
            records,
            tuple(partial),
            tuple(remaining),
        )
    ]
    for column in range(total):
        unassigned_total = sum(remaining)
        candidates: list[tuple[Fraction, int]] = []
        weighted_average = Fraction(0)
        for label in range(block_count):
            if remaining[label] == 0:
                continue
            probability = Fraction(remaining[label], unassigned_total)
            partial[column] = label
            remaining[label] -= 1
            value = conditional_energy(
                records,
                tuple(partial),
                tuple(remaining),
            )
            remaining[label] += 1
            partial[column] = None
            weighted_average += probability * value
            candidates.append((value, label))
        assert weighted_average == trace[-1]
        value, selected = min(candidates)
        assert value <= trace[-1]
        partial[column] = selected
        remaining[selected] -= 1
        trace.append(value)
    assert all(value is not None for value in partial)
    return tuple(int(value) for value in partial), tuple(trace)


def record_satisfied(
    record: Constraint,
    colouring: tuple[int, ...],
) -> bool:
    columns, required = record
    return all(
        colouring[column] == required[index]
        for index, column in enumerate(columns)
    )


def swap_colours(
    colouring: tuple[int, ...],
    left: int,
    right: int,
) -> tuple[int, ...]:
    result = list(colouring)
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def creation_count(
    record: Constraint,
    colouring: tuple[int, ...],
    block_size: int,
) -> int:
    columns, required = record
    mismatches = [
        index
        for index, column in enumerate(columns)
        if colouring[column] != required[index]
    ]
    if len(mismatches) == 1:
        index = mismatches[0]
        needed = required[index]
        return block_size - sum(
            colouring[column] == needed for column in columns
        )
    if len(mismatches) == 2:
        first, second = mismatches
        return int(
            colouring[columns[first]] == required[second]
            and colouring[columns[second]] == required[first]
        )
    return 0


def destruction_count(
    record: Constraint,
    colouring: tuple[int, ...],
    block_size: int,
) -> int:
    assert record_satisfied(record, colouring)
    columns, _ = record
    internal_cross_pairs = sum(
        colouring[columns[left]] != colouring[columns[right]]
        for left, right in combinations(range(3), 2)
    )
    return 3 * (len(colouring) - block_size) - internal_cross_pairs


def verify_swap_identity(
    records: tuple[Constraint, ...],
    colouring: tuple[int, ...],
    block_size: int,
) -> tuple[bool, int]:
    cross_pairs = tuple(
        (left, right)
        for left, right in combinations(range(len(colouring)), 2)
        if colouring[left] != colouring[right]
    )
    current = sum(
        record_satisfied(record, colouring) for record in records
    )
    drifts = tuple(
        sum(
            record_satisfied(
                record,
                swap_colours(colouring, left, right),
            )
            for record in records
        )
        - current
        for left, right in cross_pairs
    )
    created_by_swap = tuple(
        sum(
            not record_satisfied(record, colouring)
            and record_satisfied(
                record,
                swap_colours(colouring, left, right),
            )
            for record in records
        )
        for left, right in cross_pairs
    )
    destroyed_by_swap = tuple(
        sum(
            record_satisfied(record, colouring)
            and not record_satisfied(
                record,
                swap_colours(colouring, left, right),
            )
            for record in records
        )
        for left, right in cross_pairs
    )
    assert all(
        drift == repaired - destroyed
        for drift, repaired, destroyed in zip(
            drifts,
            created_by_swap,
            destroyed_by_swap,
        )
    )
    created = 0
    destroyed = 0
    one_mismatch = 0
    two_mismatches = 0
    for record in records:
        columns, required = record
        mismatches = sum(
            colouring[column] != required[index]
            for index, column in enumerate(columns)
        )
        if mismatches == 0:
            closed = destruction_count(record, colouring, block_size)
            actual = sum(
                not record_satisfied(
                    record,
                    swap_colours(colouring, left, right),
                )
                for left, right in cross_pairs
            )
            assert actual == closed
            destroyed += closed
        else:
            closed = creation_count(record, colouring, block_size)
            actual = sum(
                record_satisfied(
                    record,
                    swap_colours(colouring, left, right),
                )
                for left, right in cross_pairs
            )
            assert actual == closed
            created += closed
            one_mismatch += mismatches == 1
            two_mismatches += mismatches == 2
    assert sum(drifts) == created - destroyed

    local_minimum = all(drift >= 0 for drift in drifts)
    if local_minimum and len(set(colouring)) >= 2:
        assert created >= destroyed
        assert block_size * one_mismatch + two_mismatches >= (
            (3 * (len(colouring) - block_size) - 3) * current
        )
        total = len(colouring)
        assert len(cross_pairs) == total * (total - block_size) // 2
        lower = 3 * (total - block_size) - 3
        if current and lower > 0:
            concentrated = max(
                range(len(cross_pairs)),
                key=destroyed_by_swap.__getitem__,
            )
            assert (
                destroyed_by_swap[concentrated] * len(cross_pairs)
                >= lower * current
            )
            assert (
                created_by_swap[concentrated]
                >= destroyed_by_swap[concentrated]
            )
    return local_minimum, current


def swap_descent(
    records: tuple[Constraint, ...],
    colouring: tuple[int, ...],
    block_size: int,
) -> tuple[tuple[int, ...], int]:
    current = sum(
        record_satisfied(record, colouring) for record in records
    )
    initial = current
    steps = 0
    while True:
        improvement: tuple[tuple[int, ...], int] | None = None
        for left, right in combinations(range(len(colouring)), 2):
            if colouring[left] == colouring[right]:
                continue
            candidate = swap_colours(colouring, left, right)
            value = sum(
                record_satisfied(record, candidate)
                for record in records
            )
            if value < current:
                improvement = candidate, value
                break
        if improvement is None:
            break
        colouring, current = improvement
        steps += 1
        assert steps <= initial
    local, checked = verify_swap_identity(
        records,
        colouring,
        block_size,
    )
    assert local and checked == current
    return colouring, steps


def verify_partition(
    row_colours: tuple[int, ...],
    block_count: int,
    block_size: int,
) -> None:
    total = block_count * block_size
    assert len(row_colours) == total
    assert all(row_colours.count(label) == block_size for label in range(block_count))
    colourings = balanced_colourings(block_count, block_size)
    values = [triple_count(row_colours, colouring) for colouring in colourings]
    same, double, distinct = profile_counts(row_colours)
    expected = Fraction(
        same * falling(block_size, 3)
        + double * falling(block_size, 2) * block_size
        + distinct * block_size**3,
        falling(total, 3),
    )
    assert Fraction(sum(values), len(values)) == expected
    assert min(values) <= expected

    records = constraints(row_colours)
    empty = tuple(None for _ in range(total))
    initial = conditional_energy(
        records,
        empty,
        tuple(block_size for _ in range(block_count)),
    )
    assert initial == expected
    decoded, trace = greedy_conditional_decoder(
        records,
        block_count,
        block_size,
    )
    assert all(
        decoded.count(label) == block_size
        for label in range(block_count)
    )
    assert all(
        later <= earlier for earlier, later in zip(trace, trace[1:])
    )
    assert trace[-1] == triple_count(row_colours, decoded)
    assert trace[-1] <= expected
    for colouring in colourings:
        verify_swap_identity(records, colouring, block_size)
    descended, steps = swap_descent(records, decoded, block_size)
    assert all(
        descended.count(label) == block_size
        for label in range(block_count)
    )
    assert steps <= triple_count(row_colours, decoded)

    for prefix in range(total + 1):
        partial = tuple(
            decoded[column] if column < prefix else None
            for column in range(total)
        )
        remaining = tuple(
            block_size
            - sum(
                decoded[column] == label for column in range(prefix)
            )
            for label in range(block_count)
        )
        completions = [
            colouring
            for colouring in colourings
            if all(
                partial[column] is None
                or partial[column] == colouring[column]
                for column in range(total)
            )
        ]
        assert completions
        actual = Fraction(
            sum(
                triple_count(row_colours, colouring)
                for colouring in completions
            ),
            len(completions),
        )
        assert conditional_energy(records, partial, remaining) == actual


def verify() -> None:
    for block_count, block_size in ((1, 3), (2, 2), (2, 3), (3, 2)):
        total = block_count * block_size
        consecutive = tuple(
            row // block_size for row in range(total)
        )
        interlaced = tuple(row % block_count for row in range(total))
        verify_partition(
            consecutive,
            block_count,
            block_size,
        )
        verify_partition(
            interlaced,
            block_count,
            block_size,
        )


def main() -> None:
    verify()
    print("sparse balanced compression energy: exhaustive regressions passed")


if __name__ == "__main__":
    main()
