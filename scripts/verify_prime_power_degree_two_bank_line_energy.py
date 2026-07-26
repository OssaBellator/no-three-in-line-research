#!/usr/bin/env python3
"""Finite checks for CMR1222--CMR1229."""

from itertools import combinations, permutations
from math import comb, factorial, gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def derangements(side):
    return [
        permutation
        for permutation in permutations(range(side))
        if all(permutation[row] != row for row in range(side))
    ]


def line_key(first, second):
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def board_lines(side):
    cells = [(x, y) for x in range(side) for y in range(side)]
    keys = {line_key(first, second) for first, second in combinations(cells, 2)}
    return {
        key: frozenset(
            cell for cell in cells if key[0] * cell[0] + key[1] * cell[1] + key[2] == 0
        )
        for key in keys
    }


def compatible(edges):
    return len({row for row, _ in edges}) == len(edges) and len(
        {column for _, column in edges}
    ) == len(edges)


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def check_exact_line_energies():
    rng = random.Random(1222)
    checked = 0
    triples_checked = 0
    for side in range(4, 8):
        cells = [(x, y) for x in range(side) for y in range(side)]
        lines = board_lines(side)
        opposite = matching(tuple(range(side)))
        old_list = derangements(side)
        if side >= 6:
            old_list = rng.sample(old_list, min(18, len(old_list)))
        for old_permutation in old_list:
            old_matching = matching(old_permutation)
            target_edge = rng.choice(tuple(old_matching))
            extensions = [
                permutation
                for permutation in derangements(side)
                if target_edge in matching(permutation)
            ]
            extensions = rng.sample(extensions, min(4, len(extensions)))
            for forbidden in extensions:
                forbidden_edges = matching(forbidden)
                graph = set(cells) - set(opposite) - set(forbidden_edges)
                old_allowed = set(old_matching) & graph
                old_state = set(opposite) | set(old_matching)

                line_v1 = 0
                line_v2 = 0
                line_v3 = 0
                rank_one_owner = {edge: 0 for edge in graph}
                for line_cells in lines.values():
                    o_cells = set(opposite) & set(line_cells)
                    g_cells = graph & set(line_cells)
                    m_cells = old_allowed & set(line_cells)
                    c2 = sum(compatible(pair) for pair in combinations(g_cells, 2))
                    c3 = sum(compatible(triple) for triple in combinations(g_cells, 3))
                    line_v1 += comb(len(o_cells), 2) * (len(g_cells) - len(m_cells))
                    line_v2 += len(o_cells) * (c2 - comb(len(m_cells), 2))
                    line_v3 += c3 - comb(len(m_cells), 3)
                    for edge in g_cells - m_cells:
                        rank_one_owner[edge] += comb(len(o_cells), 2)

                direct = [0, 0, 0, 0]
                for triple in combinations(cells, 3):
                    key = line_key(triple[0], triple[1])
                    if triple[2] not in lines[key]:
                        continue
                    triple_set = set(triple)
                    residual = triple_set - set(opposite)
                    rank = len(residual)
                    if rank == 0 or triple_set <= old_state:
                        continue
                    if not residual <= graph or not compatible(residual):
                        continue
                    direct[rank] += 1
                    triples_checked += 1

                assert direct[1] == line_v1
                assert direct[2] == line_v2
                assert direct[3] == line_v3
                assert sum(rank_one_owner.values()) == line_v1
                checked += 1
    return checked, triples_checked


def check_pair_stock_and_caps():
    rng = random.Random(1225)
    checked = 0
    for side in range(4, 100):
        edge_count = side * (side - 2)
        pair_stock = comb(edge_count, 2) - 2 * side * comb(side - 2, 2)
        factorized = side * (side - 2) * (side * side - 4 * side + 5) // 2
        assert pair_stock == factorized
        for _ in range(200):
            old_allowed_size = rng.randint(0, side - 1)
            pair_plus = pair_stock - comb(old_allowed_size, 2)
            rho = rng.randint(0, side)
            gamma = rng.randint(0, side)
            gamma_plus = rng.randint(0, gamma)
            v1_bound = gamma_plus * comb(side, 2)
            v2_bound = rho * pair_plus
            v3_bound = max(0, gamma - 2) * min(pair_stock / 3, pair_plus / 2)
            v1 = rng.randint(0, v1_bound)
            v2 = rng.randint(0, v2_bound)
            v3 = rng.randint(0, int(v3_bound))
            exact_score = (
                v1 / side
                + v2 / falling(side, 2)
                + v3 / falling(side, 3)
            )
            cap_score = (
                gamma_plus * comb(side, 2) / side
                + rho * pair_plus / falling(side, 2)
                + max(0, gamma - 2)
                * min(pair_stock / 3, pair_plus / 2)
                / falling(side, 3)
            )
            assert exact_score <= cap_score + 1e-12
            checked += 1
    return checked


def check_owner_line_partition():
    rng = random.Random(1228)
    checked = 0
    atoms = 0
    for side in range(4, 100):
        for _ in range(200):
            owner_counts = {}
            total = [0, 0, 0, 0]
            for _atom in range(rng.randint(0, 400)):
                rank = rng.randint(1, 3)
                line = rng.randint(0, side * side)
                prescription = tuple(sorted(rng.sample(range(side * side), rank)))
                owner = prescription[0]
                owner_counts.setdefault((line, owner), [0, 0, 0, 0])[rank] += 1
                total[rank] += 1
                atoms += 1
            global_score = sum(total[rank] / falling(side, rank) for rank in (1, 2, 3))
            local_score = sum(
                sum(counts[rank] / falling(side, rank) for rank in (1, 2, 3))
                for counts in owner_counts.values()
            )
            assert abs(global_score - local_score) < 1e-12
            checked += 1
    return checked, atoms


def main():
    exact = check_exact_line_energies()
    owners = check_owner_line_partition()
    print(
        "verified corrected degree-two bank line energy:",
        exact[0],
        "geometric banks with",
        exact[1],
        "new candidate triples,",
        check_pair_stock_and_caps(),
        "new-pair stock and cap cases, and",
        owners[0],
        "line-owner decompositions over",
        owners[1],
        "atoms",
    )


if __name__ == "__main__":
    main()
