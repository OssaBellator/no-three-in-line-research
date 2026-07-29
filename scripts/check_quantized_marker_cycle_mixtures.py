#!/usr/bin/env python3
from fractions import Fraction

LENGTHS = (2, 3, 4)
LAMBDA = (Fraction(7, 20), Fraction(1, 3), Fraction(19, 60))
LABELS = (
    (Fraction(2), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(3), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(4)),
)
CYCLE_WORDS = ("AA", "BBB", "CCCC")


def largest_remainder(k: int):
    raw = [Fraction(k) * x for x in LAMBDA]
    counts = [x.numerator // x.denominator for x in raw]
    deficit = k - sum(counts)
    order = sorted(range(len(raw)), key=lambda i: (raw[i] - counts[i], -i), reverse=True)
    for i in order[:deficit]:
        counts[i] += 1
    return tuple(counts)


def average_from_weights(weights):
    denominator = sum(weights[i] * LENGTHS[i] for i in range(3))
    numerator = tuple(
        sum(weights[i] * LABELS[i][j] for i in range(3)) for j in range(3)
    )
    return tuple(x / denominator for x in numerator), denominator


def exact_coordinate_bound(p, j):
    target_rate, d0 = average_from_weights(LAMBDA)
    rate, d1 = average_from_weights(p)
    dp = abs(p[j] - LAMBDA[j])
    dd = abs(d1 - d0)
    bound = (LENGTHS[j] * dp * d0 + LENGTHS[j] * LAMBDA[j] * dd) / (d0 * d1)
    return abs(rate[j] - target_rate[j]), bound


def main():
    assert sum(LAMBDA) == 1
    target_rate, target_length = average_from_weights(LAMBDA)
    assert target_rate == (Fraction(21, 89), Fraction(30, 89), Fraction(38, 89))
    assert target_length == Fraction(89, 30)

    max_l1 = Fraction(0)
    for k in range(1, 121):
        counts = largest_remainder(k)
        assert sum(counts) == k
        p = tuple(Fraction(c, k) for c in counts)
        for i in range(3):
            assert abs(p[i] - LAMBDA[i]) < Fraction(1, k)
        l1 = sum(abs(p[i] - LAMBDA[i]) for i in range(3))
        max_l1 = max(max_l1, l1)
        for j in range(3):
            err, bound = exact_coordinate_bound(p, j)
            assert err <= bound

        word = "".join(CYCLE_WORDS[i] * counts[i] for i in range(3))
        assert len(word) == sum(counts[i] * LENGTHS[i] for i in range(3))
        action_counts = tuple(word.count(letter) for letter in "ABC")
        rate, _ = average_from_weights(p)
        assert tuple(Fraction(action_counts[j], len(word)) for j in range(3)) == rate

    exact_counts = largest_remainder(60)
    assert exact_counts == (21, 20, 19)
    exact_p = tuple(Fraction(c, 60) for c in exact_counts)
    exact_rate, _ = average_from_weights(exact_p)
    exact_period = sum(exact_counts[i] * LENGTHS[i] for i in range(3))
    assert exact_rate == target_rate
    assert exact_period == 178

    sample_k = 17
    sample_counts = largest_remainder(sample_k)
    sample_rate, _ = average_from_weights(tuple(Fraction(c, sample_k) for c in sample_counts))
    sample_period = sum(sample_counts[i] * LENGTHS[i] for i in range(3))
    print({
        "target_cycle_weights": tuple(str(x) for x in LAMBDA),
        "target_rate": tuple(str(x) for x in target_rate),
        "sample_K": sample_k,
        "sample_counts": sample_counts,
        "sample_period": sample_period,
        "sample_rate": tuple(str(x) for x in sample_rate),
        "exact_K": 60,
        "exact_counts": exact_counts,
        "exact_period": exact_period,
        "audited_denominators": 120,
        "maximum_l1_weight_error": str(max_l1),
    })


if __name__ == "__main__":
    main()
