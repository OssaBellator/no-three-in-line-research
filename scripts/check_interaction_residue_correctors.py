#!/usr/bin/env python3
from fractions import Fraction
from heapq import heappop, heappush

# edge: name, tail, head, vector label
EDGES = (
    ("A", 0, 0, (1, 2, 0)),
    ("B", 0, 1, (1, 1, 0)),
    ("C", 1, 0, (2, 0, 1)),
    ("D", 1, 1, (1, 0, 2)),
)
LAMBDA = (1, 1, 1)
MU = Fraction(5, 2)
POTENTIAL = (Fraction(1, 2), Fraction(0))
PERIOD = 2
BASE = 0


def scalar(vector):
    return sum(LAMBDA[i] * vector[i] for i in range(3))


def reduced_cost(edge):
    _, tail, head, vector = edge
    return Fraction(scalar(vector)) - MU + POTENTIAL[tail] - POTENTIAL[head]


def residue_shortest_paths():
    start = (BASE, 0)
    dist = {start: Fraction(0)}
    witness = {start: ""}
    queue = [(Fraction(0), BASE, 0)]
    while queue:
        cost, state, residue = heappop(queue)
        if cost != dist[(state, residue)]:
            continue
        for edge in EDGES:
            name, tail, head, _ = edge
            if tail != state:
                continue
            nxt = (head, (residue + 1) % PERIOD)
            candidate = cost + reduced_cost(edge)
            candidate_word = witness[(state, residue)] + name
            if nxt not in dist or candidate < dist[nxt] or (
                candidate == dist[nxt] and candidate_word < witness[nxt]
            ):
                dist[nxt] = candidate
                witness[nxt] = candidate_word
                heappush(queue, (candidate, nxt[0], nxt[1]))
    return dist, witness


def add_vectors(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def dynamic_minimum(length):
    table = {(0, BASE): (Fraction(0), (0, 0, 0), "")}
    for step in range(length):
        next_table = {}
        for (used, state), (cost, vector, word) in table.items():
            assert used == step
            for name, tail, head, label in EDGES:
                if tail != state:
                    continue
                key = (step + 1, head)
                candidate = (cost + scalar(label), add_vectors(vector, label), word + name)
                if key not in next_table or candidate[0] < next_table[key][0] or (
                    candidate[0] == next_table[key][0] and candidate[2] < next_table[key][2]
                ):
                    next_table[key] = candidate
        table = next_table
    return table[(length, BASE)]


def formula_vector(length):
    pairs = length // 2
    base_vector = (3 * pairs, pairs, pairs)
    if length % 2 == 0:
        return base_vector, "BC" * pairs
    return add_vectors((1, 2, 0), base_vector), "A" + "BC" * pairs


def main():
    reduced = {name: reduced_cost(edge) for edge in EDGES for name in (edge[0],)}
    assert reduced == {"A": Fraction(1, 2), "B": 0, "C": 0, "D": Fraction(1, 2)}

    dist, witness = residue_shortest_paths()
    assert dist[(BASE, 0)] == 0
    assert dist[(BASE, 1)] == Fraction(1, 2)
    assert witness[(BASE, 1)] == "A"

    for length in range(1, 65):
        min_cost, min_vector, min_word = dynamic_minimum(length)
        expected_vector, expected_word = formula_vector(length)
        expected_cost = MU * length + (Fraction(1, 2) if length % 2 else 0)
        assert min_cost == expected_cost
        assert scalar(expected_vector) == expected_cost
        assert min_vector == expected_vector
        assert min_word == expected_word

    print({
        "critical_period": PERIOD,
        "minimum_cycle_mean": str(MU),
        "reduced_edge_costs": {k: str(v) for k, v in reduced.items()},
        "residue_defects": {0: "0", 1: "1/2"},
        "odd_residue_corrector": witness[(BASE, 1)],
        "even_formula": "(BC)^(N/2)",
        "odd_formula": "A(BC)^((N-1)/2)",
        "audited_lengths": 64,
    })


if __name__ == "__main__":
    main()
