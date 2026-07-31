#!/usr/bin/env python3
from fractions import Fraction

C1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
C2 = ((1, 1), (-1, 0), (0, -1))
FACETS = (
    (Fraction(1, 48), Fraction(1, 96)),
    (Fraction(-1, 96), Fraction(1, 48)),
    (Fraction(1, 120), Fraction(-1, 120)),
)


def rotate(cycle, phase):
    return cycle[phase:] + cycle[:phase]


def prefixes(cycle):
    out = [(0, 0)]
    x = y = 0
    for dx, dy in cycle:
        x += dx
        y += dy
        out.append((x, y))
    assert out[-1] == (0, 0)
    return out


def common_width(cycles):
    points = [point for cycle in cycles for point in prefixes(cycle)]
    widths = tuple(max(point[j] for point in points) - min(point[j] for point in points) for j in range(2))
    return widths


phase_data = []
for p1 in range(len(C1)):
    for p2 in range(len(C2)):
        cycles = (rotate(C1, p1), rotate(C2, p2))
        widths = common_width(cycles)
        phase_data.append(((p1, p2), widths, cycles))

best = min(max(widths) for _, widths, _ in phase_data)
optimal = [entry for entry in phase_data if max(entry[1]) == best]
assert best == 1
assert len(optimal) == 3
phase, widths, cycles = min(optimal)
assert phase == (0, 0)
assert widths == (1, 1)

facet_bounds = [sum(abs(coefficient) * width for coefficient, width in zip(facet, widths)) for facet in FACETS]
assert max(facet_bounds) == Fraction(1, 32)

# Arbitrary concatenation of the certified cycles; every interval is checked in quotient
# coordinates and after applying each actual threshold facet.
word = []
pattern = (0, 1, 1, 0, 1)
for index in pattern * 10:
    word.extend(cycles[index])

prefix = [(0, 0)]
x = y = 0
for dx, dy in word:
    x += dx
    y += dy
    prefix.append((x, y))

intervals_checked = 0
for left in range(len(prefix)):
    for right in range(left, len(prefix)):
        residual = (prefix[right][0] - prefix[left][0], prefix[right][1] - prefix[left][1])
        assert abs(residual[0]) <= widths[0]
        assert abs(residual[1]) <= widths[1]
        for facet, bound in zip(FACETS, facet_bounds):
            value = sum(coefficient * coordinate for coefficient, coordinate in zip(facet, residual))
            assert abs(value) <= bound
        intervals_checked += 1

for n in range(96, 1001):
    assert max(facet_bounds) + Fraction(1, n) <= Fraction(1, 24)

print({
    "phase_pairs": len(phase_data),
    "optimal_phase_pairs": len(optimal),
    "common_width": widths,
    "facet_loss": str(max(facet_bounds)),
    "derived_threshold_row_from": 96,
    "derived_threshold_row": "1/24",
    "intervals_checked": intervals_checked,
    "status": "passed",
})
