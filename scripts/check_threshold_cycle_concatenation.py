#!/usr/bin/env python3
from itertools import product

CYCLES = {
    "C1": ((1, 0), (0, 1), (-1, 0), (0, -1)),
    "C2": ((1, 1), (-1, 0), (0, -1)),
}


def rotations(seq):
    seq = tuple(seq)
    return [seq[i:] + seq[:i] for i in range(len(seq))]


def prefix_states(seq):
    x = y = 0
    out = [(0, 0)]
    for a, b in seq:
        x += a
        y += b
        out.append((x, y))
    assert (x, y) == (0, 0)
    return out


def common_box_width(seqs):
    pts = []
    for seq in seqs:
        pts.extend(prefix_states(seq))
    widths = tuple(max(p[i] for p in pts) - min(p[i] for p in pts) for i in range(2))
    return max(widths), widths, pts

records = []
for i, c1 in enumerate(rotations(CYCLES["C1"])):
    for j, c2 in enumerate(rotations(CYCLES["C2"])):
        value, widths, pts = common_box_width((c1, c2))
        records.append((value, i, j, widths, c1, c2, pts))

best = min(r[0] for r in records)
optimal = [r for r in records if r[0] == best]
assert best == 1
assert len(optimal) == 3

# The lexicographic optimal phases keep every global prefix in [0,1]^2.
lex = min(optimal, key=lambda r: (r[1], r[2]))
_, i, j, widths, c1, c2, pts = lex
assert widths == (1, 1)
assert all(0 <= x <= 1 and 0 <= y <= 1 for x, y in pts)

# Any concatenation of the selected zero-sum cycles stays in the same common box.
word = (c1 + c2 + c2 + c1) * 25
states = prefix_states(word)
assert all(0 <= x <= 1 and 0 <= y <= 1 for x, y in states)
for a in range(len(states)):
    for b in range(a, min(len(states), a + 30)):
        dx = states[b][0] - states[a][0]
        dy = states[b][1] - states[a][1]
        assert max(abs(dx), abs(dy)) <= 1

print({
    "phase_pairs_checked": len(records),
    "optimal_phase_pairs": len(optimal),
    "minimum_common_box_width": best,
    "lexicographic_phases": (i, j),
    "repeated_slots_checked": len(word),
    "status": "passed",
})
