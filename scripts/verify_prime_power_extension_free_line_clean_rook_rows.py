#!/usr/bin/env python3
"""Finite checks for CMR1526--CMR1533."""

from itertools import combinations, permutations
from math import factorial, gcd
import random


def poly_add(first, second):
    size = max(len(first), len(second))
    result = [0] * size
    for index, value in enumerate(first):
        result[index] += value
    for index, value in enumerate(second):
        result[index] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_mul(first, second):
    result = [0] * (len(first) + len(second) - 1)
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            result[i + j] += x * y
    return result


def shift(poly):
    return [0] + list(poly)


def matching_poly_bruteforce(edges):
    edges = list(edges)
    counts = [0] * (len(edges) + 1)
    for size in range(len(edges) + 1):
        for chosen in combinations(edges, size):
            if (
                len({row for row, _column in chosen}) == size
                and len({column for _row, column in chosen}) == size
            ):
                counts[size] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return counts


def components(edges):
    adjacency = {}
    for row, column in edges:
        left = (0, row)
        right = (1, column)
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)

    seen = set()
    result = []
    for start in adjacency:
        if start in seen:
            continue
        stack = [start]
        vertices = set()
        twice_edges = 0
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            vertices.add(vertex)
            twice_edges += len(adjacency[vertex])
            stack.extend(adjacency[vertex] - seen)
        degrees = [len(adjacency[vertex]) for vertex in vertices]
        assert max(degrees) <= 2
        edge_count = twice_edges // 2
        kind = "cycle" if all(degree == 2 for degree in degrees) else "path"
        result.append((kind, edge_count))
    return result


def path_poly(edge_count):
    if edge_count == 0:
        return [1]
    if edge_count == 1:
        return [1, 1]
    previous2 = [1]
    previous1 = [1, 1]
    for _ in range(2, edge_count + 1):
        current = poly_add(previous1, shift(previous2))
        previous2, previous1 = previous1, current
    return previous1


def cycle_poly(edge_count):
    assert edge_count >= 4 and edge_count % 2 == 0
    return poly_add(path_poly(edge_count - 1), shift(path_poly(edge_count - 3)))


def degree_two_poly(edges):
    result = [1]
    for kind, edge_count in components(edges):
        factor = path_poly(edge_count) if kind == "path" else cycle_poly(edge_count)
        result = poly_mul(result, factor)
    return result


def line_clean_rook_poly(opposite, line_trace, target):
    base = set(opposite) | set(line_trace)
    assert target not in base
    row, column = target
    contracted = {
        (r, c)
        for r, c in base
        if r != row and c != column
    }
    return poly_add(degree_two_poly(base), shift(degree_two_poly(contracted)))


def inclusion_exclusion_count(side, rook_poly):
    return sum(
        (-1) ** size * rooks * factorial(side - size)
        for size, rooks in enumerate(rook_poly)
    )


def perfect_matchings(side, forbidden):
    result = []
    for value in permutations(range(side)):
        matching = frozenset((row, value[row]) for row in range(side))
        if matching.isdisjoint(forbidden):
            result.append(matching)
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


def line_cells(side, key):
    a, b, c = key
    return {
        (x, y)
        for x in range(side)
        for y in range(side)
        if a * x + b * y + c == 0
    }


def residualise(edges, prescription):
    rows = {row for row, _column in prescription}
    columns = {column for _row, column in prescription}
    return {
        (row, column)
        for row, column in edges
        if row not in rows and column not in columns
    }


def check_degree_two_components():
    rng = random.Random(1528)
    checks = 0
    for side in range(4, 10):
        opposite = {(index, index) for index in range(side)}
        for _ in range(200):
            columns = list(range(side))
            rng.shuffle(columns)
            partial = {
                (row, columns[row])
                for row in range(side)
                if columns[row] != row and rng.random() < 0.65
            }
            base = opposite | partial
            degrees = (
                [sum(r == row for r, _column in base) for row in range(side)]
                + [
                    sum(c == column for _row, c in base)
                    for column in range(side)
                ]
            )
            assert max(degrees) <= 2
            assert degree_two_poly(base) == matching_poly_bruteforce(base)
            checks += 1
    return checks


def check_line_hosts():
    rng = random.Random(1531)
    host_checks = 0
    prescription_checks = 0
    total_matchings = 0
    for side in range(4, 8):
        points = [(x, y) for x in range(side) for y in range(side)]
        keys = list(
            {
                canonical_line(first, second)
                for first, second in combinations(points, 2)
                if first[0] != second[0] and first[1] != second[1]
            }
        )
        opposite = {(index, index) for index in range(side)}
        for _ in range(120):
            target = rng.choice(
                [
                    (row, column)
                    for row in range(side)
                    for column in range(side)
                    if row != column
                ]
            )
            key = rng.choice(keys)
            trace = line_cells(side, key) - opposite - {target}
            forbidden = opposite | trace | {target}
            rook_poly = line_clean_rook_poly(opposite, trace, target)
            matchings = perfect_matchings(side, forbidden)
            assert inclusion_exclusion_count(side, rook_poly) == len(matchings)
            assert matchings
            host_checks += 1
            total_matchings += len(matchings)

            allowed = set(points) - forbidden
            found = False
            for rank in (1, 2, 3):
                sample = list(combinations(allowed, rank))
                rng.shuffle(sample)
                for prescription in sample[:12]:
                    if (
                        len({row for row, _column in prescription}) != rank
                        or len({column for _row, column in prescription}) != rank
                    ):
                        continue
                    prescription = frozenset(prescription)
                    containing = sum(
                        prescription <= matching for matching in matchings
                    )
                    residual_forbidden = residualise(forbidden, prescription)
                    residual_poly = matching_poly_bruteforce(residual_forbidden)
                    assert (
                        inclusion_exclusion_count(side - rank, residual_poly)
                        == containing
                    )
                    found = True
                    prescription_checks += 1
            assert found or side == 4
    return host_checks, prescription_checks, total_matchings


def main():
    hosts, prescriptions, matchings = check_line_hosts()
    print(
        "verified extension-free line-clean rook rows:",
        check_degree_two_components(),
        "degree-two component polynomials,",
        hosts,
        "line-clean hosts with",
        matchings,
        "perfect matchings, and",
        prescriptions,
        "prescription completion counts",
    )


if __name__ == "__main__":
    main()
