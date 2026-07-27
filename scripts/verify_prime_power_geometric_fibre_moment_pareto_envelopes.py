#!/usr/bin/env python3
"""Finite checks for CMR1854--CMR1861."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import comb, gcd

Edge = tuple[int, int]
Point = tuple[int, int]
Line = tuple[int, int, int]
Moment = tuple[int, int, int]


EXPECTED = {
    4: {
        "host_count": 86,
        "line_count": 54,
        "pareto": {
            1: (14, 2, 2, 2, (32, 6, 0)),
            2: (40, 3, 3, 2, (53, 12, 1)),
            3: (20, 2, 2, 3, (62, 17, 1)),
            4: (9, 2, 2, 4, (69, 21, 1)),
            5: (2, 1, 1, 0, (70, 25, 5)),
            6: (1, 1, 1, 0, (77, 30, 5)),
        },
        "length_pareto": {1: 3, 2: 8, 3: 4, 4: 2, 5: 2, 6: 1},
        "pareto_total": 11,
        "active_total": 11,
        "length_total": 20,
        "global_terminal": 4,
    },
    5: {
        "host_count": 654,
        "line_count": 130,
        "pareto": {
            8: (21, 3, 3, 4, (163, 55, 4)),
            9: (18, 3, 3, 3, (163, 55, 5)),
            10: (93, 7, 4, 3, (174, 64, 3)),
            11: (48, 3, 3, 1, (178, 70, 7)),
            12: (104, 9, 6, 4, (181, 66, 5)),
            13: (30, 4, 3, 4, (185, 72, 5)),
            14: (111, 4, 3, 3, (189, 77, 7)),
            15: (50, 4, 3, 16, (191, 74, 5)),
            16: (63, 3, 2, 1, (194, 84, 9)),
            17: (12, 2, 2, 6, (195, 81, 9)),
            18: (24, 4, 3, 3, (198, 83, 7)),
            19: (15, 2, 2, 8, (200, 86, 10)),
            20: (45, 3, 2, 1, (203, 91, 10)),
            22: (6, 2, 2, 9, (205, 87, 7)),
            24: (1, 1, 1, 0, (201, 84, 7)),
            25: (6, 2, 2, 1, (212, 97, 11)),
            26: (6, 1, 1, 0, (212, 97, 11)),
            33: (1, 1, 1, 0, (220, 104, 12)),
        },
        "length_pareto": {
            8: 14,
            9: 9,
            10: 36,
            11: 13,
            12: 40,
            13: 16,
            14: 21,
            15: 17,
            16: 18,
            17: 8,
            18: 9,
            19: 4,
            20: 8,
            22: 5,
            24: 1,
            25: 3,
            26: 2,
            33: 1,
        },
        "pareto_total": 58,
        "active_total": 46,
        "length_total": 225,
        "global_terminal": 16,
    },
}


def partial_matchings(edges: set[Edge]) -> list[tuple[Edge, ...]]:
    edge_list = sorted(edges)
    output: list[tuple[Edge, ...]] = []

    def recurse(
        index: int,
        chosen: list[Edge],
        used_left: set[int],
        used_right: set[int],
    ) -> None:
        if index == len(edge_list):
            output.append(tuple(chosen))
            return
        recurse(index + 1, chosen, used_left, used_right)
        left, right = edge_list[index]
        if left not in used_left and right not in used_right:
            chosen.append((left, right))
            used_left.add(left)
            used_right.add(right)
            recurse(index + 1, chosen, used_left, used_right)
            used_right.remove(right)
            used_left.remove(left)
            chosen.pop()

    recurse(0, [], set(), set())
    return output


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def line_key(first: Point, second: Point) -> Line:
    x_1, y_1 = first
    x_2, y_2 = second
    a = y_2 - y_1
    b = x_1 - x_2
    c = a * x_1 + b * y_1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c
    return a, b, c


def nonaxis_lines(side: int) -> dict[Line, tuple[Point, ...]]:
    points = [(left, right) for left in range(side) for right in range(side)]
    output: dict[Line, tuple[Point, ...]] = {}
    for first, second in combinations(points, 2):
        key = line_key(first, second)
        a, b, c = key
        if a == 0 or b == 0:
            continue
        cells = tuple(
            point for point in points if a * point[0] + b * point[1] == c
        )
        if len(cells) >= 2:
            output[key] = cells
    return output


def height_score(moment: Moment, height: int) -> int:
    m_1, m_2, m_3 = moment
    return comb(height, 2) * m_1 + height * m_2 + m_3


def pareto_vectors(vectors: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    output: set[tuple[int, ...]] = set()
    for vector in vectors:
        dominated = any(
            all(other[index] >= vector[index] for index in range(len(vector)))
            and any(other[index] > vector[index] for index in range(len(vector)))
            for other in vectors
        )
        if not dominated:
            output.add(vector)
    return output


def terminal_from(
    vectors: set[Moment],
    candidate: Moment,
    height: int,
) -> bool:
    for competitor in vectors:
        if height_score(candidate, height) < height_score(competitor, height):
            return False
        delta_m_1 = candidate[0] - competitor[0]
        delta_m_2 = candidate[1] - competitor[1]
        if delta_m_1 < 0:
            return False
        if height * delta_m_1 + delta_m_2 < 0:
            return False
    return True


def length_signature(
    length_moments: dict[int, Moment],
    lengths: tuple[int, ...],
) -> tuple[int, ...]:
    output: list[int] = []
    for length in lengths:
        output.extend(length_moments.get(length, (0, 0, 0)))
    return tuple(output)


def main() -> None:
    raw_hosts_checked = 0
    host_line_capacities = 0
    dominance_checks = 0
    height_phase_checks = 0
    terminal_checks = 0
    length_signature_checks = 0

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        lines = nonaxis_lines(side)
        lengths = tuple(sorted({len(cells) for cells in lines.values()}))

        records: list[tuple[int, Moment, tuple[int, ...]]] = []
        for deletion_tuple in partial_matchings(allowed):
            forbidden = opposite | target | set(deletion_tuple)
            responses = perfect_matchings(side, forbidden)
            if not responses:
                continue

            capacities: list[int] = []
            by_length: dict[int, list[int]] = defaultdict(list)
            for cells in lines.values():
                cell_set = set(cells)
                capacity = max(
                    sum(
                        (left, permutation[left]) in cell_set
                        for left in range(side)
                    )
                    for permutation in responses
                )
                capacities.append(capacity)
                by_length[len(cells)].append(capacity)
                host_line_capacities += 1

            moment: Moment = tuple(
                sum(comb(capacity, rank) for capacity in capacities)
                for rank in (1, 2, 3)
            )  # type: ignore[assignment]
            length_moments = {
                length: tuple(
                    sum(comb(capacity, rank) for capacity in values)
                    for rank in (1, 2, 3)
                )
                for length, values in by_length.items()
            }
            signature = length_signature(length_moments, lengths)
            records.append((len(responses), moment, signature))
            raw_hosts_checked += 1

        expected = EXPECTED[side]
        assert len(records) == expected["host_count"]
        assert len(lines) == expected["line_count"]

        by_denominator: dict[int, list[tuple[int, Moment, tuple[int, ...]]]] = defaultdict(list)
        for record in records:
            by_denominator[record[0]].append(record)

        pareto_total = 0
        active_total = 0
        length_total = 0
        maximum_terminal_height = 0

        for denominator, group in sorted(by_denominator.items()):
            host_count, pareto_count, active_count, terminal_height, terminal = expected[
                "pareto"
            ][denominator]
            assert len(group) == host_count

            raw_moments = {record[1] for record in group}
            pareto = pareto_vectors(raw_moments)
            assert len(pareto) == pareto_count
            assert terminal in pareto
            pareto_total += len(pareto)

            for vector in raw_moments:
                assert any(
                    all(candidate[index] >= vector[index] for index in range(3))
                    for candidate in pareto
                )
                dominance_checks += 1

            assert terminal_from(pareto, terminal, terminal_height)
            for earlier_height in range(terminal_height):
                assert not any(
                    terminal_from(pareto, candidate, earlier_height)
                    for candidate in pareto
                )
            terminal_checks += 1
            maximum_terminal_height = max(maximum_terminal_height, terminal_height)

            active: set[Moment] = set()
            for height in range(terminal_height + 1):
                maximum = max(height_score(vector, height) for vector in pareto)
                active.update(
                    vector
                    for vector in pareto
                    if height_score(vector, height) == maximum
                )
                height_phase_checks += len(pareto)
            active.add(terminal)
            assert len(active) == active_count
            active_total += len(active)

            for height in range(terminal_height, terminal_height + 50):
                assert height_score(terminal, height) == max(
                    height_score(vector, height) for vector in pareto
                )
                height_phase_checks += len(pareto)

            raw_signatures = {record[2] for record in group}
            length_pareto = pareto_vectors(raw_signatures)
            assert len(length_pareto) == expected["length_pareto"][denominator]
            length_total += len(length_pareto)
            for signature in raw_signatures:
                assert any(
                    all(
                        candidate[index] >= signature[index]
                        for index in range(len(signature))
                    )
                    for candidate in length_pareto
                )
                length_signature_checks += 1

        assert pareto_total == expected["pareto_total"]
        assert active_total == expected["active_total"]
        assert length_total == expected["length_total"]
        assert maximum_terminal_height == expected["global_terminal"]

    assert raw_hosts_checked == 740
    assert host_line_capacities == 89664
    print(
        "verified geometric fibre moment Pareto envelopes: "
        f"{raw_hosts_checked} raw hosts, {host_line_capacities} host-line capacities, "
        f"{dominance_checks} moment-dominance checks, {height_phase_checks} "
        f"integer-height phase checks, {terminal_checks} terminal certificates and "
        f"{length_signature_checks} length-signature dominance checks"
    )


if __name__ == "__main__":
    main()
