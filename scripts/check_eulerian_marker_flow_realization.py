#!/usr/bin/env python3
from collections import Counter, defaultdict
from fractions import Fraction

EDGES = []


def add(u, v, label, multiplicity):
    for _ in range(multiplicity):
        EDGES.append((u, v, label))


add(0, 1, "A", 2)
add(1, 0, "B", 2)
add(1, 2, "A", 1)
add(2, 1, "C", 1)
add(2, 0, "B", 2)
add(0, 2, "A", 2)

outdeg = Counter(u for u, _, _ in EDGES)
indeg = Counter(v for _, v, _ in EDGES)
assert outdeg == indeg

adj = defaultdict(list)
for idx, (u, v, label) in enumerate(EDGES):
    adj[u].append((idx, v, label))
for u in adj:
    adj[u].sort(reverse=True)

stack = [(0, None)]
circuit = []
while stack:
    u, incoming = stack[-1]
    if adj[u]:
        idx, v, label = adj[u].pop()
        stack.append((v, (idx, u, v, label)))
    else:
        _, edge = stack.pop()
        if edge is not None:
            circuit.append(edge)
circuit.reverse()

assert len(circuit) == len(EDGES)
assert len({edge[0] for edge in circuit}) == len(EDGES)
assert all(circuit[i][2] == circuit[(i + 1) % len(circuit)][1] for i in range(len(circuit)))

word = [edge[3] for edge in circuit]
counts = Counter(word)
period = len(word)
frequencies = {a: Fraction(counts[a], period) for a in sorted(counts)}
assert frequencies == {"A": Fraction(1, 2), "B": Fraction(2, 5), "C": Fraction(1, 10)}

bounds = {}
for action, freq in frequencies.items():
    centered = [Fraction(0)]
    seen = 0
    for t, symbol in enumerate(word, 1):
        seen += symbol == action
        centered.append(Fraction(seen) - t * freq)
    fixed_phase = max(abs(x) for x in centered)
    arbitrary_phase = max(centered) - min(centered)
    bounds[action] = (fixed_phase, arbitrary_phase)

assert bounds == {
    "A": (Fraction(1, 2), Fraction(1, 2)),
    "B": (Fraction(4, 5), Fraction(6, 5)),
    "C": (Fraction(1, 2), Fraction(9, 10)),
}

for repetitions in range(7):
    long_word = word * repetitions + word[:7]
    for action, freq in frequencies.items():
        deviation = Fraction(long_word.count(action)) - len(long_word) * freq
        assert abs(deviation) <= bounds[action][0]

print({
    "period": period,
    "word": "".join(word),
    "frequencies": {k: str(v) for k, v in frequencies.items()},
    "fixed_phase_bounds": {k: str(v[0]) for k, v in bounds.items()},
    "arbitrary_phase_bounds": {k: str(v[1]) for k, v in bounds.items()},
})
