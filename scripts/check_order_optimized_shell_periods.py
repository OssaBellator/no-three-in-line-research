#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

MULTISET = "AABBC"
ACTIONS = {
    "A": (1, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
}
TARGET = (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5))
WORDS = sorted(set(permutations(MULTISET)))
assert len(WORDS) == 30


def buffer(word, horizon=None):
    if horizon is None:
        horizon = len(word)
    cumulative = [Fraction(0), Fraction(0), Fraction(0)]
    minimum = [Fraction(0), Fraction(0), Fraction(0)]
    for t in range(horizon):
        action = ACTIONS[word[t % len(word)]]
        for j in range(3):
            cumulative[j] += action[j] - TARGET[j]
            minimum[j] = min(minimum[j], cumulative[j])
    b = tuple(-x for x in minimum)
    return b, sum(b)

values = {"".join(word): buffer(word) for word in WORDS}
best = min(value[1] for value in values.values())
optimal = sorted(word for word, value in values.items() if value[1] == best)
assert best == Fraction(6, 5)
assert len(optimal) == 10
assert optimal[0] == "ABABC"
assert values["ABABC"][0] == (Fraction(0), Fraction(2, 5), Fraction(4, 5))
assert all(max(values[word][0]) < 1 for word in optimal)

word = tuple("ABABC")
b, _ = buffer(word)
account = list(b)
for t in range(200):
    action = ACTIONS[word[t % 5]]
    for j in range(3):
        account[j] += action[j] - TARGET[j]
        assert account[j] >= 0, (t, j, account[j])

print({
    "period_words_checked": len(WORDS),
    "minimum_l1_buffer": str(best),
    "optimal_words": len(optimal),
    "lexicographic_optimum": optimal[0],
    "lexicographic_buffer": tuple(str(x) for x in values[optimal[0]][0]),
    "prefixes_checked": 200,
    "status": "passed",
})
