#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations
from math import comb

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PHI = (
    (-1, 0, 0, 0),
    (1, 0, 1, 0),
    (0, 1, 0, 0),
    (0, 0, 1, -1),
)
IDENTITY = (0, 1, 2, 3)
LEGAL_TYPES = (
    (2, 3, 0, 1),
    (2, 1, 3, 0),
    (1, 3, 2, 0),
    (1, 2, 0, 3),
    (0, 2, 3, 1),
)
SYMBOLS = (IDENTITY,) + LEGAL_TYPES


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def score(permutation):
    return sum(PHI[row][permutation[row]] for row in range(4))


def matrix_score(layers):
    return sum(score(layer) for layer in layers)


all_layers = tuple(permutations(range(4)))
legal_layers = tuple(layer for layer in all_layers if legal(layer))
assert len(legal_layers) == 18
assert min(map(score, legal_layers)) == 0
assert score(IDENTITY) == -2
assert all(legal(layer) and score(layer) == 0 for layer in LEGAL_TYPES)

# For every forced-alphabet multiset of every audited width, the supplied layers
# themselves give a legal decomposition when there is no identity. If an identity
# is present, the matrix score is negative, whereas every sum of legal layers has
# nonnegative score. This is an exact separating certificate, not a catalogue
# heuristic.
forced_multisets_checked = 0
for width in range(1, 33):
    for indices in combinations_with_replacement(range(len(SYMBOLS)), width):
        layers = tuple(SYMBOLS[index] for index in indices)
        identity_count = indices.count(0)
        value = matrix_score(layers)
        assert value == -2 * identity_count
        if identity_count == 0:
            assert all(legal(layer) for layer in layers)
        else:
            assert value < 0
        forced_multisets_checked += 1


def gap_lengths(length, identity_positions):
    identities = sorted(identity_positions)
    if not identities:
        return (length,)
    gaps = []
    for index, position in enumerate(identities):
        next_position = identities[(index + 1) % len(identities)]
        gap = (next_position - position - 1) % length
        gaps.append(gap)
    assert sum(gaps) == length - len(identities)
    return tuple(gaps)


def legal_windows_from_gaps(gaps, width):
    return sum(max(0, gap - width + 1) for gap in gaps)


small_census = {}
for multiple in range(1, 4):
    length = 8 * multiple
    identity_count = 3 * multiple
    total_position_sets = comb(length, identity_count)
    maxima = [-1] * (length + 1)
    maximizers = [0] * (length + 1)
    for positions in combinations(range(length), identity_count):
        gaps = gap_lengths(length, positions)
        for width in range(1, length + 1):
            value = legal_windows_from_gaps(gaps, width)
            if value > maxima[width]:
                maxima[width] = value
                maximizers[width] = 1
            elif value == maxima[width]:
                maximizers[width] += 1
    for width in range(1, length + 1):
        expected = max(0, 5 * multiple - width + 1)
        assert maxima[width] == expected
        if width == 1 or width > 5 * multiple:
            assert maximizers[width] == total_position_sets
        else:
            assert maximizers[width] == length
    small_census[multiple] = {
        "identity_position_sets": total_position_sets,
        "maximum_by_width": tuple(maxima[1:]),
        "maximizers_by_width": tuple(maximizers[1:]),
    }

# Contiguous identity positions leave one legal gap of length 5K and attain the
# formula at every width. The gap formula also proves optimality: concentrating a
# fixed total gap length maximizes sum max(0,g-w+1).
for multiple in range(1, 65):
    length = 8 * multiple
    gaps = gap_lengths(length, range(3 * multiple))
    for width in range(1, length + 1):
        assert legal_windows_from_gaps(gaps, width) == max(
            0, 5 * multiple - width + 1
        )

print({
    "legal_permutation_layers": len(legal_layers),
    "forced_alphabet_size": len(SYMBOLS),
    "forced_multisets_checked_widths_1_through_32": forced_multisets_checked,
    "all_width_legality_criterion": "legal iff identity count is zero",
    "separating_score": "Phi(matrix)=-2 times identity count; every legal-layer sum has nonnegative score",
    "exact_maximum_legal_windows": "max(0,5K-w+1)",
    "exact_minimum_illegal_windows": "8K-max(0,5K-w+1)",
    "small_multiple_census": small_census,
    "fixed_width_asymptotic_legal_density": "5/8",
    "linear_width_w=rho*K_density": "max(0,(5-rho)/8)",
    "remaining_gap": "leave the forced minimum alphabet or use a genuinely unexposed non-rolling operation; wider rolling memory cannot conceal identity mass",
    "evidence_level": "exact_all_width_separator_and_cycle_gap_obstruction",
    "status": "passed",
})
