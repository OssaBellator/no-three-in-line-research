#!/usr/bin/env python3
from fractions import Fraction

COUNTS = (2, 2, 1, 1, 1, 1, 1, 1)
GROUP_SIZE = 8
BLOCK_TOTAL = sum(COUNTS)


def xor_convolution(a, b):
    return tuple(sum(a[x] * b[s ^ x] for x in range(GROUP_SIZE)) for s in range(GROUP_SIZE))


def walsh(values):
    out = []
    for character in range(GROUP_SIZE):
        total = 0
        for x, value in enumerate(values):
            sign = -1 if (character & x).bit_count() % 2 else 1
            total += sign * value
        out.append(total)
    return tuple(out)


def walsh_inverse(values):
    transformed = walsh(values)
    assert all(x % GROUP_SIZE == 0 for x in transformed)
    return tuple(x // GROUP_SIZE for x in transformed)


def main():
    spectrum = walsh(COUNTS)
    assert spectrum == (10, 0, 2, 0, 2, 0, 2, 0)
    normalized_nontrivial = [Fraction(abs(x), BLOCK_TOTAL) for x in spectrum[1:]]
    rho = max(normalized_nontrivial)
    assert rho == Fraction(1, 5)

    current = (1,) + (0,) * (GROUP_SIZE - 1)
    first_under_one_percent = None
    exact_deviations = []
    for n in range(1, 13):
        current = xor_convolution(current, COUNTS)
        powered_spectrum = tuple(x ** n for x in spectrum)
        reconstructed = walsh_inverse(powered_spectrum)
        assert reconstructed == current
        total = BLOCK_TOTAL ** n
        deviations = [abs(Fraction(c, total) - Fraction(1, GROUP_SIZE)) for c in current]
        actual = max(deviations)
        spectral_bound = Fraction(1, GROUP_SIZE) * sum(x ** n for x in normalized_nontrivial)
        coarse_bound = Fraction(GROUP_SIZE - 1, GROUP_SIZE) * rho ** n
        assert actual <= spectral_bound <= coarse_bound
        assert actual == Fraction(3, 8 * (5 ** n))
        exact_deviations.append(actual)
        if first_under_one_percent is None and actual <= Fraction(1, 100):
            first_under_one_percent = n

    assert first_under_one_percent == 3
    d = 20
    n = first_under_one_percent
    load_bound = Fraction(1, d) * (Fraction(1, GROUP_SIZE) + Fraction(3, 8 * (5 ** n)))
    assert load_bound == Fraction(16, 2500)

    print({
        "block_total": BLOCK_TOTAL,
        "walsh_spectrum": spectrum,
        "nontrivial_radius": str(rho),
        "exact_deviations_n1_to_n5": [str(x) for x in exact_deviations[:5]],
        "one_percent_horizon": first_under_one_percent,
        "reverse_load_bound_at_horizon_d20": str(load_bound),
        "audited_powers": 12,
    })


if __name__ == "__main__":
    main()
