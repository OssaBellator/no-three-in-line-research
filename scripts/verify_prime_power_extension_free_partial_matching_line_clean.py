#!/usr/bin/env python3
"""Finite checks for CMR1510--CMR1517."""

from itertools import combinations
from math import gcd


def has_perfect_matching(n, allowed):
    rows = sorted(range(n), key=lambda r: sum((r, c) in allowed for c in range(n)))
    used = set()

    def dfs(i):
        if i == n:
            return True
        row = rows[i]
        for column in range(n):
            if column not in used and (row, column) in allowed:
                used.add(column)
                if dfs(i + 1):
                    return True
                used.remove(column)
        return False

    return dfs(0)


def partial_matchings(edges, n):
    by_row = [[] for _ in range(n)]
    for row, column in edges:
        by_row[row].append(column)

    result = []

    def rec(row, used_columns, chosen):
        if row == n:
            result.append(frozenset(chosen))
            return
        rec(row + 1, used_columns, chosen)
        for column in by_row[row]:
            if column in used_columns:
                continue
            used_columns.add(column)
            chosen.append((row, column))
            rec(row + 1, used_columns, chosen)
            chosen.pop()
            used_columns.remove(column)

    rec(0, set(), [])
    return result


def canonical_line(first, second):
    x1, y1 = first
    x2, y2 = second
    value = [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]
    divisor = gcd(gcd(abs(value[0]), abs(value[1])), abs(value[2]))
    if divisor:
        value = [entry // divisor for entry in value]
    if value[0] < 0 or (
        value[0] == 0
        and (value[1] < 0 or (value[1] == 0 and value[2] < 0))
    ):
        value = [-entry for entry in value]
    return tuple(value)


def line_cells(n, key):
    a, b, c = key
    return {
        (x, y)
        for x in range(n)
        for y in range(n)
        if a * x + b * y + c == 0
    }


def check_hall_cuts():
    cuts = 0
    minimum_margin = None
    for n in range(4, 10):
        for target_row in range(n):
            for target_column in range(n):
                if target_row == target_column:
                    continue
                for k in range(1, n + 1):
                    z = n - k + 1
                    for rows in combinations(range(n), k):
                        for columns in combinations(range(n), z):
                            cut = {
                                (row, column)
                                for row in rows
                                for column in columns
                                if row != column
                                and (row, column) != (target_row, target_column)
                            }
                            margin = len(cut) - min(k, z)
                            assert margin >= 1
                            minimum_margin = (
                                margin
                                if minimum_margin is None
                                else min(minimum_margin, margin)
                            )
                            cuts += 1
    return cuts, minimum_margin


def check_partial_deletions():
    systems = 0
    deletions = 0
    by_size = {}
    for n in range(4, 7):
        opposite = {(index, index) for index in range(n)}
        complete = {(row, column) for row in range(n) for column in range(n)}
        for target_row in range(n):
            for target_column in range(n):
                if target_row == target_column:
                    continue
                target = (target_row, target_column)
                host = complete - opposite - {target}
                systems += 1
                for deletion in partial_matchings(host, n):
                    assert has_perfect_matching(n, host - set(deletion))
                    deletions += 1
                    by_size[len(deletion)] = by_size.get(len(deletion), 0) + 1
    return systems, deletions, by_size


def check_lines():
    systems = 0
    traces = 0
    for n in range(4, 9):
        points = [(x, y) for x in range(n) for y in range(n)]
        keys = {
            canonical_line(first, second)
            for first, second in combinations(points, 2)
            if first[0] != second[0] and first[1] != second[1]
        }
        opposite = {(index, index) for index in range(n)}
        complete = set(points)
        for target_row in range(n):
            for target_column in range(n):
                if target_row == target_column:
                    continue
                target = (target_row, target_column)
                host = complete - opposite - {target}
                systems += 1
                for key in keys:
                    deletion = host & line_cells(n, key)
                    assert len({row for row, _column in deletion}) == len(deletion)
                    assert len({column for _row, column in deletion}) == len(deletion)
                    assert has_perfect_matching(n, host - deletion)
                    traces += 1
    return systems, traces


def main():
    cuts, margin = check_hall_cuts()
    systems, deletions, by_size = check_partial_deletions()
    line_systems, traces = check_lines()
    print(
        "verified extension-free partial-matching deletion:",
        cuts,
        "Hall cuts with minimum excess",
        margin,
        ";",
        systems,
        "target systems and",
        deletions,
        "partial deletions;",
        line_systems,
        "line systems and",
        traces,
        "nonaxis traces; size histogram",
        sorted(by_size.items()),
    )


if __name__ == "__main__":
    main()
