#!/usr/bin/env python3
from fractions import Fraction

EDGES = [
    ("A", 0, 0, (Fraction(1), Fraction(2), Fraction(0))),
    ("B", 0, 1, (Fraction(1), Fraction(0), Fraction(1))),
    ("C", 1, 0, (Fraction(2), Fraction(1), Fraction(0))),
    ("D", 1, 1, (Fraction(1), Fraction(0), Fraction(2))),
]

CYCLE_MEANS = {
    "A": (Fraction(1), Fraction(2), Fraction(0)),
    "D": (Fraction(1), Fraction(0), Fraction(2)),
    "BC": (Fraction(3, 2), Fraction(1, 2), Fraction(1, 2)),
}
TARGET = CYCLE_MEANS["BC"]

feasible_weights = []
for denominator in range(1, 41):
    for i in range(denominator + 1):
        for j in range(denominator - i + 1):
            k = denominator - i - j
            weights = (Fraction(i, denominator), Fraction(j, denominator), Fraction(k, denominator))
            means = list(CYCLE_MEANS.values())
            vector = tuple(sum(weights[t] * means[t][q] for t in range(3)) for q in range(3))
            if all(vector[q] <= TARGET[q] for q in range(3)):
                feasible_weights.append((weights, vector))
                assert weights == (0, 0, 1)
assert feasible_weights

scalar_means = {name: sum(vector) for name, vector in CYCLE_MEANS.items()}
assert scalar_means == {"A": 3, "D": 3, "BC": Fraction(5, 2)}


def closed_walks(length):
    current = [(0, (), (Fraction(0), Fraction(0), Fraction(0)))]
    for _ in range(length):
        nxt = []
        for state, word, vector in current:
            for name, source, target, edge_vector in EDGES:
                if source == state:
                    nxt.append((
                        target,
                        word + (name,),
                        tuple(vector[i] + edge_vector[i] for i in range(3)),
                    ))
        current = nxt
    return [(word, vector) for state, word, vector in current if state == 0]

for length in range(2, 17):
    walks = closed_walks(length)
    best_scalar, best_word, best_vector = min((sum(vector), word, vector) for word, vector in walks)
    if length % 2 == 0:
        assert best_word == tuple("BC" * (length // 2))
        assert tuple(value / length for value in best_vector) == TARGET
        assert best_scalar / length == Fraction(5, 2)
    else:
        expected = ("A",) + tuple("BC" * ((length - 1) // 2))
        assert best_word == expected
        assert best_scalar / length - Fraction(5, 2) == Fraction(1, 2 * length)

print({
    "cycle_means": {k: tuple(map(str, v)) for k, v in CYCLE_MEANS.items()},
    "unique_target_cycle": "BC",
    "target_rate": tuple(map(str, TARGET)),
    "scalar_minimum": str(Fraction(5, 2)),
    "verified_closed_walk_lengths": 16,
    "odd_length_overhead": "1/(2N)",
})
