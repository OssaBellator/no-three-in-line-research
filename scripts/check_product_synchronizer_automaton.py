#!/usr/bin/env python3
from collections import deque
from fractions import Fraction
from itertools import product

STATES = [(hall, threshold, shell) for hall in range(2) for threshold in range(4) for shell in range(3)]
START = (0, 0, 0)


def step(state, label):
    hall, threshold, shell = state
    if label == "B" and hall == 1:
        return None
    next_hall = 1 if label == "B" else 0
    next_threshold = (threshold + (2 if label == "B" else 1)) % 4
    next_shell = (shell + (0 if label == "B" else 1)) % 3
    return next_hall, next_threshold, next_shell


def reachable(source):
    seen = {source}
    queue = deque([source])
    while queue:
        state = queue.popleft()
        for label in "AB":
            nxt = step(state, label)
            if nxt is not None and nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen

assert len(STATES) == 24
assert all(len(reachable(state)) == 24 for state in STATES)

shortest = None
shortest_words = []
for length in range(1, 20):
    words = []
    for letters in product("AB", repeat=length):
        word = "".join(letters)
        if "A" not in word or "B" not in word:
            continue
        state = START
        for label in word:
            state = step(state, label)
            if state is None:
                break
        if state == START:
            words.append(word)
    if words:
        shortest = length
        shortest_words = words
        break

assert shortest == 7
assert shortest_words == ["AAAAABA", "AAAABAA", "AAABAAA", "AABAAAA", "ABAAAAA", "BAAAAAA"]

contraction = Fraction(1, 2) ** 6 * Fraction(3, 4)
assert contraction == Fraction(3, 256)
assert contraction > Fraction(1, 100)
assert contraction ** 2 == Fraction(9, 65536)
assert contraction ** 2 < Fraction(1, 100)

for word in shortest_words:
    state = START
    for label in word:
        state = step(state, label)
        assert state is not None
    assert state == START

print({
    "product_states": len(STATES),
    "strongly_connected": True,
    "shortest_mixed_return_length": shortest,
    "shortest_mixed_return_words": len(shortest_words),
    "one_cycle_contraction": str(contraction),
    "two_cycle_contraction": str(contraction ** 2),
    "status": "passed",
})
