#!/usr/bin/env python3
"""Finite audit for AC3vq--AC3vu."""

from itertools import product
import random

SEED = 20260728


def normalized_shape(increments):
    prefixes = [0]
    for delta in increments:
        prefixes.append(prefixes[-1] + delta)
    minimum = min(prefixes)
    shape = [value - minimum for value in prefixes]
    return prefixes, minimum, shape


def guard_threshold(shape, thresholds):
    guarded = [
        threshold - shape[index]
        for index, threshold in enumerate(thresholds)
        if threshold is not None
    ]
    return max(guarded) if guarded else None


def guards_hold(base, shape, thresholds):
    return all(
        threshold is None or base + shape[index] >= threshold
        for index, threshold in enumerate(thresholds)
    )


def main():
    rng = random.Random(SEED)
    counters = {
        "words": 0,
        "guard_tests": 0,
        "zero_drift": 0,
        "positive_drift": 0,
        "negative_drift": 0,
        "negative_executions": 0,
    }

    # Exhaust bounded words over increments in [-2,2].
    for length in range(1, 7):
        for increments in product(range(-2, 3), repeat=length):
            prefixes, minimum, shape = normalized_shape(increments)
            assert min(shape) == 0
            assert max(shape) <= length * 2
            assert all(shape[index] == prefixes[index] - minimum for index in range(length + 1))

            # Sample lower-guard patterns on all prefixes.
            for _ in range(4):
                thresholds = [
                    None if rng.random() < 0.35 else rng.randint(-5, 7)
                    for _ in range(length + 1)
                ]
                threshold = guard_threshold(shape, thresholds)
                if threshold is None:
                    for base in range(-8, 9):
                        assert guards_hold(base, shape, thresholds)
                        counters["guard_tests"] += 1
                else:
                    for base in range(threshold - 3, threshold + 5):
                        assert guards_hold(base, shape, thresholds) == (base >= threshold)
                        counters["guard_tests"] += 1

                drift = prefixes[-1]
                counters["words"] += 1
                if drift == 0:
                    counters["zero_drift"] += 1
                    if threshold is not None:
                        for base in range(threshold, threshold + 4):
                            assert base + drift == base
                            assert guards_hold(base, shape, thresholds)
                elif drift > 0:
                    counters["positive_drift"] += 1
                    base = threshold if threshold is not None else -5
                    values = [base + step * drift for step in range(6)]
                    assert all(values[index + 1] > values[index] for index in range(5))
                else:
                    counters["negative_drift"] += 1
                    if threshold is None:
                        continue
                    base = threshold + rng.randint(0, 20)
                    legal_count = (base - threshold) // abs(drift) + 1
                    for execution in range(legal_count):
                        assert base + execution * drift >= threshold
                    assert base + legal_count * drift < threshold
                    counters["negative_executions"] += legal_count

    print("AC one-sided balance-tail audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
