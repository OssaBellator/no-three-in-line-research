#!/usr/bin/env python3
"""Finite audit for BDA5bv--BDA5bz.

The script checks finite closed integer walks. The Markdown note contains the
arbitrary-size proof.
"""

from itertools import product
from math import ceil, log2


def canonical_crossing(increments, denominator):
    values = [0]
    for increment in increments:
        values.append(values[-1] + increment)
    assert values[-1] == 0

    floors = [value // denominator for value in values[:-1]]
    minimum = min(floors)
    for index, increment in enumerate(increments):
        if (
            values[index] // denominator > minimum
            and values[index + 1] // denominator == minimum
        ):
            assert increment < 0
            return index
    return None


def main():
    cycles = compensation_pairs = dyadic_checks = 0

    for length in range(2, 8):
        for prefix in product(range(-4, 5), repeat=length - 1):
            last = -sum(prefix)
            if not -4 <= last <= 4:
                continue
            increments = prefix + (last,)
            if all(increment == 0 for increment in increments):
                continue

            for denominator in range(1, 5):
                index = canonical_crossing(increments, denominator)
                if index is None:
                    continue

                jump = -increments[index]
                positives = [
                    increment
                    for edge, increment in enumerate(increments)
                    if edge != index and increment > 0
                ]
                assert positives
                source = max(positives)

                assert sum(increment for increment in increments if increment > 0) == sum(
                    -increment for increment in increments if increment < 0
                )
                assert source >= ceil(jump / (length - 1))

                scale_gap = max(
                    0,
                    int(log2(jump)) - int(log2(source)),
                )
                assert scale_gap <= ceil(log2(length - 1))

                cycles += 1
                compensation_pairs += 1
                dyadic_checks += 1

    print(f"{cycles:,} exact closed floor cycles")
    print(f"{compensation_pairs:,} canonical source/restoration pairs")
    print(f"{dyadic_checks:,} dyadic scale-gap checks")


if __name__ == "__main__":
    main()
